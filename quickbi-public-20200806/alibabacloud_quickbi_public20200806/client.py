# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quickbi_public20200806 import models as quickbi_public_20200806_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-hangzhou': 'quickbi-public-share.aliyuncs.com',
            'cn-hongkong': 'quickbi-public-share.aliyuncs.com',
            'ap-southeast-1': 'quickbi-public-share.aliyuncs.com',
            'ap-southeast-3': 'quickbi-public-share.aliyuncs.com',
            'eu-central-1': 'quickbi-public-share.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('quickbi-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_dataset_detail_info_with_options(
        self,
        request: quickbi_public_20200806_models.QueryDatasetDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200806_models.QueryDatasetDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDatasetDetailInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200806_models.QueryDatasetDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_detail_info_with_options_async(
        self,
        request: quickbi_public_20200806_models.QueryDatasetDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200806_models.QueryDatasetDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDatasetDetailInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200806_models.QueryDatasetDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_detail_info(
        self,
        request: quickbi_public_20200806_models.QueryDatasetDetailInfoRequest,
    ) -> quickbi_public_20200806_models.QueryDatasetDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_detail_info_with_options(request, runtime)

    async def query_dataset_detail_info_async(
        self,
        request: quickbi_public_20200806_models.QueryDatasetDetailInfoRequest,
    ) -> quickbi_public_20200806_models.QueryDatasetDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_detail_info_with_options_async(request, runtime)

    def query_dataset_list_with_options(
        self,
        request: quickbi_public_20200806_models.QueryDatasetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200806_models.QueryDatasetListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['WorkspaceId'] = request.workspace_id
        query['DirectoryId'] = request.directory_id
        query['WithChildren'] = request.with_children
        query['Keyword'] = request.keyword
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDatasetList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200806_models.QueryDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_list_with_options_async(
        self,
        request: quickbi_public_20200806_models.QueryDatasetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200806_models.QueryDatasetListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['WorkspaceId'] = request.workspace_id
        query['DirectoryId'] = request.directory_id
        query['WithChildren'] = request.with_children
        query['Keyword'] = request.keyword
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDatasetList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200806_models.QueryDatasetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_list(
        self,
        request: quickbi_public_20200806_models.QueryDatasetListRequest,
    ) -> quickbi_public_20200806_models.QueryDatasetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_list_with_options(request, runtime)

    async def query_dataset_list_async(
        self,
        request: quickbi_public_20200806_models.QueryDatasetListRequest,
    ) -> quickbi_public_20200806_models.QueryDatasetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_list_with_options_async(request, runtime)
