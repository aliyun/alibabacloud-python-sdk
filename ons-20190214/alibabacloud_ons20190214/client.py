# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ons20190214 import models as ons_20190214_models
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
            'ap-northeast-2-pop': 'ons.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ons.aliyuncs.com',
            'cn-beijing-finance-pop': 'ons.aliyuncs.com',
            'cn-beijing-gov-1': 'ons.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ons.aliyuncs.com',
            'cn-edge-1': 'ons.aliyuncs.com',
            'cn-fujian': 'ons.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ons.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ons.aliyuncs.com',
            'cn-hangzhou-test-306': 'ons.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ons.aliyuncs.com',
            'cn-qingdao-nebula': 'ons.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ons.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ons.aliyuncs.com',
            'cn-shanghai-inner': 'ons.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ons.aliyuncs.com',
            'cn-shenzhen-inner': 'ons.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ons.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ons.aliyuncs.com',
            'cn-wuhan': 'ons.aliyuncs.com',
            'cn-yushanfang': 'ons.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ons.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ons.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ons.aliyuncs.com',
            'eu-west-1-oxs': 'ons.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'ons.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ons', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_tag_resources_with_options(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you call the **ListTagResources** operation, specify at least one of the following parameters in the request: **Tag.N.Key** and **ResourceId.N**. You can specify a resource ID to query all tags that are attached to the specified resource. You can also specify a tag key to query the tag value and the resource to which the tag is attached.
        *   If you include the **Tag.N.Key** parameter in a request, you can obtain the tag value and the ID of the resource to which the tag is attached.********\
        *   If you include the **ResourceId.N** parameter in a request, you can obtain the keys and values of all tags that are attached to the specified resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you call the **ListTagResources** operation, specify at least one of the following parameters in the request: **Tag.N.Key** and **ResourceId.N**. You can specify a resource ID to query all tags that are attached to the specified resource. You can also specify a tag key to query the tag value and the resource to which the tag is attached.
        *   If you include the **Tag.N.Key** parameter in a request, you can obtain the tag value and the ID of the resource to which the tag is attached.********\
        *   If you include the **ResourceId.N** parameter in a request, you can obtain the keys and values of all tags that are attached to the specified resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you call the **ListTagResources** operation, specify at least one of the following parameters in the request: **Tag.N.Key** and **ResourceId.N**. You can specify a resource ID to query all tags that are attached to the specified resource. You can also specify a tag key to query the tag value and the resource to which the tag is attached.
        *   If you include the **Tag.N.Key** parameter in a request, you can obtain the tag value and the ID of the resource to which the tag is attached.********\
        *   If you include the **ResourceId.N** parameter in a request, you can obtain the keys and values of all tags that are attached to the specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you call the **ListTagResources** operation, specify at least one of the following parameters in the request: **Tag.N.Key** and **ResourceId.N**. You can specify a resource ID to query all tags that are attached to the specified resource. You can also specify a tag key to query the tag value and the resource to which the tag is attached.
        *   If you include the **Tag.N.Key** parameter in a request, you can obtain the tag value and the ID of the resource to which the tag is attached.********\
        *   If you include the **ResourceId.N** parameter in a request, you can obtain the keys and values of all tags that are attached to the specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def ons_consumer_accumulate_with_options(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation in scenarios in which you want to know the message consumption progress of a specified consumer group in production environments. You can obtain the information about message consumption and consumption latency based on the returned information. This operation returns the total number of accumulated messages in all topics to which the specified consumer group subscribes and the number of accumulated messages in each topic.
        
        @param request: OnsConsumerAccumulateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerAccumulateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerAccumulate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerAccumulateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_accumulate_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation in scenarios in which you want to know the message consumption progress of a specified consumer group in production environments. You can obtain the information about message consumption and consumption latency based on the returned information. This operation returns the total number of accumulated messages in all topics to which the specified consumer group subscribes and the number of accumulated messages in each topic.
        
        @param request: OnsConsumerAccumulateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerAccumulateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerAccumulate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerAccumulateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_accumulate(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation in scenarios in which you want to know the message consumption progress of a specified consumer group in production environments. You can obtain the information about message consumption and consumption latency based on the returned information. This operation returns the total number of accumulated messages in all topics to which the specified consumer group subscribes and the number of accumulated messages in each topic.
        
        @param request: OnsConsumerAccumulateRequest
        @return: OnsConsumerAccumulateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_accumulate_with_options(request, runtime)

    async def ons_consumer_accumulate_async(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation in scenarios in which you want to know the message consumption progress of a specified consumer group in production environments. You can obtain the information about message consumption and consumption latency based on the returned information. This operation returns the total number of accumulated messages in all topics to which the specified consumer group subscribes and the number of accumulated messages in each topic.
        
        @param request: OnsConsumerAccumulateRequest
        @return: OnsConsumerAccumulateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_accumulate_with_options_async(request, runtime)

    def ons_consumer_get_connection_with_options(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When messages are accumulated in a topic, you can call this operation to check whether a consumer is online.
        
        @param request: OnsConsumerGetConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerGetConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerGetConnection',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerGetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_get_connection_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When messages are accumulated in a topic, you can call this operation to check whether a consumer is online.
        
        @param request: OnsConsumerGetConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerGetConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerGetConnection',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerGetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_get_connection(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When messages are accumulated in a topic, you can call this operation to check whether a consumer is online.
        
        @param request: OnsConsumerGetConnectionRequest
        @return: OnsConsumerGetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_get_connection_with_options(request, runtime)

    async def ons_consumer_get_connection_async(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When messages are accumulated in a topic, you can call this operation to check whether a consumer is online.
        
        @param request: OnsConsumerGetConnectionRequest
        @return: OnsConsumerGetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_get_connection_with_options_async(request, runtime)

    def ons_consumer_reset_offset_with_options(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to clear accumulated messages or reset the consumption progress. You can use one of the following methods to clear accumulated messages:
        *   Clear all accumulated messages in a specified topic.
        *   Clear the messages that were published to the specified topic before a specified point in time.
        
        @param request: OnsConsumerResetOffsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerResetOffsetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reset_timestamp):
            query['ResetTimestamp'] = request.reset_timestamp
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerResetOffset',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerResetOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_reset_offset_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to clear accumulated messages or reset the consumption progress. You can use one of the following methods to clear accumulated messages:
        *   Clear all accumulated messages in a specified topic.
        *   Clear the messages that were published to the specified topic before a specified point in time.
        
        @param request: OnsConsumerResetOffsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerResetOffsetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reset_timestamp):
            query['ResetTimestamp'] = request.reset_timestamp
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerResetOffset',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerResetOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_reset_offset(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to clear accumulated messages or reset the consumption progress. You can use one of the following methods to clear accumulated messages:
        *   Clear all accumulated messages in a specified topic.
        *   Clear the messages that were published to the specified topic before a specified point in time.
        
        @param request: OnsConsumerResetOffsetRequest
        @return: OnsConsumerResetOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_reset_offset_with_options(request, runtime)

    async def ons_consumer_reset_offset_async(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to clear accumulated messages or reset the consumption progress. You can use one of the following methods to clear accumulated messages:
        *   Clear all accumulated messages in a specified topic.
        *   Clear the messages that were published to the specified topic before a specified point in time.
        
        @param request: OnsConsumerResetOffsetRequest
        @return: OnsConsumerResetOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_reset_offset_with_options_async(request, runtime)

    def ons_consumer_status_with_options(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation in scenarios in which consumers are online and messages are accumulated. You can troubleshoot errors based on the information that is returned by this operation. You can check whether all consumers in the consumer group subscribe to the same topics and tags, and whether load balancing is performed as expected. You can also obtain the information about thread stack traces of online consumers.
        *   This operation uses multiple backend operations to query and aggregate data. The system requires a long period of time to process a request. We recommend that you do not frequently call this operation.
        
        @param request: OnsConsumerStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_jstack):
            query['NeedJstack'] = request.need_jstack
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerStatus',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_status_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation in scenarios in which consumers are online and messages are accumulated. You can troubleshoot errors based on the information that is returned by this operation. You can check whether all consumers in the consumer group subscribe to the same topics and tags, and whether load balancing is performed as expected. You can also obtain the information about thread stack traces of online consumers.
        *   This operation uses multiple backend operations to query and aggregate data. The system requires a long period of time to process a request. We recommend that you do not frequently call this operation.
        
        @param request: OnsConsumerStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_jstack):
            query['NeedJstack'] = request.need_jstack
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerStatus',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_status(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation in scenarios in which consumers are online and messages are accumulated. You can troubleshoot errors based on the information that is returned by this operation. You can check whether all consumers in the consumer group subscribe to the same topics and tags, and whether load balancing is performed as expected. You can also obtain the information about thread stack traces of online consumers.
        *   This operation uses multiple backend operations to query and aggregate data. The system requires a long period of time to process a request. We recommend that you do not frequently call this operation.
        
        @param request: OnsConsumerStatusRequest
        @return: OnsConsumerStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_status_with_options(request, runtime)

    async def ons_consumer_status_async(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation in scenarios in which consumers are online and messages are accumulated. You can troubleshoot errors based on the information that is returned by this operation. You can check whether all consumers in the consumer group subscribe to the same topics and tags, and whether load balancing is performed as expected. You can also obtain the information about thread stack traces of online consumers.
        *   This operation uses multiple backend operations to query and aggregate data. The system requires a long period of time to process a request. We recommend that you do not frequently call this operation.
        
        @param request: OnsConsumerStatusRequest
        @return: OnsConsumerStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_status_with_options_async(request, runtime)

    def ons_consumer_time_span_with_options(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the earliest point in time when a message was published to a specified topic and the most recent point in time when a message was published to the specified topic. You can also obtain the most recent point in time when a message in the topic was consumed. This operation is usually used with the \\*\\*OnsConsumerAccumulate\\*\\* operation to display the overview of the consumption progress.
        
        @param request: OnsConsumerTimeSpanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerTimeSpanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerTimeSpan',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerTimeSpanResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_time_span_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the earliest point in time when a message was published to a specified topic and the most recent point in time when a message was published to the specified topic. You can also obtain the most recent point in time when a message in the topic was consumed. This operation is usually used with the \\*\\*OnsConsumerAccumulate\\*\\* operation to display the overview of the consumption progress.
        
        @param request: OnsConsumerTimeSpanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsConsumerTimeSpanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsConsumerTimeSpan',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsConsumerTimeSpanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_time_span(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the earliest point in time when a message was published to a specified topic and the most recent point in time when a message was published to the specified topic. You can also obtain the most recent point in time when a message in the topic was consumed. This operation is usually used with the \\*\\*OnsConsumerAccumulate\\*\\* operation to display the overview of the consumption progress.
        
        @param request: OnsConsumerTimeSpanRequest
        @return: OnsConsumerTimeSpanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_time_span_with_options(request, runtime)

    async def ons_consumer_time_span_async(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the earliest point in time when a message was published to a specified topic and the most recent point in time when a message was published to the specified topic. You can also obtain the most recent point in time when a message in the topic was consumed. This operation is usually used with the \\*\\*OnsConsumerAccumulate\\*\\* operation to display the overview of the consumption progress.
        
        @param request: OnsConsumerTimeSpanRequest
        @return: OnsConsumerTimeSpanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_time_span_with_options_async(request, runtime)

    def ons_dlqmessage_get_by_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation uses the exact match method to query a dead-letter message based on the message ID. You can obtain the message ID that is required to query the information about a dead-letter message from the SendResult parameter that is returned after the message is sent. You can also obtain the message ID by calling the OnsDLQMessagePageQueryByGroupId operation to query multiple messages at a time. The queried information about the dead-letter message includes the point in time when the message is stored, the message body, and attributes such as the message tag and the message key.
        
        @param request: OnsDLQMessageGetByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessageGetByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessageGetById',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessageGetByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_get_by_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation uses the exact match method to query a dead-letter message based on the message ID. You can obtain the message ID that is required to query the information about a dead-letter message from the SendResult parameter that is returned after the message is sent. You can also obtain the message ID by calling the OnsDLQMessagePageQueryByGroupId operation to query multiple messages at a time. The queried information about the dead-letter message includes the point in time when the message is stored, the message body, and attributes such as the message tag and the message key.
        
        @param request: OnsDLQMessageGetByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessageGetByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessageGetById',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessageGetByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_get_by_id(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation uses the exact match method to query a dead-letter message based on the message ID. You can obtain the message ID that is required to query the information about a dead-letter message from the SendResult parameter that is returned after the message is sent. You can also obtain the message ID by calling the OnsDLQMessagePageQueryByGroupId operation to query multiple messages at a time. The queried information about the dead-letter message includes the point in time when the message is stored, the message body, and attributes such as the message tag and the message key.
        
        @param request: OnsDLQMessageGetByIdRequest
        @return: OnsDLQMessageGetByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_get_by_id_with_options(request, runtime)

    async def ons_dlqmessage_get_by_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation uses the exact match method to query a dead-letter message based on the message ID. You can obtain the message ID that is required to query the information about a dead-letter message from the SendResult parameter that is returned after the message is sent. You can also obtain the message ID by calling the OnsDLQMessagePageQueryByGroupId operation to query multiple messages at a time. The queried information about the dead-letter message includes the point in time when the message is stored, the message body, and attributes such as the message tag and the message key.
        
        @param request: OnsDLQMessageGetByIdRequest
        @return: OnsDLQMessageGetByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_get_by_id_with_options_async(request, runtime)

    def ons_dlqmessage_page_query_by_group_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the ID of the dead-letter message that you want to query, you can call this operation to query all dead-letter messages that are sent to a specified consumer group within a specified time range. The results are returned by page.
        *   We recommend that you specify a short time range to query dead-letter messages in this method. If you specify a long time range, a large number of dead-letter messages are returned. In this case, you cannot find the dead-letter message that you want to query in an efficient manner. You can perform the following steps to query dead-letter messages:
        1.  Perform a paged query by specifying the group ID, start time, end time, and number of entries to return on each page. If matched messages are found, the information about the dead-letter messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the dead-letter messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsDLQMessagePageQueryByGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessagePageQueryByGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessagePageQueryByGroupId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_page_query_by_group_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the ID of the dead-letter message that you want to query, you can call this operation to query all dead-letter messages that are sent to a specified consumer group within a specified time range. The results are returned by page.
        *   We recommend that you specify a short time range to query dead-letter messages in this method. If you specify a long time range, a large number of dead-letter messages are returned. In this case, you cannot find the dead-letter message that you want to query in an efficient manner. You can perform the following steps to query dead-letter messages:
        1.  Perform a paged query by specifying the group ID, start time, end time, and number of entries to return on each page. If matched messages are found, the information about the dead-letter messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the dead-letter messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsDLQMessagePageQueryByGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessagePageQueryByGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessagePageQueryByGroupId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_page_query_by_group_id(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the ID of the dead-letter message that you want to query, you can call this operation to query all dead-letter messages that are sent to a specified consumer group within a specified time range. The results are returned by page.
        *   We recommend that you specify a short time range to query dead-letter messages in this method. If you specify a long time range, a large number of dead-letter messages are returned. In this case, you cannot find the dead-letter message that you want to query in an efficient manner. You can perform the following steps to query dead-letter messages:
        1.  Perform a paged query by specifying the group ID, start time, end time, and number of entries to return on each page. If matched messages are found, the information about the dead-letter messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the dead-letter messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsDLQMessagePageQueryByGroupIdRequest
        @return: OnsDLQMessagePageQueryByGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_page_query_by_group_id_with_options(request, runtime)

    async def ons_dlqmessage_page_query_by_group_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the ID of the dead-letter message that you want to query, you can call this operation to query all dead-letter messages that are sent to a specified consumer group within a specified time range. The results are returned by page.
        *   We recommend that you specify a short time range to query dead-letter messages in this method. If you specify a long time range, a large number of dead-letter messages are returned. In this case, you cannot find the dead-letter message that you want to query in an efficient manner. You can perform the following steps to query dead-letter messages:
        1.  Perform a paged query by specifying the group ID, start time, end time, and number of entries to return on each page. If matched messages are found, the information about the dead-letter messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the dead-letter messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsDLQMessagePageQueryByGroupIdRequest
        @return: OnsDLQMessagePageQueryByGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_page_query_by_group_id_with_options_async(request, runtime)

    def ons_dlqmessage_resend_by_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After the number of retries to send a message to a consumer group for consumption reaches the upper limit and the message is not consumed by a consumer in the group, the message is added to the dead-letter queue of the consumer group. The message is a dead-letter message. After you resend the dead-letter message to the consumer group for consumption and the message fails to be consumed again after the maximum number of retries, a dead-letter message with the same message ID is added to the dead-letter queue. You can view the details of the dead-letter message on the Dead-letter Queues page in the Message Queue for Apache RocketMQ console or by calling the API operations that are used to query dead-letter messages. You can obtain the number of consumption failures for a message based on the number of dead-letter messages with the same message ID in the dead-letter queue.
        *   A dead-letter message is a message that fails to be consumed after the number of consumption retries reaches the upper limit. Generally, dead-letter messages are produced because of incorrect consumption logic. We recommend that you troubleshoot the consumption failures and then call this operation to send the message to the consumer group for consumption again.
        *   Message Queue for Apache RocketMQ does not manage the status of dead-letter messages based on the consumption status of the dead-letter messages. After you call this operation to send a dead-letter message to a consumer group and the message is consumed, Message Queue for Apache RocketMQ does not remove the dead-letter message from the dead-letter queue. You must manage dead-letter messages and determine whether to send a dead-letter message to a consumer group for consumption. This way, you do not resend and reconsume the messages that are consumed.
        
        @param request: OnsDLQMessageResendByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessageResendByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessageResendById',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessageResendByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_resend_by_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After the number of retries to send a message to a consumer group for consumption reaches the upper limit and the message is not consumed by a consumer in the group, the message is added to the dead-letter queue of the consumer group. The message is a dead-letter message. After you resend the dead-letter message to the consumer group for consumption and the message fails to be consumed again after the maximum number of retries, a dead-letter message with the same message ID is added to the dead-letter queue. You can view the details of the dead-letter message on the Dead-letter Queues page in the Message Queue for Apache RocketMQ console or by calling the API operations that are used to query dead-letter messages. You can obtain the number of consumption failures for a message based on the number of dead-letter messages with the same message ID in the dead-letter queue.
        *   A dead-letter message is a message that fails to be consumed after the number of consumption retries reaches the upper limit. Generally, dead-letter messages are produced because of incorrect consumption logic. We recommend that you troubleshoot the consumption failures and then call this operation to send the message to the consumer group for consumption again.
        *   Message Queue for Apache RocketMQ does not manage the status of dead-letter messages based on the consumption status of the dead-letter messages. After you call this operation to send a dead-letter message to a consumer group and the message is consumed, Message Queue for Apache RocketMQ does not remove the dead-letter message from the dead-letter queue. You must manage dead-letter messages and determine whether to send a dead-letter message to a consumer group for consumption. This way, you do not resend and reconsume the messages that are consumed.
        
        @param request: OnsDLQMessageResendByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsDLQMessageResendByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsDLQMessageResendById',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsDLQMessageResendByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_resend_by_id(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After the number of retries to send a message to a consumer group for consumption reaches the upper limit and the message is not consumed by a consumer in the group, the message is added to the dead-letter queue of the consumer group. The message is a dead-letter message. After you resend the dead-letter message to the consumer group for consumption and the message fails to be consumed again after the maximum number of retries, a dead-letter message with the same message ID is added to the dead-letter queue. You can view the details of the dead-letter message on the Dead-letter Queues page in the Message Queue for Apache RocketMQ console or by calling the API operations that are used to query dead-letter messages. You can obtain the number of consumption failures for a message based on the number of dead-letter messages with the same message ID in the dead-letter queue.
        *   A dead-letter message is a message that fails to be consumed after the number of consumption retries reaches the upper limit. Generally, dead-letter messages are produced because of incorrect consumption logic. We recommend that you troubleshoot the consumption failures and then call this operation to send the message to the consumer group for consumption again.
        *   Message Queue for Apache RocketMQ does not manage the status of dead-letter messages based on the consumption status of the dead-letter messages. After you call this operation to send a dead-letter message to a consumer group and the message is consumed, Message Queue for Apache RocketMQ does not remove the dead-letter message from the dead-letter queue. You must manage dead-letter messages and determine whether to send a dead-letter message to a consumer group for consumption. This way, you do not resend and reconsume the messages that are consumed.
        
        @param request: OnsDLQMessageResendByIdRequest
        @return: OnsDLQMessageResendByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_resend_by_id_with_options(request, runtime)

    async def ons_dlqmessage_resend_by_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After the number of retries to send a message to a consumer group for consumption reaches the upper limit and the message is not consumed by a consumer in the group, the message is added to the dead-letter queue of the consumer group. The message is a dead-letter message. After you resend the dead-letter message to the consumer group for consumption and the message fails to be consumed again after the maximum number of retries, a dead-letter message with the same message ID is added to the dead-letter queue. You can view the details of the dead-letter message on the Dead-letter Queues page in the Message Queue for Apache RocketMQ console or by calling the API operations that are used to query dead-letter messages. You can obtain the number of consumption failures for a message based on the number of dead-letter messages with the same message ID in the dead-letter queue.
        *   A dead-letter message is a message that fails to be consumed after the number of consumption retries reaches the upper limit. Generally, dead-letter messages are produced because of incorrect consumption logic. We recommend that you troubleshoot the consumption failures and then call this operation to send the message to the consumer group for consumption again.
        *   Message Queue for Apache RocketMQ does not manage the status of dead-letter messages based on the consumption status of the dead-letter messages. After you call this operation to send a dead-letter message to a consumer group and the message is consumed, Message Queue for Apache RocketMQ does not remove the dead-letter message from the dead-letter queue. You must manage dead-letter messages and determine whether to send a dead-letter message to a consumer group for consumption. This way, you do not resend and reconsume the messages that are consumed.
        
        @param request: OnsDLQMessageResendByIdRequest
        @return: OnsDLQMessageResendByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_resend_by_id_with_options_async(request, runtime)

    def ons_group_consumer_update_with_options(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to configure the permissions for a consumer group to read messages based on a specified region of Message Queue for Apache RocketMQ and a specified group ID. You can call this operation in scenarios in which you want to forbid consumers in a specific group from reading messages.
        
        @param request: OnsGroupConsumerUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupConsumerUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.read_enable):
            query['ReadEnable'] = request.read_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupConsumerUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupConsumerUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_consumer_update_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to configure the permissions for a consumer group to read messages based on a specified region of Message Queue for Apache RocketMQ and a specified group ID. You can call this operation in scenarios in which you want to forbid consumers in a specific group from reading messages.
        
        @param request: OnsGroupConsumerUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupConsumerUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.read_enable):
            query['ReadEnable'] = request.read_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupConsumerUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupConsumerUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_consumer_update(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to configure the permissions for a consumer group to read messages based on a specified region of Message Queue for Apache RocketMQ and a specified group ID. You can call this operation in scenarios in which you want to forbid consumers in a specific group from reading messages.
        
        @param request: OnsGroupConsumerUpdateRequest
        @return: OnsGroupConsumerUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_group_consumer_update_with_options(request, runtime)

    async def ons_group_consumer_update_async(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to configure the permissions for a consumer group to read messages based on a specified region of Message Queue for Apache RocketMQ and a specified group ID. You can call this operation in scenarios in which you want to forbid consumers in a specific group from reading messages.
        
        @param request: OnsGroupConsumerUpdateRequest
        @return: OnsGroupConsumerUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_consumer_update_with_options_async(request, runtime)

    def ons_group_create_with_options(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you release a new application or implement new business logic, you need new consumer groups. You can call this operation to create a consumer group.
        
        @param request: OnsGroupCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_create_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you release a new application or implement new business logic, you need new consumer groups. You can call this operation to create a consumer group.
        
        @param request: OnsGroupCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_create(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you release a new application or implement new business logic, you need new consumer groups. You can call this operation to create a consumer group.
        
        @param request: OnsGroupCreateRequest
        @return: OnsGroupCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_group_create_with_options(request, runtime)

    async def ons_group_create_async(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you release a new application or implement new business logic, you need new consumer groups. You can call this operation to create a consumer group.
        
        @param request: OnsGroupCreateRequest
        @return: OnsGroupCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_create_with_options_async(request, runtime)

    def ons_group_delete_with_options(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        """
        >
        *   The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After you delete a group, the consumers in the group immediately stop receiving messages. Exercise caution when you call this operation.
        You can call this operation to delete a group when you need to deallocate the resources of the group. For example, after an application is brought offline, you can delete the groups that are used for the application. After you delete a group, the backend of Message Queue for Apache RocketMQ deallocates the resources of the group. The system requires a long period of time to deallocate the resources. We recommend that you do not create a group that uses the same name as a deleted group immediately after you delete the group. If the system fails to delete the specified group, troubleshoot the issue based on the error code.
        
        @param request: OnsGroupDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        """
        >
        *   The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After you delete a group, the consumers in the group immediately stop receiving messages. Exercise caution when you call this operation.
        You can call this operation to delete a group when you need to deallocate the resources of the group. For example, after an application is brought offline, you can delete the groups that are used for the application. After you delete a group, the backend of Message Queue for Apache RocketMQ deallocates the resources of the group. The system requires a long period of time to deallocate the resources. We recommend that you do not create a group that uses the same name as a deleted group immediately after you delete the group. If the system fails to delete the specified group, troubleshoot the issue based on the error code.
        
        @param request: OnsGroupDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_delete(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        """
        >
        *   The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After you delete a group, the consumers in the group immediately stop receiving messages. Exercise caution when you call this operation.
        You can call this operation to delete a group when you need to deallocate the resources of the group. For example, after an application is brought offline, you can delete the groups that are used for the application. After you delete a group, the backend of Message Queue for Apache RocketMQ deallocates the resources of the group. The system requires a long period of time to deallocate the resources. We recommend that you do not create a group that uses the same name as a deleted group immediately after you delete the group. If the system fails to delete the specified group, troubleshoot the issue based on the error code.
        
        @param request: OnsGroupDeleteRequest
        @return: OnsGroupDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_group_delete_with_options(request, runtime)

    async def ons_group_delete_async(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        """
        >
        *   The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After you delete a group, the consumers in the group immediately stop receiving messages. Exercise caution when you call this operation.
        You can call this operation to delete a group when you need to deallocate the resources of the group. For example, after an application is brought offline, you can delete the groups that are used for the application. After you delete a group, the backend of Message Queue for Apache RocketMQ deallocates the resources of the group. The system requires a long period of time to deallocate the resources. We recommend that you do not create a group that uses the same name as a deleted group immediately after you delete the group. If the system fails to delete the specified group, troubleshoot the issue based on the error code.
        
        @param request: OnsGroupDeleteRequest
        @return: OnsGroupDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_delete_with_options_async(request, runtime)

    def ons_group_list_with_options(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_list_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_list(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
    ) -> ons_20190214_models.OnsGroupListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupListRequest
        @return: OnsGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_group_list_with_options(request, runtime)

    async def ons_group_list_async(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
    ) -> ons_20190214_models.OnsGroupListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupListRequest
        @return: OnsGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_list_with_options_async(request, runtime)

    def ons_group_sub_detail_with_options(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupSubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupSubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupSubDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupSubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_sub_detail_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupSubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsGroupSubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsGroupSubDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsGroupSubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_sub_detail(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupSubDetailRequest
        @return: OnsGroupSubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_group_sub_detail_with_options(request, runtime)

    async def ons_group_sub_detail_async(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsGroupSubDetailRequest
        @return: OnsGroupSubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_sub_detail_with_options_async(request, runtime)

    def ons_instance_base_info_with_options(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        To send and receive messages, a client must be connected to a Message Queue for Apache RocketMQ instance by using an endpoint. You can call this operation to query the endpoints of the instance.
        
        @param request: OnsInstanceBaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceBaseInfo',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_base_info_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        To send and receive messages, a client must be connected to a Message Queue for Apache RocketMQ instance by using an endpoint. You can call this operation to query the endpoints of the instance.
        
        @param request: OnsInstanceBaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceBaseInfo',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_base_info(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        To send and receive messages, a client must be connected to a Message Queue for Apache RocketMQ instance by using an endpoint. You can call this operation to query the endpoints of the instance.
        
        @param request: OnsInstanceBaseInfoRequest
        @return: OnsInstanceBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_base_info_with_options(request, runtime)

    async def ons_instance_base_info_async(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        To send and receive messages, a client must be connected to a Message Queue for Apache RocketMQ instance by using an endpoint. You can call this operation to query the endpoints of the instance.
        
        @param request: OnsInstanceBaseInfoRequest
        @return: OnsInstanceBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_base_info_with_options_async(request, runtime)

    def ons_instance_create_with_options(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        An instance is a virtual machine (VM) that can be used to store information about the topics and groups of Message Queue for Apache RocketMQ. You can call this operation when you need to create service resources for the business that you want to launch. Take note of the following points when you call this operation:
        *   A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        *   This operation can be called to create only a Standard Edition instance. You can use the Message Queue for Apache RocketMQ console to create Standard Edition instances and Enterprise Platinum Edition instances. For information about how to create Message Queue for Apache RocketMQ instances, see [Manage instances](~~200153~~).
        
        @param request: OnsInstanceCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_create_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        An instance is a virtual machine (VM) that can be used to store information about the topics and groups of Message Queue for Apache RocketMQ. You can call this operation when you need to create service resources for the business that you want to launch. Take note of the following points when you call this operation:
        *   A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        *   This operation can be called to create only a Standard Edition instance. You can use the Message Queue for Apache RocketMQ console to create Standard Edition instances and Enterprise Platinum Edition instances. For information about how to create Message Queue for Apache RocketMQ instances, see [Manage instances](~~200153~~).
        
        @param request: OnsInstanceCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_create(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        An instance is a virtual machine (VM) that can be used to store information about the topics and groups of Message Queue for Apache RocketMQ. You can call this operation when you need to create service resources for the business that you want to launch. Take note of the following points when you call this operation:
        *   A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        *   This operation can be called to create only a Standard Edition instance. You can use the Message Queue for Apache RocketMQ console to create Standard Edition instances and Enterprise Platinum Edition instances. For information about how to create Message Queue for Apache RocketMQ instances, see [Manage instances](~~200153~~).
        
        @param request: OnsInstanceCreateRequest
        @return: OnsInstanceCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_create_with_options(request, runtime)

    async def ons_instance_create_async(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        An instance is a virtual machine (VM) that can be used to store information about the topics and groups of Message Queue for Apache RocketMQ. You can call this operation when you need to create service resources for the business that you want to launch. Take note of the following points when you call this operation:
        *   A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        *   This operation can be called to create only a Standard Edition instance. You can use the Message Queue for Apache RocketMQ console to create Standard Edition instances and Enterprise Platinum Edition instances. For information about how to create Message Queue for Apache RocketMQ instances, see [Manage instances](~~200153~~).
        
        @param request: OnsInstanceCreateRequest
        @return: OnsInstanceCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_create_with_options_async(request, runtime)

    def ons_instance_delete_with_options(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation when you need to reclaim resources. For example, after you unpublish an application, you can reclaim the resources that were used for the application. An instance can be deleted only when the instance does not contain topics and groups.
        *   After an instance is deleted, the instance cannot be recovered. Exercise caution when you call this operation.
        
        @param request: OnsInstanceDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation when you need to reclaim resources. For example, after you unpublish an application, you can reclaim the resources that were used for the application. An instance can be deleted only when the instance does not contain topics and groups.
        *   After an instance is deleted, the instance cannot be recovered. Exercise caution when you call this operation.
        
        @param request: OnsInstanceDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_delete(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation when you need to reclaim resources. For example, after you unpublish an application, you can reclaim the resources that were used for the application. An instance can be deleted only when the instance does not contain topics and groups.
        *   After an instance is deleted, the instance cannot be recovered. Exercise caution when you call this operation.
        
        @param request: OnsInstanceDeleteRequest
        @return: OnsInstanceDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_delete_with_options(request, runtime)

    async def ons_instance_delete_async(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation when you need to reclaim resources. For example, after you unpublish an application, you can reclaim the resources that were used for the application. An instance can be deleted only when the instance does not contain topics and groups.
        *   After an instance is deleted, the instance cannot be recovered. Exercise caution when you call this operation.
        
        @param request: OnsInstanceDeleteRequest
        @return: OnsInstanceDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_delete_with_options_async(request, runtime)

    def ons_instance_in_service_list_with_options(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsInstanceInServiceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceInServiceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceInServiceList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceInServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_in_service_list_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsInstanceInServiceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceInServiceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceInServiceList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceInServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_in_service_list(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsInstanceInServiceListRequest
        @return: OnsInstanceInServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_in_service_list_with_options(request, runtime)

    async def ons_instance_in_service_list_async(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: OnsInstanceInServiceListRequest
        @return: OnsInstanceInServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_in_service_list_with_options_async(request, runtime)

    def ons_instance_update_with_options(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        
        @param request: OnsInstanceUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_update_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        
        @param request: OnsInstanceUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsInstanceUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsInstanceUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsInstanceUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_update(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        
        @param request: OnsInstanceUpdateRequest
        @return: OnsInstanceUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_update_with_options(request, runtime)

    async def ons_instance_update_async(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        A maximum of eight Message Queue for Apache RocketMQ instances can be deployed in each region.
        
        @param request: OnsInstanceUpdateRequest
        @return: OnsInstanceUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_update_with_options_async(request, runtime)

    def ons_message_detail_with_options(
        self,
        request: ons_20190214_models.OnsMessageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_detail_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_detail(
        self,
        request: ons_20190214_models.OnsMessageDetailRequest,
    ) -> ons_20190214_models.OnsMessageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_detail_with_options(request, runtime)

    async def ons_message_detail_async(
        self,
        request: ons_20190214_models.OnsMessageDetailRequest,
    ) -> ons_20190214_models.OnsMessageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_detail_with_options_async(request, runtime)

    def ons_message_get_by_key_with_options(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   This operation uses the fuzzy match method to query messages based on a specified message key. The same message key may be used by multiple messages. Therefore, the returned result may contain the information about multiple messages.
        *   This operation can be used in scenarios in which you cannot obtain the IDs of the messages that you want to query. You can perform the following steps to query the information about messages:
        1.  Call this operation to query message IDs.
        2.  Call the **OnsMessageGetByMsgId** operation to query the details of a specified message. The OnsMessageGetByMsgId operation uses the exact match method. For more information about the **OnsMessageGetByMsgId** operation, see [OnsMessageGetByMsgId](~~29607~~).
        
        @param request: OnsMessageGetByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageGetByKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageGetByKey',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageGetByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_get_by_key_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   This operation uses the fuzzy match method to query messages based on a specified message key. The same message key may be used by multiple messages. Therefore, the returned result may contain the information about multiple messages.
        *   This operation can be used in scenarios in which you cannot obtain the IDs of the messages that you want to query. You can perform the following steps to query the information about messages:
        1.  Call this operation to query message IDs.
        2.  Call the **OnsMessageGetByMsgId** operation to query the details of a specified message. The OnsMessageGetByMsgId operation uses the exact match method. For more information about the **OnsMessageGetByMsgId** operation, see [OnsMessageGetByMsgId](~~29607~~).
        
        @param request: OnsMessageGetByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageGetByKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageGetByKey',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageGetByKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_get_by_key(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   This operation uses the fuzzy match method to query messages based on a specified message key. The same message key may be used by multiple messages. Therefore, the returned result may contain the information about multiple messages.
        *   This operation can be used in scenarios in which you cannot obtain the IDs of the messages that you want to query. You can perform the following steps to query the information about messages:
        1.  Call this operation to query message IDs.
        2.  Call the **OnsMessageGetByMsgId** operation to query the details of a specified message. The OnsMessageGetByMsgId operation uses the exact match method. For more information about the **OnsMessageGetByMsgId** operation, see [OnsMessageGetByMsgId](~~29607~~).
        
        @param request: OnsMessageGetByKeyRequest
        @return: OnsMessageGetByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_message_get_by_key_with_options(request, runtime)

    async def ons_message_get_by_key_async(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   This operation uses the fuzzy match method to query messages based on a specified message key. The same message key may be used by multiple messages. Therefore, the returned result may contain the information about multiple messages.
        *   This operation can be used in scenarios in which you cannot obtain the IDs of the messages that you want to query. You can perform the following steps to query the information about messages:
        1.  Call this operation to query message IDs.
        2.  Call the **OnsMessageGetByMsgId** operation to query the details of a specified message. The OnsMessageGetByMsgId operation uses the exact match method. For more information about the **OnsMessageGetByMsgId** operation, see [OnsMessageGetByMsgId](~~29607~~).
        
        @param request: OnsMessageGetByKeyRequest
        @return: OnsMessageGetByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_get_by_key_with_options_async(request, runtime)

    def ons_message_get_by_msg_id_with_options(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If a message is not consumed as expected, you can call this operation to query the information about the message for troubleshooting.
        *   This operation uses the exact match method to query a message based on the message ID. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. You must store the returned information after each message is sent. The queried information about a message includes the point in time when the message was sent, the broker on which the message is stored, and the attributes of the message such as the message key and tag.
        
        @param request: OnsMessageGetByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageGetByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageGetByMsgId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageGetByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_get_by_msg_id_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If a message is not consumed as expected, you can call this operation to query the information about the message for troubleshooting.
        *   This operation uses the exact match method to query a message based on the message ID. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. You must store the returned information after each message is sent. The queried information about a message includes the point in time when the message was sent, the broker on which the message is stored, and the attributes of the message such as the message key and tag.
        
        @param request: OnsMessageGetByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageGetByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageGetByMsgId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageGetByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_get_by_msg_id(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If a message is not consumed as expected, you can call this operation to query the information about the message for troubleshooting.
        *   This operation uses the exact match method to query a message based on the message ID. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. You must store the returned information after each message is sent. The queried information about a message includes the point in time when the message was sent, the broker on which the message is stored, and the attributes of the message such as the message key and tag.
        
        @param request: OnsMessageGetByMsgIdRequest
        @return: OnsMessageGetByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_message_get_by_msg_id_with_options(request, runtime)

    async def ons_message_get_by_msg_id_async(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If a message is not consumed as expected, you can call this operation to query the information about the message for troubleshooting.
        *   This operation uses the exact match method to query a message based on the message ID. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. You must store the returned information after each message is sent. The queried information about a message includes the point in time when the message was sent, the broker on which the message is stored, and the attributes of the message such as the message key and tag.
        
        @param request: OnsMessageGetByMsgIdRequest
        @return: OnsMessageGetByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_get_by_msg_id_with_options_async(request, runtime)

    def ons_message_page_query_by_topic_with_options(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the message ID or message key of a message that you want to query, you can call this operation to query all messages that are stored in a topic within a specified time range. The results are displayed by page.
        *   We recommend that you specify a short time range to query messages. If you specify a long time range, a large number of messages are returned. In this case, you cannot find the message that you want to query in an efficient manner. You can perform the following steps to query messages:
        1.  Perform a paged query by specifying the topic, start time, end time, and number of entries to return on each page. If the topic contains messages, the information about the messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsMessagePageQueryByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessagePageQueryByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessagePageQueryByTopic',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessagePageQueryByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_page_query_by_topic_with_options_async(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the message ID or message key of a message that you want to query, you can call this operation to query all messages that are stored in a topic within a specified time range. The results are displayed by page.
        *   We recommend that you specify a short time range to query messages. If you specify a long time range, a large number of messages are returned. In this case, you cannot find the message that you want to query in an efficient manner. You can perform the following steps to query messages:
        1.  Perform a paged query by specifying the topic, start time, end time, and number of entries to return on each page. If the topic contains messages, the information about the messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsMessagePageQueryByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessagePageQueryByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessagePageQueryByTopic',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessagePageQueryByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_page_query_by_topic(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the message ID or message key of a message that you want to query, you can call this operation to query all messages that are stored in a topic within a specified time range. The results are displayed by page.
        *   We recommend that you specify a short time range to query messages. If you specify a long time range, a large number of messages are returned. In this case, you cannot find the message that you want to query in an efficient manner. You can perform the following steps to query messages:
        1.  Perform a paged query by specifying the topic, start time, end time, and number of entries to return on each page. If the topic contains messages, the information about the messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsMessagePageQueryByTopicRequest
        @return: OnsMessagePageQueryByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_message_page_query_by_topic_with_options(request, runtime)

    async def ons_message_page_query_by_topic_async(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   If you do not know the message ID or message key of a message that you want to query, you can call this operation to query all messages that are stored in a topic within a specified time range. The results are displayed by page.
        *   We recommend that you specify a short time range to query messages. If you specify a long time range, a large number of messages are returned. In this case, you cannot find the message that you want to query in an efficient manner. You can perform the following steps to query messages:
        1.  Perform a paged query by specifying the topic, start time, end time, and number of entries to return on each page. If the topic contains messages, the information about the messages on the first page, total number of pages, and task ID are returned by default.
        2.  Specify the task ID and a page number to call this operation again to query the messages on the specified page. In this query, the BeginTime, EndTime, and PageSize parameters do not take effect. By default, the system uses the values of these parameters that you specified in the request when you created the specified query task.
        
        @param request: OnsMessagePageQueryByTopicRequest
        @return: OnsMessagePageQueryByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_page_query_by_topic_with_options_async(request, runtime)

    def ons_message_push_with_options(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        """
        ## Note
        This operation can be used to check whether messages in a specified topic can be consumed by consumers in a specified consumer group. This operation obtains the body of the message that is specified by the MsgId parameter, re-encapsulates the message body to produce a new message, and then pushes the new message to a specified consumer. The content of the message that is sent to the consumer is the same as the content of the original message. They are not the same message because they use different message IDs.
        
        @param request: OnsMessagePushRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessagePushResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessagePush',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessagePushResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_push_with_options_async(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        """
        ## Note
        This operation can be used to check whether messages in a specified topic can be consumed by consumers in a specified consumer group. This operation obtains the body of the message that is specified by the MsgId parameter, re-encapsulates the message body to produce a new message, and then pushes the new message to a specified consumer. The content of the message that is sent to the consumer is the same as the content of the original message. They are not the same message because they use different message IDs.
        
        @param request: OnsMessagePushRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessagePushResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessagePush',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessagePushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_push(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        """
        ## Note
        This operation can be used to check whether messages in a specified topic can be consumed by consumers in a specified consumer group. This operation obtains the body of the message that is specified by the MsgId parameter, re-encapsulates the message body to produce a new message, and then pushes the new message to a specified consumer. The content of the message that is sent to the consumer is the same as the content of the original message. They are not the same message because they use different message IDs.
        
        @param request: OnsMessagePushRequest
        @return: OnsMessagePushResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_message_push_with_options(request, runtime)

    async def ons_message_push_async(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        """
        ## Note
        This operation can be used to check whether messages in a specified topic can be consumed by consumers in a specified consumer group. This operation obtains the body of the message that is specified by the MsgId parameter, re-encapsulates the message body to produce a new message, and then pushes the new message to a specified consumer. The content of the message that is sent to the consumer is the same as the content of the original message. They are not the same message because they use different message IDs.
        
        @param request: OnsMessagePushRequest
        @return: OnsMessagePushResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_push_with_options_async(request, runtime)

    def ons_message_trace_with_options(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation to check whether a specified message is consumed. If the message is not consumed, you can troubleshoot the issue based on the returned information.
        *   This operation queries information based on the built-in offset mechanism of Message Queue for Apache RocketMQ. In most cases, the results are correct. If you have reset the consumer offset or cleared accumulated messages, the results may not be correct.
        
        @param request: OnsMessageTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageTraceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageTrace',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_trace_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation to check whether a specified message is consumed. If the message is not consumed, you can troubleshoot the issue based on the returned information.
        *   This operation queries information based on the built-in offset mechanism of Message Queue for Apache RocketMQ. In most cases, the results are correct. If you have reset the consumer offset or cleared accumulated messages, the results may not be correct.
        
        @param request: OnsMessageTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsMessageTraceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsMessageTrace',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsMessageTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_trace(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation to check whether a specified message is consumed. If the message is not consumed, you can troubleshoot the issue based on the returned information.
        *   This operation queries information based on the built-in offset mechanism of Message Queue for Apache RocketMQ. In most cases, the results are correct. If you have reset the consumer offset or cleared accumulated messages, the results may not be correct.
        
        @param request: OnsMessageTraceRequest
        @return: OnsMessageTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_message_trace_with_options(request, runtime)

    async def ons_message_trace_async(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   You can call this operation to check whether a specified message is consumed. If the message is not consumed, you can troubleshoot the issue based on the returned information.
        *   This operation queries information based on the built-in offset mechanism of Message Queue for Apache RocketMQ. In most cases, the results are correct. If you have reset the consumer offset or cleared accumulated messages, the results may not be correct.
        
        @param request: OnsMessageTraceRequest
        @return: OnsMessageTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_trace_with_options_async(request, runtime)

    def ons_region_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsRegionListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you use an SDK to access and manage a Message Queue for Apache RocketMQ instance, you must sequentially specify the information about two regions. You can query the information about the second region by calling the \\*\\*OnsRegionList\\*\\* operation. You must apply for a public endpoint in the following scenarios:
        *   Connect your application to Message Queue for Apache RocketMQ: Select the nearest API gateway endpoint based on the region where your application is deployed, and enter the corresponding **region ID**. The **regionId** is used to access Alibaba Cloud API Gateway because Message Queue for Apache RocketMQ instances provide API services by using the OpenAPI Explorer platform, which is also called POP.
        *   Access a region to manage its resources: Specify a region where you want to manage Message Queue for Apache RocketMQ resources and enter the region ID. You can query the region ID by calling the **OnsRegionList** operation.
        
        @param request: OnsRegionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsRegionListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OnsRegionList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_region_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsRegionListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you use an SDK to access and manage a Message Queue for Apache RocketMQ instance, you must sequentially specify the information about two regions. You can query the information about the second region by calling the \\*\\*OnsRegionList\\*\\* operation. You must apply for a public endpoint in the following scenarios:
        *   Connect your application to Message Queue for Apache RocketMQ: Select the nearest API gateway endpoint based on the region where your application is deployed, and enter the corresponding **region ID**. The **regionId** is used to access Alibaba Cloud API Gateway because Message Queue for Apache RocketMQ instances provide API services by using the OpenAPI Explorer platform, which is also called POP.
        *   Access a region to manage its resources: Specify a region where you want to manage Message Queue for Apache RocketMQ resources and enter the region ID. You can query the region ID by calling the **OnsRegionList** operation.
        
        @param request: OnsRegionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsRegionListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OnsRegionList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_region_list(self) -> ons_20190214_models.OnsRegionListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you use an SDK to access and manage a Message Queue for Apache RocketMQ instance, you must sequentially specify the information about two regions. You can query the information about the second region by calling the \\*\\*OnsRegionList\\*\\* operation. You must apply for a public endpoint in the following scenarios:
        *   Connect your application to Message Queue for Apache RocketMQ: Select the nearest API gateway endpoint based on the region where your application is deployed, and enter the corresponding **region ID**. The **regionId** is used to access Alibaba Cloud API Gateway because Message Queue for Apache RocketMQ instances provide API services by using the OpenAPI Explorer platform, which is also called POP.
        *   Access a region to manage its resources: Specify a region where you want to manage Message Queue for Apache RocketMQ resources and enter the region ID. You can query the region ID by calling the **OnsRegionList** operation.
        
        @return: OnsRegionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_region_list_with_options(runtime)

    async def ons_region_list_async(self) -> ons_20190214_models.OnsRegionListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you use an SDK to access and manage a Message Queue for Apache RocketMQ instance, you must sequentially specify the information about two regions. You can query the information about the second region by calling the \\*\\*OnsRegionList\\*\\* operation. You must apply for a public endpoint in the following scenarios:
        *   Connect your application to Message Queue for Apache RocketMQ: Select the nearest API gateway endpoint based on the region where your application is deployed, and enter the corresponding **region ID**. The **regionId** is used to access Alibaba Cloud API Gateway because Message Queue for Apache RocketMQ instances provide API services by using the OpenAPI Explorer platform, which is also called POP.
        *   Access a region to manage its resources: Specify a region where you want to manage Message Queue for Apache RocketMQ resources and enter the region ID. You can query the region ID by calling the **OnsRegionList** operation.
        
        @return: OnsRegionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_region_list_with_options_async(runtime)

    def ons_topic_create_with_options(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you want to release a new application or expand your business, you can call this operation to create a topic based on your business requirements.
        
        @param request: OnsTopicCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_create_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you want to release a new application or expand your business, you can call this operation to create a topic based on your business requirements.
        
        @param request: OnsTopicCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicCreate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_create(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you want to release a new application or expand your business, you can call this operation to create a topic based on your business requirements.
        
        @param request: OnsTopicCreateRequest
        @return: OnsTopicCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_create_with_options(request, runtime)

    async def ons_topic_create_async(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        When you want to release a new application or expand your business, you can call this operation to create a topic based on your business requirements.
        
        @param request: OnsTopicCreateRequest
        @return: OnsTopicCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_create_with_options_async(request, runtime)

    def ons_topic_delete_with_options(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        """
        >  The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur. - After you delete the topic, the publishing and subscription relationships that are constructed based on the topic are cleared. Exercise caution when you call this operation.
        You can call this operation to delete a topic when you need to reclaim the resources from the topic. For example, after an application is brought offline, you can delete the topics that are used for the application. After you delete a topic, the backend of Message Queue for Apache RocketMQ reclaims the resources from the topic. The system requires a long period of time to reclaim the resources. After you delete a topic, we recommend that you do not create a topic that uses the same name as the deleted topic within a short period of time. If the system fails to delete the specified topic, troubleshoot the issue based on the error code.
        
        @param request: OnsTopicDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        """
        >  The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur. - After you delete the topic, the publishing and subscription relationships that are constructed based on the topic are cleared. Exercise caution when you call this operation.
        You can call this operation to delete a topic when you need to reclaim the resources from the topic. For example, after an application is brought offline, you can delete the topics that are used for the application. After you delete a topic, the backend of Message Queue for Apache RocketMQ reclaims the resources from the topic. The system requires a long period of time to reclaim the resources. After you delete a topic, we recommend that you do not create a topic that uses the same name as the deleted topic within a short period of time. If the system fails to delete the specified topic, troubleshoot the issue based on the error code.
        
        @param request: OnsTopicDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicDelete',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_delete(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        """
        >  The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur. - After you delete the topic, the publishing and subscription relationships that are constructed based on the topic are cleared. Exercise caution when you call this operation.
        You can call this operation to delete a topic when you need to reclaim the resources from the topic. For example, after an application is brought offline, you can delete the topics that are used for the application. After you delete a topic, the backend of Message Queue for Apache RocketMQ reclaims the resources from the topic. The system requires a long period of time to reclaim the resources. After you delete a topic, we recommend that you do not create a topic that uses the same name as the deleted topic within a short period of time. If the system fails to delete the specified topic, troubleshoot the issue based on the error code.
        
        @param request: OnsTopicDeleteRequest
        @return: OnsTopicDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_delete_with_options(request, runtime)

    async def ons_topic_delete_async(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        """
        >  The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur. - After you delete the topic, the publishing and subscription relationships that are constructed based on the topic are cleared. Exercise caution when you call this operation.
        You can call this operation to delete a topic when you need to reclaim the resources from the topic. For example, after an application is brought offline, you can delete the topics that are used for the application. After you delete a topic, the backend of Message Queue for Apache RocketMQ reclaims the resources from the topic. The system requires a long period of time to reclaim the resources. After you delete a topic, we recommend that you do not create a topic that uses the same name as the deleted topic within a short period of time. If the system fails to delete the specified topic, troubleshoot the issue based on the error code.
        
        @param request: OnsTopicDeleteRequest
        @return: OnsTopicDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_delete_with_options_async(request, runtime)

    def ons_topic_list_with_options(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation returns the basic information about topics and does not return the details of topics.
        
        @param request: OnsTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_list_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation returns the basic information about topics and does not return the details of topics.
        
        @param request: OnsTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicList',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_list(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
    ) -> ons_20190214_models.OnsTopicListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation returns the basic information about topics and does not return the details of topics.
        
        @param request: OnsTopicListRequest
        @return: OnsTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_list_with_options(request, runtime)

    async def ons_topic_list_async(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
    ) -> ons_20190214_models.OnsTopicListResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        This operation returns the basic information about topics and does not return the details of topics.
        
        @param request: OnsTopicListRequest
        @return: OnsTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_list_with_options_async(request, runtime)

    def ons_topic_status_with_options(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can determine the resource usage of a topic based on the information that is returned by this operation. The returned information includes the total number of messages in the topic and the most recent point in time when a message was published to the topic.
        
        @param request: OnsTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicStatus',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_status_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can determine the resource usage of a topic based on the information that is returned by this operation. The returned information includes the total number of messages in the topic and the most recent point in time when a message was published to the topic.
        
        @param request: OnsTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicStatus',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_status(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can determine the resource usage of a topic based on the information that is returned by this operation. The returned information includes the total number of messages in the topic and the most recent point in time when a message was published to the topic.
        
        @param request: OnsTopicStatusRequest
        @return: OnsTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_status_with_options(request, runtime)

    async def ons_topic_status_async(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can determine the resource usage of a topic based on the information that is returned by this operation. The returned information includes the total number of messages in the topic and the most recent point in time when a message was published to the topic.
        
        @param request: OnsTopicStatusRequest
        @return: OnsTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_status_with_options_async(request, runtime)

    def ons_topic_sub_detail_with_options(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the online consumer groups that subscribe to a specified topic. If all consumers in a group are offline, the information about the group is not returned.
        
        @param request: OnsTopicSubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicSubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicSubDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicSubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_sub_detail_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the online consumer groups that subscribe to a specified topic. If all consumers in a group are offline, the information about the group is not returned.
        
        @param request: OnsTopicSubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicSubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicSubDetail',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicSubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_sub_detail(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the online consumer groups that subscribe to a specified topic. If all consumers in a group are offline, the information about the group is not returned.
        
        @param request: OnsTopicSubDetailRequest
        @return: OnsTopicSubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_sub_detail_with_options(request, runtime)

    async def ons_topic_sub_detail_async(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to query the online consumer groups that subscribe to a specified topic. If all consumers in a group are offline, the information about the group is not returned.
        
        @param request: OnsTopicSubDetailRequest
        @return: OnsTopicSubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_sub_detail_with_options_async(request, runtime)

    def ons_topic_update_with_options(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        """
        @deprecated
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise system risks may occur.
        You can call this operation to forbid read or write operations on a specific topic.
        
        @param request: OnsTopicUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicUpdateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perm):
            query['Perm'] = request.perm
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_update_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        """
        @deprecated
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise system risks may occur.
        You can call this operation to forbid read or write operations on a specific topic.
        
        @param request: OnsTopicUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTopicUpdateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perm):
            query['Perm'] = request.perm
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTopicUpdate',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTopicUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_update(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        """
        @deprecated
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise system risks may occur.
        You can call this operation to forbid read or write operations on a specific topic.
        
        @param request: OnsTopicUpdateRequest
        @return: OnsTopicUpdateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_update_with_options(request, runtime)

    async def ons_topic_update_async(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        """
        @deprecated
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise system risks may occur.
        You can call this operation to forbid read or write operations on a specific topic.
        
        @param request: OnsTopicUpdateRequest
        @return: OnsTopicUpdateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_update_with_options_async(request, runtime)

    def ons_trace_get_result_with_options(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        """
        ## Usage notes
        *   Before you call this operation to query the details of the trace of a message, you must create a task to query the trace of the message based on the message ID or message key and obtains the task ID. Then, you can call this operation to query the details of the message trace based on the task ID. You can call the [OnsTraceQueryByMsgId](~~59830~~) operation or the [OnsTraceQueryByMsgKey](~~59831~~) operation to create a task to query the trace of the message and obtain the task ID from the **QueryId** response parameter.
        *   A trace query task is time-consuming. If you call this operation to query the details immediately after you create a trace query task, the results may be empty. In this case, we recommend that you try again later.
        
        @param request: OnsTraceGetResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceGetResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceGetResult',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceGetResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_get_result_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        """
        ## Usage notes
        *   Before you call this operation to query the details of the trace of a message, you must create a task to query the trace of the message based on the message ID or message key and obtains the task ID. Then, you can call this operation to query the details of the message trace based on the task ID. You can call the [OnsTraceQueryByMsgId](~~59830~~) operation or the [OnsTraceQueryByMsgKey](~~59831~~) operation to create a task to query the trace of the message and obtain the task ID from the **QueryId** response parameter.
        *   A trace query task is time-consuming. If you call this operation to query the details immediately after you create a trace query task, the results may be empty. In this case, we recommend that you try again later.
        
        @param request: OnsTraceGetResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceGetResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceGetResult',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceGetResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_get_result(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        """
        ## Usage notes
        *   Before you call this operation to query the details of the trace of a message, you must create a task to query the trace of the message based on the message ID or message key and obtains the task ID. Then, you can call this operation to query the details of the message trace based on the task ID. You can call the [OnsTraceQueryByMsgId](~~59830~~) operation or the [OnsTraceQueryByMsgKey](~~59831~~) operation to create a task to query the trace of the message and obtain the task ID from the **QueryId** response parameter.
        *   A trace query task is time-consuming. If you call this operation to query the details immediately after you create a trace query task, the results may be empty. In this case, we recommend that you try again later.
        
        @param request: OnsTraceGetResultRequest
        @return: OnsTraceGetResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_get_result_with_options(request, runtime)

    async def ons_trace_get_result_async(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        """
        ## Usage notes
        *   Before you call this operation to query the details of the trace of a message, you must create a task to query the trace of the message based on the message ID or message key and obtains the task ID. Then, you can call this operation to query the details of the message trace based on the task ID. You can call the [OnsTraceQueryByMsgId](~~59830~~) operation or the [OnsTraceQueryByMsgKey](~~59831~~) operation to create a task to query the trace of the message and obtain the task ID from the **QueryId** response parameter.
        *   A trace query task is time-consuming. If you call this operation to query the details immediately after you create a trace query task, the results may be empty. In this case, we recommend that you try again later.
        
        @param request: OnsTraceGetResultRequest
        @return: OnsTraceGetResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_get_result_with_options_async(request, runtime)

    def ons_trace_query_by_msg_id_with_options(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        """
        ## Note
        If you want to query the trace of a message based on the message ID, you can call this operation to create a query task. After you obtain the task ID, you can call the [OnsTraceGetResult](~~59832~~) operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceQueryByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceQueryByMsgId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceQueryByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_query_by_msg_id_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        """
        ## Note
        If you want to query the trace of a message based on the message ID, you can call this operation to create a query task. After you obtain the task ID, you can call the [OnsTraceGetResult](~~59832~~) operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceQueryByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceQueryByMsgId',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceQueryByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_query_by_msg_id(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        """
        ## Note
        If you want to query the trace of a message based on the message ID, you can call this operation to create a query task. After you obtain the task ID, you can call the [OnsTraceGetResult](~~59832~~) operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgIdRequest
        @return: OnsTraceQueryByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_query_by_msg_id_with_options(request, runtime)

    async def ons_trace_query_by_msg_id_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        """
        ## Note
        If you want to query the trace of a message based on the message ID, you can call this operation to create a query task. After you obtain the task ID, you can call the [OnsTraceGetResult](~~59832~~) operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgIdRequest
        @return: OnsTraceQueryByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_query_by_msg_id_with_options_async(request, runtime)

    def ons_trace_query_by_msg_key_with_options(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        If you obtain the key of a message and want to query the trace of the message, you can call this operation to create a query task. After you obtain the task ID, you can call the OnsTraceGetResult operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceQueryByMsgKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_key):
            query['MsgKey'] = request.msg_key
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceQueryByMsgKey',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceQueryByMsgKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_query_by_msg_key_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        If you obtain the key of a message and want to query the trace of the message, you can call this operation to create a query task. After you obtain the task ID, you can call the OnsTraceGetResult operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTraceQueryByMsgKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_key):
            query['MsgKey'] = request.msg_key
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTraceQueryByMsgKey',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTraceQueryByMsgKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_query_by_msg_key(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        If you obtain the key of a message and want to query the trace of the message, you can call this operation to create a query task. After you obtain the task ID, you can call the OnsTraceGetResult operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgKeyRequest
        @return: OnsTraceQueryByMsgKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_query_by_msg_key_with_options(request, runtime)

    async def ons_trace_query_by_msg_key_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        If you obtain the key of a message and want to query the trace of the message, you can call this operation to create a query task. After you obtain the task ID, you can call the OnsTraceGetResult operation to query the details of the message trace based on the task ID.
        
        @param request: OnsTraceQueryByMsgKeyRequest
        @return: OnsTraceQueryByMsgKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_query_by_msg_key_with_options_async(request, runtime)

    def ons_trend_group_output_tps_with_options(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        """
        ## Note
        You can call this operation to query the following statistics that are collected in the production environment:
        *   The number of messages that are consumed during each sampling period
        *   The transactions per second (TPS) for message consumption during each sampling period
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are consumed during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendGroupOutputTpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTrendGroupOutputTpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTrendGroupOutputTps',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTrendGroupOutputTpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trend_group_output_tps_with_options_async(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        """
        ## Note
        You can call this operation to query the following statistics that are collected in the production environment:
        *   The number of messages that are consumed during each sampling period
        *   The transactions per second (TPS) for message consumption during each sampling period
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are consumed during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendGroupOutputTpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTrendGroupOutputTpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTrendGroupOutputTps',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTrendGroupOutputTpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trend_group_output_tps(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        """
        ## Note
        You can call this operation to query the following statistics that are collected in the production environment:
        *   The number of messages that are consumed during each sampling period
        *   The transactions per second (TPS) for message consumption during each sampling period
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are consumed during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendGroupOutputTpsRequest
        @return: OnsTrendGroupOutputTpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_trend_group_output_tps_with_options(request, runtime)

    async def ons_trend_group_output_tps_async(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        """
        ## Note
        You can call this operation to query the following statistics that are collected in the production environment:
        *   The number of messages that are consumed during each sampling period
        *   The transactions per second (TPS) for message consumption during each sampling period
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are consumed during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendGroupOutputTpsRequest
        @return: OnsTrendGroupOutputTpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_trend_group_output_tps_with_options_async(request, runtime)

    def ons_trend_topic_input_tps_with_options(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        """
        ## Note
        You can call this operation to query the statistics of messages that are published to a specified topic in the production environment. You can obtain the number of messages that are published to the topic or the transactions per second (TPS) for message publishing during each sampling period within a specified time range.
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are published to the topic during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendTopicInputTpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTrendTopicInputTpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTrendTopicInputTps',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTrendTopicInputTpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trend_topic_input_tps_with_options_async(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        """
        ## Note
        You can call this operation to query the statistics of messages that are published to a specified topic in the production environment. You can obtain the number of messages that are published to the topic or the transactions per second (TPS) for message publishing during each sampling period within a specified time range.
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are published to the topic during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendTopicInputTpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnsTrendTopicInputTpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnsTrendTopicInputTps',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OnsTrendTopicInputTpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trend_topic_input_tps(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        """
        ## Note
        You can call this operation to query the statistics of messages that are published to a specified topic in the production environment. You can obtain the number of messages that are published to the topic or the transactions per second (TPS) for message publishing during each sampling period within a specified time range.
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are published to the topic during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendTopicInputTpsRequest
        @return: OnsTrendTopicInputTpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ons_trend_topic_input_tps_with_options(request, runtime)

    async def ons_trend_topic_input_tps_async(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        """
        ## Note
        You can call this operation to query the statistics of messages that are published to a specified topic in the production environment. You can obtain the number of messages that are published to the topic or the transactions per second (TPS) for message publishing during each sampling period within a specified time range.
        >  If your application publishes a small number of messages and does not publish messages at a specific interval, we recommend that you query the number of messages that are published to the topic during each sampling period because the statistics of TPS may not show a clear change trend.
        
        @param request: OnsTrendTopicInputTpsRequest
        @return: OnsTrendTopicInputTpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ons_trend_topic_input_tps_with_options_async(request, runtime)

    def open_ons_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OpenOnsServiceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation when you use Message Queue for Apache RocketMQ for the first time. You can use Message Queue for Apache RocketMQ only after this service is activated.
        The Message Queue for Apache RocketMQ service can be activated only in the China (Hangzhou) region. Service activation is not billed.
        
        @param request: OpenOnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenOnsServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenOnsService',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OpenOnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ons_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OpenOnsServiceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation when you use Message Queue for Apache RocketMQ for the first time. You can use Message Queue for Apache RocketMQ only after this service is activated.
        The Message Queue for Apache RocketMQ service can be activated only in the China (Hangzhou) region. Service activation is not billed.
        
        @param request: OpenOnsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenOnsServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenOnsService',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.OpenOnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ons_service(self) -> ons_20190214_models.OpenOnsServiceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation when you use Message Queue for Apache RocketMQ for the first time. You can use Message Queue for Apache RocketMQ only after this service is activated.
        The Message Queue for Apache RocketMQ service can be activated only in the China (Hangzhou) region. Service activation is not billed.
        
        @return: OpenOnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_ons_service_with_options(runtime)

    async def open_ons_service_async(self) -> ons_20190214_models.OpenOnsServiceResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation when you use Message Queue for Apache RocketMQ for the first time. You can use Message Queue for Apache RocketMQ only after this service is activated.
        The Message Queue for Apache RocketMQ service can be activated only in the China (Hangzhou) region. Service activation is not billed.
        
        @return: OpenOnsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_ons_service_with_options_async(runtime)

    def tag_resources_with_options(
        self,
        request: ons_20190214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.TagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to attach tags to a source. You can use tags to classify resources in Message Queue for Apache RocketMQ. This can help you aggregate and search resources in an efficient manner.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ons_20190214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.TagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to attach tags to a source. You can use tags to classify resources in Message Queue for Apache RocketMQ. This can help you aggregate and search resources in an efficient manner.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ons_20190214_models.TagResourcesRequest,
    ) -> ons_20190214_models.TagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to attach tags to a source. You can use tags to classify resources in Message Queue for Apache RocketMQ. This can help you aggregate and search resources in an efficient manner.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ons_20190214_models.TagResourcesRequest,
    ) -> ons_20190214_models.TagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        You can call this operation to attach tags to a source. You can use tags to classify resources in Message Queue for Apache RocketMQ. This can help you aggregate and search resources in an efficient manner.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.UntagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.UntagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-02-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_20190214_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
    ) -> ons_20190214_models.UntagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
    ) -> ons_20190214_models.UntagResourcesResponse:
        """
        > : The API operations that are provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
