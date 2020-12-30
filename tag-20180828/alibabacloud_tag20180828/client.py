# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tag20180828 import models as tag_20180828_models
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
            'cn-qingdao': 'tag.aliyuncs.com',
            'cn-beijing': 'tag.aliyuncs.com',
            'cn-hangzhou': 'tag.aliyuncs.com',
            'cn-shanghai': 'tag.aliyuncs.com',
            'cn-shenzhen': 'tag.aliyuncs.com',
            'cn-hongkong': 'tag.aliyuncs.com',
            'ap-southeast-1': 'tag.aliyuncs.com',
            'us-west-1': 'tag.aliyuncs.com',
            'us-east-1': 'tag.aliyuncs.com',
            'cn-hangzhou-finance': 'tag.aliyuncs.com',
            'cn-shanghai-finance-1': 'tag.aliyuncs.com',
            'ap-northeast-2-pop': 'tag.aliyuncs.com',
            'cn-beijing-finance-1': 'tag.aliyuncs.com',
            'cn-beijing-finance-pop': 'tag.aliyuncs.com',
            'cn-beijing-gov-1': 'tag.aliyuncs.com',
            'cn-beijing-nu16-b01': 'tag.aliyuncs.com',
            'cn-edge-1': 'tag.aliyuncs.com',
            'cn-fujian': 'tag.aliyuncs.com',
            'cn-haidian-cm12-c01': 'tag.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'tag.aliyuncs.com',
            'cn-hangzhou-test-306': 'tag.aliyuncs.com',
            'cn-hongkong-finance-pop': 'tag.aliyuncs.com',
            'cn-qingdao-nebula': 'tag.aliyuncs.com',
            'cn-shanghai-et15-b01': 'tag.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tag.aliyuncs.com',
            'cn-shanghai-inner': 'tag.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'tag.aliyuncs.com',
            'cn-shenzhen-finance-1': 'tag.aliyuncs.com',
            'cn-shenzhen-inner': 'tag.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'tag.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'tag.aliyuncs.com',
            'cn-wuhan': 'tag.aliyuncs.com',
            'cn-yushanfang': 'tag.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'tag.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'tag.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'tag.aliyuncs.com',
            'eu-west-1-oxs': 'tag.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'tag.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_tag_keys_with_options(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: tag_20180828_models.ListTagKeysRequest,
    ) -> tag_20180828_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: tag_20180828_models.ListTagResourcesRequest,
    ) -> tag_20180828_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagValuesResponse().from_map(
            self.do_rpcrequest('ListTagValues', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.ListTagValuesResponse().from_map(
            await self.do_rpcrequest_async('ListTagValues', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: tag_20180828_models.ListTagValuesRequest,
    ) -> tag_20180828_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: tag_20180828_models.TagResourcesRequest,
    ) -> tag_20180828_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tag_20180828_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return tag_20180828_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2018-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: tag_20180828_models.UntagResourcesRequest,
    ) -> tag_20180828_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
