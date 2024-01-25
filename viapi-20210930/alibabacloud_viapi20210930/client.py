# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_viapi20210930 import models as viapi_20210930_models
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
        self._endpoint = self.get_endpoint('viapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)

    def create_ai_store_bucket_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreBucket',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_store_bucket_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreBucket',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_store_bucket(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_bucket_with_options(request, runtime)

    async def create_ai_store_bucket_async(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_store_bucket_with_options_async(request, runtime)

    def create_ai_store_receive_config_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreReceiveConfig',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreReceiveConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_store_receive_config_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreReceiveConfig',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreReceiveConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_store_receive_config(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_receive_config_with_options(request, runtime)

    async def create_ai_store_receive_config_async(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_store_receive_config_with_options_async(request, runtime)

    def create_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_key_prefix):
            body['BucketKeyPrefix'] = request.bucket_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.create_config):
            body['CreateConfig'] = request.create_config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.param_info):
            body['ParamInfo'] = request.param_info
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.receive_config):
            body['ReceiveConfig'] = request.receive_config
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_key_prefix):
            body['BucketKeyPrefix'] = request.bucket_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.create_config):
            body['CreateConfig'] = request.create_config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.param_info):
            body['ParamInfo'] = request.param_info
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.receive_config):
            body['ReceiveConfig'] = request.receive_config
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_store_user_task(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_user_task_with_options(request, runtime)

    async def create_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ai_store_user_task_with_options_async(request, runtime)

    def delete_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.DeleteAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.DeleteAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ai_store_user_task(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ai_store_user_task_with_options(request, runtime)

    async def delete_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ai_store_user_task_with_options_async(request, runtime)

    def disable_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.DisableAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.DisableAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_ai_store_user_task(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_ai_store_user_task_with_options(request, runtime)

    async def disable_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_ai_store_user_task_with_options_async(request, runtime)

    def enable_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.EnableAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aistore_version):
            body['AistoreVersion'] = request.aistore_version
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.EnableAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_ai_store_user_task(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_ai_store_user_task_with_options(request, runtime)

    async def enable_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_ai_store_user_task_with_options_async(request, runtime)

    def get_ai_store_receive_config_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreReceiveConfig',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreReceiveConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_store_receive_config_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreReceiveConfig',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreReceiveConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_store_receive_config(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_receive_config_with_options(request, runtime)

    async def get_ai_store_receive_config_async(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_store_receive_config_with_options_async(request, runtime)

    def get_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_store_user_task(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_user_task_with_options(request, runtime)

    async def get_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_store_user_task_with_options_async(request, runtime)

    def get_ai_store_user_task_by_name_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreUserTaskByName',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_store_user_task_by_name_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAiStoreUserTaskByName',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_store_user_task_by_name(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_user_task_by_name_with_options(request, runtime)

    async def get_ai_store_user_task_by_name_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ai_store_user_task_by_name_with_options_async(request, runtime)

    def list_ai_store_buckets_with_options(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAiStoreBuckets',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.ListAiStoreBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ai_store_buckets_with_options_async(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAiStoreBuckets',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.ListAiStoreBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ai_store_buckets(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ai_store_buckets_with_options(request, runtime)

    async def list_ai_store_buckets_async(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ai_store_buckets_with_options_async(request, runtime)

    def query_ai_store_api_tree_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAiStoreApiTree',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreApiTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_store_api_tree_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAiStoreApiTree',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreApiTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_store_api_tree(self) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_api_tree_with_options(runtime)

    async def query_ai_store_api_tree_async(self) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_store_api_tree_with_options_async(runtime)

    def query_ai_store_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAiStoreRegions',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_store_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAiStoreRegions',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_store_regions(self) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_regions_with_options(runtime)

    async def query_ai_store_regions_async(self) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_store_regions_with_options_async(runtime)

    def query_ai_store_user_task_page_with_options(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiStoreUserTaskPage',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreUserTaskPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ai_store_user_task_page_with_options_async(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAiStoreUserTaskPage',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreUserTaskPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ai_store_user_task_page(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_user_task_page_with_options(request, runtime)

    async def query_ai_store_user_task_page_async(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_store_user_task_page_with_options_async(request, runtime)

    def update_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_key_prefix):
            body['BucketKeyPrefix'] = request.bucket_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.param_info):
            body['ParamInfo'] = request.param_info
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.receive_config):
            body['ReceiveConfig'] = request.receive_config
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.UpdateAiStoreUserTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_name):
            body['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.bucket_key_prefix):
            body['BucketKeyPrefix'] = request.bucket_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.param_info):
            body['ParamInfo'] = request.param_info
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.receive_config):
            body['ReceiveConfig'] = request.receive_config
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiStoreUserTask',
            version='2021-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20210930_models.UpdateAiStoreUserTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_store_user_task(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ai_store_user_task_with_options(request, runtime)

    async def update_ai_store_user_task_async(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ai_store_user_task_with_options_async(request, runtime)
