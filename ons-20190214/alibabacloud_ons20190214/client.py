# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ons20190214 import models as ons_20190214_models
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ons_20190214_models.ListTagResourcesRequest,
    ) -> ons_20190214_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def ons_consumer_accumulate_with_options(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerAccumulateResponse().from_map(
            self.do_rpcrequest('OnsConsumerAccumulate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_consumer_accumulate_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerAccumulateResponse().from_map(
            await self.do_rpcrequest_async('OnsConsumerAccumulate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_consumer_accumulate(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_accumulate_with_options(request, runtime)

    async def ons_consumer_accumulate_async(
        self,
        request: ons_20190214_models.OnsConsumerAccumulateRequest,
    ) -> ons_20190214_models.OnsConsumerAccumulateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_accumulate_with_options_async(request, runtime)

    def ons_consumer_get_connection_with_options(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerGetConnectionResponse().from_map(
            self.do_rpcrequest('OnsConsumerGetConnection', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_consumer_get_connection_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerGetConnectionResponse().from_map(
            await self.do_rpcrequest_async('OnsConsumerGetConnection', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_consumer_get_connection(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_get_connection_with_options(request, runtime)

    async def ons_consumer_get_connection_async(
        self,
        request: ons_20190214_models.OnsConsumerGetConnectionRequest,
    ) -> ons_20190214_models.OnsConsumerGetConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_get_connection_with_options_async(request, runtime)

    def ons_consumer_reset_offset_with_options(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerResetOffsetResponse().from_map(
            self.do_rpcrequest('OnsConsumerResetOffset', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_consumer_reset_offset_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerResetOffsetResponse().from_map(
            await self.do_rpcrequest_async('OnsConsumerResetOffset', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_consumer_reset_offset(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_reset_offset_with_options(request, runtime)

    async def ons_consumer_reset_offset_async(
        self,
        request: ons_20190214_models.OnsConsumerResetOffsetRequest,
    ) -> ons_20190214_models.OnsConsumerResetOffsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_reset_offset_with_options_async(request, runtime)

    def ons_consumer_status_with_options(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerStatusResponse().from_map(
            self.do_rpcrequest('OnsConsumerStatus', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_consumer_status_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerStatusResponse().from_map(
            await self.do_rpcrequest_async('OnsConsumerStatus', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_consumer_status(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_status_with_options(request, runtime)

    async def ons_consumer_status_async(
        self,
        request: ons_20190214_models.OnsConsumerStatusRequest,
    ) -> ons_20190214_models.OnsConsumerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_status_with_options_async(request, runtime)

    def ons_consumer_time_span_with_options(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerTimeSpanResponse().from_map(
            self.do_rpcrequest('OnsConsumerTimeSpan', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_consumer_time_span_with_options_async(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsConsumerTimeSpanResponse().from_map(
            await self.do_rpcrequest_async('OnsConsumerTimeSpan', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_consumer_time_span(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_consumer_time_span_with_options(request, runtime)

    async def ons_consumer_time_span_async(
        self,
        request: ons_20190214_models.OnsConsumerTimeSpanRequest,
    ) -> ons_20190214_models.OnsConsumerTimeSpanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_consumer_time_span_with_options_async(request, runtime)

    def ons_dlqmessage_get_by_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessageGetByIdResponse().from_map(
            self.do_rpcrequest('OnsDLQMessageGetById', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_dlqmessage_get_by_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessageGetByIdResponse().from_map(
            await self.do_rpcrequest_async('OnsDLQMessageGetById', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_dlqmessage_get_by_id(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_get_by_id_with_options(request, runtime)

    async def ons_dlqmessage_get_by_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessageGetByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageGetByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_get_by_id_with_options_async(request, runtime)

    def ons_dlqmessage_page_query_by_group_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse().from_map(
            self.do_rpcrequest('OnsDLQMessagePageQueryByGroupId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_dlqmessage_page_query_by_group_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse().from_map(
            await self.do_rpcrequest_async('OnsDLQMessagePageQueryByGroupId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_dlqmessage_page_query_by_group_id(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_page_query_by_group_id_with_options(request, runtime)

    async def ons_dlqmessage_page_query_by_group_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> ons_20190214_models.OnsDLQMessagePageQueryByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_page_query_by_group_id_with_options_async(request, runtime)

    def ons_dlqmessage_resend_by_id_with_options(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessageResendByIdResponse().from_map(
            self.do_rpcrequest('OnsDLQMessageResendById', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_dlqmessage_resend_by_id_with_options_async(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsDLQMessageResendByIdResponse().from_map(
            await self.do_rpcrequest_async('OnsDLQMessageResendById', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_dlqmessage_resend_by_id(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_dlqmessage_resend_by_id_with_options(request, runtime)

    async def ons_dlqmessage_resend_by_id_async(
        self,
        request: ons_20190214_models.OnsDLQMessageResendByIdRequest,
    ) -> ons_20190214_models.OnsDLQMessageResendByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_dlqmessage_resend_by_id_with_options_async(request, runtime)

    def ons_group_consumer_update_with_options(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupConsumerUpdateResponse().from_map(
            self.do_rpcrequest('OnsGroupConsumerUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_group_consumer_update_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupConsumerUpdateResponse().from_map(
            await self.do_rpcrequest_async('OnsGroupConsumerUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_group_consumer_update(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_group_consumer_update_with_options(request, runtime)

    async def ons_group_consumer_update_async(
        self,
        request: ons_20190214_models.OnsGroupConsumerUpdateRequest,
    ) -> ons_20190214_models.OnsGroupConsumerUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_consumer_update_with_options_async(request, runtime)

    def ons_group_create_with_options(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupCreateResponse().from_map(
            self.do_rpcrequest('OnsGroupCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_group_create_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupCreateResponse().from_map(
            await self.do_rpcrequest_async('OnsGroupCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_group_create(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_group_create_with_options(request, runtime)

    async def ons_group_create_async(
        self,
        request: ons_20190214_models.OnsGroupCreateRequest,
    ) -> ons_20190214_models.OnsGroupCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_create_with_options_async(request, runtime)

    def ons_group_delete_with_options(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupDeleteResponse().from_map(
            self.do_rpcrequest('OnsGroupDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_group_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupDeleteResponse().from_map(
            await self.do_rpcrequest_async('OnsGroupDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_group_delete(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_group_delete_with_options(request, runtime)

    async def ons_group_delete_async(
        self,
        request: ons_20190214_models.OnsGroupDeleteRequest,
    ) -> ons_20190214_models.OnsGroupDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_delete_with_options_async(request, runtime)

    def ons_group_list_with_options(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupListResponse().from_map(
            self.do_rpcrequest('OnsGroupList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_group_list_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupListResponse().from_map(
            await self.do_rpcrequest_async('OnsGroupList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_group_list(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
    ) -> ons_20190214_models.OnsGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_group_list_with_options(request, runtime)

    async def ons_group_list_async(
        self,
        request: ons_20190214_models.OnsGroupListRequest,
    ) -> ons_20190214_models.OnsGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_list_with_options_async(request, runtime)

    def ons_group_sub_detail_with_options(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupSubDetailResponse().from_map(
            self.do_rpcrequest('OnsGroupSubDetail', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_group_sub_detail_with_options_async(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsGroupSubDetailResponse().from_map(
            await self.do_rpcrequest_async('OnsGroupSubDetail', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_group_sub_detail(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_group_sub_detail_with_options(request, runtime)

    async def ons_group_sub_detail_async(
        self,
        request: ons_20190214_models.OnsGroupSubDetailRequest,
    ) -> ons_20190214_models.OnsGroupSubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_group_sub_detail_with_options_async(request, runtime)

    def ons_instance_base_info_with_options(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceBaseInfoResponse().from_map(
            self.do_rpcrequest('OnsInstanceBaseInfo', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_instance_base_info_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceBaseInfoResponse().from_map(
            await self.do_rpcrequest_async('OnsInstanceBaseInfo', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_instance_base_info(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_base_info_with_options(request, runtime)

    async def ons_instance_base_info_async(
        self,
        request: ons_20190214_models.OnsInstanceBaseInfoRequest,
    ) -> ons_20190214_models.OnsInstanceBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_base_info_with_options_async(request, runtime)

    def ons_instance_create_with_options(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceCreateResponse().from_map(
            self.do_rpcrequest('OnsInstanceCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_instance_create_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceCreateResponse().from_map(
            await self.do_rpcrequest_async('OnsInstanceCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_instance_create(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_create_with_options(request, runtime)

    async def ons_instance_create_async(
        self,
        request: ons_20190214_models.OnsInstanceCreateRequest,
    ) -> ons_20190214_models.OnsInstanceCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_create_with_options_async(request, runtime)

    def ons_instance_delete_with_options(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceDeleteResponse().from_map(
            self.do_rpcrequest('OnsInstanceDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_instance_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceDeleteResponse().from_map(
            await self.do_rpcrequest_async('OnsInstanceDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_instance_delete(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_delete_with_options(request, runtime)

    async def ons_instance_delete_async(
        self,
        request: ons_20190214_models.OnsInstanceDeleteRequest,
    ) -> ons_20190214_models.OnsInstanceDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_delete_with_options_async(request, runtime)

    def ons_instance_in_service_list_with_options(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceInServiceListResponse().from_map(
            self.do_rpcrequest('OnsInstanceInServiceList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_instance_in_service_list_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceInServiceListResponse().from_map(
            await self.do_rpcrequest_async('OnsInstanceInServiceList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_instance_in_service_list(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_in_service_list_with_options(request, runtime)

    async def ons_instance_in_service_list_async(
        self,
        request: ons_20190214_models.OnsInstanceInServiceListRequest,
    ) -> ons_20190214_models.OnsInstanceInServiceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_in_service_list_with_options_async(request, runtime)

    def ons_instance_update_with_options(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceUpdateResponse().from_map(
            self.do_rpcrequest('OnsInstanceUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_instance_update_with_options_async(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsInstanceUpdateResponse().from_map(
            await self.do_rpcrequest_async('OnsInstanceUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_instance_update(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_instance_update_with_options(request, runtime)

    async def ons_instance_update_async(
        self,
        request: ons_20190214_models.OnsInstanceUpdateRequest,
    ) -> ons_20190214_models.OnsInstanceUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_instance_update_with_options_async(request, runtime)

    def ons_message_get_by_key_with_options(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageGetByKeyResponse().from_map(
            self.do_rpcrequest('OnsMessageGetByKey', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_get_by_key_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageGetByKeyResponse().from_map(
            await self.do_rpcrequest_async('OnsMessageGetByKey', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_get_by_key(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_get_by_key_with_options(request, runtime)

    async def ons_message_get_by_key_async(
        self,
        request: ons_20190214_models.OnsMessageGetByKeyRequest,
    ) -> ons_20190214_models.OnsMessageGetByKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_get_by_key_with_options_async(request, runtime)

    def ons_message_get_by_msg_id_with_options(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageGetByMsgIdResponse().from_map(
            self.do_rpcrequest('OnsMessageGetByMsgId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_get_by_msg_id_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageGetByMsgIdResponse().from_map(
            await self.do_rpcrequest_async('OnsMessageGetByMsgId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_get_by_msg_id(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_get_by_msg_id_with_options(request, runtime)

    async def ons_message_get_by_msg_id_async(
        self,
        request: ons_20190214_models.OnsMessageGetByMsgIdRequest,
    ) -> ons_20190214_models.OnsMessageGetByMsgIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_get_by_msg_id_with_options_async(request, runtime)

    def ons_message_page_query_by_topic_with_options(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessagePageQueryByTopicResponse().from_map(
            self.do_rpcrequest('OnsMessagePageQueryByTopic', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_page_query_by_topic_with_options_async(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessagePageQueryByTopicResponse().from_map(
            await self.do_rpcrequest_async('OnsMessagePageQueryByTopic', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_page_query_by_topic(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_page_query_by_topic_with_options(request, runtime)

    async def ons_message_page_query_by_topic_async(
        self,
        request: ons_20190214_models.OnsMessagePageQueryByTopicRequest,
    ) -> ons_20190214_models.OnsMessagePageQueryByTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_page_query_by_topic_with_options_async(request, runtime)

    def ons_message_push_with_options(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessagePushResponse().from_map(
            self.do_rpcrequest('OnsMessagePush', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_push_with_options_async(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessagePushResponse().from_map(
            await self.do_rpcrequest_async('OnsMessagePush', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_push(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_push_with_options(request, runtime)

    async def ons_message_push_async(
        self,
        request: ons_20190214_models.OnsMessagePushRequest,
    ) -> ons_20190214_models.OnsMessagePushResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_push_with_options_async(request, runtime)

    def ons_message_send_with_options(
        self,
        request: ons_20190214_models.OnsMessageSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageSendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageSendResponse().from_map(
            self.do_rpcrequest('OnsMessageSend', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_send_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageSendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageSendResponse().from_map(
            await self.do_rpcrequest_async('OnsMessageSend', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_send(
        self,
        request: ons_20190214_models.OnsMessageSendRequest,
    ) -> ons_20190214_models.OnsMessageSendResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_send_with_options(request, runtime)

    async def ons_message_send_async(
        self,
        request: ons_20190214_models.OnsMessageSendRequest,
    ) -> ons_20190214_models.OnsMessageSendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_send_with_options_async(request, runtime)

    def ons_message_trace_with_options(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageTraceResponse().from_map(
            self.do_rpcrequest('OnsMessageTrace', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_message_trace_with_options_async(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMessageTraceResponse().from_map(
            await self.do_rpcrequest_async('OnsMessageTrace', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_message_trace(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_message_trace_with_options(request, runtime)

    async def ons_message_trace_async(
        self,
        request: ons_20190214_models.OnsMessageTraceRequest,
    ) -> ons_20190214_models.OnsMessageTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_message_trace_with_options_async(request, runtime)

    def ons_mqtt_group_id_create_with_options(
        self,
        request: ons_20190214_models.OnsMqttGroupIdCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdCreateResponse().from_map(
            self.do_rpcrequest('OnsMqttGroupIdCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_group_id_create_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdCreateResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttGroupIdCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_group_id_create(
        self,
        request: ons_20190214_models.OnsMqttGroupIdCreateRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_group_id_create_with_options(request, runtime)

    async def ons_mqtt_group_id_create_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdCreateRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_group_id_create_with_options_async(request, runtime)

    def ons_mqtt_group_id_delete_with_options(
        self,
        request: ons_20190214_models.OnsMqttGroupIdDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdDeleteResponse().from_map(
            self.do_rpcrequest('OnsMqttGroupIdDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_group_id_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdDeleteResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttGroupIdDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_group_id_delete(
        self,
        request: ons_20190214_models.OnsMqttGroupIdDeleteRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_group_id_delete_with_options(request, runtime)

    async def ons_mqtt_group_id_delete_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdDeleteRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_group_id_delete_with_options_async(request, runtime)

    def ons_mqtt_group_id_list_with_options(
        self,
        request: ons_20190214_models.OnsMqttGroupIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdListResponse().from_map(
            self.do_rpcrequest('OnsMqttGroupIdList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_group_id_list_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttGroupIdListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttGroupIdListResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttGroupIdList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_group_id_list(
        self,
        request: ons_20190214_models.OnsMqttGroupIdListRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_group_id_list_with_options(request, runtime)

    async def ons_mqtt_group_id_list_async(
        self,
        request: ons_20190214_models.OnsMqttGroupIdListRequest,
    ) -> ons_20190214_models.OnsMqttGroupIdListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_group_id_list_with_options_async(request, runtime)

    def ons_mqtt_query_client_by_client_id_with_options(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByClientIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByClientIdResponse().from_map(
            self.do_rpcrequest('OnsMqttQueryClientByClientId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_query_client_by_client_id_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByClientIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByClientIdResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttQueryClientByClientId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_query_client_by_client_id(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByClientIdRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_query_client_by_client_id_with_options(request, runtime)

    async def ons_mqtt_query_client_by_client_id_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByClientIdRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_query_client_by_client_id_with_options_async(request, runtime)

    def ons_mqtt_query_client_by_group_id_with_options(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByGroupIdResponse().from_map(
            self.do_rpcrequest('OnsMqttQueryClientByGroupId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_query_client_by_group_id_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByGroupIdResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttQueryClientByGroupId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_query_client_by_group_id(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByGroupIdRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_query_client_by_group_id_with_options(request, runtime)

    async def ons_mqtt_query_client_by_group_id_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByGroupIdRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_query_client_by_group_id_with_options_async(request, runtime)

    def ons_mqtt_query_client_by_topic_with_options(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByTopicResponse().from_map(
            self.do_rpcrequest('OnsMqttQueryClientByTopic', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_query_client_by_topic_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryClientByTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryClientByTopicResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttQueryClientByTopic', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_query_client_by_topic(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByTopicRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_query_client_by_topic_with_options(request, runtime)

    async def ons_mqtt_query_client_by_topic_async(
        self,
        request: ons_20190214_models.OnsMqttQueryClientByTopicRequest,
    ) -> ons_20190214_models.OnsMqttQueryClientByTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_query_client_by_topic_with_options_async(request, runtime)

    def ons_mqtt_query_history_online_with_options(
        self,
        request: ons_20190214_models.OnsMqttQueryHistoryOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryHistoryOnlineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryHistoryOnlineResponse().from_map(
            self.do_rpcrequest('OnsMqttQueryHistoryOnline', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_query_history_online_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttQueryHistoryOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryHistoryOnlineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryHistoryOnlineResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttQueryHistoryOnline', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_query_history_online(
        self,
        request: ons_20190214_models.OnsMqttQueryHistoryOnlineRequest,
    ) -> ons_20190214_models.OnsMqttQueryHistoryOnlineResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_query_history_online_with_options(request, runtime)

    async def ons_mqtt_query_history_online_async(
        self,
        request: ons_20190214_models.OnsMqttQueryHistoryOnlineRequest,
    ) -> ons_20190214_models.OnsMqttQueryHistoryOnlineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_query_history_online_with_options_async(request, runtime)

    def ons_mqtt_query_msg_trans_trend_with_options(
        self,
        request: ons_20190214_models.OnsMqttQueryMsgTransTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryMsgTransTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryMsgTransTrendResponse().from_map(
            self.do_rpcrequest('OnsMqttQueryMsgTransTrend', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_mqtt_query_msg_trans_trend_with_options_async(
        self,
        request: ons_20190214_models.OnsMqttQueryMsgTransTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsMqttQueryMsgTransTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsMqttQueryMsgTransTrendResponse().from_map(
            await self.do_rpcrequest_async('OnsMqttQueryMsgTransTrend', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_mqtt_query_msg_trans_trend(
        self,
        request: ons_20190214_models.OnsMqttQueryMsgTransTrendRequest,
    ) -> ons_20190214_models.OnsMqttQueryMsgTransTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_mqtt_query_msg_trans_trend_with_options(request, runtime)

    async def ons_mqtt_query_msg_trans_trend_async(
        self,
        request: ons_20190214_models.OnsMqttQueryMsgTransTrendRequest,
    ) -> ons_20190214_models.OnsMqttQueryMsgTransTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_mqtt_query_msg_trans_trend_with_options_async(request, runtime)

    def ons_region_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsRegionListResponse:
        req = open_api_models.OpenApiRequest()
        return ons_20190214_models.OnsRegionListResponse().from_map(
            self.do_rpcrequest('OnsRegionList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_region_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsRegionListResponse:
        req = open_api_models.OpenApiRequest()
        return ons_20190214_models.OnsRegionListResponse().from_map(
            await self.do_rpcrequest_async('OnsRegionList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_region_list(self) -> ons_20190214_models.OnsRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_region_list_with_options(runtime)

    async def ons_region_list_async(self) -> ons_20190214_models.OnsRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_region_list_with_options_async(runtime)

    def ons_topic_create_with_options(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicCreateResponse().from_map(
            self.do_rpcrequest('OnsTopicCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_create_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicCreateResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_create(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_create_with_options(request, runtime)

    async def ons_topic_create_async(
        self,
        request: ons_20190214_models.OnsTopicCreateRequest,
    ) -> ons_20190214_models.OnsTopicCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_create_with_options_async(request, runtime)

    def ons_topic_delete_with_options(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicDeleteResponse().from_map(
            self.do_rpcrequest('OnsTopicDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicDeleteResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_delete(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_delete_with_options(request, runtime)

    async def ons_topic_delete_async(
        self,
        request: ons_20190214_models.OnsTopicDeleteRequest,
    ) -> ons_20190214_models.OnsTopicDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_delete_with_options_async(request, runtime)

    def ons_topic_list_with_options(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicListResponse().from_map(
            self.do_rpcrequest('OnsTopicList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_list_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicListResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicList', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_list(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
    ) -> ons_20190214_models.OnsTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_list_with_options(request, runtime)

    async def ons_topic_list_async(
        self,
        request: ons_20190214_models.OnsTopicListRequest,
    ) -> ons_20190214_models.OnsTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_list_with_options_async(request, runtime)

    def ons_topic_status_with_options(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicStatusResponse().from_map(
            self.do_rpcrequest('OnsTopicStatus', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_status_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicStatusResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicStatus', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_status(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_status_with_options(request, runtime)

    async def ons_topic_status_async(
        self,
        request: ons_20190214_models.OnsTopicStatusRequest,
    ) -> ons_20190214_models.OnsTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_status_with_options_async(request, runtime)

    def ons_topic_sub_detail_with_options(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicSubDetailResponse().from_map(
            self.do_rpcrequest('OnsTopicSubDetail', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_sub_detail_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicSubDetailResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicSubDetail', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_sub_detail(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_sub_detail_with_options(request, runtime)

    async def ons_topic_sub_detail_async(
        self,
        request: ons_20190214_models.OnsTopicSubDetailRequest,
    ) -> ons_20190214_models.OnsTopicSubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_sub_detail_with_options_async(request, runtime)

    def ons_topic_update_with_options(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicUpdateResponse().from_map(
            self.do_rpcrequest('OnsTopicUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_topic_update_with_options_async(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTopicUpdateResponse().from_map(
            await self.do_rpcrequest_async('OnsTopicUpdate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_topic_update(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_topic_update_with_options(request, runtime)

    async def ons_topic_update_async(
        self,
        request: ons_20190214_models.OnsTopicUpdateRequest,
    ) -> ons_20190214_models.OnsTopicUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_topic_update_with_options_async(request, runtime)

    def ons_trace_get_result_with_options(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceGetResultResponse().from_map(
            self.do_rpcrequest('OnsTraceGetResult', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_trace_get_result_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceGetResultResponse().from_map(
            await self.do_rpcrequest_async('OnsTraceGetResult', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_trace_get_result(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_get_result_with_options(request, runtime)

    async def ons_trace_get_result_async(
        self,
        request: ons_20190214_models.OnsTraceGetResultRequest,
    ) -> ons_20190214_models.OnsTraceGetResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_get_result_with_options_async(request, runtime)

    def ons_trace_query_by_msg_id_with_options(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceQueryByMsgIdResponse().from_map(
            self.do_rpcrequest('OnsTraceQueryByMsgId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_trace_query_by_msg_id_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceQueryByMsgIdResponse().from_map(
            await self.do_rpcrequest_async('OnsTraceQueryByMsgId', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_trace_query_by_msg_id(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_query_by_msg_id_with_options(request, runtime)

    async def ons_trace_query_by_msg_id_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgIdRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_query_by_msg_id_with_options_async(request, runtime)

    def ons_trace_query_by_msg_key_with_options(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceQueryByMsgKeyResponse().from_map(
            self.do_rpcrequest('OnsTraceQueryByMsgKey', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_trace_query_by_msg_key_with_options_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTraceQueryByMsgKeyResponse().from_map(
            await self.do_rpcrequest_async('OnsTraceQueryByMsgKey', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_trace_query_by_msg_key(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_trace_query_by_msg_key_with_options(request, runtime)

    async def ons_trace_query_by_msg_key_async(
        self,
        request: ons_20190214_models.OnsTraceQueryByMsgKeyRequest,
    ) -> ons_20190214_models.OnsTraceQueryByMsgKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_trace_query_by_msg_key_with_options_async(request, runtime)

    def ons_trend_group_output_tps_with_options(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTrendGroupOutputTpsResponse().from_map(
            self.do_rpcrequest('OnsTrendGroupOutputTps', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_trend_group_output_tps_with_options_async(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTrendGroupOutputTpsResponse().from_map(
            await self.do_rpcrequest_async('OnsTrendGroupOutputTps', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_trend_group_output_tps(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_trend_group_output_tps_with_options(request, runtime)

    async def ons_trend_group_output_tps_async(
        self,
        request: ons_20190214_models.OnsTrendGroupOutputTpsRequest,
    ) -> ons_20190214_models.OnsTrendGroupOutputTpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_trend_group_output_tps_with_options_async(request, runtime)

    def ons_trend_topic_input_tps_with_options(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTrendTopicInputTpsResponse().from_map(
            self.do_rpcrequest('OnsTrendTopicInputTps', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_trend_topic_input_tps_with_options_async(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsTrendTopicInputTpsResponse().from_map(
            await self.do_rpcrequest_async('OnsTrendTopicInputTps', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_trend_topic_input_tps(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_trend_topic_input_tps_with_options(request, runtime)

    async def ons_trend_topic_input_tps_async(
        self,
        request: ons_20190214_models.OnsTrendTopicInputTpsRequest,
    ) -> ons_20190214_models.OnsTrendTopicInputTpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_trend_topic_input_tps_with_options_async(request, runtime)

    def ons_warn_create_with_options(
        self,
        request: ons_20190214_models.OnsWarnCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsWarnCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsWarnCreateResponse().from_map(
            self.do_rpcrequest('OnsWarnCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_warn_create_with_options_async(
        self,
        request: ons_20190214_models.OnsWarnCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsWarnCreateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsWarnCreateResponse().from_map(
            await self.do_rpcrequest_async('OnsWarnCreate', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_warn_create(
        self,
        request: ons_20190214_models.OnsWarnCreateRequest,
    ) -> ons_20190214_models.OnsWarnCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_warn_create_with_options(request, runtime)

    async def ons_warn_create_async(
        self,
        request: ons_20190214_models.OnsWarnCreateRequest,
    ) -> ons_20190214_models.OnsWarnCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_warn_create_with_options_async(request, runtime)

    def ons_warn_delete_with_options(
        self,
        request: ons_20190214_models.OnsWarnDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsWarnDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsWarnDeleteResponse().from_map(
            self.do_rpcrequest('OnsWarnDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ons_warn_delete_with_options_async(
        self,
        request: ons_20190214_models.OnsWarnDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OnsWarnDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.OnsWarnDeleteResponse().from_map(
            await self.do_rpcrequest_async('OnsWarnDelete', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ons_warn_delete(
        self,
        request: ons_20190214_models.OnsWarnDeleteRequest,
    ) -> ons_20190214_models.OnsWarnDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.ons_warn_delete_with_options(request, runtime)

    async def ons_warn_delete_async(
        self,
        request: ons_20190214_models.OnsWarnDeleteRequest,
    ) -> ons_20190214_models.OnsWarnDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ons_warn_delete_with_options_async(request, runtime)

    def open_ons_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OpenOnsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return ons_20190214_models.OpenOnsServiceResponse().from_map(
            self.do_rpcrequest('OpenOnsService', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_ons_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.OpenOnsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return ons_20190214_models.OpenOnsServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenOnsService', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_ons_service(self) -> ons_20190214_models.OpenOnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_ons_service_with_options(runtime)

    async def open_ons_service_async(self) -> ons_20190214_models.OpenOnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_ons_service_with_options_async(runtime)

    def tag_resources_with_options(
        self,
        request: ons_20190214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ons_20190214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ons_20190214_models.TagResourcesRequest,
    ) -> ons_20190214_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ons_20190214_models.TagResourcesRequest,
    ) -> ons_20190214_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_20190214_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_20190214_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-02-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
    ) -> ons_20190214_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ons_20190214_models.UntagResourcesRequest,
    ) -> ons_20190214_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
