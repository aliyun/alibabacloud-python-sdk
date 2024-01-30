# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_dms_yaochi_portal20230206 import models as dms_yaochi_portal_20230206_models
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
        self._endpoint = self.get_endpoint('dms-yaochi-portal', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_user_auth_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.CheckUserAuthResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckUserAuth',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.CheckUserAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_auth_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.CheckUserAuthResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckUserAuth',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.CheckUserAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_auth(self) -> dms_yaochi_portal_20230206_models.CheckUserAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_user_auth_with_options(runtime)

    async def check_user_auth_async(self) -> dms_yaochi_portal_20230206_models.CheckUserAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_user_auth_with_options_async(runtime)

    def list_resources_by_tag_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListResourcesByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not UtilClient.is_unset(request.tag_values):
            query['TagValues'] = request.tag_values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByTag',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListResourcesByTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_tag_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.ListResourcesByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListResourcesByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not UtilClient.is_unset(request.tag_values):
            query['TagValues'] = request.tag_values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByTag',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListResourcesByTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_tag(
        self,
        request: dms_yaochi_portal_20230206_models.ListResourcesByTagRequest,
    ) -> dms_yaochi_portal_20230206_models.ListResourcesByTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_tag_with_options(request, runtime)

    async def list_resources_by_tag_async(
        self,
        request: dms_yaochi_portal_20230206_models.ListResourcesByTagRequest,
    ) -> dms_yaochi_portal_20230206_models.ListResourcesByTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_by_tag_with_options_async(request, runtime)

    def list_tags_all_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListTagsAllResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListTagsAll',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListTagsAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_all_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListTagsAllResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListTagsAll',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListTagsAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_all(self) -> dms_yaochi_portal_20230206_models.ListTagsAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_all_with_options(runtime)

    async def list_tags_all_async(self) -> dms_yaochi_portal_20230206_models.ListTagsAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_all_with_options_async(runtime)

    def list_tags_by_resource_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.ListTagsByResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListTagsByResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsByResource',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListTagsByResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_by_resource_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.ListTagsByResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.ListTagsByResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsByResource',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.ListTagsByResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_by_resource(
        self,
        request: dms_yaochi_portal_20230206_models.ListTagsByResourceRequest,
    ) -> dms_yaochi_portal_20230206_models.ListTagsByResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_by_resource_with_options(request, runtime)

    async def list_tags_by_resource_async(
        self,
        request: dms_yaochi_portal_20230206_models.ListTagsByResourceRequest,
    ) -> dms_yaochi_portal_20230206_models.ListTagsByResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_by_resource_with_options_async(request, runtime)

    def meta_database_search_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.MetaDatabaseSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MetaDatabaseSearch',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def meta_database_search_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.MetaDatabaseSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MetaDatabaseSearch',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def meta_database_search(
        self,
        request: dms_yaochi_portal_20230206_models.MetaDatabaseSearchRequest,
    ) -> dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.meta_database_search_with_options(request, runtime)

    async def meta_database_search_async(
        self,
        request: dms_yaochi_portal_20230206_models.MetaDatabaseSearchRequest,
    ) -> dms_yaochi_portal_20230206_models.MetaDatabaseSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.meta_database_search_with_options_async(request, runtime)

    def meta_search_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.MetaSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.MetaSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MetaSearch',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.MetaSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def meta_search_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.MetaSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.MetaSearchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MetaSearch',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.MetaSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def meta_search(
        self,
        request: dms_yaochi_portal_20230206_models.MetaSearchRequest,
    ) -> dms_yaochi_portal_20230206_models.MetaSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.meta_search_with_options(request, runtime)

    async def meta_search_async(
        self,
        request: dms_yaochi_portal_20230206_models.MetaSearchRequest,
    ) -> dms_yaochi_portal_20230206_models.MetaSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.meta_search_with_options_async(request, runtime)

    def update_user_auth_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.UpdateUserAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.UpdateUserAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_state):
            query['GrantState'] = request.grant_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserAuth',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.UpdateUserAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_auth_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.UpdateUserAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.UpdateUserAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_state):
            query['GrantState'] = request.grant_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserAuth',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.UpdateUserAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_auth(
        self,
        request: dms_yaochi_portal_20230206_models.UpdateUserAuthRequest,
    ) -> dms_yaochi_portal_20230206_models.UpdateUserAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_auth_with_options(request, runtime)

    async def update_user_auth_async(
        self,
        request: dms_yaochi_portal_20230206_models.UpdateUserAuthRequest,
    ) -> dms_yaochi_portal_20230206_models.UpdateUserAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_auth_with_options_async(request, runtime)

    def yaochi_suggest_with_options(
        self,
        request: dms_yaochi_portal_20230206_models.YaochiSuggestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.YaochiSuggestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.suggest_text):
            query['SuggestText'] = request.suggest_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='YaochiSuggest',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.YaochiSuggestResponse(),
            self.call_api(params, req, runtime)
        )

    async def yaochi_suggest_with_options_async(
        self,
        request: dms_yaochi_portal_20230206_models.YaochiSuggestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_yaochi_portal_20230206_models.YaochiSuggestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.suggest_text):
            query['SuggestText'] = request.suggest_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='YaochiSuggest',
            version='2023-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_yaochi_portal_20230206_models.YaochiSuggestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def yaochi_suggest(
        self,
        request: dms_yaochi_portal_20230206_models.YaochiSuggestRequest,
    ) -> dms_yaochi_portal_20230206_models.YaochiSuggestResponse:
        runtime = util_models.RuntimeOptions()
        return self.yaochi_suggest_with_options(request, runtime)

    async def yaochi_suggest_async(
        self,
        request: dms_yaochi_portal_20230206_models.YaochiSuggestRequest,
    ) -> dms_yaochi_portal_20230206_models.YaochiSuggestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.yaochi_suggest_with_options_async(request, runtime)
