# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_speechfiletranscriberlite20211221 import models as speech_file_transcriber_lite_20211221_models
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
        self._endpoint = self.get_endpoint('speechfiletranscriberlite', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_task_result_with_options(
        self,
        request: speech_file_transcriber_lite_20211221_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> speech_file_transcriber_lite_20211221_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskResult',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            speech_file_transcriber_lite_20211221_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        request: speech_file_transcriber_lite_20211221_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> speech_file_transcriber_lite_20211221_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskResult',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            speech_file_transcriber_lite_20211221_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        request: speech_file_transcriber_lite_20211221_models.GetTaskResultRequest,
    ) -> speech_file_transcriber_lite_20211221_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_result_with_options(request, runtime)

    async def get_task_result_async(
        self,
        request: speech_file_transcriber_lite_20211221_models.GetTaskResultRequest,
    ) -> speech_file_transcriber_lite_20211221_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_result_with_options_async(request, runtime)

    def submit_task_with_options(
        self,
        request: speech_file_transcriber_lite_20211221_models.SubmitTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> speech_file_transcriber_lite_20211221_models.SubmitTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTask',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            speech_file_transcriber_lite_20211221_models.SubmitTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_task_with_options_async(
        self,
        request: speech_file_transcriber_lite_20211221_models.SubmitTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> speech_file_transcriber_lite_20211221_models.SubmitTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTask',
            version='2021-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            speech_file_transcriber_lite_20211221_models.SubmitTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_task(
        self,
        request: speech_file_transcriber_lite_20211221_models.SubmitTaskRequest,
    ) -> speech_file_transcriber_lite_20211221_models.SubmitTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_task_with_options(request, runtime)

    async def submit_task_async(
        self,
        request: speech_file_transcriber_lite_20211221_models.SubmitTaskRequest,
    ) -> speech_file_transcriber_lite_20211221_models.SubmitTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_task_with_options_async(request, runtime)
