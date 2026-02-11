# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloud_siem20220616 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloud-siem', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_data_source_with_options(
        self,
        request: main_models.AddDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not DaraCore.is_null(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not DaraCore.is_null(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_source_with_options_async(
        self,
        request: main_models.AddDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not DaraCore.is_null(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not DaraCore.is_null(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_source(
        self,
        request: main_models.AddDataSourceRequest,
    ) -> main_models.AddDataSourceResponse:
        runtime = RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    async def add_data_source_async(
        self,
        request: main_models.AddDataSourceRequest,
    ) -> main_models.AddDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.add_data_source_with_options_async(request, runtime)

    def add_data_source_log_with_options(
        self,
        request: main_models.AddDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_source_log_with_options_async(
        self,
        request: main_models.AddDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_source_log(
        self,
        request: main_models.AddDataSourceLogRequest,
    ) -> main_models.AddDataSourceLogResponse:
        runtime = RuntimeOptions()
        return self.add_data_source_log_with_options(request, runtime)

    async def add_data_source_log_async(
        self,
        request: main_models.AddDataSourceLogRequest,
    ) -> main_models.AddDataSourceLogResponse:
        runtime = RuntimeOptions()
        return await self.add_data_source_log_with_options_async(request, runtime)

    def add_user_source_log_config_with_options(
        self,
        request: main_models.AddUserSourceLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserSourceLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deleted):
            body['Deleted'] = request.deleted
        if not DaraCore.is_null(request.dis_play_line):
            body['DisPlayLine'] = request.dis_play_line
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not DaraCore.is_null(request.source_log_info):
            body['SourceLogInfo'] = request.source_log_info
        if not DaraCore.is_null(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserSourceLogConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserSourceLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_source_log_config_with_options_async(
        self,
        request: main_models.AddUserSourceLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserSourceLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deleted):
            body['Deleted'] = request.deleted
        if not DaraCore.is_null(request.dis_play_line):
            body['DisPlayLine'] = request.dis_play_line
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not DaraCore.is_null(request.source_log_info):
            body['SourceLogInfo'] = request.source_log_info
        if not DaraCore.is_null(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserSourceLogConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserSourceLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_source_log_config(
        self,
        request: main_models.AddUserSourceLogConfigRequest,
    ) -> main_models.AddUserSourceLogConfigResponse:
        runtime = RuntimeOptions()
        return self.add_user_source_log_config_with_options(request, runtime)

    async def add_user_source_log_config_async(
        self,
        request: main_models.AddUserSourceLogConfigRequest,
    ) -> main_models.AddUserSourceLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.add_user_source_log_config_with_options_async(request, runtime)

    def bind_account_with_options(
        self,
        request: main_models.BindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_with_options_async(
        self,
        request: main_models.BindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account(
        self,
        request: main_models.BindAccountRequest,
    ) -> main_models.BindAccountResponse:
        runtime = RuntimeOptions()
        return self.bind_account_with_options(request, runtime)

    async def bind_account_async(
        self,
        request: main_models.BindAccountRequest,
    ) -> main_models.BindAccountResponse:
        runtime = RuntimeOptions()
        return await self.bind_account_with_options_async(request, runtime)

    def close_delivery_with_options(
        self,
        request: main_models.CloseDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_delivery_with_options_async(
        self,
        request: main_models.CloseDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_delivery(
        self,
        request: main_models.CloseDeliveryRequest,
    ) -> main_models.CloseDeliveryResponse:
        runtime = RuntimeOptions()
        return self.close_delivery_with_options(request, runtime)

    async def close_delivery_async(
        self,
        request: main_models.CloseDeliveryRequest,
    ) -> main_models.CloseDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.close_delivery_with_options_async(request, runtime)

    def delete_automate_response_config_with_options(
        self,
        request: main_models.DeleteAutomateResponseConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutomateResponseConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutomateResponseConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_automate_response_config_with_options_async(
        self,
        request: main_models.DeleteAutomateResponseConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutomateResponseConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutomateResponseConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutomateResponseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_automate_response_config(
        self,
        request: main_models.DeleteAutomateResponseConfigRequest,
    ) -> main_models.DeleteAutomateResponseConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_automate_response_config_with_options(request, runtime)

    async def delete_automate_response_config_async(
        self,
        request: main_models.DeleteAutomateResponseConfigRequest,
    ) -> main_models.DeleteAutomateResponseConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_automate_response_config_with_options_async(request, runtime)

    def delete_bind_account_with_options(
        self,
        request: main_models.DeleteBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.bind_id):
            body['BindId'] = request.bind_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bind_account_with_options_async(
        self,
        request: main_models.DeleteBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.bind_id):
            body['BindId'] = request.bind_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bind_account(
        self,
        request: main_models.DeleteBindAccountRequest,
    ) -> main_models.DeleteBindAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_bind_account_with_options(request, runtime)

    async def delete_bind_account_async(
        self,
        request: main_models.DeleteBindAccountRequest,
    ) -> main_models.DeleteBindAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_bind_account_with_options_async(request, runtime)

    def delete_customize_rule_with_options(
        self,
        request: main_models.DeleteCustomizeRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizeRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizeRule',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customize_rule_with_options_async(
        self,
        request: main_models.DeleteCustomizeRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizeRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizeRule',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customize_rule(
        self,
        request: main_models.DeleteCustomizeRuleRequest,
    ) -> main_models.DeleteCustomizeRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_customize_rule_with_options(request, runtime)

    async def delete_customize_rule_async(
        self,
        request: main_models.DeleteCustomizeRuleRequest,
    ) -> main_models.DeleteCustomizeRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_customize_rule_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_data_source_log_with_options(
        self,
        request: main_models.DeleteDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_log_with_options_async(
        self,
        request: main_models.DeleteDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source_log(
        self,
        request: main_models.DeleteDataSourceLogRequest,
    ) -> main_models.DeleteDataSourceLogResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_log_with_options(request, runtime)

    async def delete_data_source_log_async(
        self,
        request: main_models.DeleteDataSourceLogRequest,
    ) -> main_models.DeleteDataSourceLogResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_log_with_options_async(request, runtime)

    def delete_white_rule_list_with_options(
        self,
        request: main_models.DeleteWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_white_rule_list_with_options_async(
        self,
        request: main_models.DeleteWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_white_rule_list(
        self,
        request: main_models.DeleteWhiteRuleListRequest,
    ) -> main_models.DeleteWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return self.delete_white_rule_list_with_options(request, runtime)

    async def delete_white_rule_list_async(
        self,
        request: main_models.DeleteWhiteRuleListRequest,
    ) -> main_models.DeleteWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return await self.delete_white_rule_list_with_options_async(request, runtime)

    def describe_aggregate_function_with_options(
        self,
        request: main_models.DescribeAggregateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAggregateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAggregateFunction',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAggregateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aggregate_function_with_options_async(
        self,
        request: main_models.DescribeAggregateFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAggregateFunctionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAggregateFunction',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAggregateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aggregate_function(
        self,
        request: main_models.DescribeAggregateFunctionRequest,
    ) -> main_models.DescribeAggregateFunctionResponse:
        runtime = RuntimeOptions()
        return self.describe_aggregate_function_with_options(request, runtime)

    async def describe_aggregate_function_async(
        self,
        request: main_models.DescribeAggregateFunctionRequest,
    ) -> main_models.DescribeAggregateFunctionResponse:
        runtime = RuntimeOptions()
        return await self.describe_aggregate_function_with_options_async(request, runtime)

    def describe_alert_scene_with_options(
        self,
        request: main_models.DescribeAlertSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertScene',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_scene_with_options_async(
        self,
        request: main_models.DescribeAlertSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertScene',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_scene(
        self,
        request: main_models.DescribeAlertSceneRequest,
    ) -> main_models.DescribeAlertSceneResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_scene_with_options(request, runtime)

    async def describe_alert_scene_async(
        self,
        request: main_models.DescribeAlertSceneRequest,
    ) -> main_models.DescribeAlertSceneResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_scene_with_options_async(request, runtime)

    def describe_alert_scene_by_event_with_options(
        self,
        request: main_models.DescribeAlertSceneByEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSceneByEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSceneByEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSceneByEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_scene_by_event_with_options_async(
        self,
        request: main_models.DescribeAlertSceneByEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSceneByEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSceneByEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSceneByEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_scene_by_event(
        self,
        request: main_models.DescribeAlertSceneByEventRequest,
    ) -> main_models.DescribeAlertSceneByEventResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_scene_by_event_with_options(request, runtime)

    async def describe_alert_scene_by_event_async(
        self,
        request: main_models.DescribeAlertSceneByEventRequest,
    ) -> main_models.DescribeAlertSceneByEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_scene_by_event_with_options_async(request, runtime)

    def describe_alert_source_with_options(
        self,
        request: main_models.DescribeAlertSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_source_with_options_async(
        self,
        request: main_models.DescribeAlertSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_source(
        self,
        request: main_models.DescribeAlertSourceRequest,
    ) -> main_models.DescribeAlertSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_source_with_options(request, runtime)

    async def describe_alert_source_async(
        self,
        request: main_models.DescribeAlertSourceRequest,
    ) -> main_models.DescribeAlertSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_source_with_options_async(request, runtime)

    def describe_alert_source_with_event_with_options(
        self,
        request: main_models.DescribeAlertSourceWithEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSourceWithEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSourceWithEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSourceWithEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_source_with_event_with_options_async(
        self,
        request: main_models.DescribeAlertSourceWithEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertSourceWithEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertSourceWithEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertSourceWithEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_source_with_event(
        self,
        request: main_models.DescribeAlertSourceWithEventRequest,
    ) -> main_models.DescribeAlertSourceWithEventResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_source_with_event_with_options(request, runtime)

    async def describe_alert_source_with_event_async(
        self,
        request: main_models.DescribeAlertSourceWithEventRequest,
    ) -> main_models.DescribeAlertSourceWithEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_source_with_event_with_options_async(request, runtime)

    def describe_alert_type_with_options(
        self,
        request: main_models.DescribeAlertTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertType',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_type_with_options_async(
        self,
        request: main_models.DescribeAlertTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertType',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_type(
        self,
        request: main_models.DescribeAlertTypeRequest,
    ) -> main_models.DescribeAlertTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_type_with_options(request, runtime)

    async def describe_alert_type_async(
        self,
        request: main_models.DescribeAlertTypeRequest,
    ) -> main_models.DescribeAlertTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_type_with_options_async(request, runtime)

    def describe_alerts_with_options(
        self,
        request: main_models.DescribeAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not DaraCore.is_null(request.label_type):
            body['LabelType'] = request.label_type
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlerts',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_options_async(
        self,
        request: main_models.DescribeAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not DaraCore.is_null(request.label_type):
            body['LabelType'] = request.label_type
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlerts',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts(
        self,
        request: main_models.DescribeAlertsRequest,
    ) -> main_models.DescribeAlertsResponse:
        runtime = RuntimeOptions()
        return self.describe_alerts_with_options(request, runtime)

    async def describe_alerts_async(
        self,
        request: main_models.DescribeAlertsRequest,
    ) -> main_models.DescribeAlertsResponse:
        runtime = RuntimeOptions()
        return await self.describe_alerts_with_options_async(request, runtime)

    def describe_alerts_count_with_options(
        self,
        request: main_models.DescribeAlertsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_type):
            body['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_count_with_options_async(
        self,
        request: main_models.DescribeAlertsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query_type):
            body['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_count(
        self,
        request: main_models.DescribeAlertsCountRequest,
    ) -> main_models.DescribeAlertsCountResponse:
        runtime = RuntimeOptions()
        return self.describe_alerts_count_with_options(request, runtime)

    async def describe_alerts_count_async(
        self,
        request: main_models.DescribeAlertsCountRequest,
    ) -> main_models.DescribeAlertsCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_alerts_count_with_options_async(request, runtime)

    def describe_alerts_with_entity_with_options(
        self,
        request: main_models.DescribeAlertsWithEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsWithEntityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsWithEntity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsWithEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_entity_with_options_async(
        self,
        request: main_models.DescribeAlertsWithEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsWithEntityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsWithEntity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsWithEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_with_entity(
        self,
        request: main_models.DescribeAlertsWithEntityRequest,
    ) -> main_models.DescribeAlertsWithEntityResponse:
        runtime = RuntimeOptions()
        return self.describe_alerts_with_entity_with_options(request, runtime)

    async def describe_alerts_with_entity_async(
        self,
        request: main_models.DescribeAlertsWithEntityRequest,
    ) -> main_models.DescribeAlertsWithEntityResponse:
        runtime = RuntimeOptions()
        return await self.describe_alerts_with_entity_with_options_async(request, runtime)

    def describe_alerts_with_event_with_options(
        self,
        request: main_models.DescribeAlertsWithEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsWithEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsWithEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsWithEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerts_with_event_with_options_async(
        self,
        request: main_models.DescribeAlertsWithEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertsWithEventResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_title):
            body['AlertTitle'] = request.alert_title
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.is_defend):
            body['IsDefend'] = request.is_defend
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertsWithEvent',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertsWithEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerts_with_event(
        self,
        request: main_models.DescribeAlertsWithEventRequest,
    ) -> main_models.DescribeAlertsWithEventResponse:
        runtime = RuntimeOptions()
        return self.describe_alerts_with_event_with_options(request, runtime)

    async def describe_alerts_with_event_async(
        self,
        request: main_models.DescribeAlertsWithEventRequest,
    ) -> main_models.DescribeAlertsWithEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_alerts_with_event_with_options_async(request, runtime)

    def describe_auth_with_options(
        self,
        request: main_models.DescribeAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuth',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auth_with_options_async(
        self,
        request: main_models.DescribeAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuth',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auth(
        self,
        request: main_models.DescribeAuthRequest,
    ) -> main_models.DescribeAuthResponse:
        runtime = RuntimeOptions()
        return self.describe_auth_with_options(request, runtime)

    async def describe_auth_async(
        self,
        request: main_models.DescribeAuthRequest,
    ) -> main_models.DescribeAuthResponse:
        runtime = RuntimeOptions()
        return await self.describe_auth_with_options_async(request, runtime)

    def describe_automate_response_config_counter_with_options(
        self,
        request: main_models.DescribeAutomateResponseConfigCounterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutomateResponseConfigCounterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutomateResponseConfigCounter',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutomateResponseConfigCounterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_automate_response_config_counter_with_options_async(
        self,
        request: main_models.DescribeAutomateResponseConfigCounterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutomateResponseConfigCounterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutomateResponseConfigCounter',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutomateResponseConfigCounterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_automate_response_config_counter(
        self,
        request: main_models.DescribeAutomateResponseConfigCounterRequest,
    ) -> main_models.DescribeAutomateResponseConfigCounterResponse:
        runtime = RuntimeOptions()
        return self.describe_automate_response_config_counter_with_options(request, runtime)

    async def describe_automate_response_config_counter_async(
        self,
        request: main_models.DescribeAutomateResponseConfigCounterRequest,
    ) -> main_models.DescribeAutomateResponseConfigCounterResponse:
        runtime = RuntimeOptions()
        return await self.describe_automate_response_config_counter_with_options_async(request, runtime)

    def describe_automate_response_config_feature_with_options(
        self,
        request: main_models.DescribeAutomateResponseConfigFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutomateResponseConfigFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutomateResponseConfigFeature',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutomateResponseConfigFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_automate_response_config_feature_with_options_async(
        self,
        request: main_models.DescribeAutomateResponseConfigFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutomateResponseConfigFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutomateResponseConfigFeature',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutomateResponseConfigFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_automate_response_config_feature(
        self,
        request: main_models.DescribeAutomateResponseConfigFeatureRequest,
    ) -> main_models.DescribeAutomateResponseConfigFeatureResponse:
        runtime = RuntimeOptions()
        return self.describe_automate_response_config_feature_with_options(request, runtime)

    async def describe_automate_response_config_feature_async(
        self,
        request: main_models.DescribeAutomateResponseConfigFeatureRequest,
    ) -> main_models.DescribeAutomateResponseConfigFeatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_automate_response_config_feature_with_options_async(request, runtime)

    def describe_cloud_siem_assets_with_options(
        self,
        request: main_models.DescribeCloudSiemAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemAssetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_type):
            body['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.asset_uuid):
            body['AssetUuid'] = request.asset_uuid
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemAssets',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_assets_with_options_async(
        self,
        request: main_models.DescribeCloudSiemAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemAssetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asset_name):
            body['AssetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_type):
            body['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.asset_uuid):
            body['AssetUuid'] = request.asset_uuid
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemAssets',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_assets(
        self,
        request: main_models.DescribeCloudSiemAssetsRequest,
    ) -> main_models.DescribeCloudSiemAssetsResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_siem_assets_with_options(request, runtime)

    async def describe_cloud_siem_assets_async(
        self,
        request: main_models.DescribeCloudSiemAssetsRequest,
    ) -> main_models.DescribeCloudSiemAssetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_siem_assets_with_options_async(request, runtime)

    def describe_cloud_siem_assets_counter_with_options(
        self,
        request: main_models.DescribeCloudSiemAssetsCounterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemAssetsCounterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemAssetsCounter',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemAssetsCounterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_assets_counter_with_options_async(
        self,
        request: main_models.DescribeCloudSiemAssetsCounterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemAssetsCounterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemAssetsCounter',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemAssetsCounterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_assets_counter(
        self,
        request: main_models.DescribeCloudSiemAssetsCounterRequest,
    ) -> main_models.DescribeCloudSiemAssetsCounterResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_siem_assets_counter_with_options(request, runtime)

    async def describe_cloud_siem_assets_counter_async(
        self,
        request: main_models.DescribeCloudSiemAssetsCounterRequest,
    ) -> main_models.DescribeCloudSiemAssetsCounterResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_siem_assets_counter_with_options_async(request, runtime)

    def describe_cloud_siem_event_detail_with_options(
        self,
        request: main_models.DescribeCloudSiemEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemEventDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemEventDetail',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_event_detail_with_options_async(
        self,
        request: main_models.DescribeCloudSiemEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemEventDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemEventDetail',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_event_detail(
        self,
        request: main_models.DescribeCloudSiemEventDetailRequest,
    ) -> main_models.DescribeCloudSiemEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_siem_event_detail_with_options(request, runtime)

    async def describe_cloud_siem_event_detail_async(
        self,
        request: main_models.DescribeCloudSiemEventDetailRequest,
    ) -> main_models.DescribeCloudSiemEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_siem_event_detail_with_options_async(request, runtime)

    def describe_cloud_siem_events_with_options(
        self,
        request: main_models.DescribeCloudSiemEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemEventsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.event_name):
            body['EventName'] = request.event_name
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.thread_level):
            body['ThreadLevel'] = request.thread_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemEvents',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_siem_events_with_options_async(
        self,
        request: main_models.DescribeCloudSiemEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudSiemEventsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asset_id):
            body['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.event_name):
            body['EventName'] = request.event_name
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.thread_level):
            body['ThreadLevel'] = request.thread_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudSiemEvents',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudSiemEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_siem_events(
        self,
        request: main_models.DescribeCloudSiemEventsRequest,
    ) -> main_models.DescribeCloudSiemEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_siem_events_with_options(request, runtime)

    async def describe_cloud_siem_events_async(
        self,
        request: main_models.DescribeCloudSiemEventsRequest,
    ) -> main_models.DescribeCloudSiemEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_siem_events_with_options_async(request, runtime)

    def describe_customize_rule_count_with_options(
        self,
        request: main_models.DescribeCustomizeRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_count_with_options_async(
        self,
        request: main_models.DescribeCustomizeRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_count(
        self,
        request: main_models.DescribeCustomizeRuleCountRequest,
    ) -> main_models.DescribeCustomizeRuleCountResponse:
        runtime = RuntimeOptions()
        return self.describe_customize_rule_count_with_options(request, runtime)

    async def describe_customize_rule_count_async(
        self,
        request: main_models.DescribeCustomizeRuleCountRequest,
    ) -> main_models.DescribeCustomizeRuleCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_customize_rule_count_with_options_async(request, runtime)

    def describe_customize_rule_test_with_options(
        self,
        request: main_models.DescribeCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_test_with_options_async(
        self,
        request: main_models.DescribeCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_test(
        self,
        request: main_models.DescribeCustomizeRuleTestRequest,
    ) -> main_models.DescribeCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return self.describe_customize_rule_test_with_options(request, runtime)

    async def describe_customize_rule_test_async(
        self,
        request: main_models.DescribeCustomizeRuleTestRequest,
    ) -> main_models.DescribeCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return await self.describe_customize_rule_test_with_options_async(request, runtime)

    def describe_customize_rule_test_histogram_with_options(
        self,
        request: main_models.DescribeCustomizeRuleTestHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleTestHistogramResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleTestHistogram',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleTestHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customize_rule_test_histogram_with_options_async(
        self,
        request: main_models.DescribeCustomizeRuleTestHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomizeRuleTestHistogramResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomizeRuleTestHistogram',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomizeRuleTestHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customize_rule_test_histogram(
        self,
        request: main_models.DescribeCustomizeRuleTestHistogramRequest,
    ) -> main_models.DescribeCustomizeRuleTestHistogramResponse:
        runtime = RuntimeOptions()
        return self.describe_customize_rule_test_histogram_with_options(request, runtime)

    async def describe_customize_rule_test_histogram_async(
        self,
        request: main_models.DescribeCustomizeRuleTestHistogramRequest,
    ) -> main_models.DescribeCustomizeRuleTestHistogramResponse:
        runtime = RuntimeOptions()
        return await self.describe_customize_rule_test_histogram_with_options_async(request, runtime)

    def describe_data_source_instance_with_options(
        self,
        request: main_models.DescribeDataSourceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceInstance',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_instance_with_options_async(
        self,
        request: main_models.DescribeDataSourceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceInstance',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_instance(
        self,
        request: main_models.DescribeDataSourceInstanceRequest,
    ) -> main_models.DescribeDataSourceInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_data_source_instance_with_options(request, runtime)

    async def describe_data_source_instance_async(
        self,
        request: main_models.DescribeDataSourceInstanceRequest,
    ) -> main_models.DescribeDataSourceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_source_instance_with_options_async(request, runtime)

    def describe_data_source_parameters_with_options(
        self,
        request: main_models.DescribeDataSourceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceParametersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceParameters',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_parameters_with_options_async(
        self,
        request: main_models.DescribeDataSourceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataSourceParametersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataSourceParameters',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataSourceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_source_parameters(
        self,
        request: main_models.DescribeDataSourceParametersRequest,
    ) -> main_models.DescribeDataSourceParametersResponse:
        runtime = RuntimeOptions()
        return self.describe_data_source_parameters_with_options(request, runtime)

    async def describe_data_source_parameters_async(
        self,
        request: main_models.DescribeDataSourceParametersRequest,
    ) -> main_models.DescribeDataSourceParametersResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_source_parameters_with_options_async(request, runtime)

    def describe_dispose_and_playbook_with_options(
        self,
        request: main_models.DescribeDisposeAndPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisposeAndPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisposeAndPlaybook',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisposeAndPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispose_and_playbook_with_options_async(
        self,
        request: main_models.DescribeDisposeAndPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisposeAndPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisposeAndPlaybook',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisposeAndPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispose_and_playbook(
        self,
        request: main_models.DescribeDisposeAndPlaybookRequest,
    ) -> main_models.DescribeDisposeAndPlaybookResponse:
        runtime = RuntimeOptions()
        return self.describe_dispose_and_playbook_with_options(request, runtime)

    async def describe_dispose_and_playbook_async(
        self,
        request: main_models.DescribeDisposeAndPlaybookRequest,
    ) -> main_models.DescribeDisposeAndPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.describe_dispose_and_playbook_with_options_async(request, runtime)

    def describe_dispose_strategy_playbook_with_options(
        self,
        request: main_models.DescribeDisposeStrategyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisposeStrategyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisposeStrategyPlaybook',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisposeStrategyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispose_strategy_playbook_with_options_async(
        self,
        request: main_models.DescribeDisposeStrategyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisposeStrategyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisposeStrategyPlaybook',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisposeStrategyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispose_strategy_playbook(
        self,
        request: main_models.DescribeDisposeStrategyPlaybookRequest,
    ) -> main_models.DescribeDisposeStrategyPlaybookResponse:
        runtime = RuntimeOptions()
        return self.describe_dispose_strategy_playbook_with_options(request, runtime)

    async def describe_dispose_strategy_playbook_async(
        self,
        request: main_models.DescribeDisposeStrategyPlaybookRequest,
    ) -> main_models.DescribeDisposeStrategyPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.describe_dispose_strategy_playbook_with_options_async(request, runtime)

    def describe_entity_info_with_options(
        self,
        request: main_models.DescribeEntityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEntityInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEntityInfo',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEntityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_entity_info_with_options_async(
        self,
        request: main_models.DescribeEntityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEntityInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEntityInfo',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEntityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_entity_info(
        self,
        request: main_models.DescribeEntityInfoRequest,
    ) -> main_models.DescribeEntityInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_entity_info_with_options(request, runtime)

    async def describe_entity_info_async(
        self,
        request: main_models.DescribeEntityInfoRequest,
    ) -> main_models.DescribeEntityInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_entity_info_with_options_async(request, runtime)

    def describe_event_count_by_threat_level_with_options(
        self,
        request: main_models.DescribeEventCountByThreatLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventCountByThreatLevelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventCountByThreatLevel',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventCountByThreatLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_count_by_threat_level_with_options_async(
        self,
        request: main_models.DescribeEventCountByThreatLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventCountByThreatLevelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventCountByThreatLevel',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventCountByThreatLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_count_by_threat_level(
        self,
        request: main_models.DescribeEventCountByThreatLevelRequest,
    ) -> main_models.DescribeEventCountByThreatLevelResponse:
        runtime = RuntimeOptions()
        return self.describe_event_count_by_threat_level_with_options(request, runtime)

    async def describe_event_count_by_threat_level_async(
        self,
        request: main_models.DescribeEventCountByThreatLevelRequest,
    ) -> main_models.DescribeEventCountByThreatLevelResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_count_by_threat_level_with_options_async(request, runtime)

    def describe_event_dispose_with_options(
        self,
        request: main_models.DescribeEventDisposeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDisposeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDispose',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDisposeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_dispose_with_options_async(
        self,
        request: main_models.DescribeEventDisposeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDisposeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDispose',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDisposeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_dispose(
        self,
        request: main_models.DescribeEventDisposeRequest,
    ) -> main_models.DescribeEventDisposeResponse:
        runtime = RuntimeOptions()
        return self.describe_event_dispose_with_options(request, runtime)

    async def describe_event_dispose_async(
        self,
        request: main_models.DescribeEventDisposeRequest,
    ) -> main_models.DescribeEventDisposeResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_dispose_with_options_async(request, runtime)

    def describe_imported_log_count_with_options(
        self,
        request: main_models.DescribeImportedLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImportedLogCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImportedLogCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImportedLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imported_log_count_with_options_async(
        self,
        request: main_models.DescribeImportedLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImportedLogCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImportedLogCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImportedLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imported_log_count(
        self,
        request: main_models.DescribeImportedLogCountRequest,
    ) -> main_models.DescribeImportedLogCountResponse:
        runtime = RuntimeOptions()
        return self.describe_imported_log_count_with_options(request, runtime)

    async def describe_imported_log_count_async(
        self,
        request: main_models.DescribeImportedLogCountRequest,
    ) -> main_models.DescribeImportedLogCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_imported_log_count_with_options_async(request, runtime)

    def describe_log_fields_with_options(
        self,
        request: main_models.DescribeLogFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogFieldsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogFields',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_fields_with_options_async(
        self,
        request: main_models.DescribeLogFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogFieldsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogFields',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_fields(
        self,
        request: main_models.DescribeLogFieldsRequest,
    ) -> main_models.DescribeLogFieldsResponse:
        runtime = RuntimeOptions()
        return self.describe_log_fields_with_options(request, runtime)

    async def describe_log_fields_async(
        self,
        request: main_models.DescribeLogFieldsRequest,
    ) -> main_models.DescribeLogFieldsResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_fields_with_options_async(request, runtime)

    def describe_log_source_with_options(
        self,
        request: main_models.DescribeLogSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_source_with_options_async(
        self,
        request: main_models.DescribeLogSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_source(
        self,
        request: main_models.DescribeLogSourceRequest,
    ) -> main_models.DescribeLogSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_log_source_with_options(request, runtime)

    async def describe_log_source_async(
        self,
        request: main_models.DescribeLogSourceRequest,
    ) -> main_models.DescribeLogSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_source_with_options_async(request, runtime)

    def describe_log_type_with_options(
        self,
        request: main_models.DescribeLogTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogType',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_type_with_options_async(
        self,
        request: main_models.DescribeLogTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogType',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_type(
        self,
        request: main_models.DescribeLogTypeRequest,
    ) -> main_models.DescribeLogTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_log_type_with_options(request, runtime)

    async def describe_log_type_async(
        self,
        request: main_models.DescribeLogTypeRequest,
    ) -> main_models.DescribeLogTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_type_with_options_async(request, runtime)

    def describe_operators_with_options(
        self,
        request: main_models.DescribeOperatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperators',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operators_with_options_async(
        self,
        request: main_models.DescribeOperatorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperators',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operators(
        self,
        request: main_models.DescribeOperatorsRequest,
    ) -> main_models.DescribeOperatorsResponse:
        runtime = RuntimeOptions()
        return self.describe_operators_with_options(request, runtime)

    async def describe_operators_async(
        self,
        request: main_models.DescribeOperatorsRequest,
    ) -> main_models.DescribeOperatorsResponse:
        runtime = RuntimeOptions()
        return await self.describe_operators_with_options_async(request, runtime)

    def describe_prod_count_with_options(
        self,
        request: main_models.DescribeProdCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProdCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProdCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProdCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prod_count_with_options_async(
        self,
        request: main_models.DescribeProdCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProdCountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProdCount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProdCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prod_count(
        self,
        request: main_models.DescribeProdCountRequest,
    ) -> main_models.DescribeProdCountResponse:
        runtime = RuntimeOptions()
        return self.describe_prod_count_with_options(request, runtime)

    async def describe_prod_count_async(
        self,
        request: main_models.DescribeProdCountRequest,
    ) -> main_models.DescribeProdCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_prod_count_with_options_async(request, runtime)

    def describe_scope_users_with_options(
        self,
        request: main_models.DescribeScopeUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScopeUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScopeUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScopeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scope_users_with_options_async(
        self,
        request: main_models.DescribeScopeUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScopeUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScopeUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScopeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scope_users(
        self,
        request: main_models.DescribeScopeUsersRequest,
    ) -> main_models.DescribeScopeUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_scope_users_with_options(request, runtime)

    async def describe_scope_users_async(
        self,
        request: main_models.DescribeScopeUsersRequest,
    ) -> main_models.DescribeScopeUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_scope_users_with_options_async(request, runtime)

    def describe_service_status_with_options(
        self,
        request: main_models.DescribeServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_status_with_options_async(
        self,
        request: main_models.DescribeServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_status(
        self,
        request: main_models.DescribeServiceStatusRequest,
    ) -> main_models.DescribeServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_service_status_with_options(request, runtime)

    async def describe_service_status_async(
        self,
        request: main_models.DescribeServiceStatusRequest,
    ) -> main_models.DescribeServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_status_with_options_async(request, runtime)

    def describe_storage_with_options(
        self,
        request: main_models.DescribeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_with_options_async(
        self,
        request: main_models.DescribeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage(
        self,
        request: main_models.DescribeStorageRequest,
    ) -> main_models.DescribeStorageResponse:
        runtime = RuntimeOptions()
        return self.describe_storage_with_options(request, runtime)

    async def describe_storage_async(
        self,
        request: main_models.DescribeStorageRequest,
    ) -> main_models.DescribeStorageResponse:
        runtime = RuntimeOptions()
        return await self.describe_storage_with_options_async(request, runtime)

    def describe_user_buy_status_with_options(
        self,
        request: main_models.DescribeUserBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserBuyStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserBuyStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_buy_status_with_options_async(
        self,
        request: main_models.DescribeUserBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserBuyStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserBuyStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_buy_status(
        self,
        request: main_models.DescribeUserBuyStatusRequest,
    ) -> main_models.DescribeUserBuyStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_buy_status_with_options(request, runtime)

    async def describe_user_buy_status_async(
        self,
        request: main_models.DescribeUserBuyStatusRequest,
    ) -> main_models.DescribeUserBuyStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_buy_status_with_options_async(request, runtime)

    def describe_waf_scope_with_options(
        self,
        request: main_models.DescribeWafScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWafScopeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWafScope',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWafScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_scope_with_options_async(
        self,
        request: main_models.DescribeWafScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWafScopeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWafScope',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWafScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_scope(
        self,
        request: main_models.DescribeWafScopeRequest,
    ) -> main_models.DescribeWafScopeResponse:
        runtime = RuntimeOptions()
        return self.describe_waf_scope_with_options(request, runtime)

    async def describe_waf_scope_async(
        self,
        request: main_models.DescribeWafScopeRequest,
    ) -> main_models.DescribeWafScopeResponse:
        runtime = RuntimeOptions()
        return await self.describe_waf_scope_with_options_async(request, runtime)

    def describe_white_rule_list_with_options(
        self,
        request: main_models.DescribeWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_white_rule_list_with_options_async(
        self,
        request: main_models.DescribeWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_white_rule_list(
        self,
        request: main_models.DescribeWhiteRuleListRequest,
    ) -> main_models.DescribeWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_white_rule_list_with_options(request, runtime)

    async def describe_white_rule_list_async(
        self,
        request: main_models.DescribeWhiteRuleListRequest,
    ) -> main_models.DescribeWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_white_rule_list_with_options_async(request, runtime)

    def enable_access_for_cloud_siem_with_options(
        self,
        request: main_models.EnableAccessForCloudSiemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAccessForCloudSiemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_submit):
            body['AutoSubmit'] = request.auto_submit
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableAccessForCloudSiem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAccessForCloudSiemResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_access_for_cloud_siem_with_options_async(
        self,
        request: main_models.EnableAccessForCloudSiemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAccessForCloudSiemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_submit):
            body['AutoSubmit'] = request.auto_submit
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableAccessForCloudSiem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAccessForCloudSiemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_access_for_cloud_siem(
        self,
        request: main_models.EnableAccessForCloudSiemRequest,
    ) -> main_models.EnableAccessForCloudSiemResponse:
        runtime = RuntimeOptions()
        return self.enable_access_for_cloud_siem_with_options(request, runtime)

    async def enable_access_for_cloud_siem_async(
        self,
        request: main_models.EnableAccessForCloudSiemRequest,
    ) -> main_models.EnableAccessForCloudSiemResponse:
        runtime = RuntimeOptions()
        return await self.enable_access_for_cloud_siem_with_options_async(request, runtime)

    def enable_service_for_cloud_siem_with_options(
        self,
        request: main_models.EnableServiceForCloudSiemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceForCloudSiemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableServiceForCloudSiem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceForCloudSiemResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_for_cloud_siem_with_options_async(
        self,
        request: main_models.EnableServiceForCloudSiemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceForCloudSiemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableServiceForCloudSiem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceForCloudSiemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service_for_cloud_siem(
        self,
        request: main_models.EnableServiceForCloudSiemRequest,
    ) -> main_models.EnableServiceForCloudSiemResponse:
        runtime = RuntimeOptions()
        return self.enable_service_for_cloud_siem_with_options(request, runtime)

    async def enable_service_for_cloud_siem_async(
        self,
        request: main_models.EnableServiceForCloudSiemRequest,
    ) -> main_models.EnableServiceForCloudSiemResponse:
        runtime = RuntimeOptions()
        return await self.enable_service_for_cloud_siem_with_options_async(request, runtime)

    def get_capacity_with_options(
        self,
        request: main_models.GetCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCapacityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCapacity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_capacity_with_options_async(
        self,
        request: main_models.GetCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCapacityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCapacity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_capacity(
        self,
        request: main_models.GetCapacityRequest,
    ) -> main_models.GetCapacityResponse:
        runtime = RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    async def get_capacity_async(
        self,
        request: main_models.GetCapacityRequest,
    ) -> main_models.GetCapacityResponse:
        runtime = RuntimeOptions()
        return await self.get_capacity_with_options_async(request, runtime)

    def get_storage_with_options(
        self,
        request: main_models.GetStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_with_options_async(
        self,
        request: main_models.GetStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage(
        self,
        request: main_models.GetStorageRequest,
    ) -> main_models.GetStorageResponse:
        runtime = RuntimeOptions()
        return self.get_storage_with_options(request, runtime)

    async def get_storage_async(
        self,
        request: main_models.GetStorageRequest,
    ) -> main_models.GetStorageResponse:
        runtime = RuntimeOptions()
        return await self.get_storage_with_options_async(request, runtime)

    def list_account_access_id_with_options(
        self,
        request: main_models.ListAccountAccessIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountAccessIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountAccessId',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountAccessIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_access_id_with_options_async(
        self,
        request: main_models.ListAccountAccessIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountAccessIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountAccessId',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountAccessIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_access_id(
        self,
        request: main_models.ListAccountAccessIdRequest,
    ) -> main_models.ListAccountAccessIdResponse:
        runtime = RuntimeOptions()
        return self.list_account_access_id_with_options(request, runtime)

    async def list_account_access_id_async(
        self,
        request: main_models.ListAccountAccessIdRequest,
    ) -> main_models.ListAccountAccessIdResponse:
        runtime = RuntimeOptions()
        return await self.list_account_access_id_with_options_async(request, runtime)

    def list_accounts_by_log_with_options(
        self,
        request: main_models.ListAccountsByLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsByLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountsByLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsByLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_by_log_with_options_async(
        self,
        request: main_models.ListAccountsByLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsByLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountsByLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsByLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_by_log(
        self,
        request: main_models.ListAccountsByLogRequest,
    ) -> main_models.ListAccountsByLogResponse:
        runtime = RuntimeOptions()
        return self.list_accounts_by_log_with_options(request, runtime)

    async def list_accounts_by_log_async(
        self,
        request: main_models.ListAccountsByLogRequest,
    ) -> main_models.ListAccountsByLogResponse:
        runtime = RuntimeOptions()
        return await self.list_accounts_by_log_with_options_async(request, runtime)

    def list_all_prods_with_options(
        self,
        request: main_models.ListAllProdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllProdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAllProds',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllProdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_prods_with_options_async(
        self,
        request: main_models.ListAllProdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllProdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAllProds',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllProdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_prods(
        self,
        request: main_models.ListAllProdsRequest,
    ) -> main_models.ListAllProdsResponse:
        runtime = RuntimeOptions()
        return self.list_all_prods_with_options(request, runtime)

    async def list_all_prods_async(
        self,
        request: main_models.ListAllProdsRequest,
    ) -> main_models.ListAllProdsResponse:
        runtime = RuntimeOptions()
        return await self.list_all_prods_with_options_async(request, runtime)

    def list_automate_response_configs_with_options(
        self,
        request: main_models.ListAutomateResponseConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutomateResponseConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_type):
            body['ActionType'] = request.action_type
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_rule_type):
            body['ResponseRuleType'] = request.response_rule_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAutomateResponseConfigs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutomateResponseConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_automate_response_configs_with_options_async(
        self,
        request: main_models.ListAutomateResponseConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutomateResponseConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_type):
            body['ActionType'] = request.action_type
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_rule_type):
            body['ResponseRuleType'] = request.response_rule_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAutomateResponseConfigs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutomateResponseConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_automate_response_configs(
        self,
        request: main_models.ListAutomateResponseConfigsRequest,
    ) -> main_models.ListAutomateResponseConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_automate_response_configs_with_options(request, runtime)

    async def list_automate_response_configs_async(
        self,
        request: main_models.ListAutomateResponseConfigsRequest,
    ) -> main_models.ListAutomateResponseConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_automate_response_configs_with_options_async(request, runtime)

    def list_bind_account_with_options(
        self,
        request: main_models.ListBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_account_with_options_async(
        self,
        request: main_models.ListBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_account(
        self,
        request: main_models.ListBindAccountRequest,
    ) -> main_models.ListBindAccountResponse:
        runtime = RuntimeOptions()
        return self.list_bind_account_with_options(request, runtime)

    async def list_bind_account_async(
        self,
        request: main_models.ListBindAccountRequest,
    ) -> main_models.ListBindAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_bind_account_with_options_async(request, runtime)

    def list_bind_data_sources_with_options(
        self,
        request: main_models.ListBindDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindDataSourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindDataSources',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_data_sources_with_options_async(
        self,
        request: main_models.ListBindDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindDataSourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindDataSources',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_data_sources(
        self,
        request: main_models.ListBindDataSourcesRequest,
    ) -> main_models.ListBindDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_bind_data_sources_with_options(request, runtime)

    async def list_bind_data_sources_async(
        self,
        request: main_models.ListBindDataSourcesRequest,
    ) -> main_models.ListBindDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_bind_data_sources_with_options_async(request, runtime)

    def list_cloud_siem_customize_rules_with_options(
        self,
        request: main_models.ListCloudSiemCustomizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudSiemCustomizeRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudSiemCustomizeRules',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudSiemCustomizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_siem_customize_rules_with_options_async(
        self,
        request: main_models.ListCloudSiemCustomizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudSiemCustomizeRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudSiemCustomizeRules',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudSiemCustomizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_siem_customize_rules(
        self,
        request: main_models.ListCloudSiemCustomizeRulesRequest,
    ) -> main_models.ListCloudSiemCustomizeRulesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_siem_customize_rules_with_options(request, runtime)

    async def list_cloud_siem_customize_rules_async(
        self,
        request: main_models.ListCloudSiemCustomizeRulesRequest,
    ) -> main_models.ListCloudSiemCustomizeRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_siem_customize_rules_with_options_async(request, runtime)

    def list_cloud_siem_predefined_rules_with_options(
        self,
        request: main_models.ListCloudSiemPredefinedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudSiemPredefinedRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.att_ck):
            body['AttCk'] = request.att_ck
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudSiemPredefinedRules',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudSiemPredefinedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_siem_predefined_rules_with_options_async(
        self,
        request: main_models.ListCloudSiemPredefinedRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudSiemPredefinedRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.att_ck):
            body['AttCk'] = request.att_ck
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudSiemPredefinedRules',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudSiemPredefinedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_siem_predefined_rules(
        self,
        request: main_models.ListCloudSiemPredefinedRulesRequest,
    ) -> main_models.ListCloudSiemPredefinedRulesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_siem_predefined_rules_with_options(request, runtime)

    async def list_cloud_siem_predefined_rules_async(
        self,
        request: main_models.ListCloudSiemPredefinedRulesRequest,
    ) -> main_models.ListCloudSiemPredefinedRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_siem_predefined_rules_with_options_async(request, runtime)

    def list_customize_rule_test_result_with_options(
        self,
        request: main_models.ListCustomizeRuleTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomizeRuleTestResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.verify_type):
            body['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomizeRuleTestResult',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomizeRuleTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_customize_rule_test_result_with_options_async(
        self,
        request: main_models.ListCustomizeRuleTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomizeRuleTestResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.verify_type):
            body['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomizeRuleTestResult',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomizeRuleTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_customize_rule_test_result(
        self,
        request: main_models.ListCustomizeRuleTestResultRequest,
    ) -> main_models.ListCustomizeRuleTestResultResponse:
        runtime = RuntimeOptions()
        return self.list_customize_rule_test_result_with_options(request, runtime)

    async def list_customize_rule_test_result_async(
        self,
        request: main_models.ListCustomizeRuleTestResultRequest,
    ) -> main_models.ListCustomizeRuleTestResultResponse:
        runtime = RuntimeOptions()
        return await self.list_customize_rule_test_result_with_options_async(request, runtime)

    def list_data_source_logs_with_options(
        self,
        request: main_models.ListDataSourceLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceLogsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceLogs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_logs_with_options_async(
        self,
        request: main_models.ListDataSourceLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceLogsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceLogs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_logs(
        self,
        request: main_models.ListDataSourceLogsRequest,
    ) -> main_models.ListDataSourceLogsResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_logs_with_options(request, runtime)

    async def list_data_source_logs_async(
        self,
        request: main_models.ListDataSourceLogsRequest,
    ) -> main_models.ListDataSourceLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_logs_with_options_async(request, runtime)

    def list_data_source_types_with_options(
        self,
        request: main_models.ListDataSourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTypes',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_types_with_options_async(
        self,
        request: main_models.ListDataSourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTypes',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_types(
        self,
        request: main_models.ListDataSourceTypesRequest,
    ) -> main_models.ListDataSourceTypesResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_types_with_options(request, runtime)

    async def list_data_source_types_async(
        self,
        request: main_models.ListDataSourceTypesRequest,
    ) -> main_models.ListDataSourceTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_types_with_options_async(request, runtime)

    def list_delivery_with_options(
        self,
        request: main_models.ListDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_with_options_async(
        self,
        request: main_models.ListDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery(
        self,
        request: main_models.ListDeliveryRequest,
    ) -> main_models.ListDeliveryResponse:
        runtime = RuntimeOptions()
        return self.list_delivery_with_options(request, runtime)

    async def list_delivery_async(
        self,
        request: main_models.ListDeliveryRequest,
    ) -> main_models.ListDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.list_delivery_with_options_async(request, runtime)

    def list_dispose_strategy_with_options(
        self,
        request: main_models.ListDisposeStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDisposeStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.effective_status):
            body['EffectiveStatus'] = request.effective_status
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_types):
            body['PlaybookTypes'] = request.playbook_types
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDisposeStrategy',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisposeStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dispose_strategy_with_options_async(
        self,
        request: main_models.ListDisposeStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDisposeStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.effective_status):
            body['EffectiveStatus'] = request.effective_status
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_types):
            body['PlaybookTypes'] = request.playbook_types
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDisposeStrategy',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisposeStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dispose_strategy(
        self,
        request: main_models.ListDisposeStrategyRequest,
    ) -> main_models.ListDisposeStrategyResponse:
        runtime = RuntimeOptions()
        return self.list_dispose_strategy_with_options(request, runtime)

    async def list_dispose_strategy_async(
        self,
        request: main_models.ListDisposeStrategyRequest,
    ) -> main_models.ListDisposeStrategyResponse:
        runtime = RuntimeOptions()
        return await self.list_dispose_strategy_with_options_async(request, runtime)

    def list_entities_with_options(
        self,
        request: main_models.ListEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.entity_uuids):
            body['EntityUuids'] = request.entity_uuids
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.is_malware_entity):
            body['IsMalwareEntity'] = request.is_malware_entity
        if not DaraCore.is_null(request.malware_type):
            body['MalwareType'] = request.malware_type
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEntities',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_with_options_async(
        self,
        request: main_models.ListEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.entity_name):
            body['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            body['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            body['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.entity_uuids):
            body['EntityUuids'] = request.entity_uuids
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.is_malware_entity):
            body['IsMalwareEntity'] = request.is_malware_entity
        if not DaraCore.is_null(request.malware_type):
            body['MalwareType'] = request.malware_type
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEntities',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities(
        self,
        request: main_models.ListEntitiesRequest,
    ) -> main_models.ListEntitiesResponse:
        runtime = RuntimeOptions()
        return self.list_entities_with_options(request, runtime)

    async def list_entities_async(
        self,
        request: main_models.ListEntitiesRequest,
    ) -> main_models.ListEntitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_entities_with_options_async(request, runtime)

    def list_imported_logs_by_prod_with_options(
        self,
        request: main_models.ListImportedLogsByProdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImportedLogsByProdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImportedLogsByProd',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImportedLogsByProdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_imported_logs_by_prod_with_options_async(
        self,
        request: main_models.ListImportedLogsByProdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImportedLogsByProdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImportedLogsByProd',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImportedLogsByProdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_imported_logs_by_prod(
        self,
        request: main_models.ListImportedLogsByProdRequest,
    ) -> main_models.ListImportedLogsByProdResponse:
        runtime = RuntimeOptions()
        return self.list_imported_logs_by_prod_with_options(request, runtime)

    async def list_imported_logs_by_prod_async(
        self,
        request: main_models.ListImportedLogsByProdRequest,
    ) -> main_models.ListImportedLogsByProdResponse:
        runtime = RuntimeOptions()
        return await self.list_imported_logs_by_prod_with_options_async(request, runtime)

    def list_project_log_stores_with_options(
        self,
        request: main_models.ListProjectLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectLogStoresResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not DaraCore.is_null(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectLogStores',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_log_stores_with_options_async(
        self,
        request: main_models.ListProjectLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectLogStoresResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_log_code):
            body['SourceLogCode'] = request.source_log_code
        if not DaraCore.is_null(request.source_prod_code):
            body['SourceProdCode'] = request.source_prod_code
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectLogStores',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_log_stores(
        self,
        request: main_models.ListProjectLogStoresRequest,
    ) -> main_models.ListProjectLogStoresResponse:
        runtime = RuntimeOptions()
        return self.list_project_log_stores_with_options(request, runtime)

    async def list_project_log_stores_async(
        self,
        request: main_models.ListProjectLogStoresRequest,
    ) -> main_models.ListProjectLogStoresResponse:
        runtime = RuntimeOptions()
        return await self.list_project_log_stores_with_options_async(request, runtime)

    def list_rd_users_with_options(
        self,
        request: main_models.ListRdUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRdUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRdUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRdUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rd_users_with_options_async(
        self,
        request: main_models.ListRdUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRdUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRdUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRdUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rd_users(
        self,
        request: main_models.ListRdUsersRequest,
    ) -> main_models.ListRdUsersResponse:
        runtime = RuntimeOptions()
        return self.list_rd_users_with_options(request, runtime)

    async def list_rd_users_async(
        self,
        request: main_models.ListRdUsersRequest,
    ) -> main_models.ListRdUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_rd_users_with_options_async(request, runtime)

    def modify_bind_account_with_options(
        self,
        request: main_models.ModifyBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.bind_id):
            body['BindId'] = request.bind_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_bind_account_with_options_async(
        self,
        request: main_models.ModifyBindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBindAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_id):
            body['AccessId'] = request.access_id
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.bind_id):
            body['BindId'] = request.bind_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBindAccount',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_bind_account(
        self,
        request: main_models.ModifyBindAccountRequest,
    ) -> main_models.ModifyBindAccountResponse:
        runtime = RuntimeOptions()
        return self.modify_bind_account_with_options(request, runtime)

    async def modify_bind_account_async(
        self,
        request: main_models.ModifyBindAccountRequest,
    ) -> main_models.ModifyBindAccountResponse:
        runtime = RuntimeOptions()
        return await self.modify_bind_account_with_options_async(request, runtime)

    def modify_data_source_with_options(
        self,
        request: main_models.ModifyDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not DaraCore.is_null(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not DaraCore.is_null(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        request: main_models.ModifyDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_name):
            body['DataSourceInstanceName'] = request.data_source_instance_name
        if not DaraCore.is_null(request.data_source_instance_params):
            body['DataSourceInstanceParams'] = request.data_source_instance_params
        if not DaraCore.is_null(request.data_source_instance_remark):
            body['DataSourceInstanceRemark'] = request.data_source_instance_remark
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataSource',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source(
        self,
        request: main_models.ModifyDataSourceRequest,
    ) -> main_models.ModifyDataSourceResponse:
        runtime = RuntimeOptions()
        return self.modify_data_source_with_options(request, runtime)

    async def modify_data_source_async(
        self,
        request: main_models.ModifyDataSourceRequest,
    ) -> main_models.ModifyDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_source_with_options_async(request, runtime)

    def modify_data_source_log_with_options(
        self,
        request: main_models.ModifyDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataSourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_log_with_options_async(
        self,
        request: main_models.ModifyDataSourceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataSourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['AccountId'] = request.account_id
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.data_source_instance_id):
            body['DataSourceInstanceId'] = request.data_source_instance_id
        if not DaraCore.is_null(request.data_source_instance_logs):
            body['DataSourceInstanceLogs'] = request.data_source_instance_logs
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.log_instance_id):
            body['LogInstanceId'] = request.log_instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataSourceLog',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataSourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source_log(
        self,
        request: main_models.ModifyDataSourceLogRequest,
    ) -> main_models.ModifyDataSourceLogResponse:
        runtime = RuntimeOptions()
        return self.modify_data_source_log_with_options(request, runtime)

    async def modify_data_source_log_async(
        self,
        request: main_models.ModifyDataSourceLogRequest,
    ) -> main_models.ModifyDataSourceLogResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_source_log_with_options_async(request, runtime)

    def open_delivery_with_options(
        self,
        request: main_models.OpenDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_delivery_with_options_async(
        self,
        request: main_models.OpenDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDelivery',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_delivery(
        self,
        request: main_models.OpenDeliveryRequest,
    ) -> main_models.OpenDeliveryResponse:
        runtime = RuntimeOptions()
        return self.open_delivery_with_options(request, runtime)

    async def open_delivery_async(
        self,
        request: main_models.OpenDeliveryRequest,
    ) -> main_models.OpenDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.open_delivery_with_options_async(request, runtime)

    def post_automate_response_config_with_options(
        self,
        request: main_models.PostAutomateResponseConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostAutomateResponseConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_config):
            body['ActionConfig'] = request.action_config
        if not DaraCore.is_null(request.action_type):
            body['ActionType'] = request.action_type
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.execution_condition):
            body['ExecutionCondition'] = request.execution_condition
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostAutomateResponseConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_automate_response_config_with_options_async(
        self,
        request: main_models.PostAutomateResponseConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostAutomateResponseConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_config):
            body['ActionConfig'] = request.action_config
        if not DaraCore.is_null(request.action_type):
            body['ActionType'] = request.action_type
        if not DaraCore.is_null(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not DaraCore.is_null(request.execution_condition):
            body['ExecutionCondition'] = request.execution_condition
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostAutomateResponseConfig',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostAutomateResponseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_automate_response_config(
        self,
        request: main_models.PostAutomateResponseConfigRequest,
    ) -> main_models.PostAutomateResponseConfigResponse:
        runtime = RuntimeOptions()
        return self.post_automate_response_config_with_options(request, runtime)

    async def post_automate_response_config_async(
        self,
        request: main_models.PostAutomateResponseConfigRequest,
    ) -> main_models.PostAutomateResponseConfigResponse:
        runtime = RuntimeOptions()
        return await self.post_automate_response_config_with_options_async(request, runtime)

    def post_customize_rule_with_options(
        self,
        request: main_models.PostCustomizeRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostCustomizeRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not DaraCore.is_null(request.att_ck):
            body['AttCk'] = request.att_ck
        if not DaraCore.is_null(request.event_transfer_ext):
            body['EventTransferExt'] = request.event_transfer_ext
        if not DaraCore.is_null(request.event_transfer_switch):
            body['EventTransferSwitch'] = request.event_transfer_switch
        if not DaraCore.is_null(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.log_source_mds):
            body['LogSourceMds'] = request.log_source_mds
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.log_type_mds):
            body['LogTypeMds'] = request.log_type_mds
        if not DaraCore.is_null(request.query_cycle):
            body['QueryCycle'] = request.query_cycle
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_condition):
            body['RuleCondition'] = request.rule_condition
        if not DaraCore.is_null(request.rule_desc):
            body['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_group):
            body['RuleGroup'] = request.rule_group
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_threshold):
            body['RuleThreshold'] = request.rule_threshold
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostCustomizeRule',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_customize_rule_with_options_async(
        self,
        request: main_models.PostCustomizeRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostCustomizeRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not DaraCore.is_null(request.att_ck):
            body['AttCk'] = request.att_ck
        if not DaraCore.is_null(request.event_transfer_ext):
            body['EventTransferExt'] = request.event_transfer_ext
        if not DaraCore.is_null(request.event_transfer_switch):
            body['EventTransferSwitch'] = request.event_transfer_switch
        if not DaraCore.is_null(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.log_source):
            body['LogSource'] = request.log_source
        if not DaraCore.is_null(request.log_source_mds):
            body['LogSourceMds'] = request.log_source_mds
        if not DaraCore.is_null(request.log_type):
            body['LogType'] = request.log_type
        if not DaraCore.is_null(request.log_type_mds):
            body['LogTypeMds'] = request.log_type_mds
        if not DaraCore.is_null(request.query_cycle):
            body['QueryCycle'] = request.query_cycle
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_condition):
            body['RuleCondition'] = request.rule_condition
        if not DaraCore.is_null(request.rule_desc):
            body['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_group):
            body['RuleGroup'] = request.rule_group
        if not DaraCore.is_null(request.rule_name):
            body['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_threshold):
            body['RuleThreshold'] = request.rule_threshold
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostCustomizeRule',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostCustomizeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_customize_rule(
        self,
        request: main_models.PostCustomizeRuleRequest,
    ) -> main_models.PostCustomizeRuleResponse:
        runtime = RuntimeOptions()
        return self.post_customize_rule_with_options(request, runtime)

    async def post_customize_rule_async(
        self,
        request: main_models.PostCustomizeRuleRequest,
    ) -> main_models.PostCustomizeRuleResponse:
        runtime = RuntimeOptions()
        return await self.post_customize_rule_with_options_async(request, runtime)

    def post_customize_rule_test_with_options(
        self,
        request: main_models.PostCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.simulated_data):
            body['SimulatedData'] = request.simulated_data
        if not DaraCore.is_null(request.test_type):
            body['TestType'] = request.test_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_customize_rule_test_with_options_async(
        self,
        request: main_models.PostCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.simulated_data):
            body['SimulatedData'] = request.simulated_data
        if not DaraCore.is_null(request.test_type):
            body['TestType'] = request.test_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_customize_rule_test(
        self,
        request: main_models.PostCustomizeRuleTestRequest,
    ) -> main_models.PostCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return self.post_customize_rule_test_with_options(request, runtime)

    async def post_customize_rule_test_async(
        self,
        request: main_models.PostCustomizeRuleTestRequest,
    ) -> main_models.PostCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return await self.post_customize_rule_test_with_options_async(request, runtime)

    def post_event_dispose_and_whiterule_list_with_options(
        self,
        request: main_models.PostEventDisposeAndWhiteruleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostEventDisposeAndWhiteruleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dispose_strategy_ids):
            body['DisposeStrategyIds'] = request.dispose_strategy_ids
        if not DaraCore.is_null(request.event_dispose):
            body['EventDispose'] = request.event_dispose
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.receiver_info):
            body['ReceiverInfo'] = request.receiver_info
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.response_source):
            body['ResponseSource'] = request.response_source
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostEventDisposeAndWhiteruleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEventDisposeAndWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_event_dispose_and_whiterule_list_with_options_async(
        self,
        request: main_models.PostEventDisposeAndWhiteruleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostEventDisposeAndWhiteruleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dispose_strategy_ids):
            body['DisposeStrategyIds'] = request.dispose_strategy_ids
        if not DaraCore.is_null(request.event_dispose):
            body['EventDispose'] = request.event_dispose
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.owner):
            body['Owner'] = request.owner
        if not DaraCore.is_null(request.receiver_info):
            body['ReceiverInfo'] = request.receiver_info
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.response_source):
            body['ResponseSource'] = request.response_source
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostEventDisposeAndWhiteruleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEventDisposeAndWhiteruleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_event_dispose_and_whiterule_list(
        self,
        request: main_models.PostEventDisposeAndWhiteruleListRequest,
    ) -> main_models.PostEventDisposeAndWhiteruleListResponse:
        runtime = RuntimeOptions()
        return self.post_event_dispose_and_whiterule_list_with_options(request, runtime)

    async def post_event_dispose_and_whiterule_list_async(
        self,
        request: main_models.PostEventDisposeAndWhiteruleListRequest,
    ) -> main_models.PostEventDisposeAndWhiteruleListResponse:
        runtime = RuntimeOptions()
        return await self.post_event_dispose_and_whiterule_list_with_options_async(request, runtime)

    def post_event_whiterule_list_with_options(
        self,
        request: main_models.PostEventWhiteruleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostEventWhiteruleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.whiterule_list):
            body['WhiteruleList'] = request.whiterule_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostEventWhiteruleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEventWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_event_whiterule_list_with_options_async(
        self,
        request: main_models.PostEventWhiteruleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostEventWhiteruleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.whiterule_list):
            body['WhiteruleList'] = request.whiterule_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostEventWhiteruleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEventWhiteruleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_event_whiterule_list(
        self,
        request: main_models.PostEventWhiteruleListRequest,
    ) -> main_models.PostEventWhiteruleListResponse:
        runtime = RuntimeOptions()
        return self.post_event_whiterule_list_with_options(request, runtime)

    async def post_event_whiterule_list_async(
        self,
        request: main_models.PostEventWhiteruleListRequest,
    ) -> main_models.PostEventWhiteruleListResponse:
        runtime = RuntimeOptions()
        return await self.post_event_whiterule_list_with_options_async(request, runtime)

    def post_finish_customize_rule_test_with_options(
        self,
        request: main_models.PostFinishCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostFinishCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostFinishCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostFinishCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_finish_customize_rule_test_with_options_async(
        self,
        request: main_models.PostFinishCustomizeRuleTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostFinishCustomizeRuleTestResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostFinishCustomizeRuleTest',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostFinishCustomizeRuleTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_finish_customize_rule_test(
        self,
        request: main_models.PostFinishCustomizeRuleTestRequest,
    ) -> main_models.PostFinishCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return self.post_finish_customize_rule_test_with_options(request, runtime)

    async def post_finish_customize_rule_test_async(
        self,
        request: main_models.PostFinishCustomizeRuleTestRequest,
    ) -> main_models.PostFinishCustomizeRuleTestResponse:
        runtime = RuntimeOptions()
        return await self.post_finish_customize_rule_test_with_options_async(request, runtime)

    def post_rule_status_change_with_options(
        self,
        request: main_models.PostRuleStatusChangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostRuleStatusChangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.in_use):
            body['InUse'] = request.in_use
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostRuleStatusChange',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostRuleStatusChangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_rule_status_change_with_options_async(
        self,
        request: main_models.PostRuleStatusChangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PostRuleStatusChangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.in_use):
            body['InUse'] = request.in_use
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostRuleStatusChange',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostRuleStatusChangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_rule_status_change(
        self,
        request: main_models.PostRuleStatusChangeRequest,
    ) -> main_models.PostRuleStatusChangeResponse:
        runtime = RuntimeOptions()
        return self.post_rule_status_change_with_options(request, runtime)

    async def post_rule_status_change_async(
        self,
        request: main_models.PostRuleStatusChangeRequest,
    ) -> main_models.PostRuleStatusChangeResponse:
        runtime = RuntimeOptions()
        return await self.post_rule_status_change_with_options_async(request, runtime)

    def restore_capacity_with_options(
        self,
        request: main_models.RestoreCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreCapacityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreCapacity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_capacity_with_options_async(
        self,
        request: main_models.RestoreCapacityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreCapacityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreCapacity',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_capacity(
        self,
        request: main_models.RestoreCapacityRequest,
    ) -> main_models.RestoreCapacityResponse:
        runtime = RuntimeOptions()
        return self.restore_capacity_with_options(request, runtime)

    async def restore_capacity_async(
        self,
        request: main_models.RestoreCapacityRequest,
    ) -> main_models.RestoreCapacityResponse:
        runtime = RuntimeOptions()
        return await self.restore_capacity_with_options_async(request, runtime)

    def set_storage_with_options(
        self,
        request: main_models.SetStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_storage_with_options_async(
        self,
        request: main_models.SetStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetStorage',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_storage(
        self,
        request: main_models.SetStorageRequest,
    ) -> main_models.SetStorageResponse:
        runtime = RuntimeOptions()
        return self.set_storage_with_options(request, runtime)

    async def set_storage_async(
        self,
        request: main_models.SetStorageRequest,
    ) -> main_models.SetStorageResponse:
        runtime = RuntimeOptions()
        return await self.set_storage_with_options_async(request, runtime)

    def submit_import_log_tasks_with_options(
        self,
        request: main_models.SubmitImportLogTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImportLogTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accounts):
            body['Accounts'] = request.accounts
        if not DaraCore.is_null(request.auto_imported):
            body['AutoImported'] = request.auto_imported
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImportLogTasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImportLogTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_import_log_tasks_with_options_async(
        self,
        request: main_models.SubmitImportLogTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImportLogTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accounts):
            body['Accounts'] = request.accounts
        if not DaraCore.is_null(request.auto_imported):
            body['AutoImported'] = request.auto_imported
        if not DaraCore.is_null(request.cloud_code):
            body['CloudCode'] = request.cloud_code
        if not DaraCore.is_null(request.log_codes):
            body['LogCodes'] = request.log_codes
        if not DaraCore.is_null(request.prod_code):
            body['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImportLogTasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImportLogTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_import_log_tasks(
        self,
        request: main_models.SubmitImportLogTasksRequest,
    ) -> main_models.SubmitImportLogTasksResponse:
        runtime = RuntimeOptions()
        return self.submit_import_log_tasks_with_options(request, runtime)

    async def submit_import_log_tasks_async(
        self,
        request: main_models.SubmitImportLogTasksRequest,
    ) -> main_models.SubmitImportLogTasksResponse:
        runtime = RuntimeOptions()
        return await self.submit_import_log_tasks_with_options_async(request, runtime)

    def update_automate_response_config_status_with_options(
        self,
        request: main_models.UpdateAutomateResponseConfigStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutomateResponseConfigStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.in_use):
            body['InUse'] = request.in_use
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutomateResponseConfigStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutomateResponseConfigStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_automate_response_config_status_with_options_async(
        self,
        request: main_models.UpdateAutomateResponseConfigStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutomateResponseConfigStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.in_use):
            body['InUse'] = request.in_use
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutomateResponseConfigStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutomateResponseConfigStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_automate_response_config_status(
        self,
        request: main_models.UpdateAutomateResponseConfigStatusRequest,
    ) -> main_models.UpdateAutomateResponseConfigStatusResponse:
        runtime = RuntimeOptions()
        return self.update_automate_response_config_status_with_options(request, runtime)

    async def update_automate_response_config_status_async(
        self,
        request: main_models.UpdateAutomateResponseConfigStatusRequest,
    ) -> main_models.UpdateAutomateResponseConfigStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_automate_response_config_status_with_options_async(request, runtime)

    def update_white_rule_list_with_options(
        self,
        request: main_models.UpdateWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expression):
            body['Expression'] = request.expression
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.white_rule_id):
            body['WhiteRuleId'] = request.white_rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_white_rule_list_with_options_async(
        self,
        request: main_models.UpdateWhiteRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWhiteRuleListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expression):
            body['Expression'] = request.expression
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.white_rule_id):
            body['WhiteRuleId'] = request.white_rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWhiteRuleList',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWhiteRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_white_rule_list(
        self,
        request: main_models.UpdateWhiteRuleListRequest,
    ) -> main_models.UpdateWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return self.update_white_rule_list_with_options(request, runtime)

    async def update_white_rule_list_async(
        self,
        request: main_models.UpdateWhiteRuleListRequest,
    ) -> main_models.UpdateWhiteRuleListResponse:
        runtime = RuntimeOptions()
        return await self.update_white_rule_list_with_options_async(request, runtime)
