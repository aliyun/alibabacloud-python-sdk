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
        """
        @summary 创建 Group
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        """
        @summary 创建 Group
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        """
        @summary 创建 Group
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: alikafka_20181015_models.CreateConsumerGroupRequest,
    ) -> alikafka_20181015_models.CreateConsumerGroupResponse:
        """
        @summary 创建 Group
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        """
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        """
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        """
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: alikafka_20181015_models.CreateTopicRequest,
    ) -> alikafka_20181015_models.CreateTopicResponse:
        """
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        """
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        """
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        """
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: alikafka_20181015_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20181015_models.DeleteConsumerGroupResponse:
        """
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        """
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        """
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        """
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: alikafka_20181015_models.DeleteTopicRequest,
    ) -> alikafka_20181015_models.DeleteTopicResponse:
        """
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        """
        @param request: GetConsumerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        """
        @param request: GetConsumerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_list(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        """
        @param request: GetConsumerListRequest
        @return: GetConsumerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: alikafka_20181015_models.GetConsumerListRequest,
    ) -> alikafka_20181015_models.GetConsumerListResponse:
        """
        @param request: GetConsumerListRequest
        @return: GetConsumerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        """
        @param request: GetConsumerProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerProgress',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_progress_with_options_async(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        """
        @param request: GetConsumerProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerProgress',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetConsumerProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_progress(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        """
        @param request: GetConsumerProgressRequest
        @return: GetConsumerProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: alikafka_20181015_models.GetConsumerProgressRequest,
    ) -> alikafka_20181015_models.GetConsumerProgressResponse:
        """
        @param request: GetConsumerProgressRequest
        @return: GetConsumerProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_list(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: alikafka_20181015_models.GetInstanceListRequest,
    ) -> alikafka_20181015_models.GetInstanceListResponse:
        """
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        """
        @param request: GetTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_list_with_options_async(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        """
        @param request: GetTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicList',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_list(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        """
        @param request: GetTopicListRequest
        @return: GetTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: alikafka_20181015_models.GetTopicListRequest,
    ) -> alikafka_20181015_models.GetTopicListResponse:
        """
        @param request: GetTopicListRequest
        @return: GetTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        """
        @param request: GetTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicStatus',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_status_with_options_async(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        """
        @param request: GetTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicStatus',
            version='2018-10-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20181015_models.GetTopicStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_status(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        """
        @param request: GetTopicStatusRequest
        @return: GetTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: alikafka_20181015_models.GetTopicStatusRequest,
    ) -> alikafka_20181015_models.GetTopicStatusResponse:
        """
        @param request: GetTopicStatusRequest
        @return: GetTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)
