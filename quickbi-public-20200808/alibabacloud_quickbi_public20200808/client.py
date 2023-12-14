# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quickbi_public20200808 import models as quickbi_public_20200808_models
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

    def authorize_menu_with_options(
        self,
        request: quickbi_public_20200808_models.AuthorizeMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.AuthorizeMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMenu',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.AuthorizeMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_menu_with_options_async(
        self,
        request: quickbi_public_20200808_models.AuthorizeMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.AuthorizeMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMenu',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.AuthorizeMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_menu(
        self,
        request: quickbi_public_20200808_models.AuthorizeMenuRequest,
    ) -> quickbi_public_20200808_models.AuthorizeMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_menu_with_options(request, runtime)

    async def authorize_menu_async(
        self,
        request: quickbi_public_20200808_models.AuthorizeMenuRequest,
    ) -> quickbi_public_20200808_models.AuthorizeMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_menu_with_options_async(request, runtime)

    def cancel_authorization_menu_with_options(
        self,
        request: quickbi_public_20200808_models.CancelAuthorizationMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.CancelAuthorizationMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAuthorizationMenu',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.CancelAuthorizationMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_authorization_menu_with_options_async(
        self,
        request: quickbi_public_20200808_models.CancelAuthorizationMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.CancelAuthorizationMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAuthorizationMenu',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.CancelAuthorizationMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_authorization_menu(
        self,
        request: quickbi_public_20200808_models.CancelAuthorizationMenuRequest,
    ) -> quickbi_public_20200808_models.CancelAuthorizationMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_authorization_menu_with_options(request, runtime)

    async def cancel_authorization_menu_async(
        self,
        request: quickbi_public_20200808_models.CancelAuthorizationMenuRequest,
    ) -> quickbi_public_20200808_models.CancelAuthorizationMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_authorization_menu_with_options_async(request, runtime)

    def change_visibility_model_with_options(
        self,
        request: quickbi_public_20200808_models.ChangeVisibilityModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ChangeVisibilityModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibilityModel',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ChangeVisibilityModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_visibility_model_with_options_async(
        self,
        request: quickbi_public_20200808_models.ChangeVisibilityModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ChangeVisibilityModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibilityModel',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ChangeVisibilityModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_visibility_model(
        self,
        request: quickbi_public_20200808_models.ChangeVisibilityModelRequest,
    ) -> quickbi_public_20200808_models.ChangeVisibilityModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_visibility_model_with_options(request, runtime)

    async def change_visibility_model_async(
        self,
        request: quickbi_public_20200808_models.ChangeVisibilityModelRequest,
    ) -> quickbi_public_20200808_models.ChangeVisibilityModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_visibility_model_with_options_async(request, runtime)

    def list_portal_menu_authorization_with_options(
        self,
        request: quickbi_public_20200808_models.ListPortalMenuAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenuAuthorization',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menu_authorization_with_options_async(
        self,
        request: quickbi_public_20200808_models.ListPortalMenuAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenuAuthorization',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menu_authorization(
        self,
        request: quickbi_public_20200808_models.ListPortalMenuAuthorizationRequest,
    ) -> quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menu_authorization_with_options(request, runtime)

    async def list_portal_menu_authorization_async(
        self,
        request: quickbi_public_20200808_models.ListPortalMenuAuthorizationRequest,
    ) -> quickbi_public_20200808_models.ListPortalMenuAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menu_authorization_with_options_async(request, runtime)

    def list_portal_menus_with_options(
        self,
        request: quickbi_public_20200808_models.ListPortalMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ListPortalMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenus',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ListPortalMenusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menus_with_options_async(
        self,
        request: quickbi_public_20200808_models.ListPortalMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20200808_models.ListPortalMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenus',
            version='2020-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20200808_models.ListPortalMenusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menus(
        self,
        request: quickbi_public_20200808_models.ListPortalMenusRequest,
    ) -> quickbi_public_20200808_models.ListPortalMenusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menus_with_options(request, runtime)

    async def list_portal_menus_async(
        self,
        request: quickbi_public_20200808_models.ListPortalMenusRequest,
    ) -> quickbi_public_20200808_models.ListPortalMenusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menus_with_options_async(request, runtime)
