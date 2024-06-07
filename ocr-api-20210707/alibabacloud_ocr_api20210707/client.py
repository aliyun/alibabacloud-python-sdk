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
        """
        @summary 全文识别高精版
        
        @param request: RecognizeAdvancedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAdvancedResponse
        """
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
        """
        @summary 全文识别高精版
        
        @param request: RecognizeAdvancedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAdvancedResponse
        """
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
        """
        @summary 全文识别高精版
        
        @param request: RecognizeAdvancedRequest
        @return: RecognizeAdvancedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_advanced_with_options(request, runtime)

    async def recognize_advanced_async(
        self,
        request: ocr_api_20210707_models.RecognizeAdvancedRequest,
    ) -> ocr_api_20210707_models.RecognizeAdvancedResponse:
        """
        @summary 全文识别高精版
        
        @param request: RecognizeAdvancedRequest
        @return: RecognizeAdvancedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_advanced_with_options_async(request, runtime)

    def recognize_air_itinerary_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        """
        @summary 航空行程单
        
        @param request: RecognizeAirItineraryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAirItineraryResponse
        """
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
        """
        @summary 航空行程单
        
        @param request: RecognizeAirItineraryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAirItineraryResponse
        """
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
        """
        @summary 航空行程单
        
        @param request: RecognizeAirItineraryRequest
        @return: RecognizeAirItineraryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_air_itinerary_with_options(request, runtime)

    async def recognize_air_itinerary_async(
        self,
        request: ocr_api_20210707_models.RecognizeAirItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeAirItineraryResponse:
        """
        @summary 航空行程单
        
        @param request: RecognizeAirItineraryRequest
        @return: RecognizeAirItineraryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_air_itinerary_with_options_async(request, runtime)

    def recognize_all_text_with_options(
        self,
        tmp_req: ocr_api_20210707_models.RecognizeAllTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAllTextResponse:
        """
        @summary 统一Api
        
        @param tmp_req: RecognizeAllTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAllTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeAllTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_config):
            request.advanced_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_config, 'AdvancedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.id_card_config):
            request.id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.id_card_config, 'IdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.international_business_license_config):
            request.international_business_license_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.international_business_license_config, 'InternationalBusinessLicenseConfig', 'json')
        if not UtilClient.is_unset(tmp_req.international_id_card_config):
            request.international_id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.international_id_card_config, 'InternationalIdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.multi_lan_config):
            request.multi_lan_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_lan_config, 'MultiLanConfig', 'json')
        if not UtilClient.is_unset(tmp_req.table_config):
            request.table_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_config, 'TableConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_config_shrink):
            query['AdvancedConfig'] = request.advanced_config_shrink
        if not UtilClient.is_unset(request.id_card_config_shrink):
            query['IdCardConfig'] = request.id_card_config_shrink
        if not UtilClient.is_unset(request.international_business_license_config_shrink):
            query['InternationalBusinessLicenseConfig'] = request.international_business_license_config_shrink
        if not UtilClient.is_unset(request.international_id_card_config_shrink):
            query['InternationalIdCardConfig'] = request.international_id_card_config_shrink
        if not UtilClient.is_unset(request.multi_lan_config_shrink):
            query['MultiLanConfig'] = request.multi_lan_config_shrink
        if not UtilClient.is_unset(request.output_bar_code):
            query['OutputBarCode'] = request.output_bar_code
        if not UtilClient.is_unset(request.output_coordinate):
            query['OutputCoordinate'] = request.output_coordinate
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_kvexcel):
            query['OutputKVExcel'] = request.output_kvexcel
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.output_qrcode):
            query['OutputQrcode'] = request.output_qrcode
        if not UtilClient.is_unset(request.output_stamp):
            query['OutputStamp'] = request.output_stamp
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.table_config_shrink):
            query['TableConfig'] = request.table_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=tmp_req.body
        )
        params = open_api_models.Params(
            action='RecognizeAllText',
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
            ocr_api_20210707_models.RecognizeAllTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_all_text_with_options_async(
        self,
        tmp_req: ocr_api_20210707_models.RecognizeAllTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeAllTextResponse:
        """
        @summary 统一Api
        
        @param tmp_req: RecognizeAllTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeAllTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeAllTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_config):
            request.advanced_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_config, 'AdvancedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.id_card_config):
            request.id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.id_card_config, 'IdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.international_business_license_config):
            request.international_business_license_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.international_business_license_config, 'InternationalBusinessLicenseConfig', 'json')
        if not UtilClient.is_unset(tmp_req.international_id_card_config):
            request.international_id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.international_id_card_config, 'InternationalIdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.multi_lan_config):
            request.multi_lan_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_lan_config, 'MultiLanConfig', 'json')
        if not UtilClient.is_unset(tmp_req.table_config):
            request.table_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_config, 'TableConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_config_shrink):
            query['AdvancedConfig'] = request.advanced_config_shrink
        if not UtilClient.is_unset(request.id_card_config_shrink):
            query['IdCardConfig'] = request.id_card_config_shrink
        if not UtilClient.is_unset(request.international_business_license_config_shrink):
            query['InternationalBusinessLicenseConfig'] = request.international_business_license_config_shrink
        if not UtilClient.is_unset(request.international_id_card_config_shrink):
            query['InternationalIdCardConfig'] = request.international_id_card_config_shrink
        if not UtilClient.is_unset(request.multi_lan_config_shrink):
            query['MultiLanConfig'] = request.multi_lan_config_shrink
        if not UtilClient.is_unset(request.output_bar_code):
            query['OutputBarCode'] = request.output_bar_code
        if not UtilClient.is_unset(request.output_coordinate):
            query['OutputCoordinate'] = request.output_coordinate
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_kvexcel):
            query['OutputKVExcel'] = request.output_kvexcel
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.output_qrcode):
            query['OutputQrcode'] = request.output_qrcode
        if not UtilClient.is_unset(request.output_stamp):
            query['OutputStamp'] = request.output_stamp
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.table_config_shrink):
            query['TableConfig'] = request.table_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=tmp_req.body
        )
        params = open_api_models.Params(
            action='RecognizeAllText',
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
            ocr_api_20210707_models.RecognizeAllTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_all_text(
        self,
        request: ocr_api_20210707_models.RecognizeAllTextRequest,
    ) -> ocr_api_20210707_models.RecognizeAllTextResponse:
        """
        @summary 统一Api
        
        @param request: RecognizeAllTextRequest
        @return: RecognizeAllTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_all_text_with_options(request, runtime)

    async def recognize_all_text_async(
        self,
        request: ocr_api_20210707_models.RecognizeAllTextRequest,
    ) -> ocr_api_20210707_models.RecognizeAllTextResponse:
        """
        @summary 统一Api
        
        @param request: RecognizeAllTextRequest
        @return: RecognizeAllTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_all_text_with_options_async(request, runtime)

    def recognize_bank_acceptance_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankAcceptanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAcceptanceResponse:
        """
        @summary 银承汇票识别
        
        @param request: RecognizeBankAcceptanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankAcceptanceResponse
        """
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
            action='RecognizeBankAcceptance',
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
            ocr_api_20210707_models.RecognizeBankAcceptanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_bank_acceptance_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAcceptanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAcceptanceResponse:
        """
        @summary 银承汇票识别
        
        @param request: RecognizeBankAcceptanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankAcceptanceResponse
        """
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
            action='RecognizeBankAcceptance',
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
            ocr_api_20210707_models.RecognizeBankAcceptanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_bank_acceptance(
        self,
        request: ocr_api_20210707_models.RecognizeBankAcceptanceRequest,
    ) -> ocr_api_20210707_models.RecognizeBankAcceptanceResponse:
        """
        @summary 银承汇票识别
        
        @param request: RecognizeBankAcceptanceRequest
        @return: RecognizeBankAcceptanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_acceptance_with_options(request, runtime)

    async def recognize_bank_acceptance_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAcceptanceRequest,
    ) -> ocr_api_20210707_models.RecognizeBankAcceptanceResponse:
        """
        @summary 银承汇票识别
        
        @param request: RecognizeBankAcceptanceRequest
        @return: RecognizeBankAcceptanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_acceptance_with_options_async(request, runtime)

    def recognize_bank_account_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        """
        @summary 银行开户许可证识别
        
        @param request: RecognizeBankAccountLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankAccountLicenseResponse
        """
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
        """
        @summary 银行开户许可证识别
        
        @param request: RecognizeBankAccountLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankAccountLicenseResponse
        """
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
        """
        @summary 银行开户许可证识别
        
        @param request: RecognizeBankAccountLicenseRequest
        @return: RecognizeBankAccountLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_account_license_with_options(request, runtime)

    async def recognize_bank_account_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankAccountLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBankAccountLicenseResponse:
        """
        @summary 银行开户许可证识别
        
        @param request: RecognizeBankAccountLicenseRequest
        @return: RecognizeBankAccountLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_account_license_with_options_async(request, runtime)

    def recognize_bank_card_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        """
        @summary 银行卡识别
        
        @param request: RecognizeBankCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankCardResponse
        """
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
        """
        @summary 银行卡识别
        
        @param request: RecognizeBankCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBankCardResponse
        """
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
        """
        @summary 银行卡识别
        
        @param request: RecognizeBankCardRequest
        @return: RecognizeBankCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_card_with_options(request, runtime)

    async def recognize_bank_card_async(
        self,
        request: ocr_api_20210707_models.RecognizeBankCardRequest,
    ) -> ocr_api_20210707_models.RecognizeBankCardResponse:
        """
        @summary 银行卡识别
        
        @param request: RecognizeBankCardRequest
        @return: RecognizeBankCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bank_card_with_options_async(request, runtime)

    def recognize_basic_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        """
        @summary 电商图片文字识别
        
        @param request: RecognizeBasicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBasicResponse
        """
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
        """
        @summary 电商图片文字识别
        
        @param request: RecognizeBasicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBasicResponse
        """
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
        """
        @summary 电商图片文字识别
        
        @param request: RecognizeBasicRequest
        @return: RecognizeBasicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_basic_with_options(request, runtime)

    async def recognize_basic_async(
        self,
        request: ocr_api_20210707_models.RecognizeBasicRequest,
    ) -> ocr_api_20210707_models.RecognizeBasicResponse:
        """
        @summary 电商图片文字识别
        
        @param request: RecognizeBasicRequest
        @return: RecognizeBasicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_basic_with_options_async(request, runtime)

    def recognize_birth_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        """
        @summary 出生证明
        
        @param request: RecognizeBirthCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBirthCertificationResponse
        """
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
        """
        @summary 出生证明
        
        @param request: RecognizeBirthCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBirthCertificationResponse
        """
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
        """
        @summary 出生证明
        
        @param request: RecognizeBirthCertificationRequest
        @return: RecognizeBirthCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_birth_certification_with_options(request, runtime)

    async def recognize_birth_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeBirthCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeBirthCertificationResponse:
        """
        @summary 出生证明
        
        @param request: RecognizeBirthCertificationRequest
        @return: RecognizeBirthCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_birth_certification_with_options_async(request, runtime)

    def recognize_bus_ship_ticket_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        """
        @summary 客运车船票识别
        
        @param request: RecognizeBusShipTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusShipTicketResponse
        """
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
        """
        @summary 客运车船票识别
        
        @param request: RecognizeBusShipTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusShipTicketResponse
        """
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
        """
        @summary 客运车船票识别
        
        @param request: RecognizeBusShipTicketRequest
        @return: RecognizeBusShipTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_bus_ship_ticket_with_options(request, runtime)

    async def recognize_bus_ship_ticket_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusShipTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeBusShipTicketResponse:
        """
        @summary 客运车船票识别
        
        @param request: RecognizeBusShipTicketRequest
        @return: RecognizeBusShipTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_bus_ship_ticket_with_options_async(request, runtime)

    def recognize_business_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        """
        @summary 营业执照识别
        
        @param request: RecognizeBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusinessLicenseResponse
        """
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
        """
        @summary 营业执照识别
        
        @param request: RecognizeBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeBusinessLicenseResponse
        """
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
        """
        @summary 营业执照识别
        
        @param request: RecognizeBusinessLicenseRequest
        @return: RecognizeBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_business_license_with_options(request, runtime)

    async def recognize_business_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeBusinessLicenseResponse:
        """
        @summary 营业执照识别
        
        @param request: RecognizeBusinessLicenseRequest
        @return: RecognizeBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_business_license_with_options_async(request, runtime)

    def recognize_car_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        """
        @summary 机动车销售发票
        
        @param request: RecognizeCarInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarInvoiceResponse
        """
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
        """
        @summary 机动车销售发票
        
        @param request: RecognizeCarInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarInvoiceResponse
        """
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
        """
        @summary 机动车销售发票
        
        @param request: RecognizeCarInvoiceRequest
        @return: RecognizeCarInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_invoice_with_options(request, runtime)

    async def recognize_car_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCarInvoiceResponse:
        """
        @summary 机动车销售发票
        
        @param request: RecognizeCarInvoiceRequest
        @return: RecognizeCarInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_invoice_with_options_async(request, runtime)

    def recognize_car_number_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        """
        @summary 车牌识别
        
        @param request: RecognizeCarNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarNumberResponse
        """
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
        """
        @summary 车牌识别
        
        @param request: RecognizeCarNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarNumberResponse
        """
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
        """
        @summary 车牌识别
        
        @param request: RecognizeCarNumberRequest
        @return: RecognizeCarNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_number_with_options(request, runtime)

    async def recognize_car_number_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarNumberRequest,
    ) -> ocr_api_20210707_models.RecognizeCarNumberResponse:
        """
        @summary 车牌识别
        
        @param request: RecognizeCarNumberRequest
        @return: RecognizeCarNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_number_with_options_async(request, runtime)

    def recognize_car_vin_code_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        """
        @summary 车辆vin码识别
        
        @param request: RecognizeCarVinCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarVinCodeResponse
        """
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
        """
        @summary 车辆vin码识别
        
        @param request: RecognizeCarVinCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCarVinCodeResponse
        """
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
        """
        @summary 车辆vin码识别
        
        @param request: RecognizeCarVinCodeRequest
        @return: RecognizeCarVinCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_vin_code_with_options(request, runtime)

    async def recognize_car_vin_code_async(
        self,
        request: ocr_api_20210707_models.RecognizeCarVinCodeRequest,
    ) -> ocr_api_20210707_models.RecognizeCarVinCodeResponse:
        """
        @summary 车辆vin码识别
        
        @param request: RecognizeCarVinCodeRequest
        @return: RecognizeCarVinCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_vin_code_with_options_async(request, runtime)

    def recognize_chinese_passport_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        """
        @summary 中国护照识别
        
        @param request: RecognizeChinesePassportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeChinesePassportResponse
        """
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
        """
        @summary 中国护照识别
        
        @param request: RecognizeChinesePassportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeChinesePassportResponse
        """
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
        """
        @summary 中国护照识别
        
        @param request: RecognizeChinesePassportRequest
        @return: RecognizeChinesePassportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_chinese_passport_with_options(request, runtime)

    async def recognize_chinese_passport_async(
        self,
        request: ocr_api_20210707_models.RecognizeChinesePassportRequest,
    ) -> ocr_api_20210707_models.RecognizeChinesePassportResponse:
        """
        @summary 中国护照识别
        
        @param request: RecognizeChinesePassportRequest
        @return: RecognizeChinesePassportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_chinese_passport_with_options_async(request, runtime)

    def recognize_common_printed_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        """
        @summary 通用机打发票识别
        
        @param request: RecognizeCommonPrintedInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCommonPrintedInvoiceResponse
        """
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
        """
        @summary 通用机打发票识别
        
        @param request: RecognizeCommonPrintedInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCommonPrintedInvoiceResponse
        """
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
        """
        @summary 通用机打发票识别
        
        @param request: RecognizeCommonPrintedInvoiceRequest
        @return: RecognizeCommonPrintedInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_common_printed_invoice_with_options(request, runtime)

    async def recognize_common_printed_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeCommonPrintedInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse:
        """
        @summary 通用机打发票识别
        
        @param request: RecognizeCommonPrintedInvoiceRequest
        @return: RecognizeCommonPrintedInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_common_printed_invoice_with_options_async(request, runtime)

    def recognize_cosmetic_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCosmeticProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse:
        """
        @summary 化妆品生产许可证识别
        
        @param request: RecognizeCosmeticProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCosmeticProduceLicenseResponse
        """
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
            action='RecognizeCosmeticProduceLicense',
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
            ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_cosmetic_produce_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCosmeticProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse:
        """
        @summary 化妆品生产许可证识别
        
        @param request: RecognizeCosmeticProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCosmeticProduceLicenseResponse
        """
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
            action='RecognizeCosmeticProduceLicense',
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
            ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_cosmetic_produce_license(
        self,
        request: ocr_api_20210707_models.RecognizeCosmeticProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse:
        """
        @summary 化妆品生产许可证识别
        
        @param request: RecognizeCosmeticProduceLicenseRequest
        @return: RecognizeCosmeticProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_cosmetic_produce_license_with_options(request, runtime)

    async def recognize_cosmetic_produce_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeCosmeticProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse:
        """
        @summary 化妆品生产许可证识别
        
        @param request: RecognizeCosmeticProduceLicenseRequest
        @return: RecognizeCosmeticProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_cosmetic_produce_license_with_options_async(request, runtime)

    def recognize_covid_test_report_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCovidTestReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCovidTestReportResponse:
        """
        @summary 核算检测报告识别
        
        @param request: RecognizeCovidTestReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCovidTestReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.multiple_result):
            query['MultipleResult'] = request.multiple_result
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCovidTestReport',
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
            ocr_api_20210707_models.RecognizeCovidTestReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_covid_test_report_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeCovidTestReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCovidTestReportResponse:
        """
        @summary 核算检测报告识别
        
        @param request: RecognizeCovidTestReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCovidTestReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.multiple_result):
            query['MultipleResult'] = request.multiple_result
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCovidTestReport',
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
            ocr_api_20210707_models.RecognizeCovidTestReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_covid_test_report(
        self,
        request: ocr_api_20210707_models.RecognizeCovidTestReportRequest,
    ) -> ocr_api_20210707_models.RecognizeCovidTestReportResponse:
        """
        @summary 核算检测报告识别
        
        @param request: RecognizeCovidTestReportRequest
        @return: RecognizeCovidTestReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_covid_test_report_with_options(request, runtime)

    async def recognize_covid_test_report_async(
        self,
        request: ocr_api_20210707_models.RecognizeCovidTestReportRequest,
    ) -> ocr_api_20210707_models.RecognizeCovidTestReportResponse:
        """
        @summary 核算检测报告识别
        
        @param request: RecognizeCovidTestReportRequest
        @return: RecognizeCovidTestReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_covid_test_report_with_options_async(request, runtime)

    def recognize_ctwo_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        """
        @summary 第二类医疗器械经营备案凭证
        
        @param request: RecognizeCtwoMedicalDeviceManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCtwoMedicalDeviceManageLicenseResponse
        """
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
        """
        @summary 第二类医疗器械经营备案凭证
        
        @param request: RecognizeCtwoMedicalDeviceManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeCtwoMedicalDeviceManageLicenseResponse
        """
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
        """
        @summary 第二类医疗器械经营备案凭证
        
        @param request: RecognizeCtwoMedicalDeviceManageLicenseRequest
        @return: RecognizeCtwoMedicalDeviceManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_ctwo_medical_device_manage_license_with_options(request, runtime)

    async def recognize_ctwo_medical_device_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse:
        """
        @summary 第二类医疗器械经营备案凭证
        
        @param request: RecognizeCtwoMedicalDeviceManageLicenseRequest
        @return: RecognizeCtwoMedicalDeviceManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_ctwo_medical_device_manage_license_with_options_async(request, runtime)

    def recognize_document_structure_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDocumentStructureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDocumentStructureResponse:
        """
        @summary 文档结构化识别
        
        @param request: RecognizeDocumentStructureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDocumentStructureResponse
        """
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
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.use_new_style_output):
            query['UseNewStyleOutput'] = request.use_new_style_output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDocumentStructure',
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
            ocr_api_20210707_models.RecognizeDocumentStructureResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_document_structure_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeDocumentStructureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDocumentStructureResponse:
        """
        @summary 文档结构化识别
        
        @param request: RecognizeDocumentStructureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDocumentStructureResponse
        """
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
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.use_new_style_output):
            query['UseNewStyleOutput'] = request.use_new_style_output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDocumentStructure',
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
            ocr_api_20210707_models.RecognizeDocumentStructureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_document_structure(
        self,
        request: ocr_api_20210707_models.RecognizeDocumentStructureRequest,
    ) -> ocr_api_20210707_models.RecognizeDocumentStructureResponse:
        """
        @summary 文档结构化识别
        
        @param request: RecognizeDocumentStructureRequest
        @return: RecognizeDocumentStructureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_document_structure_with_options(request, runtime)

    async def recognize_document_structure_async(
        self,
        request: ocr_api_20210707_models.RecognizeDocumentStructureRequest,
    ) -> ocr_api_20210707_models.RecognizeDocumentStructureResponse:
        """
        @summary 文档结构化识别
        
        @param request: RecognizeDocumentStructureRequest
        @return: RecognizeDocumentStructureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_document_structure_with_options_async(request, runtime)

    def recognize_driving_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        """
        @summary 驾驶证识别
        
        @param request: RecognizeDrivingLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDrivingLicenseResponse
        """
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
        """
        @summary 驾驶证识别
        
        @param request: RecognizeDrivingLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeDrivingLicenseResponse
        """
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
        """
        @summary 驾驶证识别
        
        @param request: RecognizeDrivingLicenseRequest
        @return: RecognizeDrivingLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_driving_license_with_options(request, runtime)

    async def recognize_driving_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeDrivingLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeDrivingLicenseResponse:
        """
        @summary 驾驶证识别
        
        @param request: RecognizeDrivingLicenseRequest
        @return: RecognizeDrivingLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_driving_license_with_options_async(request, runtime)

    def recognize_edu_formula_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        """
        @summary 印刷体数学公式识别
        
        @param request: RecognizeEduFormulaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduFormulaResponse
        """
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
        """
        @summary 印刷体数学公式识别
        
        @param request: RecognizeEduFormulaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduFormulaResponse
        """
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
        """
        @summary 印刷体数学公式识别
        
        @param request: RecognizeEduFormulaRequest
        @return: RecognizeEduFormulaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_formula_with_options(request, runtime)

    async def recognize_edu_formula_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduFormulaRequest,
    ) -> ocr_api_20210707_models.RecognizeEduFormulaResponse:
        """
        @summary 印刷体数学公式识别
        
        @param request: RecognizeEduFormulaRequest
        @return: RecognizeEduFormulaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_formula_with_options_async(request, runtime)

    def recognize_edu_oral_calculation_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        """
        @summary 口算判题
        
        @param request: RecognizeEduOralCalculationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduOralCalculationResponse
        """
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
        """
        @summary 口算判题
        
        @param request: RecognizeEduOralCalculationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduOralCalculationResponse
        """
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
        """
        @summary 口算判题
        
        @param request: RecognizeEduOralCalculationRequest
        @return: RecognizeEduOralCalculationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_oral_calculation_with_options(request, runtime)

    async def recognize_edu_oral_calculation_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduOralCalculationRequest,
    ) -> ocr_api_20210707_models.RecognizeEduOralCalculationResponse:
        """
        @summary 口算判题
        
        @param request: RecognizeEduOralCalculationRequest
        @return: RecognizeEduOralCalculationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_oral_calculation_with_options_async(request, runtime)

    def recognize_edu_paper_cut_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        """
        @summary 试卷切题识别
        
        @param request: RecognizeEduPaperCutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperCutResponse
        """
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
        """
        @summary 试卷切题识别
        
        @param request: RecognizeEduPaperCutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperCutResponse
        """
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
        """
        @summary 试卷切题识别
        
        @param request: RecognizeEduPaperCutRequest
        @return: RecognizeEduPaperCutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_cut_with_options(request, runtime)

    async def recognize_edu_paper_cut_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperCutRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperCutResponse:
        """
        @summary 试卷切题识别
        
        @param request: RecognizeEduPaperCutRequest
        @return: RecognizeEduPaperCutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_cut_with_options_async(request, runtime)

    def recognize_edu_paper_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        """
        @summary 整页试卷识别
        
        @param request: RecognizeEduPaperOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperOcrResponse
        """
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
        """
        @summary 整页试卷识别
        
        @param request: RecognizeEduPaperOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperOcrResponse
        """
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
        """
        @summary 整页试卷识别
        
        @param request: RecognizeEduPaperOcrRequest
        @return: RecognizeEduPaperOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_ocr_with_options(request, runtime)

    async def recognize_edu_paper_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperOcrResponse:
        """
        @summary 整页试卷识别
        
        @param request: RecognizeEduPaperOcrRequest
        @return: RecognizeEduPaperOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_ocr_with_options_async(request, runtime)

    def recognize_edu_paper_structed_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        """
        @summary 精细版结构化切题
        
        @param request: RecognizeEduPaperStructedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperStructedResponse
        """
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
        """
        @summary 精细版结构化切题
        
        @param request: RecognizeEduPaperStructedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduPaperStructedResponse
        """
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
        """
        @summary 精细版结构化切题
        
        @param request: RecognizeEduPaperStructedRequest
        @return: RecognizeEduPaperStructedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_structed_with_options(request, runtime)

    async def recognize_edu_paper_structed_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduPaperStructedRequest,
    ) -> ocr_api_20210707_models.RecognizeEduPaperStructedResponse:
        """
        @summary 精细版结构化切题
        
        @param request: RecognizeEduPaperStructedRequest
        @return: RecognizeEduPaperStructedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_paper_structed_with_options_async(request, runtime)

    def recognize_edu_question_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        """
        @summary 题目识别
        
        @param request: RecognizeEduQuestionOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduQuestionOcrResponse
        """
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
        """
        @summary 题目识别
        
        @param request: RecognizeEduQuestionOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEduQuestionOcrResponse
        """
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
        """
        @summary 题目识别
        
        @param request: RecognizeEduQuestionOcrRequest
        @return: RecognizeEduQuestionOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_question_ocr_with_options(request, runtime)

    async def recognize_edu_question_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeEduQuestionOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeEduQuestionOcrResponse:
        """
        @summary 题目识别
        
        @param request: RecognizeEduQuestionOcrRequest
        @return: RecognizeEduQuestionOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_edu_question_ocr_with_options_async(request, runtime)

    def recognize_english_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        """
        @summary 英语专项识别
        
        @param request: RecognizeEnglishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEnglishResponse
        """
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
        """
        @summary 英语专项识别
        
        @param request: RecognizeEnglishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEnglishResponse
        """
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
        """
        @summary 英语专项识别
        
        @param request: RecognizeEnglishRequest
        @return: RecognizeEnglishResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_english_with_options(request, runtime)

    async def recognize_english_async(
        self,
        request: ocr_api_20210707_models.RecognizeEnglishRequest,
    ) -> ocr_api_20210707_models.RecognizeEnglishResponse:
        """
        @summary 英语专项识别
        
        @param request: RecognizeEnglishRequest
        @return: RecognizeEnglishResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_english_with_options_async(request, runtime)

    def recognize_estate_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        """
        @summary 不动产权证
        
        @param request: RecognizeEstateCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEstateCertificationResponse
        """
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
        """
        @summary 不动产权证
        
        @param request: RecognizeEstateCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeEstateCertificationResponse
        """
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
        """
        @summary 不动产权证
        
        @param request: RecognizeEstateCertificationRequest
        @return: RecognizeEstateCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_estate_certification_with_options(request, runtime)

    async def recognize_estate_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeEstateCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeEstateCertificationResponse:
        """
        @summary 不动产权证
        
        @param request: RecognizeEstateCertificationRequest
        @return: RecognizeEstateCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_estate_certification_with_options_async(request, runtime)

    def recognize_exit_entry_permit_to_hkwith_options(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        """
        @summary 来往港澳台通行证识别
        
        @param request: RecognizeExitEntryPermitToHKRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExitEntryPermitToHKResponse
        """
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
        """
        @summary 来往港澳台通行证识别
        
        @param request: RecognizeExitEntryPermitToHKRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExitEntryPermitToHKResponse
        """
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
        """
        @summary 来往港澳台通行证识别
        
        @param request: RecognizeExitEntryPermitToHKRequest
        @return: RecognizeExitEntryPermitToHKResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_hkwith_options(request, runtime)

    async def recognize_exit_entry_permit_to_hk_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToHKRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse:
        """
        @summary 来往港澳台通行证识别
        
        @param request: RecognizeExitEntryPermitToHKRequest
        @return: RecognizeExitEntryPermitToHKResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_exit_entry_permit_to_hkwith_options_async(request, runtime)

    def recognize_exit_entry_permit_to_mainland_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        """
        @summary 来往大陆(内地)通行证识别
        
        @param request: RecognizeExitEntryPermitToMainlandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExitEntryPermitToMainlandResponse
        """
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
        """
        @summary 来往大陆(内地)通行证识别
        
        @param request: RecognizeExitEntryPermitToMainlandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeExitEntryPermitToMainlandResponse
        """
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
        """
        @summary 来往大陆(内地)通行证识别
        
        @param request: RecognizeExitEntryPermitToMainlandRequest
        @return: RecognizeExitEntryPermitToMainlandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_mainland_with_options(request, runtime)

    async def recognize_exit_entry_permit_to_mainland_async(
        self,
        request: ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandRequest,
    ) -> ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse:
        """
        @summary 来往大陆(内地)通行证识别
        
        @param request: RecognizeExitEntryPermitToMainlandRequest
        @return: RecognizeExitEntryPermitToMainlandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_exit_entry_permit_to_mainland_with_options_async(request, runtime)

    def recognize_food_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        """
        @summary 食品经营许可证
        
        @param request: RecognizeFoodManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFoodManageLicenseResponse
        """
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
        """
        @summary 食品经营许可证
        
        @param request: RecognizeFoodManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFoodManageLicenseResponse
        """
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
        """
        @summary 食品经营许可证
        
        @param request: RecognizeFoodManageLicenseRequest
        @return: RecognizeFoodManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_manage_license_with_options(request, runtime)

    async def recognize_food_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodManageLicenseResponse:
        """
        @summary 食品经营许可证
        
        @param request: RecognizeFoodManageLicenseRequest
        @return: RecognizeFoodManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_food_manage_license_with_options_async(request, runtime)

    def recognize_food_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        """
        @summary 食品生产许可证
        
        @param request: RecognizeFoodProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFoodProduceLicenseResponse
        """
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
        """
        @summary 食品生产许可证
        
        @param request: RecognizeFoodProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeFoodProduceLicenseResponse
        """
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
        """
        @summary 食品生产许可证
        
        @param request: RecognizeFoodProduceLicenseRequest
        @return: RecognizeFoodProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_produce_license_with_options(request, runtime)

    async def recognize_food_produce_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeFoodProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse:
        """
        @summary 食品生产许可证
        
        @param request: RecognizeFoodProduceLicenseRequest
        @return: RecognizeFoodProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_food_produce_license_with_options_async(request, runtime)

    def recognize_general_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        """
        @summary 通用文字识别
        
        @param request: RecognizeGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeGeneralResponse
        """
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
        """
        @summary 通用文字识别
        
        @param request: RecognizeGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeGeneralResponse
        """
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
        """
        @summary 通用文字识别
        
        @param request: RecognizeGeneralRequest
        @return: RecognizeGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_general_with_options(request, runtime)

    async def recognize_general_async(
        self,
        request: ocr_api_20210707_models.RecognizeGeneralRequest,
    ) -> ocr_api_20210707_models.RecognizeGeneralResponse:
        """
        @summary 通用文字识别
        
        @param request: RecognizeGeneralRequest
        @return: RecognizeGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_general_with_options_async(request, runtime)

    def recognize_hkidcard_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHKIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHKIdcardResponse:
        """
        @summary 香港身份证识别
        
        @param request: RecognizeHKIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHKIdcardResponse
        """
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
            action='RecognizeHKIdcard',
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
            ocr_api_20210707_models.RecognizeHKIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_hkidcard_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHKIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHKIdcardResponse:
        """
        @summary 香港身份证识别
        
        @param request: RecognizeHKIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHKIdcardResponse
        """
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
            action='RecognizeHKIdcard',
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
            ocr_api_20210707_models.RecognizeHKIdcardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_hkidcard(
        self,
        request: ocr_api_20210707_models.RecognizeHKIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeHKIdcardResponse:
        """
        @summary 香港身份证识别
        
        @param request: RecognizeHKIdcardRequest
        @return: RecognizeHKIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_hkidcard_with_options(request, runtime)

    async def recognize_hkidcard_async(
        self,
        request: ocr_api_20210707_models.RecognizeHKIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeHKIdcardResponse:
        """
        @summary 香港身份证识别
        
        @param request: RecognizeHKIdcardRequest
        @return: RecognizeHKIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_hkidcard_with_options_async(request, runtime)

    def recognize_handwriting_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        """
        @summary 通用手写体识别
        
        @param request: RecognizeHandwritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHandwritingResponse
        """
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
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
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
        """
        @summary 通用手写体识别
        
        @param request: RecognizeHandwritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHandwritingResponse
        """
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
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
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
        """
        @summary 通用手写体识别
        
        @param request: RecognizeHandwritingRequest
        @return: RecognizeHandwritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_handwriting_with_options(request, runtime)

    async def recognize_handwriting_async(
        self,
        request: ocr_api_20210707_models.RecognizeHandwritingRequest,
    ) -> ocr_api_20210707_models.RecognizeHandwritingResponse:
        """
        @summary 通用手写体识别
        
        @param request: RecognizeHandwritingRequest
        @return: RecognizeHandwritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_handwriting_with_options_async(request, runtime)

    def recognize_health_code_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHealthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHealthCodeResponse:
        """
        @summary 防疫健康码识别
        
        @param request: RecognizeHealthCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHealthCodeResponse
        """
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
            action='RecognizeHealthCode',
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
            ocr_api_20210707_models.RecognizeHealthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_health_code_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHealthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHealthCodeResponse:
        """
        @summary 防疫健康码识别
        
        @param request: RecognizeHealthCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHealthCodeResponse
        """
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
            action='RecognizeHealthCode',
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
            ocr_api_20210707_models.RecognizeHealthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_health_code(
        self,
        request: ocr_api_20210707_models.RecognizeHealthCodeRequest,
    ) -> ocr_api_20210707_models.RecognizeHealthCodeResponse:
        """
        @summary 防疫健康码识别
        
        @param request: RecognizeHealthCodeRequest
        @return: RecognizeHealthCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_health_code_with_options(request, runtime)

    async def recognize_health_code_async(
        self,
        request: ocr_api_20210707_models.RecognizeHealthCodeRequest,
    ) -> ocr_api_20210707_models.RecognizeHealthCodeResponse:
        """
        @summary 防疫健康码识别
        
        @param request: RecognizeHealthCodeRequest
        @return: RecognizeHealthCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_health_code_with_options_async(request, runtime)

    def recognize_hotel_consume_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHotelConsumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHotelConsumeResponse:
        """
        @summary 酒店流水识别
        
        @param request: RecognizeHotelConsumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHotelConsumeResponse
        """
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
            action='RecognizeHotelConsume',
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
            ocr_api_20210707_models.RecognizeHotelConsumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_hotel_consume_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeHotelConsumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHotelConsumeResponse:
        """
        @summary 酒店流水识别
        
        @param request: RecognizeHotelConsumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHotelConsumeResponse
        """
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
            action='RecognizeHotelConsume',
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
            ocr_api_20210707_models.RecognizeHotelConsumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_hotel_consume(
        self,
        request: ocr_api_20210707_models.RecognizeHotelConsumeRequest,
    ) -> ocr_api_20210707_models.RecognizeHotelConsumeResponse:
        """
        @summary 酒店流水识别
        
        @param request: RecognizeHotelConsumeRequest
        @return: RecognizeHotelConsumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_hotel_consume_with_options(request, runtime)

    async def recognize_hotel_consume_async(
        self,
        request: ocr_api_20210707_models.RecognizeHotelConsumeRequest,
    ) -> ocr_api_20210707_models.RecognizeHotelConsumeResponse:
        """
        @summary 酒店流水识别
        
        @param request: RecognizeHotelConsumeRequest
        @return: RecognizeHotelConsumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_hotel_consume_with_options_async(request, runtime)

    def recognize_household_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        """
        @summary 户口本识别
        
        @param request: RecognizeHouseholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHouseholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_resident_page):
            query['IsResidentPage'] = request.is_resident_page
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
        """
        @summary 户口本识别
        
        @param request: RecognizeHouseholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeHouseholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_resident_page):
            query['IsResidentPage'] = request.is_resident_page
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
        """
        @summary 户口本识别
        
        @param request: RecognizeHouseholdRequest
        @return: RecognizeHouseholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_household_with_options(request, runtime)

    async def recognize_household_async(
        self,
        request: ocr_api_20210707_models.RecognizeHouseholdRequest,
    ) -> ocr_api_20210707_models.RecognizeHouseholdResponse:
        """
        @summary 户口本识别
        
        @param request: RecognizeHouseholdRequest
        @return: RecognizeHouseholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_household_with_options_async(request, runtime)

    def recognize_idcard_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        """
        @summary 身份证识别
        
        @param request: RecognizeIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIdcardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_quality_info):
            query['OutputQualityInfo'] = request.output_quality_info
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
        """
        @summary 身份证识别
        
        @param request: RecognizeIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeIdcardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_quality_info):
            query['OutputQualityInfo'] = request.output_quality_info
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
        """
        @summary 身份证识别
        
        @param request: RecognizeIdcardRequest
        @return: RecognizeIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_idcard_with_options(request, runtime)

    async def recognize_idcard_async(
        self,
        request: ocr_api_20210707_models.RecognizeIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeIdcardResponse:
        """
        @summary 身份证识别
        
        @param request: RecognizeIdcardRequest
        @return: RecognizeIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_idcard_with_options_async(request, runtime)

    def recognize_international_business_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse:
        """
        @summary 国际营业执照识别
        
        @param request: RecognizeInternationalBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInternationalBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalBusinessLicense',
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
            ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_international_business_license_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse:
        """
        @summary 国际营业执照识别
        
        @param request: RecognizeInternationalBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInternationalBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalBusinessLicense',
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
            ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_international_business_license(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse:
        """
        @summary 国际营业执照识别
        
        @param request: RecognizeInternationalBusinessLicenseRequest
        @return: RecognizeInternationalBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_international_business_license_with_options(request, runtime)

    async def recognize_international_business_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse:
        """
        @summary 国际营业执照识别
        
        @param request: RecognizeInternationalBusinessLicenseRequest
        @return: RecognizeInternationalBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_international_business_license_with_options_async(request, runtime)

    def recognize_international_idcard_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInternationalIdcardResponse:
        """
        @summary 国际身份证识别
        
        @param request: RecognizeInternationalIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInternationalIdcardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalIdcard',
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
            ocr_api_20210707_models.RecognizeInternationalIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_international_idcard_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalIdcardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInternationalIdcardResponse:
        """
        @summary 国际身份证识别
        
        @param request: RecognizeInternationalIdcardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInternationalIdcardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalIdcard',
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
            ocr_api_20210707_models.RecognizeInternationalIdcardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_international_idcard(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeInternationalIdcardResponse:
        """
        @summary 国际身份证识别
        
        @param request: RecognizeInternationalIdcardRequest
        @return: RecognizeInternationalIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_international_idcard_with_options(request, runtime)

    async def recognize_international_idcard_async(
        self,
        request: ocr_api_20210707_models.RecognizeInternationalIdcardRequest,
    ) -> ocr_api_20210707_models.RecognizeInternationalIdcardResponse:
        """
        @summary 国际身份证识别
        
        @param request: RecognizeInternationalIdcardRequest
        @return: RecognizeInternationalIdcardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_international_idcard_with_options_async(request, runtime)

    def recognize_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        """
        @summary 增值税发票识别
        
        @param request: RecognizeInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInvoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
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
        """
        @summary 增值税发票识别
        
        @param request: RecognizeInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeInvoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
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
        """
        @summary 增值税发票识别
        
        @param request: RecognizeInvoiceRequest
        @return: RecognizeInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_invoice_with_options(request, runtime)

    async def recognize_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeInvoiceResponse:
        """
        @summary 增值税发票识别
        
        @param request: RecognizeInvoiceRequest
        @return: RecognizeInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_invoice_with_options_async(request, runtime)

    def recognize_janpanese_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        """
        @summary 日语识别
        
        @param request: RecognizeJanpaneseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeJanpaneseResponse
        """
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
        """
        @summary 日语识别
        
        @param request: RecognizeJanpaneseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeJanpaneseResponse
        """
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
        """
        @summary 日语识别
        
        @param request: RecognizeJanpaneseRequest
        @return: RecognizeJanpaneseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_janpanese_with_options(request, runtime)

    async def recognize_janpanese_async(
        self,
        request: ocr_api_20210707_models.RecognizeJanpaneseRequest,
    ) -> ocr_api_20210707_models.RecognizeJanpaneseResponse:
        """
        @summary 日语识别
        
        @param request: RecognizeJanpaneseRequest
        @return: RecognizeJanpaneseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_janpanese_with_options_async(request, runtime)

    def recognize_korean_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        """
        @summary 韩语识别
        
        @param request: RecognizeKoreanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeKoreanResponse
        """
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
        """
        @summary 韩语识别
        
        @param request: RecognizeKoreanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeKoreanResponse
        """
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
        """
        @summary 韩语识别
        
        @param request: RecognizeKoreanRequest
        @return: RecognizeKoreanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_korean_with_options(request, runtime)

    async def recognize_korean_async(
        self,
        request: ocr_api_20210707_models.RecognizeKoreanRequest,
    ) -> ocr_api_20210707_models.RecognizeKoreanResponse:
        """
        @summary 韩语识别
        
        @param request: RecognizeKoreanRequest
        @return: RecognizeKoreanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_korean_with_options_async(request, runtime)

    def recognize_latin_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        """
        @summary 拉丁语识别
        
        @param request: RecognizeLatinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeLatinResponse
        """
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
        """
        @summary 拉丁语识别
        
        @param request: RecognizeLatinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeLatinResponse
        """
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
        """
        @summary 拉丁语识别
        
        @param request: RecognizeLatinRequest
        @return: RecognizeLatinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_latin_with_options(request, runtime)

    async def recognize_latin_async(
        self,
        request: ocr_api_20210707_models.RecognizeLatinRequest,
    ) -> ocr_api_20210707_models.RecognizeLatinResponse:
        """
        @summary 拉丁语识别
        
        @param request: RecognizeLatinRequest
        @return: RecognizeLatinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_latin_with_options_async(request, runtime)

    def recognize_medical_device_manage_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        """
        @summary 医疗器械经营许可证
        
        @param request: RecognizeMedicalDeviceManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMedicalDeviceManageLicenseResponse
        """
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
        """
        @summary 医疗器械经营许可证
        
        @param request: RecognizeMedicalDeviceManageLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMedicalDeviceManageLicenseResponse
        """
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
        """
        @summary 医疗器械经营许可证
        
        @param request: RecognizeMedicalDeviceManageLicenseRequest
        @return: RecognizeMedicalDeviceManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_manage_license_with_options(request, runtime)

    async def recognize_medical_device_manage_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse:
        """
        @summary 医疗器械经营许可证
        
        @param request: RecognizeMedicalDeviceManageLicenseRequest
        @return: RecognizeMedicalDeviceManageLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_medical_device_manage_license_with_options_async(request, runtime)

    def recognize_medical_device_produce_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        """
        @summary 医疗器械生产许可证
        
        @param request: RecognizeMedicalDeviceProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMedicalDeviceProduceLicenseResponse
        """
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
        """
        @summary 医疗器械生产许可证
        
        @param request: RecognizeMedicalDeviceProduceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMedicalDeviceProduceLicenseResponse
        """
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
        """
        @summary 医疗器械生产许可证
        
        @param request: RecognizeMedicalDeviceProduceLicenseRequest
        @return: RecognizeMedicalDeviceProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_produce_license_with_options(request, runtime)

    async def recognize_medical_device_produce_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse:
        """
        @summary 医疗器械生产许可证
        
        @param request: RecognizeMedicalDeviceProduceLicenseRequest
        @return: RecognizeMedicalDeviceProduceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_medical_device_produce_license_with_options_async(request, runtime)

    def recognize_mixed_invoices_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        """
        @summary 混贴发票识别
        
        @param request: RecognizeMixedInvoicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMixedInvoicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merge_pdf_pages):
            query['MergePdfPages'] = request.merge_pdf_pages
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
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
        """
        @summary 混贴发票识别
        
        @param request: RecognizeMixedInvoicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMixedInvoicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merge_pdf_pages):
            query['MergePdfPages'] = request.merge_pdf_pages
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
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
        """
        @summary 混贴发票识别
        
        @param request: RecognizeMixedInvoicesRequest
        @return: RecognizeMixedInvoicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_invoices_with_options(request, runtime)

    async def recognize_mixed_invoices_async(
        self,
        request: ocr_api_20210707_models.RecognizeMixedInvoicesRequest,
    ) -> ocr_api_20210707_models.RecognizeMixedInvoicesResponse:
        """
        @summary 混贴发票识别
        
        @param request: RecognizeMixedInvoicesRequest
        @return: RecognizeMixedInvoicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_mixed_invoices_with_options_async(request, runtime)

    def recognize_multi_language_with_options(
        self,
        tmp_req: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        """
        @summary 通用多语言识别
        
        @param tmp_req: RecognizeMultiLanguageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMultiLanguageResponse
        """
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
            stream=tmp_req.body
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
        """
        @summary 通用多语言识别
        
        @param tmp_req: RecognizeMultiLanguageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeMultiLanguageResponse
        """
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
            stream=tmp_req.body
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
        """
        @summary 通用多语言识别
        
        @param request: RecognizeMultiLanguageRequest
        @return: RecognizeMultiLanguageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_multi_language_with_options(request, runtime)

    async def recognize_multi_language_async(
        self,
        request: ocr_api_20210707_models.RecognizeMultiLanguageRequest,
    ) -> ocr_api_20210707_models.RecognizeMultiLanguageResponse:
        """
        @summary 通用多语言识别
        
        @param request: RecognizeMultiLanguageRequest
        @return: RecognizeMultiLanguageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_multi_language_with_options_async(request, runtime)

    def recognize_non_tax_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeNonTaxInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse:
        """
        @summary 非税收入票据识别
        
        @param request: RecognizeNonTaxInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeNonTaxInvoiceResponse
        """
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
            action='RecognizeNonTaxInvoice',
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
            ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_non_tax_invoice_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeNonTaxInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse:
        """
        @summary 非税收入票据识别
        
        @param request: RecognizeNonTaxInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeNonTaxInvoiceResponse
        """
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
            action='RecognizeNonTaxInvoice',
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
            ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_non_tax_invoice(
        self,
        request: ocr_api_20210707_models.RecognizeNonTaxInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse:
        """
        @summary 非税收入票据识别
        
        @param request: RecognizeNonTaxInvoiceRequest
        @return: RecognizeNonTaxInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_non_tax_invoice_with_options(request, runtime)

    async def recognize_non_tax_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeNonTaxInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse:
        """
        @summary 非税收入票据识别
        
        @param request: RecognizeNonTaxInvoiceRequest
        @return: RecognizeNonTaxInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_non_tax_invoice_with_options_async(request, runtime)

    def recognize_passport_with_options(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        """
        @summary 护照识别
        
        @param request: RecognizePassportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePassportResponse
        """
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
        """
        @summary 护照识别
        
        @param request: RecognizePassportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePassportResponse
        """
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
        """
        @summary 护照识别
        
        @param request: RecognizePassportRequest
        @return: RecognizePassportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_passport_with_options(request, runtime)

    async def recognize_passport_async(
        self,
        request: ocr_api_20210707_models.RecognizePassportRequest,
    ) -> ocr_api_20210707_models.RecognizePassportResponse:
        """
        @summary 护照识别
        
        @param request: RecognizePassportRequest
        @return: RecognizePassportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_passport_with_options_async(request, runtime)

    def recognize_payment_record_with_options(
        self,
        request: ocr_api_20210707_models.RecognizePaymentRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePaymentRecordResponse:
        """
        @summary 支付详情页识别
        
        @param request: RecognizePaymentRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePaymentRecordResponse
        """
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
            action='RecognizePaymentRecord',
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
            ocr_api_20210707_models.RecognizePaymentRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_payment_record_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizePaymentRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePaymentRecordResponse:
        """
        @summary 支付详情页识别
        
        @param request: RecognizePaymentRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePaymentRecordResponse
        """
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
            action='RecognizePaymentRecord',
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
            ocr_api_20210707_models.RecognizePaymentRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_payment_record(
        self,
        request: ocr_api_20210707_models.RecognizePaymentRecordRequest,
    ) -> ocr_api_20210707_models.RecognizePaymentRecordResponse:
        """
        @summary 支付详情页识别
        
        @param request: RecognizePaymentRecordRequest
        @return: RecognizePaymentRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_payment_record_with_options(request, runtime)

    async def recognize_payment_record_async(
        self,
        request: ocr_api_20210707_models.RecognizePaymentRecordRequest,
    ) -> ocr_api_20210707_models.RecognizePaymentRecordResponse:
        """
        @summary 支付详情页识别
        
        @param request: RecognizePaymentRecordRequest
        @return: RecognizePaymentRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_payment_record_with_options_async(request, runtime)

    def recognize_purchase_record_with_options(
        self,
        request: ocr_api_20210707_models.RecognizePurchaseRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePurchaseRecordResponse:
        """
        @summary 电商订单页识别
        
        @param request: RecognizePurchaseRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePurchaseRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_multi_orders):
            query['OutputMultiOrders'] = request.output_multi_orders
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePurchaseRecord',
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
            ocr_api_20210707_models.RecognizePurchaseRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_purchase_record_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizePurchaseRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizePurchaseRecordResponse:
        """
        @summary 电商订单页识别
        
        @param request: RecognizePurchaseRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizePurchaseRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_multi_orders):
            query['OutputMultiOrders'] = request.output_multi_orders
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePurchaseRecord',
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
            ocr_api_20210707_models.RecognizePurchaseRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_purchase_record(
        self,
        request: ocr_api_20210707_models.RecognizePurchaseRecordRequest,
    ) -> ocr_api_20210707_models.RecognizePurchaseRecordResponse:
        """
        @summary 电商订单页识别
        
        @param request: RecognizePurchaseRecordRequest
        @return: RecognizePurchaseRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_purchase_record_with_options(request, runtime)

    async def recognize_purchase_record_async(
        self,
        request: ocr_api_20210707_models.RecognizePurchaseRecordRequest,
    ) -> ocr_api_20210707_models.RecognizePurchaseRecordResponse:
        """
        @summary 电商订单页识别
        
        @param request: RecognizePurchaseRecordRequest
        @return: RecognizePurchaseRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_purchase_record_with_options_async(request, runtime)

    def recognize_quota_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票
        
        @param request: RecognizeQuotaInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQuotaInvoiceResponse
        """
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
        """
        @summary 定额发票
        
        @param request: RecognizeQuotaInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeQuotaInvoiceResponse
        """
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
        """
        @summary 定额发票
        
        @param request: RecognizeQuotaInvoiceRequest
        @return: RecognizeQuotaInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_quota_invoice_with_options(request, runtime)

    async def recognize_quota_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeQuotaInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeQuotaInvoiceResponse:
        """
        @summary 定额发票
        
        @param request: RecognizeQuotaInvoiceRequest
        @return: RecognizeQuotaInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_quota_invoice_with_options_async(request, runtime)

    def recognize_ride_hailing_itinerary_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        """
        @summary 网约车行程单识别
        
        @param request: RecognizeRideHailingItineraryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRideHailingItineraryResponse
        """
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
        """
        @summary 网约车行程单识别
        
        @param request: RecognizeRideHailingItineraryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRideHailingItineraryResponse
        """
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
        """
        @summary 网约车行程单识别
        
        @param request: RecognizeRideHailingItineraryRequest
        @return: RecognizeRideHailingItineraryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_ride_hailing_itinerary_with_options(request, runtime)

    async def recognize_ride_hailing_itinerary_async(
        self,
        request: ocr_api_20210707_models.RecognizeRideHailingItineraryRequest,
    ) -> ocr_api_20210707_models.RecognizeRideHailingItineraryResponse:
        """
        @summary 网约车行程单识别
        
        @param request: RecognizeRideHailingItineraryRequest
        @return: RecognizeRideHailingItineraryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_ride_hailing_itinerary_with_options_async(request, runtime)

    def recognize_roll_ticket_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeRollTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRollTicketResponse
        """
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
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeRollTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRollTicketResponse
        """
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
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeRollTicketRequest
        @return: RecognizeRollTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_roll_ticket_with_options(request, runtime)

    async def recognize_roll_ticket_async(
        self,
        request: ocr_api_20210707_models.RecognizeRollTicketRequest,
    ) -> ocr_api_20210707_models.RecognizeRollTicketResponse:
        """
        @summary 增值税发票卷票
        
        @param request: RecognizeRollTicketRequest
        @return: RecognizeRollTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_roll_ticket_with_options_async(request, runtime)

    def recognize_russian_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        """
        @summary 俄语识别
        
        @param request: RecognizeRussianRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRussianResponse
        """
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
        """
        @summary 俄语识别
        
        @param request: RecognizeRussianRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeRussianResponse
        """
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
        """
        @summary 俄语识别
        
        @param request: RecognizeRussianRequest
        @return: RecognizeRussianResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_russian_with_options(request, runtime)

    async def recognize_russian_async(
        self,
        request: ocr_api_20210707_models.RecognizeRussianRequest,
    ) -> ocr_api_20210707_models.RecognizeRussianResponse:
        """
        @summary 俄语识别
        
        @param request: RecognizeRussianRequest
        @return: RecognizeRussianResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_russian_with_options_async(request, runtime)

    def recognize_shopping_receipt_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeShoppingReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeShoppingReceiptResponse:
        """
        @summary 购物小票识别
        
        @param request: RecognizeShoppingReceiptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeShoppingReceiptResponse
        """
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
            action='RecognizeShoppingReceipt',
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
            ocr_api_20210707_models.RecognizeShoppingReceiptResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_shopping_receipt_with_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeShoppingReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeShoppingReceiptResponse:
        """
        @summary 购物小票识别
        
        @param request: RecognizeShoppingReceiptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeShoppingReceiptResponse
        """
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
            action='RecognizeShoppingReceipt',
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
            ocr_api_20210707_models.RecognizeShoppingReceiptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_shopping_receipt(
        self,
        request: ocr_api_20210707_models.RecognizeShoppingReceiptRequest,
    ) -> ocr_api_20210707_models.RecognizeShoppingReceiptResponse:
        """
        @summary 购物小票识别
        
        @param request: RecognizeShoppingReceiptRequest
        @return: RecognizeShoppingReceiptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_shopping_receipt_with_options(request, runtime)

    async def recognize_shopping_receipt_async(
        self,
        request: ocr_api_20210707_models.RecognizeShoppingReceiptRequest,
    ) -> ocr_api_20210707_models.RecognizeShoppingReceiptResponse:
        """
        @summary 购物小票识别
        
        @param request: RecognizeShoppingReceiptRequest
        @return: RecognizeShoppingReceiptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_shopping_receipt_with_options_async(request, runtime)

    def recognize_social_security_card_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        """
        @summary 社会保障卡识别
        
        @param request: RecognizeSocialSecurityCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeSocialSecurityCardResponse
        """
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
        """
        @summary 社会保障卡识别
        
        @param request: RecognizeSocialSecurityCardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeSocialSecurityCardResponse
        """
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
        """
        @summary 社会保障卡识别
        
        @param request: RecognizeSocialSecurityCardRequest
        @return: RecognizeSocialSecurityCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_social_security_card_with_options(request, runtime)

    async def recognize_social_security_card_async(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardRequest,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardResponse:
        """
        @summary 社会保障卡识别
        
        @param request: RecognizeSocialSecurityCardRequest
        @return: RecognizeSocialSecurityCardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_social_security_card_with_options_async(request, runtime)

    def recognize_social_security_card_version_iiwith_options(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse:
        """
        @summary 社保卡识别
        
        @param request: RecognizeSocialSecurityCardVersionIIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeSocialSecurityCardVersionIIResponse
        """
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
            action='RecognizeSocialSecurityCardVersionII',
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
            ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_social_security_card_version_iiwith_options_async(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse:
        """
        @summary 社保卡识别
        
        @param request: RecognizeSocialSecurityCardVersionIIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeSocialSecurityCardVersionIIResponse
        """
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
            action='RecognizeSocialSecurityCardVersionII',
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
            ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_social_security_card_version_ii(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIRequest,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse:
        """
        @summary 社保卡识别
        
        @param request: RecognizeSocialSecurityCardVersionIIRequest
        @return: RecognizeSocialSecurityCardVersionIIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_social_security_card_version_iiwith_options(request, runtime)

    async def recognize_social_security_card_version_ii_async(
        self,
        request: ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIRequest,
    ) -> ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse:
        """
        @summary 社保卡识别
        
        @param request: RecognizeSocialSecurityCardVersionIIRequest
        @return: RecognizeSocialSecurityCardVersionIIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_social_security_card_version_iiwith_options_async(request, runtime)

    def recognize_table_ocr_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        """
        @summary 表格识别
        
        @param request: RecognizeTableOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTableOcrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_hand_writing):
            query['IsHandWriting'] = request.is_hand_writing
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
        """
        @summary 表格识别
        
        @param request: RecognizeTableOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTableOcrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_hand_writing):
            query['IsHandWriting'] = request.is_hand_writing
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
        """
        @summary 表格识别
        
        @param request: RecognizeTableOcrRequest
        @return: RecognizeTableOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_table_ocr_with_options(request, runtime)

    async def recognize_table_ocr_async(
        self,
        request: ocr_api_20210707_models.RecognizeTableOcrRequest,
    ) -> ocr_api_20210707_models.RecognizeTableOcrResponse:
        """
        @summary 表格识别
        
        @param request: RecognizeTableOcrRequest
        @return: RecognizeTableOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_table_ocr_with_options_async(request, runtime)

    def recognize_tax_clearance_certificate_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        """
        @summary 税收完税证明识别
        
        @param request: RecognizeTaxClearanceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxClearanceCertificateResponse
        """
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
        """
        @summary 税收完税证明识别
        
        @param request: RecognizeTaxClearanceCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxClearanceCertificateResponse
        """
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
        """
        @summary 税收完税证明识别
        
        @param request: RecognizeTaxClearanceCertificateRequest
        @return: RecognizeTaxClearanceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_tax_clearance_certificate_with_options(request, runtime)

    async def recognize_tax_clearance_certificate_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxClearanceCertificateRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse:
        """
        @summary 税收完税证明识别
        
        @param request: RecognizeTaxClearanceCertificateRequest
        @return: RecognizeTaxClearanceCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_tax_clearance_certificate_with_options_async(request, runtime)

    def recognize_taxi_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        """
        @summary 出租车发票
        
        @param request: RecognizeTaxiInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxiInvoiceResponse
        """
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
        """
        @summary 出租车发票
        
        @param request: RecognizeTaxiInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTaxiInvoiceResponse
        """
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
        """
        @summary 出租车发票
        
        @param request: RecognizeTaxiInvoiceRequest
        @return: RecognizeTaxiInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_taxi_invoice_with_options(request, runtime)

    async def recognize_taxi_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTaxiInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTaxiInvoiceResponse:
        """
        @summary 出租车发票
        
        @param request: RecognizeTaxiInvoiceRequest
        @return: RecognizeTaxiInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_taxi_invoice_with_options_async(request, runtime)

    def recognize_thai_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        """
        @summary 泰语识别
        
        @param request: RecognizeThaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeThaiResponse
        """
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
        """
        @summary 泰语识别
        
        @param request: RecognizeThaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeThaiResponse
        """
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
        """
        @summary 泰语识别
        
        @param request: RecognizeThaiRequest
        @return: RecognizeThaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_thai_with_options(request, runtime)

    async def recognize_thai_async(
        self,
        request: ocr_api_20210707_models.RecognizeThaiRequest,
    ) -> ocr_api_20210707_models.RecognizeThaiResponse:
        """
        @summary 泰语识别
        
        @param request: RecognizeThaiRequest
        @return: RecognizeThaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_thai_with_options_async(request, runtime)

    def recognize_toll_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        """
        @summary 过路过桥费发票识别
        
        @param request: RecognizeTollInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTollInvoiceResponse
        """
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
        """
        @summary 过路过桥费发票识别
        
        @param request: RecognizeTollInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTollInvoiceResponse
        """
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
        """
        @summary 过路过桥费发票识别
        
        @param request: RecognizeTollInvoiceRequest
        @return: RecognizeTollInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_toll_invoice_with_options(request, runtime)

    async def recognize_toll_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTollInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTollInvoiceResponse:
        """
        @summary 过路过桥费发票识别
        
        @param request: RecognizeTollInvoiceRequest
        @return: RecognizeTollInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_toll_invoice_with_options_async(request, runtime)

    def recognize_trade_mark_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        """
        @summary 商标注册证
        
        @param request: RecognizeTradeMarkCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTradeMarkCertificationResponse
        """
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
        """
        @summary 商标注册证
        
        @param request: RecognizeTradeMarkCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTradeMarkCertificationResponse
        """
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
        """
        @summary 商标注册证
        
        @param request: RecognizeTradeMarkCertificationRequest
        @return: RecognizeTradeMarkCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_trade_mark_certification_with_options(request, runtime)

    async def recognize_trade_mark_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeTradeMarkCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse:
        """
        @summary 商标注册证
        
        @param request: RecognizeTradeMarkCertificationRequest
        @return: RecognizeTradeMarkCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_trade_mark_certification_with_options_async(request, runtime)

    def recognize_train_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        """
        @summary 火车票
        
        @param request: RecognizeTrainInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTrainInvoiceResponse
        """
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
        """
        @summary 火车票
        
        @param request: RecognizeTrainInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeTrainInvoiceResponse
        """
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
        """
        @summary 火车票
        
        @param request: RecognizeTrainInvoiceRequest
        @return: RecognizeTrainInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_train_invoice_with_options(request, runtime)

    async def recognize_train_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeTrainInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeTrainInvoiceResponse:
        """
        @summary 火车票
        
        @param request: RecognizeTrainInvoiceRequest
        @return: RecognizeTrainInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_train_invoice_with_options_async(request, runtime)

    def recognize_used_car_invoice_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        """
        @summary 二手车统一销售发票识别
        
        @param request: RecognizeUsedCarInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeUsedCarInvoiceResponse
        """
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
        """
        @summary 二手车统一销售发票识别
        
        @param request: RecognizeUsedCarInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeUsedCarInvoiceResponse
        """
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
        """
        @summary 二手车统一销售发票识别
        
        @param request: RecognizeUsedCarInvoiceRequest
        @return: RecognizeUsedCarInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_used_car_invoice_with_options(request, runtime)

    async def recognize_used_car_invoice_async(
        self,
        request: ocr_api_20210707_models.RecognizeUsedCarInvoiceRequest,
    ) -> ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse:
        """
        @summary 二手车统一销售发票识别
        
        @param request: RecognizeUsedCarInvoiceRequest
        @return: RecognizeUsedCarInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_used_car_invoice_with_options_async(request, runtime)

    def recognize_vehicle_certification_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        """
        @summary 车辆合格证识别
        
        @param request: RecognizeVehicleCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleCertificationResponse
        """
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
        """
        @summary 车辆合格证识别
        
        @param request: RecognizeVehicleCertificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleCertificationResponse
        """
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
        """
        @summary 车辆合格证识别
        
        @param request: RecognizeVehicleCertificationRequest
        @return: RecognizeVehicleCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_certification_with_options(request, runtime)

    async def recognize_vehicle_certification_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleCertificationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleCertificationResponse:
        """
        @summary 车辆合格证识别
        
        @param request: RecognizeVehicleCertificationRequest
        @return: RecognizeVehicleCertificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_certification_with_options_async(request, runtime)

    def recognize_vehicle_license_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        """
        @summary 行驶证识别
        
        @param request: RecognizeVehicleLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleLicenseResponse
        """
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
        """
        @summary 行驶证识别
        
        @param request: RecognizeVehicleLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleLicenseResponse
        """
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
        """
        @summary 行驶证识别
        
        @param request: RecognizeVehicleLicenseRequest
        @return: RecognizeVehicleLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_license_with_options(request, runtime)

    async def recognize_vehicle_license_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleLicenseRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleLicenseResponse:
        """
        @summary 行驶证识别
        
        @param request: RecognizeVehicleLicenseRequest
        @return: RecognizeVehicleLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_license_with_options_async(request, runtime)

    def recognize_vehicle_registration_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        """
        @summary 机动车注册登记证识别
        
        @param request: RecognizeVehicleRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleRegistrationResponse
        """
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
        """
        @summary 机动车注册登记证识别
        
        @param request: RecognizeVehicleRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeVehicleRegistrationResponse
        """
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
        """
        @summary 机动车注册登记证识别
        
        @param request: RecognizeVehicleRegistrationRequest
        @return: RecognizeVehicleRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_registration_with_options(request, runtime)

    async def recognize_vehicle_registration_async(
        self,
        request: ocr_api_20210707_models.RecognizeVehicleRegistrationRequest,
    ) -> ocr_api_20210707_models.RecognizeVehicleRegistrationResponse:
        """
        @summary 机动车注册登记证识别
        
        @param request: RecognizeVehicleRegistrationRequest
        @return: RecognizeVehicleRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_registration_with_options_async(request, runtime)

    def recognize_waybill_with_options(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        """
        @summary 电子面单识别
        
        @param request: RecognizeWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeWaybillResponse
        """
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
        """
        @summary 电子面单识别
        
        @param request: RecognizeWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecognizeWaybillResponse
        """
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
        """
        @summary 电子面单识别
        
        @param request: RecognizeWaybillRequest
        @return: RecognizeWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recognize_waybill_with_options(request, runtime)

    async def recognize_waybill_async(
        self,
        request: ocr_api_20210707_models.RecognizeWaybillRequest,
    ) -> ocr_api_20210707_models.RecognizeWaybillResponse:
        """
        @summary 电子面单识别
        
        @param request: RecognizeWaybillRequest
        @return: RecognizeWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recognize_waybill_with_options_async(request, runtime)

    def verify_business_license_with_options(
        self,
        request: ocr_api_20210707_models.VerifyBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.VerifyBusinessLicenseResponse:
        """
        @summary 营业执照核验
        
        @param request: VerifyBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.credit_code):
            query['CreditCode'] = request.credit_code
        if not UtilClient.is_unset(request.legal_person):
            query['LegalPerson'] = request.legal_person
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyBusinessLicense',
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
            ocr_api_20210707_models.VerifyBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_business_license_with_options_async(
        self,
        request: ocr_api_20210707_models.VerifyBusinessLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.VerifyBusinessLicenseResponse:
        """
        @summary 营业执照核验
        
        @param request: VerifyBusinessLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyBusinessLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.credit_code):
            query['CreditCode'] = request.credit_code
        if not UtilClient.is_unset(request.legal_person):
            query['LegalPerson'] = request.legal_person
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyBusinessLicense',
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
            ocr_api_20210707_models.VerifyBusinessLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_business_license(
        self,
        request: ocr_api_20210707_models.VerifyBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.VerifyBusinessLicenseResponse:
        """
        @summary 营业执照核验
        
        @param request: VerifyBusinessLicenseRequest
        @return: VerifyBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_business_license_with_options(request, runtime)

    async def verify_business_license_async(
        self,
        request: ocr_api_20210707_models.VerifyBusinessLicenseRequest,
    ) -> ocr_api_20210707_models.VerifyBusinessLicenseResponse:
        """
        @summary 营业执照核验
        
        @param request: VerifyBusinessLicenseRequest
        @return: VerifyBusinessLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_business_license_with_options_async(request, runtime)

    def verify_vatinvoice_with_options(
        self,
        request: ocr_api_20210707_models.VerifyVATInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.VerifyVATInvoiceResponse:
        """
        @summary 增值税发票核验
        
        @param request: VerifyVATInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyVATInvoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invoice_code):
            query['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_date):
            query['InvoiceDate'] = request.invoice_date
        if not UtilClient.is_unset(request.invoice_kind):
            query['InvoiceKind'] = request.invoice_kind
        if not UtilClient.is_unset(request.invoice_no):
            query['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.invoice_sum):
            query['InvoiceSum'] = request.invoice_sum
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyVATInvoice',
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
            ocr_api_20210707_models.VerifyVATInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_vatinvoice_with_options_async(
        self,
        request: ocr_api_20210707_models.VerifyVATInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocr_api_20210707_models.VerifyVATInvoiceResponse:
        """
        @summary 增值税发票核验
        
        @param request: VerifyVATInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyVATInvoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invoice_code):
            query['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_date):
            query['InvoiceDate'] = request.invoice_date
        if not UtilClient.is_unset(request.invoice_kind):
            query['InvoiceKind'] = request.invoice_kind
        if not UtilClient.is_unset(request.invoice_no):
            query['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.invoice_sum):
            query['InvoiceSum'] = request.invoice_sum
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyVATInvoice',
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
            ocr_api_20210707_models.VerifyVATInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_vatinvoice(
        self,
        request: ocr_api_20210707_models.VerifyVATInvoiceRequest,
    ) -> ocr_api_20210707_models.VerifyVATInvoiceResponse:
        """
        @summary 增值税发票核验
        
        @param request: VerifyVATInvoiceRequest
        @return: VerifyVATInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_vatinvoice_with_options(request, runtime)

    async def verify_vatinvoice_async(
        self,
        request: ocr_api_20210707_models.VerifyVATInvoiceRequest,
    ) -> ocr_api_20210707_models.VerifyVATInvoiceResponse:
        """
        @summary 增值税发票核验
        
        @param request: VerifyVATInvoiceRequest
        @return: VerifyVATInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_vatinvoice_with_options_async(request, runtime)
