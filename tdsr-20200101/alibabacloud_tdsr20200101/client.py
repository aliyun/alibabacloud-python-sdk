# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tdsr20200101 import models as tdsr_20200101_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'lyj.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tdsr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_single_conn_data_with_options(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            self.do_rpcrequest('GetSingleConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_single_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            await self.do_rpcrequest_async('GetSingleConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_single_conn_data(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_single_conn_data_with_options(request, runtime)

    async def get_single_conn_data_async(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_single_conn_data_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            self.do_rpcrequest('GetTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            await self.do_rpcrequest_async('GetTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_status(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def link_image_with_options(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LinkImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            self.do_rpcrequest('LinkImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def link_image_with_options_async(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LinkImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            await self.do_rpcrequest_async('LinkImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def link_image(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
    ) -> tdsr_20200101_models.LinkImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.link_image_with_options(request, runtime)

    async def link_image_async(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
    ) -> tdsr_20200101_models.LinkImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.link_image_with_options_async(request, runtime)

    def add_scene_with_options(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            self.do_rpcrequest('AddScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_scene_with_options_async(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            await self.do_rpcrequest_async('AddScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scene(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
    ) -> tdsr_20200101_models.AddSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scene_with_options(request, runtime)

    async def add_scene_async(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
    ) -> tdsr_20200101_models.AddSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scene_with_options_async(request, runtime)

    def update_conn_data_with_options(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            self.do_rpcrequest('UpdateConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            await self.do_rpcrequest_async('UpdateConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_conn_data(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_conn_data_with_options(request, runtime)

    async def update_conn_data_async(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_conn_data_with_options_async(request, runtime)

    def rectify_image_with_options(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            self.do_rpcrequest('RectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rectify_image_with_options_async(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            await self.do_rpcrequest_async('RectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rectify_image(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.rectify_image_with_options(request, runtime)

    async def rectify_image_async(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rectify_image_with_options_async(request, runtime)

    def label_build_with_options(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            self.do_rpcrequest('LabelBuild', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def label_build_with_options_async(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            await self.do_rpcrequest_async('LabelBuild', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def label_build(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        runtime = util_models.RuntimeOptions()
        return self.label_build_with_options(request, runtime)

    async def label_build_async(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        runtime = util_models.RuntimeOptions()
        return await self.label_build_with_options_async(request, runtime)

    def drop_scene_with_options(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            self.do_rpcrequest('DropScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def drop_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            await self.do_rpcrequest_async('DropScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_scene(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
    ) -> tdsr_20200101_models.DropSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_scene_with_options(request, runtime)

    async def drop_scene_async(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
    ) -> tdsr_20200101_models.DropSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_scene_with_options_async(request, runtime)

    def optimize_right_angle_with_options(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            self.do_rpcrequest('OptimizeRightAngle', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def optimize_right_angle_with_options_async(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            await self.do_rpcrequest_async('OptimizeRightAngle', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def optimize_right_angle(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        runtime = util_models.RuntimeOptions()
        return self.optimize_right_angle_with_options(request, runtime)

    async def optimize_right_angle_async(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.optimize_right_angle_with_options_async(request, runtime)

    def add_relative_position_with_options(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            self.do_rpcrequest('AddRelativePosition', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_relative_position_with_options_async(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            await self.do_rpcrequest_async('AddRelativePosition', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_relative_position(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_relative_position_with_options(request, runtime)

    async def add_relative_position_async(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_relative_position_with_options_async(request, runtime)

    def detail_scene_with_options(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            self.do_rpcrequest('DetailScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detail_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            await self.do_rpcrequest_async('DetailScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_scene(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_scene_with_options(request, runtime)

    async def detail_scene_async(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_scene_with_options_async(request, runtime)

    def create_scene_with_options(
        self,
        request: tdsr_20200101_models.CreateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateSceneResponse(),
            self.do_rpcrequest('CreateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        request: tdsr_20200101_models.CreateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateSceneResponse(),
            await self.do_rpcrequest_async('CreateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scene(
        self,
        request: tdsr_20200101_models.CreateSceneRequest,
    ) -> tdsr_20200101_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_with_options(request, runtime)

    async def create_scene_async(
        self,
        request: tdsr_20200101_models.CreateSceneRequest,
    ) -> tdsr_20200101_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: tdsr_20200101_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteFileResponse(),
            self.do_rpcrequest('DeleteFile', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: tdsr_20200101_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteFileResponse(),
            await self.do_rpcrequest_async('DeleteFile', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file(
        self,
        request: tdsr_20200101_models.DeleteFileRequest,
    ) -> tdsr_20200101_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: tdsr_20200101_models.DeleteFileRequest,
    ) -> tdsr_20200101_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def check_resource_with_options(
        self,
        request: tdsr_20200101_models.CheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckResourceResponse(),
            self.do_rpcrequest('CheckResource', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_resource_with_options_async(
        self,
        request: tdsr_20200101_models.CheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckResourceResponse(),
            await self.do_rpcrequest_async('CheckResource', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_resource(
        self,
        request: tdsr_20200101_models.CheckResourceRequest,
    ) -> tdsr_20200101_models.CheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_resource_with_options(request, runtime)

    async def check_resource_async(
        self,
        request: tdsr_20200101_models.CheckResourceRequest,
    ) -> tdsr_20200101_models.CheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_resource_with_options_async(request, runtime)

    def list_scene_with_options(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            self.do_rpcrequest('ListScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scene_with_options_async(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            await self.do_rpcrequest_async('ListScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scene(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
    ) -> tdsr_20200101_models.ListSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scene_with_options(request, runtime)

    async def list_scene_async(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
    ) -> tdsr_20200101_models.ListSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scene_with_options_async(request, runtime)

    def publish_hotspot_with_options(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            self.do_rpcrequest('PublishHotspot', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_hotspot_with_options_async(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            await self.do_rpcrequest_async('PublishHotspot', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_hotspot(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    async def publish_hotspot_async(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_hotspot_with_options_async(request, runtime)

    def update_scene_with_options(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            self.do_rpcrequest('UpdateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            await self.do_rpcrequest_async('UpdateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_scene(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    async def update_scene_async(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_with_options_async(request, runtime)

    def update_layout_data_with_options(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            self.do_rpcrequest('UpdateLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            await self.do_rpcrequest_async('UpdateLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_layout_data(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_layout_data_with_options(request, runtime)

    async def update_layout_data_async(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_layout_data_with_options_async(request, runtime)

    def save_hotspot_tag_with_options(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            self.do_rpcrequest('SaveHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_hotspot_tag_with_options_async(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            await self.do_rpcrequest_async('SaveHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_hotspot_tag(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    async def save_hotspot_tag_async(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_hotspot_tag_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: tdsr_20200101_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: tdsr_20200101_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteProjectResponse(),
            await self.do_rpcrequest_async('DeleteProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: tdsr_20200101_models.DeleteProjectRequest,
    ) -> tdsr_20200101_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: tdsr_20200101_models.DeleteProjectRequest,
    ) -> tdsr_20200101_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def rect_vertical_with_options(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            self.do_rpcrequest('RectVertical', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rect_vertical_with_options_async(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            await self.do_rpcrequest_async('RectVertical', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rect_vertical(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        runtime = util_models.RuntimeOptions()
        return self.rect_vertical_with_options(request, runtime)

    async def rect_vertical_async(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rect_vertical_with_options_async(request, runtime)

    def pred_image_with_options(
        self,
        request: tdsr_20200101_models.PredImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            self.do_rpcrequest('PredImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pred_image_with_options_async(
        self,
        request: tdsr_20200101_models.PredImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            await self.do_rpcrequest_async('PredImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pred_image(
        self,
        request: tdsr_20200101_models.PredImageRequest,
    ) -> tdsr_20200101_models.PredImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.pred_image_with_options(request, runtime)

    async def pred_image_async(
        self,
        request: tdsr_20200101_models.PredImageRequest,
    ) -> tdsr_20200101_models.PredImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pred_image_with_options_async(request, runtime)

    def get_oss_policy_with_options(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            self.do_rpcrequest('GetOssPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_oss_policy_with_options_async(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            await self.do_rpcrequest_async('GetOssPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_oss_policy(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    async def get_oss_policy_async(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_policy_with_options_async(request, runtime)

    def get_conn_data_with_options(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            self.do_rpcrequest('GetConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            await self.do_rpcrequest_async('GetConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conn_data(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conn_data_with_options(request, runtime)

    async def get_conn_data_async(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conn_data_with_options_async(request, runtime)

    def temp_preview_status_with_options(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            self.do_rpcrequest('TempPreviewStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def temp_preview_status_with_options_async(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            await self.do_rpcrequest_async('TempPreviewStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def temp_preview_status(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_status_with_options(request, runtime)

    async def temp_preview_status_async(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_preview_status_with_options_async(request, runtime)

    def add_project_with_options(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            self.do_rpcrequest('AddProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_project_with_options_async(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            await self.do_rpcrequest_async('AddProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_project(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
    ) -> tdsr_20200101_models.AddProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_project_with_options(request, runtime)

    async def add_project_async(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
    ) -> tdsr_20200101_models.AddProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_project_with_options_async(request, runtime)

    def detail_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            self.do_rpcrequest('DetailSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detail_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            await self.do_rpcrequest_async('DetailSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_sub_scene(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_sub_scene_with_options(request, runtime)

    async def detail_sub_scene_async(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_sub_scene_with_options_async(request, runtime)

    def list_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            self.do_rpcrequest('ListSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            await self.do_rpcrequest_async('ListSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sub_scene(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sub_scene_with_options(request, runtime)

    async def list_sub_scene_async(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sub_scene_with_options_async(request, runtime)

    def update_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            self.do_rpcrequest('UpdateSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            await self.do_rpcrequest_async('UpdateSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sub_scene(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_with_options(request, runtime)

    async def update_sub_scene_async(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sub_scene_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: tdsr_20200101_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetJobResponse(),
            self.do_rpcrequest('GetJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: tdsr_20200101_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetJobResponse(),
            await self.do_rpcrequest_async('GetJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job(
        self,
        request: tdsr_20200101_models.GetJobRequest,
    ) -> tdsr_20200101_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: tdsr_20200101_models.GetJobRequest,
    ) -> tdsr_20200101_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: tdsr_20200101_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: tdsr_20200101_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateProjectResponse(),
            await self.do_rpcrequest_async('CreateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: tdsr_20200101_models.CreateProjectRequest,
    ) -> tdsr_20200101_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: tdsr_20200101_models.CreateProjectRequest,
    ) -> tdsr_20200101_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def save_hotspot_config_with_options(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            self.do_rpcrequest('SaveHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_hotspot_config_with_options_async(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            await self.do_rpcrequest_async('SaveHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_hotspot_config(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    async def save_hotspot_config_async(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_hotspot_config_with_options_async(request, runtime)

    def get_window_config_with_options(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            self.do_rpcrequest('GetWindowConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_window_config_with_options_async(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            await self.do_rpcrequest_async('GetWindowConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_window_config(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    async def get_window_config_async(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_window_config_with_options_async(request, runtime)

    def get_hotspot_config_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            self.do_rpcrequest('GetHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotspot_config_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            await self.do_rpcrequest_async('GetHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_config(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    async def get_hotspot_config_async(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_config_with_options_async(request, runtime)

    def get_scene_build_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            self.do_rpcrequest('GetSceneBuildTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_scene_build_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            await self.do_rpcrequest_async('GetSceneBuildTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scene_build_task_status(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_build_task_status_with_options(request, runtime)

    async def get_scene_build_task_status_async(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_build_task_status_with_options_async(request, runtime)

    def temp_preview_with_options(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            self.do_rpcrequest('TempPreview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def temp_preview_with_options_async(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            await self.do_rpcrequest_async('TempPreview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def temp_preview(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_with_options(request, runtime)

    async def temp_preview_async(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_preview_with_options_async(request, runtime)

    def detail_project_with_options(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            self.do_rpcrequest('DetailProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detail_project_with_options_async(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            await self.do_rpcrequest_async('DetailProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_project(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_project_with_options(request, runtime)

    async def detail_project_async(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_project_with_options_async(request, runtime)

    def list_scenes_with_options(
        self,
        request: tdsr_20200101_models.ListScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListScenesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListScenesResponse(),
            self.do_rpcrequest('ListScenes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenes_with_options_async(
        self,
        request: tdsr_20200101_models.ListScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListScenesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListScenesResponse(),
            await self.do_rpcrequest_async('ListScenes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenes(
        self,
        request: tdsr_20200101_models.ListScenesRequest,
    ) -> tdsr_20200101_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenes_with_options(request, runtime)

    async def list_scenes_async(
        self,
        request: tdsr_20200101_models.ListScenesRequest,
    ) -> tdsr_20200101_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenes_with_options_async(request, runtime)

    def drop_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            self.do_rpcrequest('DropSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def drop_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            await self.do_rpcrequest_async('DropSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_sub_scene(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_sub_scene_with_options(request, runtime)

    async def drop_sub_scene_async(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_sub_scene_with_options_async(request, runtime)

    def get_hotspot_tag_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            self.do_rpcrequest('GetHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotspot_tag_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            await self.do_rpcrequest_async('GetHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_tag(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    async def get_hotspot_tag_async(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_tag_with_options_async(request, runtime)

    def drop_project_with_options(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            self.do_rpcrequest('DropProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def drop_project_with_options_async(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            await self.do_rpcrequest_async('DropProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_project(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
    ) -> tdsr_20200101_models.DropProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_project_with_options(request, runtime)

    async def drop_project_async(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
    ) -> tdsr_20200101_models.DropProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_project_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            self.do_rpcrequest('ListProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            await self.do_rpcrequest_async('ListProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
    ) -> tdsr_20200101_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
    ) -> tdsr_20200101_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def get_origin_layout_data_with_options(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            self.do_rpcrequest('GetOriginLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_origin_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            await self.do_rpcrequest_async('GetOriginLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_origin_layout_data(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_origin_layout_data_with_options(request, runtime)

    async def get_origin_layout_data_async(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_origin_layout_data_with_options_async(request, runtime)

    def get_hotspot_scene_data_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            self.do_rpcrequest('GetHotspotSceneData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hotspot_scene_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            await self.do_rpcrequest_async('GetHotspotSceneData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_scene_data(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_scene_data_with_options(request, runtime)

    async def get_hotspot_scene_data_async(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_scene_data_with_options_async(request, runtime)

    def scene_publish_with_options(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            self.do_rpcrequest('ScenePublish', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def scene_publish_with_options_async(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            await self.do_rpcrequest_async('ScenePublish', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scene_publish(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.scene_publish_with_options(request, runtime)

    async def scene_publish_async(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scene_publish_with_options_async(request, runtime)

    def get_rectify_image_with_options(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            self.do_rpcrequest('GetRectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rectify_image_with_options_async(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            await self.do_rpcrequest_async('GetRectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rectify_image(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rectify_image_with_options(request, runtime)

    async def get_rectify_image_async(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rectify_image_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            await self.do_rpcrequest_async('UpdateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def get_sub_scene_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            self.do_rpcrequest('GetSubSceneTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sub_scene_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            await self.do_rpcrequest_async('GetSubSceneTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sub_scene_task_status(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sub_scene_task_status_with_options(request, runtime)

    async def get_sub_scene_task_status_async(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sub_scene_task_status_with_options_async(request, runtime)

    def prediction_wall_line_with_options(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            self.do_rpcrequest('PredictionWallLine', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def prediction_wall_line_with_options_async(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            await self.do_rpcrequest_async('PredictionWallLine', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def prediction_wall_line(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.prediction_wall_line_with_options(request, runtime)

    async def prediction_wall_line_async(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.prediction_wall_line_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: tdsr_20200101_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPolicyResponse(),
            self.do_rpcrequest('GetPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: tdsr_20200101_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPolicyResponse(),
            await self.do_rpcrequest_async('GetPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_policy(
        self,
        request: tdsr_20200101_models.GetPolicyRequest,
    ) -> tdsr_20200101_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: tdsr_20200101_models.GetPolicyRequest,
    ) -> tdsr_20200101_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_scene_preview_info_with_options(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            self.do_rpcrequest('GetScenePreviewInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_scene_preview_info_with_options_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            await self.do_rpcrequest_async('GetScenePreviewInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scene_preview_info(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_info_with_options(request, runtime)

    async def get_scene_preview_info_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_preview_info_with_options_async(request, runtime)

    def add_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            self.do_rpcrequest('AddSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            await self.do_rpcrequest_async('AddSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sub_scene(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sub_scene_with_options(request, runtime)

    async def add_sub_scene_async(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sub_scene_with_options_async(request, runtime)

    def get_layout_data_with_options(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            self.do_rpcrequest('GetLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            await self.do_rpcrequest_async('GetLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_layout_data(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_layout_data_with_options(request, runtime)

    async def get_layout_data_async(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_layout_data_with_options_async(request, runtime)
