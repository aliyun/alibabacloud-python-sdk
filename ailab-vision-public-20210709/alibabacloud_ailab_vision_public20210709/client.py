# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ailab_vision_public20210709 import models as ailab_vision_public_20210709_models
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
        self._endpoint = self.get_endpoint('ailab-vision-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def calib(
        self,
        request: ailab_vision_public_20210709_models.CalibRequest,
    ) -> ailab_vision_public_20210709_models.CalibResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.calib_with_options(request, headers, runtime)

    async def calib_async(
        self,
        request: ailab_vision_public_20210709_models.CalibRequest,
    ) -> ailab_vision_public_20210709_models.CalibResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.calib_with_options_async(request, headers, runtime)

    def calib_with_options(
        self,
        request: ailab_vision_public_20210709_models.CalibRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.CalibResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.floor_id):
            body['floorId'] = request.floor_id
        if not UtilClient.is_unset(request.camera_id):
            body['cameraId'] = request.camera_id
        if not UtilClient.is_unset(request.feature_match):
            body['featureMatch'] = request.feature_match
        if not UtilClient.is_unset(request.camera_type):
            body['cameraType'] = request.camera_type
        if not UtilClient.is_unset(request.zoom_level):
            body['zoomLevel'] = request.zoom_level
        if not UtilClient.is_unset(request.kpts_num):
            body['kptsNum'] = request.kpts_num
        if not UtilClient.is_unset(request.reproject_thresh):
            body['reprojectThresh'] = request.reproject_thresh
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.CalibResponse(),
            self.do_roarequest('Calib', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/calib', 'json', req, runtime)
        )

    async def calib_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.CalibRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.CalibResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.floor_id):
            body['floorId'] = request.floor_id
        if not UtilClient.is_unset(request.camera_id):
            body['cameraId'] = request.camera_id
        if not UtilClient.is_unset(request.feature_match):
            body['featureMatch'] = request.feature_match
        if not UtilClient.is_unset(request.camera_type):
            body['cameraType'] = request.camera_type
        if not UtilClient.is_unset(request.zoom_level):
            body['zoomLevel'] = request.zoom_level
        if not UtilClient.is_unset(request.kpts_num):
            body['kptsNum'] = request.kpts_num
        if not UtilClient.is_unset(request.reproject_thresh):
            body['reprojectThresh'] = request.reproject_thresh
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.CalibResponse(),
            await self.do_roarequest_async('Calib', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/calib', 'json', req, runtime)
        )

    def reid_body(
        self,
        request: ailab_vision_public_20210709_models.ReidBodyRequest,
    ) -> ailab_vision_public_20210709_models.ReidBodyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reid_body_with_options(request, headers, runtime)

    async def reid_body_async(
        self,
        request: ailab_vision_public_20210709_models.ReidBodyRequest,
    ) -> ailab_vision_public_20210709_models.ReidBodyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reid_body_with_options_async(request, headers, runtime)

    def reid_body_with_options(
        self,
        request: ailab_vision_public_20210709_models.ReidBodyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.ReidBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.ReidBodyResponse(),
            self.do_roarequest('ReidBody', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/reid_pub', 'json', req, runtime)
        )

    async def reid_body_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.ReidBodyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.ReidBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.ReidBodyResponse(),
            await self.do_roarequest_async('ReidBody', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/reid_pub', 'json', req, runtime)
        )

    def attr_body(
        self,
        request: ailab_vision_public_20210709_models.AttrBodyRequest,
    ) -> ailab_vision_public_20210709_models.AttrBodyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attr_body_with_options(request, headers, runtime)

    async def attr_body_async(
        self,
        request: ailab_vision_public_20210709_models.AttrBodyRequest,
    ) -> ailab_vision_public_20210709_models.AttrBodyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attr_body_with_options_async(request, headers, runtime)

    def attr_body_with_options(
        self,
        request: ailab_vision_public_20210709_models.AttrBodyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.AttrBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.AttrBodyResponse(),
            self.do_roarequest('AttrBody', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/attr_body', 'json', req, runtime)
        )

    async def attr_body_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.AttrBodyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.AttrBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.AttrBodyResponse(),
            await self.do_roarequest_async('AttrBody', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/attr_body', 'json', req, runtime)
        )

    def reid_face(
        self,
        request: ailab_vision_public_20210709_models.ReidFaceRequest,
    ) -> ailab_vision_public_20210709_models.ReidFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reid_face_with_options(request, headers, runtime)

    async def reid_face_async(
        self,
        request: ailab_vision_public_20210709_models.ReidFaceRequest,
    ) -> ailab_vision_public_20210709_models.ReidFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reid_face_with_options_async(request, headers, runtime)

    def reid_face_with_options(
        self,
        request: ailab_vision_public_20210709_models.ReidFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.ReidFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.ReidFaceResponse(),
            self.do_roarequest('ReidFace', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/reid_face', 'json', req, runtime)
        )

    async def reid_face_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.ReidFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.ReidFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.ReidFaceResponse(),
            await self.do_roarequest_async('ReidFace', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/reid_face', 'json', req, runtime)
        )

    def attr_face(
        self,
        request: ailab_vision_public_20210709_models.AttrFaceRequest,
    ) -> ailab_vision_public_20210709_models.AttrFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attr_face_with_options(request, headers, runtime)

    async def attr_face_async(
        self,
        request: ailab_vision_public_20210709_models.AttrFaceRequest,
    ) -> ailab_vision_public_20210709_models.AttrFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attr_face_with_options_async(request, headers, runtime)

    def attr_face_with_options(
        self,
        request: ailab_vision_public_20210709_models.AttrFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.AttrFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.AttrFaceResponse(),
            self.do_roarequest('AttrFace', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/attr_face', 'json', req, runtime)
        )

    async def attr_face_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.AttrFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.AttrFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.AttrFaceResponse(),
            await self.do_roarequest_async('AttrFace', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/attr_face', 'json', req, runtime)
        )

    def match(
        self,
        request: ailab_vision_public_20210709_models.MatchRequest,
    ) -> ailab_vision_public_20210709_models.MatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.match_with_options(request, headers, runtime)

    async def match_async(
        self,
        request: ailab_vision_public_20210709_models.MatchRequest,
    ) -> ailab_vision_public_20210709_models.MatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.match_with_options_async(request, headers, runtime)

    def match_with_options(
        self,
        request: ailab_vision_public_20210709_models.MatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.MatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.floor_id):
            body['floorId'] = request.floor_id
        if not UtilClient.is_unset(request.camera_id):
            body['cameraId'] = request.camera_id
        if not UtilClient.is_unset(request.camera_coord):
            body['cameraCoord'] = request.camera_coord
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.MatchResponse(),
            self.do_roarequest('Match', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/match', 'json', req, runtime)
        )

    async def match_with_options_async(
        self,
        request: ailab_vision_public_20210709_models.MatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ailab_vision_public_20210709_models.MatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.floor_id):
            body['floorId'] = request.floor_id
        if not UtilClient.is_unset(request.camera_id):
            body['cameraId'] = request.camera_id
        if not UtilClient.is_unset(request.camera_coord):
            body['cameraCoord'] = request.camera_coord
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            ailab_vision_public_20210709_models.MatchResponse(),
            await self.do_roarequest_async('Match', '2021-07-09', 'HTTPS', 'POST', 'AK', f'/api/predict/match', 'json', req, runtime)
        )
