# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
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
        self._endpoint = self.get_endpoint('ocr-api', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def recognize_driving_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            self.do_rpcrequest('RecognizeDrivingLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_driving_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeDrivingLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_driving_license(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_driving_license_with_options(request, runtime)

    async def recognize_driving_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_driving_license_with_options_async(request, runtime)

    def recognize_korean_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            self.do_rpcrequest('RecognizeKorean', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_korean_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            await self.do_rpcrequest_async('RecognizeKorean', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_korean(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_korean_with_options(request, runtime)

    async def recognize_korean_async(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_korean_with_options_async(request, runtime)

    def recognize_car_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            self.do_rpcrequest('RecognizeCarInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_car_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            await self.do_rpcrequest_async('RecognizeCarInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_invoice_with_options(request, runtime)

    async def recognize_car_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_invoice_with_options_async(request, runtime)

    def recognize_mixed_invoices_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            self.do_rpcrequest('RecognizeMixedInvoices', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_mixed_invoices_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            await self.do_rpcrequest_async('RecognizeMixedInvoices', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_mixed_invoices(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_invoices_with_options(request, runtime)

    async def recognize_mixed_invoices_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_mixed_invoices_with_options_async(request, runtime)

    def recognize_estate_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            self.do_rpcrequest('RecognizeEstateCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_estate_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            await self.do_rpcrequest_async('RecognizeEstateCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_estate_certification(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_estate_certification_with_options(request, runtime)

    async def recognize_estate_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_estate_certification_with_options_async(request, runtime)

    def recognize_car_number_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            self.do_rpcrequest('RecognizeCarNumber', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_car_number_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            await self.do_rpcrequest_async('RecognizeCarNumber', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_number(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_number_with_options(request, runtime)

    async def recognize_car_number_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_number_with_options_async(request, runtime)

    def recognize_edu_paper_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            self.do_rpcrequest('RecognizeEduPaperOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_paper_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            await self.do_rpcrequest_async('RecognizeEduPaperOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_ocr(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_ocr_with_options(request, runtime)

    async def recognize_edu_paper_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_ocr_with_options_async(request, runtime)

    def recognize_trade_mark_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            self.do_rpcrequest('RecognizeTradeMarkCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_trade_mark_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            await self.do_rpcrequest_async('RecognizeTradeMarkCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_trade_mark_certification(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_trade_mark_certification_with_options(request, runtime)

    async def recognize_trade_mark_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_trade_mark_certification_with_options_async(request, runtime)

    def recognize_birth_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            self.do_rpcrequest('RecognizeBirthCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_birth_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            await self.do_rpcrequest_async('RecognizeBirthCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_birth_certification(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_birth_certification_with_options(request, runtime)

    async def recognize_birth_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_birth_certification_with_options_async(request, runtime)

    def recognize_doctype_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDoctypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDoctypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDoctypeResponse(),
            self.do_rpcrequest('RecognizeDoctype', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_doctype_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeDoctypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDoctypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDoctypeResponse(),
            await self.do_rpcrequest_async('RecognizeDoctype', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_doctype(
        self,
        request: ocr_api_20210707_models.RecognizeDoctypeRequest,
    ) -> ocr_api_20210707_models.RecognizeDoctypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_doctype_with_options(request, runtime)

    async def recognize_doctype_async(
        self,
        request: ocr_api_20210707_models.RecognizeDoctypeRequest,
    ) -> ocr_api_20210707_models.RecognizeDoctypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_doctype_with_options_async(request, runtime)

    def recognize_bank_account_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            self.do_rpcrequest('RecognizeBankAccountLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_bank_account_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeBankAccountLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_bank_account_license(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_account_license_with_options(request, runtime)

    async def recognize_bank_account_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_account_license_with_options_async(request, runtime)

    def recognize_food_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            self.do_rpcrequest('RecognizeFoodManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_food_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeFoodManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_food_manage_license(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_manage_license_with_options(request, runtime)

    async def recognize_food_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_food_manage_license_with_options_async(request, runtime)

    def recognize_roll_ticket_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            self.do_rpcrequest('RecognizeRollTicket', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_roll_ticket_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            await self.do_rpcrequest_async('RecognizeRollTicket', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_roll_ticket(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_roll_ticket_with_options(request, runtime)

    async def recognize_roll_ticket_async(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_roll_ticket_with_options_async(request, runtime)

    def recognize_edu_formula_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            self.do_rpcrequest('RecognizeEduFormula', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_formula_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            await self.do_rpcrequest_async('RecognizeEduFormula', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_formula(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_formula_with_options(request, runtime)

    async def recognize_edu_formula_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_formula_with_options_async(request, runtime)

    def recognize_passport_with_options(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            self.do_rpcrequest('RecognizePassport', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_passport_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            await self.do_rpcrequest_async('RecognizePassport', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_passport(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_passport_with_options(request, runtime)

    async def recognize_passport_async(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_passport_with_options_async(request, runtime)

    def recognize_taxi_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            self.do_rpcrequest('RecognizeTaxiInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_taxi_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            await self.do_rpcrequest_async('RecognizeTaxiInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_taxi_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_taxi_invoice_with_options(request, runtime)

    async def recognize_taxi_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_taxi_invoice_with_options_async(request, runtime)

    def recognize_food_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            self.do_rpcrequest('RecognizeFoodProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_food_produce_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeFoodProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_food_produce_license(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_produce_license_with_options(request, runtime)

    async def recognize_food_produce_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_food_produce_license_with_options_async(request, runtime)

    def recognize_medical_device_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            self.do_rpcrequest('RecognizeMedicalDeviceProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_medical_device_produce_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeMedicalDeviceProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_medical_device_produce_license(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_produce_license_with_options(request, runtime)

    async def recognize_medical_device_produce_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_medical_device_produce_license_with_options_async(request, runtime)

    def recognize_handwriting_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            self.do_rpcrequest('RecognizeHandwriting', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_handwriting_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            await self.do_rpcrequest_async('RecognizeHandwriting', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_handwriting(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_handwriting_with_options(request, runtime)

    async def recognize_handwriting_async(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_handwriting_with_options_async(request, runtime)

    def recognize_air_itinerary_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            self.do_rpcrequest('RecognizeAirItinerary', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_air_itinerary_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            await self.do_rpcrequest_async('RecognizeAirItinerary', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_air_itinerary(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_air_itinerary_with_options(request, runtime)

    async def recognize_air_itinerary_async(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_air_itinerary_with_options_async(request, runtime)

    def recognize_janpanese_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            self.do_rpcrequest('RecognizeJanpanese', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_janpanese_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            await self.do_rpcrequest_async('RecognizeJanpanese', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_janpanese(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_janpanese_with_options(request, runtime)

    async def recognize_janpanese_async(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_janpanese_with_options_async(request, runtime)

    def recognize_ctwo_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            self.do_rpcrequest('RecognizeCtwoMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_ctwo_medical_device_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeCtwoMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_ctwo_medical_device_manage_license(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_ctwo_medical_device_manage_license_with_options(request, runtime)

    async def recognize_ctwo_medical_device_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_ctwo_medical_device_manage_license_with_options_async(request, runtime)

    def recognize_thai_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            self.do_rpcrequest('RecognizeThai', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_thai_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            await self.do_rpcrequest_async('RecognizeThai', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_thai(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_thai_with_options(request, runtime)

    async def recognize_thai_async(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_thai_with_options_async(request, runtime)

    def recognize_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            self.do_rpcrequest('RecognizeMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_medical_device_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_medical_device_manage_license(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_manage_license_with_options(request, runtime)

    async def recognize_medical_device_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_medical_device_manage_license_with_options_async(request, runtime)

    def recognize_latin_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            self.do_rpcrequest('RecognizeLatin', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_latin_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            await self.do_rpcrequest_async('RecognizeLatin', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_latin(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_latin_with_options(request, runtime)

    async def recognize_latin_async(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_latin_with_options_async(request, runtime)

    def recognize_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            self.do_rpcrequest('RecognizeInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            await self.do_rpcrequest_async('RecognizeInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_invoice_with_options(request, runtime)

    async def recognize_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_invoice_with_options_async(request, runtime)

    def recognize_mixed_cards_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMixedCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedCardsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedCardsResponse(),
            self.do_rpcrequest('RecognizeMixedCards', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_mixed_cards_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedCardsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedCardsResponse(),
            await self.do_rpcrequest_async('RecognizeMixedCards', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_mixed_cards(
        self,
        request: ocr_api_20210707_models.RecognizeMixedCardsRequest,
    ) -> ocr_api_20210707_models.RecognizeMixedCardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_cards_with_options(request, runtime)

    async def recognize_mixed_cards_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedCardsRequest,
    ) -> ocr_api_20210707_models.RecognizeMixedCardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_mixed_cards_with_options_async(request, runtime)

    def recognize_waybill_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            self.do_rpcrequest('RecognizeWaybill', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_waybill_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            await self.do_rpcrequest_async('RecognizeWaybill', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_waybill(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_waybill_with_options(request, runtime)

    async def recognize_waybill_async(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_waybill_with_options_async(request, runtime)

    def recognize_car_vin_code_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            self.do_rpcrequest('RecognizeCarVinCode', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_car_vin_code_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            await self.do_rpcrequest_async('RecognizeCarVinCode', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_vin_code(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_vin_code_with_options(request, runtime)

    async def recognize_car_vin_code_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_vin_code_with_options_async(request, runtime)

    def recognize_advanced_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            self.do_rpcrequest('RecognizeAdvanced', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_advanced_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            await self.do_rpcrequest_async('RecognizeAdvanced', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_advanced(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_advanced_with_options(request, runtime)

    async def recognize_advanced_async(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_advanced_with_options_async(request, runtime)

    def recognize_vehicle_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            self.do_rpcrequest('RecognizeVehicleLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_vehicle_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeVehicleLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_license(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_license_with_options(request, runtime)

    async def recognize_vehicle_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_license_with_options_async(request, runtime)

    def recognize_russian_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            self.do_rpcrequest('RecognizeRussian', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_russian_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            await self.do_rpcrequest_async('RecognizeRussian', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_russian(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_russian_with_options(request, runtime)

    async def recognize_russian_async(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_russian_with_options_async(request, runtime)

    def recognize_basic_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            self.do_rpcrequest('RecognizeBasic', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_basic_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            await self.do_rpcrequest_async('RecognizeBasic', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_basic(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_basic_with_options(request, runtime)

    async def recognize_basic_async(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_basic_with_options_async(request, runtime)

    def recognize_business_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            self.do_rpcrequest('RecognizeBusinessLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_business_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            await self.do_rpcrequest_async('RecognizeBusinessLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_business_license(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_business_license_with_options(request, runtime)

    async def recognize_business_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_business_license_with_options_async(request, runtime)

    def recognize_bank_card_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            self.do_rpcrequest('RecognizeBankCard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_bank_card_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            await self.do_rpcrequest_async('RecognizeBankCard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_bank_card(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_card_with_options(request, runtime)

    async def recognize_bank_card_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_card_with_options_async(request, runtime)

    def recognize_edu_paper_cut_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            self.do_rpcrequest('RecognizeEduPaperCut', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_paper_cut_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            await self.do_rpcrequest_async('RecognizeEduPaperCut', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_cut(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_cut_with_options(request, runtime)

    async def recognize_edu_paper_cut_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_cut_with_options_async(request, runtime)

    def recognize_household_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            self.do_rpcrequest('RecognizeHousehold', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_household_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            await self.do_rpcrequest_async('RecognizeHousehold', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_household(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_household_with_options(request, runtime)

    async def recognize_household_async(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_household_with_options_async(request, runtime)

    def recognize_edu_question_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            self.do_rpcrequest('RecognizeEduQuestionOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_question_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            await self.do_rpcrequest_async('RecognizeEduQuestionOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_question_ocr(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_question_ocr_with_options(request, runtime)

    async def recognize_edu_question_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_question_ocr_with_options_async(request, runtime)

    def recognize_train_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            self.do_rpcrequest('RecognizeTrainInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_train_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            await self.do_rpcrequest_async('RecognizeTrainInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_train_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_train_invoice_with_options(request, runtime)

    async def recognize_train_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_train_invoice_with_options_async(request, runtime)

    def recognize_table_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            self.do_rpcrequest('RecognizeTableOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_table_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            await self.do_rpcrequest_async('RecognizeTableOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_table_ocr(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_table_ocr_with_options(request, runtime)

    async def recognize_table_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_table_ocr_with_options_async(request, runtime)

    def recognize_english_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            self.do_rpcrequest('RecognizeEnglish', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_english_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            await self.do_rpcrequest_async('RecognizeEnglish', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_english(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_english_with_options(request, runtime)

    async def recognize_english_async(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_english_with_options_async(request, runtime)

    def recognize_multi_language_with_options(
        self,
        tmp_req: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeMultiLanguageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.languages):
            request.languages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.languages, 'Languages', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            self.do_rpcrequest('RecognizeMultiLanguage', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_multi_language_with_options_async(
        self,
        tmp_req: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeMultiLanguageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.languages):
            request.languages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.languages, 'Languages', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            await self.do_rpcrequest_async('RecognizeMultiLanguage', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_multi_language(
        self,
        request: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_multi_language_with_options(request, runtime)

    async def recognize_multi_language_async(
        self,
        request: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_multi_language_with_options_async(request, runtime)

    def recognize_edu_oral_calculation_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            self.do_rpcrequest('RecognizeEduOralCalculation', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_oral_calculation_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            await self.do_rpcrequest_async('RecognizeEduOralCalculation', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_oral_calculation(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_oral_calculation_with_options(request, runtime)

    async def recognize_edu_oral_calculation_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_oral_calculation_with_options_async(request, runtime)

    def recognize_quota_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            self.do_rpcrequest('RecognizeQuotaInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_quota_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            await self.do_rpcrequest_async('RecognizeQuotaInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_quota_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_quota_invoice_with_options(request, runtime)

    async def recognize_quota_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_quota_invoice_with_options_async(request, runtime)

    def recognize_general_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            self.do_rpcrequest('RecognizeGeneral', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_general_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            await self.do_rpcrequest_async('RecognizeGeneral', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_general(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_general_with_options(request, runtime)

    async def recognize_general_async(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_general_with_options_async(request, runtime)

    def recognize_edu_paper_structed_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            self.do_rpcrequest('RecognizeEduPaperStructed', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_edu_paper_structed_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            await self.do_rpcrequest_async('RecognizeEduPaperStructed', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_structed(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_structed_with_options(request, runtime)

    async def recognize_edu_paper_structed_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_structed_with_options_async(request, runtime)

    def recognize_idcard_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            self.do_rpcrequest('RecognizeIdcard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def recognize_idcard_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            await self.do_rpcrequest_async('RecognizeIdcard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_idcard(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_idcard_with_options(request, runtime)

    async def recognize_idcard_async(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_idcard_with_options_async(request, runtime)
