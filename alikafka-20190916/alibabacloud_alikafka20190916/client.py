# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20190916 import models as alikafka_20190916_models
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

    def convert_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ConvertPostPayOrderResponse(),
            self.do_rpcrequest('ConvertPostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ConvertPostPayOrderResponse(),
            await self.do_rpcrequest_async('ConvertPostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_post_pay_order(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    async def convert_post_pay_order_async(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_post_pay_order_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateAclResponse(),
            self.do_rpcrequest('CreateAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateAclResponse(),
            await self.do_rpcrequest_async('CreateAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
    ) -> alikafka_20190916_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
    ) -> alikafka_20190916_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateConsumerGroupResponse(),
            self.do_rpcrequest('CreateConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateConsumerGroupResponse(),
            await self.do_rpcrequest_async('CreateConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_consumer_group(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePostPayOrderResponse(),
            self.do_rpcrequest('CreatePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePostPayOrderResponse(),
            await self.do_rpcrequest_async('CreatePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_post_pay_order(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_post_pay_order_with_options(request, runtime)

    async def create_post_pay_order_async(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_post_pay_order_with_options_async(request, runtime)

    def create_pre_pay_order_with_options(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePrePayOrderResponse(),
            self.do_rpcrequest('CreatePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pre_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePrePayOrderResponse(),
            await self.do_rpcrequest_async('CreatePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pre_pay_order(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pre_pay_order_with_options(request, runtime)

    async def create_pre_pay_order_async(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pre_pay_order_with_options_async(request, runtime)

    def create_sasl_user_with_options(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateSaslUserResponse(),
            self.do_rpcrequest('CreateSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sasl_user_with_options_async(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateSaslUserResponse(),
            await self.do_rpcrequest_async('CreateSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sasl_user(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    async def create_sasl_user_async(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sasl_user_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateTopicResponse(),
            self.do_rpcrequest('CreateTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateTopicResponse(),
            await self.do_rpcrequest_async('CreateTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_topic(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteAclResponse(),
            self.do_rpcrequest('DeleteAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteAclResponse(),
            await self.do_rpcrequest_async('DeleteAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteConsumerGroupResponse(),
            self.do_rpcrequest('DeleteConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteConsumerGroupResponse(),
            await self.do_rpcrequest_async('DeleteConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_consumer_group(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteInstanceResponse(),
            await self.do_rpcrequest_async('DeleteInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sasl_user_with_options(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteSaslUserResponse(),
            self.do_rpcrequest('DeleteSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sasl_user_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteSaslUserResponse(),
            await self.do_rpcrequest_async('DeleteSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sasl_user(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    async def delete_sasl_user_async(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sasl_user_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteTopicResponse(),
            self.do_rpcrequest('DeleteTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteTopicResponse(),
            await self.do_rpcrequest_async('DeleteTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_topic(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeAclsResponse(),
            self.do_rpcrequest('DescribeAcls', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeAclsResponse(),
            await self.do_rpcrequest_async('DescribeAcls', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acls(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_node_status_with_options(
        self,
        request: alikafka_20190916_models.DescribeNodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeNodeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeNodeStatusResponse(),
            self.do_rpcrequest('DescribeNodeStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_node_status_with_options_async(
        self,
        request: alikafka_20190916_models.DescribeNodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeNodeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeNodeStatusResponse(),
            await self.do_rpcrequest_async('DescribeNodeStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_node_status(
        self,
        request: alikafka_20190916_models.DescribeNodeStatusRequest,
    ) -> alikafka_20190916_models.DescribeNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_status_with_options(request, runtime)

    async def describe_node_status_async(
        self,
        request: alikafka_20190916_models.DescribeNodeStatusRequest,
    ) -> alikafka_20190916_models.DescribeNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_status_with_options_async(request, runtime)

    def describe_sasl_users_with_options(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeSaslUsersResponse(),
            self.do_rpcrequest('DescribeSaslUsers', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sasl_users_with_options_async(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeSaslUsersResponse(),
            await self.do_rpcrequest_async('DescribeSaslUsers', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sasl_users(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    async def describe_sasl_users_async(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sasl_users_with_options_async(request, runtime)

    def get_allowed_ip_list_with_options(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllowedIpListResponse(),
            self.do_rpcrequest('GetAllowedIpList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_allowed_ip_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllowedIpListResponse(),
            await self.do_rpcrequest_async('GetAllowedIpList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_allowed_ip_list(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    async def get_allowed_ip_list_async(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_allowed_ip_list_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerListResponse(),
            self.do_rpcrequest('GetConsumerList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consumer_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerListResponse(),
            await self.do_rpcrequest_async('GetConsumerList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_list(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerProgressResponse(),
            self.do_rpcrequest('GetConsumerProgress', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consumer_progress_with_options_async(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerProgressResponse(),
            await self.do_rpcrequest_async('GetConsumerProgress', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_progress(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetInstanceListResponse(),
            self.do_rpcrequest('GetInstanceList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetInstanceListResponse(),
            await self.do_rpcrequest_async('GetInstanceList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_list(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_meta_product_list_with_options(
        self,
        request: alikafka_20190916_models.GetMetaProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetMetaProductListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetMetaProductListResponse(),
            self.do_rpcrequest('GetMetaProductList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_product_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetMetaProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetMetaProductListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetMetaProductListResponse(),
            await self.do_rpcrequest_async('GetMetaProductList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_product_list(
        self,
        request: alikafka_20190916_models.GetMetaProductListRequest,
    ) -> alikafka_20190916_models.GetMetaProductListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_product_list_with_options(request, runtime)

    async def get_meta_product_list_async(
        self,
        request: alikafka_20190916_models.GetMetaProductListRequest,
    ) -> alikafka_20190916_models.GetMetaProductListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_product_list_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicListResponse(),
            self.do_rpcrequest('GetTopicList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicListResponse(),
            await self.do_rpcrequest_async('GetTopicList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_list(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicStatusResponse(),
            self.do_rpcrequest('GetTopicStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_status_with_options_async(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicStatusResponse(),
            await self.do_rpcrequest_async('GetTopicStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_status(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyInstanceNameResponse(),
            self.do_rpcrequest('ModifyInstanceName', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyInstanceNameResponse(),
            await self.do_rpcrequest_async('ModifyInstanceName', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_name(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_partition_num_with_options(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyPartitionNumResponse(),
            self.do_rpcrequest('ModifyPartitionNum', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_partition_num_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyPartitionNumResponse(),
            await self.do_rpcrequest_async('ModifyPartitionNum', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_partition_num(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    async def modify_partition_num_async(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_partition_num_with_options_async(request, runtime)

    def modify_topic_remark_with_options(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyTopicRemarkResponse(),
            self.do_rpcrequest('ModifyTopicRemark', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_topic_remark_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyTopicRemarkResponse(),
            await self.do_rpcrequest_async('ModifyTopicRemark', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_topic_remark(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    async def modify_topic_remark_async(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_topic_remark_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ReleaseInstanceResponse(),
            self.do_rpcrequest('ReleaseInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ReleaseInstanceResponse(),
            await self.do_rpcrequest_async('ReleaseInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.StartInstanceResponse(),
            await self.do_rpcrequest_async('StartInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_allowed_ip_with_options(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateAllowedIpResponse(),
            self.do_rpcrequest('UpdateAllowedIp', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_allowed_ip_with_options_async(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateAllowedIpResponse(),
            await self.do_rpcrequest_async('UpdateAllowedIp', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_allowed_ip(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    async def update_allowed_ip_async(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_allowed_ip_with_options_async(request, runtime)

    def update_instance_config_with_options(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateInstanceConfigResponse(),
            self.do_rpcrequest('UpdateInstanceConfig', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_config_with_options_async(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateInstanceConfigResponse(),
            await self.do_rpcrequest_async('UpdateInstanceConfig', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_config(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_config_with_options(request, runtime)

    async def update_instance_config_async(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_config_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradeInstanceVersionResponse(),
            self.do_rpcrequest('UpgradeInstanceVersion', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradeInstanceVersionResponse(),
            await self.do_rpcrequest_async('UpgradeInstanceVersion', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def upgrade_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePostPayOrderResponse(),
            self.do_rpcrequest('UpgradePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePostPayOrderResponse(),
            await self.do_rpcrequest_async('UpgradePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_post_pay_order(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_post_pay_order_with_options(request, runtime)

    async def upgrade_post_pay_order_async(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_post_pay_order_with_options_async(request, runtime)

    def upgrade_pre_pay_order_with_options(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePrePayOrderResponse(),
            self.do_rpcrequest('UpgradePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_pre_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePrePayOrderResponse(),
            await self.do_rpcrequest_async('UpgradePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_pre_pay_order(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_pre_pay_order_with_options(request, runtime)

    async def upgrade_pre_pay_order_async(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_pre_pay_order_with_options_async(request, runtime)
