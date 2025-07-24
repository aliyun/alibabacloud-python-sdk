# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eduaiservice20231218 import models as eduaiservice_20231218_models
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
        self._endpoint = self.get_endpoint('eduaiservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_org_lab_record_list_with_options(
        self,
        request: eduaiservice_20231218_models.QueryOrgLabRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eduaiservice_20231218_models.QueryOrgLabRecordListResponse:
        """
        @summary 查询指定学生实验记录
        
        @param request: QueryOrgLabRecordListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrgLabRecordListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.lab_id):
            query['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrgLabRecordList',
            version='2023-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eduaiservice_20231218_models.QueryOrgLabRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_org_lab_record_list_with_options_async(
        self,
        request: eduaiservice_20231218_models.QueryOrgLabRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eduaiservice_20231218_models.QueryOrgLabRecordListResponse:
        """
        @summary 查询指定学生实验记录
        
        @param request: QueryOrgLabRecordListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrgLabRecordListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.lab_id):
            query['LabId'] = request.lab_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrgLabRecordList',
            version='2023-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eduaiservice_20231218_models.QueryOrgLabRecordListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_org_lab_record_list(
        self,
        request: eduaiservice_20231218_models.QueryOrgLabRecordListRequest,
    ) -> eduaiservice_20231218_models.QueryOrgLabRecordListResponse:
        """
        @summary 查询指定学生实验记录
        
        @param request: QueryOrgLabRecordListRequest
        @return: QueryOrgLabRecordListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_org_lab_record_list_with_options(request, runtime)

    async def query_org_lab_record_list_async(
        self,
        request: eduaiservice_20231218_models.QueryOrgLabRecordListRequest,
    ) -> eduaiservice_20231218_models.QueryOrgLabRecordListResponse:
        """
        @summary 查询指定学生实验记录
        
        @param request: QueryOrgLabRecordListRequest
        @return: QueryOrgLabRecordListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_org_lab_record_list_with_options_async(request, runtime)
