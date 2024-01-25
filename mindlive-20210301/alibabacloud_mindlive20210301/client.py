# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mindlive20210301 import models as mind_live_20210301_models
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
        self._endpoint = self.get_endpoint('mindlive', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def login_device_with_options(
        self,
        request: mind_live_20210301_models.LoginDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.LoginDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LoginDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_device_with_options_async(
        self,
        request: mind_live_20210301_models.LoginDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.LoginDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LoginDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_device(
        self,
        request: mind_live_20210301_models.LoginDeviceRequest,
    ) -> mind_live_20210301_models.LoginDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.login_device_with_options(request, runtime)

    async def login_device_async(
        self,
        request: mind_live_20210301_models.LoginDeviceRequest,
    ) -> mind_live_20210301_models.LoginDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.login_device_with_options_async(request, runtime)

    def logout_device_with_options(
        self,
        request: mind_live_20210301_models.LogoutDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.LogoutDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LogoutDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LogoutDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def logout_device_with_options_async(
        self,
        request: mind_live_20210301_models.LogoutDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.LogoutDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source):
            query['UserSource'] = request.user_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LogoutDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.LogoutDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def logout_device(
        self,
        request: mind_live_20210301_models.LogoutDeviceRequest,
    ) -> mind_live_20210301_models.LogoutDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.logout_device_with_options(request, runtime)

    async def logout_device_async(
        self,
        request: mind_live_20210301_models.LogoutDeviceRequest,
    ) -> mind_live_20210301_models.LogoutDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.logout_device_with_options_async(request, runtime)

    def query_item_backgrounds_with_options(
        self,
        tmp_req: mind_live_20210301_models.QueryItemBackgroundsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.QueryItemBackgroundsResponse:
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.QueryItemBackgroundsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemBackgrounds',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.QueryItemBackgroundsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_backgrounds_with_options_async(
        self,
        tmp_req: mind_live_20210301_models.QueryItemBackgroundsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.QueryItemBackgroundsResponse:
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.QueryItemBackgroundsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemBackgrounds',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.QueryItemBackgroundsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_backgrounds(
        self,
        request: mind_live_20210301_models.QueryItemBackgroundsRequest,
    ) -> mind_live_20210301_models.QueryItemBackgroundsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_backgrounds_with_options(request, runtime)

    async def query_item_backgrounds_async(
        self,
        request: mind_live_20210301_models.QueryItemBackgroundsRequest,
    ) -> mind_live_20210301_models.QueryItemBackgroundsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_backgrounds_with_options_async(request, runtime)

    def report_current_background_with_options(
        self,
        tmp_req: mind_live_20210301_models.ReportCurrentBackgroundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportCurrentBackgroundResponse:
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.ReportCurrentBackgroundShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bg_config):
            request.bg_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bg_config, 'BgConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.bg_config_shrink):
            query['BgConfig'] = request.bg_config_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.resource_uuid):
            query['ResourceUuid'] = request.resource_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportCurrentBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportCurrentBackgroundResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_current_background_with_options_async(
        self,
        tmp_req: mind_live_20210301_models.ReportCurrentBackgroundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportCurrentBackgroundResponse:
        UtilClient.validate_model(tmp_req)
        request = mind_live_20210301_models.ReportCurrentBackgroundShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bg_config):
            request.bg_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bg_config, 'BgConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.bg_config_shrink):
            query['BgConfig'] = request.bg_config_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.resource_uuid):
            query['ResourceUuid'] = request.resource_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportCurrentBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportCurrentBackgroundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_current_background(
        self,
        request: mind_live_20210301_models.ReportCurrentBackgroundRequest,
    ) -> mind_live_20210301_models.ReportCurrentBackgroundResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_current_background_with_options(request, runtime)

    async def report_current_background_async(
        self,
        request: mind_live_20210301_models.ReportCurrentBackgroundRequest,
    ) -> mind_live_20210301_models.ReportCurrentBackgroundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_current_background_with_options_async(request, runtime)

    def report_dev_config_with_options(
        self,
        request: mind_live_20210301_models.ReportDevConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportDevConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportDevConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportDevConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_dev_config_with_options_async(
        self,
        request: mind_live_20210301_models.ReportDevConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportDevConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportDevConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportDevConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_dev_config(
        self,
        request: mind_live_20210301_models.ReportDevConfigRequest,
    ) -> mind_live_20210301_models.ReportDevConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_dev_config_with_options(request, runtime)

    async def report_dev_config_async(
        self,
        request: mind_live_20210301_models.ReportDevConfigRequest,
    ) -> mind_live_20210301_models.ReportDevConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_dev_config_with_options_async(request, runtime)

    def report_live_state_with_options(
        self,
        request: mind_live_20210301_models.ReportLiveStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportLiveStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.live_mode):
            query['LiveMode'] = request.live_mode
        if not UtilClient.is_unset(request.live_state):
            query['LiveState'] = request.live_state
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportLiveState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportLiveStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_live_state_with_options_async(
        self,
        request: mind_live_20210301_models.ReportLiveStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportLiveStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.live_mode):
            query['LiveMode'] = request.live_mode
        if not UtilClient.is_unset(request.live_state):
            query['LiveState'] = request.live_state
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportLiveState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportLiveStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_live_state(
        self,
        request: mind_live_20210301_models.ReportLiveStateRequest,
    ) -> mind_live_20210301_models.ReportLiveStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_live_state_with_options(request, runtime)

    async def report_live_state_async(
        self,
        request: mind_live_20210301_models.ReportLiveStateRequest,
    ) -> mind_live_20210301_models.ReportLiveStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_live_state_with_options_async(request, runtime)

    def report_screen_with_options(
        self,
        request: mind_live_20210301_models.ReportScreenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportScreenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportScreen',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportScreenResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_screen_with_options_async(
        self,
        request: mind_live_20210301_models.ReportScreenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportScreenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportScreen',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportScreenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_screen(
        self,
        request: mind_live_20210301_models.ReportScreenRequest,
    ) -> mind_live_20210301_models.ReportScreenResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_screen_with_options(request, runtime)

    async def report_screen_async(
        self,
        request: mind_live_20210301_models.ReportScreenRequest,
    ) -> mind_live_20210301_models.ReportScreenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_screen_with_options_async(request, runtime)

    def report_user_config_with_options(
        self,
        request: mind_live_20210301_models.ReportUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_user_config_with_options_async(
        self,
        request: mind_live_20210301_models.ReportUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ReportUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ReportUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_user_config(
        self,
        request: mind_live_20210301_models.ReportUserConfigRequest,
    ) -> mind_live_20210301_models.ReportUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_user_config_with_options(request, runtime)

    async def report_user_config_async(
        self,
        request: mind_live_20210301_models.ReportUserConfigRequest,
    ) -> mind_live_20210301_models.ReportUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_user_config_with_options_async(request, runtime)

    def request_authorization_data_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestAuthorizationDataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestAuthorizationData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestAuthorizationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_authorization_data_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestAuthorizationDataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestAuthorizationData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestAuthorizationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_authorization_data(self) -> mind_live_20210301_models.RequestAuthorizationDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_authorization_data_with_options(runtime)

    async def request_authorization_data_async(self) -> mind_live_20210301_models.RequestAuthorizationDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_authorization_data_with_options_async(runtime)

    def request_background_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBackgroundResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBackgroundResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_background_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBackgroundResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBackground',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBackgroundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_background(self) -> mind_live_20210301_models.RequestBackgroundResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_background_with_options(runtime)

    async def request_background_async(self) -> mind_live_20210301_models.RequestBackgroundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_background_with_options_async(runtime)

    def request_bind_data_with_options(
        self,
        request: mind_live_20210301_models.RequestBindDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBindDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestBindData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_bind_data_with_options_async(
        self,
        request: mind_live_20210301_models.RequestBindDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBindDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestBindData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_bind_data(
        self,
        request: mind_live_20210301_models.RequestBindDataRequest,
    ) -> mind_live_20210301_models.RequestBindDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_bind_data_with_options(request, runtime)

    async def request_bind_data_async(
        self,
        request: mind_live_20210301_models.RequestBindDataRequest,
    ) -> mind_live_20210301_models.RequestBindDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_bind_data_with_options_async(request, runtime)

    def request_binding_state_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBindingStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBindingState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindingStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_binding_state_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestBindingStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestBindingState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestBindingStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_binding_state(self) -> mind_live_20210301_models.RequestBindingStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_binding_state_with_options(runtime)

    async def request_binding_state_async(self) -> mind_live_20210301_models.RequestBindingStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_binding_state_with_options_async(runtime)

    def request_device_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestDeviceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestDeviceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_device_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestDeviceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestDeviceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_device_info(self) -> mind_live_20210301_models.RequestDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_device_info_with_options(runtime)

    async def request_device_info_async(self) -> mind_live_20210301_models.RequestDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_device_info_with_options_async(runtime)

    def request_iot_triad_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestIotTriadResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestIotTriad',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestIotTriadResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_iot_triad_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestIotTriadResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestIotTriad',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestIotTriadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_iot_triad(self) -> mind_live_20210301_models.RequestIotTriadResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_iot_triad_with_options(runtime)

    async def request_iot_triad_async(self) -> mind_live_20210301_models.RequestIotTriadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_iot_triad_with_options_async(runtime)

    def request_live_sell_point_state_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestLiveSellPointStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveSellPointStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_live_sell_point_state_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestLiveSellPointStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveSellPointStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_live_sell_point_state(self) -> mind_live_20210301_models.RequestLiveSellPointStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_live_sell_point_state_with_options(runtime)

    async def request_live_sell_point_state_async(self) -> mind_live_20210301_models.RequestLiveSellPointStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_live_sell_point_state_with_options_async(runtime)

    def request_live_teleprompter_state_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestLiveTeleprompterStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveTeleprompterStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_live_teleprompter_state_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestLiveTeleprompterStateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestLiveTeleprompterStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_live_teleprompter_state(self) -> mind_live_20210301_models.RequestLiveTeleprompterStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_live_teleprompter_state_with_options(runtime)

    async def request_live_teleprompter_state_async(self) -> mind_live_20210301_models.RequestLiveTeleprompterStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_live_teleprompter_state_with_options_async(runtime)

    def request_oss_sts_with_options(
        self,
        request: mind_live_20210301_models.RequestOssStsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestOssStsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestOssSts',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestOssStsResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_oss_sts_with_options_async(
        self,
        request: mind_live_20210301_models.RequestOssStsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestOssStsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestOssSts',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestOssStsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_oss_sts(
        self,
        request: mind_live_20210301_models.RequestOssStsRequest,
    ) -> mind_live_20210301_models.RequestOssStsResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_oss_sts_with_options(request, runtime)

    async def request_oss_sts_async(
        self,
        request: mind_live_20210301_models.RequestOssStsRequest,
    ) -> mind_live_20210301_models.RequestOssStsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_oss_sts_with_options_async(request, runtime)

    def request_paster_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestPasterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestPaster',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestPasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_paster_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestPasterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestPaster',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestPasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_paster(self) -> mind_live_20210301_models.RequestPasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_paster_with_options(runtime)

    async def request_paster_async(self) -> mind_live_20210301_models.RequestPasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_paster_with_options_async(runtime)

    def request_reset_data_with_options(
        self,
        request: mind_live_20210301_models.RequestResetDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestResetDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestResetData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestResetDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_reset_data_with_options_async(
        self,
        request: mind_live_20210301_models.RequestResetDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestResetDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.live_source):
            query['LiveSource'] = request.live_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestResetData',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestResetDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_reset_data(
        self,
        request: mind_live_20210301_models.RequestResetDataRequest,
    ) -> mind_live_20210301_models.RequestResetDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_reset_data_with_options(request, runtime)

    async def request_reset_data_async(
        self,
        request: mind_live_20210301_models.RequestResetDataRequest,
    ) -> mind_live_20210301_models.RequestResetDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_reset_data_with_options_async(request, runtime)

    def request_service_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestServiceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestServiceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestServiceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_service_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestServiceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestServiceInfo',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestServiceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_service_info(self) -> mind_live_20210301_models.RequestServiceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_service_info_with_options(runtime)

    async def request_service_info_async(self) -> mind_live_20210301_models.RequestServiceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_service_info_with_options_async(runtime)

    def request_user_config_with_options(
        self,
        request: mind_live_20210301_models.RequestUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_user_config_with_options_async(
        self,
        request: mind_live_20210301_models.RequestUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequestUserConfig',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_user_config(
        self,
        request: mind_live_20210301_models.RequestUserConfigRequest,
    ) -> mind_live_20210301_models.RequestUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_user_config_with_options(request, runtime)

    async def request_user_config_async(
        self,
        request: mind_live_20210301_models.RequestUserConfigRequest,
    ) -> mind_live_20210301_models.RequestUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_user_config_with_options_async(request, runtime)

    def request_user_sell_point_template_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestUserSellPointTemplateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestUserSellPointTemplate',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserSellPointTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_user_sell_point_template_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.RequestUserSellPointTemplateResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RequestUserSellPointTemplate',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.RequestUserSellPointTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_user_sell_point_template(self) -> mind_live_20210301_models.RequestUserSellPointTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_user_sell_point_template_with_options(runtime)

    async def request_user_sell_point_template_async(self) -> mind_live_20210301_models.RequestUserSellPointTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_user_sell_point_template_with_options_async(runtime)

    def reset_device_with_options(
        self,
        request: mind_live_20210301_models.ResetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ResetDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ResetDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_device_with_options_async(
        self,
        request: mind_live_20210301_models.ResetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.ResetDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDevice',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.ResetDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_device(
        self,
        request: mind_live_20210301_models.ResetDeviceRequest,
    ) -> mind_live_20210301_models.ResetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_device_with_options(request, runtime)

    async def reset_device_async(
        self,
        request: mind_live_20210301_models.ResetDeviceRequest,
    ) -> mind_live_20210301_models.ResetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_device_with_options_async(request, runtime)

    def update_current_item_with_options(
        self,
        request: mind_live_20210301_models.UpdateCurrentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateCurrentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCurrentItem',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateCurrentItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_current_item_with_options_async(
        self,
        request: mind_live_20210301_models.UpdateCurrentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateCurrentItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCurrentItem',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateCurrentItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_current_item(
        self,
        request: mind_live_20210301_models.UpdateCurrentItemRequest,
    ) -> mind_live_20210301_models.UpdateCurrentItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_current_item_with_options(request, runtime)

    async def update_current_item_async(
        self,
        request: mind_live_20210301_models.UpdateCurrentItemRequest,
    ) -> mind_live_20210301_models.UpdateCurrentItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_current_item_with_options_async(request, runtime)

    def update_live_sell_point_state_with_options(
        self,
        request: mind_live_20210301_models.UpdateLiveSellPointStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateLiveSellPointStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveSellPointStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_sell_point_state_with_options_async(
        self,
        request: mind_live_20210301_models.UpdateLiveSellPointStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateLiveSellPointStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSellPointState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveSellPointStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_sell_point_state(
        self,
        request: mind_live_20210301_models.UpdateLiveSellPointStateRequest,
    ) -> mind_live_20210301_models.UpdateLiveSellPointStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_sell_point_state_with_options(request, runtime)

    async def update_live_sell_point_state_async(
        self,
        request: mind_live_20210301_models.UpdateLiveSellPointStateRequest,
    ) -> mind_live_20210301_models.UpdateLiveSellPointStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_sell_point_state_with_options_async(request, runtime)

    def update_live_teleprompter_state_with_options(
        self,
        request: mind_live_20210301_models.UpdateLiveTeleprompterStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateLiveTeleprompterStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveTeleprompterStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_teleprompter_state_with_options_async(
        self,
        request: mind_live_20210301_models.UpdateLiveTeleprompterStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mind_live_20210301_models.UpdateLiveTeleprompterStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display):
            query['Display'] = request.display
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTeleprompterState',
            version='2021-03-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mind_live_20210301_models.UpdateLiveTeleprompterStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_teleprompter_state(
        self,
        request: mind_live_20210301_models.UpdateLiveTeleprompterStateRequest,
    ) -> mind_live_20210301_models.UpdateLiveTeleprompterStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_teleprompter_state_with_options(request, runtime)

    async def update_live_teleprompter_state_async(
        self,
        request: mind_live_20210301_models.UpdateLiveTeleprompterStateRequest,
    ) -> mind_live_20210301_models.UpdateLiveTeleprompterStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_teleprompter_state_with_options_async(request, runtime)
