# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs_workbench20251111 import models as ecs_workbench_20251111_models
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
        self._endpoint = self.get_endpoint('ecs-workbench', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_terminal_settings_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20251111_models.DescribeTerminalSettingsResponse:
        """
        @summary 查询Workbench终端配置
        
        @description 查询Workbench终端配置
        
        @param request: DescribeTerminalSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTerminalSettingsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTerminalSettings',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20251111_models.DescribeTerminalSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_terminal_settings_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20251111_models.DescribeTerminalSettingsResponse:
        """
        @summary 查询Workbench终端配置
        
        @description 查询Workbench终端配置
        
        @param request: DescribeTerminalSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTerminalSettingsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTerminalSettings',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20251111_models.DescribeTerminalSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_terminal_settings(self) -> ecs_workbench_20251111_models.DescribeTerminalSettingsResponse:
        """
        @summary 查询Workbench终端配置
        
        @description 查询Workbench终端配置
        
        @return: DescribeTerminalSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_terminal_settings_with_options(runtime)

    async def describe_terminal_settings_async(self) -> ecs_workbench_20251111_models.DescribeTerminalSettingsResponse:
        """
        @summary 查询Workbench终端配置
        
        @description 查询Workbench终端配置
        
        @return: DescribeTerminalSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_terminal_settings_with_options_async(runtime)

    def modify_terminal_settings_with_options(
        self,
        tmp_req: ecs_workbench_20251111_models.ModifyTerminalSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20251111_models.ModifyTerminalSettingsResponse:
        """
        @summary 修改Workbench终端配置
        
        @description 修改Workbench终端配置
        
        @param tmp_req: ModifyTerminalSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTerminalSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ecs_workbench_20251111_models.ModifyTerminalSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.passwordless_login_config):
            request.passwordless_login_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passwordless_login_config, 'PasswordlessLoginConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.passwordless_login_config_shrink):
            query['PasswordlessLoginConfig'] = request.passwordless_login_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTerminalSettings',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20251111_models.ModifyTerminalSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_terminal_settings_with_options_async(
        self,
        tmp_req: ecs_workbench_20251111_models.ModifyTerminalSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20251111_models.ModifyTerminalSettingsResponse:
        """
        @summary 修改Workbench终端配置
        
        @description 修改Workbench终端配置
        
        @param tmp_req: ModifyTerminalSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTerminalSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ecs_workbench_20251111_models.ModifyTerminalSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.passwordless_login_config):
            request.passwordless_login_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passwordless_login_config, 'PasswordlessLoginConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.passwordless_login_config_shrink):
            query['PasswordlessLoginConfig'] = request.passwordless_login_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTerminalSettings',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20251111_models.ModifyTerminalSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_terminal_settings(
        self,
        request: ecs_workbench_20251111_models.ModifyTerminalSettingsRequest,
    ) -> ecs_workbench_20251111_models.ModifyTerminalSettingsResponse:
        """
        @summary 修改Workbench终端配置
        
        @description 修改Workbench终端配置
        
        @param request: ModifyTerminalSettingsRequest
        @return: ModifyTerminalSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_terminal_settings_with_options(request, runtime)

    async def modify_terminal_settings_async(
        self,
        request: ecs_workbench_20251111_models.ModifyTerminalSettingsRequest,
    ) -> ecs_workbench_20251111_models.ModifyTerminalSettingsResponse:
        """
        @summary 修改Workbench终端配置
        
        @description 修改Workbench终端配置
        
        @param request: ModifyTerminalSettingsRequest
        @return: ModifyTerminalSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_terminal_settings_with_options_async(request, runtime)
