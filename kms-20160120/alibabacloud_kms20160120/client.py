# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
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
        self._product_id = 'Kms'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
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
        """
        @summary Decrypts data by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        
        @param request: AsymmetricDecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricDecryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Decrypts data by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        
        @param request: AsymmetricDecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricDecryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Decrypts data by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        
        @param request: AsymmetricDecryptRequest
        @return: AsymmetricDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    async def asymmetric_decrypt_async(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        """
        @summary Decrypts data by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        
        @param request: AsymmetricDecryptRequest
        @return: AsymmetricDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_decrypt_with_options_async(request, runtime)

    def asymmetric_encrypt_with_options(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        """
        @summary Encrypts data by using an asymmetric customer master key (CMK).
        
        @description This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        
        @param request: AsymmetricEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricEncryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Encrypts data by using an asymmetric customer master key (CMK).
        
        @description This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        
        @param request: AsymmetricEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricEncryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Encrypts data by using an asymmetric customer master key (CMK).
        
        @description This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        
        @param request: AsymmetricEncryptRequest
        @return: AsymmetricEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    async def asymmetric_encrypt_async(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        """
        @summary Encrypts data by using an asymmetric customer master key (CMK).
        
        @description This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c***` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        
        @param request: AsymmetricEncryptRequest
        @return: AsymmetricEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_encrypt_with_options_async(request, runtime)

    def asymmetric_sign_with_options(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        """
        @summary AsymmetricSign
        
        @description Generates a signature by using an asymmetric key.
        
        @param request: AsymmetricSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary AsymmetricSign
        
        @description Generates a signature by using an asymmetric key.
        
        @param request: AsymmetricSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary AsymmetricSign
        
        @description Generates a signature by using an asymmetric key.
        
        @param request: AsymmetricSignRequest
        @return: AsymmetricSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    async def asymmetric_sign_async(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        """
        @summary AsymmetricSign
        
        @description Generates a signature by using an asymmetric key.
        
        @param request: AsymmetricSignRequest
        @return: AsymmetricSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_sign_with_options_async(request, runtime)

    def asymmetric_verify_with_options(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        """
        @summary Verifies a signature by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the *Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        
        @param request: AsymmetricVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Verifies a signature by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the *Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        
        @param request: AsymmetricVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AsymmetricVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Verifies a signature by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the *Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        
        @param request: AsymmetricVerifyRequest
        @return: AsymmetricVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    async def asymmetric_verify_async(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        """
        @summary Verifies a signature by using an asymmetric key.
        
        @description This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the *Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        
        @param request: AsymmetricVerifyRequest
        @return: AsymmetricVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.asymmetric_verify_with_options_async(request, runtime)

    def cancel_key_deletion_with_options(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        """
        @description If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        
        @param request: CancelKeyDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelKeyDeletionResponse
        """
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
        """
        @description If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        
        @param request: CancelKeyDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelKeyDeletionResponse
        """
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
        """
        @description If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        
        @param request: CancelKeyDeletionRequest
        @return: CancelKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    async def cancel_key_deletion_async(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        """
        @description If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        
        @param request: CancelKeyDeletionRequest
        @return: CancelKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_key_deletion_with_options_async(request, runtime)

    def certificate_private_key_decrypt_with_options(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        """
        @summary Decrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        
        @param request: CertificatePrivateKeyDecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePrivateKeyDecryptResponse
        """
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
        """
        @summary Decrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        
        @param request: CertificatePrivateKeyDecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePrivateKeyDecryptResponse
        """
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
        """
        @summary Decrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        
        @param request: CertificatePrivateKeyDecryptRequest
        @return: CertificatePrivateKeyDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_decrypt_with_options(request, runtime)

    async def certificate_private_key_decrypt_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        """
        @summary Decrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        
        @param request: CertificatePrivateKeyDecryptRequest
        @return: CertificatePrivateKeyDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.certificate_private_key_decrypt_with_options_async(request, runtime)

    def certificate_private_key_sign_with_options(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        """
        @summary Generates a signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePrivateKeySignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePrivateKeySignResponse
        """
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
        """
        @summary Generates a signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePrivateKeySignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePrivateKeySignResponse
        """
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
        """
        @summary Generates a signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePrivateKeySignRequest
        @return: CertificatePrivateKeySignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_sign_with_options(request, runtime)

    async def certificate_private_key_sign_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        """
        @summary Generates a signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePrivateKeySignRequest
        @return: CertificatePrivateKeySignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.certificate_private_key_sign_with_options_async(request, runtime)

    def certificate_public_key_encrypt_with_options(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        """
        @summary Encrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePublicKeyEncryptResponse
        """
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
        """
        @summary Encrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePublicKeyEncryptResponse
        """
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
        """
        @summary Encrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyEncryptRequest
        @return: CertificatePublicKeyEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_encrypt_with_options(request, runtime)

    async def certificate_public_key_encrypt_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        """
        @summary Encrypts data by using a specific certificate.
        
        @description Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyEncryptRequest
        @return: CertificatePublicKeyEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.certificate_public_key_encrypt_with_options_async(request, runtime)

    def certificate_public_key_verify_with_options(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        """
        @summary Verifies a digital signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePublicKeyVerifyResponse
        """
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
        """
        @summary Verifies a digital signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CertificatePublicKeyVerifyResponse
        """
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
        """
        @summary Verifies a digital signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyVerifyRequest
        @return: CertificatePublicKeyVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_verify_with_options(request, runtime)

    async def certificate_public_key_verify_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        """
        @summary Verifies a digital signature by using a specified certificate.
        
        @description The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678***` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        
        @param request: CertificatePublicKeyVerifyRequest
        @return: CertificatePublicKeyVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.certificate_public_key_verify_with_options_async(request, runtime)

    def connect_kms_instance_with_options(
        self,
        request: kms_20160120_models.ConnectKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ConnectKmsInstanceResponse:
        """
        @summary Enables a Key Management Service (KMS) instance.
        
        @description ### [](#)Limits
        You can enable only instances of the software key management type. You cannot enable instances of the hardware key management type.
        
        @param request: ConnectKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConnectKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kmprovider):
            query['KMProvider'] = request.kmprovider
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConnectKmsInstance',
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
            kms_20160120_models.ConnectKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def connect_kms_instance_with_options_async(
        self,
        request: kms_20160120_models.ConnectKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ConnectKmsInstanceResponse:
        """
        @summary Enables a Key Management Service (KMS) instance.
        
        @description ### [](#)Limits
        You can enable only instances of the software key management type. You cannot enable instances of the hardware key management type.
        
        @param request: ConnectKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConnectKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kmprovider):
            query['KMProvider'] = request.kmprovider
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConnectKmsInstance',
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
            kms_20160120_models.ConnectKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def connect_kms_instance(
        self,
        request: kms_20160120_models.ConnectKmsInstanceRequest,
    ) -> kms_20160120_models.ConnectKmsInstanceResponse:
        """
        @summary Enables a Key Management Service (KMS) instance.
        
        @description ### [](#)Limits
        You can enable only instances of the software key management type. You cannot enable instances of the hardware key management type.
        
        @param request: ConnectKmsInstanceRequest
        @return: ConnectKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.connect_kms_instance_with_options(request, runtime)

    async def connect_kms_instance_async(
        self,
        request: kms_20160120_models.ConnectKmsInstanceRequest,
    ) -> kms_20160120_models.ConnectKmsInstanceResponse:
        """
        @summary Enables a Key Management Service (KMS) instance.
        
        @description ### [](#)Limits
        You can enable only instances of the software key management type. You cannot enable instances of the hardware key management type.
        
        @param request: ConnectKmsInstanceRequest
        @return: ConnectKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.connect_kms_instance_with_options_async(request, runtime)

    def create_alias_with_options(
        self,
        request: kms_20160120_models.CreateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateAliasResponse:
        """
        @description    Each alias can be bound to only one CMK at a time.
        The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: CreateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
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
        """
        @description    Each alias can be bound to only one CMK at a time.
        The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: CreateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
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
        """
        @description    Each alias can be bound to only one CMK at a time.
        The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alias_with_options(request, runtime)

    async def create_alias_async(
        self,
        request: kms_20160120_models.CreateAliasRequest,
    ) -> kms_20160120_models.CreateAliasResponse:
        """
        @description    Each alias can be bound to only one CMK at a time.
        The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alias_with_options_async(request, runtime)

    def create_application_access_point_with_options(
        self,
        request: kms_20160120_models.CreateApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateApplicationAccessPointResponse:
        """
        @summary Creates an application access point (AAP)
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based AAP:
        1.Create a network access rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access KMS. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind network access rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. This topic describes how to create an AAP.
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_method):
            query['AuthenticationMethod'] = request.authentication_method
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policies):
            query['Policies'] = request.policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationAccessPoint',
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
            kms_20160120_models.CreateApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_access_point_with_options_async(
        self,
        request: kms_20160120_models.CreateApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateApplicationAccessPointResponse:
        """
        @summary Creates an application access point (AAP)
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based AAP:
        1.Create a network access rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access KMS. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind network access rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. This topic describes how to create an AAP.
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_method):
            query['AuthenticationMethod'] = request.authentication_method
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policies):
            query['Policies'] = request.policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationAccessPoint',
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
            kms_20160120_models.CreateApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_access_point(
        self,
        request: kms_20160120_models.CreateApplicationAccessPointRequest,
    ) -> kms_20160120_models.CreateApplicationAccessPointResponse:
        """
        @summary Creates an application access point (AAP)
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based AAP:
        1.Create a network access rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access KMS. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind network access rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. This topic describes how to create an AAP.
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateApplicationAccessPointRequest
        @return: CreateApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_access_point_with_options(request, runtime)

    async def create_application_access_point_async(
        self,
        request: kms_20160120_models.CreateApplicationAccessPointRequest,
    ) -> kms_20160120_models.CreateApplicationAccessPointResponse:
        """
        @summary Creates an application access point (AAP)
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based AAP:
        1.Create a network access rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access KMS. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind network access rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. This topic describes how to create an AAP.
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateApplicationAccessPointRequest
        @return: CreateApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_access_point_with_options_async(request, runtime)

    def create_certificate_with_options(
        self,
        tmp_req: kms_20160120_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateCertificateResponse:
        """
        @description To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](https://help.aliyun.com/document_detail/212136.html) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        
        @param tmp_req: CreateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateResponse
        """
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
        """
        @description To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](https://help.aliyun.com/document_detail/212136.html) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        
        @param tmp_req: CreateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateResponse
        """
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
        """
        @description To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](https://help.aliyun.com/document_detail/212136.html) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        
        @param request: CreateCertificateRequest
        @return: CreateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    async def create_certificate_async(
        self,
        request: kms_20160120_models.CreateCertificateRequest,
    ) -> kms_20160120_models.CreateCertificateResponse:
        """
        @description To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](https://help.aliyun.com/document_detail/212136.html) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        
        @param request: CreateCertificateRequest
        @return: CreateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_options_async(request, runtime)

    def create_client_key_with_options(
        self,
        request: kms_20160120_models.CreateClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateClientKeyResponse:
        """
        @summary Creates a client key.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP.
        ### Precautions
        A client key has a validity period. After a client key expires, applications into which the client key is integrated cannot access the required KMS instance. You must replace the client key before the client key expires. We recommend that you delete the expired client key in KMS after the new client key is used.
        
        @param request: CreateClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aap_name):
            query['AapName'] = request.aap_name
        if not UtilClient.is_unset(request.not_after):
            query['NotAfter'] = request.not_after
        if not UtilClient.is_unset(request.not_before):
            query['NotBefore'] = request.not_before
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientKey',
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
            kms_20160120_models.CreateClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_key_with_options_async(
        self,
        request: kms_20160120_models.CreateClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateClientKeyResponse:
        """
        @summary Creates a client key.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP.
        ### Precautions
        A client key has a validity period. After a client key expires, applications into which the client key is integrated cannot access the required KMS instance. You must replace the client key before the client key expires. We recommend that you delete the expired client key in KMS after the new client key is used.
        
        @param request: CreateClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aap_name):
            query['AapName'] = request.aap_name
        if not UtilClient.is_unset(request.not_after):
            query['NotAfter'] = request.not_after
        if not UtilClient.is_unset(request.not_before):
            query['NotBefore'] = request.not_before
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientKey',
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
            kms_20160120_models.CreateClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_key(
        self,
        request: kms_20160120_models.CreateClientKeyRequest,
    ) -> kms_20160120_models.CreateClientKeyResponse:
        """
        @summary Creates a client key.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP.
        ### Precautions
        A client key has a validity period. After a client key expires, applications into which the client key is integrated cannot access the required KMS instance. You must replace the client key before the client key expires. We recommend that you delete the expired client key in KMS after the new client key is used.
        
        @param request: CreateClientKeyRequest
        @return: CreateClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_client_key_with_options(request, runtime)

    async def create_client_key_async(
        self,
        request: kms_20160120_models.CreateClientKeyRequest,
    ) -> kms_20160120_models.CreateClientKeyResponse:
        """
        @summary Creates a client key.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP.
        ### Precautions
        A client key has a validity period. After a client key expires, applications into which the client key is integrated cannot access the required KMS instance. You must replace the client key before the client key expires. We recommend that you delete the expired client key in KMS after the new client key is used.
        
        @param request: CreateClientKeyRequest
        @return: CreateClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_client_key_with_options_async(request, runtime)

    def create_key_with_options(
        self,
        request: kms_20160120_models.CreateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyResponse:
        """
        @summary Creates a customer master key (CMK).
        
        @description KMS supports common symmetric keys and asymmetric keys. For more information, see [Key types and specifications](https://help.aliyun.com/document_detail/480161.html).
        
        @param request: CreateKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.key_storage_mechanism):
            query['KeyStorageMechanism'] = request.key_storage_mechanism
        if not UtilClient.is_unset(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        @summary Creates a customer master key (CMK).
        
        @description KMS supports common symmetric keys and asymmetric keys. For more information, see [Key types and specifications](https://help.aliyun.com/document_detail/480161.html).
        
        @param request: CreateKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.key_storage_mechanism):
            query['KeyStorageMechanism'] = request.key_storage_mechanism
        if not UtilClient.is_unset(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        @summary Creates a customer master key (CMK).
        
        @description KMS supports common symmetric keys and asymmetric keys. For more information, see [Key types and specifications](https://help.aliyun.com/document_detail/480161.html).
        
        @param request: CreateKeyRequest
        @return: CreateKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    async def create_key_async(
        self,
        request: kms_20160120_models.CreateKeyRequest,
    ) -> kms_20160120_models.CreateKeyResponse:
        """
        @summary Creates a customer master key (CMK).
        
        @description KMS supports common symmetric keys and asymmetric keys. For more information, see [Key types and specifications](https://help.aliyun.com/document_detail/480161.html).
        
        @param request: CreateKeyRequest
        @return: CreateKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_key_with_options_async(request, runtime)

    def create_key_version_with_options(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        """
        @summary 为密钥创建新的密钥版本。
        
        @description    You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation to create an asymmetric CMK and the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        If a CMK is in a private key store, you cannot create a version for the CMK.
        You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c***` by using the parameter settings provided in this topic.
        
        @param request: CreateKeyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyVersionResponse
        """
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
        """
        @summary 为密钥创建新的密钥版本。
        
        @description    You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation to create an asymmetric CMK and the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        If a CMK is in a private key store, you cannot create a version for the CMK.
        You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c***` by using the parameter settings provided in this topic.
        
        @param request: CreateKeyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyVersionResponse
        """
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
        """
        @summary 为密钥创建新的密钥版本。
        
        @description    You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation to create an asymmetric CMK and the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        If a CMK is in a private key store, you cannot create a version for the CMK.
        You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c***` by using the parameter settings provided in this topic.
        
        @param request: CreateKeyVersionRequest
        @return: CreateKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_version_with_options(request, runtime)

    async def create_key_version_async(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        """
        @summary 为密钥创建新的密钥版本。
        
        @description    You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation to create an asymmetric CMK and the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        If a CMK is in a private key store, you cannot create a version for the CMK.
        You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c***` by using the parameter settings provided in this topic.
        
        @param request: CreateKeyVersionRequest
        @return: CreateKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_key_version_with_options_async(request, runtime)

    def create_network_rule_with_options(
        self,
        request: kms_20160120_models.CreateNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateNetworkRuleResponse:
        """
        @summary Creates an access control rule to configure the private IP addresses or CIDR blocks that are allowed to access a Key Management Service (KMS) instance.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a KMS instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance.
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkRule',
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
            kms_20160120_models.CreateNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_rule_with_options_async(
        self,
        request: kms_20160120_models.CreateNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateNetworkRuleResponse:
        """
        @summary Creates an access control rule to configure the private IP addresses or CIDR blocks that are allowed to access a Key Management Service (KMS) instance.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a KMS instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance.
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkRule',
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
            kms_20160120_models.CreateNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_rule(
        self,
        request: kms_20160120_models.CreateNetworkRuleRequest,
    ) -> kms_20160120_models.CreateNetworkRuleResponse:
        """
        @summary Creates an access control rule to configure the private IP addresses or CIDR blocks that are allowed to access a Key Management Service (KMS) instance.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a KMS instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance.
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateNetworkRuleRequest
        @return: CreateNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_rule_with_options(request, runtime)

    async def create_network_rule_async(
        self,
        request: kms_20160120_models.CreateNetworkRuleRequest,
    ) -> kms_20160120_models.CreateNetworkRuleResponse:
        """
        @summary Creates an access control rule to configure the private IP addresses or CIDR blocks that are allowed to access a Key Management Service (KMS) instance.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a KMS instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance.
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets. For more information, see [CreatePolicy](https://help.aliyun.com/document_detail/2539454.html).
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreateNetworkRuleRequest
        @return: CreateNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_rule_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: kms_20160120_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreatePolicyResponse:
        """
        @summary Creates a permission policy to configure the keys and secrets that are allowed to access.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets.
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.kms_instance):
            query['KmsInstance'] = request.kms_instance
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
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
            kms_20160120_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: kms_20160120_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreatePolicyResponse:
        """
        @summary Creates a permission policy to configure the keys and secrets that are allowed to access.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets.
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.kms_instance):
            query['KmsInstance'] = request.kms_instance
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
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
            kms_20160120_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: kms_20160120_models.CreatePolicyRequest,
    ) -> kms_20160120_models.CreatePolicyResponse:
        """
        @summary Creates a permission policy to configure the keys and secrets that are allowed to access.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets.
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: kms_20160120_models.CreatePolicyRequest,
    ) -> kms_20160120_models.CreatePolicyResponse:
        """
        @summary Creates a permission policy to configure the keys and secrets that are allowed to access.
        
        @description To perform cryptographic operations and retrieve secret values, self-managed applications must use a client key to access a Key Management Service (KMS) instance. The following process shows how to create a client key-based application access point (AAP):
        1.Create an access control rule: You can configure the private IP addresses or private CIDR blocks that are allowed to access a KMS instance. For more information, see [CreateNetworkRule](https://help.aliyun.com/document_detail/2539407.html).
        2.Create a permission policy: You can configure the keys and secrets that are allowed to access and bind access control rules to the keys and secrets.
        3.Create an AAP: You can configure an authentication method and bind a permission policy to an AAP. For more information, see [CreateApplicationAccessPoint](https://help.aliyun.com/document_detail/2539467.html).
        4.Create a client key: You can configure the encryption password and validity period of a client key and bind the client key to an AAP. For more information, see [CreateClientKey](https://help.aliyun.com/document_detail/2539509.html).
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_secret_with_options(
        self,
        tmp_req: kms_20160120_models.CreateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateSecretResponse:
        """
        @summary 创建凭据并存入凭据的初始版本。
        
        @description The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        
        @param tmp_req: CreateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        """
        @summary 创建凭据并存入凭据的初始版本。
        
        @description The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        
        @param tmp_req: CreateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
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
        """
        @summary 创建凭据并存入凭据的初始版本。
        
        @description The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        
        @param request: CreateSecretRequest
        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    async def create_secret_async(
        self,
        request: kms_20160120_models.CreateSecretRequest,
    ) -> kms_20160120_models.CreateSecretResponse:
        """
        @summary 创建凭据并存入凭据的初始版本。
        
        @description The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        
        @param request: CreateSecretRequest
        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        tmp_req: kms_20160120_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DecryptResponse:
        """
        @summary 调用Decrypt接口解密CiphertextBlob中的密文。
        
        @param tmp_req: DecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.DecryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 调用Decrypt接口解密CiphertextBlob中的密文。
        
        @param tmp_req: DecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.DecryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 调用Decrypt接口解密CiphertextBlob中的密文。
        
        @param request: DecryptRequest
        @return: DecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: kms_20160120_models.DecryptRequest,
    ) -> kms_20160120_models.DecryptResponse:
        """
        @summary 调用Decrypt接口解密CiphertextBlob中的密文。
        
        @param request: DecryptRequest
        @return: DecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_alias_with_options(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteAliasResponse:
        """
        @param request: DeleteAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
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
        """
        @param request: DeleteAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
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
        """
        @param request: DeleteAliasRequest
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_alias_with_options(request, runtime)

    async def delete_alias_async(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
    ) -> kms_20160120_models.DeleteAliasResponse:
        """
        @param request: DeleteAliasRequest
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_alias_with_options_async(request, runtime)

    def delete_application_access_point_with_options(
        self,
        request: kms_20160120_models.DeleteApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteApplicationAccessPointResponse:
        """
        @summary Deletes an application access point (AAP).
        
        @description Before you delete an AAP, make sure that the AAP is no longer in use. If you delete an AAP that is in use, applications that use the AAP cannot access Key Management Service (KMS). Exercise caution when you delete an AAP.
        
        @param request: DeleteApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationAccessPoint',
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
            kms_20160120_models.DeleteApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_access_point_with_options_async(
        self,
        request: kms_20160120_models.DeleteApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteApplicationAccessPointResponse:
        """
        @summary Deletes an application access point (AAP).
        
        @description Before you delete an AAP, make sure that the AAP is no longer in use. If you delete an AAP that is in use, applications that use the AAP cannot access Key Management Service (KMS). Exercise caution when you delete an AAP.
        
        @param request: DeleteApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationAccessPoint',
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
            kms_20160120_models.DeleteApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_access_point(
        self,
        request: kms_20160120_models.DeleteApplicationAccessPointRequest,
    ) -> kms_20160120_models.DeleteApplicationAccessPointResponse:
        """
        @summary Deletes an application access point (AAP).
        
        @description Before you delete an AAP, make sure that the AAP is no longer in use. If you delete an AAP that is in use, applications that use the AAP cannot access Key Management Service (KMS). Exercise caution when you delete an AAP.
        
        @param request: DeleteApplicationAccessPointRequest
        @return: DeleteApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_access_point_with_options(request, runtime)

    async def delete_application_access_point_async(
        self,
        request: kms_20160120_models.DeleteApplicationAccessPointRequest,
    ) -> kms_20160120_models.DeleteApplicationAccessPointResponse:
        """
        @summary Deletes an application access point (AAP).
        
        @description Before you delete an AAP, make sure that the AAP is no longer in use. If you delete an AAP that is in use, applications that use the AAP cannot access Key Management Service (KMS). Exercise caution when you delete an AAP.
        
        @param request: DeleteApplicationAccessPointRequest
        @return: DeleteApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_access_point_with_options_async(request, runtime)

    def delete_certificate_with_options(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        """
        @description After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` and its private key and certificate chain are deleted.
        
        @param request: DeleteCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCertificateResponse
        """
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
        """
        @description After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` and its private key and certificate chain are deleted.
        
        @param request: DeleteCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCertificateResponse
        """
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
        """
        @description After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` and its private key and certificate chain are deleted.
        
        @param request: DeleteCertificateRequest
        @return: DeleteCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    async def delete_certificate_async(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        """
        @description After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` and its private key and certificate chain are deleted.
        
        @param request: DeleteCertificateRequest
        @return: DeleteCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_certificate_with_options_async(request, runtime)

    def delete_client_key_with_options(
        self,
        request: kms_20160120_models.DeleteClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteClientKeyResponse:
        """
        @description Before you delete a client key, make sure that the client key is no longer in use. If you delete a client key that is in use, applications that use the client key cannot access Key Management Service (KMS). Exercise caution when you delete a client key.
        
        @param request: DeleteClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_key_id):
            query['ClientKeyId'] = request.client_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientKey',
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
            kms_20160120_models.DeleteClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_key_with_options_async(
        self,
        request: kms_20160120_models.DeleteClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteClientKeyResponse:
        """
        @description Before you delete a client key, make sure that the client key is no longer in use. If you delete a client key that is in use, applications that use the client key cannot access Key Management Service (KMS). Exercise caution when you delete a client key.
        
        @param request: DeleteClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_key_id):
            query['ClientKeyId'] = request.client_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientKey',
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
            kms_20160120_models.DeleteClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_key(
        self,
        request: kms_20160120_models.DeleteClientKeyRequest,
    ) -> kms_20160120_models.DeleteClientKeyResponse:
        """
        @description Before you delete a client key, make sure that the client key is no longer in use. If you delete a client key that is in use, applications that use the client key cannot access Key Management Service (KMS). Exercise caution when you delete a client key.
        
        @param request: DeleteClientKeyRequest
        @return: DeleteClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_client_key_with_options(request, runtime)

    async def delete_client_key_async(
        self,
        request: kms_20160120_models.DeleteClientKeyRequest,
    ) -> kms_20160120_models.DeleteClientKeyResponse:
        """
        @description Before you delete a client key, make sure that the client key is no longer in use. If you delete a client key that is in use, applications that use the client key cannot access Key Management Service (KMS). Exercise caution when you delete a client key.
        
        @param request: DeleteClientKeyRequest
        @return: DeleteClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_key_with_options_async(request, runtime)

    def delete_key_material_with_options(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        """
        @description This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        
        @param request: DeleteKeyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyMaterialResponse
        """
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
        """
        @description This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        
        @param request: DeleteKeyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyMaterialResponse
        """
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
        """
        @description This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        
        @param request: DeleteKeyMaterialRequest
        @return: DeleteKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    async def delete_key_material_async(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        """
        @description This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        
        @param request: DeleteKeyMaterialRequest
        @return: DeleteKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_material_with_options_async(request, runtime)

    def delete_network_rule_with_options(
        self,
        request: kms_20160120_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a network access rule.
        
        @description Before you delete a network access rule, make sure that the network access rule is not bound to permission policies. Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeleteNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
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
            kms_20160120_models.DeleteNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_rule_with_options_async(
        self,
        request: kms_20160120_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a network access rule.
        
        @description Before you delete a network access rule, make sure that the network access rule is not bound to permission policies. Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeleteNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
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
            kms_20160120_models.DeleteNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_rule(
        self,
        request: kms_20160120_models.DeleteNetworkRuleRequest,
    ) -> kms_20160120_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a network access rule.
        
        @description Before you delete a network access rule, make sure that the network access rule is not bound to permission policies. Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeleteNetworkRuleRequest
        @return: DeleteNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    async def delete_network_rule_async(
        self,
        request: kms_20160120_models.DeleteNetworkRuleRequest,
    ) -> kms_20160120_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a network access rule.
        
        @description Before you delete a network access rule, make sure that the network access rule is not bound to permission policies. Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeleteNetworkRuleRequest
        @return: DeleteNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_rule_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: kms_20160120_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeletePolicyResponse:
        """
        @summary Deletes a permission policy.
        
        @description Before you delete a permission policy, make sure that the permission policy is not associated with application access points (AAPs). Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
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
            kms_20160120_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: kms_20160120_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeletePolicyResponse:
        """
        @summary Deletes a permission policy.
        
        @description Before you delete a permission policy, make sure that the permission policy is not associated with application access points (AAPs). Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
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
            kms_20160120_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: kms_20160120_models.DeletePolicyRequest,
    ) -> kms_20160120_models.DeletePolicyResponse:
        """
        @summary Deletes a permission policy.
        
        @description Before you delete a permission policy, make sure that the permission policy is not associated with application access points (AAPs). Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: kms_20160120_models.DeletePolicyRequest,
    ) -> kms_20160120_models.DeletePolicyResponse:
        """
        @summary Deletes a permission policy.
        
        @description Before you delete a permission policy, make sure that the permission policy is not associated with application access points (AAPs). Otherwise, related applications cannot access Key Management Service (KMS).
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_secret_with_options(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteSecretResponse:
        """
        @description If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        
        @param request: DeleteSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretResponse
        """
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
        """
        @description If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        
        @param request: DeleteSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretResponse
        """
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
        """
        @description If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        
        @param request: DeleteSecretRequest
        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    async def delete_secret_async(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
    ) -> kms_20160120_models.DeleteSecretResponse:
        """
        @description If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        
        @param request: DeleteSecretRequest
        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_with_options_async(request, runtime)

    def describe_account_kms_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        """
        @param request: DescribeAccountKmsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountKmsStatusResponse
        """
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
        """
        @param request: DescribeAccountKmsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountKmsStatusResponse
        """
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
        """
        @return: DescribeAccountKmsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_kms_status_with_options(runtime)

    async def describe_account_kms_status_async(self) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        """
        @return: DescribeAccountKmsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_kms_status_with_options_async(runtime)

    def describe_application_access_point_with_options(
        self,
        request: kms_20160120_models.DescribeApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeApplicationAccessPointResponse:
        """
        @summary Queries the details of an application access point (AAP).
        
        @param request: DescribeApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationAccessPoint',
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
            kms_20160120_models.DescribeApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_access_point_with_options_async(
        self,
        request: kms_20160120_models.DescribeApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeApplicationAccessPointResponse:
        """
        @summary Queries the details of an application access point (AAP).
        
        @param request: DescribeApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationAccessPoint',
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
            kms_20160120_models.DescribeApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_access_point(
        self,
        request: kms_20160120_models.DescribeApplicationAccessPointRequest,
    ) -> kms_20160120_models.DescribeApplicationAccessPointResponse:
        """
        @summary Queries the details of an application access point (AAP).
        
        @param request: DescribeApplicationAccessPointRequest
        @return: DescribeApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_application_access_point_with_options(request, runtime)

    async def describe_application_access_point_async(
        self,
        request: kms_20160120_models.DescribeApplicationAccessPointRequest,
    ) -> kms_20160120_models.DescribeApplicationAccessPointResponse:
        """
        @summary Queries the details of an application access point (AAP).
        
        @param request: DescribeApplicationAccessPointRequest
        @return: DescribeApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_application_access_point_with_options_async(request, runtime)

    def describe_certificate_with_options(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        """
        @description In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        
        @param request: DescribeCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateResponse
        """
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
        """
        @description In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        
        @param request: DescribeCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateResponse
        """
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
        """
        @description In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        
        @param request: DescribeCertificateRequest
        @return: DescribeCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_with_options(request, runtime)

    async def describe_certificate_async(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        """
        @description In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        
        @param request: DescribeCertificateRequest
        @return: DescribeCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_with_options_async(request, runtime)

    def describe_key_with_options(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyResponse:
        """
        @summary Queries the information about a customer master key (CMK).
        
        @description You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        
        @param request: DescribeKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyResponse
        """
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
        """
        @summary Queries the information about a customer master key (CMK).
        
        @description You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        
        @param request: DescribeKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyResponse
        """
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
        """
        @summary Queries the information about a customer master key (CMK).
        
        @description You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        
        @param request: DescribeKeyRequest
        @return: DescribeKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    async def describe_key_async(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
    ) -> kms_20160120_models.DescribeKeyResponse:
        """
        @summary Queries the information about a customer master key (CMK).
        
        @description You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        
        @param request: DescribeKeyRequest
        @return: DescribeKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_with_options_async(request, runtime)

    def describe_key_version_with_options(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        """
        @description This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        
        @param request: DescribeKeyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyVersionResponse
        """
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
        """
        @description This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        
        @param request: DescribeKeyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyVersionResponse
        """
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
        """
        @description This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        
        @param request: DescribeKeyVersionRequest
        @return: DescribeKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_key_version_with_options(request, runtime)

    async def describe_key_version_async(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        """
        @description This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        
        @param request: DescribeKeyVersionRequest
        @return: DescribeKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_version_with_options_async(request, runtime)

    def describe_network_rule_with_options(
        self,
        request: kms_20160120_models.DescribeNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeNetworkRuleResponse:
        """
        @summary Queries the details of an access control rule.
        
        @param request: DescribeNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRule',
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
            kms_20160120_models.DescribeNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rule_with_options_async(
        self,
        request: kms_20160120_models.DescribeNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeNetworkRuleResponse:
        """
        @summary Queries the details of an access control rule.
        
        @param request: DescribeNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRule',
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
            kms_20160120_models.DescribeNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_rule(
        self,
        request: kms_20160120_models.DescribeNetworkRuleRequest,
    ) -> kms_20160120_models.DescribeNetworkRuleResponse:
        """
        @summary Queries the details of an access control rule.
        
        @param request: DescribeNetworkRuleRequest
        @return: DescribeNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rule_with_options(request, runtime)

    async def describe_network_rule_async(
        self,
        request: kms_20160120_models.DescribeNetworkRuleRequest,
    ) -> kms_20160120_models.DescribeNetworkRuleResponse:
        """
        @summary Queries the details of an access control rule.
        
        @param request: DescribeNetworkRuleRequest
        @return: DescribeNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_rule_with_options_async(request, runtime)

    def describe_policy_with_options(
        self,
        request: kms_20160120_models.DescribePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribePolicyResponse:
        """
        @summary Queries the details of a permission policy.
        
        @param request: DescribePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicy',
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
            kms_20160120_models.DescribePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_with_options_async(
        self,
        request: kms_20160120_models.DescribePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribePolicyResponse:
        """
        @summary Queries the details of a permission policy.
        
        @param request: DescribePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicy',
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
            kms_20160120_models.DescribePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy(
        self,
        request: kms_20160120_models.DescribePolicyRequest,
    ) -> kms_20160120_models.DescribePolicyResponse:
        """
        @summary Queries the details of a permission policy.
        
        @param request: DescribePolicyRequest
        @return: DescribePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_with_options(request, runtime)

    async def describe_policy_async(
        self,
        request: kms_20160120_models.DescribePolicyRequest,
    ) -> kms_20160120_models.DescribePolicyResponse:
        """
        @summary Queries the details of a permission policy.
        
        @param request: DescribePolicyRequest
        @return: DescribePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Kms\\&api=DescribeRegions\\&type=RPC\\&version=2016-01-20)
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries available regions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Kms\\&api=DescribeRegions\\&type=RPC\\&version=2016-01-20)
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries available regions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Kms\\&api=DescribeRegions\\&type=RPC\\&version=2016-01-20)
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> kms_20160120_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Kms\\&api=DescribeRegions\\&type=RPC\\&version=2016-01-20)
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_secret_with_options(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeSecretResponse:
        """
        @description This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        
        @param request: DescribeSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecretResponse
        """
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
        """
        @description This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        
        @param request: DescribeSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecretResponse
        """
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
        """
        @description This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        
        @param request: DescribeSecretRequest
        @return: DescribeSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    async def describe_secret_async(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
    ) -> kms_20160120_models.DescribeSecretResponse:
        """
        @description This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        
        @param request: DescribeSecretRequest
        @return: DescribeSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_secret_with_options_async(request, runtime)

    def disable_key_with_options(
        self,
        request: kms_20160120_models.DisableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        """
        @description If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](https://help.aliyun.com/document_detail/35150.html) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***` is disabled.
        
        @param request: DisableKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableKeyResponse
        """
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
        """
        @description If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](https://help.aliyun.com/document_detail/35150.html) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***` is disabled.
        
        @param request: DisableKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableKeyResponse
        """
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
        """
        @description If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](https://help.aliyun.com/document_detail/35150.html) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***` is disabled.
        
        @param request: DisableKeyRequest
        @return: DisableKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_key_with_options(request, runtime)

    async def disable_key_async(
        self,
        request: kms_20160120_models.DisableKeyRequest,
    ) -> kms_20160120_models.DisableKeyResponse:
        """
        @description If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](https://help.aliyun.com/document_detail/35150.html) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***` is disabled.
        
        @param request: DisableKeyRequest
        @return: DisableKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_key_with_options_async(request, runtime)

    def enable_key_with_options(
        self,
        request: kms_20160120_models.EnableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EnableKeyResponse:
        """
        @param request: EnableKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableKeyResponse
        """
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
        """
        @param request: EnableKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableKeyResponse
        """
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
        """
        @param request: EnableKeyRequest
        @return: EnableKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_key_with_options(request, runtime)

    async def enable_key_async(
        self,
        request: kms_20160120_models.EnableKeyRequest,
    ) -> kms_20160120_models.EnableKeyResponse:
        """
        @param request: EnableKeyRequest
        @return: EnableKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_key_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        tmp_req: kms_20160120_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EncryptResponse:
        """
        @description    KMS uses the primary version of a specified CMK to encrypt data.
        Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the data key.
        
        @param tmp_req: EncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.EncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description    KMS uses the primary version of a specified CMK to encrypt data.
        Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the data key.
        
        @param tmp_req: EncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.EncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description    KMS uses the primary version of a specified CMK to encrypt data.
        Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the data key.
        
        @param request: EncryptRequest
        @return: EncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: kms_20160120_models.EncryptRequest,
    ) -> kms_20160120_models.EncryptResponse:
        """
        @description    KMS uses the primary version of a specified CMK to encrypt data.
        Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the data key.
        
        @param request: EncryptRequest
        @return: EncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def export_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.ExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        """
        @description You can call the [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        
        @param tmp_req: ExportDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description You can call the [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        
        @param tmp_req: ExportDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description You can call the [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        
        @param request: ExportDataKeyRequest
        @return: ExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_data_key_with_options(request, runtime)

    async def export_data_key_async(
        self,
        request: kms_20160120_models.ExportDataKeyRequest,
    ) -> kms_20160120_models.ExportDataKeyResponse:
        """
        @description You can call the [GenerateDataKeyWithoutPlaintext](https://help.aliyun.com/document_detail/134043.html) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        
        @param request: ExportDataKeyRequest
        @return: ExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_data_key_with_options_async(request, runtime)

    def generate_and_export_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateAndExportDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        """
        @description We recommend that you perform the following steps to import your data key to a cryptographic module:
        Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        
        @param tmp_req: GenerateAndExportDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAndExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateAndExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description We recommend that you perform the following steps to import your data key to a cryptographic module:
        Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        
        @param tmp_req: GenerateAndExportDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAndExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateAndExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description We recommend that you perform the following steps to import your data key to a cryptographic module:
        Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        
        @param request: GenerateAndExportDataKeyRequest
        @return: GenerateAndExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_and_export_data_key_with_options(request, runtime)

    async def generate_and_export_data_key_async(
        self,
        request: kms_20160120_models.GenerateAndExportDataKeyRequest,
    ) -> kms_20160120_models.GenerateAndExportDataKeyResponse:
        """
        @description We recommend that you perform the following steps to import your data key to a cryptographic module:
        Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        
        @param request: GenerateAndExportDataKeyRequest
        @return: GenerateAndExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_and_export_data_key_with_options_async(request, runtime)

    def generate_data_key_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        """
        @summary 生成一个数据密钥
        
        @description This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        Call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param tmp_req: GenerateDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 生成一个数据密钥
        
        @description This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        Call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param tmp_req: GenerateDataKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 生成一个数据密钥
        
        @description This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        Call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: GenerateDataKeyRequest
        @return: GenerateDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    async def generate_data_key_async(
        self,
        request: kms_20160120_models.GenerateDataKeyRequest,
    ) -> kms_20160120_models.GenerateDataKeyResponse:
        """
        @summary 生成一个数据密钥
        
        @description This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        Call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc***`.
        
        @param request: GenerateDataKeyRequest
        @return: GenerateDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_data_key_with_options_async(request, runtime)

    def generate_data_key_without_plaintext_with_options(
        self,
        tmp_req: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        """
        @summary Generates a random data key, which can be used to encrypt local data.
        
        @description This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        >  This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the ciphertext of the data key.
        >  This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        
        @param tmp_req: GenerateDataKeyWithoutPlaintextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Generates a random data key, which can be used to encrypt local data.
        
        @description This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        >  This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the ciphertext of the data key.
        >  This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        
        @param tmp_req: GenerateDataKeyWithoutPlaintextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary Generates a random data key, which can be used to encrypt local data.
        
        @description This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        >  This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the ciphertext of the data key.
        >  This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        
        @param request: GenerateDataKeyWithoutPlaintextRequest
        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    async def generate_data_key_without_plaintext_async(
        self,
        request: kms_20160120_models.GenerateDataKeyWithoutPlaintextRequest,
    ) -> kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse:
        """
        @summary Generates a random data key, which can be used to encrypt local data.
        
        @description This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](https://help.aliyun.com/document_detail/28948.html) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        >  This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](https://help.aliyun.com/document_detail/28950.html) operation to decrypt the ciphertext of the data key.
        >  This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        
        @param request: GenerateDataKeyWithoutPlaintextRequest
        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_data_key_without_plaintext_with_options_async(request, runtime)

    def get_certificate_with_options(
        self,
        request: kms_20160120_models.GetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetCertificateResponse:
        """
        @description In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        
        @param request: GetCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCertificateResponse
        """
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
        """
        @description In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        
        @param request: GetCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCertificateResponse
        """
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
        """
        @description In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        
        @param request: GetCertificateRequest
        @return: GetCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    async def get_certificate_async(
        self,
        request: kms_20160120_models.GetCertificateRequest,
    ) -> kms_20160120_models.GetCertificateResponse:
        """
        @description In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        
        @param request: GetCertificateRequest
        @return: GetCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_certificate_with_options_async(request, runtime)

    def get_client_key_with_options(
        self,
        request: kms_20160120_models.GetClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetClientKeyResponse:
        """
        @summary Queries the information about a client key.
        
        @param request: GetClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetClientKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_key_with_options_async(
        self,
        request: kms_20160120_models.GetClientKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetClientKeyResponse:
        """
        @summary Queries the information about a client key.
        
        @param request: GetClientKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientKeyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetClientKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_key(
        self,
        request: kms_20160120_models.GetClientKeyRequest,
    ) -> kms_20160120_models.GetClientKeyResponse:
        """
        @summary Queries the information about a client key.
        
        @param request: GetClientKeyRequest
        @return: GetClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_client_key_with_options(request, runtime)

    async def get_client_key_async(
        self,
        request: kms_20160120_models.GetClientKeyRequest,
    ) -> kms_20160120_models.GetClientKeyResponse:
        """
        @summary Queries the information about a client key.
        
        @param request: GetClientKeyRequest
        @return: GetClientKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_client_key_with_options_async(request, runtime)

    def get_default_kms_instance_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetDefaultKmsInstanceResponse:
        """
        @summary 获取默认KMS实例
        
        @param request: GetDefaultKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultKmsInstanceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultKmsInstance',
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
            kms_20160120_models.GetDefaultKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_kms_instance_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetDefaultKmsInstanceResponse:
        """
        @summary 获取默认KMS实例
        
        @param request: GetDefaultKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultKmsInstanceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultKmsInstance',
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
            kms_20160120_models.GetDefaultKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_kms_instance(self) -> kms_20160120_models.GetDefaultKmsInstanceResponse:
        """
        @summary 获取默认KMS实例
        
        @return: GetDefaultKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_default_kms_instance_with_options(runtime)

    async def get_default_kms_instance_async(self) -> kms_20160120_models.GetDefaultKmsInstanceResponse:
        """
        @summary 获取默认KMS实例
        
        @return: GetDefaultKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_default_kms_instance_with_options_async(runtime)

    def get_key_policy_with_options(
        self,
        request: kms_20160120_models.GetKeyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetKeyPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Key Policy，否则提示 Not Found。
        
        @param request: GetKeyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKeyPolicy',
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
            kms_20160120_models.GetKeyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_key_policy_with_options_async(
        self,
        request: kms_20160120_models.GetKeyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetKeyPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Key Policy，否则提示 Not Found。
        
        @param request: GetKeyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKeyPolicy',
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
            kms_20160120_models.GetKeyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_key_policy(
        self,
        request: kms_20160120_models.GetKeyPolicyRequest,
    ) -> kms_20160120_models.GetKeyPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Key Policy，否则提示 Not Found。
        
        @param request: GetKeyPolicyRequest
        @return: GetKeyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_key_policy_with_options(request, runtime)

    async def get_key_policy_async(
        self,
        request: kms_20160120_models.GetKeyPolicyRequest,
    ) -> kms_20160120_models.GetKeyPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Key Policy，否则提示 Not Found。
        
        @param request: GetKeyPolicyRequest
        @return: GetKeyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_key_policy_with_options_async(request, runtime)

    def get_kms_instance_with_options(
        self,
        request: kms_20160120_models.GetKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetKmsInstanceResponse:
        """
        @summary Queries the details of a Key Management Service (KMS) instance.
        
        @param request: GetKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKmsInstance',
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
            kms_20160120_models.GetKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kms_instance_with_options_async(
        self,
        request: kms_20160120_models.GetKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetKmsInstanceResponse:
        """
        @summary Queries the details of a Key Management Service (KMS) instance.
        
        @param request: GetKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKmsInstance',
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
            kms_20160120_models.GetKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kms_instance(
        self,
        request: kms_20160120_models.GetKmsInstanceRequest,
    ) -> kms_20160120_models.GetKmsInstanceResponse:
        """
        @summary Queries the details of a Key Management Service (KMS) instance.
        
        @param request: GetKmsInstanceRequest
        @return: GetKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_kms_instance_with_options(request, runtime)

    async def get_kms_instance_async(
        self,
        request: kms_20160120_models.GetKmsInstanceRequest,
    ) -> kms_20160120_models.GetKmsInstanceResponse:
        """
        @summary Queries the details of a Key Management Service (KMS) instance.
        
        @param request: GetKmsInstanceRequest
        @return: GetKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_kms_instance_with_options_async(request, runtime)

    def get_parameters_for_import_with_options(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        """
        @summary Queries the parameters that are used to import key material for a customer master key (CMK).
        
        @description The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678***`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        
        @param request: GetParametersForImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersForImportResponse
        """
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
        """
        @summary Queries the parameters that are used to import key material for a customer master key (CMK).
        
        @description The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678***`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        
        @param request: GetParametersForImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParametersForImportResponse
        """
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
        """
        @summary Queries the parameters that are used to import key material for a customer master key (CMK).
        
        @description The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678***`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        
        @param request: GetParametersForImportRequest
        @return: GetParametersForImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_for_import_with_options(request, runtime)

    async def get_parameters_for_import_async(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        """
        @summary Queries the parameters that are used to import key material for a customer master key (CMK).
        
        @description The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678***`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        
        @param request: GetParametersForImportRequest
        @return: GetParametersForImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_for_import_with_options_async(request, runtime)

    def get_public_key_with_options(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        """
        @param request: GetPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @param request: GetPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @param request: GetPublicKeyRequest
        @return: GetPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    async def get_public_key_async(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        """
        @param request: GetPublicKeyRequest
        @return: GetPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_key_with_options_async(request, runtime)

    def get_random_password_with_options(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        """
        @param request: GetRandomPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRandomPasswordResponse
        """
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
        """
        @param request: GetRandomPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRandomPasswordResponse
        """
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
        """
        @param request: GetRandomPasswordRequest
        @return: GetRandomPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_random_password_with_options(request, runtime)

    async def get_random_password_async(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        """
        @param request: GetRandomPasswordRequest
        @return: GetRandomPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_random_password_with_options_async(request, runtime)

    def get_secret_policy_with_options(
        self,
        request: kms_20160120_models.GetSecretPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Secret Policy，否则提示 Not Found。
        
        @param request: GetSecretPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretPolicy',
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
            kms_20160120_models.GetSecretPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_policy_with_options_async(
        self,
        request: kms_20160120_models.GetSecretPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Secret Policy，否则提示 Not Found。
        
        @param request: GetSecretPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretPolicy',
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
            kms_20160120_models.GetSecretPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_policy(
        self,
        request: kms_20160120_models.GetSecretPolicyRequest,
    ) -> kms_20160120_models.GetSecretPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Secret Policy，否则提示 Not Found。
        
        @param request: GetSecretPolicyRequest
        @return: GetSecretPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_policy_with_options(request, runtime)

    async def get_secret_policy_async(
        self,
        request: kms_20160120_models.GetSecretPolicyRequest,
    ) -> kms_20160120_models.GetSecretPolicyResponse:
        """
        @summary 仅可查询名称为 default 的 Secret Policy，否则提示 Not Found。
        
        @param request: GetSecretPolicyRequest
        @return: GetSecretPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_policy_with_options_async(request, runtime)

    def get_secret_value_with_options(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretValueResponse:
        """
        @summary 调用GetSecretValue接口获取凭据值。
        
        @description If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        
        @param request: GetSecretValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 调用GetSecretValue接口获取凭据值。
        
        @description If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        
        @param request: GetSecretValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @summary 调用GetSecretValue接口获取凭据值。
        
        @description If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        
        @param request: GetSecretValueRequest
        @return: GetSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    async def get_secret_value_async(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
    ) -> kms_20160120_models.GetSecretValueResponse:
        """
        @summary 调用GetSecretValue接口获取凭据值。
        
        @description If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        
        @param request: GetSecretValueRequest
        @return: GetSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_value_with_options_async(request, runtime)

    def import_key_material_with_options(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        """
        @summary Call the ImportKeyMaterial operation to import the key material.
        
        @description Call [CreateKey](https://help.aliyun.com/document_detail/28947.html) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        To view the CMK **Origin**, see [DescribeKey](https://help.aliyun.com/document_detail/28952.html).
        Before importing key material, you need to call the [GetParametersForImport](https://help.aliyun.com/document_detail/68621.html) obtain the parameters required to import the key material, including the public key and import token.
        >    The key type of the pair is **Aliyun_AES_256** the key material must be 256 bits. The key type must be **Aliyun_SM4** the CMK and key material must be 128 bits.
        >    You can set the expiration time for the key material, or you can set it to never expire.
        >    You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        >    After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        >    A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        
        @param request: ImportKeyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyMaterialResponse
        """
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
        """
        @summary Call the ImportKeyMaterial operation to import the key material.
        
        @description Call [CreateKey](https://help.aliyun.com/document_detail/28947.html) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        To view the CMK **Origin**, see [DescribeKey](https://help.aliyun.com/document_detail/28952.html).
        Before importing key material, you need to call the [GetParametersForImport](https://help.aliyun.com/document_detail/68621.html) obtain the parameters required to import the key material, including the public key and import token.
        >    The key type of the pair is **Aliyun_AES_256** the key material must be 256 bits. The key type must be **Aliyun_SM4** the CMK and key material must be 128 bits.
        >    You can set the expiration time for the key material, or you can set it to never expire.
        >    You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        >    After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        >    A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        
        @param request: ImportKeyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyMaterialResponse
        """
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
        """
        @summary Call the ImportKeyMaterial operation to import the key material.
        
        @description Call [CreateKey](https://help.aliyun.com/document_detail/28947.html) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        To view the CMK **Origin**, see [DescribeKey](https://help.aliyun.com/document_detail/28952.html).
        Before importing key material, you need to call the [GetParametersForImport](https://help.aliyun.com/document_detail/68621.html) obtain the parameters required to import the key material, including the public key and import token.
        >    The key type of the pair is **Aliyun_AES_256** the key material must be 256 bits. The key type must be **Aliyun_SM4** the CMK and key material must be 128 bits.
        >    You can set the expiration time for the key material, or you can set it to never expire.
        >    You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        >    After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        >    A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        
        @param request: ImportKeyMaterialRequest
        @return: ImportKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_material_with_options(request, runtime)

    async def import_key_material_async(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        """
        @summary Call the ImportKeyMaterial operation to import the key material.
        
        @description Call [CreateKey](https://help.aliyun.com/document_detail/28947.html) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        To view the CMK **Origin**, see [DescribeKey](https://help.aliyun.com/document_detail/28952.html).
        Before importing key material, you need to call the [GetParametersForImport](https://help.aliyun.com/document_detail/68621.html) obtain the parameters required to import the key material, including the public key and import token.
        >    The key type of the pair is **Aliyun_AES_256** the key material must be 256 bits. The key type must be **Aliyun_SM4** the CMK and key material must be 128 bits.
        >    You can set the expiration time for the key material, or you can set it to never expire.
        >    You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        >    After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        >    A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        
        @param request: ImportKeyMaterialRequest
        @return: ImportKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_key_material_with_options_async(request, runtime)

    def list_aliases_with_options(
        self,
        request: kms_20160120_models.ListAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesResponse:
        """
        @summary Queries all aliases in the current region for the current account.
        
        @param request: ListAliasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
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
        """
        @summary Queries all aliases in the current region for the current account.
        
        @param request: ListAliasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
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
        """
        @summary Queries all aliases in the current region for the current account.
        
        @param request: ListAliasesRequest
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_with_options(request, runtime)

    async def list_aliases_async(
        self,
        request: kms_20160120_models.ListAliasesRequest,
    ) -> kms_20160120_models.ListAliasesResponse:
        """
        @summary Queries all aliases in the current region for the current account.
        
        @param request: ListAliasesRequest
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aliases_with_options_async(request, runtime)

    def list_aliases_by_key_id_with_options(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        """
        @param request: ListAliasesByKeyIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesByKeyIdResponse
        """
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
        """
        @param request: ListAliasesByKeyIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesByKeyIdResponse
        """
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
        """
        @param request: ListAliasesByKeyIdRequest
        @return: ListAliasesByKeyIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_by_key_id_with_options(request, runtime)

    async def list_aliases_by_key_id_async(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        """
        @param request: ListAliasesByKeyIdRequest
        @return: ListAliasesByKeyIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aliases_by_key_id_with_options_async(request, runtime)

    def list_application_access_points_with_options(
        self,
        request: kms_20160120_models.ListApplicationAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListApplicationAccessPointsResponse:
        """
        @summary Queries a list of application access points (AAPs).
        
        @param request: ListApplicationAccessPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccessPointsResponse
        """
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
            action='ListApplicationAccessPoints',
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
            kms_20160120_models.ListApplicationAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_access_points_with_options_async(
        self,
        request: kms_20160120_models.ListApplicationAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListApplicationAccessPointsResponse:
        """
        @summary Queries a list of application access points (AAPs).
        
        @param request: ListApplicationAccessPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccessPointsResponse
        """
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
            action='ListApplicationAccessPoints',
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
            kms_20160120_models.ListApplicationAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_access_points(
        self,
        request: kms_20160120_models.ListApplicationAccessPointsRequest,
    ) -> kms_20160120_models.ListApplicationAccessPointsResponse:
        """
        @summary Queries a list of application access points (AAPs).
        
        @param request: ListApplicationAccessPointsRequest
        @return: ListApplicationAccessPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_access_points_with_options(request, runtime)

    async def list_application_access_points_async(
        self,
        request: kms_20160120_models.ListApplicationAccessPointsRequest,
    ) -> kms_20160120_models.ListApplicationAccessPointsResponse:
        """
        @summary Queries a list of application access points (AAPs).
        
        @param request: ListApplicationAccessPointsRequest
        @return: ListApplicationAccessPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_access_points_with_options_async(request, runtime)

    def list_client_keys_with_options(
        self,
        request: kms_20160120_models.ListClientKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListClientKeysResponse:
        """
        @param request: ListClientKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientKeysResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientKeys',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListClientKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_keys_with_options_async(
        self,
        request: kms_20160120_models.ListClientKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListClientKeysResponse:
        """
        @param request: ListClientKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientKeysResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientKeys',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListClientKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_keys(
        self,
        request: kms_20160120_models.ListClientKeysRequest,
    ) -> kms_20160120_models.ListClientKeysResponse:
        """
        @param request: ListClientKeysRequest
        @return: ListClientKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_client_keys_with_options(request, runtime)

    async def list_client_keys_async(
        self,
        request: kms_20160120_models.ListClientKeysRequest,
    ) -> kms_20160120_models.ListClientKeysResponse:
        """
        @param request: ListClientKeysRequest
        @return: ListClientKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_client_keys_with_options_async(request, runtime)

    def list_key_versions_with_options(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        """
        @summary Queries all versions of a specified CMK.
        
        @param request: ListKeyVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyVersionsResponse
        """
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
        """
        @summary Queries all versions of a specified CMK.
        
        @param request: ListKeyVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyVersionsResponse
        """
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
        """
        @summary Queries all versions of a specified CMK.
        
        @param request: ListKeyVersionsRequest
        @return: ListKeyVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_key_versions_with_options(request, runtime)

    async def list_key_versions_async(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        """
        @summary Queries all versions of a specified CMK.
        
        @param request: ListKeyVersionsRequest
        @return: ListKeyVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_key_versions_with_options_async(request, runtime)

    def list_keys_with_options(
        self,
        request: kms_20160120_models.ListKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        """
        @summary Queries all customer master keys (CMKs) of the current Alibaba Cloud account in the current region.
        
        @param request: ListKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeysResponse
        """
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
        """
        @summary Queries all customer master keys (CMKs) of the current Alibaba Cloud account in the current region.
        
        @param request: ListKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeysResponse
        """
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
        """
        @summary Queries all customer master keys (CMKs) of the current Alibaba Cloud account in the current region.
        
        @param request: ListKeysRequest
        @return: ListKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_keys_with_options(request, runtime)

    async def list_keys_async(
        self,
        request: kms_20160120_models.ListKeysRequest,
    ) -> kms_20160120_models.ListKeysResponse:
        """
        @summary Queries all customer master keys (CMKs) of the current Alibaba Cloud account in the current region.
        
        @param request: ListKeysRequest
        @return: ListKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_keys_with_options_async(request, runtime)

    def list_kms_instances_with_options(
        self,
        request: kms_20160120_models.ListKmsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKmsInstancesResponse:
        """
        @summary Queries a list of Key Management Service (KMS) instances.
        
        @param request: ListKmsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKmsInstancesResponse
        """
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
            action='ListKmsInstances',
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
            kms_20160120_models.ListKmsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kms_instances_with_options_async(
        self,
        request: kms_20160120_models.ListKmsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKmsInstancesResponse:
        """
        @summary Queries a list of Key Management Service (KMS) instances.
        
        @param request: ListKmsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKmsInstancesResponse
        """
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
            action='ListKmsInstances',
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
            kms_20160120_models.ListKmsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kms_instances(
        self,
        request: kms_20160120_models.ListKmsInstancesRequest,
    ) -> kms_20160120_models.ListKmsInstancesResponse:
        """
        @summary Queries a list of Key Management Service (KMS) instances.
        
        @param request: ListKmsInstancesRequest
        @return: ListKmsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_kms_instances_with_options(request, runtime)

    async def list_kms_instances_async(
        self,
        request: kms_20160120_models.ListKmsInstancesRequest,
    ) -> kms_20160120_models.ListKmsInstancesResponse:
        """
        @summary Queries a list of Key Management Service (KMS) instances.
        
        @param request: ListKmsInstancesRequest
        @return: ListKmsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_kms_instances_with_options_async(request, runtime)

    def list_network_rules_with_options(
        self,
        request: kms_20160120_models.ListNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListNetworkRulesResponse:
        """
        @summary Queries a list of access control rules.
        
        @param request: ListNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkRulesResponse
        """
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
            action='ListNetworkRules',
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
            kms_20160120_models.ListNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_rules_with_options_async(
        self,
        request: kms_20160120_models.ListNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListNetworkRulesResponse:
        """
        @summary Queries a list of access control rules.
        
        @param request: ListNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkRulesResponse
        """
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
            action='ListNetworkRules',
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
            kms_20160120_models.ListNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_rules(
        self,
        request: kms_20160120_models.ListNetworkRulesRequest,
    ) -> kms_20160120_models.ListNetworkRulesResponse:
        """
        @summary Queries a list of access control rules.
        
        @param request: ListNetworkRulesRequest
        @return: ListNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_rules_with_options(request, runtime)

    async def list_network_rules_async(
        self,
        request: kms_20160120_models.ListNetworkRulesRequest,
    ) -> kms_20160120_models.ListNetworkRulesResponse:
        """
        @summary Queries a list of access control rules.
        
        @param request: ListNetworkRulesRequest
        @return: ListNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_rules_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: kms_20160120_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListPoliciesResponse:
        """
        @summary Queries a list of permission policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
            action='ListPolicies',
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
            kms_20160120_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: kms_20160120_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListPoliciesResponse:
        """
        @summary Queries a list of permission policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
            action='ListPolicies',
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
            kms_20160120_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: kms_20160120_models.ListPoliciesRequest,
    ) -> kms_20160120_models.ListPoliciesResponse:
        """
        @summary Queries a list of permission policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: kms_20160120_models.ListPoliciesRequest,
    ) -> kms_20160120_models.ListPoliciesResponse:
        """
        @summary Queries a list of permission policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_resource_tags_with_options(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        """
        @description Request format: KeyId="string"
        
        @param request: ListResourceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTagsResponse
        """
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
        """
        @description Request format: KeyId="string"
        
        @param request: ListResourceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTagsResponse
        """
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
        """
        @description Request format: KeyId="string"
        
        @param request: ListResourceTagsRequest
        @return: ListResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    async def list_resource_tags_async(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        """
        @description Request format: KeyId="string"
        
        @param request: ListResourceTagsRequest
        @return: ListResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_tags_with_options_async(request, runtime)

    def list_secret_version_ids_with_options(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        """
        @description The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        
        @param request: ListSecretVersionIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretVersionIdsResponse
        """
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
        """
        @description The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        
        @param request: ListSecretVersionIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretVersionIdsResponse
        """
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
        """
        @description The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        
        @param request: ListSecretVersionIdsRequest
        @return: ListSecretVersionIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    async def list_secret_version_ids_async(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        """
        @description The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        
        @param request: ListSecretVersionIdsRequest
        @return: ListSecretVersionIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_version_ids_with_options_async(request, runtime)

    def list_secrets_with_options(
        self,
        request: kms_20160120_models.ListSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        """
        @description Specifies whether to return the resource tags of the secret. Valid values:
        true: returns the resource tags.
        false: does not return the resource tags. This is the default value.
        
        @param request: ListSecretsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretsResponse
        """
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
        """
        @description Specifies whether to return the resource tags of the secret. Valid values:
        true: returns the resource tags.
        false: does not return the resource tags. This is the default value.
        
        @param request: ListSecretsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretsResponse
        """
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
        """
        @description Specifies whether to return the resource tags of the secret. Valid values:
        true: returns the resource tags.
        false: does not return the resource tags. This is the default value.
        
        @param request: ListSecretsRequest
        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    async def list_secrets_async(
        self,
        request: kms_20160120_models.ListSecretsRequest,
    ) -> kms_20160120_models.ListSecretsResponse:
        """
        @description Specifies whether to return the resource tags of the secret. Valid values:
        true: returns the resource tags.
        false: does not return the resource tags. This is the default value.
        
        @param request: ListSecretsRequest
        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_secrets_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: kms_20160120_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a key or a secret.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            kms_20160120_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: kms_20160120_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a key or a secret.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            kms_20160120_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: kms_20160120_models.ListTagResourcesRequest,
    ) -> kms_20160120_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a key or a secret.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: kms_20160120_models.ListTagResourcesRequest,
    ) -> kms_20160120_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a key or a secret.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def open_kms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        """
        @summary Activates Key Management Service (KMS) under your Alibaba cloud account.
        
        @description When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        
        @param request: OpenKmsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenKmsServiceResponse
        """
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
        """
        @summary Activates Key Management Service (KMS) under your Alibaba cloud account.
        
        @description When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        
        @param request: OpenKmsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenKmsServiceResponse
        """
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
        """
        @summary Activates Key Management Service (KMS) under your Alibaba cloud account.
        
        @description When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        
        @return: OpenKmsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    async def open_kms_service_async(self) -> kms_20160120_models.OpenKmsServiceResponse:
        """
        @summary Activates Key Management Service (KMS) under your Alibaba cloud account.
        
        @description When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        
        @return: OpenKmsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_kms_service_with_options_async(runtime)

    def put_secret_value_with_options(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.PutSecretValueResponse:
        """
        @description This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        
        @param request: PutSecretValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutSecretValueResponse
        """
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
        """
        @description This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        
        @param request: PutSecretValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutSecretValueResponse
        """
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
        """
        @description This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        
        @param request: PutSecretValueRequest
        @return: PutSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    async def put_secret_value_async(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
    ) -> kms_20160120_models.PutSecretValueResponse:
        """
        @description This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        
        @param request: PutSecretValueRequest
        @return: PutSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_secret_value_with_options_async(request, runtime)

    def re_encrypt_with_options(
        self,
        tmp_req: kms_20160120_models.ReEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReEncryptResponse:
        """
        @description You can call this operation in the following scenarios:
        After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](https://help.aliyun.com/document_detail/134270.html).
        The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        kms:ReEncryptFrom on the source CMK
        kms:ReEncryptTo on the destination CMK
        For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        
        @param tmp_req: ReEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReEncryptResponse
        """
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
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description You can call this operation in the following scenarios:
        After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](https://help.aliyun.com/document_detail/134270.html).
        The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        kms:ReEncryptFrom on the source CMK
        kms:ReEncryptTo on the destination CMK
        For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        
        @param tmp_req: ReEncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReEncryptResponse
        """
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
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        """
        @description You can call this operation in the following scenarios:
        After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](https://help.aliyun.com/document_detail/134270.html).
        The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        kms:ReEncryptFrom on the source CMK
        kms:ReEncryptTo on the destination CMK
        For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        
        @param request: ReEncryptRequest
        @return: ReEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    async def re_encrypt_async(
        self,
        request: kms_20160120_models.ReEncryptRequest,
    ) -> kms_20160120_models.ReEncryptResponse:
        """
        @description You can call this operation in the following scenarios:
        After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](https://help.aliyun.com/document_detail/134270.html).
        The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        kms:ReEncryptFrom on the source CMK
        kms:ReEncryptTo on the destination CMK
        For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        
        @param request: ReEncryptRequest
        @return: ReEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.re_encrypt_with_options_async(request, runtime)

    def release_kms_instance_with_options(
        self,
        request: kms_20160120_models.ReleaseKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReleaseKmsInstanceResponse:
        """
        @summary 仅后付费实例支持释放，预付费实例需要从用户中心-退订管理释放。
        
        @param request: ReleaseKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_without_backup):
            query['ForceDeleteWithoutBackup'] = request.force_delete_without_backup
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseKmsInstance',
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
            kms_20160120_models.ReleaseKmsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_kms_instance_with_options_async(
        self,
        request: kms_20160120_models.ReleaseKmsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReleaseKmsInstanceResponse:
        """
        @summary 仅后付费实例支持释放，预付费实例需要从用户中心-退订管理释放。
        
        @param request: ReleaseKmsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseKmsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_without_backup):
            query['ForceDeleteWithoutBackup'] = request.force_delete_without_backup
        if not UtilClient.is_unset(request.kms_instance_id):
            query['KmsInstanceId'] = request.kms_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseKmsInstance',
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
            kms_20160120_models.ReleaseKmsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_kms_instance(
        self,
        request: kms_20160120_models.ReleaseKmsInstanceRequest,
    ) -> kms_20160120_models.ReleaseKmsInstanceResponse:
        """
        @summary 仅后付费实例支持释放，预付费实例需要从用户中心-退订管理释放。
        
        @param request: ReleaseKmsInstanceRequest
        @return: ReleaseKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_kms_instance_with_options(request, runtime)

    async def release_kms_instance_async(
        self,
        request: kms_20160120_models.ReleaseKmsInstanceRequest,
    ) -> kms_20160120_models.ReleaseKmsInstanceResponse:
        """
        @summary 仅后付费实例支持释放，预付费实例需要从用户中心-退订管理释放。
        
        @param request: ReleaseKmsInstanceRequest
        @return: ReleaseKmsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_kms_instance_with_options_async(request, runtime)

    def restore_secret_with_options(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RestoreSecretResponse:
        """
        @description You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        
        @param request: RestoreSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreSecretResponse
        """
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
        """
        @description You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        
        @param request: RestoreSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreSecretResponse
        """
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
        """
        @description You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        
        @param request: RestoreSecretRequest
        @return: RestoreSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    async def restore_secret_async(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
    ) -> kms_20160120_models.RestoreSecretResponse:
        """
        @description You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        
        @param request: RestoreSecretRequest
        @return: RestoreSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_secret_with_options_async(request, runtime)

    def rotate_secret_with_options(
        self,
        request: kms_20160120_models.RotateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RotateSecretResponse:
        """
        @description Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        
        @param request: RotateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RotateSecretResponse
        """
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
        """
        @description Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        
        @param request: RotateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RotateSecretResponse
        """
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
        """
        @description Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        
        @param request: RotateSecretRequest
        @return: RotateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    async def rotate_secret_async(
        self,
        request: kms_20160120_models.RotateSecretRequest,
    ) -> kms_20160120_models.RotateSecretResponse:
        """
        @description Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        
        @param request: RotateSecretRequest
        @return: RotateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rotate_secret_with_options_async(request, runtime)

    def schedule_key_deletion_with_options(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        """
        @description During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](https://help.aliyun.com/document_detail/35151.html) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](https://help.aliyun.com/document_detail/44197.html) operation to cancel the key deletion task before the scheduled period ends.
        
        @param request: ScheduleKeyDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScheduleKeyDeletionResponse
        """
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
        """
        @description During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](https://help.aliyun.com/document_detail/35151.html) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](https://help.aliyun.com/document_detail/44197.html) operation to cancel the key deletion task before the scheduled period ends.
        
        @param request: ScheduleKeyDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScheduleKeyDeletionResponse
        """
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
        """
        @description During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](https://help.aliyun.com/document_detail/35151.html) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](https://help.aliyun.com/document_detail/44197.html) operation to cancel the key deletion task before the scheduled period ends.
        
        @param request: ScheduleKeyDeletionRequest
        @return: ScheduleKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    async def schedule_key_deletion_async(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        """
        @description During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](https://help.aliyun.com/document_detail/35151.html) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](https://help.aliyun.com/document_detail/44197.html) operation to cancel the key deletion task before the scheduled period ends.
        
        @param request: ScheduleKeyDeletionRequest
        @return: ScheduleKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.schedule_key_deletion_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        """
        @summary Enables or disables deletion protection for a customer master key (CMK).
        
        @description    After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123***:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        
        @param request: SetDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not UtilClient.is_unset(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
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
        """
        @summary Enables or disables deletion protection for a customer master key (CMK).
        
        @description    After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123***:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        
        @param request: SetDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not UtilClient.is_unset(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
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
        """
        @summary Enables or disables deletion protection for a customer master key (CMK).
        
        @description    After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123***:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        
        @param request: SetDeletionProtectionRequest
        @return: SetDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: kms_20160120_models.SetDeletionProtectionRequest,
    ) -> kms_20160120_models.SetDeletionProtectionResponse:
        """
        @summary Enables or disables deletion protection for a customer master key (CMK).
        
        @description    After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123***:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        
        @param request: SetDeletionProtectionRequest
        @return: SetDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def set_key_policy_with_options(
        self,
        request: kms_20160120_models.SetKeyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetKeyPolicyResponse:
        """
        @summary 可以设置一条 Key Policy，且名称必须为 default。
        
        @param request: SetKeyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetKeyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetKeyPolicy',
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
            kms_20160120_models.SetKeyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_key_policy_with_options_async(
        self,
        request: kms_20160120_models.SetKeyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetKeyPolicyResponse:
        """
        @summary 可以设置一条 Key Policy，且名称必须为 default。
        
        @param request: SetKeyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetKeyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetKeyPolicy',
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
            kms_20160120_models.SetKeyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_key_policy(
        self,
        request: kms_20160120_models.SetKeyPolicyRequest,
    ) -> kms_20160120_models.SetKeyPolicyResponse:
        """
        @summary 可以设置一条 Key Policy，且名称必须为 default。
        
        @param request: SetKeyPolicyRequest
        @return: SetKeyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_key_policy_with_options(request, runtime)

    async def set_key_policy_async(
        self,
        request: kms_20160120_models.SetKeyPolicyRequest,
    ) -> kms_20160120_models.SetKeyPolicyResponse:
        """
        @summary 可以设置一条 Key Policy，且名称必须为 default。
        
        @param request: SetKeyPolicyRequest
        @return: SetKeyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_key_policy_with_options_async(request, runtime)

    def set_secret_policy_with_options(
        self,
        request: kms_20160120_models.SetSecretPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetSecretPolicyResponse:
        """
        @summary 可以设置一条 Secret Policy，且名称必须为 default。
        
        @param request: SetSecretPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSecretPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSecretPolicy',
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
            kms_20160120_models.SetSecretPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_secret_policy_with_options_async(
        self,
        request: kms_20160120_models.SetSecretPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.SetSecretPolicyResponse:
        """
        @summary 可以设置一条 Secret Policy，且名称必须为 default。
        
        @param request: SetSecretPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSecretPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSecretPolicy',
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
            kms_20160120_models.SetSecretPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_secret_policy(
        self,
        request: kms_20160120_models.SetSecretPolicyRequest,
    ) -> kms_20160120_models.SetSecretPolicyResponse:
        """
        @summary 可以设置一条 Secret Policy，且名称必须为 default。
        
        @param request: SetSecretPolicyRequest
        @return: SetSecretPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_secret_policy_with_options(request, runtime)

    async def set_secret_policy_async(
        self,
        request: kms_20160120_models.SetSecretPolicyRequest,
    ) -> kms_20160120_models.SetSecretPolicyResponse:
        """
        @summary 可以设置一条 Secret Policy，且名称必须为 default。
        
        @param request: SetSecretPolicyRequest
        @return: SetSecretPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_secret_policy_with_options_async(request, runtime)

    def tag_resource_with_options(
        self,
        request: kms_20160120_models.TagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        """
        @description You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf***`.
        
        @param request: TagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourceResponse
        """
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
        """
        @description You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf***`.
        
        @param request: TagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourceResponse
        """
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
        """
        @description You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf***`.
        
        @param request: TagResourceRequest
        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    async def tag_resource_async(
        self,
        request: kms_20160120_models.TagResourceRequest,
    ) -> kms_20160120_models.TagResourceResponse:
        """
        @description You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf***`.
        
        @param request: TagResourceRequest
        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resource_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: kms_20160120_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourcesResponse:
        """
        @summary Adds tags to keys or secrets.
        
        @description You can add multiple tags to multiple keys or multiple secrets at a time.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            kms_20160120_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: kms_20160120_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourcesResponse:
        """
        @summary Adds tags to keys or secrets.
        
        @description You can add multiple tags to multiple keys or multiple secrets at a time.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            kms_20160120_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: kms_20160120_models.TagResourcesRequest,
    ) -> kms_20160120_models.TagResourcesResponse:
        """
        @summary Adds tags to keys or secrets.
        
        @description You can add multiple tags to multiple keys or multiple secrets at a time.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: kms_20160120_models.TagResourcesRequest,
    ) -> kms_20160120_models.TagResourcesResponse:
        """
        @summary Adds tags to keys or secrets.
        
        @description You can add multiple tags to multiple keys or multiple secrets at a time.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resource_with_options(
        self,
        request: kms_20160120_models.UntagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourceResponse:
        """
        @description One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        
        @param request: UntagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourceResponse
        """
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
        """
        @description One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        
        @param request: UntagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourceResponse
        """
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
        """
        @description One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        
        @param request: UntagResourceRequest
        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

    async def untag_resource_async(
        self,
        request: kms_20160120_models.UntagResourceRequest,
    ) -> kms_20160120_models.UntagResourceResponse:
        """
        @description One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        
        @param request: UntagResourceRequest
        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resource_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: kms_20160120_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourcesResponse:
        """
        @summary Removes tags from keys or secrets.
        
        @description You can remove multiple tags from multiple keys or multiple secrets at a time. You cannot remove tags that start with aliyun or acs:.
        If you enter multiple tag keys in the request parameters and only some of the tag keys are associated with resources, the operation can be called and the tags whose keys are associated with resources are removed from the resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            kms_20160120_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: kms_20160120_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourcesResponse:
        """
        @summary Removes tags from keys or secrets.
        
        @description You can remove multiple tags from multiple keys or multiple secrets at a time. You cannot remove tags that start with aliyun or acs:.
        If you enter multiple tag keys in the request parameters and only some of the tag keys are associated with resources, the operation can be called and the tags whose keys are associated with resources are removed from the resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            kms_20160120_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: kms_20160120_models.UntagResourcesRequest,
    ) -> kms_20160120_models.UntagResourcesResponse:
        """
        @summary Removes tags from keys or secrets.
        
        @description You can remove multiple tags from multiple keys or multiple secrets at a time. You cannot remove tags that start with aliyun or acs:.
        If you enter multiple tag keys in the request parameters and only some of the tag keys are associated with resources, the operation can be called and the tags whose keys are associated with resources are removed from the resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: kms_20160120_models.UntagResourcesRequest,
    ) -> kms_20160120_models.UntagResourcesResponse:
        """
        @summary Removes tags from keys or secrets.
        
        @description You can remove multiple tags from multiple keys or multiple secrets at a time. You cannot remove tags that start with aliyun or acs:.
        If you enter multiple tag keys in the request parameters and only some of the tag keys are associated with resources, the operation can be called and the tags whose keys are associated with resources are removed from the resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_alias_with_options(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateAliasResponse:
        """
        @param request: UpdateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
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
        """
        @param request: UpdateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
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
        """
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    async def update_alias_async(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
    ) -> kms_20160120_models.UpdateAliasResponse:
        """
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_alias_with_options_async(request, runtime)

    def update_application_access_point_with_options(
        self,
        request: kms_20160120_models.UpdateApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateApplicationAccessPointResponse:
        """
        @description The update takes effect immediately after an AAP information is updated. Exercise caution when you perform this operation. You can update the description of an AAP and the permission policies that are associated with the AAP. You cannot update the name of the AAP.
        
        @param request: UpdateApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policies):
            query['Policies'] = request.policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationAccessPoint',
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
            kms_20160120_models.UpdateApplicationAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_access_point_with_options_async(
        self,
        request: kms_20160120_models.UpdateApplicationAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateApplicationAccessPointResponse:
        """
        @description The update takes effect immediately after an AAP information is updated. Exercise caution when you perform this operation. You can update the description of an AAP and the permission policies that are associated with the AAP. You cannot update the name of the AAP.
        
        @param request: UpdateApplicationAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policies):
            query['Policies'] = request.policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationAccessPoint',
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
            kms_20160120_models.UpdateApplicationAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_access_point(
        self,
        request: kms_20160120_models.UpdateApplicationAccessPointRequest,
    ) -> kms_20160120_models.UpdateApplicationAccessPointResponse:
        """
        @description The update takes effect immediately after an AAP information is updated. Exercise caution when you perform this operation. You can update the description of an AAP and the permission policies that are associated with the AAP. You cannot update the name of the AAP.
        
        @param request: UpdateApplicationAccessPointRequest
        @return: UpdateApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_access_point_with_options(request, runtime)

    async def update_application_access_point_async(
        self,
        request: kms_20160120_models.UpdateApplicationAccessPointRequest,
    ) -> kms_20160120_models.UpdateApplicationAccessPointResponse:
        """
        @description The update takes effect immediately after an AAP information is updated. Exercise caution when you perform this operation. You can update the description of an AAP and the permission policies that are associated with the AAP. You cannot update the name of the AAP.
        
        @param request: UpdateApplicationAccessPointRequest
        @return: UpdateApplicationAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_access_point_with_options_async(request, runtime)

    def update_certificate_status_with_options(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        """
        @description In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        
        @param request: UpdateCertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCertificateStatusResponse
        """
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
        """
        @description In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        
        @param request: UpdateCertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCertificateStatusResponse
        """
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
        """
        @description In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        
        @param request: UpdateCertificateStatusRequest
        @return: UpdateCertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_certificate_status_with_options(request, runtime)

    async def update_certificate_status_async(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        """
        @description In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        
        @param request: UpdateCertificateStatusRequest
        @return: UpdateCertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_certificate_status_with_options_async(request, runtime)

    def update_key_description_with_options(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        """
        @summary 调用UpdateKeyDescription接口更新主密钥的描述信息。
        
        @description This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation. You can call this operation to add, modify, or delete the description of a CMK.
        
        @param request: UpdateKeyDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKeyDescriptionResponse
        """
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
        """
        @summary 调用UpdateKeyDescription接口更新主密钥的描述信息。
        
        @description This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation. You can call this operation to add, modify, or delete the description of a CMK.
        
        @param request: UpdateKeyDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKeyDescriptionResponse
        """
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
        """
        @summary 调用UpdateKeyDescription接口更新主密钥的描述信息。
        
        @description This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation. You can call this operation to add, modify, or delete the description of a CMK.
        
        @param request: UpdateKeyDescriptionRequest
        @return: UpdateKeyDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    async def update_key_description_async(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        """
        @summary 调用UpdateKeyDescription接口更新主密钥的描述信息。
        
        @description This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation. You can call this operation to add, modify, or delete the description of a CMK.
        
        @param request: UpdateKeyDescriptionRequest
        @return: UpdateKeyDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_key_description_with_options_async(request, runtime)

    def update_kms_instance_bind_vpc_with_options(
        self,
        request: kms_20160120_models.UpdateKmsInstanceBindVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKmsInstanceBindVpcResponse:
        """
        @summary Updates the virtual private cloud (VPC) that is associated with a Key Management Service (KMS) instance.
        
        @description If your own applications are deployed in multiple VPCs in the same region, you can associate the VPCs except the VPC in which the KMS instance resides with the KMS instance. This topic describes how to configure the VPCs.
        The VPCs can belong to the same Alibaba Cloud account or different Alibaba Cloud accounts. After the configuration is complete, the applications in these VPCs can access the KMS instance.
        > If the VPCs belong to different Alibaba Cloud accounts, you must first configure resource sharing to share the vSwitches of other Alibaba Cloud accounts with the Alibaba Cloud account to which the KMS instance belongs. For more information, see [Access a KMS instance from multiple VPCs in the same region](https://help.aliyun.com/document_detail/2393236.html).
        
        @param request: UpdateKmsInstanceBindVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKmsInstanceBindVpcResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKmsInstanceBindVpc',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateKmsInstanceBindVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kms_instance_bind_vpc_with_options_async(
        self,
        request: kms_20160120_models.UpdateKmsInstanceBindVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKmsInstanceBindVpcResponse:
        """
        @summary Updates the virtual private cloud (VPC) that is associated with a Key Management Service (KMS) instance.
        
        @description If your own applications are deployed in multiple VPCs in the same region, you can associate the VPCs except the VPC in which the KMS instance resides with the KMS instance. This topic describes how to configure the VPCs.
        The VPCs can belong to the same Alibaba Cloud account or different Alibaba Cloud accounts. After the configuration is complete, the applications in these VPCs can access the KMS instance.
        > If the VPCs belong to different Alibaba Cloud accounts, you must first configure resource sharing to share the vSwitches of other Alibaba Cloud accounts with the Alibaba Cloud account to which the KMS instance belongs. For more information, see [Access a KMS instance from multiple VPCs in the same region](https://help.aliyun.com/document_detail/2393236.html).
        
        @param request: UpdateKmsInstanceBindVpcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKmsInstanceBindVpcResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKmsInstanceBindVpc',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateKmsInstanceBindVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kms_instance_bind_vpc(
        self,
        request: kms_20160120_models.UpdateKmsInstanceBindVpcRequest,
    ) -> kms_20160120_models.UpdateKmsInstanceBindVpcResponse:
        """
        @summary Updates the virtual private cloud (VPC) that is associated with a Key Management Service (KMS) instance.
        
        @description If your own applications are deployed in multiple VPCs in the same region, you can associate the VPCs except the VPC in which the KMS instance resides with the KMS instance. This topic describes how to configure the VPCs.
        The VPCs can belong to the same Alibaba Cloud account or different Alibaba Cloud accounts. After the configuration is complete, the applications in these VPCs can access the KMS instance.
        > If the VPCs belong to different Alibaba Cloud accounts, you must first configure resource sharing to share the vSwitches of other Alibaba Cloud accounts with the Alibaba Cloud account to which the KMS instance belongs. For more information, see [Access a KMS instance from multiple VPCs in the same region](https://help.aliyun.com/document_detail/2393236.html).
        
        @param request: UpdateKmsInstanceBindVpcRequest
        @return: UpdateKmsInstanceBindVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_kms_instance_bind_vpc_with_options(request, runtime)

    async def update_kms_instance_bind_vpc_async(
        self,
        request: kms_20160120_models.UpdateKmsInstanceBindVpcRequest,
    ) -> kms_20160120_models.UpdateKmsInstanceBindVpcResponse:
        """
        @summary Updates the virtual private cloud (VPC) that is associated with a Key Management Service (KMS) instance.
        
        @description If your own applications are deployed in multiple VPCs in the same region, you can associate the VPCs except the VPC in which the KMS instance resides with the KMS instance. This topic describes how to configure the VPCs.
        The VPCs can belong to the same Alibaba Cloud account or different Alibaba Cloud accounts. After the configuration is complete, the applications in these VPCs can access the KMS instance.
        > If the VPCs belong to different Alibaba Cloud accounts, you must first configure resource sharing to share the vSwitches of other Alibaba Cloud accounts with the Alibaba Cloud account to which the KMS instance belongs. For more information, see [Access a KMS instance from multiple VPCs in the same region](https://help.aliyun.com/document_detail/2393236.html).
        
        @param request: UpdateKmsInstanceBindVpcRequest
        @return: UpdateKmsInstanceBindVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_kms_instance_bind_vpc_with_options_async(request, runtime)

    def update_network_rule_with_options(
        self,
        request: kms_20160120_models.UpdateNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateNetworkRuleResponse:
        """
        @summary Updates an access control rule.
        
        @description - You can update only private IP addresses and description of an access control rule. You cannot update the name and network type of an access control rule.
        - Updating an access control rule affects all permission policies that are bound to the access control rule. Exercise caution when you perform this operation.
        
        @param request: UpdateNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkRule',
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
            kms_20160120_models.UpdateNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_rule_with_options_async(
        self,
        request: kms_20160120_models.UpdateNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateNetworkRuleResponse:
        """
        @summary Updates an access control rule.
        
        @description - You can update only private IP addresses and description of an access control rule. You cannot update the name and network type of an access control rule.
        - Updating an access control rule affects all permission policies that are bound to the access control rule. Exercise caution when you perform this operation.
        
        @param request: UpdateNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_private_ip):
            query['SourcePrivateIp'] = request.source_private_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkRule',
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
            kms_20160120_models.UpdateNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_rule(
        self,
        request: kms_20160120_models.UpdateNetworkRuleRequest,
    ) -> kms_20160120_models.UpdateNetworkRuleResponse:
        """
        @summary Updates an access control rule.
        
        @description - You can update only private IP addresses and description of an access control rule. You cannot update the name and network type of an access control rule.
        - Updating an access control rule affects all permission policies that are bound to the access control rule. Exercise caution when you perform this operation.
        
        @param request: UpdateNetworkRuleRequest
        @return: UpdateNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_network_rule_with_options(request, runtime)

    async def update_network_rule_async(
        self,
        request: kms_20160120_models.UpdateNetworkRuleRequest,
    ) -> kms_20160120_models.UpdateNetworkRuleResponse:
        """
        @summary Updates an access control rule.
        
        @description - You can update only private IP addresses and description of an access control rule. You cannot update the name and network type of an access control rule.
        - Updating an access control rule affects all permission policies that are bound to the access control rule. Exercise caution when you perform this operation.
        
        @param request: UpdateNetworkRuleRequest
        @return: UpdateNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_network_rule_with_options_async(request, runtime)

    def update_policy_with_options(
        self,
        request: kms_20160120_models.UpdatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdatePolicyResponse:
        """
        @summary 更新一个权限策略
        
        @description - You can update the role-based access control (RBAC) permissions, accessible resources, access control rules, and description of a permission policy. You cannot update the name or scope of a permission policy.
        - Updating a permission policy affects all application access points (AAPs) that are bound to the permission policy. Exercise caution when you perform this operation.
        
        @param request: UpdatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
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
            kms_20160120_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        request: kms_20160120_models.UpdatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdatePolicyResponse:
        """
        @summary 更新一个权限策略
        
        @description - You can update the role-based access control (RBAC) permissions, accessible resources, access control rules, and description of a permission policy. You cannot update the name or scope of a permission policy.
        - Updating a permission policy affects all application access points (AAPs) that are bound to the permission policy. Exercise caution when you perform this operation.
        
        @param request: UpdatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_rules):
            query['AccessControlRules'] = request.access_control_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
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
            kms_20160120_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        request: kms_20160120_models.UpdatePolicyRequest,
    ) -> kms_20160120_models.UpdatePolicyResponse:
        """
        @summary 更新一个权限策略
        
        @description - You can update the role-based access control (RBAC) permissions, accessible resources, access control rules, and description of a permission policy. You cannot update the name or scope of a permission policy.
        - Updating a permission policy affects all application access points (AAPs) that are bound to the permission policy. Exercise caution when you perform this operation.
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_policy_with_options(request, runtime)

    async def update_policy_async(
        self,
        request: kms_20160120_models.UpdatePolicyRequest,
    ) -> kms_20160120_models.UpdatePolicyResponse:
        """
        @summary 更新一个权限策略
        
        @description - You can update the role-based access control (RBAC) permissions, accessible resources, access control rules, and description of a permission policy. You cannot update the name or scope of a permission policy.
        - Updating a permission policy affects all application access points (AAPs) that are bound to the permission policy. Exercise caution when you perform this operation.
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_policy_with_options_async(request, runtime)

    def update_rotation_policy_with_options(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        """
        @description When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        Asymmetric key
        Service-managed key
        Bring your own key (BYOK) that is imported into KMS
        Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***`. The automatic rotation period is 30 days.
        
        @param request: UpdateRotationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRotationPolicyResponse
        """
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
        """
        @description When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        Asymmetric key
        Service-managed key
        Bring your own key (BYOK) that is imported into KMS
        Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***`. The automatic rotation period is 30 days.
        
        @param request: UpdateRotationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRotationPolicyResponse
        """
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
        """
        @description When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        Asymmetric key
        Service-managed key
        Bring your own key (BYOK) that is imported into KMS
        Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***`. The automatic rotation period is 30 days.
        
        @param request: UpdateRotationPolicyRequest
        @return: UpdateRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    async def update_rotation_policy_async(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        """
        @description When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        Asymmetric key
        Service-managed key
        Bring your own key (BYOK) that is imported into KMS
        Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678***`. The automatic rotation period is 30 days.
        
        @param request: UpdateRotationPolicyRequest
        @return: UpdateRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rotation_policy_with_options_async(request, runtime)

    def update_secret_with_options(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretResponse:
        """
        @summary Updates the metadata of a secret.
        
        @description In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        
        @param request: UpdateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretResponse
        """
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
        """
        @summary Updates the metadata of a secret.
        
        @description In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        
        @param request: UpdateSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretResponse
        """
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
        """
        @summary Updates the metadata of a secret.
        
        @description In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        
        @param request: UpdateSecretRequest
        @return: UpdateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_with_options(request, runtime)

    async def update_secret_async(
        self,
        request: kms_20160120_models.UpdateSecretRequest,
    ) -> kms_20160120_models.UpdateSecretResponse:
        """
        @summary Updates the metadata of a secret.
        
        @description In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        
        @param request: UpdateSecretRequest
        @return: UpdateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_with_options_async(request, runtime)

    def update_secret_rotation_policy_with_options(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        """
        @description After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        
        @param request: UpdateSecretRotationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretRotationPolicyResponse
        """
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
        """
        @description After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        
        @param request: UpdateSecretRotationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretRotationPolicyResponse
        """
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
        """
        @description After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        
        @param request: UpdateSecretRotationPolicyRequest
        @return: UpdateSecretRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    async def update_secret_rotation_policy_async(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        """
        @description After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        
        @param request: UpdateSecretRotationPolicyRequest
        @return: UpdateSecretRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_rotation_policy_with_options_async(request, runtime)

    def update_secret_version_stage_with_options(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        """
        @summary UpdateSecretVersionStage
        
        @description Updates the stage label that marks a secret version.
        
        @param request: UpdateSecretVersionStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretVersionStageResponse
        """
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
        """
        @summary UpdateSecretVersionStage
        
        @description Updates the stage label that marks a secret version.
        
        @param request: UpdateSecretVersionStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretVersionStageResponse
        """
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
        """
        @summary UpdateSecretVersionStage
        
        @description Updates the stage label that marks a secret version.
        
        @param request: UpdateSecretVersionStageRequest
        @return: UpdateSecretVersionStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    async def update_secret_version_stage_async(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        """
        @summary UpdateSecretVersionStage
        
        @description Updates the stage label that marks a secret version.
        
        @param request: UpdateSecretVersionStageRequest
        @return: UpdateSecretVersionStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_version_stage_with_options_async(request, runtime)

    def upload_certificate_with_options(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UploadCertificateResponse:
        """
        @description In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        
        @param request: UploadCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCertificateResponse
        """
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
        """
        @description In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        
        @param request: UploadCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCertificateResponse
        """
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
        """
        @description In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        
        @param request: UploadCertificateRequest
        @return: UploadCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_certificate_with_options(request, runtime)

    async def upload_certificate_async(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
    ) -> kms_20160120_models.UploadCertificateResponse:
        """
        @description In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        
        @param request: UploadCertificateRequest
        @return: UploadCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_certificate_with_options_async(request, runtime)
