# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_osssddp20240222 import models as oss_sddp_20240222_models
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
        self._endpoint = self.get_endpoint('osssddp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_sddp_version_with_options(
        self,
        request: oss_sddp_20240222_models.GetSddpVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_sddp_20240222_models.GetSddpVersionResponse:
        """
        @summary 查看用户的敏感数据保护版本信息
        
        @param request: GetSddpVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSddpVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSddpVersion',
            version='2024-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_sddp_20240222_models.GetSddpVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sddp_version_with_options_async(
        self,
        request: oss_sddp_20240222_models.GetSddpVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_sddp_20240222_models.GetSddpVersionResponse:
        """
        @summary 查看用户的敏感数据保护版本信息
        
        @param request: GetSddpVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSddpVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSddpVersion',
            version='2024-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_sddp_20240222_models.GetSddpVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sddp_version(
        self,
        request: oss_sddp_20240222_models.GetSddpVersionRequest,
    ) -> oss_sddp_20240222_models.GetSddpVersionResponse:
        """
        @summary 查看用户的敏感数据保护版本信息
        
        @param request: GetSddpVersionRequest
        @return: GetSddpVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sddp_version_with_options(request, runtime)

    async def get_sddp_version_async(
        self,
        request: oss_sddp_20240222_models.GetSddpVersionRequest,
    ) -> oss_sddp_20240222_models.GetSddpVersionResponse:
        """
        @summary 查看用户的敏感数据保护版本信息
        
        @param request: GetSddpVersionRequest
        @return: GetSddpVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sddp_version_with_options_async(request, runtime)

    def upgrade_sddp_version_with_options(
        self,
        request: oss_sddp_20240222_models.UpgradeSddpVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_sddp_20240222_models.UpgradeSddpVersionResponse:
        """
        @summary 升级敏感数据保护版本
        
        @param request: UpgradeSddpVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeSddpVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.oss_version):
            query['OssVersion'] = request.oss_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSddpVersion',
            version='2024-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_sddp_20240222_models.UpgradeSddpVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_sddp_version_with_options_async(
        self,
        request: oss_sddp_20240222_models.UpgradeSddpVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_sddp_20240222_models.UpgradeSddpVersionResponse:
        """
        @summary 升级敏感数据保护版本
        
        @param request: UpgradeSddpVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeSddpVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.oss_version):
            query['OssVersion'] = request.oss_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeSddpVersion',
            version='2024-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_sddp_20240222_models.UpgradeSddpVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_sddp_version(
        self,
        request: oss_sddp_20240222_models.UpgradeSddpVersionRequest,
    ) -> oss_sddp_20240222_models.UpgradeSddpVersionResponse:
        """
        @summary 升级敏感数据保护版本
        
        @param request: UpgradeSddpVersionRequest
        @return: UpgradeSddpVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_sddp_version_with_options(request, runtime)

    async def upgrade_sddp_version_async(
        self,
        request: oss_sddp_20240222_models.UpgradeSddpVersionRequest,
    ) -> oss_sddp_20240222_models.UpgradeSddpVersionResponse:
        """
        @summary 升级敏感数据保护版本
        
        @param request: UpgradeSddpVersionRequest
        @return: UpgradeSddpVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_sddp_version_with_options_async(request, runtime)
