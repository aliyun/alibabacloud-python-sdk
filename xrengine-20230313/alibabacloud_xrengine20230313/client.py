# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xrengine20230313 import models as xr_engine_20230313_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'xrengine-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'xrengine-daily.aliyuncs.com',
            'ap-south-1': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-1': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-2': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-3': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-5': 'xrengine-daily.aliyuncs.com',
            'cn-beijing': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'xrengine-daily.aliyuncs.com',
            'cn-chengdu': 'xrengine-daily.aliyuncs.com',
            'cn-edge-1': 'xrengine-daily.aliyuncs.com',
            'cn-fujian': 'xrengine-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'xrengine-daily.aliyuncs.com',
            'cn-hongkong': 'xrengine-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'xrengine-daily.aliyuncs.com',
            'cn-huhehaote': 'xrengine-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'xrengine-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'xrengine-daily.aliyuncs.com',
            'cn-qingdao': 'xrengine-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-et15-b01': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-inner': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'xrengine-daily.aliyuncs.com',
            'cn-wuhan': 'xrengine-daily.aliyuncs.com',
            'cn-wulanchabu': 'xrengine-daily.aliyuncs.com',
            'cn-yushanfang': 'xrengine-daily.aliyuncs.com',
            'cn-zhangbei': 'xrengine-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'xrengine-daily.aliyuncs.com',
            'cn-zhangjiakou': 'xrengine-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'xrengine-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'xrengine-daily.aliyuncs.com',
            'eu-central-1': 'xrengine-daily.aliyuncs.com',
            'eu-west-1': 'xrengine-daily.aliyuncs.com',
            'eu-west-1-oxs': 'xrengine-daily.aliyuncs.com',
            'me-east-1': 'xrengine-daily.aliyuncs.com',
            'rus-west-1-pop': 'xrengine-daily.aliyuncs.com',
            'us-east-1': 'xrengine-daily.aliyuncs.com',
            'us-west-1': 'xrengine-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('xrengine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_map_data_with_options(
        self,
        request: xr_engine_20230313_models.GetMapDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.GetMapDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_map_data_with_options_async(
        self,
        request: xr_engine_20230313_models.GetMapDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.GetMapDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_map_data(
        self,
        request: xr_engine_20230313_models.GetMapDataRequest,
    ) -> xr_engine_20230313_models.GetMapDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_map_data_with_options(request, runtime)

    async def get_map_data_async(
        self,
        request: xr_engine_20230313_models.GetMapDataRequest,
    ) -> xr_engine_20230313_models.GetMapDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_map_data_with_options_async(request, runtime)

    def get_map_publish_data_with_options(
        self,
        request: xr_engine_20230313_models.GetMapPublishDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.GetMapPublishDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapPublishData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapPublishDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_map_publish_data_with_options_async(
        self,
        request: xr_engine_20230313_models.GetMapPublishDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.GetMapPublishDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapPublishData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapPublishDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_map_publish_data(
        self,
        request: xr_engine_20230313_models.GetMapPublishDataRequest,
    ) -> xr_engine_20230313_models.GetMapPublishDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_map_publish_data_with_options(request, runtime)

    async def get_map_publish_data_async(
        self,
        request: xr_engine_20230313_models.GetMapPublishDataRequest,
    ) -> xr_engine_20230313_models.GetMapPublishDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_map_publish_data_with_options_async(request, runtime)

    def init_locate_with_options(
        self,
        request: xr_engine_20230313_models.InitLocateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.InitLocateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitLocate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.InitLocateResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_locate_with_options_async(
        self,
        request: xr_engine_20230313_models.InitLocateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.InitLocateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitLocate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.InitLocateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_locate(
        self,
        request: xr_engine_20230313_models.InitLocateRequest,
    ) -> xr_engine_20230313_models.InitLocateResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_locate_with_options(request, runtime)

    async def init_locate_async(
        self,
        request: xr_engine_20230313_models.InitLocateRequest,
    ) -> xr_engine_20230313_models.InitLocateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_locate_with_options_async(request, runtime)

    def list_location_service_with_options(
        self,
        request: xr_engine_20230313_models.ListLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.ListLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLocationService',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.ListLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_location_service_with_options_async(
        self,
        request: xr_engine_20230313_models.ListLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.ListLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLocationService',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.ListLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_location_service(
        self,
        request: xr_engine_20230313_models.ListLocationServiceRequest,
    ) -> xr_engine_20230313_models.ListLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_location_service_with_options(request, runtime)

    async def list_location_service_async(
        self,
        request: xr_engine_20230313_models.ListLocationServiceRequest,
    ) -> xr_engine_20230313_models.ListLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_location_service_with_options_async(request, runtime)

    def locate_with_options(
        self,
        request: xr_engine_20230313_models.LocateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.LocateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Locate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.LocateResponse(),
            self.call_api(params, req, runtime)
        )

    async def locate_with_options_async(
        self,
        request: xr_engine_20230313_models.LocateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.LocateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Locate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.LocateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def locate(
        self,
        request: xr_engine_20230313_models.LocateRequest,
    ) -> xr_engine_20230313_models.LocateResponse:
        runtime = util_models.RuntimeOptions()
        return self.locate_with_options(request, runtime)

    async def locate_async(
        self,
        request: xr_engine_20230313_models.LocateRequest,
    ) -> xr_engine_20230313_models.LocateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.locate_with_options_async(request, runtime)

    def pop_batch_query_object_project_status_with_options(
        self,
        request: xr_engine_20230313_models.PopBatchQueryObjectProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_ids):
            body['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBatchQueryObjectProjectStatus',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_batch_query_object_project_status_with_options_async(
        self,
        request: xr_engine_20230313_models.PopBatchQueryObjectProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_ids):
            body['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBatchQueryObjectProjectStatus',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_batch_query_object_project_status(
        self,
        request: xr_engine_20230313_models.PopBatchQueryObjectProjectStatusRequest,
    ) -> xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_batch_query_object_project_status_with_options(request, runtime)

    async def pop_batch_query_object_project_status_async(
        self,
        request: xr_engine_20230313_models.PopBatchQueryObjectProjectStatusRequest,
    ) -> xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_batch_query_object_project_status_with_options_async(request, runtime)

    def pop_build_feature_to_avatar_project_with_options(
        self,
        request: xr_engine_20230313_models.PopBuildFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_build_feature_to_avatar_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopBuildFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_build_feature_to_avatar_project(
        self,
        request: xr_engine_20230313_models.PopBuildFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_build_feature_to_avatar_project_with_options(request, runtime)

    async def pop_build_feature_to_avatar_project_async(
        self,
        request: xr_engine_20230313_models.PopBuildFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_build_feature_to_avatar_project_with_options_async(request, runtime)

    def pop_build_object_project_with_options(
        self,
        request: xr_engine_20230313_models.PopBuildObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBuildObjectProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopBuildObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_build_object_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopBuildObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopBuildObjectProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopBuildObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildObjectProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_build_object_project(
        self,
        request: xr_engine_20230313_models.PopBuildObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopBuildObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_build_object_project_with_options(request, runtime)

    async def pop_build_object_project_async(
        self,
        request: xr_engine_20230313_models.PopBuildObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopBuildObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_build_object_project_with_options_async(request, runtime)

    def pop_create_feature_to_avatar_project_with_options(
        self,
        request: xr_engine_20230313_models.PopCreateFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_create_feature_to_avatar_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopCreateFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_create_feature_to_avatar_project(
        self,
        request: xr_engine_20230313_models.PopCreateFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_create_feature_to_avatar_project_with_options(request, runtime)

    async def pop_create_feature_to_avatar_project_async(
        self,
        request: xr_engine_20230313_models.PopCreateFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_create_feature_to_avatar_project_with_options_async(request, runtime)

    def pop_create_object_project_with_options(
        self,
        request: xr_engine_20230313_models.PopCreateObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopCreateObjectProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_build):
            body['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.dependencies):
            body['Dependencies'] = request.dependencies
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_create_object_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopCreateObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopCreateObjectProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_build):
            body['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.dependencies):
            body['Dependencies'] = request.dependencies
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateObjectProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_create_object_project(
        self,
        request: xr_engine_20230313_models.PopCreateObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopCreateObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_create_object_project_with_options(request, runtime)

    async def pop_create_object_project_async(
        self,
        request: xr_engine_20230313_models.PopCreateObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopCreateObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_create_object_project_with_options_async(request, runtime)

    def pop_list_feature_to_avatar_materials_with_options(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.list_status):
            body['ListStatus'] = request.list_status
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarMaterials',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_list_feature_to_avatar_materials_with_options_async(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.list_status):
            body['ListStatus'] = request.list_status
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarMaterials',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_list_feature_to_avatar_materials(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarMaterialsRequest,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_list_feature_to_avatar_materials_with_options(request, runtime)

    async def pop_list_feature_to_avatar_materials_async(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarMaterialsRequest,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_list_feature_to_avatar_materials_with_options_async(request, runtime)

    def pop_list_feature_to_avatar_project_with_options(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_list_feature_to_avatar_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_list_feature_to_avatar_project(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_list_feature_to_avatar_project_with_options(request, runtime)

    async def pop_list_feature_to_avatar_project_async(
        self,
        request: xr_engine_20230313_models.PopListFeatureToAvatarProjectRequest,
    ) -> xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_list_feature_to_avatar_project_with_options_async(request, runtime)

    def pop_list_object_project_with_options(
        self,
        request: xr_engine_20230313_models.PopListObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListObjectProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_list_object_project_with_options_async(
        self,
        request: xr_engine_20230313_models.PopListObjectProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopListObjectProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListObjectProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_list_object_project(
        self,
        request: xr_engine_20230313_models.PopListObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopListObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_list_object_project_with_options(request, runtime)

    async def pop_list_object_project_async(
        self,
        request: xr_engine_20230313_models.PopListObjectProjectRequest,
    ) -> xr_engine_20230313_models.PopListObjectProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_list_object_project_with_options_async(request, runtime)

    def pop_object_project_detail_with_options(
        self,
        request: xr_engine_20230313_models.PopObjectProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopObjectProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopObjectProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopObjectProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def pop_object_project_detail_with_options_async(
        self,
        request: xr_engine_20230313_models.PopObjectProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20230313_models.PopObjectProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopObjectProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopObjectProjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pop_object_project_detail(
        self,
        request: xr_engine_20230313_models.PopObjectProjectDetailRequest,
    ) -> xr_engine_20230313_models.PopObjectProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.pop_object_project_detail_with_options(request, runtime)

    async def pop_object_project_detail_async(
        self,
        request: xr_engine_20230313_models.PopObjectProjectDetailRequest,
    ) -> xr_engine_20230313_models.PopObjectProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pop_object_project_detail_with_options_async(request, runtime)
