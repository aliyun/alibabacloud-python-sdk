# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xrengine20221111 import models as xr_engine_20221111_models
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
        self._signature_algorithm = 'v2'
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

    def add_whitelist_with_options(
        self,
        request: xr_engine_20221111_models.AddWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.AddWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWhitelist',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.AddWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_whitelist_with_options_async(
        self,
        request: xr_engine_20221111_models.AddWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.AddWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWhitelist',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.AddWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_whitelist(
        self,
        request: xr_engine_20221111_models.AddWhitelistRequest,
    ) -> xr_engine_20221111_models.AddWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_whitelist_with_options(request, runtime)

    async def add_whitelist_async(
        self,
        request: xr_engine_20221111_models.AddWhitelistRequest,
    ) -> xr_engine_20221111_models.AddWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_whitelist_with_options_async(request, runtime)

    def auth_user_with_options(
        self,
        request: xr_engine_20221111_models.AuthUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.AuthUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthUser',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.AuthUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_user_with_options_async(
        self,
        request: xr_engine_20221111_models.AuthUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.AuthUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthUser',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.AuthUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_user(
        self,
        request: xr_engine_20221111_models.AuthUserRequest,
    ) -> xr_engine_20221111_models.AuthUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.auth_user_with_options(request, runtime)

    async def auth_user_async(
        self,
        request: xr_engine_20221111_models.AuthUserRequest,
    ) -> xr_engine_20221111_models.AuthUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.auth_user_with_options_async(request, runtime)

    def batch_create_svc_map_bind_with_options(
        self,
        tmp_req: xr_engine_20221111_models.BatchCreateSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BatchCreateSvcMapBindResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.BatchCreateSvcMapBindShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.map_ids):
            request.map_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.map_ids, 'MapIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_ids_shrink):
            body['MapIds'] = request.map_ids_shrink
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BatchCreateSvcMapBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_svc_map_bind_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.BatchCreateSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BatchCreateSvcMapBindResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.BatchCreateSvcMapBindShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.map_ids):
            request.map_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.map_ids, 'MapIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_ids_shrink):
            body['MapIds'] = request.map_ids_shrink
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BatchCreateSvcMapBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_svc_map_bind(
        self,
        request: xr_engine_20221111_models.BatchCreateSvcMapBindRequest,
    ) -> xr_engine_20221111_models.BatchCreateSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_create_svc_map_bind_with_options(request, runtime)

    async def batch_create_svc_map_bind_async(
        self,
        request: xr_engine_20221111_models.BatchCreateSvcMapBindRequest,
    ) -> xr_engine_20221111_models.BatchCreateSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_svc_map_bind_with_options_async(request, runtime)

    def batch_delete_svc_map_bind_with_options(
        self,
        tmp_req: xr_engine_20221111_models.BatchDeleteSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BatchDeleteSvcMapBindResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.BatchDeleteSvcMapBindShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BatchDeleteSvcMapBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_svc_map_bind_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.BatchDeleteSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BatchDeleteSvcMapBindResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.BatchDeleteSvcMapBindShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BatchDeleteSvcMapBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_svc_map_bind(
        self,
        request: xr_engine_20221111_models.BatchDeleteSvcMapBindRequest,
    ) -> xr_engine_20221111_models.BatchDeleteSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_svc_map_bind_with_options(request, runtime)

    async def batch_delete_svc_map_bind_async(
        self,
        request: xr_engine_20221111_models.BatchDeleteSvcMapBindRequest,
    ) -> xr_engine_20221111_models.BatchDeleteSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_svc_map_bind_with_options_async(request, runtime)

    def build_project_with_options(
        self,
        request: xr_engine_20221111_models.BuildProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BuildProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.video_name):
            query['VideoName'] = request.video_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BuildProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BuildProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def build_project_with_options_async(
        self,
        request: xr_engine_20221111_models.BuildProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.BuildProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.video_name):
            query['VideoName'] = request.video_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BuildProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.BuildProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def build_project(
        self,
        request: xr_engine_20221111_models.BuildProjectRequest,
    ) -> xr_engine_20221111_models.BuildProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.build_project_with_options(request, runtime)

    async def build_project_async(
        self,
        request: xr_engine_20221111_models.BuildProjectRequest,
    ) -> xr_engine_20221111_models.BuildProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.build_project_with_options_async(request, runtime)

    def create_location_service_with_options(
        self,
        request: xr_engine_20221111_models.CreateLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.qps):
            body['Qps'] = request.qps
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.CreateLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.qps):
            body['Qps'] = request.qps
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_location_service(
        self,
        request: xr_engine_20221111_models.CreateLocationServiceRequest,
    ) -> xr_engine_20221111_models.CreateLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_location_service_with_options(request, runtime)

    async def create_location_service_async(
        self,
        request: xr_engine_20221111_models.CreateLocationServiceRequest,
    ) -> xr_engine_20221111_models.CreateLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_location_service_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: xr_engine_20221111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.try_on_params):
            request.try_on_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.try_on_params, 'TryOnParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_build):
            body['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.dependencies):
            body['Dependencies'] = request.dependencies
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_uuid):
            body['MapUuid'] = request.map_uuid
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.try_on_params_shrink):
            body['TryOnParams'] = request.try_on_params_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.try_on_params):
            request.try_on_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.try_on_params, 'TryOnParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.auto_build):
            body['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.dependencies):
            body['Dependencies'] = request.dependencies
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_uuid):
            body['MapUuid'] = request.map_uuid
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.try_on_params_shrink):
            body['TryOnParams'] = request.try_on_params_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: xr_engine_20221111_models.CreateProjectRequest,
    ) -> xr_engine_20221111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: xr_engine_20221111_models.CreateProjectRequest,
    ) -> xr_engine_20221111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_source_policy_with_options(
        self,
        request: xr_engine_20221111_models.CreateSourcePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateSourcePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSourcePolicy',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateSourcePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_source_policy_with_options_async(
        self,
        request: xr_engine_20221111_models.CreateSourcePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.CreateSourcePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSourcePolicy',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.CreateSourcePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_source_policy(
        self,
        request: xr_engine_20221111_models.CreateSourcePolicyRequest,
    ) -> xr_engine_20221111_models.CreateSourcePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_source_policy_with_options(request, runtime)

    async def create_source_policy_async(
        self,
        request: xr_engine_20221111_models.CreateSourcePolicyRequest,
    ) -> xr_engine_20221111_models.CreateSourcePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_source_policy_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: xr_engine_20221111_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: xr_engine_20221111_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: xr_engine_20221111_models.DeleteProjectRequest,
    ) -> xr_engine_20221111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: xr_engine_20221111_models.DeleteProjectRequest,
    ) -> xr_engine_20221111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_source_file_with_options(
        self,
        request: xr_engine_20221111_models.DeleteSourceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeleteSourceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceFile',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeleteSourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_file_with_options_async(
        self,
        request: xr_engine_20221111_models.DeleteSourceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeleteSourceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceFile',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeleteSourceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source_file(
        self,
        request: xr_engine_20221111_models.DeleteSourceFileRequest,
    ) -> xr_engine_20221111_models.DeleteSourceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_source_file_with_options(request, runtime)

    async def delete_source_file_async(
        self,
        request: xr_engine_20221111_models.DeleteSourceFileRequest,
    ) -> xr_engine_20221111_models.DeleteSourceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_source_file_with_options_async(request, runtime)

    def deploy_location_tree_with_options(
        self,
        request: xr_engine_20221111_models.DeployLocationTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeployLocationTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_update):
            body['ForceUpdate'] = request.force_update
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployLocationTree',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeployLocationTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_location_tree_with_options_async(
        self,
        request: xr_engine_20221111_models.DeployLocationTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.DeployLocationTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_update):
            body['ForceUpdate'] = request.force_update
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployLocationTree',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.DeployLocationTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_location_tree(
        self,
        request: xr_engine_20221111_models.DeployLocationTreeRequest,
    ) -> xr_engine_20221111_models.DeployLocationTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_location_tree_with_options(request, runtime)

    async def deploy_location_tree_async(
        self,
        request: xr_engine_20221111_models.DeployLocationTreeRequest,
    ) -> xr_engine_20221111_models.DeployLocationTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_location_tree_with_options_async(request, runtime)

    def find_svc_map_bind_with_options(
        self,
        request: xr_engine_20221111_models.FindSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.FindSvcMapBindResponse:
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
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.FindSvcMapBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_svc_map_bind_with_options_async(
        self,
        request: xr_engine_20221111_models.FindSvcMapBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.FindSvcMapBindResponse:
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
        if not UtilClient.is_unset(request.svc_id):
            body['SvcId'] = request.svc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindSvcMapBind',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.FindSvcMapBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_svc_map_bind(
        self,
        request: xr_engine_20221111_models.FindSvcMapBindRequest,
    ) -> xr_engine_20221111_models.FindSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_svc_map_bind_with_options(request, runtime)

    async def find_svc_map_bind_async(
        self,
        request: xr_engine_20221111_models.FindSvcMapBindRequest,
    ) -> xr_engine_20221111_models.FindSvcMapBindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_svc_map_bind_with_options_async(request, runtime)

    def get_ar_edit_common_material_with_options(
        self,
        request: xr_engine_20221111_models.GetArEditCommonMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditCommonMaterialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditCommonMaterial',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditCommonMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ar_edit_common_material_with_options_async(
        self,
        request: xr_engine_20221111_models.GetArEditCommonMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditCommonMaterialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditCommonMaterial',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditCommonMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ar_edit_common_material(
        self,
        request: xr_engine_20221111_models.GetArEditCommonMaterialRequest,
    ) -> xr_engine_20221111_models.GetArEditCommonMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ar_edit_common_material_with_options(request, runtime)

    async def get_ar_edit_common_material_async(
        self,
        request: xr_engine_20221111_models.GetArEditCommonMaterialRequest,
    ) -> xr_engine_20221111_models.GetArEditCommonMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ar_edit_common_material_with_options_async(request, runtime)

    def get_ar_edit_sts_auth_with_options(
        self,
        request: xr_engine_20221111_models.GetArEditStsAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditStsAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditStsAuth',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditStsAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ar_edit_sts_auth_with_options_async(
        self,
        request: xr_engine_20221111_models.GetArEditStsAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditStsAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditStsAuth',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditStsAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ar_edit_sts_auth(
        self,
        request: xr_engine_20221111_models.GetArEditStsAuthRequest,
    ) -> xr_engine_20221111_models.GetArEditStsAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ar_edit_sts_auth_with_options(request, runtime)

    async def get_ar_edit_sts_auth_async(
        self,
        request: xr_engine_20221111_models.GetArEditStsAuthRequest,
    ) -> xr_engine_20221111_models.GetArEditStsAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ar_edit_sts_auth_with_options_async(request, runtime)

    def get_ar_edit_ugc_material_with_options(
        self,
        request: xr_engine_20221111_models.GetArEditUgcMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditUgcMaterialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditUgcMaterial',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditUgcMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ar_edit_ugc_material_with_options_async(
        self,
        request: xr_engine_20221111_models.GetArEditUgcMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetArEditUgcMaterialResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetArEditUgcMaterial',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetArEditUgcMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ar_edit_ugc_material(
        self,
        request: xr_engine_20221111_models.GetArEditUgcMaterialRequest,
    ) -> xr_engine_20221111_models.GetArEditUgcMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ar_edit_ugc_material_with_options(request, runtime)

    async def get_ar_edit_ugc_material_async(
        self,
        request: xr_engine_20221111_models.GetArEditUgcMaterialRequest,
    ) -> xr_engine_20221111_models.GetArEditUgcMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ar_edit_ugc_material_with_options_async(request, runtime)

    def get_project_dataset_with_options(
        self,
        request: xr_engine_20221111_models.GetProjectDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetProjectDatasetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectDataset',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetProjectDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_dataset_with_options_async(
        self,
        request: xr_engine_20221111_models.GetProjectDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.GetProjectDatasetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectDataset',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.GetProjectDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_dataset(
        self,
        request: xr_engine_20221111_models.GetProjectDatasetRequest,
    ) -> xr_engine_20221111_models.GetProjectDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_dataset_with_options(request, runtime)

    async def get_project_dataset_async(
        self,
        request: xr_engine_20221111_models.GetProjectDatasetRequest,
    ) -> xr_engine_20221111_models.GetProjectDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_dataset_with_options_async(request, runtime)

    def list_area_map_with_options(
        self,
        request: xr_engine_20221111_models.ListAreaMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListAreaMapResponse:
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
            action='ListAreaMap',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListAreaMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_area_map_with_options_async(
        self,
        request: xr_engine_20221111_models.ListAreaMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListAreaMapResponse:
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
            action='ListAreaMap',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListAreaMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_area_map(
        self,
        request: xr_engine_20221111_models.ListAreaMapRequest,
    ) -> xr_engine_20221111_models.ListAreaMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_area_map_with_options(request, runtime)

    async def list_area_map_async(
        self,
        request: xr_engine_20221111_models.ListAreaMapRequest,
    ) -> xr_engine_20221111_models.ListAreaMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_area_map_with_options_async(request, runtime)

    def list_cloth_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListClothTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListClothTypes',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListClothTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloth_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListClothTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListClothTypes',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListClothTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloth_types(self) -> xr_engine_20221111_models.ListClothTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cloth_types_with_options(runtime)

    async def list_cloth_types_async(self) -> xr_engine_20221111_models.ListClothTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cloth_types_with_options_async(runtime)

    def list_clothes_with_options(
        self,
        tmp_req: xr_engine_20221111_models.ListClothesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListClothesResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.ListClothesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cloth_size):
            query['ClothSize'] = request.cloth_size
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClothes',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListClothesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clothes_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.ListClothesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListClothesResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.ListClothesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cloth_size):
            query['ClothSize'] = request.cloth_size
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClothes',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListClothesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clothes(
        self,
        request: xr_engine_20221111_models.ListClothesRequest,
    ) -> xr_engine_20221111_models.ListClothesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clothes_with_options(request, runtime)

    async def list_clothes_async(
        self,
        request: xr_engine_20221111_models.ListClothesRequest,
    ) -> xr_engine_20221111_models.ListClothesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clothes_with_options_async(request, runtime)

    def list_hdr_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListHdrResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListHdr',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListHdrResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hdr_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListHdrResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListHdr',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListHdrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hdr(self) -> xr_engine_20221111_models.ListHdrResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hdr_with_options(runtime)

    async def list_hdr_async(self) -> xr_engine_20221111_models.ListHdrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hdr_with_options_async(runtime)

    def list_location_pai_image_with_options(
        self,
        request: xr_engine_20221111_models.ListLocationPaiImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListLocationPaiImageResponse:
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
            action='ListLocationPaiImage',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListLocationPaiImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_location_pai_image_with_options_async(
        self,
        request: xr_engine_20221111_models.ListLocationPaiImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListLocationPaiImageResponse:
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
            action='ListLocationPaiImage',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListLocationPaiImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_location_pai_image(
        self,
        request: xr_engine_20221111_models.ListLocationPaiImageRequest,
    ) -> xr_engine_20221111_models.ListLocationPaiImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_location_pai_image_with_options(request, runtime)

    async def list_location_pai_image_async(
        self,
        request: xr_engine_20221111_models.ListLocationPaiImageRequest,
    ) -> xr_engine_20221111_models.ListLocationPaiImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_location_pai_image_with_options_async(request, runtime)

    def list_location_service_with_options(
        self,
        request: xr_engine_20221111_models.ListLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListLocationServiceResponse:
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
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.ListLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListLocationServiceResponse:
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
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_location_service(
        self,
        request: xr_engine_20221111_models.ListLocationServiceRequest,
    ) -> xr_engine_20221111_models.ListLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_location_service_with_options(request, runtime)

    async def list_location_service_async(
        self,
        request: xr_engine_20221111_models.ListLocationServiceRequest,
    ) -> xr_engine_20221111_models.ListLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_location_service_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: xr_engine_20221111_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        if not UtilClient.is_unset(request.with_user):
            body['WithUser'] = request.with_user
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: xr_engine_20221111_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        if not UtilClient.is_unset(request.with_user):
            body['WithUser'] = request.with_user
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: xr_engine_20221111_models.ListProjectRequest,
    ) -> xr_engine_20221111_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: xr_engine_20221111_models.ListProjectRequest,
    ) -> xr_engine_20221111_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def list_projects_by_dependency_id_with_options(
        self,
        request: xr_engine_20221111_models.ListProjectsByDependencyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListProjectsByDependencyIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dependency_project_id):
            body['DependencyProjectId'] = request.dependency_project_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_uuid):
            body['MapUuid'] = request.map_uuid
        if not UtilClient.is_unset(request.with_dataset):
            body['WithDataset'] = request.with_dataset
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectsByDependencyId',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListProjectsByDependencyIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_by_dependency_id_with_options_async(
        self,
        request: xr_engine_20221111_models.ListProjectsByDependencyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListProjectsByDependencyIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dependency_project_id):
            body['DependencyProjectId'] = request.dependency_project_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_uuid):
            body['MapUuid'] = request.map_uuid
        if not UtilClient.is_unset(request.with_dataset):
            body['WithDataset'] = request.with_dataset
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectsByDependencyId',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListProjectsByDependencyIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects_by_dependency_id(
        self,
        request: xr_engine_20221111_models.ListProjectsByDependencyIdRequest,
    ) -> xr_engine_20221111_models.ListProjectsByDependencyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_by_dependency_id_with_options(request, runtime)

    async def list_projects_by_dependency_id_async(
        self,
        request: xr_engine_20221111_models.ListProjectsByDependencyIdRequest,
    ) -> xr_engine_20221111_models.ListProjectsByDependencyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_by_dependency_id_with_options_async(request, runtime)

    def list_source_file_with_options(
        self,
        request: xr_engine_20221111_models.ListSourceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListSourceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSourceFile',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListSourceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_source_file_with_options_async(
        self,
        request: xr_engine_20221111_models.ListSourceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListSourceFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSourceFile',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListSourceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_source_file(
        self,
        request: xr_engine_20221111_models.ListSourceFileRequest,
    ) -> xr_engine_20221111_models.ListSourceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_source_file_with_options(request, runtime)

    async def list_source_file_async(
        self,
        request: xr_engine_20221111_models.ListSourceFileRequest,
    ) -> xr_engine_20221111_models.ListSourceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_source_file_with_options_async(request, runtime)

    def list_workflow_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListWorkflowResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListWorkflow',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ListWorkflowResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListWorkflow',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ListWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow(self) -> xr_engine_20221111_models.ListWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_with_options(runtime)

    async def list_workflow_async(self) -> xr_engine_20221111_models.ListWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_workflow_with_options_async(runtime)

    def login_with_options(
        self,
        request: xr_engine_20221111_models.LoginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.LoginResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.emp_id):
            body['EmpId'] = request.emp_id
        if not UtilClient.is_unset(request.emp_name):
            body['EmpName'] = request.emp_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Login',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.LoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_with_options_async(
        self,
        request: xr_engine_20221111_models.LoginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.LoginResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.emp_id):
            body['EmpId'] = request.emp_id
        if not UtilClient.is_unset(request.emp_name):
            body['EmpName'] = request.emp_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Login',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.LoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login(
        self,
        request: xr_engine_20221111_models.LoginRequest,
    ) -> xr_engine_20221111_models.LoginResponse:
        runtime = util_models.RuntimeOptions()
        return self.login_with_options(request, runtime)

    async def login_async(
        self,
        request: xr_engine_20221111_models.LoginRequest,
    ) -> xr_engine_20221111_models.LoginResponse:
        runtime = util_models.RuntimeOptions()
        return await self.login_with_options_async(request, runtime)

    def publish_ar_edit_project_with_options(
        self,
        request: xr_engine_20221111_models.PublishArEditProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.PublishArEditProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishArEditProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.PublishArEditProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_ar_edit_project_with_options_async(
        self,
        request: xr_engine_20221111_models.PublishArEditProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.PublishArEditProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishArEditProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.PublishArEditProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_ar_edit_project(
        self,
        request: xr_engine_20221111_models.PublishArEditProjectRequest,
    ) -> xr_engine_20221111_models.PublishArEditProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_ar_edit_project_with_options(request, runtime)

    async def publish_ar_edit_project_async(
        self,
        request: xr_engine_20221111_models.PublishArEditProjectRequest,
    ) -> xr_engine_20221111_models.PublishArEditProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_ar_edit_project_with_options_async(request, runtime)

    def query_area_map_with_options(
        self,
        request: xr_engine_20221111_models.QueryAreaMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryAreaMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAreaMap',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryAreaMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_area_map_with_options_async(
        self,
        request: xr_engine_20221111_models.QueryAreaMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryAreaMapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAreaMap',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryAreaMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_area_map(
        self,
        request: xr_engine_20221111_models.QueryAreaMapRequest,
    ) -> xr_engine_20221111_models.QueryAreaMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_area_map_with_options(request, runtime)

    async def query_area_map_async(
        self,
        request: xr_engine_20221111_models.QueryAreaMapRequest,
    ) -> xr_engine_20221111_models.QueryAreaMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_area_map_with_options_async(request, runtime)

    def query_build_breakpoint_with_options(
        self,
        request: xr_engine_20221111_models.QueryBuildBreakpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryBuildBreakpointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBuildBreakpoint',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryBuildBreakpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_build_breakpoint_with_options_async(
        self,
        request: xr_engine_20221111_models.QueryBuildBreakpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryBuildBreakpointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBuildBreakpoint',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryBuildBreakpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_build_breakpoint(
        self,
        request: xr_engine_20221111_models.QueryBuildBreakpointRequest,
    ) -> xr_engine_20221111_models.QueryBuildBreakpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_build_breakpoint_with_options(request, runtime)

    async def query_build_breakpoint_async(
        self,
        request: xr_engine_20221111_models.QueryBuildBreakpointRequest,
    ) -> xr_engine_20221111_models.QueryBuildBreakpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_build_breakpoint_with_options_async(request, runtime)

    def query_location_service_with_options(
        self,
        request: xr_engine_20221111_models.QueryLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.QueryLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_location_service(
        self,
        request: xr_engine_20221111_models.QueryLocationServiceRequest,
    ) -> xr_engine_20221111_models.QueryLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_location_service_with_options(request, runtime)

    async def query_location_service_async(
        self,
        request: xr_engine_20221111_models.QueryLocationServiceRequest,
    ) -> xr_engine_20221111_models.QueryLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_location_service_with_options_async(request, runtime)

    def query_project_build_detail_with_options(
        self,
        request: xr_engine_20221111_models.QueryProjectBuildDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryProjectBuildDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProjectBuildDetail',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryProjectBuildDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_build_detail_with_options_async(
        self,
        request: xr_engine_20221111_models.QueryProjectBuildDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryProjectBuildDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProjectBuildDetail',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryProjectBuildDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project_build_detail(
        self,
        request: xr_engine_20221111_models.QueryProjectBuildDetailRequest,
    ) -> xr_engine_20221111_models.QueryProjectBuildDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_project_build_detail_with_options(request, runtime)

    async def query_project_build_detail_async(
        self,
        request: xr_engine_20221111_models.QueryProjectBuildDetailRequest,
    ) -> xr_engine_20221111_models.QueryProjectBuildDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_project_build_detail_with_options_async(request, runtime)

    def query_project_detail_with_options(
        self,
        request: xr_engine_20221111_models.QueryProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProjectDetail',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_detail_with_options_async(
        self,
        request: xr_engine_20221111_models.QueryProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.QueryProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProjectDetail',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.QueryProjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project_detail(
        self,
        request: xr_engine_20221111_models.QueryProjectDetailRequest,
    ) -> xr_engine_20221111_models.QueryProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_project_detail_with_options(request, runtime)

    async def query_project_detail_async(
        self,
        request: xr_engine_20221111_models.QueryProjectDetailRequest,
    ) -> xr_engine_20221111_models.QueryProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_project_detail_with_options_async(request, runtime)

    def recognize_product_regions_with_options(
        self,
        request: xr_engine_20221111_models.RecognizeProductRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.RecognizeProductRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeProductRegions',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.RecognizeProductRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_product_regions_with_options_async(
        self,
        request: xr_engine_20221111_models.RecognizeProductRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.RecognizeProductRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeProductRegions',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.RecognizeProductRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_product_regions(
        self,
        request: xr_engine_20221111_models.RecognizeProductRegionsRequest,
    ) -> xr_engine_20221111_models.RecognizeProductRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_product_regions_with_options(request, runtime)

    async def recognize_product_regions_async(
        self,
        request: xr_engine_20221111_models.RecognizeProductRegionsRequest,
    ) -> xr_engine_20221111_models.RecognizeProductRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_product_regions_with_options_async(request, runtime)

    def register_user_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.RegisterUserResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RegisterUser',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.RegisterUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_user_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.RegisterUserResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RegisterUser',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.RegisterUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_user(self) -> xr_engine_20221111_models.RegisterUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_user_with_options(runtime)

    async def register_user_async(self) -> xr_engine_20221111_models.RegisterUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_user_with_options_async(runtime)

    def resume_location_service_with_options(
        self,
        request: xr_engine_20221111_models.ResumeLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ResumeLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ResumeLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.ResumeLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.ResumeLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.ResumeLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_location_service(
        self,
        request: xr_engine_20221111_models.ResumeLocationServiceRequest,
    ) -> xr_engine_20221111_models.ResumeLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_location_service_with_options(request, runtime)

    async def resume_location_service_async(
        self,
        request: xr_engine_20221111_models.ResumeLocationServiceRequest,
    ) -> xr_engine_20221111_models.ResumeLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_location_service_with_options_async(request, runtime)

    def save_ar_edit_project_with_options(
        self,
        request: xr_engine_20221111_models.SaveArEditProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SaveArEditProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveArEditProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SaveArEditProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ar_edit_project_with_options_async(
        self,
        request: xr_engine_20221111_models.SaveArEditProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SaveArEditProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.map_id):
            body['MapId'] = request.map_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveArEditProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SaveArEditProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ar_edit_project(
        self,
        request: xr_engine_20221111_models.SaveArEditProjectRequest,
    ) -> xr_engine_20221111_models.SaveArEditProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ar_edit_project_with_options(request, runtime)

    async def save_ar_edit_project_async(
        self,
        request: xr_engine_20221111_models.SaveArEditProjectRequest,
    ) -> xr_engine_20221111_models.SaveArEditProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ar_edit_project_with_options_async(request, runtime)

    def save_source_with_options(
        self,
        request: xr_engine_20221111_models.SaveSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SaveSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSource',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SaveSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_source_with_options_async(
        self,
        request: xr_engine_20221111_models.SaveSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SaveSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSource',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SaveSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_source(
        self,
        request: xr_engine_20221111_models.SaveSourceRequest,
    ) -> xr_engine_20221111_models.SaveSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_source_with_options(request, runtime)

    async def save_source_async(
        self,
        request: xr_engine_20221111_models.SaveSourceRequest,
    ) -> xr_engine_20221111_models.SaveSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_source_with_options_async(request, runtime)

    def search_products_by_image_with_options(
        self,
        tmp_req: xr_engine_20221111_models.SearchProductsByImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SearchProductsByImageResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.SearchProductsByImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region):
            request.region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region, 'Region', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        if not UtilClient.is_unset(request.region_shrink):
            body['Region'] = request.region_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchProductsByImage',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SearchProductsByImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_products_by_image_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.SearchProductsByImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SearchProductsByImageResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.SearchProductsByImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region):
            request.region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region, 'Region', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.image_base_64):
            body['ImageBase64'] = request.image_base_64
        if not UtilClient.is_unset(request.region_shrink):
            body['Region'] = request.region_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchProductsByImage',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SearchProductsByImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_products_by_image(
        self,
        request: xr_engine_20221111_models.SearchProductsByImageRequest,
    ) -> xr_engine_20221111_models.SearchProductsByImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_products_by_image_with_options(request, runtime)

    async def search_products_by_image_async(
        self,
        request: xr_engine_20221111_models.SearchProductsByImageRequest,
    ) -> xr_engine_20221111_models.SearchProductsByImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_products_by_image_with_options_async(request, runtime)

    def suspend_location_service_with_options(
        self,
        request: xr_engine_20221111_models.SuspendLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SuspendLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SuspendLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.SuspendLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.SuspendLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.SuspendLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_location_service(
        self,
        request: xr_engine_20221111_models.SuspendLocationServiceRequest,
    ) -> xr_engine_20221111_models.SuspendLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_location_service_with_options(request, runtime)

    async def suspend_location_service_async(
        self,
        request: xr_engine_20221111_models.SuspendLocationServiceRequest,
    ) -> xr_engine_20221111_models.SuspendLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_location_service_with_options_async(request, runtime)

    def update_location_service_with_options(
        self,
        request: xr_engine_20221111_models.UpdateLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.qps):
            body['Qps'] = request.qps
        if not UtilClient.is_unset(request.svc_name):
            body['SvcName'] = request.svc_name
        if not UtilClient.is_unset(request.svc_state):
            body['SvcState'] = request.svc_state
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_location_service_with_options_async(
        self,
        request: xr_engine_20221111_models.UpdateLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateLocationServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.qps):
            body['Qps'] = request.qps
        if not UtilClient.is_unset(request.svc_name):
            body['SvcName'] = request.svc_name
        if not UtilClient.is_unset(request.svc_state):
            body['SvcState'] = request.svc_state
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLocationService',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_location_service(
        self,
        request: xr_engine_20221111_models.UpdateLocationServiceRequest,
    ) -> xr_engine_20221111_models.UpdateLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_location_service_with_options(request, runtime)

    async def update_location_service_async(
        self,
        request: xr_engine_20221111_models.UpdateLocationServiceRequest,
    ) -> xr_engine_20221111_models.UpdateLocationServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_location_service_with_options_async(request, runtime)

    def update_location_tree_with_options(
        self,
        request: xr_engine_20221111_models.UpdateLocationTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateLocationTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.tree_config):
            body['TreeConfig'] = request.tree_config
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLocationTree',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateLocationTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_location_tree_with_options_async(
        self,
        request: xr_engine_20221111_models.UpdateLocationTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateLocationTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.tree_config):
            body['TreeConfig'] = request.tree_config
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLocationTree',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateLocationTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_location_tree(
        self,
        request: xr_engine_20221111_models.UpdateLocationTreeRequest,
    ) -> xr_engine_20221111_models.UpdateLocationTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_location_tree_with_options(request, runtime)

    async def update_location_tree_async(
        self,
        request: xr_engine_20221111_models.UpdateLocationTreeRequest,
    ) -> xr_engine_20221111_models.UpdateLocationTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_location_tree_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: xr_engine_20221111_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'Ext', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.ext_shrink):
            query['Ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.intro):
            query['Intro'] = request.intro
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: xr_engine_20221111_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xr_engine_20221111_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = xr_engine_20221111_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'Ext', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.ext_shrink):
            query['Ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.intro):
            query['Intro'] = request.intro
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2022-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20221111_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: xr_engine_20221111_models.UpdateProjectRequest,
    ) -> xr_engine_20221111_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: xr_engine_20221111_models.UpdateProjectRequest,
    ) -> xr_engine_20221111_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)
