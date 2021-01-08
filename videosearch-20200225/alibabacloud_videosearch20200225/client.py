# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_videosearch20200225 import models as videosearch_20200225_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'multisearch.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'multisearch.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('videosearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def create_batch_task_with_options(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.CreateBatchTaskResponse().from_map(
            self.do_request('CreateBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_batch_task_with_options_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.CreateBatchTaskResponse().from_map(
            await self.do_request_async('CreateBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_storage_history_with_options(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetStorageHistoryResponse().from_map(
            self.do_request('GetStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_storage_history_with_options_async(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetStorageHistoryResponse().from_map(
            await self.do_request_async('GetStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_batch_task_with_options(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListBatchTaskResponse().from_map(
            self.do_request('ListBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_batch_task_with_options_async(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListBatchTaskResponse().from_map(
            await self.do_request_async('ListBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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
        return videosearch_20200225_models.ListInstancesResponse().from_map(
            self.do_request('ListInstances', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListInstancesResponse().from_map(
            await self.do_request_async('ListInstances', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_storage_video_tasks_with_options(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListStorageVideoTasksResponse().from_map(
            self.do_request('ListStorageVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_storage_video_tasks_with_options_async(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListStorageVideoTasksResponse().from_map(
            await self.do_request_async('ListStorageVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_search_video_tasks_with_options(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListSearchVideoTasksResponse().from_map(
            self.do_request('ListSearchVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_search_video_tasks_with_options_async(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.ListSearchVideoTasksResponse().from_map(
            await self.do_request_async('ListSearchVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def add_storage_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddStorageVideoTaskResponse().from_map(
            self.do_request('AddStorageVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_storage_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddStorageVideoTaskResponse().from_map(
            await self.do_request_async('AddStorageVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_instance_with_options(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetInstanceResponse().from_map(
            self.do_request('GetInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetInstanceResponse().from_map(
            await self.do_request_async('GetInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def add_deletion_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddDeletionVideoTaskResponse().from_map(
            self.do_request('AddDeletionVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_deletion_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddDeletionVideoTaskResponse().from_map(
            await self.do_request_async('AddDeletionVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_task_status_with_options(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetTaskStatusResponse().from_map(
            self.do_request('GetTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetTaskStatusResponse().from_map(
            await self.do_request_async('GetTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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

    def add_search_video_task_with_options(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddSearchVideoTaskResponse().from_map(
            self.do_request('AddSearchVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_search_video_task_with_options_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddSearchVideoTaskResponse().from_map(
            await self.do_request_async('AddSearchVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
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
