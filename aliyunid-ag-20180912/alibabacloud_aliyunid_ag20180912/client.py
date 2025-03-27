# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliyunid_ag20180912 import models as aliyunid_ag_20180912_models
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
        self._endpoint = self.get_endpoint('aliyunid-ag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_ag_account_with_options(
        self,
        request: aliyunid_ag_20180912_models.CreateAgAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.CreateAgAccountResponse:
        """
        @summary 创建ag账号
        
        @param request: CreateAgAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgAccount',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.CreateAgAccountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.CreateAgAccountResponse(),
                self.execute(params, req, runtime)
            )

    async def create_ag_account_with_options_async(
        self,
        request: aliyunid_ag_20180912_models.CreateAgAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.CreateAgAccountResponse:
        """
        @summary 创建ag账号
        
        @param request: CreateAgAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgAccount',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.CreateAgAccountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.CreateAgAccountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_ag_account(
        self,
        request: aliyunid_ag_20180912_models.CreateAgAccountRequest,
    ) -> aliyunid_ag_20180912_models.CreateAgAccountResponse:
        """
        @summary 创建ag账号
        
        @param request: CreateAgAccountRequest
        @return: CreateAgAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    async def create_ag_account_async(
        self,
        request: aliyunid_ag_20180912_models.CreateAgAccountRequest,
    ) -> aliyunid_ag_20180912_models.CreateAgAccountResponse:
        """
        @summary 创建ag账号
        
        @param request: CreateAgAccountRequest
        @return: CreateAgAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ag_account_with_options_async(request, runtime)

    def get_ag_relation_with_options(
        self,
        request: aliyunid_ag_20180912_models.GetAgRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.GetAgRelationResponse:
        """
        @param request: GetAgRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgRelation',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetAgRelationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetAgRelationResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ag_relation_with_options_async(
        self,
        request: aliyunid_ag_20180912_models.GetAgRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.GetAgRelationResponse:
        """
        @param request: GetAgRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgRelation',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetAgRelationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetAgRelationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ag_relation(
        self,
        request: aliyunid_ag_20180912_models.GetAgRelationRequest,
    ) -> aliyunid_ag_20180912_models.GetAgRelationResponse:
        """
        @param request: GetAgRelationRequest
        @return: GetAgRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ag_relation_with_options(request, runtime)

    async def get_ag_relation_async(
        self,
        request: aliyunid_ag_20180912_models.GetAgRelationRequest,
    ) -> aliyunid_ag_20180912_models.GetAgRelationResponse:
        """
        @param request: GetAgRelationRequest
        @return: GetAgRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ag_relation_with_options_async(request, runtime)

    def get_ram_bind_with_options(
        self,
        request: aliyunid_ag_20180912_models.GetRamBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.GetRamBindResponse:
        """
        @param request: GetRamBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamBindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRamBind',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetRamBindResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetRamBindResponse(),
                self.execute(params, req, runtime)
            )

    async def get_ram_bind_with_options_async(
        self,
        request: aliyunid_ag_20180912_models.GetRamBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.GetRamBindResponse:
        """
        @param request: GetRamBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamBindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRamBind',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetRamBindResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.GetRamBindResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_ram_bind(
        self,
        request: aliyunid_ag_20180912_models.GetRamBindRequest,
    ) -> aliyunid_ag_20180912_models.GetRamBindResponse:
        """
        @param request: GetRamBindRequest
        @return: GetRamBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ram_bind_with_options(request, runtime)

    async def get_ram_bind_async(
        self,
        request: aliyunid_ag_20180912_models.GetRamBindRequest,
    ) -> aliyunid_ag_20180912_models.GetRamBindResponse:
        """
        @param request: GetRamBindRequest
        @return: GetRamBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ram_bind_with_options_async(request, runtime)

    def paginate_ag_relations_with_options(
        self,
        request: aliyunid_ag_20180912_models.PaginateAgRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.PaginateAgRelationsResponse:
        """
        @param request: PaginateAgRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PaginateAgRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_count):
            query['QueryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PaginateAgRelations',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.PaginateAgRelationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.PaginateAgRelationsResponse(),
                self.execute(params, req, runtime)
            )

    async def paginate_ag_relations_with_options_async(
        self,
        request: aliyunid_ag_20180912_models.PaginateAgRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunid_ag_20180912_models.PaginateAgRelationsResponse:
        """
        @param request: PaginateAgRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PaginateAgRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_count):
            query['QueryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PaginateAgRelations',
            version='2018-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.PaginateAgRelationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                aliyunid_ag_20180912_models.PaginateAgRelationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def paginate_ag_relations(
        self,
        request: aliyunid_ag_20180912_models.PaginateAgRelationsRequest,
    ) -> aliyunid_ag_20180912_models.PaginateAgRelationsResponse:
        """
        @param request: PaginateAgRelationsRequest
        @return: PaginateAgRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.paginate_ag_relations_with_options(request, runtime)

    async def paginate_ag_relations_async(
        self,
        request: aliyunid_ag_20180912_models.PaginateAgRelationsRequest,
    ) -> aliyunid_ag_20180912_models.PaginateAgRelationsResponse:
        """
        @param request: PaginateAgRelationsRequest
        @return: PaginateAgRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.paginate_ag_relations_with_options_async(request, runtime)
