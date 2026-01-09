# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('umeng-finplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def build_sts_akwith_options(
        self,
        request: main_models.BuildStsAKRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildStsAKResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'BuildStsAK',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/buildStsAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildStsAKResponse(),
            self.call_api(params, req, runtime)
        )

    async def build_sts_akwith_options_async(
        self,
        request: main_models.BuildStsAKRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildStsAKResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'BuildStsAK',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/buildStsAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildStsAKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def build_sts_ak(
        self,
        request: main_models.BuildStsAKRequest,
    ) -> main_models.BuildStsAKResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.build_sts_akwith_options(request, headers, runtime)

    async def build_sts_ak_async(
        self,
        request: main_models.BuildStsAKRequest,
    ) -> main_models.BuildStsAKResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.build_sts_akwith_options_async(request, headers, runtime)

    def build_sts_ak2with_options(
        self,
        request: main_models.BuildStsAK2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildStsAK2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BuildStsAK2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/buildStsAK2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildStsAK2Response(),
            self.call_api(params, req, runtime)
        )

    async def build_sts_ak2with_options_async(
        self,
        request: main_models.BuildStsAK2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildStsAK2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BuildStsAK2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/buildStsAK2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildStsAK2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def build_sts_ak2(
        self,
        request: main_models.BuildStsAK2Request,
    ) -> main_models.BuildStsAK2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.build_sts_ak2with_options(request, headers, runtime)

    async def build_sts_ak2_async(
        self,
        request: main_models.BuildStsAK2Request,
    ) -> main_models.BuildStsAK2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.build_sts_ak2with_options_async(request, headers, runtime)

    def cancel_task_with_options(
        self,
        request: main_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/cancelTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: main_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/cancelTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(request, headers, runtime)

    async def cancel_task_async(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(request, headers, runtime)

    def cancel_task_2with_options(
        self,
        request: main_models.CancelTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bc_id):
            body['bcId'] = request.bc_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/cancelTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_2with_options_async(
        self,
        request: main_models.CancelTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bc_id):
            body['bcId'] = request.bc_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/cancelTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task_2(
        self,
        request: main_models.CancelTask2Request,
    ) -> main_models.CancelTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_task_2with_options(request, headers, runtime)

    async def cancel_task_2_async(
        self,
        request: main_models.CancelTask2Request,
    ) -> main_models.CancelTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_task_2with_options_async(request, headers, runtime)

    def create_compute_task_with_options(
        self,
        request: main_models.CreateComputeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_task_with_options_async(
        self,
        request: main_models.CreateComputeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_task(
        self,
        request: main_models.CreateComputeTaskRequest,
    ) -> main_models.CreateComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_compute_task_with_options(request, headers, runtime)

    async def create_compute_task_async(
        self,
        request: main_models.CreateComputeTaskRequest,
    ) -> main_models.CreateComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_compute_task_with_options_async(request, headers, runtime)

    def create_compute_task_2with_options(
        self,
        request: main_models.CreateComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.task_source):
            body['taskSource'] = request.task_source
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_task_2with_options_async(
        self,
        request: main_models.CreateComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.task_source):
            body['taskSource'] = request.task_source
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_task_2(
        self,
        request: main_models.CreateComputeTask2Request,
    ) -> main_models.CreateComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_compute_task_2with_options(request, headers, runtime)

    async def create_compute_task_2_async(
        self,
        request: main_models.CreateComputeTask2Request,
    ) -> main_models.CreateComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_compute_task_2with_options_async(request, headers, runtime)

    def create_data_set_with_options(
        self,
        request: main_models.CreateDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_with_options_async(
        self,
        request: main_models.CreateDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set(
        self,
        request: main_models.CreateDataSetRequest,
    ) -> main_models.CreateDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_data_set_with_options(request, headers, runtime)

    async def create_data_set_async(
        self,
        request: main_models.CreateDataSetRequest,
    ) -> main_models.CreateDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_data_set_with_options_async(request, headers, runtime)

    def create_data_set_2with_options(
        self,
        request: main_models.CreateDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_2with_options_async(
        self,
        request: main_models.CreateDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/createDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set_2(
        self,
        request: main_models.CreateDataSet2Request,
    ) -> main_models.CreateDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_data_set_2with_options(request, headers, runtime)

    async def create_data_set_2_async(
        self,
        request: main_models.CreateDataSet2Request,
    ) -> main_models.CreateDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_data_set_2with_options_async(request, headers, runtime)

    def create_instance_task_with_options(
        self,
        request: main_models.CreateInstanceTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.calback_url):
            body['CalbackUrl'] = request.calback_url
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not DaraCore.is_null(request.monitor_type):
            body['MonitorType'] = request.monitor_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.output_config):
            body['OutputConfig'] = request.output_config
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.score_strategy_config):
            body['ScoreStrategyConfig'] = request.score_strategy_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/CreateInstanceTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_task_with_options_async(
        self,
        request: main_models.CreateInstanceTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.calback_url):
            body['CalbackUrl'] = request.calback_url
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not DaraCore.is_null(request.monitor_type):
            body['MonitorType'] = request.monitor_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.output_config):
            body['OutputConfig'] = request.output_config
        if not DaraCore.is_null(request.request_id):
            body['RequestId'] = request.request_id
        if not DaraCore.is_null(request.score_strategy_config):
            body['ScoreStrategyConfig'] = request.score_strategy_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/CreateInstanceTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_task(
        self,
        request: main_models.CreateInstanceTaskRequest,
    ) -> main_models.CreateInstanceTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_task_with_options(request, headers, runtime)

    async def create_instance_task_async(
        self,
        request: main_models.CreateInstanceTaskRequest,
    ) -> main_models.CreateInstanceTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_task_with_options_async(request, headers, runtime)

    def create_know_ledge_with_options(
        self,
        tmp_req: main_models.CreateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowLedgeResponse:
        tmp_req.validate()
        request = main_models.CreateKnowLedgeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowLedge',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/createKnowLedge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowLedgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_know_ledge_with_options_async(
        self,
        tmp_req: main_models.CreateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowLedgeResponse:
        tmp_req.validate()
        request = main_models.CreateKnowLedgeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowLedge',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/createKnowLedge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowLedgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_know_ledge(
        self,
        request: main_models.CreateKnowLedgeRequest,
    ) -> main_models.CreateKnowLedgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_know_ledge_with_options(request, headers, runtime)

    async def create_know_ledge_async(
        self,
        request: main_models.CreateKnowLedgeRequest,
    ) -> main_models.CreateKnowLedgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_know_ledge_with_options_async(request, headers, runtime)

    def encrypt_invoke_with_options(
        self,
        request: main_models.EncryptInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EncryptInvokeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.encrypt_key):
            body['encryptKey'] = request.encrypt_key
        if not DaraCore.is_null(request.method_name):
            body['methodName'] = request.method_name
        if not DaraCore.is_null(request.sign):
            body['sign'] = request.sign
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EncryptInvoke',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/encryptInvoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_invoke_with_options_async(
        self,
        request: main_models.EncryptInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EncryptInvokeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.encrypt_key):
            body['encryptKey'] = request.encrypt_key
        if not DaraCore.is_null(request.method_name):
            body['methodName'] = request.method_name
        if not DaraCore.is_null(request.sign):
            body['sign'] = request.sign
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EncryptInvoke',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/encryptInvoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt_invoke(
        self,
        request: main_models.EncryptInvokeRequest,
    ) -> main_models.EncryptInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.encrypt_invoke_with_options(request, headers, runtime)

    async def encrypt_invoke_async(
        self,
        request: main_models.EncryptInvokeRequest,
    ) -> main_models.EncryptInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.encrypt_invoke_with_options_async(request, headers, runtime)

    def get_crowd_dataset_with_options(
        self,
        tmp_req: main_models.GetCrowdDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCrowdDatasetResponse:
        tmp_req.validate()
        request = main_models.GetCrowdDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCrowdDataset',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getCrowdDataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCrowdDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_crowd_dataset_with_options_async(
        self,
        tmp_req: main_models.GetCrowdDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCrowdDatasetResponse:
        tmp_req.validate()
        request = main_models.GetCrowdDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCrowdDataset',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getCrowdDataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCrowdDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_crowd_dataset(
        self,
        request: main_models.GetCrowdDatasetRequest,
    ) -> main_models.GetCrowdDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_crowd_dataset_with_options(request, headers, runtime)

    async def get_crowd_dataset_async(
        self,
        request: main_models.GetCrowdDatasetRequest,
    ) -> main_models.GetCrowdDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_crowd_dataset_with_options_async(request, headers, runtime)

    def get_knowledge_data_with_options(
        self,
        tmp_req: main_models.GetKnowledgeDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeDataResponse:
        tmp_req.validate()
        request = main_models.GetKnowledgeDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeData',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getKnowledgeData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_data_with_options_async(
        self,
        tmp_req: main_models.GetKnowledgeDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeDataResponse:
        tmp_req.validate()
        request = main_models.GetKnowledgeDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeData',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getKnowledgeData',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_data(
        self,
        request: main_models.GetKnowledgeDataRequest,
    ) -> main_models.GetKnowledgeDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_data_with_options(request, headers, runtime)

    async def get_knowledge_data_async(
        self,
        request: main_models.GetKnowledgeDataRequest,
    ) -> main_models.GetKnowledgeDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_data_with_options_async(request, headers, runtime)

    def get_yzd_instance_task_result_with_options(
        self,
        tmp_req: main_models.GetYzdInstanceTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetYzdInstanceTaskResultResponse:
        tmp_req.validate()
        request = main_models.GetYzdInstanceTaskResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYzdInstanceTaskResult',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getYzdInstanceTaskResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYzdInstanceTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yzd_instance_task_result_with_options_async(
        self,
        tmp_req: main_models.GetYzdInstanceTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetYzdInstanceTaskResultResponse:
        tmp_req.validate()
        request = main_models.GetYzdInstanceTaskResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYzdInstanceTaskResult',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getYzdInstanceTaskResult',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYzdInstanceTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yzd_instance_task_result(
        self,
        request: main_models.GetYzdInstanceTaskResultRequest,
    ) -> main_models.GetYzdInstanceTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_yzd_instance_task_result_with_options(request, headers, runtime)

    async def get_yzd_instance_task_result_async(
        self,
        request: main_models.GetYzdInstanceTaskResultRequest,
    ) -> main_models.GetYzdInstanceTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_yzd_instance_task_result_with_options_async(request, headers, runtime)

    def get_yzd_sts_akwith_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetYzdStsAKResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetYzdStsAK',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getYzdStsAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYzdStsAKResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yzd_sts_akwith_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetYzdStsAKResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetYzdStsAK',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/getYzdStsAK',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYzdStsAKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yzd_sts_ak(self) -> main_models.GetYzdStsAKResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_yzd_sts_akwith_options(headers, runtime)

    async def get_yzd_sts_ak_async(self) -> main_models.GetYzdStsAKResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_yzd_sts_akwith_options_async(headers, runtime)

    def list_compute_task_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_task_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_task(self) -> main_models.ListComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_compute_task_with_options(headers, runtime)

    async def list_compute_task_async(self) -> main_models.ListComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_compute_task_with_options_async(headers, runtime)

    def list_compute_task_2with_options(
        self,
        request: main_models.ListComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_task_2with_options_async(
        self,
        request: main_models.ListComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_task_2(
        self,
        request: main_models.ListComputeTask2Request,
    ) -> main_models.ListComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_compute_task_2with_options(request, headers, runtime)

    async def list_compute_task_2_async(
        self,
        request: main_models.ListComputeTask2Request,
    ) -> main_models.ListComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_compute_task_2with_options_async(request, headers, runtime)

    def list_data_set_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(self) -> main_models.ListDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_set_with_options(headers, runtime)

    async def list_data_set_async(self) -> main_models.ListDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_set_with_options_async(headers, runtime)

    def list_data_set_2with_options(
        self,
        request: main_models.ListDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.page_no):
            body['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_2with_options_async(
        self,
        request: main_models.ListDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.page_no):
            body['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/listDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set_2(
        self,
        request: main_models.ListDataSet2Request,
    ) -> main_models.ListDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_set_2with_options(request, headers, runtime)

    async def list_data_set_2_async(
        self,
        request: main_models.ListDataSet2Request,
    ) -> main_models.ListDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_set_2with_options_async(request, headers, runtime)

    def remove_data_set_with_options(
        self,
        request: main_models.RemoveDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/removeDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_set_with_options_async(
        self,
        request: main_models.RemoveDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/removeDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_set(
        self,
        request: main_models.RemoveDataSetRequest,
    ) -> main_models.RemoveDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_data_set_with_options(request, headers, runtime)

    async def remove_data_set_async(
        self,
        request: main_models.RemoveDataSetRequest,
    ) -> main_models.RemoveDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_data_set_with_options_async(request, headers, runtime)

    def remove_data_set_2with_options(
        self,
        request: main_models.RemoveDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/removeDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_set_2with_options_async(
        self,
        request: main_models.RemoveDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/removeDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_set_2(
        self,
        request: main_models.RemoveDataSet2Request,
    ) -> main_models.RemoveDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_data_set_2with_options(request, headers, runtime)

    async def remove_data_set_2_async(
        self,
        request: main_models.RemoveDataSet2Request,
    ) -> main_models.RemoveDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_data_set_2with_options_async(request, headers, runtime)

    def save_crowd_dataset_and_binding_dataset_with_options(
        self,
        tmp_req: main_models.SaveCrowdDatasetAndBindingDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveCrowdDatasetAndBindingDatasetResponse:
        tmp_req.validate()
        request = main_models.SaveCrowdDatasetAndBindingDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveCrowdDatasetAndBindingDataset',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/saveCrowdDatasetAndBindingDataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCrowdDatasetAndBindingDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_crowd_dataset_and_binding_dataset_with_options_async(
        self,
        tmp_req: main_models.SaveCrowdDatasetAndBindingDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveCrowdDatasetAndBindingDatasetResponse:
        tmp_req.validate()
        request = main_models.SaveCrowdDatasetAndBindingDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveCrowdDatasetAndBindingDataset',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/saveCrowdDatasetAndBindingDataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCrowdDatasetAndBindingDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_crowd_dataset_and_binding_dataset(
        self,
        request: main_models.SaveCrowdDatasetAndBindingDatasetRequest,
    ) -> main_models.SaveCrowdDatasetAndBindingDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.save_crowd_dataset_and_binding_dataset_with_options(request, headers, runtime)

    async def save_crowd_dataset_and_binding_dataset_async(
        self,
        request: main_models.SaveCrowdDatasetAndBindingDatasetRequest,
    ) -> main_models.SaveCrowdDatasetAndBindingDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.save_crowd_dataset_and_binding_dataset_with_options_async(request, headers, runtime)

    def select_compute_task_with_options(
        self,
        request: main_models.SelectComputeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectComputeTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SelectComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_compute_task_with_options_async(
        self,
        request: main_models.SelectComputeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectComputeTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SelectComputeTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectComputeTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_compute_task(
        self,
        request: main_models.SelectComputeTaskRequest,
    ) -> main_models.SelectComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_compute_task_with_options(request, headers, runtime)

    async def select_compute_task_async(
        self,
        request: main_models.SelectComputeTaskRequest,
    ) -> main_models.SelectComputeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_compute_task_with_options_async(request, headers, runtime)

    def select_compute_task_2with_options(
        self,
        request: main_models.SelectComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bc_confirm):
            body['bcConfirm'] = request.bc_confirm
        if not DaraCore.is_null(request.bc_id):
            body['bcId'] = request.bc_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def select_compute_task_2with_options_async(
        self,
        request: main_models.SelectComputeTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectComputeTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bc_confirm):
            body['bcConfirm'] = request.bc_confirm
        if not DaraCore.is_null(request.bc_id):
            body['bcId'] = request.bc_id
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectComputeTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectComputeTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def select_compute_task_2(
        self,
        request: main_models.SelectComputeTask2Request,
    ) -> main_models.SelectComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_compute_task_2with_options(request, headers, runtime)

    async def select_compute_task_2_async(
        self,
        request: main_models.SelectComputeTask2Request,
    ) -> main_models.SelectComputeTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_compute_task_2with_options_async(request, headers, runtime)

    def select_data_set_with_options(
        self,
        request: main_models.SelectDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SelectDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_data_set_with_options_async(
        self,
        request: main_models.SelectDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SelectDataSet',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectDataSet',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_data_set(
        self,
        request: main_models.SelectDataSetRequest,
    ) -> main_models.SelectDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_data_set_with_options(request, headers, runtime)

    async def select_data_set_async(
        self,
        request: main_models.SelectDataSetRequest,
    ) -> main_models.SelectDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_data_set_with_options_async(request, headers, runtime)

    def select_data_set_2with_options(
        self,
        request: main_models.SelectDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def select_data_set_2with_options_async(
        self,
        request: main_models.SelectDataSet2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectDataSet2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectDataSet2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/selectDataSet2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def select_data_set_2(
        self,
        request: main_models.SelectDataSet2Request,
    ) -> main_models.SelectDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_data_set_2with_options(request, headers, runtime)

    async def select_data_set_2_async(
        self,
        request: main_models.SelectDataSet2Request,
    ) -> main_models.SelectDataSet2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_data_set_2with_options_async(request, headers, runtime)

    def submit_data_set_task_with_options(
        self,
        request: main_models.SubmitDataSetTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDataSetTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SubmitDataSetTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/submitDataSetTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDataSetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_data_set_task_with_options_async(
        self,
        request: main_models.SubmitDataSetTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDataSetTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'SubmitDataSetTask',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/submitDataSetTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDataSetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_data_set_task(
        self,
        request: main_models.SubmitDataSetTaskRequest,
    ) -> main_models.SubmitDataSetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_data_set_task_with_options(request, headers, runtime)

    async def submit_data_set_task_async(
        self,
        request: main_models.SubmitDataSetTaskRequest,
    ) -> main_models.SubmitDataSetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_data_set_task_with_options_async(request, headers, runtime)

    def submit_data_set_task_2with_options(
        self,
        request: main_models.SubmitDataSetTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDataSetTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDataSetTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/submitDataSetTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDataSetTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def submit_data_set_task_2with_options_async(
        self,
        request: main_models.SubmitDataSetTask2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDataSetTask2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        if not DaraCore.is_null(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDataSetTask2',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/bc/submitDataSetTask2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDataSetTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_data_set_task_2(
        self,
        request: main_models.SubmitDataSetTask2Request,
    ) -> main_models.SubmitDataSetTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_data_set_task_2with_options(request, headers, runtime)

    async def submit_data_set_task_2_async(
        self,
        request: main_models.SubmitDataSetTask2Request,
    ) -> main_models.SubmitDataSetTask2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_data_set_task_2with_options_async(request, headers, runtime)

    def validate_know_ledge_with_options(
        self,
        tmp_req: main_models.ValidateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateKnowLedgeResponse:
        tmp_req.validate()
        request = main_models.ValidateKnowLedgeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'simple')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateKnowLedge',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/validateKnowLedge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateKnowLedgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_know_ledge_with_options_async(
        self,
        tmp_req: main_models.ValidateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateKnowLedgeResponse:
        tmp_req.validate()
        request = main_models.ValidateKnowLedgeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'simple')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateKnowLedge',
            version = '2022-09-13',
            protocol = 'HTTPS',
            pathname = f'/yzd/validateKnowLedge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateKnowLedgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_know_ledge(
        self,
        request: main_models.ValidateKnowLedgeRequest,
    ) -> main_models.ValidateKnowLedgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_know_ledge_with_options(request, headers, runtime)

    async def validate_know_ledge_async(
        self,
        request: main_models.ValidateKnowLedgeRequest,
    ) -> main_models.ValidateKnowLedgeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_know_ledge_with_options_async(request, headers, runtime)
