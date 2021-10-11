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

    def get_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskResponse(),
            self.do_rpcrequest('GetAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('GetAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_ai_store_user_task_page_with_options(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreUserTaskPageResponse(),
            self.do_rpcrequest('QueryAiStoreUserTaskPage', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ai_store_user_task_page_with_options_async(
        self,
        request: viapi_20210930_models.QueryAiStoreUserTaskPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreUserTaskPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreUserTaskPageResponse(),
            await self.do_rpcrequest_async('QueryAiStoreUserTaskPage', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_ai_store_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreRegionsResponse(),
            self.do_rpcrequest('QueryAiStoreRegions', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ai_store_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreRegionsResponse(),
            await self.do_rpcrequest_async('QueryAiStoreRegions', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ai_store_regions(self) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_regions_with_options(runtime)

    async def query_ai_store_regions_async(self) -> viapi_20210930_models.QueryAiStoreRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_store_regions_with_options_async(runtime)

    def list_ai_store_buckets_with_options(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.ListAiStoreBucketsResponse(),
            self.do_rpcrequest('ListAiStoreBuckets', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ai_store_buckets_with_options_async(
        self,
        request: viapi_20210930_models.ListAiStoreBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.ListAiStoreBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.ListAiStoreBucketsResponse(),
            await self.do_rpcrequest_async('ListAiStoreBuckets', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_ai_store_user_task_by_name_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskByNameResponse(),
            self.do_rpcrequest('GetAiStoreUserTaskByName', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ai_store_user_task_by_name_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreUserTaskByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreUserTaskByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskByNameResponse(),
            await self.do_rpcrequest_async('GetAiStoreUserTaskByName', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.UpdateAiStoreUserTaskResponse(),
            self.do_rpcrequest('UpdateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.UpdateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.UpdateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.UpdateAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('UpdateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def disable_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DisableAiStoreUserTaskResponse(),
            self.do_rpcrequest('DisableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.DisableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DisableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DisableAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('DisableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_ai_store_api_tree_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreApiTreeResponse(),
            self.do_rpcrequest('QueryAiStoreApiTree', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ai_store_api_tree_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreApiTreeResponse(),
            await self.do_rpcrequest_async('QueryAiStoreApiTree', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ai_store_api_tree(self) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_api_tree_with_options(runtime)

    async def query_ai_store_api_tree_async(self) -> viapi_20210930_models.QueryAiStoreApiTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ai_store_api_tree_with_options_async(runtime)

    def delete_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DeleteAiStoreUserTaskResponse(),
            self.do_rpcrequest('DeleteAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.DeleteAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.DeleteAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DeleteAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('DeleteAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreUserTaskResponse(),
            self.do_rpcrequest('CreateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('CreateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_ai_store_receive_config_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreReceiveConfigResponse(),
            self.do_rpcrequest('CreateAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ai_store_receive_config_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreReceiveConfigResponse(),
            await self.do_rpcrequest_async('CreateAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_ai_store_receive_config_with_options(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreReceiveConfigResponse(),
            self.do_rpcrequest('GetAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ai_store_receive_config_with_options_async(
        self,
        request: viapi_20210930_models.GetAiStoreReceiveConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.GetAiStoreReceiveConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreReceiveConfigResponse(),
            await self.do_rpcrequest_async('GetAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def enable_ai_store_user_task_with_options(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.EnableAiStoreUserTaskResponse(),
            self.do_rpcrequest('EnableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_ai_store_user_task_with_options_async(
        self,
        request: viapi_20210930_models.EnableAiStoreUserTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.EnableAiStoreUserTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.EnableAiStoreUserTaskResponse(),
            await self.do_rpcrequest_async('EnableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_ai_store_bucket_with_options(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreBucketResponse(),
            self.do_rpcrequest('CreateAiStoreBucket', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ai_store_bucket_with_options_async(
        self,
        request: viapi_20210930_models.CreateAiStoreBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CreateAiStoreBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreBucketResponse(),
            await self.do_rpcrequest_async('CreateAiStoreBucket', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.do_rpcrequest('CheckServiceLinkedRoleForDeleting', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: viapi_20210930_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.do_rpcrequest_async('CheckServiceLinkedRoleForDeleting', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
