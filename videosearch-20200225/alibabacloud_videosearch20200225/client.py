# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_videosearch20200225 import models as videosearch_20200225_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
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

    def add_deletion_audio_task(
        self,
        request: videosearch_20200225_models.AddDeletionAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionAudioTaskResponse(),
            self.do_request('AddDeletionAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_deletion_audio_task_async(
        self,
        request: videosearch_20200225_models.AddDeletionAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionAudioTaskResponse(),
            await self.do_request_async('AddDeletionAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_deletion_audio_task_simply(
        self,
        request: videosearch_20200225_models.AddDeletionAudioTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_deletion_audio_task(request, runtime)

    async def add_deletion_audio_task_simply_async(
        self,
        request: videosearch_20200225_models.AddDeletionAudioTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_deletion_audio_task_async(request, runtime)

    def get_audio_task_status(
        self,
        request: videosearch_20200225_models.GetAudioTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioTaskStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioTaskStatusResponse(),
            self.do_request('GetAudioTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_audio_task_status_async(
        self,
        request: videosearch_20200225_models.GetAudioTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioTaskStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioTaskStatusResponse(),
            await self.do_request_async('GetAudioTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_audio_task_status_simply(
        self,
        request: videosearch_20200225_models.GetAudioTaskStatusRequest,
    ) -> videosearch_20200225_models.GetAudioTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_task_status(request, runtime)

    async def get_audio_task_status_simply_async(
        self,
        request: videosearch_20200225_models.GetAudioTaskStatusRequest,
    ) -> videosearch_20200225_models.GetAudioTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_task_status_async(request, runtime)

    def cancel_batch_task(
        self,
        request: videosearch_20200225_models.CancelBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CancelBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.CancelBatchTaskResponse(),
            self.do_request('CancelBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_batch_task_async(
        self,
        request: videosearch_20200225_models.CancelBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CancelBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.CancelBatchTaskResponse(),
            await self.do_request_async('CancelBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_batch_task_simply(
        self,
        request: videosearch_20200225_models.CancelBatchTaskRequest,
    ) -> videosearch_20200225_models.CancelBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_batch_task(request, runtime)

    async def cancel_batch_task_simply_async(
        self,
        request: videosearch_20200225_models.CancelBatchTaskRequest,
    ) -> videosearch_20200225_models.CancelBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_batch_task_async(request, runtime)

    def get_audio_storage_history(
        self,
        request: videosearch_20200225_models.GetAudioStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioStorageHistoryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioStorageHistoryResponse(),
            self.do_request('GetAudioStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_audio_storage_history_async(
        self,
        request: videosearch_20200225_models.GetAudioStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioStorageHistoryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioStorageHistoryResponse(),
            await self.do_request_async('GetAudioStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_audio_storage_history_simply(
        self,
        request: videosearch_20200225_models.GetAudioStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetAudioStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_storage_history(request, runtime)

    async def get_audio_storage_history_simply_async(
        self,
        request: videosearch_20200225_models.GetAudioStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetAudioStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_storage_history_async(request, runtime)

    def modify_priority(
        self,
        request: videosearch_20200225_models.ModifyPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ModifyPriorityResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ModifyPriorityResponse(),
            self.do_request('ModifyPriority', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_priority_async(
        self,
        request: videosearch_20200225_models.ModifyPriorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ModifyPriorityResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ModifyPriorityResponse(),
            await self.do_request_async('ModifyPriority', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_priority_simply(
        self,
        request: videosearch_20200225_models.ModifyPriorityRequest,
    ) -> videosearch_20200225_models.ModifyPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_priority(request, runtime)

    async def modify_priority_simply_async(
        self,
        request: videosearch_20200225_models.ModifyPriorityRequest,
    ) -> videosearch_20200225_models.ModifyPriorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_priority_async(request, runtime)

    def get_audio_instance(
        self,
        request: videosearch_20200225_models.GetAudioInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioInstanceResponse(),
            self.do_request('GetAudioInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_audio_instance_async(
        self,
        request: videosearch_20200225_models.GetAudioInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetAudioInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetAudioInstanceResponse(),
            await self.do_request_async('GetAudioInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_audio_instance_simply(
        self,
        request: videosearch_20200225_models.GetAudioInstanceRequest,
    ) -> videosearch_20200225_models.GetAudioInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_instance(request, runtime)

    async def get_audio_instance_simply_async(
        self,
        request: videosearch_20200225_models.GetAudioInstanceRequest,
    ) -> videosearch_20200225_models.GetAudioInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_instance_async(request, runtime)

    def get_batch_task(
        self,
        request: videosearch_20200225_models.GetBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetBatchTaskResponse(),
            self.do_request('GetBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_batch_task_async(
        self,
        request: videosearch_20200225_models.GetBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetBatchTaskResponse(),
            await self.do_request_async('GetBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_batch_task_simply(
        self,
        request: videosearch_20200225_models.GetBatchTaskRequest,
    ) -> videosearch_20200225_models.GetBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task(request, runtime)

    async def get_batch_task_simply_async(
        self,
        request: videosearch_20200225_models.GetBatchTaskRequest,
    ) -> videosearch_20200225_models.GetBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_async(request, runtime)

    def add_search_audio_task(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchAudioTaskResponse(),
            self.do_request('AddSearchAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_search_audio_task_async(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchAudioTaskResponse(),
            await self.do_request_async('AddSearchAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_search_audio_task_simply(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskRequest,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_search_audio_task(request, runtime)

    async def add_search_audio_task_simply_async(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskRequest,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_search_audio_task_async(request, runtime)

    def add_search_audio_task_advance(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_search_audio_task_req = videosearch_20200225_models.AddSearchAudioTaskRequest()
        RPCUtilClient.convert(request, add_search_audio_task_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.audio_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_search_audio_task_req.audio_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_search_audio_task_resp = self.add_search_audio_task(add_search_audio_task_req, runtime)
        return add_search_audio_task_resp

    async def add_search_audio_task_advance_async(
        self,
        request: videosearch_20200225_models.AddSearchAudioTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchAudioTaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_search_audio_task_req = videosearch_20200225_models.AddSearchAudioTaskRequest()
        RPCUtilClient.convert(request, add_search_audio_task_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.audio_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        add_search_audio_task_req.audio_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_search_audio_task_resp = await self.add_search_audio_task_async(add_search_audio_task_req, runtime)
        return add_search_audio_task_resp

    def add_storage_audio_task(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageAudioTaskResponse(),
            self.do_request('AddStorageAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_storage_audio_task_async(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageAudioTaskResponse(),
            await self.do_request_async('AddStorageAudioTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_storage_audio_task_simply(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskRequest,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_storage_audio_task(request, runtime)

    async def add_storage_audio_task_simply_async(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskRequest,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_storage_audio_task_async(request, runtime)

    def add_storage_audio_task_advance(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_storage_audio_task_req = videosearch_20200225_models.AddStorageAudioTaskRequest()
        RPCUtilClient.convert(request, add_storage_audio_task_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.audio_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_storage_audio_task_req.audio_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_storage_audio_task_resp = self.add_storage_audio_task(add_storage_audio_task_req, runtime)
        return add_storage_audio_task_resp

    async def add_storage_audio_task_advance_async(
        self,
        request: videosearch_20200225_models.AddStorageAudioTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageAudioTaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_storage_audio_task_req = videosearch_20200225_models.AddStorageAudioTaskRequest()
        RPCUtilClient.convert(request, add_storage_audio_task_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.audio_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        add_storage_audio_task_req.audio_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_storage_audio_task_resp = await self.add_storage_audio_task_async(add_storage_audio_task_req, runtime)
        return add_storage_audio_task_resp

    def list_storage_audio_tasks(
        self,
        request: videosearch_20200225_models.ListStorageAudioTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageAudioTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageAudioTasksResponse(),
            self.do_request('ListStorageAudioTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_storage_audio_tasks_async(
        self,
        request: videosearch_20200225_models.ListStorageAudioTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageAudioTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageAudioTasksResponse(),
            await self.do_request_async('ListStorageAudioTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_storage_audio_tasks_simply(
        self,
        request: videosearch_20200225_models.ListStorageAudioTasksRequest,
    ) -> videosearch_20200225_models.ListStorageAudioTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_storage_audio_tasks(request, runtime)

    async def list_storage_audio_tasks_simply_async(
        self,
        request: videosearch_20200225_models.ListStorageAudioTasksRequest,
    ) -> videosearch_20200225_models.ListStorageAudioTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_storage_audio_tasks_async(request, runtime)

    def list_search_audio_tasks(
        self,
        request: videosearch_20200225_models.ListSearchAudioTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchAudioTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchAudioTasksResponse(),
            self.do_request('ListSearchAudioTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_search_audio_tasks_async(
        self,
        request: videosearch_20200225_models.ListSearchAudioTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchAudioTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchAudioTasksResponse(),
            await self.do_request_async('ListSearchAudioTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_search_audio_tasks_simply(
        self,
        request: videosearch_20200225_models.ListSearchAudioTasksRequest,
    ) -> videosearch_20200225_models.ListSearchAudioTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_search_audio_tasks(request, runtime)

    async def list_search_audio_tasks_simply_async(
        self,
        request: videosearch_20200225_models.ListSearchAudioTasksRequest,
    ) -> videosearch_20200225_models.ListSearchAudioTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_search_audio_tasks_async(request, runtime)

    def create_batch_task(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.CreateBatchTaskResponse(),
            self.do_request('CreateBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_batch_task_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.CreateBatchTaskResponse(),
            await self.do_request_async('CreateBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_batch_task_simply(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_batch_task(request, runtime)

    async def create_batch_task_simply_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskRequest,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_task_async(request, runtime)

    def create_batch_task_advance(
        self,
        request: videosearch_20200225_models.CreateBatchTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        create_batch_task_req = videosearch_20200225_models.CreateBatchTaskRequest()
        RPCUtilClient.convert(request, create_batch_task_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.file_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        create_batch_task_req.file_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        create_batch_task_resp = self.create_batch_task(create_batch_task_req, runtime)
        return create_batch_task_resp

    async def create_batch_task_advance_async(
        self,
        request: videosearch_20200225_models.CreateBatchTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.CreateBatchTaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        create_batch_task_req = videosearch_20200225_models.CreateBatchTaskRequest()
        RPCUtilClient.convert(request, create_batch_task_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.file_url_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        create_batch_task_req.file_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        create_batch_task_resp = await self.create_batch_task_async(create_batch_task_req, runtime)
        return create_batch_task_resp

    def get_storage_history(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetStorageHistoryResponse(),
            self.do_request('GetStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_storage_history_async(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetStorageHistoryResponse(),
            await self.do_request_async('GetStorageHistory', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_storage_history_simply(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_storage_history(request, runtime)

    async def get_storage_history_simply_async(
        self,
        request: videosearch_20200225_models.GetStorageHistoryRequest,
    ) -> videosearch_20200225_models.GetStorageHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_storage_history_async(request, runtime)

    def list_batch_task(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListBatchTaskResponse(),
            self.do_request('ListBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_batch_task_async(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListBatchTaskResponse(),
            await self.do_request_async('ListBatchTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_batch_task_simply(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_batch_task(request, runtime)

    async def list_batch_task_simply_async(
        self,
        request: videosearch_20200225_models.ListBatchTaskRequest,
    ) -> videosearch_20200225_models.ListBatchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_batch_task_async(request, runtime)

    def list_instances(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListInstancesResponse(),
            self.do_request('ListInstances', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_instances_async(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListInstancesResponse(),
            await self.do_request_async('ListInstances', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_instances_simply(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances(request, runtime)

    async def list_instances_simply_async(
        self,
        request: videosearch_20200225_models.ListInstancesRequest,
    ) -> videosearch_20200225_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_async(request, runtime)

    def list_storage_video_tasks(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageVideoTasksResponse(),
            self.do_request('ListStorageVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_storage_video_tasks_async(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListStorageVideoTasksResponse(),
            await self.do_request_async('ListStorageVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_storage_video_tasks_simply(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_storage_video_tasks(request, runtime)

    async def list_storage_video_tasks_simply_async(
        self,
        request: videosearch_20200225_models.ListStorageVideoTasksRequest,
    ) -> videosearch_20200225_models.ListStorageVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_storage_video_tasks_async(request, runtime)

    def list_search_video_tasks(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchVideoTasksResponse(),
            self.do_request('ListSearchVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_search_video_tasks_async(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.ListSearchVideoTasksResponse(),
            await self.do_request_async('ListSearchVideoTasks', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_search_video_tasks_simply(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_search_video_tasks(request, runtime)

    async def list_search_video_tasks_simply_async(
        self,
        request: videosearch_20200225_models.ListSearchVideoTasksRequest,
    ) -> videosearch_20200225_models.ListSearchVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_search_video_tasks_async(request, runtime)

    def add_storage_video_task(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageVideoTaskResponse(),
            self.do_request('AddStorageVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_storage_video_task_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddStorageVideoTaskResponse(),
            await self.do_request_async('AddStorageVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_storage_video_task_simply(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_storage_video_task(request, runtime)

    async def add_storage_video_task_simply_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskRequest,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_storage_video_task_async(request, runtime)

    def add_storage_video_task_advance(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_storage_video_task_req = videosearch_20200225_models.AddStorageVideoTaskRequest()
        RPCUtilClient.convert(request, add_storage_video_task_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_storage_video_task_req.video_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_storage_video_task_resp = self.add_storage_video_task(add_storage_video_task_req, runtime)
        return add_storage_video_task_resp

    async def add_storage_video_task_advance_async(
        self,
        request: videosearch_20200225_models.AddStorageVideoTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddStorageVideoTaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_storage_video_task_req = videosearch_20200225_models.AddStorageVideoTaskRequest()
        RPCUtilClient.convert(request, add_storage_video_task_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        add_storage_video_task_req.video_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_storage_video_task_resp = await self.add_storage_video_task_async(add_storage_video_task_req, runtime)
        return add_storage_video_task_resp

    def get_instance(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetInstanceResponse(),
            self.do_request('GetInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_instance_async(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetInstanceResponse(),
            await self.do_request_async('GetInstance', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_instance_simply(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance(request, runtime)

    async def get_instance_simply_async(
        self,
        request: videosearch_20200225_models.GetInstanceRequest,
    ) -> videosearch_20200225_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_async(request, runtime)

    def add_deletion_video_task(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionVideoTaskResponse(),
            self.do_request('AddDeletionVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_deletion_video_task_async(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddDeletionVideoTaskResponse(),
            await self.do_request_async('AddDeletionVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_deletion_video_task_simply(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_deletion_video_task(request, runtime)

    async def add_deletion_video_task_simply_async(
        self,
        request: videosearch_20200225_models.AddDeletionVideoTaskRequest,
    ) -> videosearch_20200225_models.AddDeletionVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_deletion_video_task_async(request, runtime)

    def get_task_status(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetTaskStatusResponse(),
            self.do_request('GetTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_task_status_async(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.GetTaskStatusResponse(),
            await self.do_request_async('GetTaskStatus', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_task_status_simply(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status(request, runtime)

    async def get_task_status_simply_async(
        self,
        request: videosearch_20200225_models.GetTaskStatusRequest,
    ) -> videosearch_20200225_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_async(request, runtime)

    def add_search_video_task(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchVideoTaskResponse(),
            self.do_request('AddSearchVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_search_video_task_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            videosearch_20200225_models.AddSearchVideoTaskResponse(),
            await self.do_request_async('AddSearchVideoTask', 'HTTPS', 'POST', '2020-02-25', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_search_video_task_simply(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_search_video_task(request, runtime)

    async def add_search_video_task_simply_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskRequest,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_search_video_task_async(request, runtime)

    def add_search_video_task_advance(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_search_video_task_req = videosearch_20200225_models.AddSearchVideoTaskRequest()
        RPCUtilClient.convert(request, add_search_video_task_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_search_video_task_req.video_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_search_video_task_resp = self.add_search_video_task(add_search_video_task_req, runtime)
        return add_search_video_task_resp

    async def add_search_video_task_advance_async(
        self,
        request: videosearch_20200225_models.AddSearchVideoTaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> videosearch_20200225_models.AddSearchVideoTaskResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='videosearch',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_search_video_task_req = videosearch_20200225_models.AddSearchVideoTaskRequest()
        RPCUtilClient.convert(request, add_search_video_task_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_file_object,
            content_type=''
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status='201'
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        await oss_client.post_object_async(upload_request, oss_runtime)
        add_search_video_task_req.video_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        add_search_video_task_resp = await self.add_search_video_task_async(add_search_video_task_req, runtime)
        return add_search_video_task_resp

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
