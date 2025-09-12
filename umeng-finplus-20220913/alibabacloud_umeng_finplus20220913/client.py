# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_finplus20220913 import models as umeng_finplus_20220913_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def build_sts_akwith_options(
        self,
        request: umeng_finplus_20220913_models.BuildStsAKRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.BuildStsAKResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAKRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildStsAKResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='BuildStsAK',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/buildStsAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.BuildStsAKResponse(),
            self.call_api(params, req, runtime)
        )

    async def build_sts_akwith_options_async(
        self,
        request: umeng_finplus_20220913_models.BuildStsAKRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.BuildStsAKResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAKRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildStsAKResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='BuildStsAK',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/buildStsAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.BuildStsAKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def build_sts_ak(
        self,
        request: umeng_finplus_20220913_models.BuildStsAKRequest,
    ) -> umeng_finplus_20220913_models.BuildStsAKResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAKRequest
        @return: BuildStsAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.build_sts_akwith_options(request, headers, runtime)

    async def build_sts_ak_async(
        self,
        request: umeng_finplus_20220913_models.BuildStsAKRequest,
    ) -> umeng_finplus_20220913_models.BuildStsAKResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAKRequest
        @return: BuildStsAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.build_sts_akwith_options_async(request, headers, runtime)

    def build_sts_ak2with_options(
        self,
        request: umeng_finplus_20220913_models.BuildStsAK2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.BuildStsAK2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAK2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildStsAK2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BuildStsAK2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/buildStsAK2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.BuildStsAK2Response(),
            self.call_api(params, req, runtime)
        )

    async def build_sts_ak2with_options_async(
        self,
        request: umeng_finplus_20220913_models.BuildStsAK2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.BuildStsAK2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAK2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildStsAK2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BuildStsAK2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/buildStsAK2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.BuildStsAK2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def build_sts_ak2(
        self,
        request: umeng_finplus_20220913_models.BuildStsAK2Request,
    ) -> umeng_finplus_20220913_models.BuildStsAK2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAK2Request
        @return: BuildStsAK2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.build_sts_ak2with_options(request, headers, runtime)

    async def build_sts_ak2_async(
        self,
        request: umeng_finplus_20220913_models.BuildStsAK2Request,
    ) -> umeng_finplus_20220913_models.BuildStsAK2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: BuildStsAK2Request
        @return: BuildStsAK2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.build_sts_ak2with_options_async(request, headers, runtime)

    def cancel_task_with_options(
        self,
        request: umeng_finplus_20220913_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CancelTaskResponse:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/cancelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: umeng_finplus_20220913_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CancelTaskResponse:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/cancelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: umeng_finplus_20220913_models.CancelTaskRequest,
    ) -> umeng_finplus_20220913_models.CancelTaskResponse:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(request, headers, runtime)

    async def cancel_task_async(
        self,
        request: umeng_finplus_20220913_models.CancelTaskRequest,
    ) -> umeng_finplus_20220913_models.CancelTaskResponse:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(request, headers, runtime)

    def cancel_task_2with_options(
        self,
        request: umeng_finplus_20220913_models.CancelTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CancelTask2Response:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bc_id):
            body['bcId'] = request.bc_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/cancelTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CancelTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.CancelTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CancelTask2Response:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bc_id):
            body['bcId'] = request.bc_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/cancelTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CancelTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task_2(
        self,
        request: umeng_finplus_20220913_models.CancelTask2Request,
    ) -> umeng_finplus_20220913_models.CancelTask2Response:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTask2Request
        @return: CancelTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_2with_options(request, headers, runtime)

    async def cancel_task_2_async(
        self,
        request: umeng_finplus_20220913_models.CancelTask2Request,
    ) -> umeng_finplus_20220913_models.CancelTask2Response:
        """
        @summary 取消批量计算任务
        
        @param request: CancelTask2Request
        @return: CancelTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_2with_options_async(request, headers, runtime)

    def create_compute_task_with_options(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateComputeTaskResponse:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_task_with_options_async(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateComputeTaskResponse:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_task(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTaskRequest,
    ) -> umeng_finplus_20220913_models.CreateComputeTaskResponse:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTaskRequest
        @return: CreateComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_compute_task_with_options(request, headers, runtime)

    async def create_compute_task_async(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTaskRequest,
    ) -> umeng_finplus_20220913_models.CreateComputeTaskResponse:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTaskRequest
        @return: CreateComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_compute_task_with_options_async(request, headers, runtime)

    def create_compute_task_2with_options(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateComputeTask2Response:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.task_source):
            body['taskSource'] = request.task_source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_task_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateComputeTask2Response:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.morse_info_list):
            body['morseInfoList'] = request.morse_info_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.task_source):
            body['taskSource'] = request.task_source
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_task_2(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTask2Request,
    ) -> umeng_finplus_20220913_models.CreateComputeTask2Response:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTask2Request
        @return: CreateComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_compute_task_2with_options(request, headers, runtime)

    async def create_compute_task_2_async(
        self,
        request: umeng_finplus_20220913_models.CreateComputeTask2Request,
    ) -> umeng_finplus_20220913_models.CreateComputeTask2Response:
        """
        @summary 创建批量计算任务
        
        @param request: CreateComputeTask2Request
        @return: CreateComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_compute_task_2with_options_async(request, headers, runtime)

    def create_data_set_with_options(
        self,
        request: umeng_finplus_20220913_models.CreateDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_with_options_async(
        self,
        request: umeng_finplus_20220913_models.CreateDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set(
        self,
        request: umeng_finplus_20220913_models.CreateDataSetRequest,
    ) -> umeng_finplus_20220913_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @return: CreateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_set_with_options(request, headers, runtime)

    async def create_data_set_async(
        self,
        request: umeng_finplus_20220913_models.CreateDataSetRequest,
    ) -> umeng_finplus_20220913_models.CreateDataSetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDataSetRequest
        @return: CreateDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_set_with_options_async(request, headers, runtime)

    def create_data_set_2with_options(
        self,
        request: umeng_finplus_20220913_models.CreateDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateDataSet2Response:
        """
        @summary 创建数据集
        
        @param request: CreateDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.CreateDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateDataSet2Response:
        """
        @summary 创建数据集
        
        @param request: CreateDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/createDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set_2(
        self,
        request: umeng_finplus_20220913_models.CreateDataSet2Request,
    ) -> umeng_finplus_20220913_models.CreateDataSet2Response:
        """
        @summary 创建数据集
        
        @param request: CreateDataSet2Request
        @return: CreateDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_set_2with_options(request, headers, runtime)

    async def create_data_set_2_async(
        self,
        request: umeng_finplus_20220913_models.CreateDataSet2Request,
    ) -> umeng_finplus_20220913_models.CreateDataSet2Response:
        """
        @summary 创建数据集
        
        @param request: CreateDataSet2Request
        @return: CreateDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_set_2with_options_async(request, headers, runtime)

    def create_know_ledge_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.CreateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateKnowLedgeResponse:
        """
        @summary 友准达-创建知识库
        
        @param tmp_req: CreateKnowLedgeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKnowLedgeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.CreateKnowLedgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKnowLedge',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/createKnowLedge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateKnowLedgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_know_ledge_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.CreateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.CreateKnowLedgeResponse:
        """
        @summary 友准达-创建知识库
        
        @param tmp_req: CreateKnowLedgeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKnowLedgeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.CreateKnowLedgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKnowLedge',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/createKnowLedge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.CreateKnowLedgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_know_ledge(
        self,
        request: umeng_finplus_20220913_models.CreateKnowLedgeRequest,
    ) -> umeng_finplus_20220913_models.CreateKnowLedgeResponse:
        """
        @summary 友准达-创建知识库
        
        @param request: CreateKnowLedgeRequest
        @return: CreateKnowLedgeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_know_ledge_with_options(request, headers, runtime)

    async def create_know_ledge_async(
        self,
        request: umeng_finplus_20220913_models.CreateKnowLedgeRequest,
    ) -> umeng_finplus_20220913_models.CreateKnowLedgeResponse:
        """
        @summary 友准达-创建知识库
        
        @param request: CreateKnowLedgeRequest
        @return: CreateKnowLedgeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_know_ledge_with_options_async(request, headers, runtime)

    def encrypt_invoke_with_options(
        self,
        request: umeng_finplus_20220913_models.EncryptInvokeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.EncryptInvokeResponse:
        """
        @summary 加密调用OpenAPI
        
        @param request: EncryptInvokeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptInvokeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.encrypt_key):
            body['encryptKey'] = request.encrypt_key
        if not UtilClient.is_unset(request.method_name):
            body['methodName'] = request.method_name
        if not UtilClient.is_unset(request.sign):
            body['sign'] = request.sign
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EncryptInvoke',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/encryptInvoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.EncryptInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_invoke_with_options_async(
        self,
        request: umeng_finplus_20220913_models.EncryptInvokeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.EncryptInvokeResponse:
        """
        @summary 加密调用OpenAPI
        
        @param request: EncryptInvokeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptInvokeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.encrypt_key):
            body['encryptKey'] = request.encrypt_key
        if not UtilClient.is_unset(request.method_name):
            body['methodName'] = request.method_name
        if not UtilClient.is_unset(request.sign):
            body['sign'] = request.sign
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EncryptInvoke',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/encryptInvoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.EncryptInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt_invoke(
        self,
        request: umeng_finplus_20220913_models.EncryptInvokeRequest,
    ) -> umeng_finplus_20220913_models.EncryptInvokeResponse:
        """
        @summary 加密调用OpenAPI
        
        @param request: EncryptInvokeRequest
        @return: EncryptInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.encrypt_invoke_with_options(request, headers, runtime)

    async def encrypt_invoke_async(
        self,
        request: umeng_finplus_20220913_models.EncryptInvokeRequest,
    ) -> umeng_finplus_20220913_models.EncryptInvokeResponse:
        """
        @summary 加密调用OpenAPI
        
        @param request: EncryptInvokeRequest
        @return: EncryptInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.encrypt_invoke_with_options_async(request, headers, runtime)

    def get_crowd_dataset_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.GetCrowdDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetCrowdDatasetResponse:
        """
        @summary 获取人群集信息
        
        @param tmp_req: GetCrowdDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCrowdDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetCrowdDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCrowdDataset',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getCrowdDataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetCrowdDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_crowd_dataset_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.GetCrowdDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetCrowdDatasetResponse:
        """
        @summary 获取人群集信息
        
        @param tmp_req: GetCrowdDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCrowdDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetCrowdDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCrowdDataset',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getCrowdDataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetCrowdDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_crowd_dataset(
        self,
        request: umeng_finplus_20220913_models.GetCrowdDatasetRequest,
    ) -> umeng_finplus_20220913_models.GetCrowdDatasetResponse:
        """
        @summary 获取人群集信息
        
        @param request: GetCrowdDatasetRequest
        @return: GetCrowdDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_crowd_dataset_with_options(request, headers, runtime)

    async def get_crowd_dataset_async(
        self,
        request: umeng_finplus_20220913_models.GetCrowdDatasetRequest,
    ) -> umeng_finplus_20220913_models.GetCrowdDatasetResponse:
        """
        @summary 获取人群集信息
        
        @param request: GetCrowdDatasetRequest
        @return: GetCrowdDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_crowd_dataset_with_options_async(request, headers, runtime)

    def get_knowledge_data_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.GetKnowledgeDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetKnowledgeDataResponse:
        """
        @summary  获取知识库数据数据
        
        @param tmp_req: GetKnowledgeDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKnowledgeDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetKnowledgeDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKnowledgeData',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getKnowledgeData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetKnowledgeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_data_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.GetKnowledgeDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetKnowledgeDataResponse:
        """
        @summary  获取知识库数据数据
        
        @param tmp_req: GetKnowledgeDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKnowledgeDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetKnowledgeDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKnowledgeData',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getKnowledgeData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetKnowledgeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_data(
        self,
        request: umeng_finplus_20220913_models.GetKnowledgeDataRequest,
    ) -> umeng_finplus_20220913_models.GetKnowledgeDataResponse:
        """
        @summary  获取知识库数据数据
        
        @param request: GetKnowledgeDataRequest
        @return: GetKnowledgeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_knowledge_data_with_options(request, headers, runtime)

    async def get_knowledge_data_async(
        self,
        request: umeng_finplus_20220913_models.GetKnowledgeDataRequest,
    ) -> umeng_finplus_20220913_models.GetKnowledgeDataResponse:
        """
        @summary  获取知识库数据数据
        
        @param request: GetKnowledgeDataRequest
        @return: GetKnowledgeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_knowledge_data_with_options_async(request, headers, runtime)

    def get_yzd_instance_task_result_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.GetYzdInstanceTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse:
        """
        @summary 获取实例结果
        
        @param tmp_req: GetYzdInstanceTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetYzdInstanceTaskResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetYzdInstanceTaskResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetYzdInstanceTaskResult',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getYzdInstanceTaskResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yzd_instance_task_result_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.GetYzdInstanceTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse:
        """
        @summary 获取实例结果
        
        @param tmp_req: GetYzdInstanceTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetYzdInstanceTaskResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.GetYzdInstanceTaskResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetYzdInstanceTaskResult',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getYzdInstanceTaskResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yzd_instance_task_result(
        self,
        request: umeng_finplus_20220913_models.GetYzdInstanceTaskResultRequest,
    ) -> umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse:
        """
        @summary 获取实例结果
        
        @param request: GetYzdInstanceTaskResultRequest
        @return: GetYzdInstanceTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_yzd_instance_task_result_with_options(request, headers, runtime)

    async def get_yzd_instance_task_result_async(
        self,
        request: umeng_finplus_20220913_models.GetYzdInstanceTaskResultRequest,
    ) -> umeng_finplus_20220913_models.GetYzdInstanceTaskResultResponse:
        """
        @summary 获取实例结果
        
        @param request: GetYzdInstanceTaskResultRequest
        @return: GetYzdInstanceTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_yzd_instance_task_result_with_options_async(request, headers, runtime)

    def get_yzd_sts_akwith_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetYzdStsAKResponse:
        """
        @summary 友准达知识库获取上传OSS数据文件的TOKEN
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetYzdStsAKResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetYzdStsAK',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getYzdStsAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetYzdStsAKResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yzd_sts_akwith_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.GetYzdStsAKResponse:
        """
        @summary 友准达知识库获取上传OSS数据文件的TOKEN
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetYzdStsAKResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetYzdStsAK',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/getYzdStsAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.GetYzdStsAKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yzd_sts_ak(self) -> umeng_finplus_20220913_models.GetYzdStsAKResponse:
        """
        @summary 友准达知识库获取上传OSS数据文件的TOKEN
        
        @return: GetYzdStsAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_yzd_sts_akwith_options(headers, runtime)

    async def get_yzd_sts_ak_async(self) -> umeng_finplus_20220913_models.GetYzdStsAKResponse:
        """
        @summary 友准达知识库获取上传OSS数据文件的TOKEN
        
        @return: GetYzdStsAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_yzd_sts_akwith_options_async(headers, runtime)

    def list_compute_task_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_task_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_task(self) -> umeng_finplus_20220913_models.ListComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @return: ListComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_compute_task_with_options(headers, runtime)

    async def list_compute_task_async(self) -> umeng_finplus_20220913_models.ListComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @return: ListComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_compute_task_with_options_async(headers, runtime)

    def list_compute_task_2with_options(
        self,
        request: umeng_finplus_20220913_models.ListComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: ListComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_task_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.ListComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: ListComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_task_2(
        self,
        request: umeng_finplus_20220913_models.ListComputeTask2Request,
    ) -> umeng_finplus_20220913_models.ListComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: ListComputeTask2Request
        @return: ListComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_compute_task_2with_options(request, headers, runtime)

    async def list_compute_task_2_async(
        self,
        request: umeng_finplus_20220913_models.ListComputeTask2Request,
    ) -> umeng_finplus_20220913_models.ListComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: ListComputeTask2Request
        @return: ListComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_compute_task_2with_options_async(request, headers, runtime)

    def list_data_set_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(self) -> umeng_finplus_20220913_models.ListDataSetResponse:
        """
        @summary 查询单个数据集
        
        @return: ListDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_set_with_options(headers, runtime)

    async def list_data_set_async(self) -> umeng_finplus_20220913_models.ListDataSetResponse:
        """
        @summary 查询单个数据集
        
        @return: ListDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_set_with_options_async(headers, runtime)

    def list_data_set_2with_options(
        self,
        request: umeng_finplus_20220913_models.ListDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: ListDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.page_no):
            body['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.ListDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ListDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: ListDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.page_no):
            body['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/listDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ListDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set_2(
        self,
        request: umeng_finplus_20220913_models.ListDataSet2Request,
    ) -> umeng_finplus_20220913_models.ListDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: ListDataSet2Request
        @return: ListDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_set_2with_options(request, headers, runtime)

    async def list_data_set_2_async(
        self,
        request: umeng_finplus_20220913_models.ListDataSet2Request,
    ) -> umeng_finplus_20220913_models.ListDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: ListDataSet2Request
        @return: ListDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_set_2with_options_async(request, headers, runtime)

    def remove_data_set_with_options(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.RemoveDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataSetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='RemoveDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/removeDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.RemoveDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_set_with_options_async(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.RemoveDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataSetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='RemoveDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/removeDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.RemoveDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_set(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSetRequest,
    ) -> umeng_finplus_20220913_models.RemoveDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSetRequest
        @return: RemoveDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_data_set_with_options(request, headers, runtime)

    async def remove_data_set_async(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSetRequest,
    ) -> umeng_finplus_20220913_models.RemoveDataSetResponse:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSetRequest
        @return: RemoveDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_data_set_with_options_async(request, headers, runtime)

    def remove_data_set_2with_options(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.RemoveDataSet2Response:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/removeDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.RemoveDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_set_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.RemoveDataSet2Response:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/removeDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.RemoveDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_set_2(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSet2Request,
    ) -> umeng_finplus_20220913_models.RemoveDataSet2Response:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSet2Request
        @return: RemoveDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_data_set_2with_options(request, headers, runtime)

    async def remove_data_set_2_async(
        self,
        request: umeng_finplus_20220913_models.RemoveDataSet2Request,
    ) -> umeng_finplus_20220913_models.RemoveDataSet2Response:
        """
        @summary 删除数据集
        
        @param request: RemoveDataSet2Request
        @return: RemoveDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_data_set_2with_options_async(request, headers, runtime)

    def save_crowd_dataset_and_binding_dataset_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse:
        """
        @summary 创建人群集并绑定数据集
        
        @param tmp_req: SaveCrowdDatasetAndBindingDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCrowdDatasetAndBindingDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCrowdDatasetAndBindingDataset',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/saveCrowdDatasetAndBindingDataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_crowd_dataset_and_binding_dataset_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse:
        """
        @summary 创建人群集并绑定数据集
        
        @param tmp_req: SaveCrowdDatasetAndBindingDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCrowdDatasetAndBindingDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCrowdDatasetAndBindingDataset',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/saveCrowdDatasetAndBindingDataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_crowd_dataset_and_binding_dataset(
        self,
        request: umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetRequest,
    ) -> umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse:
        """
        @summary 创建人群集并绑定数据集
        
        @param request: SaveCrowdDatasetAndBindingDatasetRequest
        @return: SaveCrowdDatasetAndBindingDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_crowd_dataset_and_binding_dataset_with_options(request, headers, runtime)

    async def save_crowd_dataset_and_binding_dataset_async(
        self,
        request: umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetRequest,
    ) -> umeng_finplus_20220913_models.SaveCrowdDatasetAndBindingDatasetResponse:
        """
        @summary 创建人群集并绑定数据集
        
        @param request: SaveCrowdDatasetAndBindingDatasetRequest
        @return: SaveCrowdDatasetAndBindingDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_crowd_dataset_and_binding_dataset_with_options_async(request, headers, runtime)

    def select_compute_task_with_options(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectComputeTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SelectComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_compute_task_with_options_async(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectComputeTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SelectComputeTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectComputeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_compute_task(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTaskRequest,
    ) -> umeng_finplus_20220913_models.SelectComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTaskRequest
        @return: SelectComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_compute_task_with_options(request, headers, runtime)

    async def select_compute_task_async(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTaskRequest,
    ) -> umeng_finplus_20220913_models.SelectComputeTaskResponse:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTaskRequest
        @return: SelectComputeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_compute_task_with_options_async(request, headers, runtime)

    def select_compute_task_2with_options(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bc_confirm):
            body['bcConfirm'] = request.bc_confirm
        if not UtilClient.is_unset(request.bc_id):
            body['bcId'] = request.bc_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SelectComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectComputeTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def select_compute_task_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectComputeTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bc_confirm):
            body['bcConfirm'] = request.bc_confirm
        if not UtilClient.is_unset(request.bc_id):
            body['bcId'] = request.bc_id
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SelectComputeTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectComputeTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectComputeTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def select_compute_task_2(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTask2Request,
    ) -> umeng_finplus_20220913_models.SelectComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTask2Request
        @return: SelectComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_compute_task_2with_options(request, headers, runtime)

    async def select_compute_task_2_async(
        self,
        request: umeng_finplus_20220913_models.SelectComputeTask2Request,
    ) -> umeng_finplus_20220913_models.SelectComputeTask2Response:
        """
        @summary 查询单个批量任务
        
        @param request: SelectComputeTask2Request
        @return: SelectComputeTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_compute_task_2with_options_async(request, headers, runtime)

    def select_data_set_with_options(
        self,
        request: umeng_finplus_20220913_models.SelectDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectDataSetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SelectDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_data_set_with_options_async(
        self,
        request: umeng_finplus_20220913_models.SelectDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectDataSetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SelectDataSet',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectDataSet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_data_set(
        self,
        request: umeng_finplus_20220913_models.SelectDataSetRequest,
    ) -> umeng_finplus_20220913_models.SelectDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSetRequest
        @return: SelectDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_data_set_with_options(request, headers, runtime)

    async def select_data_set_async(
        self,
        request: umeng_finplus_20220913_models.SelectDataSetRequest,
    ) -> umeng_finplus_20220913_models.SelectDataSetResponse:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSetRequest
        @return: SelectDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_data_set_with_options_async(request, headers, runtime)

    def select_data_set_2with_options(
        self,
        request: umeng_finplus_20220913_models.SelectDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SelectDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectDataSet2Response(),
            self.call_api(params, req, runtime)
        )

    async def select_data_set_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.SelectDataSet2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SelectDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSet2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectDataSet2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SelectDataSet2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/selectDataSet2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SelectDataSet2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def select_data_set_2(
        self,
        request: umeng_finplus_20220913_models.SelectDataSet2Request,
    ) -> umeng_finplus_20220913_models.SelectDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSet2Request
        @return: SelectDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_data_set_2with_options(request, headers, runtime)

    async def select_data_set_2_async(
        self,
        request: umeng_finplus_20220913_models.SelectDataSet2Request,
    ) -> umeng_finplus_20220913_models.SelectDataSet2Response:
        """
        @summary 查询单个数据集
        
        @param request: SelectDataSet2Request
        @return: SelectDataSet2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_data_set_2with_options_async(request, headers, runtime)

    def submit_data_set_task_with_options(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTaskResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDataSetTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SubmitDataSetTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/submitDataSetTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SubmitDataSetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_data_set_task_with_options_async(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTaskResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDataSetTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='SubmitDataSetTask',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/submitDataSetTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SubmitDataSetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_data_set_task(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTaskRequest,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTaskResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTaskRequest
        @return: SubmitDataSetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_data_set_task_with_options(request, headers, runtime)

    async def submit_data_set_task_async(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTaskRequest,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTaskResponse:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTaskRequest
        @return: SubmitDataSetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_data_set_task_with_options_async(request, headers, runtime)

    def submit_data_set_task_2with_options(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTask2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDataSetTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDataSetTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/submitDataSetTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SubmitDataSetTask2Response(),
            self.call_api(params, req, runtime)
        )

    async def submit_data_set_task_2with_options_async(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTask2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTask2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTask2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDataSetTask2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.data_set_id):
            body['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDataSetTask2',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/bc/submitDataSetTask2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.SubmitDataSetTask2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_data_set_task_2(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTask2Request,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTask2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTask2Request
        @return: SubmitDataSetTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_data_set_task_2with_options(request, headers, runtime)

    async def submit_data_set_task_2_async(
        self,
        request: umeng_finplus_20220913_models.SubmitDataSetTask2Request,
    ) -> umeng_finplus_20220913_models.SubmitDataSetTask2Response:
        """
        @summary 提交数据集任务，校验数据集
        
        @param request: SubmitDataSetTask2Request
        @return: SubmitDataSetTask2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_data_set_task_2with_options_async(request, headers, runtime)

    def validate_know_ledge_with_options(
        self,
        tmp_req: umeng_finplus_20220913_models.ValidateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ValidateKnowLedgeResponse:
        """
        @summary 提交知识库校验任务
        
        @param tmp_req: ValidateKnowLedgeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateKnowLedgeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.ValidateKnowLedgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'simple')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateKnowLedge',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/validateKnowLedge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ValidateKnowLedgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_know_ledge_with_options_async(
        self,
        tmp_req: umeng_finplus_20220913_models.ValidateKnowLedgeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20220913_models.ValidateKnowLedgeResponse:
        """
        @summary 提交知识库校验任务
        
        @param tmp_req: ValidateKnowLedgeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateKnowLedgeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_finplus_20220913_models.ValidateKnowLedgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'simple')
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateKnowLedge',
            version='2022-09-13',
            protocol='HTTPS',
            pathname=f'/yzd/validateKnowLedge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20220913_models.ValidateKnowLedgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_know_ledge(
        self,
        request: umeng_finplus_20220913_models.ValidateKnowLedgeRequest,
    ) -> umeng_finplus_20220913_models.ValidateKnowLedgeResponse:
        """
        @summary 提交知识库校验任务
        
        @param request: ValidateKnowLedgeRequest
        @return: ValidateKnowLedgeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_know_ledge_with_options(request, headers, runtime)

    async def validate_know_ledge_async(
        self,
        request: umeng_finplus_20220913_models.ValidateKnowLedgeRequest,
    ) -> umeng_finplus_20220913_models.ValidateKnowLedgeResponse:
        """
        @summary 提交知识库校验任务
        
        @param request: ValidateKnowLedgeRequest
        @return: ValidateKnowLedgeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_know_ledge_with_options_async(request, headers, runtime)
