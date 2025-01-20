# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iqs20240712 import models as iqs20240712_models
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
        self._endpoint = self.get_endpoint('iqs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bicycling_direction_nova_with_options(
        self,
        request: iqs20240712_models.BicyclingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.BicyclingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的骑行路线规划方案
        
        @param request: BicyclingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BicyclingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BicyclingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/bicycling',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.BicyclingDirectionNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.BicyclingDirectionNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def bicycling_direction_nova_with_options_async(
        self,
        request: iqs20240712_models.BicyclingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.BicyclingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的骑行路线规划方案
        
        @param request: BicyclingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BicyclingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BicyclingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/bicycling',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.BicyclingDirectionNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.BicyclingDirectionNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def bicycling_direction_nova(
        self,
        request: iqs20240712_models.BicyclingDirectionNovaRequest,
    ) -> iqs20240712_models.BicyclingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的骑行路线规划方案
        
        @param request: BicyclingDirectionNovaRequest
        @return: BicyclingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bicycling_direction_nova_with_options(request, headers, runtime)

    async def bicycling_direction_nova_async(
        self,
        request: iqs20240712_models.BicyclingDirectionNovaRequest,
    ) -> iqs20240712_models.BicyclingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的骑行路线规划方案
        
        @param request: BicyclingDirectionNovaRequest
        @return: BicyclingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bicycling_direction_nova_with_options_async(request, headers, runtime)

    def common_query_by_scene_with_options(
        self,
        request: iqs20240712_models.CommonQueryBySceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.CommonQueryBySceneResponse:
        """
        @summary 自然语言通用查询
        
        @param request: CommonQueryBySceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommonQueryBySceneResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CommonQueryByScene',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/common',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.CommonQueryBySceneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.CommonQueryBySceneResponse(),
                self.execute(params, req, runtime)
            )

    async def common_query_by_scene_with_options_async(
        self,
        request: iqs20240712_models.CommonQueryBySceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.CommonQueryBySceneResponse:
        """
        @summary 自然语言通用查询
        
        @param request: CommonQueryBySceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommonQueryBySceneResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CommonQueryByScene',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/common',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.CommonQueryBySceneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.CommonQueryBySceneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def common_query_by_scene(
        self,
        request: iqs20240712_models.CommonQueryBySceneRequest,
    ) -> iqs20240712_models.CommonQueryBySceneResponse:
        """
        @summary 自然语言通用查询
        
        @param request: CommonQueryBySceneRequest
        @return: CommonQueryBySceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.common_query_by_scene_with_options(request, headers, runtime)

    async def common_query_by_scene_async(
        self,
        request: iqs20240712_models.CommonQueryBySceneRequest,
    ) -> iqs20240712_models.CommonQueryBySceneResponse:
        """
        @summary 自然语言通用查询
        
        @param request: CommonQueryBySceneRequest
        @return: CommonQueryBySceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.common_query_by_scene_with_options_async(request, headers, runtime)

    def driving_direction_nova_with_options(
        self,
        request: iqs20240712_models.DrivingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.DrivingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的驾车路线规划方案
        
        @param request: DrivingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DrivingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.car_type):
            query['carType'] = request.car_type
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        if not UtilClient.is_unset(request.plate):
            query['plate'] = request.plate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DrivingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/driving',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.DrivingDirectionNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.DrivingDirectionNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def driving_direction_nova_with_options_async(
        self,
        request: iqs20240712_models.DrivingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.DrivingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的驾车路线规划方案
        
        @param request: DrivingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DrivingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.car_type):
            query['carType'] = request.car_type
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        if not UtilClient.is_unset(request.plate):
            query['plate'] = request.plate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DrivingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/driving',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.DrivingDirectionNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.DrivingDirectionNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def driving_direction_nova(
        self,
        request: iqs20240712_models.DrivingDirectionNovaRequest,
    ) -> iqs20240712_models.DrivingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的驾车路线规划方案
        
        @param request: DrivingDirectionNovaRequest
        @return: DrivingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.driving_direction_nova_with_options(request, headers, runtime)

    async def driving_direction_nova_async(
        self,
        request: iqs20240712_models.DrivingDirectionNovaRequest,
    ) -> iqs20240712_models.DrivingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的驾车路线规划方案
        
        @param request: DrivingDirectionNovaRequest
        @return: DrivingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.driving_direction_nova_with_options_async(request, headers, runtime)

    def electrobike_direction_nova_with_options(
        self,
        request: iqs20240712_models.ElectrobikeDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.ElectrobikeDirectionNovaResponse:
        """
        @summary 电动车路线规划方案V2
        
        @param request: ElectrobikeDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ElectrobikeDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ElectrobikeDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/electrobike',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.ElectrobikeDirectionNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.ElectrobikeDirectionNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def electrobike_direction_nova_with_options_async(
        self,
        request: iqs20240712_models.ElectrobikeDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.ElectrobikeDirectionNovaResponse:
        """
        @summary 电动车路线规划方案V2
        
        @param request: ElectrobikeDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ElectrobikeDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ElectrobikeDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/electrobike',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.ElectrobikeDirectionNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.ElectrobikeDirectionNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def electrobike_direction_nova(
        self,
        request: iqs20240712_models.ElectrobikeDirectionNovaRequest,
    ) -> iqs20240712_models.ElectrobikeDirectionNovaResponse:
        """
        @summary 电动车路线规划方案V2
        
        @param request: ElectrobikeDirectionNovaRequest
        @return: ElectrobikeDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.electrobike_direction_nova_with_options(request, headers, runtime)

    async def electrobike_direction_nova_async(
        self,
        request: iqs20240712_models.ElectrobikeDirectionNovaRequest,
    ) -> iqs20240712_models.ElectrobikeDirectionNovaResponse:
        """
        @summary 电动车路线规划方案V2
        
        @param request: ElectrobikeDirectionNovaRequest
        @return: ElectrobikeDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.electrobike_direction_nova_with_options_async(request, headers, runtime)

    def geo_code_with_options(
        self,
        request: iqs20240712_models.GeoCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.GeoCodeResponse:
        """
        @summary 地理编码，将详细的结构化地址转换为高德经纬度坐标
        
        @param request: GeoCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GeoCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['city'] = request.city
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GeoCode',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v1/geocode/geo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.GeoCodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.GeoCodeResponse(),
                self.execute(params, req, runtime)
            )

    async def geo_code_with_options_async(
        self,
        request: iqs20240712_models.GeoCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.GeoCodeResponse:
        """
        @summary 地理编码，将详细的结构化地址转换为高德经纬度坐标
        
        @param request: GeoCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GeoCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['city'] = request.city
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GeoCode',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v1/geocode/geo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.GeoCodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.GeoCodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def geo_code(
        self,
        request: iqs20240712_models.GeoCodeRequest,
    ) -> iqs20240712_models.GeoCodeResponse:
        """
        @summary 地理编码，将详细的结构化地址转换为高德经纬度坐标
        
        @param request: GeoCodeRequest
        @return: GeoCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.geo_code_with_options(request, headers, runtime)

    async def geo_code_async(
        self,
        request: iqs20240712_models.GeoCodeRequest,
    ) -> iqs20240712_models.GeoCodeResponse:
        """
        @summary 地理编码，将详细的结构化地址转换为高德经纬度坐标
        
        @param request: GeoCodeRequest
        @return: GeoCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.geo_code_with_options_async(request, headers, runtime)

    def nearby_search_nova_with_options(
        self,
        request: iqs20240712_models.NearbySearchNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.NearbySearchNovaResponse:
        """
        @summary 通过经纬度查询附近的地点
        
        @param request: NearbySearchNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: NearbySearchNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_limit):
            query['cityLimit'] = request.city_limit
        if not UtilClient.is_unset(request.keywords):
            query['keywords'] = request.keywords
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.radius):
            query['radius'] = request.radius
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.sort_rule):
            query['sortRule'] = request.sort_rule
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NearbySearchNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/pois/nearby',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.NearbySearchNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.NearbySearchNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def nearby_search_nova_with_options_async(
        self,
        request: iqs20240712_models.NearbySearchNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.NearbySearchNovaResponse:
        """
        @summary 通过经纬度查询附近的地点
        
        @param request: NearbySearchNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: NearbySearchNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_limit):
            query['cityLimit'] = request.city_limit
        if not UtilClient.is_unset(request.keywords):
            query['keywords'] = request.keywords
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.radius):
            query['radius'] = request.radius
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.sort_rule):
            query['sortRule'] = request.sort_rule
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NearbySearchNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/pois/nearby',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.NearbySearchNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.NearbySearchNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def nearby_search_nova(
        self,
        request: iqs20240712_models.NearbySearchNovaRequest,
    ) -> iqs20240712_models.NearbySearchNovaResponse:
        """
        @summary 通过经纬度查询附近的地点
        
        @param request: NearbySearchNovaRequest
        @return: NearbySearchNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.nearby_search_nova_with_options(request, headers, runtime)

    async def nearby_search_nova_async(
        self,
        request: iqs20240712_models.NearbySearchNovaRequest,
    ) -> iqs20240712_models.NearbySearchNovaResponse:
        """
        @summary 通过经纬度查询附近的地点
        
        @param request: NearbySearchNovaRequest
        @return: NearbySearchNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.nearby_search_nova_with_options_async(request, headers, runtime)

    def place_search_nova_with_options(
        self,
        request: iqs20240712_models.PlaceSearchNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.PlaceSearchNovaResponse:
        """
        @summary 通过关键词搜索地点
        
        @param request: PlaceSearchNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PlaceSearchNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_limit):
            query['cityLimit'] = request.city_limit
        if not UtilClient.is_unset(request.keywords):
            query['keywords'] = request.keywords
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlaceSearchNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/pois/place',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.PlaceSearchNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.PlaceSearchNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def place_search_nova_with_options_async(
        self,
        request: iqs20240712_models.PlaceSearchNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.PlaceSearchNovaResponse:
        """
        @summary 通过关键词搜索地点
        
        @param request: PlaceSearchNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PlaceSearchNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_limit):
            query['cityLimit'] = request.city_limit
        if not UtilClient.is_unset(request.keywords):
            query['keywords'] = request.keywords
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlaceSearchNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/pois/place',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.PlaceSearchNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.PlaceSearchNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def place_search_nova(
        self,
        request: iqs20240712_models.PlaceSearchNovaRequest,
    ) -> iqs20240712_models.PlaceSearchNovaResponse:
        """
        @summary 通过关键词搜索地点
        
        @param request: PlaceSearchNovaRequest
        @return: PlaceSearchNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.place_search_nova_with_options(request, headers, runtime)

    async def place_search_nova_async(
        self,
        request: iqs20240712_models.PlaceSearchNovaRequest,
    ) -> iqs20240712_models.PlaceSearchNovaResponse:
        """
        @summary 通过关键词搜索地点
        
        @param request: PlaceSearchNovaRequest
        @return: PlaceSearchNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.place_search_nova_with_options_async(request, headers, runtime)

    def query_attractions_with_options(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractions',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsResponse(),
                self.execute(params, req, runtime)
            )

    async def query_attractions_with_options_async(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractions',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_attractions(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @return: QueryAttractionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_attractions_with_options(request, headers, runtime)

    async def query_attractions_async(
        self,
        request: iqs20240712_models.QueryAttractionsRequest,
    ) -> iqs20240712_models.QueryAttractionsResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsRequest
        @return: QueryAttractionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_attractions_with_options_async(request, headers, runtime)

    def query_attractions_nl_with_options(
        self,
        request: iqs20240712_models.QueryAttractionsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsNlResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractionsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsNlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsNlResponse(),
                self.execute(params, req, runtime)
            )

    async def query_attractions_nl_with_options_async(
        self,
        request: iqs20240712_models.QueryAttractionsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryAttractionsNlResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAttractionsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryAttractionsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/attractions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsNlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryAttractionsNlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_attractions_nl(
        self,
        request: iqs20240712_models.QueryAttractionsNlRequest,
    ) -> iqs20240712_models.QueryAttractionsNlResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsNlRequest
        @return: QueryAttractionsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_attractions_nl_with_options(request, headers, runtime)

    async def query_attractions_nl_async(
        self,
        request: iqs20240712_models.QueryAttractionsNlRequest,
    ) -> iqs20240712_models.QueryAttractionsNlResponse:
        """
        @summary 景点查询
        
        @param request: QueryAttractionsNlRequest
        @return: QueryAttractionsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_attractions_nl_with_options_async(request, headers, runtime)

    def query_hotels_with_options(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotels',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsResponse(),
                self.execute(params, req, runtime)
            )

    async def query_hotels_with_options_async(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotels',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_hotels(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsRequest
        @return: QueryHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_hotels_with_options(request, headers, runtime)

    async def query_hotels_async(
        self,
        request: iqs20240712_models.QueryHotelsRequest,
    ) -> iqs20240712_models.QueryHotelsResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsRequest
        @return: QueryHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_hotels_with_options_async(request, headers, runtime)

    def query_hotels_nl_with_options(
        self,
        request: iqs20240712_models.QueryHotelsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsNlResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotelsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsNlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsNlResponse(),
                self.execute(params, req, runtime)
            )

    async def query_hotels_nl_with_options_async(
        self,
        request: iqs20240712_models.QueryHotelsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryHotelsNlResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryHotelsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/hotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsNlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryHotelsNlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_hotels_nl(
        self,
        request: iqs20240712_models.QueryHotelsNlRequest,
    ) -> iqs20240712_models.QueryHotelsNlResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsNlRequest
        @return: QueryHotelsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_hotels_nl_with_options(request, headers, runtime)

    async def query_hotels_nl_async(
        self,
        request: iqs20240712_models.QueryHotelsNlRequest,
    ) -> iqs20240712_models.QueryHotelsNlResponse:
        """
        @summary 酒店查询
        
        @param request: QueryHotelsNlRequest
        @return: QueryHotelsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_hotels_nl_with_options_async(request, headers, runtime)

    def query_restaurants_with_options(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurants',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsResponse(),
                self.execute(params, req, runtime)
            )

    async def query_restaurants_with_options_async(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurants',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v1/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_restaurants(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @return: QueryRestaurantsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_restaurants_with_options(request, headers, runtime)

    async def query_restaurants_async(
        self,
        request: iqs20240712_models.QueryRestaurantsRequest,
    ) -> iqs20240712_models.QueryRestaurantsResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsRequest
        @return: QueryRestaurantsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_restaurants_with_options_async(request, headers, runtime)

    def query_restaurants_nl_with_options(
        self,
        request: iqs20240712_models.QueryRestaurantsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsNlResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurantsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsNlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsNlResponse(),
                self.execute(params, req, runtime)
            )

    async def query_restaurants_nl_with_options_async(
        self,
        request: iqs20240712_models.QueryRestaurantsNlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.QueryRestaurantsNlResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsNlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRestaurantsNlResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryRestaurantsNl',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/amap-function-call-agent/iqs-agent-service/v2/nl/restaurants',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsNlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.QueryRestaurantsNlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_restaurants_nl(
        self,
        request: iqs20240712_models.QueryRestaurantsNlRequest,
    ) -> iqs20240712_models.QueryRestaurantsNlResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsNlRequest
        @return: QueryRestaurantsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_restaurants_nl_with_options(request, headers, runtime)

    async def query_restaurants_nl_async(
        self,
        request: iqs20240712_models.QueryRestaurantsNlRequest,
    ) -> iqs20240712_models.QueryRestaurantsNlResponse:
        """
        @summary 餐厅查询
        
        @param request: QueryRestaurantsNlRequest
        @return: QueryRestaurantsNlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_restaurants_nl_with_options_async(request, headers, runtime)

    def rgeo_code_with_options(
        self,
        request: iqs20240712_models.RgeoCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.RgeoCodeResponse:
        """
        @summary 逆地理编码，将经纬度转换为详细结构化的地址信息
        
        @param request: RgeoCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RgeoCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RgeoCode',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v1/geocode/regeo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.RgeoCodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.RgeoCodeResponse(),
                self.execute(params, req, runtime)
            )

    async def rgeo_code_with_options_async(
        self,
        request: iqs20240712_models.RgeoCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.RgeoCodeResponse:
        """
        @summary 逆地理编码，将经纬度转换为详细结构化的地址信息
        
        @param request: RgeoCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RgeoCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RgeoCode',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v1/geocode/regeo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.RgeoCodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.RgeoCodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def rgeo_code(
        self,
        request: iqs20240712_models.RgeoCodeRequest,
    ) -> iqs20240712_models.RgeoCodeResponse:
        """
        @summary 逆地理编码，将经纬度转换为详细结构化的地址信息
        
        @param request: RgeoCodeRequest
        @return: RgeoCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rgeo_code_with_options(request, headers, runtime)

    async def rgeo_code_async(
        self,
        request: iqs20240712_models.RgeoCodeRequest,
    ) -> iqs20240712_models.RgeoCodeResponse:
        """
        @summary 逆地理编码，将经纬度转换为详细结构化的地址信息
        
        @param request: RgeoCodeRequest
        @return: RgeoCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rgeo_code_with_options_async(request, headers, runtime)

    def transit_integrated_direction_with_options(
        self,
        request: iqs20240712_models.TransitIntegratedDirectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.TransitIntegratedDirectionResponse:
        """
        @summary 公共交通路线规划方案
        
        @param request: TransitIntegratedDirectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransitIntegratedDirectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_city):
            query['destinationCity'] = request.destination_city
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_city):
            query['originCity'] = request.origin_city
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransitIntegratedDirection',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/transit/integrated',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.TransitIntegratedDirectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.TransitIntegratedDirectionResponse(),
                self.execute(params, req, runtime)
            )

    async def transit_integrated_direction_with_options_async(
        self,
        request: iqs20240712_models.TransitIntegratedDirectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.TransitIntegratedDirectionResponse:
        """
        @summary 公共交通路线规划方案
        
        @param request: TransitIntegratedDirectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransitIntegratedDirectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_city):
            query['destinationCity'] = request.destination_city
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_city):
            query['originCity'] = request.origin_city
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransitIntegratedDirection',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/transit/integrated',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.TransitIntegratedDirectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.TransitIntegratedDirectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def transit_integrated_direction(
        self,
        request: iqs20240712_models.TransitIntegratedDirectionRequest,
    ) -> iqs20240712_models.TransitIntegratedDirectionResponse:
        """
        @summary 公共交通路线规划方案
        
        @param request: TransitIntegratedDirectionRequest
        @return: TransitIntegratedDirectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transit_integrated_direction_with_options(request, headers, runtime)

    async def transit_integrated_direction_async(
        self,
        request: iqs20240712_models.TransitIntegratedDirectionRequest,
    ) -> iqs20240712_models.TransitIntegratedDirectionResponse:
        """
        @summary 公共交通路线规划方案
        
        @param request: TransitIntegratedDirectionRequest
        @return: TransitIntegratedDirectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transit_integrated_direction_with_options_async(request, headers, runtime)

    def walking_direction_nova_with_options(
        self,
        request: iqs20240712_models.WalkingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.WalkingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的步行路线规划方案
        
        @param request: WalkingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WalkingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WalkingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/walking',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.WalkingDirectionNovaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.WalkingDirectionNovaResponse(),
                self.execute(params, req, runtime)
            )

    async def walking_direction_nova_with_options_async(
        self,
        request: iqs20240712_models.WalkingDirectionNovaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20240712_models.WalkingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的步行路线规划方案
        
        @param request: WalkingDirectionNovaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WalkingDirectionNovaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_latitude):
            query['destinationLatitude'] = request.destination_latitude
        if not UtilClient.is_unset(request.destination_longitude):
            query['destinationLongitude'] = request.destination_longitude
        if not UtilClient.is_unset(request.origin_latitude):
            query['originLatitude'] = request.origin_latitude
        if not UtilClient.is_unset(request.origin_longitude):
            query['originLongitude'] = request.origin_longitude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WalkingDirectionNova',
            version='2024-07-12',
            protocol='HTTPS',
            pathname=f'/ipaas/v2/direction/walking',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                iqs20240712_models.WalkingDirectionNovaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                iqs20240712_models.WalkingDirectionNovaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def walking_direction_nova(
        self,
        request: iqs20240712_models.WalkingDirectionNovaRequest,
    ) -> iqs20240712_models.WalkingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的步行路线规划方案
        
        @param request: WalkingDirectionNovaRequest
        @return: WalkingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.walking_direction_nova_with_options(request, headers, runtime)

    async def walking_direction_nova_async(
        self,
        request: iqs20240712_models.WalkingDirectionNovaRequest,
    ) -> iqs20240712_models.WalkingDirectionNovaResponse:
        """
        @summary 根据起终点坐标检索符合条件的步行路线规划方案
        
        @param request: WalkingDirectionNovaRequest
        @return: WalkingDirectionNovaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.walking_direction_nova_with_options_async(request, headers, runtime)
