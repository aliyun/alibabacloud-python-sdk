# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_buss20160718 import models as buss_20160718_models
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
        self._endpoint = self.get_endpoint('buss', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_removing_punish_with_options(
        self,
        request: buss_20160718_models.ApplyRemovingPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.ApplyRemovingPunishResponse:
        """
        @summary 自助解锁(安全管控控制台)
        
        @param request: ApplyRemovingPunishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyRemovingPunishResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyRemovingPunish',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.ApplyRemovingPunishResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_removing_punish_with_options_async(
        self,
        request: buss_20160718_models.ApplyRemovingPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.ApplyRemovingPunishResponse:
        """
        @summary 自助解锁(安全管控控制台)
        
        @param request: ApplyRemovingPunishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyRemovingPunishResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyRemovingPunish',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.ApplyRemovingPunishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_removing_punish(
        self,
        request: buss_20160718_models.ApplyRemovingPunishRequest,
    ) -> buss_20160718_models.ApplyRemovingPunishResponse:
        """
        @summary 自助解锁(安全管控控制台)
        
        @param request: ApplyRemovingPunishRequest
        @return: ApplyRemovingPunishResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_removing_punish_with_options(request, runtime)

    async def apply_removing_punish_async(
        self,
        request: buss_20160718_models.ApplyRemovingPunishRequest,
    ) -> buss_20160718_models.ApplyRemovingPunishResponse:
        """
        @summary 自助解锁(安全管控控制台)
        
        @param request: ApplyRemovingPunishRequest
        @return: ApplyRemovingPunishResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_removing_punish_with_options_async(request, runtime)

    def batch_add_punish_list_with_options(
        self,
        request: buss_20160718_models.BatchAddPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.BatchAddPunishListResponse:
        """
        @param request: BatchAddPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.BatchAddPunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_punish_list_with_options_async(
        self,
        request: buss_20160718_models.BatchAddPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.BatchAddPunishListResponse:
        """
        @param request: BatchAddPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.BatchAddPunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_punish_list(
        self,
        request: buss_20160718_models.BatchAddPunishListRequest,
    ) -> buss_20160718_models.BatchAddPunishListResponse:
        """
        @param request: BatchAddPunishListRequest
        @return: BatchAddPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_add_punish_list_with_options(request, runtime)

    async def batch_add_punish_list_async(
        self,
        request: buss_20160718_models.BatchAddPunishListRequest,
    ) -> buss_20160718_models.BatchAddPunishListResponse:
        """
        @param request: BatchAddPunishListRequest
        @return: BatchAddPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_punish_list_with_options_async(request, runtime)

    def batch_del_punish_list_with_options(
        self,
        request: buss_20160718_models.BatchDelPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.BatchDelPunishListResponse:
        """
        @param request: BatchDelPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDelPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDelPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.BatchDelPunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_del_punish_list_with_options_async(
        self,
        request: buss_20160718_models.BatchDelPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.BatchDelPunishListResponse:
        """
        @param request: BatchDelPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDelPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDelPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.BatchDelPunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_del_punish_list(
        self,
        request: buss_20160718_models.BatchDelPunishListRequest,
    ) -> buss_20160718_models.BatchDelPunishListResponse:
        """
        @param request: BatchDelPunishListRequest
        @return: BatchDelPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_del_punish_list_with_options(request, runtime)

    async def batch_del_punish_list_async(
        self,
        request: buss_20160718_models.BatchDelPunishListRequest,
    ) -> buss_20160718_models.BatchDelPunishListResponse:
        """
        @param request: BatchDelPunishListRequest
        @return: BatchDelPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_del_punish_list_with_options_async(request, runtime)

    def del_punish_white_for_idcisp_with_options(
        self,
        request: buss_20160718_models.DelPunishWhiteForIdcispRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.DelPunishWhiteForIdcispResponse:
        """
        @summary 删除idcisp的白名单
        
        @param request: DelPunishWhiteForIdcispRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelPunishWhiteForIdcispResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelPunishWhiteForIdcisp',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.DelPunishWhiteForIdcispResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_punish_white_for_idcisp_with_options_async(
        self,
        request: buss_20160718_models.DelPunishWhiteForIdcispRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.DelPunishWhiteForIdcispResponse:
        """
        @summary 删除idcisp的白名单
        
        @param request: DelPunishWhiteForIdcispRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelPunishWhiteForIdcispResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_list_requests):
            query['PunishListRequests'] = request.punish_list_requests
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelPunishWhiteForIdcisp',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.DelPunishWhiteForIdcispResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_punish_white_for_idcisp(
        self,
        request: buss_20160718_models.DelPunishWhiteForIdcispRequest,
    ) -> buss_20160718_models.DelPunishWhiteForIdcispResponse:
        """
        @summary 删除idcisp的白名单
        
        @param request: DelPunishWhiteForIdcispRequest
        @return: DelPunishWhiteForIdcispResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.del_punish_white_for_idcisp_with_options(request, runtime)

    async def del_punish_white_for_idcisp_async(
        self,
        request: buss_20160718_models.DelPunishWhiteForIdcispRequest,
    ) -> buss_20160718_models.DelPunishWhiteForIdcispResponse:
        """
        @summary 删除idcisp的白名单
        
        @param request: DelPunishWhiteForIdcispRequest
        @return: DelPunishWhiteForIdcispResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.del_punish_white_for_idcisp_with_options_async(request, runtime)

    def find_full_punish_white_list_with_options(
        self,
        request: buss_20160718_models.FindFullPunishWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindFullPunishWhiteListResponse:
        """
        @param request: FindFullPunishWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindFullPunishWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindFullPunishWhiteList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindFullPunishWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_full_punish_white_list_with_options_async(
        self,
        request: buss_20160718_models.FindFullPunishWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindFullPunishWhiteListResponse:
        """
        @param request: FindFullPunishWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindFullPunishWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindFullPunishWhiteList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindFullPunishWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_full_punish_white_list(
        self,
        request: buss_20160718_models.FindFullPunishWhiteListRequest,
    ) -> buss_20160718_models.FindFullPunishWhiteListResponse:
        """
        @param request: FindFullPunishWhiteListRequest
        @return: FindFullPunishWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_full_punish_white_list_with_options(request, runtime)

    async def find_full_punish_white_list_async(
        self,
        request: buss_20160718_models.FindFullPunishWhiteListRequest,
    ) -> buss_20160718_models.FindFullPunishWhiteListResponse:
        """
        @param request: FindFullPunishWhiteListRequest
        @return: FindFullPunishWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_full_punish_white_list_with_options_async(request, runtime)

    def find_punish_request_by_ext_id_with_options(
        self,
        request: buss_20160718_models.FindPunishRequestByExtIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishRequestByExtIdResponse:
        """
        @param request: FindPunishRequestByExtIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishRequestByExtIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishRequestByExtId',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishRequestByExtIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_punish_request_by_ext_id_with_options_async(
        self,
        request: buss_20160718_models.FindPunishRequestByExtIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishRequestByExtIdResponse:
        """
        @param request: FindPunishRequestByExtIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishRequestByExtIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishRequestByExtId',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishRequestByExtIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_punish_request_by_ext_id(
        self,
        request: buss_20160718_models.FindPunishRequestByExtIdRequest,
    ) -> buss_20160718_models.FindPunishRequestByExtIdResponse:
        """
        @param request: FindPunishRequestByExtIdRequest
        @return: FindPunishRequestByExtIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_punish_request_by_ext_id_with_options(request, runtime)

    async def find_punish_request_by_ext_id_async(
        self,
        request: buss_20160718_models.FindPunishRequestByExtIdRequest,
    ) -> buss_20160718_models.FindPunishRequestByExtIdResponse:
        """
        @param request: FindPunishRequestByExtIdRequest
        @return: FindPunishRequestByExtIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_punish_request_by_ext_id_with_options_async(request, runtime)

    def find_punish_request_by_id_with_options(
        self,
        request: buss_20160718_models.FindPunishRequestByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishRequestByIdResponse:
        """
        @param request: FindPunishRequestByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishRequestByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishRequestById',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishRequestByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_punish_request_by_id_with_options_async(
        self,
        request: buss_20160718_models.FindPunishRequestByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishRequestByIdResponse:
        """
        @param request: FindPunishRequestByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishRequestByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishRequestById',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishRequestByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_punish_request_by_id(
        self,
        request: buss_20160718_models.FindPunishRequestByIdRequest,
    ) -> buss_20160718_models.FindPunishRequestByIdResponse:
        """
        @param request: FindPunishRequestByIdRequest
        @return: FindPunishRequestByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_punish_request_by_id_with_options(request, runtime)

    async def find_punish_request_by_id_async(
        self,
        request: buss_20160718_models.FindPunishRequestByIdRequest,
    ) -> buss_20160718_models.FindPunishRequestByIdResponse:
        """
        @param request: FindPunishRequestByIdRequest
        @return: FindPunishRequestByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_punish_request_by_id_with_options_async(request, runtime)

    def find_punish_white_with_options(
        self,
        request: buss_20160718_models.FindPunishWhiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishWhiteResponse:
        """
        @param request: FindPunishWhiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishWhiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_values):
            query['DataValues'] = request.data_values
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishWhite',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishWhiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_punish_white_with_options_async(
        self,
        request: buss_20160718_models.FindPunishWhiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.FindPunishWhiteResponse:
        """
        @param request: FindPunishWhiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindPunishWhiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_values):
            query['DataValues'] = request.data_values
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindPunishWhite',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.FindPunishWhiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_punish_white(
        self,
        request: buss_20160718_models.FindPunishWhiteRequest,
    ) -> buss_20160718_models.FindPunishWhiteResponse:
        """
        @param request: FindPunishWhiteRequest
        @return: FindPunishWhiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_punish_white_with_options(request, runtime)

    async def find_punish_white_async(
        self,
        request: buss_20160718_models.FindPunishWhiteRequest,
    ) -> buss_20160718_models.FindPunishWhiteResponse:
        """
        @param request: FindPunishWhiteRequest
        @return: FindPunishWhiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_punish_white_with_options_async(request, runtime)

    def punish_white_list_service_with_options(
        self,
        tmp_req: buss_20160718_models.PunishWhiteListServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.PunishWhiteListServiceResponse:
        """
        @summary 白名单服务
        
        @param tmp_req: PunishWhiteListServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PunishWhiteListServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.PunishWhiteListServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_values):
            request.data_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_values, 'DataValues', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PunishWhiteListService',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.PunishWhiteListServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def punish_white_list_service_with_options_async(
        self,
        tmp_req: buss_20160718_models.PunishWhiteListServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.PunishWhiteListServiceResponse:
        """
        @summary 白名单服务
        
        @param tmp_req: PunishWhiteListServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PunishWhiteListServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.PunishWhiteListServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_values):
            request.data_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_values, 'DataValues', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PunishWhiteListService',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.PunishWhiteListServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def punish_white_list_service(
        self,
        request: buss_20160718_models.PunishWhiteListServiceRequest,
    ) -> buss_20160718_models.PunishWhiteListServiceResponse:
        """
        @summary 白名单服务
        
        @param request: PunishWhiteListServiceRequest
        @return: PunishWhiteListServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.punish_white_list_service_with_options(request, runtime)

    async def punish_white_list_service_async(
        self,
        request: buss_20160718_models.PunishWhiteListServiceRequest,
    ) -> buss_20160718_models.PunishWhiteListServiceResponse:
        """
        @summary 白名单服务
        
        @param request: PunishWhiteListServiceRequest
        @return: PunishWhiteListServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.punish_white_list_service_with_options_async(request, runtime)

    def query_ipp_task_list_with_options(
        self,
        request: buss_20160718_models.QueryIppTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryIppTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIppTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_0):
            query['Param0'] = request.param_0
        if not UtilClient.is_unset(request.param_1):
            query['Param1'] = request.param_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIppTaskList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryIppTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ipp_task_list_with_options_async(
        self,
        request: buss_20160718_models.QueryIppTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryIppTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIppTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_0):
            query['Param0'] = request.param_0
        if not UtilClient.is_unset(request.param_1):
            query['Param1'] = request.param_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIppTaskList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryIppTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ipp_task_list(
        self,
        request: buss_20160718_models.QueryIppTaskListRequest,
    ) -> buss_20160718_models.QueryIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryIppTaskListRequest
        @return: QueryIppTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ipp_task_list_with_options(request, runtime)

    async def query_ipp_task_list_async(
        self,
        request: buss_20160718_models.QueryIppTaskListRequest,
    ) -> buss_20160718_models.QueryIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryIppTaskListRequest
        @return: QueryIppTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ipp_task_list_with_options_async(request, runtime)

    def query_oversea_ipp_task_list_with_options(
        self,
        request: buss_20160718_models.QueryOverseaIppTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryOverseaIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryOverseaIppTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOverseaIppTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_0):
            query['Param0'] = request.param_0
        if not UtilClient.is_unset(request.param_1):
            query['Param1'] = request.param_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOverseaIppTaskList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryOverseaIppTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_oversea_ipp_task_list_with_options_async(
        self,
        request: buss_20160718_models.QueryOverseaIppTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryOverseaIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryOverseaIppTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOverseaIppTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_0):
            query['Param0'] = request.param_0
        if not UtilClient.is_unset(request.param_1):
            query['Param1'] = request.param_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOverseaIppTaskList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryOverseaIppTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_oversea_ipp_task_list(
        self,
        request: buss_20160718_models.QueryOverseaIppTaskListRequest,
    ) -> buss_20160718_models.QueryOverseaIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryOverseaIppTaskListRequest
        @return: QueryOverseaIppTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_oversea_ipp_task_list_with_options(request, runtime)

    async def query_oversea_ipp_task_list_async(
        self,
        request: buss_20160718_models.QueryOverseaIppTaskListRequest,
    ) -> buss_20160718_models.QueryOverseaIppTaskListResponse:
        """
        @summary 验证 IPP 接口连通性
        
        @param request: QueryOverseaIppTaskListRequest
        @return: QueryOverseaIppTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_oversea_ipp_task_list_with_options_async(request, runtime)

    def query_punish_for_rc_with_options(
        self,
        request: buss_20160718_models.QueryPunishForRcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryPunishForRcResponse:
        """
        @param request: QueryPunishForRcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPunishForRcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.date_end):
            query['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            query['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPunishForRc',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryPunishForRcResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_punish_for_rc_with_options_async(
        self,
        request: buss_20160718_models.QueryPunishForRcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryPunishForRcResponse:
        """
        @param request: QueryPunishForRcRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPunishForRcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.date_end):
            query['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            query['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPunishForRc',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryPunishForRcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_punish_for_rc(
        self,
        request: buss_20160718_models.QueryPunishForRcRequest,
    ) -> buss_20160718_models.QueryPunishForRcResponse:
        """
        @param request: QueryPunishForRcRequest
        @return: QueryPunishForRcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_punish_for_rc_with_options(request, runtime)

    async def query_punish_for_rc_async(
        self,
        request: buss_20160718_models.QueryPunishForRcRequest,
    ) -> buss_20160718_models.QueryPunishForRcResponse:
        """
        @param request: QueryPunishForRcRequest
        @return: QueryPunishForRcResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_punish_for_rc_with_options_async(request, runtime)

    def query_punish_list_with_options(
        self,
        request: buss_20160718_models.QueryPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryPunishListResponse:
        """
        @param request: QueryPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.date_end):
            query['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            query['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.punish_ip):
            query['PunishIp'] = request.punish_ip
        if not UtilClient.is_unset(request.punish_url):
            query['PunishUrl'] = request.punish_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPunishList',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryPunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_punish_list_with_options_async(
        self,
        request: buss_20160718_models.QueryPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryPunishListResponse:
        """
        @param request: QueryPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPunishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.date_end):
            query['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            query['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.punish_ip):
            query['PunishIp'] = request.punish_ip
        if not UtilClient.is_unset(request.punish_url):
            query['PunishUrl'] = request.punish_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPunishList',
            version='2016-07-18',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryPunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_punish_list(
        self,
        request: buss_20160718_models.QueryPunishListRequest,
    ) -> buss_20160718_models.QueryPunishListResponse:
        """
        @param request: QueryPunishListRequest
        @return: QueryPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_punish_list_with_options(request, runtime)

    async def query_punish_list_async(
        self,
        request: buss_20160718_models.QueryPunishListRequest,
    ) -> buss_20160718_models.QueryPunishListResponse:
        """
        @param request: QueryPunishListRequest
        @return: QueryPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_punish_list_with_options_async(request, runtime)

    def query_risk_punish_list_with_options(
        self,
        request: buss_20160718_models.QueryRiskPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryRiskPunishListResponse:
        """
        @summary 查询处罚记录（安全管控控制台)
        
        @param request: QueryRiskPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRiskPunishListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRiskPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryRiskPunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_risk_punish_list_with_options_async(
        self,
        request: buss_20160718_models.QueryRiskPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryRiskPunishListResponse:
        """
        @summary 查询处罚记录（安全管控控制台)
        
        @param request: QueryRiskPunishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRiskPunishListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRiskPunishList',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryRiskPunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_risk_punish_list(
        self,
        request: buss_20160718_models.QueryRiskPunishListRequest,
    ) -> buss_20160718_models.QueryRiskPunishListResponse:
        """
        @summary 查询处罚记录（安全管控控制台)
        
        @param request: QueryRiskPunishListRequest
        @return: QueryRiskPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_risk_punish_list_with_options(request, runtime)

    async def query_risk_punish_list_async(
        self,
        request: buss_20160718_models.QueryRiskPunishListRequest,
    ) -> buss_20160718_models.QueryRiskPunishListResponse:
        """
        @summary 查询处罚记录（安全管控控制台)
        
        @param request: QueryRiskPunishListRequest
        @return: QueryRiskPunishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_risk_punish_list_with_options_async(request, runtime)

    def query_risk_punish_record_with_options(
        self,
        request: buss_20160718_models.QueryRiskPunishRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryRiskPunishRecordResponse:
        """
        @summary 查询处罚记录(安全管控控制台)
        
        @param request: QueryRiskPunishRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRiskPunishRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRiskPunishRecord',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryRiskPunishRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_risk_punish_record_with_options_async(
        self,
        request: buss_20160718_models.QueryRiskPunishRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.QueryRiskPunishRecordResponse:
        """
        @summary 查询处罚记录(安全管控控制台)
        
        @param request: QueryRiskPunishRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRiskPunishRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRiskPunishRecord',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.QueryRiskPunishRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_risk_punish_record(
        self,
        request: buss_20160718_models.QueryRiskPunishRecordRequest,
    ) -> buss_20160718_models.QueryRiskPunishRecordResponse:
        """
        @summary 查询处罚记录(安全管控控制台)
        
        @param request: QueryRiskPunishRecordRequest
        @return: QueryRiskPunishRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_risk_punish_record_with_options(request, runtime)

    async def query_risk_punish_record_async(
        self,
        request: buss_20160718_models.QueryRiskPunishRecordRequest,
    ) -> buss_20160718_models.QueryRiskPunishRecordResponse:
        """
        @summary 查询处罚记录(安全管控控制台)
        
        @param request: QueryRiskPunishRecordRequest
        @return: QueryRiskPunishRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_risk_punish_record_with_options_async(request, runtime)

    def receive_raider_data_with_options(
        self,
        tmp_req: buss_20160718_models.ReceiveRaiderDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.ReceiveRaiderDataResponse:
        """
        @param tmp_req: ReceiveRaiderDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReceiveRaiderDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.ReceiveRaiderDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.raider_data):
            request.raider_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.raider_data, 'RaiderData', 'json')
        body = {}
        if not UtilClient.is_unset(request.raider_data_shrink):
            body['RaiderData'] = request.raider_data_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReceiveRaiderData',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.ReceiveRaiderDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def receive_raider_data_with_options_async(
        self,
        tmp_req: buss_20160718_models.ReceiveRaiderDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.ReceiveRaiderDataResponse:
        """
        @param tmp_req: ReceiveRaiderDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReceiveRaiderDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.ReceiveRaiderDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.raider_data):
            request.raider_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.raider_data, 'RaiderData', 'json')
        body = {}
        if not UtilClient.is_unset(request.raider_data_shrink):
            body['RaiderData'] = request.raider_data_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReceiveRaiderData',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.ReceiveRaiderDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def receive_raider_data(
        self,
        request: buss_20160718_models.ReceiveRaiderDataRequest,
    ) -> buss_20160718_models.ReceiveRaiderDataResponse:
        """
        @param request: ReceiveRaiderDataRequest
        @return: ReceiveRaiderDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.receive_raider_data_with_options(request, runtime)

    async def receive_raider_data_async(
        self,
        request: buss_20160718_models.ReceiveRaiderDataRequest,
    ) -> buss_20160718_models.ReceiveRaiderDataResponse:
        """
        @param request: ReceiveRaiderDataRequest
        @return: ReceiveRaiderDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.receive_raider_data_with_options_async(request, runtime)

    def risk_punish_with_options(
        self,
        tmp_req: buss_20160718_models.RiskPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.RiskPunishResponse:
        """
        @param tmp_req: RiskPunishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskPunishResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.RiskPunishShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'Extras', 'json')
        query = {}
        if not UtilClient.is_unset(request.bussiness_code):
            query['BussinessCode'] = request.bussiness_code
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.event_code):
            query['EventCode'] = request.event_code
        if not UtilClient.is_unset(request.expected_remove_time):
            query['ExpectedRemoveTime'] = request.expected_remove_time
        if not UtilClient.is_unset(request.extras_shrink):
            query['Extras'] = request.extras_shrink
        if not UtilClient.is_unset(request.filter_special_account):
            query['FilterSpecialAccount'] = request.filter_special_account
        if not UtilClient.is_unset(request.filter_white):
            query['FilterWhite'] = request.filter_white
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.is_direct_punish):
            query['IsDirectPunish'] = request.is_direct_punish
        if not UtilClient.is_unset(request.punish_date):
            query['PunishDate'] = request.punish_date
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.punish_url):
            query['PunishUrl'] = request.punish_url
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RiskPunish',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.RiskPunishResponse(),
            self.call_api(params, req, runtime)
        )

    async def risk_punish_with_options_async(
        self,
        tmp_req: buss_20160718_models.RiskPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.RiskPunishResponse:
        """
        @param tmp_req: RiskPunishRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskPunishResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.RiskPunishShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'Extras', 'json')
        query = {}
        if not UtilClient.is_unset(request.bussiness_code):
            query['BussinessCode'] = request.bussiness_code
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.event_code):
            query['EventCode'] = request.event_code
        if not UtilClient.is_unset(request.expected_remove_time):
            query['ExpectedRemoveTime'] = request.expected_remove_time
        if not UtilClient.is_unset(request.extras_shrink):
            query['Extras'] = request.extras_shrink
        if not UtilClient.is_unset(request.filter_special_account):
            query['FilterSpecialAccount'] = request.filter_special_account
        if not UtilClient.is_unset(request.filter_white):
            query['FilterWhite'] = request.filter_white
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.is_direct_punish):
            query['IsDirectPunish'] = request.is_direct_punish
        if not UtilClient.is_unset(request.punish_date):
            query['PunishDate'] = request.punish_date
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.punish_url):
            query['PunishUrl'] = request.punish_url
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RiskPunish',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.RiskPunishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def risk_punish(
        self,
        request: buss_20160718_models.RiskPunishRequest,
    ) -> buss_20160718_models.RiskPunishResponse:
        """
        @param request: RiskPunishRequest
        @return: RiskPunishResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.risk_punish_with_options(request, runtime)

    async def risk_punish_async(
        self,
        request: buss_20160718_models.RiskPunishRequest,
    ) -> buss_20160718_models.RiskPunishResponse:
        """
        @param request: RiskPunishRequest
        @return: RiskPunishResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.risk_punish_with_options_async(request, runtime)

    def risk_punish_remove_with_options(
        self,
        tmp_req: buss_20160718_models.RiskPunishRemoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.RiskPunishRemoveResponse:
        """
        @param tmp_req: RiskPunishRemoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskPunishRemoveResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.RiskPunishRemoveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'Extras', 'json')
        query = {}
        if not UtilClient.is_unset(request.extras_shrink):
            query['Extras'] = request.extras_shrink
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.rm_punish):
            query['RmPunish'] = request.rm_punish
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RiskPunishRemove',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.RiskPunishRemoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def risk_punish_remove_with_options_async(
        self,
        tmp_req: buss_20160718_models.RiskPunishRemoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20160718_models.RiskPunishRemoveResponse:
        """
        @param tmp_req: RiskPunishRemoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskPunishRemoveResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20160718_models.RiskPunishRemoveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'Extras', 'json')
        query = {}
        if not UtilClient.is_unset(request.extras_shrink):
            query['Extras'] = request.extras_shrink
        if not UtilClient.is_unset(request.punish_request_id):
            query['PunishRequestId'] = request.punish_request_id
        if not UtilClient.is_unset(request.rm_punish):
            query['RmPunish'] = request.rm_punish
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RiskPunishRemove',
            version='2016-07-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20160718_models.RiskPunishRemoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def risk_punish_remove(
        self,
        request: buss_20160718_models.RiskPunishRemoveRequest,
    ) -> buss_20160718_models.RiskPunishRemoveResponse:
        """
        @param request: RiskPunishRemoveRequest
        @return: RiskPunishRemoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.risk_punish_remove_with_options(request, runtime)

    async def risk_punish_remove_async(
        self,
        request: buss_20160718_models.RiskPunishRemoveRequest,
    ) -> buss_20160718_models.RiskPunishRemoveResponse:
        """
        @param request: RiskPunishRemoveRequest
        @return: RiskPunishRemoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.risk_punish_remove_with_options_async(request, runtime)
