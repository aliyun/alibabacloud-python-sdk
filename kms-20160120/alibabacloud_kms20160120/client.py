# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricDecryptResponse().from_map(
            self.do_rpcrequest('AsymmetricDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def asymmetric_decrypt_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricDecryptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricDecryptResponse().from_map(
            await self.do_rpcrequest_async('AsymmetricDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricEncryptResponse().from_map(
            self.do_rpcrequest('AsymmetricEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def asymmetric_encrypt_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricEncryptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricEncryptResponse().from_map(
            await self.do_rpcrequest_async('AsymmetricEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricSignResponse().from_map(
            self.do_rpcrequest('AsymmetricSign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def asymmetric_sign_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricSignResponse().from_map(
            await self.do_rpcrequest_async('AsymmetricSign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricVerifyResponse().from_map(
            self.do_rpcrequest('AsymmetricVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def asymmetric_verify_with_options_async(
        self,
        request: kms_20160120_models.AsymmetricVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.AsymmetricVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricVerifyResponse().from_map(
            await self.do_rpcrequest_async('AsymmetricVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CancelKeyDeletionResponse().from_map(
            self.do_rpcrequest('CancelKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_key_deletion_with_options_async(
        self,
        request: kms_20160120_models.CancelKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CancelKeyDeletionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CancelKeyDeletionResponse().from_map(
            await self.do_rpcrequest_async('CancelKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeyDecryptResponse().from_map(
            self.do_rpcrequest('CertificatePrivateKeyDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def certificate_private_key_decrypt_with_options_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeyDecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeyDecryptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeyDecryptResponse().from_map(
            await self.do_rpcrequest_async('CertificatePrivateKeyDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeySignResponse().from_map(
            self.do_rpcrequest('CertificatePrivateKeySign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def certificate_private_key_sign_with_options_async(
        self,
        request: kms_20160120_models.CertificatePrivateKeySignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePrivateKeySignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeySignResponse().from_map(
            await self.do_rpcrequest_async('CertificatePrivateKeySign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyEncryptResponse().from_map(
            self.do_rpcrequest('CertificatePublicKeyEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def certificate_public_key_encrypt_with_options_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyEncryptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyEncryptResponse().from_map(
            await self.do_rpcrequest_async('CertificatePublicKeyEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyVerifyResponse().from_map(
            self.do_rpcrequest('CertificatePublicKeyVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def certificate_public_key_verify_with_options_async(
        self,
        request: kms_20160120_models.CertificatePublicKeyVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CertificatePublicKeyVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyVerifyResponse().from_map(
            await self.do_rpcrequest_async('CertificatePublicKeyVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateAliasResponse().from_map(
            self.do_rpcrequest('CreateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        request: kms_20160120_models.CreateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateAliasResponse().from_map(
            await self.do_rpcrequest_async('CreateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateCertificateResponse().from_map(
            self.do_rpcrequest('CreateCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateCertificateResponse().from_map(
            await self.do_rpcrequest_async('CreateCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyResponse().from_map(
            self.do_rpcrequest('CreateKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_key_with_options_async(
        self,
        request: kms_20160120_models.CreateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyResponse().from_map(
            await self.do_rpcrequest_async('CreateKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyVersionResponse().from_map(
            self.do_rpcrequest('CreateKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_key_version_with_options_async(
        self,
        request: kms_20160120_models.CreateKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.CreateKeyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyVersionResponse().from_map(
            await self.do_rpcrequest_async('CreateKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateSecretResponse().from_map(
            self.do_rpcrequest('CreateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateSecretResponse().from_map(
            await self.do_rpcrequest_async('CreateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DecryptResponse().from_map(
            self.do_rpcrequest('Decrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DecryptResponse().from_map(
            await self.do_rpcrequest_async('Decrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteAliasResponse().from_map(
            self.do_rpcrequest('DeleteAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        request: kms_20160120_models.DeleteAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteAliasResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteCertificateResponse().from_map(
            self.do_rpcrequest('DeleteCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_certificate_with_options_async(
        self,
        request: kms_20160120_models.DeleteCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteCertificateResponse().from_map(
            await self.do_rpcrequest_async('DeleteCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteKeyMaterialResponse().from_map(
            self.do_rpcrequest('DeleteKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_key_material_with_options_async(
        self,
        request: kms_20160120_models.DeleteKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteKeyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteKeyMaterialResponse().from_map(
            await self.do_rpcrequest_async('DeleteKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteSecretResponse().from_map(
            self.do_rpcrequest('DeleteSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: kms_20160120_models.DeleteSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DeleteSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteSecretResponse().from_map(
            await self.do_rpcrequest_async('DeleteSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return kms_20160120_models.DescribeAccountKmsStatusResponse().from_map(
            self.do_rpcrequest('DescribeAccountKmsStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_account_kms_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeAccountKmsStatusResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeAccountKmsStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccountKmsStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeCertificateResponse().from_map(
            self.do_rpcrequest('DescribeCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_certificate_with_options_async(
        self,
        request: kms_20160120_models.DescribeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeCertificateResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyResponse().from_map(
            self.do_rpcrequest('DescribeKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_key_with_options_async(
        self,
        request: kms_20160120_models.DescribeKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyResponse().from_map(
            await self.do_rpcrequest_async('DescribeKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyVersionResponse().from_map(
            self.do_rpcrequest('DescribeKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_key_version_with_options_async(
        self,
        request: kms_20160120_models.DescribeKeyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeKeyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return kms_20160120_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeSecretResponse().from_map(
            self.do_rpcrequest('DescribeSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: kms_20160120_models.DescribeSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeSecretResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeServiceResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeServiceResponse().from_map(
            self.do_rpcrequest('DescribeService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DescribeServiceResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service(self) -> kms_20160120_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_with_options(runtime)

    async def describe_service_async(self) -> kms_20160120_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_with_options_async(runtime)

    def disable_key_with_options(
        self,
        request: kms_20160120_models.DisableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DisableKeyResponse().from_map(
            self.do_rpcrequest('DisableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_key_with_options_async(
        self,
        request: kms_20160120_models.DisableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.DisableKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DisableKeyResponse().from_map(
            await self.do_rpcrequest_async('DisableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EnableKeyResponse().from_map(
            self.do_rpcrequest('EnableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_key_with_options_async(
        self,
        request: kms_20160120_models.EnableKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.EnableKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EnableKeyResponse().from_map(
            await self.do_rpcrequest_async('EnableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EncryptResponse().from_map(
            self.do_rpcrequest('Encrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EncryptResponse().from_map(
            await self.do_rpcrequest_async('Encrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def export_certificate_with_options(
        self,
        request: kms_20160120_models.ExportCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportCertificateResponse().from_map(
            self.do_rpcrequest('ExportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_certificate_with_options_async(
        self,
        request: kms_20160120_models.ExportCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ExportCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportCertificateResponse().from_map(
            await self.do_rpcrequest_async('ExportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_certificate(
        self,
        request: kms_20160120_models.ExportCertificateRequest,
    ) -> kms_20160120_models.ExportCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_certificate_with_options(request, runtime)

    async def export_certificate_async(
        self,
        request: kms_20160120_models.ExportCertificateRequest,
    ) -> kms_20160120_models.ExportCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_certificate_with_options_async(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportDataKeyResponse().from_map(
            self.do_rpcrequest('ExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportDataKeyResponse().from_map(
            await self.do_rpcrequest_async('ExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateAndExportDataKeyResponse().from_map(
            self.do_rpcrequest('GenerateAndExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateAndExportDataKeyResponse().from_map(
            await self.do_rpcrequest_async('GenerateAndExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyResponse().from_map(
            self.do_rpcrequest('GenerateDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyResponse().from_map(
            await self.do_rpcrequest_async('GenerateDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse().from_map(
            self.do_rpcrequest('GenerateDataKeyWithoutPlaintext', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse().from_map(
            await self.do_rpcrequest_async('GenerateDataKeyWithoutPlaintext', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetCertificateResponse().from_map(
            self.do_rpcrequest('GetCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_certificate_with_options_async(
        self,
        request: kms_20160120_models.GetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetCertificateResponse().from_map(
            await self.do_rpcrequest_async('GetCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetParametersForImportResponse().from_map(
            self.do_rpcrequest('GetParametersForImport', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_parameters_for_import_with_options_async(
        self,
        request: kms_20160120_models.GetParametersForImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetParametersForImportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetParametersForImportResponse().from_map(
            await self.do_rpcrequest_async('GetParametersForImport', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetPublicKeyResponse().from_map(
            self.do_rpcrequest('GetPublicKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_public_key_with_options_async(
        self,
        request: kms_20160120_models.GetPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetPublicKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetPublicKeyResponse().from_map(
            await self.do_rpcrequest_async('GetPublicKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetRandomPasswordResponse().from_map(
            self.do_rpcrequest('GetRandomPassword', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_random_password_with_options_async(
        self,
        request: kms_20160120_models.GetRandomPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetRandomPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetRandomPasswordResponse().from_map(
            await self.do_rpcrequest_async('GetRandomPassword', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetSecretValueResponse().from_map(
            self.do_rpcrequest('GetSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_secret_value_with_options_async(
        self,
        request: kms_20160120_models.GetSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.GetSecretValueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetSecretValueResponse().from_map(
            await self.do_rpcrequest_async('GetSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def import_certificate_with_options(
        self,
        request: kms_20160120_models.ImportCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportCertificateResponse().from_map(
            self.do_rpcrequest('ImportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_certificate_with_options_async(
        self,
        request: kms_20160120_models.ImportCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportCertificateResponse().from_map(
            await self.do_rpcrequest_async('ImportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_certificate(
        self,
        request: kms_20160120_models.ImportCertificateRequest,
    ) -> kms_20160120_models.ImportCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_certificate_with_options(request, runtime)

    async def import_certificate_async(
        self,
        request: kms_20160120_models.ImportCertificateRequest,
    ) -> kms_20160120_models.ImportCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_certificate_with_options_async(request, runtime)

    def import_encryption_certificate_with_options(
        self,
        request: kms_20160120_models.ImportEncryptionCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportEncryptionCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportEncryptionCertificateResponse().from_map(
            self.do_rpcrequest('ImportEncryptionCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_encryption_certificate_with_options_async(
        self,
        request: kms_20160120_models.ImportEncryptionCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportEncryptionCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportEncryptionCertificateResponse().from_map(
            await self.do_rpcrequest_async('ImportEncryptionCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_encryption_certificate(
        self,
        request: kms_20160120_models.ImportEncryptionCertificateRequest,
    ) -> kms_20160120_models.ImportEncryptionCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_encryption_certificate_with_options(request, runtime)

    async def import_encryption_certificate_async(
        self,
        request: kms_20160120_models.ImportEncryptionCertificateRequest,
    ) -> kms_20160120_models.ImportEncryptionCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_encryption_certificate_with_options_async(request, runtime)

    def import_key_material_with_options(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportKeyMaterialResponse().from_map(
            self.do_rpcrequest('ImportKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_key_material_with_options_async(
        self,
        request: kms_20160120_models.ImportKeyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ImportKeyMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportKeyMaterialResponse().from_map(
            await self.do_rpcrequest_async('ImportKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesResponse().from_map(
            self.do_rpcrequest('ListAliases', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        request: kms_20160120_models.ListAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesResponse().from_map(
            await self.do_rpcrequest_async('ListAliases', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesByKeyIdResponse().from_map(
            self.do_rpcrequest('ListAliasesByKeyId', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aliases_by_key_id_with_options_async(
        self,
        request: kms_20160120_models.ListAliasesByKeyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListAliasesByKeyIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesByKeyIdResponse().from_map(
            await self.do_rpcrequest_async('ListAliasesByKeyId', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_certificates_with_options(
        self,
        request: kms_20160120_models.ListCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListCertificatesResponse().from_map(
            self.do_rpcrequest('ListCertificates', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_certificates_with_options_async(
        self,
        request: kms_20160120_models.ListCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListCertificatesResponse().from_map(
            await self.do_rpcrequest_async('ListCertificates', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_certificates(
        self,
        request: kms_20160120_models.ListCertificatesRequest,
    ) -> kms_20160120_models.ListCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_certificates_with_options(request, runtime)

    async def list_certificates_async(
        self,
        request: kms_20160120_models.ListCertificatesRequest,
    ) -> kms_20160120_models.ListCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_certificates_with_options_async(request, runtime)

    def list_keys_with_options(
        self,
        request: kms_20160120_models.ListKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeysResponse().from_map(
            self.do_rpcrequest('ListKeys', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_keys_with_options_async(
        self,
        request: kms_20160120_models.ListKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeysResponse().from_map(
            await self.do_rpcrequest_async('ListKeys', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_key_versions_with_options(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeyVersionsResponse().from_map(
            self.do_rpcrequest('ListKeyVersions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_key_versions_with_options_async(
        self,
        request: kms_20160120_models.ListKeyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListKeyVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeyVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListKeyVersions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_resource_tags_with_options(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListResourceTagsResponse().from_map(
            self.do_rpcrequest('ListResourceTags', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_tags_with_options_async(
        self,
        request: kms_20160120_models.ListResourceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListResourceTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListResourceTagsResponse().from_map(
            await self.do_rpcrequest_async('ListResourceTags', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_secrets_with_options(
        self,
        request: kms_20160120_models.ListSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretsResponse().from_map(
            self.do_rpcrequest('ListSecrets', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: kms_20160120_models.ListSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretsResponse().from_map(
            await self.do_rpcrequest_async('ListSecrets', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_secret_version_ids_with_options(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretVersionIdsResponse().from_map(
            self.do_rpcrequest('ListSecretVersionIds', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_secret_version_ids_with_options_async(
        self,
        request: kms_20160120_models.ListSecretVersionIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ListSecretVersionIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretVersionIdsResponse().from_map(
            await self.do_rpcrequest_async('ListSecretVersionIds', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def open_kms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.OpenKmsServiceResponse().from_map(
            self.do_rpcrequest('OpenKmsService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_kms_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.OpenKmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.OpenKmsServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenKmsService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.PutSecretValueResponse().from_map(
            self.do_rpcrequest('PutSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_secret_value_with_options_async(
        self,
        request: kms_20160120_models.PutSecretValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.PutSecretValueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.PutSecretValueResponse().from_map(
            await self.do_rpcrequest_async('PutSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ReEncryptResponse().from_map(
            self.do_rpcrequest('ReEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_encrypt_with_options_async(
        self,
        tmp_req: kms_20160120_models.ReEncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ReEncryptResponse:
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ReEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ReEncryptResponse().from_map(
            await self.do_rpcrequest_async('ReEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RestoreSecretResponse().from_map(
            self.do_rpcrequest('RestoreSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_secret_with_options_async(
        self,
        request: kms_20160120_models.RestoreSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RestoreSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RestoreSecretResponse().from_map(
            await self.do_rpcrequest_async('RestoreSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RotateSecretResponse().from_map(
            self.do_rpcrequest('RotateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rotate_secret_with_options_async(
        self,
        request: kms_20160120_models.RotateSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.RotateSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RotateSecretResponse().from_map(
            await self.do_rpcrequest_async('RotateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ScheduleKeyDeletionResponse().from_map(
            self.do_rpcrequest('ScheduleKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def schedule_key_deletion_with_options_async(
        self,
        request: kms_20160120_models.ScheduleKeyDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.ScheduleKeyDeletionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ScheduleKeyDeletionResponse().from_map(
            await self.do_rpcrequest_async('ScheduleKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def tag_resource_with_options(
        self,
        request: kms_20160120_models.TagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.TagResourceResponse().from_map(
            self.do_rpcrequest('TagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resource_with_options_async(
        self,
        request: kms_20160120_models.TagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.TagResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.TagResourceResponse().from_map(
            await self.do_rpcrequest_async('TagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UntagResourceResponse().from_map(
            self.do_rpcrequest('UntagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resource_with_options_async(
        self,
        request: kms_20160120_models.UntagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UntagResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UntagResourceResponse().from_map(
            await self.do_rpcrequest_async('UntagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateAliasResponse().from_map(
            self.do_rpcrequest('UpdateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        request: kms_20160120_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateAliasResponse().from_map(
            await self.do_rpcrequest_async('UpdateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateCertificateStatusResponse().from_map(
            self.do_rpcrequest('UpdateCertificateStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_certificate_status_with_options_async(
        self,
        request: kms_20160120_models.UpdateCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateCertificateStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateCertificateStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateCertificateStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateKeyDescriptionResponse().from_map(
            self.do_rpcrequest('UpdateKeyDescription', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_key_description_with_options_async(
        self,
        request: kms_20160120_models.UpdateKeyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateKeyDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateKeyDescriptionResponse().from_map(
            await self.do_rpcrequest_async('UpdateKeyDescription', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateRotationPolicyResponse().from_map(
            self.do_rpcrequest('UpdateRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rotation_policy_with_options_async(
        self,
        request: kms_20160120_models.UpdateRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateRotationPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateRotationPolicyResponse().from_map(
            await self.do_rpcrequest_async('UpdateRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_secret_rotation_policy_with_options(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretRotationPolicyResponse().from_map(
            self.do_rpcrequest('UpdateSecretRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_secret_rotation_policy_with_options_async(
        self,
        request: kms_20160120_models.UpdateSecretRotationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretRotationPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretRotationPolicyResponse().from_map(
            await self.do_rpcrequest_async('UpdateSecretRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretVersionStageResponse().from_map(
            self.do_rpcrequest('UpdateSecretVersionStage', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_secret_version_stage_with_options_async(
        self,
        request: kms_20160120_models.UpdateSecretVersionStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UpdateSecretVersionStageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretVersionStageResponse().from_map(
            await self.do_rpcrequest_async('UpdateSecretVersionStage', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UploadCertificateResponse().from_map(
            self.do_rpcrequest('UploadCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_certificate_with_options_async(
        self,
        request: kms_20160120_models.UploadCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> kms_20160120_models.UploadCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UploadCertificateResponse().from_map(
            await self.do_rpcrequest_async('UploadCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
