# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imp20210630 import models as imp_20210630_models
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
        self._endpoint = self.get_endpoint('imp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_live_with_options(
        self,
        request: imp_20210630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            self.do_rpcrequest('CreateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_live_with_options_async(
        self,
        request: imp_20210630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            await self.do_rpcrequest_async('CreateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_live(
        self,
        request: imp_20210630_models.CreateLiveRequest,
    ) -> imp_20210630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_with_options(request, runtime)

    async def create_live_async(
        self,
        request: imp_20210630_models.CreateLiveRequest,
    ) -> imp_20210630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: imp_20210630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: imp_20210630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppResponse(),
            await self.do_rpcrequest_async('DeleteApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(
        self,
        request: imp_20210630_models.DeleteAppRequest,
    ) -> imp_20210630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: imp_20210630_models.DeleteAppRequest,
    ) -> imp_20210630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def update_room_with_options(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            self.do_rpcrequest('UpdateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_room_with_options_async(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            await self.do_rpcrequest_async('UpdateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_room(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
    ) -> imp_20210630_models.UpdateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_room_with_options(request, runtime)

    async def update_room_async(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
    ) -> imp_20210630_models.UpdateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_room_with_options_async(request, runtime)

    def get_app_template_with_options(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppTemplateResponse(),
            self.do_rpcrequest('GetAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_template_with_options_async(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppTemplateResponse(),
            await self.do_rpcrequest_async('GetAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_template(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_template_with_options(request, runtime)

    async def get_app_template_async(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_template_with_options_async(request, runtime)

    def get_room_with_options(
        self,
        request: imp_20210630_models.GetRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            self.do_rpcrequest('GetRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_room_with_options_async(
        self,
        request: imp_20210630_models.GetRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            await self.do_rpcrequest_async('GetRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_room(
        self,
        request: imp_20210630_models.GetRoomRequest,
    ) -> imp_20210630_models.GetRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_room_with_options(request, runtime)

    async def get_room_async(
        self,
        request: imp_20210630_models.GetRoomRequest,
    ) -> imp_20210630_models.GetRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_room_with_options_async(request, runtime)

    def create_app_template_with_options(
        self,
        tmp_req: imp_20210630_models.CreateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppTemplateResponse(),
            self.do_rpcrequest('CreateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_template_with_options_async(
        self,
        tmp_req: imp_20210630_models.CreateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppTemplateResponse(),
            await self.do_rpcrequest_async('CreateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_template(
        self,
        request: imp_20210630_models.CreateAppTemplateRequest,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_template_with_options(request, runtime)

    async def create_app_template_async(
        self,
        request: imp_20210630_models.CreateAppTemplateRequest,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_template_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: imp_20210630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppsResponse(),
            self.do_rpcrequest('ListApps', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: imp_20210630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppsResponse(),
            await self.do_rpcrequest_async('ListApps', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(
        self,
        request: imp_20210630_models.ListAppsRequest,
    ) -> imp_20210630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: imp_20210630_models.ListAppsRequest,
    ) -> imp_20210630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_rooms_with_options(
        self,
        request: imp_20210630_models.ListRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            self.do_rpcrequest('ListRooms', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rooms_with_options_async(
        self,
        request: imp_20210630_models.ListRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            await self.do_rpcrequest_async('ListRooms', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rooms(
        self,
        request: imp_20210630_models.ListRoomsRequest,
    ) -> imp_20210630_models.ListRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rooms_with_options(request, runtime)

    async def list_rooms_async(
        self,
        request: imp_20210630_models.ListRoomsRequest,
    ) -> imp_20210630_models.ListRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rooms_with_options_async(request, runtime)

    def delete_app_template_with_options(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppTemplateResponse(),
            self.do_rpcrequest('DeleteAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_template_with_options_async(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppTemplateResponse(),
            await self.do_rpcrequest_async('DeleteAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_template(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_template_with_options(request, runtime)

    async def delete_app_template_async(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_template_with_options_async(request, runtime)

    def list_app_templates_with_options(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppTemplatesResponse(),
            self.do_rpcrequest('ListAppTemplates', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_templates_with_options_async(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppTemplatesResponse(),
            await self.do_rpcrequest_async('ListAppTemplates', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_templates(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    async def list_app_templates_async(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_templates_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: imp_20210630_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListComponentsResponse(),
            self.do_rpcrequest('ListComponents', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: imp_20210630_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListComponentsResponse(),
            await self.do_rpcrequest_async('ListComponents', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_components(
        self,
        request: imp_20210630_models.ListComponentsRequest,
    ) -> imp_20210630_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: imp_20210630_models.ListComponentsRequest,
    ) -> imp_20210630_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def update_live_with_options(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            self.do_rpcrequest('UpdateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_with_options_async(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            await self.do_rpcrequest_async('UpdateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
    ) -> imp_20210630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_with_options(request, runtime)

    async def update_live_async(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
    ) -> imp_20210630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_with_options_async(request, runtime)

    def update_app_template_config_with_options(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            self.do_rpcrequest('UpdateAppTemplateConfig', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_template_config_with_options_async(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            await self.do_rpcrequest_async('UpdateAppTemplateConfig', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_template_config(
        self,
        request: imp_20210630_models.UpdateAppTemplateConfigRequest,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_config_with_options(request, runtime)

    async def update_app_template_config_async(
        self,
        request: imp_20210630_models.UpdateAppTemplateConfigRequest,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_template_config_with_options_async(request, runtime)

    def stop_live_with_options(
        self,
        request: imp_20210630_models.StopLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            self.do_rpcrequest('StopLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_live_with_options_async(
        self,
        request: imp_20210630_models.StopLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            await self.do_rpcrequest_async('StopLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_live(
        self,
        request: imp_20210630_models.StopLiveRequest,
    ) -> imp_20210630_models.StopLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_with_options(request, runtime)

    async def stop_live_async(
        self,
        request: imp_20210630_models.StopLiveRequest,
    ) -> imp_20210630_models.StopLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: imp_20210630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppResponse(),
            self.do_rpcrequest('GetApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: imp_20210630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppResponse(),
            await self.do_rpcrequest_async('GetApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app(
        self,
        request: imp_20210630_models.GetAppRequest,
    ) -> imp_20210630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: imp_20210630_models.GetAppRequest,
    ) -> imp_20210630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def delete_live_with_options(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            self.do_rpcrequest('DeleteLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_with_options_async(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            await self.do_rpcrequest_async('DeleteLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_live(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
    ) -> imp_20210630_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_with_options(request, runtime)

    async def delete_live_async(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
    ) -> imp_20210630_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_with_options_async(request, runtime)

    def get_live_domain_status_with_options(
        self,
        tmp_req: imp_20210630_models.GetLiveDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveDomainStatusResponse(),
            self.do_rpcrequest('GetLiveDomainStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_live_domain_status_with_options_async(
        self,
        tmp_req: imp_20210630_models.GetLiveDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveDomainStatusResponse(),
            await self.do_rpcrequest_async('GetLiveDomainStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_live_domain_status(
        self,
        request: imp_20210630_models.GetLiveDomainStatusRequest,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_domain_status_with_options(request, runtime)

    async def get_live_domain_status_async(
        self,
        request: imp_20210630_models.GetLiveDomainStatusRequest,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_domain_status_with_options_async(request, runtime)

    def get_auth_token_with_options(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            self.do_rpcrequest('GetAuthToken', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            await self.do_rpcrequest_async('GetAuthToken', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auth_token(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    async def get_auth_token_async(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_token_with_options_async(request, runtime)

    def update_app_template_with_options(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateResponse(),
            self.do_rpcrequest('UpdateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_template_with_options_async(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateResponse(),
            await self.do_rpcrequest_async('UpdateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_template(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_with_options(request, runtime)

    async def update_app_template_async(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_template_with_options_async(request, runtime)

    def get_imp_product_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetImpProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            imp_20210630_models.GetImpProductStatusResponse(),
            self.do_rpcrequest('GetImpProductStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_imp_product_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetImpProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            imp_20210630_models.GetImpProductStatusResponse(),
            await self.do_rpcrequest_async('GetImpProductStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_imp_product_status(self) -> imp_20210630_models.GetImpProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_imp_product_status_with_options(runtime)

    async def get_imp_product_status_async(self) -> imp_20210630_models.GetImpProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_imp_product_status_with_options_async(runtime)

    def publish_live_with_options(
        self,
        request: imp_20210630_models.PublishLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            self.do_rpcrequest('PublishLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_live_with_options_async(
        self,
        request: imp_20210630_models.PublishLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            await self.do_rpcrequest_async('PublishLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_live(
        self,
        request: imp_20210630_models.PublishLiveRequest,
    ) -> imp_20210630_models.PublishLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_live_with_options(request, runtime)

    async def publish_live_async(
        self,
        request: imp_20210630_models.PublishLiveRequest,
    ) -> imp_20210630_models.PublishLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_live_with_options_async(request, runtime)

    def get_live_with_options(
        self,
        request: imp_20210630_models.GetLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            self.do_rpcrequest('GetLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_live_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            await self.do_rpcrequest_async('GetLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_live(
        self,
        request: imp_20210630_models.GetLiveRequest,
    ) -> imp_20210630_models.GetLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_with_options(request, runtime)

    async def get_live_async(
        self,
        request: imp_20210630_models.GetLiveRequest,
    ) -> imp_20210630_models.GetLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_with_options_async(request, runtime)

    def delete_room_with_options(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            self.do_rpcrequest('DeleteRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_room_with_options_async(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            await self.do_rpcrequest_async('DeleteRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_room(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
    ) -> imp_20210630_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    async def delete_room_async(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
    ) -> imp_20210630_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_room_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: imp_20210630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: imp_20210630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppResponse(),
            await self.do_rpcrequest_async('CreateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(
        self,
        request: imp_20210630_models.CreateAppRequest,
    ) -> imp_20210630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: imp_20210630_models.CreateAppRequest,
    ) -> imp_20210630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_room_with_options(
        self,
        request: imp_20210630_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_room_with_options_async(
        self,
        request: imp_20210630_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            await self.do_rpcrequest_async('CreateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(
        self,
        request: imp_20210630_models.CreateRoomRequest,
    ) -> imp_20210630_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: imp_20210630_models.CreateRoomRequest,
    ) -> imp_20210630_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: imp_20210630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppResponse(),
            self.do_rpcrequest('UpdateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: imp_20210630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppResponse(),
            await self.do_rpcrequest_async('UpdateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app(
        self,
        request: imp_20210630_models.UpdateAppRequest,
    ) -> imp_20210630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: imp_20210630_models.UpdateAppRequest,
    ) -> imp_20210630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)
