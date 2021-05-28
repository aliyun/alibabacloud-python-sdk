# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rtc_white_board20201214 import models as rtc_white_board_20201214_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('rtc-white-board', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_apps_with_options(
        self,
        request: rtc_white_board_20201214_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeAppsResponse(),
            self.do_rpcrequest('DescribeApps', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: rtc_white_board_20201214_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeAppsResponse(),
            await self.do_rpcrequest_async('DescribeApps', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apps(
        self,
        request: rtc_white_board_20201214_models.DescribeAppsRequest,
    ) -> rtc_white_board_20201214_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: rtc_white_board_20201214_models.DescribeAppsRequest,
    ) -> rtc_white_board_20201214_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def pause_white_board_recording_with_options(
        self,
        request: rtc_white_board_20201214_models.PauseWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse(),
            self.do_rpcrequest('PauseWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pause_white_board_recording_with_options_async(
        self,
        request: rtc_white_board_20201214_models.PauseWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse(),
            await self.do_rpcrequest_async('PauseWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pause_white_board_recording(
        self,
        request: rtc_white_board_20201214_models.PauseWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.pause_white_board_recording_with_options(request, runtime)

    async def pause_white_board_recording_async(
        self,
        request: rtc_white_board_20201214_models.PauseWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.PauseWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_white_board_recording_with_options_async(request, runtime)

    def set_app_callback_url_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppCallbackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackUrlResponse(),
            self.do_rpcrequest('SetAppCallbackUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_app_callback_url_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppCallbackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackUrlResponse(),
            await self.do_rpcrequest_async('SetAppCallbackUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_callback_url(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackUrlRequest,
    ) -> rtc_white_board_20201214_models.SetAppCallbackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_app_callback_url_with_options(request, runtime)

    async def set_app_callback_url_async(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackUrlRequest,
    ) -> rtc_white_board_20201214_models.SetAppCallbackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_app_callback_url_with_options_async(request, runtime)

    def start_white_board_recording_with_options(
        self,
        request: rtc_white_board_20201214_models.StartWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse(),
            self.do_rpcrequest('StartWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_white_board_recording_with_options_async(
        self,
        request: rtc_white_board_20201214_models.StartWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse(),
            await self.do_rpcrequest_async('StartWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_white_board_recording(
        self,
        request: rtc_white_board_20201214_models.StartWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_white_board_recording_with_options(request, runtime)

    async def start_white_board_recording_async(
        self,
        request: rtc_white_board_20201214_models.StartWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.StartWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_white_board_recording_with_options_async(request, runtime)

    def set_app_name_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppNameResponse(),
            self.do_rpcrequest('SetAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_app_name_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppNameResponse(),
            await self.do_rpcrequest_async('SetAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_name(
        self,
        request: rtc_white_board_20201214_models.SetAppNameRequest,
    ) -> rtc_white_board_20201214_models.SetAppNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_app_name_with_options(request, runtime)

    async def set_app_name_async(
        self,
        request: rtc_white_board_20201214_models.SetAppNameRequest,
    ) -> rtc_white_board_20201214_models.SetAppNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_app_name_with_options_async(request, runtime)

    def describe_white_boards_with_options(
        self,
        request: rtc_white_board_20201214_models.DescribeWhiteBoardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.DescribeWhiteBoardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeWhiteBoardsResponse(),
            self.do_rpcrequest('DescribeWhiteBoards', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_white_boards_with_options_async(
        self,
        request: rtc_white_board_20201214_models.DescribeWhiteBoardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.DescribeWhiteBoardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.DescribeWhiteBoardsResponse(),
            await self.do_rpcrequest_async('DescribeWhiteBoards', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_white_boards(
        self,
        request: rtc_white_board_20201214_models.DescribeWhiteBoardsRequest,
    ) -> rtc_white_board_20201214_models.DescribeWhiteBoardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_white_boards_with_options(request, runtime)

    async def describe_white_boards_async(
        self,
        request: rtc_white_board_20201214_models.DescribeWhiteBoardsRequest,
    ) -> rtc_white_board_20201214_models.DescribeWhiteBoardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_white_boards_with_options_async(request, runtime)

    def resume_white_board_recording_with_options(
        self,
        request: rtc_white_board_20201214_models.ResumeWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse(),
            self.do_rpcrequest('ResumeWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_white_board_recording_with_options_async(
        self,
        request: rtc_white_board_20201214_models.ResumeWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse(),
            await self.do_rpcrequest_async('ResumeWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_white_board_recording(
        self,
        request: rtc_white_board_20201214_models.ResumeWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_white_board_recording_with_options(request, runtime)

    async def resume_white_board_recording_async(
        self,
        request: rtc_white_board_20201214_models.ResumeWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.ResumeWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_white_board_recording_with_options_async(request, runtime)

    def set_app_domain_names_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppDomainNamesResponse(),
            self.do_rpcrequest('SetAppDomainNames', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_app_domain_names_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetAppDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppDomainNamesResponse(),
            await self.do_rpcrequest_async('SetAppDomainNames', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_domain_names(
        self,
        request: rtc_white_board_20201214_models.SetAppDomainNamesRequest,
    ) -> rtc_white_board_20201214_models.SetAppDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_app_domain_names_with_options(request, runtime)

    async def set_app_domain_names_async(
        self,
        request: rtc_white_board_20201214_models.SetAppDomainNamesRequest,
    ) -> rtc_white_board_20201214_models.SetAppDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_app_domain_names_with_options_async(request, runtime)

    def open_white_board_with_options(
        self,
        request: rtc_white_board_20201214_models.OpenWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.OpenWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.OpenWhiteBoardResponse(),
            self.do_rpcrequest('OpenWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_white_board_with_options_async(
        self,
        request: rtc_white_board_20201214_models.OpenWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.OpenWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.OpenWhiteBoardResponse(),
            await self.do_rpcrequest_async('OpenWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_white_board(
        self,
        request: rtc_white_board_20201214_models.OpenWhiteBoardRequest,
    ) -> rtc_white_board_20201214_models.OpenWhiteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_white_board_with_options(request, runtime)

    async def open_white_board_async(
        self,
        request: rtc_white_board_20201214_models.OpenWhiteBoardRequest,
    ) -> rtc_white_board_20201214_models.OpenWhiteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_white_board_with_options_async(request, runtime)

    def refresh_users_permissions_with_options(
        self,
        request: rtc_white_board_20201214_models.RefreshUsersPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.RefreshUsersPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.RefreshUsersPermissionsResponse(),
            self.do_rpcrequest('RefreshUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_users_permissions_with_options_async(
        self,
        request: rtc_white_board_20201214_models.RefreshUsersPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.RefreshUsersPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.RefreshUsersPermissionsResponse(),
            await self.do_rpcrequest_async('RefreshUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_users_permissions(
        self,
        request: rtc_white_board_20201214_models.RefreshUsersPermissionsRequest,
    ) -> rtc_white_board_20201214_models.RefreshUsersPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_users_permissions_with_options(request, runtime)

    async def refresh_users_permissions_async(
        self,
        request: rtc_white_board_20201214_models.RefreshUsersPermissionsRequest,
    ) -> rtc_white_board_20201214_models.RefreshUsersPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_users_permissions_with_options_async(request, runtime)

    def set_app_callback_type_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppCallbackTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackTypeResponse(),
            self.do_rpcrequest('SetAppCallbackType', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_app_callback_type_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppCallbackTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackTypeResponse(),
            await self.do_rpcrequest_async('SetAppCallbackType', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_callback_type(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackTypeRequest,
    ) -> rtc_white_board_20201214_models.SetAppCallbackTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_app_callback_type_with_options(request, runtime)

    async def set_app_callback_type_async(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackTypeRequest,
    ) -> rtc_white_board_20201214_models.SetAppCallbackTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_app_callback_type_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: rtc_white_board_20201214_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: rtc_white_board_20201214_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateAppResponse(),
            await self.do_rpcrequest_async('CreateApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(
        self,
        request: rtc_white_board_20201214_models.CreateAppRequest,
    ) -> rtc_white_board_20201214_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: rtc_white_board_20201214_models.CreateAppRequest,
    ) -> rtc_white_board_20201214_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def set_users_permissions_with_options(
        self,
        request: rtc_white_board_20201214_models.SetUsersPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetUsersPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetUsersPermissionsResponse(),
            self.do_rpcrequest('SetUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_users_permissions_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetUsersPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetUsersPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetUsersPermissionsResponse(),
            await self.do_rpcrequest_async('SetUsersPermissions', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_users_permissions(
        self,
        request: rtc_white_board_20201214_models.SetUsersPermissionsRequest,
    ) -> rtc_white_board_20201214_models.SetUsersPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_users_permissions_with_options(request, runtime)

    async def set_users_permissions_async(
        self,
        request: rtc_white_board_20201214_models.SetUsersPermissionsRequest,
    ) -> rtc_white_board_20201214_models.SetUsersPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_users_permissions_with_options_async(request, runtime)

    def create_white_board_with_options(
        self,
        request: rtc_white_board_20201214_models.CreateWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateWhiteBoardResponse(),
            self.do_rpcrequest('CreateWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_white_board_with_options_async(
        self,
        request: rtc_white_board_20201214_models.CreateWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateWhiteBoardResponse(),
            await self.do_rpcrequest_async('CreateWhiteBoard', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_white_board(
        self,
        request: rtc_white_board_20201214_models.CreateWhiteBoardRequest,
    ) -> rtc_white_board_20201214_models.CreateWhiteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_white_board_with_options(request, runtime)

    async def create_white_board_async(
        self,
        request: rtc_white_board_20201214_models.CreateWhiteBoardRequest,
    ) -> rtc_white_board_20201214_models.CreateWhiteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_white_board_with_options_async(request, runtime)

    def set_app_status_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppStatusResponse(),
            self.do_rpcrequest('SetAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_app_status_with_options_async(
        self,
        request: rtc_white_board_20201214_models.SetAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppStatusResponse(),
            await self.do_rpcrequest_async('SetAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_app_status(
        self,
        request: rtc_white_board_20201214_models.SetAppStatusRequest,
    ) -> rtc_white_board_20201214_models.SetAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_app_status_with_options(request, runtime)

    async def set_app_status_async(
        self,
        request: rtc_white_board_20201214_models.SetAppStatusRequest,
    ) -> rtc_white_board_20201214_models.SetAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_app_status_with_options_async(request, runtime)

    def stop_white_board_recording_with_options(
        self,
        request: rtc_white_board_20201214_models.StopWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse(),
            self.do_rpcrequest('StopWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_white_board_recording_with_options_async(
        self,
        request: rtc_white_board_20201214_models.StopWhiteBoardRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse(),
            await self.do_rpcrequest_async('StopWhiteBoardRecording', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_white_board_recording(
        self,
        request: rtc_white_board_20201214_models.StopWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_white_board_recording_with_options(request, runtime)

    async def stop_white_board_recording_async(
        self,
        request: rtc_white_board_20201214_models.StopWhiteBoardRecordingRequest,
    ) -> rtc_white_board_20201214_models.StopWhiteBoardRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_white_board_recording_with_options_async(request, runtime)
