# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_image_detect20211221 import models as image_detect_20211221_models
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
        self._endpoint = self.get_endpoint('image-detect', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_task_with_options(
        self,
        request: image_detect_20211221_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
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
            image_detect_20211221_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: image_detect_20211221_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
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
            image_detect_20211221_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: image_detect_20211221_models.CancelTaskRequest,
    ) -> image_detect_20211221_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: image_detect_20211221_models.CancelTaskRequest,
    ) -> image_detect_20211221_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def create_task_with_options(
        self,
        request: image_detect_20211221_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_config_name):
            query['OssConfigName'] = request.oss_config_name
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_input_path):
            query['OssInputPath'] = request.oss_input_path
        if not UtilClient.is_unset(request.oss_output_path):
            query['OssOutputPath'] = request.oss_output_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.task_description):
            query['TaskDescription'] = request.task_description
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
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
            image_detect_20211221_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: image_detect_20211221_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_config_name):
            query['OssConfigName'] = request.oss_config_name
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_input_path):
            query['OssInputPath'] = request.oss_input_path
        if not UtilClient.is_unset(request.oss_output_path):
            query['OssOutputPath'] = request.oss_output_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.task_description):
            query['TaskDescription'] = request.task_description
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
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
            image_detect_20211221_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: image_detect_20211221_models.CreateTaskRequest,
    ) -> image_detect_20211221_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    async def create_task_async(
        self,
        request: image_detect_20211221_models.CreateTaskRequest,
    ) -> image_detect_20211221_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_task_with_options_async(request, runtime)

    def delete_oss_config_with_options(
        self,
        request: image_detect_20211221_models.DeleteOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.DeleteOssConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOssConfig',
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
            image_detect_20211221_models.DeleteOssConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oss_config_with_options_async(
        self,
        request: image_detect_20211221_models.DeleteOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.DeleteOssConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOssConfig',
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
            image_detect_20211221_models.DeleteOssConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oss_config(
        self,
        request: image_detect_20211221_models.DeleteOssConfigRequest,
    ) -> image_detect_20211221_models.DeleteOssConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_oss_config_with_options(request, runtime)

    async def delete_oss_config_async(
        self,
        request: image_detect_20211221_models.DeleteOssConfigRequest,
    ) -> image_detect_20211221_models.DeleteOssConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_oss_config_with_options_async(request, runtime)

    def detect_image_with_options(
        self,
        request: image_detect_20211221_models.DetectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.DetectImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImage',
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
            image_detect_20211221_models.DetectImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_with_options_async(
        self,
        request: image_detect_20211221_models.DetectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.DetectImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImage',
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
            image_detect_20211221_models.DetectImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image(
        self,
        request: image_detect_20211221_models.DetectImageRequest,
    ) -> image_detect_20211221_models.DetectImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_with_options(request, runtime)

    async def detect_image_async(
        self,
        request: image_detect_20211221_models.DetectImageRequest,
    ) -> image_detect_20211221_models.DetectImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_with_options_async(request, runtime)

    def get_oss_config_list_with_options(
        self,
        request: image_detect_20211221_models.GetOssConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetOssConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssConfigList',
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
            image_detect_20211221_models.GetOssConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_config_list_with_options_async(
        self,
        request: image_detect_20211221_models.GetOssConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetOssConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssConfigList',
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
            image_detect_20211221_models.GetOssConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_config_list(
        self,
        request: image_detect_20211221_models.GetOssConfigListRequest,
    ) -> image_detect_20211221_models.GetOssConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_config_list_with_options(request, runtime)

    async def get_oss_config_list_async(
        self,
        request: image_detect_20211221_models.GetOssConfigListRequest,
    ) -> image_detect_20211221_models.GetOssConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_config_list_with_options_async(request, runtime)

    def get_task_detail_with_options(
        self,
        request: image_detect_20211221_models.GetTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskDetail',
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
            image_detect_20211221_models.GetTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_detail_with_options_async(
        self,
        request: image_detect_20211221_models.GetTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskDetail',
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
            image_detect_20211221_models.GetTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_detail(
        self,
        request: image_detect_20211221_models.GetTaskDetailRequest,
    ) -> image_detect_20211221_models.GetTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_detail_with_options(request, runtime)

    async def get_task_detail_async(
        self,
        request: image_detect_20211221_models.GetTaskDetailRequest,
    ) -> image_detect_20211221_models.GetTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_detail_with_options_async(request, runtime)

    def get_task_list_with_options(
        self,
        request: image_detect_20211221_models.GetTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskList',
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
            image_detect_20211221_models.GetTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_list_with_options_async(
        self,
        request: image_detect_20211221_models.GetTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.GetTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskList',
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
            image_detect_20211221_models.GetTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_list(
        self,
        request: image_detect_20211221_models.GetTaskListRequest,
    ) -> image_detect_20211221_models.GetTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_list_with_options(request, runtime)

    async def get_task_list_async(
        self,
        request: image_detect_20211221_models.GetTaskListRequest,
    ) -> image_detect_20211221_models.GetTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_list_with_options_async(request, runtime)

    def save_oss_config_with_options(
        self,
        request: image_detect_20211221_models.SaveOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.SaveOssConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not UtilClient.is_unset(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveOssConfig',
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
            image_detect_20211221_models.SaveOssConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_oss_config_with_options_async(
        self,
        request: image_detect_20211221_models.SaveOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.SaveOssConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not UtilClient.is_unset(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveOssConfig',
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
            image_detect_20211221_models.SaveOssConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_oss_config(
        self,
        request: image_detect_20211221_models.SaveOssConfigRequest,
    ) -> image_detect_20211221_models.SaveOssConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_oss_config_with_options(request, runtime)

    async def save_oss_config_async(
        self,
        request: image_detect_20211221_models.SaveOssConfigRequest,
    ) -> image_detect_20211221_models.SaveOssConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_oss_config_with_options_async(request, runtime)

    def update_task_priority_with_options(
        self,
        request: image_detect_20211221_models.UpdateTaskPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.UpdateTaskPriorityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskPriority',
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
            image_detect_20211221_models.UpdateTaskPriorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_priority_with_options_async(
        self,
        request: image_detect_20211221_models.UpdateTaskPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_detect_20211221_models.UpdateTaskPriorityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskPriority',
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
            image_detect_20211221_models.UpdateTaskPriorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_priority(
        self,
        request: image_detect_20211221_models.UpdateTaskPriorityRequest,
    ) -> image_detect_20211221_models.UpdateTaskPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_task_priority_with_options(request, runtime)

    async def update_task_priority_async(
        self,
        request: image_detect_20211221_models.UpdateTaskPriorityRequest,
    ) -> image_detect_20211221_models.UpdateTaskPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_task_priority_with_options_async(request, runtime)
