# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dplus20201216 import models as dplus_20201216_models
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
        self._endpoint = self.get_endpoint('dplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_image_amazon_task_with_options(
        self,
        tmp_req: dplus_20201216_models.CreateImageAmazonTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.CreateImageAmazonTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dplus_20201216_models.CreateImageAmazonTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.img_url_list):
            request.img_url_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.img_url_list, 'ImgUrlList', 'json')
        if not UtilClient.is_unset(tmp_req.text_list):
            request.text_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_list, 'TextList', 'json')
        query = {}
        query['Gif'] = request.gif
        query['ImgUrlList'] = request.img_url_list_shrink
        query['TemplateMode'] = request.template_mode
        query['TextList'] = request.text_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageAmazonTask',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.CreateImageAmazonTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_amazon_task_with_options_async(
        self,
        tmp_req: dplus_20201216_models.CreateImageAmazonTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.CreateImageAmazonTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dplus_20201216_models.CreateImageAmazonTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.img_url_list):
            request.img_url_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.img_url_list, 'ImgUrlList', 'json')
        if not UtilClient.is_unset(tmp_req.text_list):
            request.text_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_list, 'TextList', 'json')
        query = {}
        query['Gif'] = request.gif
        query['ImgUrlList'] = request.img_url_list_shrink
        query['TemplateMode'] = request.template_mode
        query['TextList'] = request.text_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageAmazonTask',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.CreateImageAmazonTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_amazon_task(
        self,
        request: dplus_20201216_models.CreateImageAmazonTaskRequest,
    ) -> dplus_20201216_models.CreateImageAmazonTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_amazon_task_with_options(request, runtime)

    async def create_image_amazon_task_async(
        self,
        request: dplus_20201216_models.CreateImageAmazonTaskRequest,
    ) -> dplus_20201216_models.CreateImageAmazonTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_amazon_task_with_options_async(request, runtime)

    def get_task_result_with_options(
        self,
        request: dplus_20201216_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskResult',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        request: dplus_20201216_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskResult',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        request: dplus_20201216_models.GetTaskResultRequest,
    ) -> dplus_20201216_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_result_with_options(request, runtime)

    async def get_task_result_async(
        self,
        request: dplus_20201216_models.GetTaskResultRequest,
    ) -> dplus_20201216_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_result_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: dplus_20201216_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: dplus_20201216_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dplus_20201216_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dplus_20201216_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: dplus_20201216_models.GetTaskStatusRequest,
    ) -> dplus_20201216_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: dplus_20201216_models.GetTaskStatusRequest,
    ) -> dplus_20201216_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)
