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

    def create_app_with_options(
        self,
        request: rtc_white_board_20201214_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_white_board_with_options(
        self,
        request: rtc_white_board_20201214_models.CreateWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.CreateWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWhiteBoard',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateWhiteBoardResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateWhiteBoard',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.CreateWhiteBoardResponse(),
            await self.call_api_async(params, req, runtime)
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

    def open_white_board_with_options(
        self,
        request: rtc_white_board_20201214_models.OpenWhiteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.OpenWhiteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenWhiteBoard',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.OpenWhiteBoardResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='OpenWhiteBoard',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.OpenWhiteBoardResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='RefreshUsersPermissions',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.RefreshUsersPermissionsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='RefreshUsersPermissions',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.RefreshUsersPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_app_callback_url_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppCallbackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppCallbackUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppCallbackUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackUrlResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='SetAppCallbackUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppCallbackUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_app_domain_names_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppDomainNames',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppDomainNamesResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='SetAppDomainNames',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppDomainNamesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_app_name_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppNameResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='SetAppName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppNameResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_app_status_with_options(
        self,
        request: rtc_white_board_20201214_models.SetAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_white_board_20201214_models.SetAppStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppStatusResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='SetAppStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_white_board_20201214_models.SetAppStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
