# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataanalysisgbi20240823 import models as data_analysis_gbi20240823_models
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
        self._endpoint = self.get_endpoint('dataanalysisgbi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_delete_synonyms_with_options(
        self,
        request: data_analysis_gbi20240823_models.BatchDeleteSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse:
        """
        @summary 批量删除当前指定业务空间下的同义词
        
        @param request: BatchDeleteSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.synonym_id_keys):
            body['synonymIdKeys'] = request.synonym_id_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/batchDelete/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_delete_synonyms_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.BatchDeleteSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse:
        """
        @summary 批量删除当前指定业务空间下的同义词
        
        @param request: BatchDeleteSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.synonym_id_keys):
            body['synonymIdKeys'] = request.synonym_id_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/batchDelete/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_delete_synonyms(
        self,
        request: data_analysis_gbi20240823_models.BatchDeleteSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse:
        """
        @summary 批量删除当前指定业务空间下的同义词
        
        @param request: BatchDeleteSynonymsRequest
        @return: BatchDeleteSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_synonyms_with_options(request, headers, runtime)

    async def batch_delete_synonyms_async(
        self,
        request: data_analysis_gbi20240823_models.BatchDeleteSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.BatchDeleteSynonymsResponse:
        """
        @summary 批量删除当前指定业务空间下的同义词
        
        @param request: BatchDeleteSynonymsRequest
        @return: BatchDeleteSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_delete_synonyms_with_options_async(request, headers, runtime)

    def cancel_datasource_authorization_with_options(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/cancel/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_datasource_authorization_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/cancel/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_datasource_authorization(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @return: CancelDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_datasource_authorization_with_options(request, headers, runtime)

    async def cancel_datasource_authorization_async(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @return: CancelDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_datasource_authorization_with_options_async(request, headers, runtime)

    def create_business_logic_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateBusinessLogicResponse:
        """
        @summary 在指定的业务空间下创建新的业务逻辑解释
        
        @param request: CreateBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateBusinessLogicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateBusinessLogicResponse(),
                self.execute(params, req, runtime)
            )

    async def create_business_logic_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateBusinessLogicResponse:
        """
        @summary 在指定的业务空间下创建新的业务逻辑解释
        
        @param request: CreateBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateBusinessLogicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateBusinessLogicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_business_logic(
        self,
        request: data_analysis_gbi20240823_models.CreateBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.CreateBusinessLogicResponse:
        """
        @summary 在指定的业务空间下创建新的业务逻辑解释
        
        @param request: CreateBusinessLogicRequest
        @return: CreateBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_business_logic_with_options(request, headers, runtime)

    async def create_business_logic_async(
        self,
        request: data_analysis_gbi20240823_models.CreateBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.CreateBusinessLogicResponse:
        """
        @summary 在指定的业务空间下创建新的业务逻辑解释
        
        @param request: CreateBusinessLogicRequest
        @return: CreateBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_business_logic_with_options_async(request, headers, runtime)

    def create_datasource_authorization_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
                self.execute(params, req, runtime)
            )

    async def create_datasource_authorization_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_datasource_authorization(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @return: CreateDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_datasource_authorization_with_options(request, headers, runtime)

    async def create_datasource_authorization_async(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @return: CreateDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_datasource_authorization_with_options_async(request, headers, runtime)

    def create_synonyms_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateSynonymsResponse:
        """
        @summary 在当前指定的业务空间下面，新建同义词
        
        @param request: CreateSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['columns'] = request.columns
        if not UtilClient.is_unset(request.word):
            body['word'] = request.word
        if not UtilClient.is_unset(request.word_synonyms):
            body['wordSynonyms'] = request.word_synonyms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateSynonymsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateSynonymsResponse(),
                self.execute(params, req, runtime)
            )

    async def create_synonyms_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateSynonymsResponse:
        """
        @summary 在当前指定的业务空间下面，新建同义词
        
        @param request: CreateSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['columns'] = request.columns
        if not UtilClient.is_unset(request.word):
            body['word'] = request.word
        if not UtilClient.is_unset(request.word_synonyms):
            body['wordSynonyms'] = request.word_synonyms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateSynonymsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateSynonymsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_synonyms(
        self,
        request: data_analysis_gbi20240823_models.CreateSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.CreateSynonymsResponse:
        """
        @summary 在当前指定的业务空间下面，新建同义词
        
        @param request: CreateSynonymsRequest
        @return: CreateSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_synonyms_with_options(request, headers, runtime)

    async def create_synonyms_async(
        self,
        request: data_analysis_gbi20240823_models.CreateSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.CreateSynonymsResponse:
        """
        @summary 在当前指定的业务空间下面，新建同义词
        
        @param request: CreateSynonymsRequest
        @return: CreateSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_synonyms_with_options_async(request, headers, runtime)

    def create_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/createVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/createVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @return: CreateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_virtual_datasource_instance_with_options(request, headers, runtime)

    async def create_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @return: CreateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def delete_business_logic_with_options(
        self,
        request: data_analysis_gbi20240823_models.DeleteBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteBusinessLogicResponse:
        """
        @summary 删除指定业务空间下所指定的业务逻辑解释
        
        @param request: DeleteBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.business_logic_id_keys):
            body['businessLogicIdKeys'] = request.business_logic_id_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteBusinessLogicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteBusinessLogicResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_business_logic_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteBusinessLogicResponse:
        """
        @summary 删除指定业务空间下所指定的业务逻辑解释
        
        @param request: DeleteBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.business_logic_id_keys):
            body['businessLogicIdKeys'] = request.business_logic_id_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteBusinessLogicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteBusinessLogicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_business_logic(
        self,
        request: data_analysis_gbi20240823_models.DeleteBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.DeleteBusinessLogicResponse:
        """
        @summary 删除指定业务空间下所指定的业务逻辑解释
        
        @param request: DeleteBusinessLogicRequest
        @return: DeleteBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_business_logic_with_options(request, headers, runtime)

    async def delete_business_logic_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.DeleteBusinessLogicResponse:
        """
        @summary 删除指定业务空间下所指定的业务逻辑解释
        
        @param request: DeleteBusinessLogicRequest
        @return: DeleteBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_business_logic_with_options_async(request, headers, runtime)

    def delete_column_with_options(
        self,
        request: data_analysis_gbi20240823_models.DeleteColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteColumnResponse:
        """
        @summary 从当前所指定的业务空间中，删除所指定的列
        
        @param request: DeleteColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteColumnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteColumnResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_column_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteColumnResponse:
        """
        @summary 从当前所指定的业务空间中，删除所指定的列
        
        @param request: DeleteColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteColumnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteColumnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_column(
        self,
        request: data_analysis_gbi20240823_models.DeleteColumnRequest,
    ) -> data_analysis_gbi20240823_models.DeleteColumnResponse:
        """
        @summary 从当前所指定的业务空间中，删除所指定的列
        
        @param request: DeleteColumnRequest
        @return: DeleteColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_column_with_options(request, headers, runtime)

    async def delete_column_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteColumnRequest,
    ) -> data_analysis_gbi20240823_models.DeleteColumnResponse:
        """
        @summary 从当前所指定的业务空间中，删除所指定的列
        
        @param request: DeleteColumnRequest
        @return: DeleteColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_column_with_options_async(request, headers, runtime)

    def delete_selected_table_with_options(
        self,
        request: data_analysis_gbi20240823_models.DeleteSelectedTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteSelectedTableResponse:
        """
        @summary 将当前指定数据表从指定业务空间管控中删除
        
        @param request: DeleteSelectedTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSelectedTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSelectedTable',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteSelectedTableResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteSelectedTableResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_selected_table_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteSelectedTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteSelectedTableResponse:
        """
        @summary 将当前指定数据表从指定业务空间管控中删除
        
        @param request: DeleteSelectedTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSelectedTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSelectedTable',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/delete/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteSelectedTableResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteSelectedTableResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_selected_table(
        self,
        request: data_analysis_gbi20240823_models.DeleteSelectedTableRequest,
    ) -> data_analysis_gbi20240823_models.DeleteSelectedTableResponse:
        """
        @summary 将当前指定数据表从指定业务空间管控中删除
        
        @param request: DeleteSelectedTableRequest
        @return: DeleteSelectedTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_selected_table_with_options(request, headers, runtime)

    async def delete_selected_table_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteSelectedTableRequest,
    ) -> data_analysis_gbi20240823_models.DeleteSelectedTableResponse:
        """
        @summary 将当前指定数据表从指定业务空间管控中删除
        
        @param request: DeleteSelectedTableRequest
        @return: DeleteSelectedTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_selected_table_with_options_async(request, headers, runtime)

    def delete_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/deleteVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/deleteVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_virtual_datasource_instance_with_options(request, headers, runtime)

    async def delete_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def list_business_logic_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListBusinessLogicResponse:
        """
        @summary 获取当前指定业务空间下的企业知识名词解释列表
        
        @param request: ListBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListBusinessLogicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListBusinessLogicResponse(),
                self.execute(params, req, runtime)
            )

    async def list_business_logic_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListBusinessLogicResponse:
        """
        @summary 获取当前指定业务空间下的企业知识名词解释列表
        
        @param request: ListBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListBusinessLogicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListBusinessLogicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_business_logic(
        self,
        request: data_analysis_gbi20240823_models.ListBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.ListBusinessLogicResponse:
        """
        @summary 获取当前指定业务空间下的企业知识名词解释列表
        
        @param request: ListBusinessLogicRequest
        @return: ListBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_business_logic_with_options(request, headers, runtime)

    async def list_business_logic_async(
        self,
        request: data_analysis_gbi20240823_models.ListBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.ListBusinessLogicResponse:
        """
        @summary 获取当前指定业务空间下的企业知识名词解释列表
        
        @param request: ListBusinessLogicRequest
        @return: ListBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_business_logic_with_options_async(request, headers, runtime)

    def list_column_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListColumnResponse:
        """
        @summary 获取当前指定业务空间，指定表下面的列信息
        
        @param request: ListColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListColumnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListColumnResponse(),
                self.execute(params, req, runtime)
            )

    async def list_column_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListColumnResponse:
        """
        @summary 获取当前指定业务空间，指定表下面的列信息
        
        @param request: ListColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListColumnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListColumnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_column(
        self,
        request: data_analysis_gbi20240823_models.ListColumnRequest,
    ) -> data_analysis_gbi20240823_models.ListColumnResponse:
        """
        @summary 获取当前指定业务空间，指定表下面的列信息
        
        @param request: ListColumnRequest
        @return: ListColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_column_with_options(request, headers, runtime)

    async def list_column_async(
        self,
        request: data_analysis_gbi20240823_models.ListColumnRequest,
    ) -> data_analysis_gbi20240823_models.ListColumnResponse:
        """
        @summary 获取当前指定业务空间，指定表下面的列信息
        
        @param request: ListColumnRequest
        @return: ListColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_column_with_options_async(request, headers, runtime)

    def list_enum_mapping_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListEnumMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListEnumMappingResponse:
        """
        @summary 获取当前业务空间，指定表、列下的枚举值
        
        @param request: ListEnumMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnumMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEnumMapping',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListEnumMappingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListEnumMappingResponse(),
                self.execute(params, req, runtime)
            )

    async def list_enum_mapping_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListEnumMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListEnumMappingResponse:
        """
        @summary 获取当前业务空间，指定表、列下的枚举值
        
        @param request: ListEnumMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnumMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEnumMapping',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListEnumMappingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListEnumMappingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_enum_mapping(
        self,
        request: data_analysis_gbi20240823_models.ListEnumMappingRequest,
    ) -> data_analysis_gbi20240823_models.ListEnumMappingResponse:
        """
        @summary 获取当前业务空间，指定表、列下的枚举值
        
        @param request: ListEnumMappingRequest
        @return: ListEnumMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_enum_mapping_with_options(request, headers, runtime)

    async def list_enum_mapping_async(
        self,
        request: data_analysis_gbi20240823_models.ListEnumMappingRequest,
    ) -> data_analysis_gbi20240823_models.ListEnumMappingResponse:
        """
        @summary 获取当前业务空间，指定表、列下的枚举值
        
        @param request: ListEnumMappingRequest
        @return: ListEnumMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_enum_mapping_with_options_async(request, headers, runtime)

    def list_selected_tables_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListSelectedTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListSelectedTablesResponse:
        """
        @summary 获取当前业务空间处于以关联状态的数据表
        
        @param request: ListSelectedTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectedTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSelectedTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/datasource/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSelectedTablesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSelectedTablesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_selected_tables_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListSelectedTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListSelectedTablesResponse:
        """
        @summary 获取当前业务空间处于以关联状态的数据表
        
        @param request: ListSelectedTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectedTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSelectedTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/datasource/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSelectedTablesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSelectedTablesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_selected_tables(
        self,
        request: data_analysis_gbi20240823_models.ListSelectedTablesRequest,
    ) -> data_analysis_gbi20240823_models.ListSelectedTablesResponse:
        """
        @summary 获取当前业务空间处于以关联状态的数据表
        
        @param request: ListSelectedTablesRequest
        @return: ListSelectedTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selected_tables_with_options(request, headers, runtime)

    async def list_selected_tables_async(
        self,
        request: data_analysis_gbi20240823_models.ListSelectedTablesRequest,
    ) -> data_analysis_gbi20240823_models.ListSelectedTablesResponse:
        """
        @summary 获取当前业务空间处于以关联状态的数据表
        
        @param request: ListSelectedTablesRequest
        @return: ListSelectedTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_selected_tables_with_options_async(request, headers, runtime)

    def list_synonyms_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListSynonymsResponse:
        """
        @summary 获取当前指定业务空间下的同义词列表
        
        @param request: ListSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSynonymsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSynonymsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_synonyms_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListSynonymsResponse:
        """
        @summary 获取当前指定业务空间下的同义词列表
        
        @param request: ListSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/list/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSynonymsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListSynonymsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_synonyms(
        self,
        request: data_analysis_gbi20240823_models.ListSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.ListSynonymsResponse:
        """
        @summary 获取当前指定业务空间下的同义词列表
        
        @param request: ListSynonymsRequest
        @return: ListSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_synonyms_with_options(request, headers, runtime)

    async def list_synonyms_async(
        self,
        request: data_analysis_gbi20240823_models.ListSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.ListSynonymsResponse:
        """
        @summary 获取当前指定业务空间下的同义词列表
        
        @param request: ListSynonymsRequest
        @return: ListSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_synonyms_with_options_async(request, headers, runtime)

    def list_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/listVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def list_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/listVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @return: ListVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_virtual_datasource_instance_with_options(request, headers, runtime)

    async def list_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @return: ListVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def recover_column_with_options(
        self,
        request: data_analysis_gbi20240823_models.RecoverColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RecoverColumnResponse:
        """
        @summary 将指定数据表的数据列恢复到初始话状态
        
        @param request: RecoverColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/recover/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RecoverColumnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RecoverColumnResponse(),
                self.execute(params, req, runtime)
            )

    async def recover_column_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.RecoverColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RecoverColumnResponse:
        """
        @summary 将指定数据表的数据列恢复到初始话状态
        
        @param request: RecoverColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/recover/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RecoverColumnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RecoverColumnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def recover_column(
        self,
        request: data_analysis_gbi20240823_models.RecoverColumnRequest,
    ) -> data_analysis_gbi20240823_models.RecoverColumnResponse:
        """
        @summary 将指定数据表的数据列恢复到初始话状态
        
        @param request: RecoverColumnRequest
        @return: RecoverColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_column_with_options(request, headers, runtime)

    async def recover_column_async(
        self,
        request: data_analysis_gbi20240823_models.RecoverColumnRequest,
    ) -> data_analysis_gbi20240823_models.RecoverColumnResponse:
        """
        @summary 将指定数据表的数据列恢复到初始话状态
        
        @param request: RecoverColumnRequest
        @return: RecoverColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recover_column_with_options_async(request, headers, runtime)

    def resync_table_with_options(
        self,
        request: data_analysis_gbi20240823_models.ResyncTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ResyncTableResponse:
        """
        @summary 从远程数据库刷新当前所关联的数据表信息
        
        @param request: ResyncTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResyncTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep):
            body['keep'] = request.keep
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResyncTable',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/refresh/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ResyncTableResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ResyncTableResponse(),
                self.execute(params, req, runtime)
            )

    async def resync_table_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ResyncTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ResyncTableResponse:
        """
        @summary 从远程数据库刷新当前所关联的数据表信息
        
        @param request: ResyncTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResyncTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep):
            body['keep'] = request.keep
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResyncTable',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/refresh/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ResyncTableResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.ResyncTableResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resync_table(
        self,
        request: data_analysis_gbi20240823_models.ResyncTableRequest,
    ) -> data_analysis_gbi20240823_models.ResyncTableResponse:
        """
        @summary 从远程数据库刷新当前所关联的数据表信息
        
        @param request: ResyncTableRequest
        @return: ResyncTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resync_table_with_options(request, headers, runtime)

    async def resync_table_async(
        self,
        request: data_analysis_gbi20240823_models.ResyncTableRequest,
    ) -> data_analysis_gbi20240823_models.ResyncTableResponse:
        """
        @summary 从远程数据库刷新当前所关联的数据表信息
        
        @param request: ResyncTableRequest
        @return: ResyncTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resync_table_with_options_async(request, headers, runtime)

    def run_data_analysis_with_options(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_ctrl_params):
            body['agentCtrlParams'] = request.agent_ctrl_params
        if not UtilClient.is_unset(request.data_role):
            body['dataRole'] = request.data_role
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        if not UtilClient.is_unset(request.user_params):
            body['userParams'] = request.user_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
                self.execute(params, req, runtime)
            )

    async def run_data_analysis_with_options_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_ctrl_params):
            body['agentCtrlParams'] = request.agent_ctrl_params
        if not UtilClient.is_unset(request.data_role):
            body['dataRole'] = request.data_role
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        if not UtilClient.is_unset(request.user_params):
            body['userParams'] = request.user_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_data_analysis(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_data_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_data_analysis_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_data_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_data_result_analysis_with_options(
        self,
        request: data_analysis_gbi20240823_models.RunDataResultAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataResultAnalysisResponse:
        """
        @summary 对结构化结果进行分析、可视化信息生成
        
        @param request: RunDataResultAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataResultAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.analysis_mode):
            body['analysisMode'] = request.analysis_mode
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.sql_data):
            body['sqlData'] = request.sql_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataResultAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/runDataResultAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataResultAnalysisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataResultAnalysisResponse(),
                self.execute(params, req, runtime)
            )

    async def run_data_result_analysis_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.RunDataResultAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataResultAnalysisResponse:
        """
        @summary 对结构化结果进行分析、可视化信息生成
        
        @param request: RunDataResultAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataResultAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.analysis_mode):
            body['analysisMode'] = request.analysis_mode
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.sql_data):
            body['sqlData'] = request.sql_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataResultAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/runDataResultAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataResultAnalysisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunDataResultAnalysisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_data_result_analysis(
        self,
        request: data_analysis_gbi20240823_models.RunDataResultAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataResultAnalysisResponse:
        """
        @summary 对结构化结果进行分析、可视化信息生成
        
        @param request: RunDataResultAnalysisRequest
        @return: RunDataResultAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_data_result_analysis_with_options(request, headers, runtime)

    async def run_data_result_analysis_async(
        self,
        request: data_analysis_gbi20240823_models.RunDataResultAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataResultAnalysisResponse:
        """
        @summary 对结构化结果进行分析、可视化信息生成
        
        @param request: RunDataResultAnalysisRequest
        @return: RunDataResultAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_data_result_analysis_with_options_async(request, headers, runtime)

    def run_sql_generation_with_options(
        self,
        request: data_analysis_gbi20240823_models.RunSqlGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunSqlGenerationResponse:
        """
        @summary 运行sql生成
        
        @param request: RunSqlGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSqlGenerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSqlGeneration',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/runSqlGeneration',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunSqlGenerationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunSqlGenerationResponse(),
                self.execute(params, req, runtime)
            )

    async def run_sql_generation_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.RunSqlGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunSqlGenerationResponse:
        """
        @summary 运行sql生成
        
        @param request: RunSqlGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSqlGenerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSqlGeneration',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/runSqlGeneration',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunSqlGenerationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.RunSqlGenerationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_sql_generation(
        self,
        request: data_analysis_gbi20240823_models.RunSqlGenerationRequest,
    ) -> data_analysis_gbi20240823_models.RunSqlGenerationResponse:
        """
        @summary 运行sql生成
        
        @param request: RunSqlGenerationRequest
        @return: RunSqlGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_sql_generation_with_options(request, headers, runtime)

    async def run_sql_generation_async(
        self,
        request: data_analysis_gbi20240823_models.RunSqlGenerationRequest,
    ) -> data_analysis_gbi20240823_models.RunSqlGenerationResponse:
        """
        @summary 运行sql生成
        
        @param request: RunSqlGenerationRequest
        @return: RunSqlGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_sql_generation_with_options_async(request, headers, runtime)

    def save_virtual_datasource_ddl_with_options(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveVirtualDatasourceDdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.ddl):
            body['ddl'] = request.ddl
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveVirtualDatasourceDdl',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/addDdl2VirtualInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
                self.execute(params, req, runtime)
            )

    async def save_virtual_datasource_ddl_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveVirtualDatasourceDdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.ddl):
            body['ddl'] = request.ddl
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveVirtualDatasourceDdl',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/addDdl2VirtualInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def save_virtual_datasource_ddl(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @return: SaveVirtualDatasourceDdlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_virtual_datasource_ddl_with_options(request, headers, runtime)

    async def save_virtual_datasource_ddl_async(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @return: SaveVirtualDatasourceDdlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_virtual_datasource_ddl_with_options_async(request, headers, runtime)

    def sync_remote_tables_with_options(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncRemoteTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep_table_names):
            body['keepTableNames'] = request.keep_table_names
        if not UtilClient.is_unset(request.no_modified_table_names):
            body['noModifiedTableNames'] = request.no_modified_table_names
        if not UtilClient.is_unset(request.pull_samples):
            body['pullSamples'] = request.pull_samples
        if not UtilClient.is_unset(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncRemoteTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/datasource/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
                self.execute(params, req, runtime)
            )

    async def sync_remote_tables_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncRemoteTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep_table_names):
            body['keepTableNames'] = request.keep_table_names
        if not UtilClient.is_unset(request.no_modified_table_names):
            body['noModifiedTableNames'] = request.no_modified_table_names
        if not UtilClient.is_unset(request.pull_samples):
            body['pullSamples'] = request.pull_samples
        if not UtilClient.is_unset(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncRemoteTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/datasource/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def sync_remote_tables(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @return: SyncRemoteTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_remote_tables_with_options(request, headers, runtime)

    async def sync_remote_tables_async(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @return: SyncRemoteTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_remote_tables_with_options_async(request, headers, runtime)

    def update_business_logic_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateBusinessLogicResponse:
        """
        @summary 修改当前指定业务空间下所指定的业务逻辑解释
        
        @param request: UpdateBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.business_logic_id_key):
            body['businessLogicIdKey'] = request.business_logic_id_key
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateBusinessLogicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateBusinessLogicResponse(),
                self.execute(params, req, runtime)
            )

    async def update_business_logic_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateBusinessLogicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateBusinessLogicResponse:
        """
        @summary 修改当前指定业务空间下所指定的业务逻辑解释
        
        @param request: UpdateBusinessLogicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBusinessLogicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.business_logic_id_key):
            body['businessLogicIdKey'] = request.business_logic_id_key
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBusinessLogic',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/logic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateBusinessLogicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateBusinessLogicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_business_logic(
        self,
        request: data_analysis_gbi20240823_models.UpdateBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.UpdateBusinessLogicResponse:
        """
        @summary 修改当前指定业务空间下所指定的业务逻辑解释
        
        @param request: UpdateBusinessLogicRequest
        @return: UpdateBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_business_logic_with_options(request, headers, runtime)

    async def update_business_logic_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateBusinessLogicRequest,
    ) -> data_analysis_gbi20240823_models.UpdateBusinessLogicResponse:
        """
        @summary 修改当前指定业务空间下所指定的业务逻辑解释
        
        @param request: UpdateBusinessLogicRequest
        @return: UpdateBusinessLogicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_business_logic_with_options_async(request, headers, runtime)

    def update_column_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateColumnResponse:
        """
        @summary 修改当前指定业务空间中，指定列的信息
        
        @param request: UpdateColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.chinese_name):
            body['chineseName'] = request.chinese_name
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enum_type):
            body['enumType'] = request.enum_type
        if not UtilClient.is_unset(request.enum_values):
            body['enumValues'] = request.enum_values
        if not UtilClient.is_unset(request.range_max):
            body['rangeMax'] = request.range_max
        if not UtilClient.is_unset(request.range_min):
            body['rangeMin'] = request.range_min
        if not UtilClient.is_unset(request.samples):
            body['samples'] = request.samples
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateColumnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateColumnResponse(),
                self.execute(params, req, runtime)
            )

    async def update_column_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateColumnRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateColumnResponse:
        """
        @summary 修改当前指定业务空间中，指定列的信息
        
        @param request: UpdateColumnRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.chinese_name):
            body['chineseName'] = request.chinese_name
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enum_type):
            body['enumType'] = request.enum_type
        if not UtilClient.is_unset(request.enum_values):
            body['enumValues'] = request.enum_values
        if not UtilClient.is_unset(request.range_max):
            body['rangeMax'] = request.range_max
        if not UtilClient.is_unset(request.range_min):
            body['rangeMin'] = request.range_min
        if not UtilClient.is_unset(request.samples):
            body['samples'] = request.samples
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateColumn',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/column',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateColumnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateColumnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_column(
        self,
        request: data_analysis_gbi20240823_models.UpdateColumnRequest,
    ) -> data_analysis_gbi20240823_models.UpdateColumnResponse:
        """
        @summary 修改当前指定业务空间中，指定列的信息
        
        @param request: UpdateColumnRequest
        @return: UpdateColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_column_with_options(request, headers, runtime)

    async def update_column_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateColumnRequest,
    ) -> data_analysis_gbi20240823_models.UpdateColumnResponse:
        """
        @summary 修改当前指定业务空间中，指定列的信息
        
        @param request: UpdateColumnRequest
        @return: UpdateColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_column_with_options_async(request, headers, runtime)

    def update_enum_mapping_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateEnumMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateEnumMappingResponse:
        """
        @summary 修改当前指定业务空间指定列下的枚举值信息
        
        @param request: UpdateEnumMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnumMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.enum_mapping):
            body['enumMapping'] = request.enum_mapping
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnumMapping',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateEnumMappingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateEnumMappingResponse(),
                self.execute(params, req, runtime)
            )

    async def update_enum_mapping_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateEnumMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateEnumMappingResponse:
        """
        @summary 修改当前指定业务空间指定列下的枚举值信息
        
        @param request: UpdateEnumMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnumMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.column_id_key):
            body['columnIdKey'] = request.column_id_key
        if not UtilClient.is_unset(request.enum_mapping):
            body['enumMapping'] = request.enum_mapping
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnumMapping',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/mapping',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateEnumMappingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateEnumMappingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_enum_mapping(
        self,
        request: data_analysis_gbi20240823_models.UpdateEnumMappingRequest,
    ) -> data_analysis_gbi20240823_models.UpdateEnumMappingResponse:
        """
        @summary 修改当前指定业务空间指定列下的枚举值信息
        
        @param request: UpdateEnumMappingRequest
        @return: UpdateEnumMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_enum_mapping_with_options(request, headers, runtime)

    async def update_enum_mapping_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateEnumMappingRequest,
    ) -> data_analysis_gbi20240823_models.UpdateEnumMappingResponse:
        """
        @summary 修改当前指定业务空间指定列下的枚举值信息
        
        @param request: UpdateEnumMappingRequest
        @return: UpdateEnumMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_enum_mapping_with_options_async(request, headers, runtime)

    def update_synonyms_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateSynonymsResponse:
        """
        @summary 修改当前业务空间指定的同义词信息
        
        @param request: UpdateSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['columns'] = request.columns
        if not UtilClient.is_unset(request.synonym_id_key):
            body['synonymIdKey'] = request.synonym_id_key
        if not UtilClient.is_unset(request.word):
            body['word'] = request.word
        if not UtilClient.is_unset(request.word_synonyms):
            body['wordSynonyms'] = request.word_synonyms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateSynonymsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateSynonymsResponse(),
                self.execute(params, req, runtime)
            )

    async def update_synonyms_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateSynonymsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateSynonymsResponse:
        """
        @summary 修改当前业务空间指定的同义词信息
        
        @param request: UpdateSynonymsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSynonymsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.columns):
            body['columns'] = request.columns
        if not UtilClient.is_unset(request.synonym_id_key):
            body['synonymIdKey'] = request.synonym_id_key
        if not UtilClient.is_unset(request.word):
            body['word'] = request.word
        if not UtilClient.is_unset(request.word_synonyms):
            body['wordSynonyms'] = request.word_synonyms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSynonyms',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/synonyms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateSynonymsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateSynonymsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_synonyms(
        self,
        request: data_analysis_gbi20240823_models.UpdateSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.UpdateSynonymsResponse:
        """
        @summary 修改当前业务空间指定的同义词信息
        
        @param request: UpdateSynonymsRequest
        @return: UpdateSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_synonyms_with_options(request, headers, runtime)

    async def update_synonyms_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateSynonymsRequest,
    ) -> data_analysis_gbi20240823_models.UpdateSynonymsResponse:
        """
        @summary 修改当前业务空间指定的同义词信息
        
        @param request: UpdateSynonymsRequest
        @return: UpdateSynonymsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_synonyms_with_options_async(request, headers, runtime)

    def update_table_info_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateTableInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateTableInfoResponse:
        """
        @summary 修改当前所指定的数据表的信息
        
        @param request: UpdateTableInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTableInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foreign_keys):
            body['foreignKeys'] = request.foreign_keys
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableInfo',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateTableInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateTableInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def update_table_info_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateTableInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateTableInfoResponse:
        """
        @summary 修改当前所指定的数据表的信息
        
        @param request: UpdateTableInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTableInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foreign_keys):
            body['foreignKeys'] = request.foreign_keys
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.table_id_key):
            body['tableIdKey'] = request.table_id_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableInfo',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/table',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateTableInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateTableInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_table_info(
        self,
        request: data_analysis_gbi20240823_models.UpdateTableInfoRequest,
    ) -> data_analysis_gbi20240823_models.UpdateTableInfoResponse:
        """
        @summary 修改当前所指定的数据表的信息
        
        @param request: UpdateTableInfoRequest
        @return: UpdateTableInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_info_with_options(request, headers, runtime)

    async def update_table_info_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateTableInfoRequest,
    ) -> data_analysis_gbi20240823_models.UpdateTableInfoResponse:
        """
        @summary 修改当前所指定的数据表的信息
        
        @param request: UpdateTableInfoRequest
        @return: UpdateTableInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_info_with_options_async(request, headers, runtime)

    def update_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/updateVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def update_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/updateVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_virtual_datasource_instance_with_options(request, headers, runtime)

    async def update_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_virtual_datasource_instance_with_options_async(request, headers, runtime)
