# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20181015 import models as alikafka_20181015_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'alikafka.aliyuncs.com',
            'ap-southeast-2': 'alikafka.aliyuncs.com',
            'cn-beijing-finance-1': 'alikafka.aliyuncs.com',
            'cn-beijing-finance-pop': 'alikafka.aliyuncs.com',
            'cn-beijing-gov-1': 'alikafka.aliyuncs.com',
            'cn-beijing-nu16-b01': 'alikafka.aliyuncs.com',
            'cn-edge-1': 'alikafka.aliyuncs.com',
            'cn-fujian': 'alikafka.aliyuncs.com',
            'cn-haidian-cm12-c01': 'alikafka.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'alikafka.aliyuncs.com',
            'cn-hangzhou-test-306': 'alikafka.aliyuncs.com',
            'cn-hongkong-finance-pop': 'alikafka.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'alikafka.aliyuncs.com',
            'cn-qingdao-nebula': 'alikafka.aliyuncs.com',
            'cn-shanghai-et15-b01': 'alikafka.aliyuncs.com',
            'cn-shanghai-et2-b01': 'alikafka.aliyuncs.com',
            'cn-shanghai-inner': 'alikafka.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'alikafka.aliyuncs.com',
            'cn-shenzhen-inner': 'alikafka.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'alikafka.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'alikafka.aliyuncs.com',
            'cn-wuhan': 'alikafka.aliyuncs.com',
            'cn-wulanchabu': 'alikafka.aliyuncs.com',
            'cn-yushanfang': 'alikafka.aliyuncs.com',
            'cn-zhangbei': 'alikafka.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'alikafka.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'alikafka.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'alikafka.aliyuncs.com',
            'eu-west-1-oxs': 'alikafka.aliyuncs.com',
            'me-east-1': 'alikafka.aliyuncs.com',
            'rus-west-1-pop': 'alikafka.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafka', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_consumer_group_with_options(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateConsumerGroupResponse(),
            self.do_rpcrequest('CreateConsumerGroup', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateConsumerGroupResponse(),
            await self.do_rpcrequest_async('CreateConsumerGroup', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_consumer_group(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateTopicResponse(),
            self.do_rpcrequest('CreateTopic', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateTopicResponse(),
            await self.do_rpcrequest_async('CreateTopic', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_topic(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteConsumerGroupResponse(),
            self.do_rpcrequest('DeleteConsumerGroup', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteConsumerGroupResponse(),
            await self.do_rpcrequest_async('DeleteConsumerGroup', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_consumer_group(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteTopicResponse(),
            self.do_rpcrequest('DeleteTopic', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteTopicResponse(),
            await self.do_rpcrequest_async('DeleteTopic', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_topic(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerListResponse(),
            self.do_rpcrequest('GetConsumerList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consumer_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerListResponse(),
            await self.do_rpcrequest_async('GetConsumerList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_list(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerProgressResponse(),
            self.do_rpcrequest('GetConsumerProgress', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consumer_progress_with_options_async(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerProgressResponse(),
            await self.do_rpcrequest_async('GetConsumerProgress', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_progress(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetInstanceListResponse(),
            self.do_rpcrequest('GetInstanceList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetInstanceListResponse(),
            await self.do_rpcrequest_async('GetInstanceList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_list(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicListResponse(),
            self.do_rpcrequest('GetTopicList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicListResponse(),
            await self.do_rpcrequest_async('GetTopicList', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_list(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicStatusResponse(),
            self.do_rpcrequest('GetTopicStatus', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_status_with_options_async(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicStatusResponse(),
            await self.do_rpcrequest_async('GetTopicStatus', '2018-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_status(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)
