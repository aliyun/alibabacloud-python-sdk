# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appstream_center20210220 import models as appstream_center_20210220_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('appstream-center', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def refresh_login_token_with_options(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.RefreshLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_login_token_with_options_async(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_identifier):
            query['LoginIdentifier'] = request.login_identifier
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2021-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210220_models.RefreshLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_login_token(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_login_token_with_options(request, runtime)

    async def refresh_login_token_async(
        self,
        request: appstream_center_20210220_models.RefreshLoginTokenRequest,
    ) -> appstream_center_20210220_models.RefreshLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_login_token_with_options_async(request, runtime)
