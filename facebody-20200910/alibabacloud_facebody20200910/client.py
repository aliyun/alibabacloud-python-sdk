# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_facebody20200910 import models as facebody_20200910_models
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
        self._endpoint = self.get_endpoint('facebody', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def detect_ipcpedestrian_optimized_with_options(
        self,
        request: facebody_20200910_models.DetectIPCPedestrianOptimizedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20200910_models.DetectIPCPedestrianOptimizedResponse:
        """
        行人检测快速版
        
        @param request: DetectIPCPedestrianOptimizedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectIPCPedestrianOptimizedResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_data):
            body['imageData'] = request.image_data
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCPedestrianOptimized',
            version='2020-09-10',
            protocol='HTTPS',
            pathname=f'/viapi/k8s/facebody/detect-ipc-pedestrian-optimized',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20200910_models.DetectIPCPedestrianOptimizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_ipcpedestrian_optimized_with_options_async(
        self,
        request: facebody_20200910_models.DetectIPCPedestrianOptimizedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20200910_models.DetectIPCPedestrianOptimizedResponse:
        """
        行人检测快速版
        
        @param request: DetectIPCPedestrianOptimizedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectIPCPedestrianOptimizedResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_data):
            body['imageData'] = request.image_data
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCPedestrianOptimized',
            version='2020-09-10',
            protocol='HTTPS',
            pathname=f'/viapi/k8s/facebody/detect-ipc-pedestrian-optimized',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20200910_models.DetectIPCPedestrianOptimizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_ipcpedestrian_optimized(
        self,
        request: facebody_20200910_models.DetectIPCPedestrianOptimizedRequest,
    ) -> facebody_20200910_models.DetectIPCPedestrianOptimizedResponse:
        """
        行人检测快速版
        
        @param request: DetectIPCPedestrianOptimizedRequest
        @return: DetectIPCPedestrianOptimizedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detect_ipcpedestrian_optimized_with_options(request, headers, runtime)

    async def detect_ipcpedestrian_optimized_async(
        self,
        request: facebody_20200910_models.DetectIPCPedestrianOptimizedRequest,
    ) -> facebody_20200910_models.DetectIPCPedestrianOptimizedResponse:
        """
        行人检测快速版
        
        @param request: DetectIPCPedestrianOptimizedRequest
        @return: DetectIPCPedestrianOptimizedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detect_ipcpedestrian_optimized_with_options_async(request, headers, runtime)

    def execute_server_side_verification_with_options(
        self,
        request: facebody_20200910_models.ExecuteServerSideVerificationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20200910_models.ExecuteServerSideVerificationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['certificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['certificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.facial_picture_data):
            body['facialPictureData'] = request.facial_picture_data
        if not UtilClient.is_unset(request.facial_picture_url):
            body['facialPictureUrl'] = request.facial_picture_url
        if not UtilClient.is_unset(request.scene_type):
            body['sceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteServerSideVerification',
            version='2020-09-10',
            protocol='HTTPS',
            pathname=f'/viapi/thirdparty/realperson/execServerSideVerification',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20200910_models.ExecuteServerSideVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_server_side_verification_with_options_async(
        self,
        request: facebody_20200910_models.ExecuteServerSideVerificationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20200910_models.ExecuteServerSideVerificationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['certificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['certificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.facial_picture_data):
            body['facialPictureData'] = request.facial_picture_data
        if not UtilClient.is_unset(request.facial_picture_url):
            body['facialPictureUrl'] = request.facial_picture_url
        if not UtilClient.is_unset(request.scene_type):
            body['sceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteServerSideVerification',
            version='2020-09-10',
            protocol='HTTPS',
            pathname=f'/viapi/thirdparty/realperson/execServerSideVerification',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20200910_models.ExecuteServerSideVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_server_side_verification(
        self,
        request: facebody_20200910_models.ExecuteServerSideVerificationRequest,
    ) -> facebody_20200910_models.ExecuteServerSideVerificationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_server_side_verification_with_options(request, headers, runtime)

    async def execute_server_side_verification_async(
        self,
        request: facebody_20200910_models.ExecuteServerSideVerificationRequest,
    ) -> facebody_20200910_models.ExecuteServerSideVerificationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_server_side_verification_with_options_async(request, headers, runtime)
