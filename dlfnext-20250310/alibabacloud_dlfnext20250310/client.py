# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dlfnext20250310 import models as dlf_next_20250310_models
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
        self._endpoint = self.get_endpoint('dlfnext', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def alter_catalog_with_options(
        self,
        catalog: str,
        request: dlf_next_20250310_models.AlterCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.AlterCatalogResponse:
        """
        @summary 更新数据目录
        
        @param request: AlterCatalogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AlterCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.removals):
            body['removals'] = request.removals
        if not UtilClient.is_unset(request.updates):
            body['updates'] = request.updates
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AlterCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.AlterCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_catalog_with_options_async(
        self,
        catalog: str,
        request: dlf_next_20250310_models.AlterCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.AlterCatalogResponse:
        """
        @summary 更新数据目录
        
        @param request: AlterCatalogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AlterCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.removals):
            body['removals'] = request.removals
        if not UtilClient.is_unset(request.updates):
            body['updates'] = request.updates
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AlterCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.AlterCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_catalog(
        self,
        catalog: str,
        request: dlf_next_20250310_models.AlterCatalogRequest,
    ) -> dlf_next_20250310_models.AlterCatalogResponse:
        """
        @summary 更新数据目录
        
        @param request: AlterCatalogRequest
        @return: AlterCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.alter_catalog_with_options(catalog, request, headers, runtime)

    async def alter_catalog_async(
        self,
        catalog: str,
        request: dlf_next_20250310_models.AlterCatalogRequest,
    ) -> dlf_next_20250310_models.AlterCatalogResponse:
        """
        @summary 更新数据目录
        
        @param request: AlterCatalogRequest
        @return: AlterCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.alter_catalog_with_options_async(catalog, request, headers, runtime)

    def batch_grant_permissions_with_options(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.BatchGrantPermissionsResponse:
        """
        @summary 批量授权
        
        @param request: BatchGrantPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGrantPermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/batchgrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.BatchGrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_grant_permissions_with_options_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.BatchGrantPermissionsResponse:
        """
        @summary 批量授权
        
        @param request: BatchGrantPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGrantPermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/batchgrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.BatchGrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_grant_permissions(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchGrantPermissionsRequest,
    ) -> dlf_next_20250310_models.BatchGrantPermissionsResponse:
        """
        @summary 批量授权
        
        @param request: BatchGrantPermissionsRequest
        @return: BatchGrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_grant_permissions_with_options(catalog_id, request, headers, runtime)

    async def batch_grant_permissions_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchGrantPermissionsRequest,
    ) -> dlf_next_20250310_models.BatchGrantPermissionsResponse:
        """
        @summary 批量授权
        
        @param request: BatchGrantPermissionsRequest
        @return: BatchGrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_grant_permissions_with_options_async(catalog_id, request, headers, runtime)

    def batch_revoke_permissions_with_options(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.BatchRevokePermissionsResponse:
        """
        @summary 批量取消授权
        
        @param request: BatchRevokePermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchRevokePermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRevokePermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/batchrevoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.BatchRevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_revoke_permissions_with_options_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.BatchRevokePermissionsResponse:
        """
        @summary 批量取消授权
        
        @param request: BatchRevokePermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchRevokePermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRevokePermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/batchrevoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.BatchRevokePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_revoke_permissions(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchRevokePermissionsRequest,
    ) -> dlf_next_20250310_models.BatchRevokePermissionsResponse:
        """
        @summary 批量取消授权
        
        @param request: BatchRevokePermissionsRequest
        @return: BatchRevokePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_revoke_permissions_with_options(catalog_id, request, headers, runtime)

    async def batch_revoke_permissions_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.BatchRevokePermissionsRequest,
    ) -> dlf_next_20250310_models.BatchRevokePermissionsResponse:
        """
        @summary 批量取消授权
        
        @param request: BatchRevokePermissionsRequest
        @return: BatchRevokePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_revoke_permissions_with_options_async(catalog_id, request, headers, runtime)

    def create_catalog_with_options(
        self,
        request: dlf_next_20250310_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.CreateCatalogResponse:
        """
        @summary 创建数据目录
        
        @param request: CreateCatalogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.optimization_config):
            body['optimizationConfig'] = request.optimization_config
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.CreateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_catalog_with_options_async(
        self,
        request: dlf_next_20250310_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.CreateCatalogResponse:
        """
        @summary 创建数据目录
        
        @param request: CreateCatalogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCatalogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.optimization_config):
            body['optimizationConfig'] = request.optimization_config
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.CreateCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_catalog(
        self,
        request: dlf_next_20250310_models.CreateCatalogRequest,
    ) -> dlf_next_20250310_models.CreateCatalogResponse:
        """
        @summary 创建数据目录
        
        @param request: CreateCatalogRequest
        @return: CreateCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_catalog_with_options(request, headers, runtime)

    async def create_catalog_async(
        self,
        request: dlf_next_20250310_models.CreateCatalogRequest,
    ) -> dlf_next_20250310_models.CreateCatalogResponse:
        """
        @summary 创建数据目录
        
        @param request: CreateCatalogRequest
        @return: CreateCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_catalog_with_options_async(request, headers, runtime)

    def create_role_with_options(
        self,
        request: dlf_next_20250310_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.CreateRoleResponse:
        """
        @summary 创建角色
        
        @param request: CreateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: dlf_next_20250310_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.CreateRoleResponse:
        """
        @summary 创建角色
        
        @param request: CreateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: dlf_next_20250310_models.CreateRoleRequest,
    ) -> dlf_next_20250310_models.CreateRoleResponse:
        """
        @summary 创建角色
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(request, headers, runtime)

    async def create_role_async(
        self,
        request: dlf_next_20250310_models.CreateRoleRequest,
    ) -> dlf_next_20250310_models.CreateRoleResponse:
        """
        @summary 创建角色
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(request, headers, runtime)

    def delete_role_with_options(
        self,
        request: dlf_next_20250310_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: dlf_next_20250310_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: dlf_next_20250310_models.DeleteRoleRequest,
    ) -> dlf_next_20250310_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    async def delete_role_async(
        self,
        request: dlf_next_20250310_models.DeleteRoleRequest,
    ) -> dlf_next_20250310_models.DeleteRoleResponse:
        """
        @summary 删除角色
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DescribeRegionsResponse:
        """
        @summary 查询 DLF 开通地域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DescribeRegionsResponse:
        """
        @summary 查询 DLF 开通地域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> dlf_next_20250310_models.DescribeRegionsResponse:
        """
        @summary 查询 DLF 开通地域
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> dlf_next_20250310_models.DescribeRegionsResponse:
        """
        @summary 查询 DLF 开通地域
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def drop_catalog_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DropCatalogResponse:
        """
        @summary 创建数据湖Catalog
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DropCatalogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DropCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DropCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_catalog_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.DropCatalogResponse:
        """
        @summary 创建数据湖Catalog
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DropCatalogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DropCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.DropCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_catalog(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.DropCatalogResponse:
        """
        @summary 创建数据湖Catalog
        
        @return: DropCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.drop_catalog_with_options(catalog, headers, runtime)

    async def drop_catalog_async(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.DropCatalogResponse:
        """
        @summary 创建数据湖Catalog
        
        @return: DropCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.drop_catalog_with_options_async(catalog, headers, runtime)

    def get_catalog_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogResponse:
        """
        @summary 查看数据湖Catalog
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogResponse:
        """
        @summary 查看数据湖Catalog
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalog',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.GetCatalogResponse:
        """
        @summary 查看数据湖Catalog
        
        @return: GetCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_with_options(catalog, headers, runtime)

    async def get_catalog_async(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.GetCatalogResponse:
        """
        @summary 查看数据湖Catalog
        
        @return: GetCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_with_options_async(catalog, headers, runtime)

    def get_catalog_summary_with_options(
        self,
        catalog_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalogSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_summary_with_options_async(
        self,
        catalog_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalogSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_summary(
        self,
        catalog_id: str,
    ) -> dlf_next_20250310_models.GetCatalogSummaryResponse:
        """
        @summary 查看表
        
        @return: GetCatalogSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_summary_with_options(catalog_id, headers, runtime)

    async def get_catalog_summary_async(
        self,
        catalog_id: str,
    ) -> dlf_next_20250310_models.GetCatalogSummaryResponse:
        """
        @summary 查看表
        
        @return: GetCatalogSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_summary_with_options_async(catalog_id, headers, runtime)

    def get_catalog_summary_trend_with_options(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.GetCatalogSummaryTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogSummaryTrendResponse:
        """
        @summary 查看表
        
        @param request: GetCatalogSummaryTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogSummaryTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogSummaryTrend',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/storage-summary/trend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogSummaryTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_summary_trend_with_options_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.GetCatalogSummaryTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogSummaryTrendResponse:
        """
        @summary 查看表
        
        @param request: GetCatalogSummaryTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogSummaryTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogSummaryTrend',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/storage-summary/trend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogSummaryTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_summary_trend(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.GetCatalogSummaryTrendRequest,
    ) -> dlf_next_20250310_models.GetCatalogSummaryTrendResponse:
        """
        @summary 查看表
        
        @param request: GetCatalogSummaryTrendRequest
        @return: GetCatalogSummaryTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_summary_trend_with_options(catalog_id, request, headers, runtime)

    async def get_catalog_summary_trend_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.GetCatalogSummaryTrendRequest,
    ) -> dlf_next_20250310_models.GetCatalogSummaryTrendResponse:
        """
        @summary 查看表
        
        @param request: GetCatalogSummaryTrendRequest
        @return: GetCatalogSummaryTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_summary_trend_with_options_async(catalog_id, request, headers, runtime)

    def get_catalog_token_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogTokenResponse:
        """
        @summary 获取数据湖Catalog的临时访问凭证
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalogToken',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_token_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetCatalogTokenResponse:
        """
        @summary 获取数据湖Catalog的临时访问凭证
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCatalogToken',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs/{OpenApiUtilClient.get_encode_param(catalog)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetCatalogTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_token(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.GetCatalogTokenResponse:
        """
        @summary 获取数据湖Catalog的临时访问凭证
        
        @return: GetCatalogTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_token_with_options(catalog, headers, runtime)

    async def get_catalog_token_async(
        self,
        catalog: str,
    ) -> dlf_next_20250310_models.GetCatalogTokenResponse:
        """
        @summary 获取数据湖Catalog的临时访问凭证
        
        @return: GetCatalogTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_token_with_options_async(catalog, headers, runtime)

    def get_database_summary_with_options(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetDatabaseSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatabaseSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetDatabaseSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_summary_with_options_async(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetDatabaseSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatabaseSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetDatabaseSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_summary(
        self,
        catalog_id: str,
        database: str,
    ) -> dlf_next_20250310_models.GetDatabaseSummaryResponse:
        """
        @summary 查看表
        
        @return: GetDatabaseSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_database_summary_with_options(catalog_id, database, headers, runtime)

    async def get_database_summary_async(
        self,
        catalog_id: str,
        database: str,
    ) -> dlf_next_20250310_models.GetDatabaseSummaryResponse:
        """
        @summary 查看表
        
        @return: GetDatabaseSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_database_summary_with_options_async(catalog_id, database, headers, runtime)

    def get_region_status_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetRegionStatusResponse:
        """
        @summary 查询 DLF 当前地域开通状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegionStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionStatus',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetRegionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_status_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetRegionStatusResponse:
        """
        @summary 查询 DLF 当前地域开通状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegionStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionStatus',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetRegionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_status(self) -> dlf_next_20250310_models.GetRegionStatusResponse:
        """
        @summary 查询 DLF 当前地域开通状态
        
        @return: GetRegionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_status_with_options(headers, runtime)

    async def get_region_status_async(self) -> dlf_next_20250310_models.GetRegionStatusResponse:
        """
        @summary 查询 DLF 当前地域开通状态
        
        @return: GetRegionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_region_status_with_options_async(headers, runtime)

    def get_role_with_options(
        self,
        request: dlf_next_20250310_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetRoleResponse:
        """
        @summary 获取角色
        
        @param request: GetRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: dlf_next_20250310_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetRoleResponse:
        """
        @summary 获取角色
        
        @param request: GetRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: dlf_next_20250310_models.GetRoleRequest,
    ) -> dlf_next_20250310_models.GetRoleResponse:
        """
        @summary 获取角色
        
        @param request: GetRoleRequest
        @return: GetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_with_options(request, headers, runtime)

    async def get_role_async(
        self,
        request: dlf_next_20250310_models.GetRoleRequest,
    ) -> dlf_next_20250310_models.GetRoleResponse:
        """
        @summary 获取角色
        
        @param request: GetRoleRequest
        @return: GetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_with_options_async(request, headers, runtime)

    def get_table_summary_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetTableSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetTableSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_summary_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetTableSummaryResponse:
        """
        @summary 查看表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableSummaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableSummary',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table)}/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetTableSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_summary(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> dlf_next_20250310_models.GetTableSummaryResponse:
        """
        @summary 查看表
        
        @return: GetTableSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_summary_with_options(catalog_id, database, table, headers, runtime)

    async def get_table_summary_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> dlf_next_20250310_models.GetTableSummaryResponse:
        """
        @summary 查看表
        
        @return: GetTableSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_summary_with_options_async(catalog_id, database, table, headers, runtime)

    def get_user_with_options(
        self,
        request: dlf_next_20250310_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetUserResponse:
        """
        @summary 获取用户
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: dlf_next_20250310_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GetUserResponse:
        """
        @summary 获取用户
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: dlf_next_20250310_models.GetUserRequest,
    ) -> dlf_next_20250310_models.GetUserResponse:
        """
        @summary 获取用户
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: dlf_next_20250310_models.GetUserRequest,
    ) -> dlf_next_20250310_models.GetUserResponse:
        """
        @summary 获取用户
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: dlf_next_20250310_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GrantRoleToUsersResponse:
        """
        @summary 批量授予角色权限给用户
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: dlf_next_20250310_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.GrantRoleToUsersResponse:
        """
        @summary 批量授予角色权限给用户
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: dlf_next_20250310_models.GrantRoleToUsersRequest,
    ) -> dlf_next_20250310_models.GrantRoleToUsersResponse:
        """
        @summary 批量授予角色权限给用户
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: dlf_next_20250310_models.GrantRoleToUsersRequest,
    ) -> dlf_next_20250310_models.GrantRoleToUsersResponse:
        """
        @summary 批量授予角色权限给用户
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def list_catalogs_with_options(
        self,
        request: dlf_next_20250310_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListCatalogsResponse:
        """
        @summary 查看数据目录列表
        
        @param request: ListCatalogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name_pattern):
            query['catalogNamePattern'] = request.catalog_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        request: dlf_next_20250310_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListCatalogsResponse:
        """
        @summary 查看数据目录列表
        
        @param request: ListCatalogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name_pattern):
            query['catalogNamePattern'] = request.catalog_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        request: dlf_next_20250310_models.ListCatalogsRequest,
    ) -> dlf_next_20250310_models.ListCatalogsResponse:
        """
        @summary 查看数据目录列表
        
        @param request: ListCatalogsRequest
        @return: ListCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(request, headers, runtime)

    async def list_catalogs_async(
        self,
        request: dlf_next_20250310_models.ListCatalogsRequest,
    ) -> dlf_next_20250310_models.ListCatalogsResponse:
        """
        @summary 查看数据目录列表
        
        @param request: ListCatalogsRequest
        @return: ListCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_catalogs_with_options_async(request, headers, runtime)

    def list_partition_summaries_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: dlf_next_20250310_models.ListPartitionSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListPartitionSummariesResponse:
        """
        @summary 查看表
        
        @param request: ListPartitionSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPartitionSummariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPartitionSummaries',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table)}/partitions/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListPartitionSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partition_summaries_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: dlf_next_20250310_models.ListPartitionSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListPartitionSummariesResponse:
        """
        @summary 查看表
        
        @param request: ListPartitionSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPartitionSummariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPartitionSummaries',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/{OpenApiUtilClient.get_encode_param(catalog_id)}/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table)}/partitions/storage-summary',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListPartitionSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partition_summaries(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: dlf_next_20250310_models.ListPartitionSummariesRequest,
    ) -> dlf_next_20250310_models.ListPartitionSummariesResponse:
        """
        @summary 查看表
        
        @param request: ListPartitionSummariesRequest
        @return: ListPartitionSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partition_summaries_with_options(catalog_id, database, table, request, headers, runtime)

    async def list_partition_summaries_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: dlf_next_20250310_models.ListPartitionSummariesRequest,
    ) -> dlf_next_20250310_models.ListPartitionSummariesResponse:
        """
        @summary 查看表
        
        @param request: ListPartitionSummariesRequest
        @return: ListPartitionSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_partition_summaries_with_options_async(catalog_id, database, table, request, headers, runtime)

    def list_permissions_with_options(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListPermissionsResponse:
        """
        @summary 获取指定资源或指定Principal的权限信息
        
        @param request: ListPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database):
            query['database'] = request.database
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.principal):
            query['principal'] = request.principal
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.table):
            query['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListPermissionsResponse:
        """
        @summary 获取指定资源或指定Principal的权限信息
        
        @param request: ListPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database):
            query['database'] = request.database
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.principal):
            query['principal'] = request.principal
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.table):
            query['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/permissions/{OpenApiUtilClient.get_encode_param(catalog_id)}/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.ListPermissionsRequest,
    ) -> dlf_next_20250310_models.ListPermissionsResponse:
        """
        @summary 获取指定资源或指定Principal的权限信息
        
        @param request: ListPermissionsRequest
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(catalog_id, request, headers, runtime)

    async def list_permissions_async(
        self,
        catalog_id: str,
        request: dlf_next_20250310_models.ListPermissionsRequest,
    ) -> dlf_next_20250310_models.ListPermissionsResponse:
        """
        @summary 获取指定资源或指定Principal的权限信息
        
        @param request: ListPermissionsRequest
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_permissions_with_options_async(catalog_id, request, headers, runtime)

    def list_role_users_with_options(
        self,
        request: dlf_next_20250310_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListRoleUsersResponse:
        """
        @summary 获取角色用户列表
        
        @param request: ListRoleUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoleUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/users/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_users_with_options_async(
        self,
        request: dlf_next_20250310_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListRoleUsersResponse:
        """
        @summary 获取角色用户列表
        
        @param request: ListRoleUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoleUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/users/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role_users(
        self,
        request: dlf_next_20250310_models.ListRoleUsersRequest,
    ) -> dlf_next_20250310_models.ListRoleUsersResponse:
        """
        @summary 获取角色用户列表
        
        @param request: ListRoleUsersRequest
        @return: ListRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_role_users_with_options(request, headers, runtime)

    async def list_role_users_async(
        self,
        request: dlf_next_20250310_models.ListRoleUsersRequest,
    ) -> dlf_next_20250310_models.ListRoleUsersResponse:
        """
        @summary 获取角色用户列表
        
        @param request: ListRoleUsersRequest
        @return: ListRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_role_users_with_options_async(request, headers, runtime)

    def list_roles_with_options(
        self,
        request: dlf_next_20250310_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListRolesResponse:
        """
        @summary 获取角色列表
        
        @param request: ListRolesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.role_name):
            query['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: dlf_next_20250310_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListRolesResponse:
        """
        @summary 获取角色列表
        
        @param request: ListRolesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.role_name):
            query['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: dlf_next_20250310_models.ListRolesRequest,
    ) -> dlf_next_20250310_models.ListRolesResponse:
        """
        @summary 获取角色列表
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(request, headers, runtime)

    async def list_roles_async(
        self,
        request: dlf_next_20250310_models.ListRolesRequest,
    ) -> dlf_next_20250310_models.ListRolesResponse:
        """
        @summary 获取角色列表
        
        @param request: ListRolesRequest
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(request, headers, runtime)

    def list_user_roles_with_options(
        self,
        request: dlf_next_20250310_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListUserRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListUserRolesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRoles',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_roles_with_options_async(
        self,
        request: dlf_next_20250310_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListUserRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListUserRolesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRoles',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_roles(
        self,
        request: dlf_next_20250310_models.ListUserRolesRequest,
    ) -> dlf_next_20250310_models.ListUserRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListUserRolesRequest
        @return: ListUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_roles_with_options(request, headers, runtime)

    async def list_user_roles_async(
        self,
        request: dlf_next_20250310_models.ListUserRolesRequest,
    ) -> dlf_next_20250310_models.ListUserRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListUserRolesRequest
        @return: ListUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_roles_with_options_async(request, headers, runtime)

    def list_users_with_options(
        self,
        request: dlf_next_20250310_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListUsersResponse:
        """
        @summary 获取用户列表
        
        @param request: ListUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            query['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: dlf_next_20250310_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.ListUsersResponse:
        """
        @summary 获取用户列表
        
        @param request: ListUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['pageToken'] = request.page_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            query['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/users/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: dlf_next_20250310_models.ListUsersRequest,
    ) -> dlf_next_20250310_models.ListUsersResponse:
        """
        @summary 获取用户列表
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: dlf_next_20250310_models.ListUsersRequest,
    ) -> dlf_next_20250310_models.ListUsersResponse:
        """
        @summary 获取用户列表
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def revoke_role_from_users_with_options(
        self,
        request: dlf_next_20250310_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.RevokeRoleFromUsersResponse:
        """
        @summary 批量取消授予角色权限给用户
        
        @param request: RevokeRoleFromUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeRoleFromUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRoleFromUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.RevokeRoleFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_role_from_users_with_options_async(
        self,
        request: dlf_next_20250310_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.RevokeRoleFromUsersResponse:
        """
        @summary 批量取消授予角色权限给用户
        
        @param request: RevokeRoleFromUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeRoleFromUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRoleFromUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.RevokeRoleFromUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_role_from_users(
        self,
        request: dlf_next_20250310_models.RevokeRoleFromUsersRequest,
    ) -> dlf_next_20250310_models.RevokeRoleFromUsersResponse:
        """
        @summary 批量取消授予角色权限给用户
        
        @param request: RevokeRoleFromUsersRequest
        @return: RevokeRoleFromUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_role_from_users_with_options(request, headers, runtime)

    async def revoke_role_from_users_async(
        self,
        request: dlf_next_20250310_models.RevokeRoleFromUsersRequest,
    ) -> dlf_next_20250310_models.RevokeRoleFromUsersResponse:
        """
        @summary 批量取消授予角色权限给用户
        
        @param request: RevokeRoleFromUsersRequest
        @return: RevokeRoleFromUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_role_from_users_with_options_async(request, headers, runtime)

    def subscribe_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.SubscribeResponse:
        """
        @summary 订阅当前地域的 DLF
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Subscribe',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/subscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.SubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.SubscribeResponse:
        """
        @summary 订阅当前地域的 DLF
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Subscribe',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/service/subscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.SubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe(self) -> dlf_next_20250310_models.SubscribeResponse:
        """
        @summary 订阅当前地域的 DLF
        
        @return: SubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.subscribe_with_options(headers, runtime)

    async def subscribe_async(self) -> dlf_next_20250310_models.SubscribeResponse:
        """
        @summary 订阅当前地域的 DLF
        
        @return: SubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.subscribe_with_options_async(headers, runtime)

    def update_role_with_options(
        self,
        request: dlf_next_20250310_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.UpdateRoleResponse:
        """
        @summary 更新角色
        
        @param request: UpdateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: dlf_next_20250310_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.UpdateRoleResponse:
        """
        @summary 更新角色
        
        @param request: UpdateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: dlf_next_20250310_models.UpdateRoleRequest,
    ) -> dlf_next_20250310_models.UpdateRoleResponse:
        """
        @summary 更新角色
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    async def update_role_async(
        self,
        request: dlf_next_20250310_models.UpdateRoleRequest,
    ) -> dlf_next_20250310_models.UpdateRoleResponse:
        """
        @summary 更新角色
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(request, headers, runtime)

    def update_role_users_with_options(
        self,
        request: dlf_next_20250310_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.UpdateRoleUsersResponse:
        """
        @summary 更新角色用户
        
        @param request: UpdateRoleUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoleUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.UpdateRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_users_with_options_async(
        self,
        request: dlf_next_20250310_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dlf_next_20250310_models.UpdateRoleUsersResponse:
        """
        @summary 更新角色用户
        
        @param request: UpdateRoleUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not UtilClient.is_unset(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoleUsers',
            version='2025-03-10',
            protocol='HTTPS',
            pathname=f'/dlf/v1/auth/roles/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            dlf_next_20250310_models.UpdateRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role_users(
        self,
        request: dlf_next_20250310_models.UpdateRoleUsersRequest,
    ) -> dlf_next_20250310_models.UpdateRoleUsersResponse:
        """
        @summary 更新角色用户
        
        @param request: UpdateRoleUsersRequest
        @return: UpdateRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_users_with_options(request, headers, runtime)

    async def update_role_users_async(
        self,
        request: dlf_next_20250310_models.UpdateRoleUsersRequest,
    ) -> dlf_next_20250310_models.UpdateRoleUsersResponse:
        """
        @summary 更新角色用户
        
        @param request: UpdateRoleUsersRequest
        @return: UpdateRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_role_users_with_options_async(request, headers, runtime)
