# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_videosearch20200225 import models as videosearch_20200225_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'multisearch.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'multisearch.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('videosearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_deletion_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDeletionVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_deletion_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddDeletionVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_deletion_video_task(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_deletion_video_task_with_options(request, runtime)

    async def add_deletion_video_task_async(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_deletion_video_task_with_options_async(request, runtime)

    def add_search_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddSearchVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_search_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddSearchVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_search_video_task(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_search_video_task_with_options(request, runtime)

    async def add_search_video_task_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_search_video_task_with_options_async(request, runtime)

    def add_storage_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddStorageVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_storage_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddStorageVideoTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_storage_video_task(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_storage_video_task_with_options(request, runtime)

    async def add_storage_video_task_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_storage_video_task_with_options_async(request, runtime)

    def create_batch_task_with_options(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBatchTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.CreateBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_task_with_options_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBatchTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.CreateBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_task(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_batch_task_with_options(request, runtime)

    async def create_batch_task_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_task_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_storage_history_with_options(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['InstanceId'] = request.instance_id
        query['VideoId'] = request.video_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetStorageHistory',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetStorageHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_history_with_options_async(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['InstanceId'] = request.instance_id
        query['VideoId'] = request.video_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetStorageHistory',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetStorageHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_history(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_storage_history_with_options(request, runtime)

    async def get_storage_history_async(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_storage_history_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def list_batch_task_with_options(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ClientToken'] = request.client_token
        query['BatchTaskType'] = request.batch_task_type
        query['Status'] = request.status
        query['InstanceId'] = request.instance_id
        query['BucketName'] = request.bucket_name
        query['DataPath'] = request.data_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBatchTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batch_task_with_options_async(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ClientToken'] = request.client_token
        query['BatchTaskType'] = request.batch_task_type
        query['Status'] = request.status
        query['InstanceId'] = request.instance_id
        query['BucketName'] = request.bucket_name
        query['DataPath'] = request.data_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBatchTask',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batch_task(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_batch_task_with_options(request, runtime)

    async def list_batch_task_async(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_batch_task_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_search_video_tasks_with_options(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSearchVideoTasks',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchVideoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_video_tasks_with_options_async(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSearchVideoTasks',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchVideoTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_video_tasks(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_search_video_tasks_with_options(request, runtime)

    async def list_search_video_tasks_async(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_search_video_tasks_with_options_async(request, runtime)

    def list_storage_video_tasks_with_options(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListStorageVideoTasks',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageVideoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_video_tasks_with_options_async(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListStorageVideoTasks',
            version='2020-02-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageVideoTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_video_tasks(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_storage_video_tasks_with_options(request, runtime)

    async def list_storage_video_tasks_async(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_storage_video_tasks_with_options_async(request, runtime)
