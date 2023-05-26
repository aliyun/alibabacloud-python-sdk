# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ekyc_saas20230112 import models as ekyc_saas_20230112_models
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
        self._endpoint = self.get_endpoint('ekyc-saas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def face_recognition_compare_with_options(
        self,
        request: ekyc_saas_20230112_models.FaceRecognitionCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.FaceRecognitionCompareResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id_card_image_data):
            body['idCardImageData'] = request.id_card_image_data
        if not UtilClient.is_unset(request.id_card_image_type):
            body['idCardImageType'] = request.id_card_image_type
        if not UtilClient.is_unset(request.id_card_image_url):
            body['idCardImageUrl'] = request.id_card_image_url
        if not UtilClient.is_unset(request.portrait_image_data):
            body['portraitImageData'] = request.portrait_image_data
        if not UtilClient.is_unset(request.portrait_image_type):
            body['portraitImageType'] = request.portrait_image_type
        if not UtilClient.is_unset(request.portrait_image_url):
            body['portraitImageUrl'] = request.portrait_image_url
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceRecognitionCompare',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/face_recognition_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.FaceRecognitionCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_recognition_compare_with_options_async(
        self,
        request: ekyc_saas_20230112_models.FaceRecognitionCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.FaceRecognitionCompareResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id_card_image_data):
            body['idCardImageData'] = request.id_card_image_data
        if not UtilClient.is_unset(request.id_card_image_type):
            body['idCardImageType'] = request.id_card_image_type
        if not UtilClient.is_unset(request.id_card_image_url):
            body['idCardImageUrl'] = request.id_card_image_url
        if not UtilClient.is_unset(request.portrait_image_data):
            body['portraitImageData'] = request.portrait_image_data
        if not UtilClient.is_unset(request.portrait_image_type):
            body['portraitImageType'] = request.portrait_image_type
        if not UtilClient.is_unset(request.portrait_image_url):
            body['portraitImageUrl'] = request.portrait_image_url
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceRecognitionCompare',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/face_recognition_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.FaceRecognitionCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_recognition_compare(
        self,
        request: ekyc_saas_20230112_models.FaceRecognitionCompareRequest,
    ) -> ekyc_saas_20230112_models.FaceRecognitionCompareResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.face_recognition_compare_with_options(request, headers, runtime)

    async def face_recognition_compare_async(
        self,
        request: ekyc_saas_20230112_models.FaceRecognitionCompareRequest,
    ) -> ekyc_saas_20230112_models.FaceRecognitionCompareResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.face_recognition_compare_with_options_async(request, headers, runtime)

    def face_to_face_compare_with_options(
        self,
        request: ekyc_saas_20230112_models.FaceToFaceCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.FaceToFaceCompareResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portrait_image_data_1):
            body['portraitImageData1'] = request.portrait_image_data_1
        if not UtilClient.is_unset(request.portrait_image_data_2):
            body['portraitImageData2'] = request.portrait_image_data_2
        if not UtilClient.is_unset(request.portrait_image_type_1):
            body['portraitImageType1'] = request.portrait_image_type_1
        if not UtilClient.is_unset(request.portrait_image_type_2):
            body['portraitImageType2'] = request.portrait_image_type_2
        if not UtilClient.is_unset(request.portrait_image_url_1):
            body['portraitImageUrl1'] = request.portrait_image_url_1
        if not UtilClient.is_unset(request.portrait_image_url_2):
            body['portraitImageUrl2'] = request.portrait_image_url_2
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceToFaceCompare',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/face_to_face_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.FaceToFaceCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_to_face_compare_with_options_async(
        self,
        request: ekyc_saas_20230112_models.FaceToFaceCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.FaceToFaceCompareResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portrait_image_data_1):
            body['portraitImageData1'] = request.portrait_image_data_1
        if not UtilClient.is_unset(request.portrait_image_data_2):
            body['portraitImageData2'] = request.portrait_image_data_2
        if not UtilClient.is_unset(request.portrait_image_type_1):
            body['portraitImageType1'] = request.portrait_image_type_1
        if not UtilClient.is_unset(request.portrait_image_type_2):
            body['portraitImageType2'] = request.portrait_image_type_2
        if not UtilClient.is_unset(request.portrait_image_url_1):
            body['portraitImageUrl1'] = request.portrait_image_url_1
        if not UtilClient.is_unset(request.portrait_image_url_2):
            body['portraitImageUrl2'] = request.portrait_image_url_2
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceToFaceCompare',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/face_to_face_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.FaceToFaceCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_to_face_compare(
        self,
        request: ekyc_saas_20230112_models.FaceToFaceCompareRequest,
    ) -> ekyc_saas_20230112_models.FaceToFaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.face_to_face_compare_with_options(request, headers, runtime)

    async def face_to_face_compare_async(
        self,
        request: ekyc_saas_20230112_models.FaceToFaceCompareRequest,
    ) -> ekyc_saas_20230112_models.FaceToFaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.face_to_face_compare_with_options_async(request, headers, runtime)

    def id_detect_ocr_compare_faces_with_options(
        self,
        request: ekyc_saas_20230112_models.IdDetectOcrCompareFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ocr):
            body['OCR'] = request.ocr
        if not UtilClient.is_unset(request.unrepeat):
            body['Unrepeat'] = request.unrepeat
        if not UtilClient.is_unset(request.card_detect):
            body['cardDetect'] = request.card_detect
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.face_compare):
            body['faceCompare'] = request.face_compare
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        if not UtilClient.is_unset(request.portrait_image_data):
            body['portraitImageData'] = request.portrait_image_data
        if not UtilClient.is_unset(request.portrait_image_url):
            body['portraitImageUrl'] = request.portrait_image_url
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IdDetectOcrCompareFaces',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/id_detect_ocr_compare_faces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_detect_ocr_compare_faces_with_options_async(
        self,
        request: ekyc_saas_20230112_models.IdDetectOcrCompareFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ocr):
            body['OCR'] = request.ocr
        if not UtilClient.is_unset(request.unrepeat):
            body['Unrepeat'] = request.unrepeat
        if not UtilClient.is_unset(request.card_detect):
            body['cardDetect'] = request.card_detect
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.face_compare):
            body['faceCompare'] = request.face_compare
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        if not UtilClient.is_unset(request.portrait_image_data):
            body['portraitImageData'] = request.portrait_image_data
        if not UtilClient.is_unset(request.portrait_image_url):
            body['portraitImageUrl'] = request.portrait_image_url
        if not UtilClient.is_unset(request.quality_control):
            body['qualityControl'] = request.quality_control
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IdDetectOcrCompareFaces',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/id_detect_ocr_compare_faces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_detect_ocr_compare_faces(
        self,
        request: ekyc_saas_20230112_models.IdDetectOcrCompareFacesRequest,
    ) -> ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.id_detect_ocr_compare_faces_with_options(request, headers, runtime)

    async def id_detect_ocr_compare_faces_async(
        self,
        request: ekyc_saas_20230112_models.IdDetectOcrCompareFacesRequest,
    ) -> ekyc_saas_20230112_models.IdDetectOcrCompareFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.id_detect_ocr_compare_faces_with_options_async(request, headers, runtime)

    def id_detection_and_scan_document_with_options(
        self,
        request: ekyc_saas_20230112_models.IdDetectionAndScanDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IdDetectionAndScanDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/id_detection_and_scan_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_detection_and_scan_document_with_options_async(
        self,
        request: ekyc_saas_20230112_models.IdDetectionAndScanDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IdDetectionAndScanDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/id_detection_and_scan_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_detection_and_scan_document(
        self,
        request: ekyc_saas_20230112_models.IdDetectionAndScanDocumentRequest,
    ) -> ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.id_detection_and_scan_document_with_options(request, headers, runtime)

    async def id_detection_and_scan_document_async(
        self,
        request: ekyc_saas_20230112_models.IdDetectionAndScanDocumentRequest,
    ) -> ekyc_saas_20230112_models.IdDetectionAndScanDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.id_detection_and_scan_document_with_options_async(request, headers, runtime)

    def scan_document_with_options(
        self,
        request: ekyc_saas_20230112_models.ScanDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.ScanDocumentResponse:
        """
        After you upload the front-side image and back-side image (optional) of the certificate, the system returns the structured OCR results.
        ### Limits
        *   Format: JPEG or PNG.
        *   Resolution: The length of an image is no greater than 4000 pixels, and the width is no smaller than 400 pixels. Recommended size: 1024\\*768.
        *   Size: the size of a single image. Valid values: \\[4KB, 6MB].
        ### Data protocol
        *   Request: application/json.
        *   Response: application/json.
        *   Binary data: Base64.
        
        @param request: ScanDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/scan_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.ScanDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_document_with_options_async(
        self,
        request: ekyc_saas_20230112_models.ScanDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.ScanDocumentResponse:
        """
        After you upload the front-side image and back-side image (optional) of the certificate, the system returns the structured OCR results.
        ### Limits
        *   Format: JPEG or PNG.
        *   Resolution: The length of an image is no greater than 4000 pixels, and the width is no smaller than 400 pixels. Recommended size: 1024\\*768.
        *   Size: the size of a single image. Valid values: \\[4KB, 6MB].
        ### Data protocol
        *   Request: application/json.
        *   Response: application/json.
        *   Binary data: Base64.
        
        @param request: ScanDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/scan_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.ScanDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_document(
        self,
        request: ekyc_saas_20230112_models.ScanDocumentRequest,
    ) -> ekyc_saas_20230112_models.ScanDocumentResponse:
        """
        After you upload the front-side image and back-side image (optional) of the certificate, the system returns the structured OCR results.
        ### Limits
        *   Format: JPEG or PNG.
        *   Resolution: The length of an image is no greater than 4000 pixels, and the width is no smaller than 400 pixels. Recommended size: 1024\\*768.
        *   Size: the size of a single image. Valid values: \\[4KB, 6MB].
        ### Data protocol
        *   Request: application/json.
        *   Response: application/json.
        *   Binary data: Base64.
        
        @param request: ScanDocumentRequest
        @return: ScanDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_document_with_options(request, headers, runtime)

    async def scan_document_async(
        self,
        request: ekyc_saas_20230112_models.ScanDocumentRequest,
    ) -> ekyc_saas_20230112_models.ScanDocumentResponse:
        """
        After you upload the front-side image and back-side image (optional) of the certificate, the system returns the structured OCR results.
        ### Limits
        *   Format: JPEG or PNG.
        *   Resolution: The length of an image is no greater than 4000 pixels, and the width is no smaller than 400 pixels. Recommended size: 1024\\*768.
        *   Size: the size of a single image. Valid values: \\[4KB, 6MB].
        ### Data protocol
        *   Request: application/json.
        *   Response: application/json.
        *   Binary data: Base64.
        
        @param request: ScanDocumentRequest
        @return: ScanDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scan_document_with_options_async(request, headers, runtime)

    def verify_document_with_options(
        self,
        request: ekyc_saas_20230112_models.VerifyDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.VerifyDocumentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.det_thickness):
            body['detThickness'] = request.det_thickness
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_ctype):
            body['imageCType'] = request.image_ctype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_data_c):
            body['imageDataC'] = request.image_data_c
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        if not UtilClient.is_unset(request.image_url_c):
            body['imageUrlC'] = request.image_url_c
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/verify_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.VerifyDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_document_with_options_async(
        self,
        request: ekyc_saas_20230112_models.VerifyDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ekyc_saas_20230112_models.VerifyDocumentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country_code):
            body['countryCode'] = request.country_code
        if not UtilClient.is_unset(request.det_thickness):
            body['detThickness'] = request.det_thickness
        if not UtilClient.is_unset(request.document_type):
            body['documentType'] = request.document_type
        if not UtilClient.is_unset(request.image_atype):
            body['imageAType'] = request.image_atype
        if not UtilClient.is_unset(request.image_btype):
            body['imageBType'] = request.image_btype
        if not UtilClient.is_unset(request.image_ctype):
            body['imageCType'] = request.image_ctype
        if not UtilClient.is_unset(request.image_data_a):
            body['imageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['imageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_data_c):
            body['imageDataC'] = request.image_data_c
        if not UtilClient.is_unset(request.image_url_a):
            body['imageUrlA'] = request.image_url_a
        if not UtilClient.is_unset(request.image_url_b):
            body['imageUrlB'] = request.image_url_b
        if not UtilClient.is_unset(request.image_url_c):
            body['imageUrlC'] = request.image_url_c
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDocument',
            version='2023-01-12',
            protocol='HTTPS',
            pathname=f'/verify_document',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ekyc_saas_20230112_models.VerifyDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_document(
        self,
        request: ekyc_saas_20230112_models.VerifyDocumentRequest,
    ) -> ekyc_saas_20230112_models.VerifyDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_document_with_options(request, headers, runtime)

    async def verify_document_async(
        self,
        request: ekyc_saas_20230112_models.VerifyDocumentRequest,
    ) -> ekyc_saas_20230112_models.VerifyDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_document_with_options_async(request, headers, runtime)
