# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_retailadvqa20230417 import models as retailadvqa_20230417_models
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
        self._endpoint = self.get_endpoint('retailadvqa', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_member_basic_info_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.AddMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.AddMemberBasicInfoResponse:
        """
        @summary 开放平台同步会员基础信息
        
        @param tmp_req: AddMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.AddMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.AddMemberBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_member_basic_info_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.AddMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.AddMemberBasicInfoResponse:
        """
        @summary 开放平台同步会员基础信息
        
        @param tmp_req: AddMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.AddMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.AddMemberBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_member_basic_info(
        self,
        request: retailadvqa_20230417_models.AddMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.AddMemberBasicInfoResponse:
        """
        @summary 开放平台同步会员基础信息
        
        @param request: AddMemberBasicInfoRequest
        @return: AddMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_member_basic_info_with_options(request, runtime)

    async def add_member_basic_info_async(
        self,
        request: retailadvqa_20230417_models.AddMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.AddMemberBasicInfoResponse:
        """
        @summary 开放平台同步会员基础信息
        
        @param request: AddMemberBasicInfoRequest
        @return: AddMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_member_basic_info_with_options_async(request, runtime)

    def batch_save_order_pop_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.BatchSaveOrderPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.BatchSaveOrderPopResponse:
        """
        @summary 批量保存订单信息
        
        @param tmp_req: BatchSaveOrderPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSaveOrderPopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.BatchSaveOrderPopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.orders):
            request.orders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.orders, 'Orders', 'json')
        query = {}
        if not UtilClient.is_unset(request.orders_shrink):
            query['Orders'] = request.orders_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSaveOrderPop',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.BatchSaveOrderPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_save_order_pop_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.BatchSaveOrderPopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.BatchSaveOrderPopResponse:
        """
        @summary 批量保存订单信息
        
        @param tmp_req: BatchSaveOrderPopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSaveOrderPopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.BatchSaveOrderPopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.orders):
            request.orders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.orders, 'Orders', 'json')
        query = {}
        if not UtilClient.is_unset(request.orders_shrink):
            query['Orders'] = request.orders_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSaveOrderPop',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.BatchSaveOrderPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_save_order_pop(
        self,
        request: retailadvqa_20230417_models.BatchSaveOrderPopRequest,
    ) -> retailadvqa_20230417_models.BatchSaveOrderPopResponse:
        """
        @summary 批量保存订单信息
        
        @param request: BatchSaveOrderPopRequest
        @return: BatchSaveOrderPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_save_order_pop_with_options(request, runtime)

    async def batch_save_order_pop_async(
        self,
        request: retailadvqa_20230417_models.BatchSaveOrderPopRequest,
    ) -> retailadvqa_20230417_models.BatchSaveOrderPopResponse:
        """
        @summary 批量保存订单信息
        
        @param request: BatchSaveOrderPopRequest
        @return: BatchSaveOrderPopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_save_order_pop_with_options_async(request, runtime)

    def calculate_member_level_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.CalculateMemberLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.CalculateMemberLevelResponse:
        """
        @summary 会员等级初始化
        
        @param tmp_req: CalculateMemberLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalculateMemberLevelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.CalculateMemberLevelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['Body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CalculateMemberLevel',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.CalculateMemberLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def calculate_member_level_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.CalculateMemberLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.CalculateMemberLevelResponse:
        """
        @summary 会员等级初始化
        
        @param tmp_req: CalculateMemberLevelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalculateMemberLevelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.CalculateMemberLevelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['Body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CalculateMemberLevel',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.CalculateMemberLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def calculate_member_level(
        self,
        request: retailadvqa_20230417_models.CalculateMemberLevelRequest,
    ) -> retailadvqa_20230417_models.CalculateMemberLevelResponse:
        """
        @summary 会员等级初始化
        
        @param request: CalculateMemberLevelRequest
        @return: CalculateMemberLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.calculate_member_level_with_options(request, runtime)

    async def calculate_member_level_async(
        self,
        request: retailadvqa_20230417_models.CalculateMemberLevelRequest,
    ) -> retailadvqa_20230417_models.CalculateMemberLevelResponse:
        """
        @summary 会员等级初始化
        
        @param request: CalculateMemberLevelRequest
        @return: CalculateMemberLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.calculate_member_level_with_options_async(request, runtime)

    def edit_member_basic_info_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.EditMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.EditMemberBasicInfoResponse:
        """
        @summary 会员信息编辑API
        
        @param tmp_req: EditMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.EditMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['Body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.EditMemberBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_member_basic_info_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.EditMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.EditMemberBasicInfoResponse:
        """
        @summary 会员信息编辑API
        
        @param tmp_req: EditMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.EditMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['Body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.EditMemberBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_member_basic_info(
        self,
        request: retailadvqa_20230417_models.EditMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.EditMemberBasicInfoResponse:
        """
        @summary 会员信息编辑API
        
        @param request: EditMemberBasicInfoRequest
        @return: EditMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_member_basic_info_with_options(request, runtime)

    async def edit_member_basic_info_async(
        self,
        request: retailadvqa_20230417_models.EditMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.EditMemberBasicInfoResponse:
        """
        @summary 会员信息编辑API
        
        @param request: EditMemberBasicInfoRequest
        @return: EditMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_member_basic_info_with_options_async(request, runtime)

    def member_account_detail_page_query_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.MemberAccountDetailPageQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse:
        """
        @summary 开放平台会员积分明细查询
        
        @param tmp_req: MemberAccountDetailPageQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MemberAccountDetailPageQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.MemberAccountDetailPageQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MemberAccountDetailPageQuery',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def member_account_detail_page_query_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.MemberAccountDetailPageQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse:
        """
        @summary 开放平台会员积分明细查询
        
        @param tmp_req: MemberAccountDetailPageQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MemberAccountDetailPageQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.MemberAccountDetailPageQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MemberAccountDetailPageQuery',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def member_account_detail_page_query(
        self,
        request: retailadvqa_20230417_models.MemberAccountDetailPageQueryRequest,
    ) -> retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse:
        """
        @summary 开放平台会员积分明细查询
        
        @param request: MemberAccountDetailPageQueryRequest
        @return: MemberAccountDetailPageQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.member_account_detail_page_query_with_options(request, runtime)

    async def member_account_detail_page_query_async(
        self,
        request: retailadvqa_20230417_models.MemberAccountDetailPageQueryRequest,
    ) -> retailadvqa_20230417_models.MemberAccountDetailPageQueryResponse:
        """
        @summary 开放平台会员积分明细查询
        
        @param request: MemberAccountDetailPageQueryRequest
        @return: MemberAccountDetailPageQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.member_account_detail_page_query_with_options_async(request, runtime)

    def member_point_change_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.MemberPointChangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.MemberPointChangeResponse:
        """
        @summary 会员积分变更
        
        @param tmp_req: MemberPointChangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MemberPointChangeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.MemberPointChangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MemberPointChange',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.MemberPointChangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def member_point_change_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.MemberPointChangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.MemberPointChangeResponse:
        """
        @summary 会员积分变更
        
        @param tmp_req: MemberPointChangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MemberPointChangeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.MemberPointChangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MemberPointChange',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.MemberPointChangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def member_point_change(
        self,
        request: retailadvqa_20230417_models.MemberPointChangeRequest,
    ) -> retailadvqa_20230417_models.MemberPointChangeResponse:
        """
        @summary 会员积分变更
        
        @param request: MemberPointChangeRequest
        @return: MemberPointChangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.member_point_change_with_options(request, runtime)

    async def member_point_change_async(
        self,
        request: retailadvqa_20230417_models.MemberPointChangeRequest,
    ) -> retailadvqa_20230417_models.MemberPointChangeResponse:
        """
        @summary 会员积分变更
        
        @param request: MemberPointChangeRequest
        @return: MemberPointChangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.member_point_change_with_options_async(request, runtime)

    def query_member_basic_info_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.QueryMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.QueryMemberBasicInfoResponse:
        """
        @summary 查询会员基础信息
        
        @param tmp_req: QueryMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.QueryMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.QueryMemberBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_member_basic_info_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.QueryMemberBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.QueryMemberBasicInfoResponse:
        """
        @summary 查询会员基础信息
        
        @param tmp_req: QueryMemberBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMemberBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.QueryMemberBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMemberBasicInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.QueryMemberBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_member_basic_info(
        self,
        request: retailadvqa_20230417_models.QueryMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.QueryMemberBasicInfoResponse:
        """
        @summary 查询会员基础信息
        
        @param request: QueryMemberBasicInfoRequest
        @return: QueryMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_member_basic_info_with_options(request, runtime)

    async def query_member_basic_info_async(
        self,
        request: retailadvqa_20230417_models.QueryMemberBasicInfoRequest,
    ) -> retailadvqa_20230417_models.QueryMemberBasicInfoResponse:
        """
        @summary 查询会员基础信息
        
        @param request: QueryMemberBasicInfoRequest
        @return: QueryMemberBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_member_basic_info_with_options_async(request, runtime)

    def sync_card_info_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.SyncCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.SyncCardInfoResponse:
        """
        @summary 卡券信息同步
        
        @param tmp_req: SyncCardInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncCardInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.SyncCardInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncCardInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.SyncCardInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_card_info_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.SyncCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.SyncCardInfoResponse:
        """
        @summary 卡券信息同步
        
        @param tmp_req: SyncCardInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncCardInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.SyncCardInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncCardInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.SyncCardInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_card_info(
        self,
        request: retailadvqa_20230417_models.SyncCardInfoRequest,
    ) -> retailadvqa_20230417_models.SyncCardInfoResponse:
        """
        @summary 卡券信息同步
        
        @param request: SyncCardInfoRequest
        @return: SyncCardInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_card_info_with_options(request, runtime)

    async def sync_card_info_async(
        self,
        request: retailadvqa_20230417_models.SyncCardInfoRequest,
    ) -> retailadvqa_20230417_models.SyncCardInfoResponse:
        """
        @summary 卡券信息同步
        
        @param request: SyncCardInfoRequest
        @return: SyncCardInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_card_info_with_options_async(request, runtime)

    def sync_member_behavior_info_with_options(
        self,
        tmp_req: retailadvqa_20230417_models.SyncMemberBehaviorInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse:
        """
        @summary 开放平台会员行为信息同步
        
        @param tmp_req: SyncMemberBehaviorInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncMemberBehaviorInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.SyncMemberBehaviorInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncMemberBehaviorInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_member_behavior_info_with_options_async(
        self,
        tmp_req: retailadvqa_20230417_models.SyncMemberBehaviorInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse:
        """
        @summary 开放平台会员行为信息同步
        
        @param tmp_req: SyncMemberBehaviorInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncMemberBehaviorInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = retailadvqa_20230417_models.SyncMemberBehaviorInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncMemberBehaviorInfo',
            version='2023-04-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_member_behavior_info(
        self,
        request: retailadvqa_20230417_models.SyncMemberBehaviorInfoRequest,
    ) -> retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse:
        """
        @summary 开放平台会员行为信息同步
        
        @param request: SyncMemberBehaviorInfoRequest
        @return: SyncMemberBehaviorInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_member_behavior_info_with_options(request, runtime)

    async def sync_member_behavior_info_async(
        self,
        request: retailadvqa_20230417_models.SyncMemberBehaviorInfoRequest,
    ) -> retailadvqa_20230417_models.SyncMemberBehaviorInfoResponse:
        """
        @summary 开放平台会员行为信息同步
        
        @param request: SyncMemberBehaviorInfoRequest
        @return: SyncMemberBehaviorInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_member_behavior_info_with_options_async(request, runtime)
