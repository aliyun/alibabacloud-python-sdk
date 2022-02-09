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

    def recognize_advanced_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.no_stamp):
            query['NoStamp'] = request.no_stamp
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAdvanced',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_advanced_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.no_stamp):
            query['NoStamp'] = request.no_stamp
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAdvanced',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_air_itinerary_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAirItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_air_itinerary_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAirItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_bank_account_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankAccountLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_bank_account_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankAccountLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_bank_card_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_bank_card_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_basic_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBasic',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_basic_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBasic',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_batch_recognize_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBatchRecognizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBatchRecognizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_op):
            query['ImageOp'] = request.image_op
        if not UtilClient.is_unset(request.image_oss_key):
            query['ImageOssKey'] = request.image_oss_key
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeBatchRecognize',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBatchRecognizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_batch_recognize_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBatchRecognizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBatchRecognizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_op):
            query['ImageOp'] = request.image_op
        if not UtilClient.is_unset(request.image_oss_key):
            query['ImageOssKey'] = request.image_oss_key
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeBatchRecognize',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBatchRecognizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_batch_recognize(
        self,
        request: ocr_api_20210707_models.RecognizeBatchRecognizeRequest,
    ) -> ocr_api_20210707_models.RecognizeBatchRecognizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_batch_recognize_with_options(request, runtime)

    async def recognize_batch_recognize_async(
        self,
        request: ocr_api_20210707_models.RecognizeBatchRecognizeRequest,
    ) -> ocr_api_20210707_models.RecognizeBatchRecognizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_batch_recognize_with_options_async(request, runtime)

    def recognize_birth_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBirthCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_birth_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBirthCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_bus_ship_ticket_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusShipTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusShipTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_bus_ship_ticket_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusShipTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusShipTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_bus_ship_ticket(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_bus_ship_ticket_with_options(request, runtime)

    async def recognize_bus_ship_ticket_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bus_ship_ticket_with_options_async(request, runtime)

    def recognize_business_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusinessLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_business_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusinessLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_car_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_car_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_car_number_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarNumber',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_car_number_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarNumber',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_car_vin_code_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarVinCode',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_car_vin_code_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarVinCode',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_chinese_passport_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeChinesePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeChinesePassportResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_chinese_passport_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeChinesePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeChinesePassportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_chinese_passport(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_chinese_passport_with_options(request, runtime)

    async def recognize_chinese_passport_async(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_chinese_passport_with_options_async(request, runtime)

    def recognize_common_printed_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCommonPrintedInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_common_printed_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCommonPrintedInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_common_printed_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_common_printed_invoice_with_options(request, runtime)

    async def recognize_common_printed_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_common_printed_invoice_with_options_async(request, runtime)

    def recognize_ctwo_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCtwoMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_ctwo_medical_device_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCtwoMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_delete_excel_record_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDeleteExcelRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeDeleteExcelRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_delete_excel_record_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeDeleteExcelRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeDeleteExcelRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_delete_excel_record(
        self,
        request: ocr_api_20210707_models.RecognizeDeleteExcelRecordRequest,
    ) -> ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_delete_excel_record_with_options(request, runtime)

    async def recognize_delete_excel_record_async(
        self,
        request: ocr_api_20210707_models.RecognizeDeleteExcelRecordRequest,
    ) -> ocr_api_20210707_models.RecognizeDeleteExcelRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_delete_excel_record_with_options_async(request, runtime)

    def recognize_driving_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDrivingLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_driving_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDrivingLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_formula_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduFormula',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_formula_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduFormula',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_oral_calculation_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduOralCalculation',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_oral_calculation_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduOralCalculation',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_paper_cut_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cut_type):
            query['CutType'] = request.cut_type
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperCut',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_paper_cut_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cut_type):
            query['CutType'] = request.cut_type
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperCut',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_paper_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_paper_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_paper_structed_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperStructed',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_paper_structed_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperStructed',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_edu_question_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduQuestionOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_edu_question_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduQuestionOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_english_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEnglish',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_english_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEnglish',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_estate_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEstateCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_estate_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEstateCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_excel_export_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeExcelExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExcelExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.image_op):
            query['ImageOp'] = request.image_op
        if not UtilClient.is_unset(request.ocr_image_count):
            query['OcrImageCount'] = request.ocr_image_count
        if not UtilClient.is_unset(request.ocr_result):
            query['OcrResult'] = request.ocr_result
        if not UtilClient.is_unset(request.ocr_type):
            query['OcrType'] = request.ocr_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeExcelExport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExcelExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_excel_export_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeExcelExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExcelExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.image_op):
            query['ImageOp'] = request.image_op
        if not UtilClient.is_unset(request.ocr_image_count):
            query['OcrImageCount'] = request.ocr_image_count
        if not UtilClient.is_unset(request.ocr_result):
            query['OcrResult'] = request.ocr_result
        if not UtilClient.is_unset(request.ocr_type):
            query['OcrType'] = request.ocr_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeExcelExport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExcelExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_excel_export(
        self,
        request: ocr_api_20210707_models.RecognizeExcelExportRequest,
    ) -> ocr_api_20210707_models.RecognizeExcelExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_excel_export_with_options(request, runtime)

    async def recognize_excel_export_async(
        self,
        request: ocr_api_20210707_models.RecognizeExcelExportRequest,
    ) -> ocr_api_20210707_models.RecognizeExcelExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_excel_export_with_options_async(request, runtime)

    def recognize_excel_record_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeExcelRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExcelRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.curr_page):
            query['CurrPage'] = request.curr_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeExcelRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExcelRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_excel_record_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeExcelRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExcelRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.curr_page):
            query['CurrPage'] = request.curr_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeExcelRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExcelRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_excel_record(
        self,
        request: ocr_api_20210707_models.RecognizeExcelRecordRequest,
    ) -> ocr_api_20210707_models.RecognizeExcelRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_excel_record_with_options(request, runtime)

    async def recognize_excel_record_async(
        self,
        request: ocr_api_20210707_models.RecognizeExcelRecordRequest,
    ) -> ocr_api_20210707_models.RecognizeExcelRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_excel_record_with_options_async(request, runtime)

    def recognize_exit_entry_permit_to_hkwith_options(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToHK',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_exit_entry_permit_to_hkwith_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToHK',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_exit_entry_permit_to_hk(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_hkwith_options(request, runtime)

    async def recognize_exit_entry_permit_to_hk_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_exit_entry_permit_to_hkwith_options_async(request, runtime)

    def recognize_exit_entry_permit_to_mainland_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToMainland',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_exit_entry_permit_to_mainland_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToMainland',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_exit_entry_permit_to_mainland(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_mainland_with_options(request, runtime)

    async def recognize_exit_entry_permit_to_mainland_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_exit_entry_permit_to_mainland_with_options_async(request, runtime)

    def recognize_food_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_food_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_food_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_food_produce_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_general_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeGeneral',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_general_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeGeneral',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_handwriting_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHandwriting',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_handwriting_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHandwriting',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_household_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHousehold',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_household_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHousehold',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_idcard_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeIdcard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_idcard_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeIdcard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_janpanese_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeJanpanese',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_janpanese_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeJanpanese',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_korean_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeKorean',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_korean_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeKorean',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_latin_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeLatin',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_latin_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeLatin',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_medical_device_manage_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_medical_device_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_medical_device_produce_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_mixed_invoices_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMixedInvoices',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_mixed_invoices_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMixedInvoices',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.languages_shrink):
            query['Languages'] = request.languages_shrink
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMultiLanguage',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.languages_shrink):
            query['Languages'] = request.languages_shrink
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMultiLanguage',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_passport_with_options(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_passport_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_quota_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeQuotaInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_quota_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeQuotaInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_ride_hailing_itinerary_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRideHailingItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRideHailingItineraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_ride_hailing_itinerary_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRideHailingItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRideHailingItineraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_ride_hailing_itinerary(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_ride_hailing_itinerary_with_options(request, runtime)

    async def recognize_ride_hailing_itinerary_async(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_ride_hailing_itinerary_with_options_async(request, runtime)

    def recognize_roll_ticket_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRollTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_roll_ticket_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRollTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_russian_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRussian',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_russian_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRussian',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_social_security_card_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeSocialSecurityCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeSocialSecurityCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_social_security_card_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeSocialSecurityCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeSocialSecurityCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_social_security_card(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_social_security_card_with_options(request, runtime)

    async def recognize_social_security_card_async(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_social_security_card_with_options_async(request, runtime)

    def recognize_table_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.line_less):
            query['LineLess'] = request.line_less
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.skip_detection):
            query['SkipDetection'] = request.skip_detection
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTableOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_table_ocr_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.line_less):
            query['LineLess'] = request.line_less
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.skip_detection):
            query['SkipDetection'] = request.skip_detection
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTableOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_tax_clearance_certificate_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxClearanceCertificate',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_tax_clearance_certificate_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxClearanceCertificate',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_tax_clearance_certificate(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_tax_clearance_certificate_with_options(request, runtime)

    async def recognize_tax_clearance_certificate_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_tax_clearance_certificate_with_options_async(request, runtime)

    def recognize_taxi_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxiInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_taxi_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxiInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_thai_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeThai',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_thai_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeThai',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_toll_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTollInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTollInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_toll_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTollInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTollInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_toll_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_toll_invoice_with_options(request, runtime)

    async def recognize_toll_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_toll_invoice_with_options_async(request, runtime)

    def recognize_trade_mark_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTradeMarkCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_trade_mark_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTradeMarkCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_train_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTrainInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_train_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTrainInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_used_car_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeUsedCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_used_car_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeUsedCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_used_car_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_used_car_invoice_with_options(request, runtime)

    async def recognize_used_car_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_used_car_invoice_with_options_async(request, runtime)

    def recognize_vehicle_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_vehicle_certification_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleCertificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_vehicle_certification(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_certification_with_options(request, runtime)

    async def recognize_vehicle_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_certification_with_options_async(request, runtime)

    def recognize_vehicle_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_vehicle_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def recognize_vehicle_registration_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleRegistration',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_vehicle_registration_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleRegistration',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_vehicle_registration(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_registration_with_options(request, runtime)

    async def recognize_vehicle_registration_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_registration_with_options_async(request, runtime)

    def recognize_waybill_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeWaybill',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_waybill_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeWaybill',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            await self.call_api_async(params, req, runtime)
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
