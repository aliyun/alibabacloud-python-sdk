# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ecs_workbench20220220 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_instance_record_config_with_options(
        self,
        request: main_models.GetInstanceRecordConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceRecordConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceRecordConfig',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_record_config_with_options_async(
        self,
        request: main_models.GetInstanceRecordConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceRecordConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceRecordConfig',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceRecordConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_record_config(
        self,
        request: main_models.GetInstanceRecordConfigRequest,
    ) -> main_models.GetInstanceRecordConfigResponse:
        runtime = RuntimeOptions()
        return self.get_instance_record_config_with_options(request, runtime)

    async def get_instance_record_config_async(
        self,
        request: main_models.GetInstanceRecordConfigRequest,
    ) -> main_models.GetInstanceRecordConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_record_config_with_options_async(request, runtime)

    def list_instance_records_with_options(
        self,
        request: main_models.ListInstanceRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRecords',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_records_with_options_async(
        self,
        request: main_models.ListInstanceRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRecords',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_records(
        self,
        request: main_models.ListInstanceRecordsRequest,
    ) -> main_models.ListInstanceRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_instance_records_with_options(request, runtime)

    async def list_instance_records_async(
        self,
        request: main_models.ListInstanceRecordsRequest,
    ) -> main_models.ListInstanceRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_records_with_options_async(request, runtime)

    def list_terminal_commands_with_options(
        self,
        request: main_models.ListTerminalCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTerminalCommandsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.terminal_session_token):
            body['TerminalSessionToken'] = request.terminal_session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTerminalCommands',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerminalCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terminal_commands_with_options_async(
        self,
        request: main_models.ListTerminalCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTerminalCommandsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.terminal_session_token):
            body['TerminalSessionToken'] = request.terminal_session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTerminalCommands',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerminalCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_terminal_commands(
        self,
        request: main_models.ListTerminalCommandsRequest,
    ) -> main_models.ListTerminalCommandsResponse:
        runtime = RuntimeOptions()
        return self.list_terminal_commands_with_options(request, runtime)

    async def list_terminal_commands_async(
        self,
        request: main_models.ListTerminalCommandsRequest,
    ) -> main_models.ListTerminalCommandsResponse:
        runtime = RuntimeOptions()
        return await self.list_terminal_commands_with_options_async(request, runtime)

    def login_instance_with_options(
        self,
        request: main_models.LoginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_login_info):
            query['InstanceLoginInfo'] = request.instance_login_info
        if not DaraCore.is_null(request.partner_info):
            query['PartnerInfo'] = request.partner_info
        if not DaraCore.is_null(request.user_account):
            query['UserAccount'] = request.user_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoginInstance',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_instance_with_options_async(
        self,
        request: main_models.LoginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_login_info):
            query['InstanceLoginInfo'] = request.instance_login_info
        if not DaraCore.is_null(request.partner_info):
            query['PartnerInfo'] = request.partner_info
        if not DaraCore.is_null(request.user_account):
            query['UserAccount'] = request.user_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoginInstance',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_instance(
        self,
        request: main_models.LoginInstanceRequest,
    ) -> main_models.LoginInstanceResponse:
        runtime = RuntimeOptions()
        return self.login_instance_with_options(request, runtime)

    async def login_instance_async(
        self,
        request: main_models.LoginInstanceRequest,
    ) -> main_models.LoginInstanceResponse:
        runtime = RuntimeOptions()
        return await self.login_instance_with_options_async(request, runtime)

    def set_instance_record_config_with_options(
        self,
        request: main_models.SetInstanceRecordConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstanceRecordConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expiration_days):
            body['ExpirationDays'] = request.expiration_days
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.record_storage_target):
            body['RecordStorageTarget'] = request.record_storage_target
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetInstanceRecordConfig',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstanceRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_record_config_with_options_async(
        self,
        request: main_models.SetInstanceRecordConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstanceRecordConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expiration_days):
            body['ExpirationDays'] = request.expiration_days
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.record_storage_target):
            body['RecordStorageTarget'] = request.record_storage_target
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetInstanceRecordConfig',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstanceRecordConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_record_config(
        self,
        request: main_models.SetInstanceRecordConfigRequest,
    ) -> main_models.SetInstanceRecordConfigResponse:
        runtime = RuntimeOptions()
        return self.set_instance_record_config_with_options(request, runtime)

    async def set_instance_record_config_async(
        self,
        request: main_models.SetInstanceRecordConfigRequest,
    ) -> main_models.SetInstanceRecordConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_instance_record_config_with_options_async(request, runtime)

    def view_instance_records_with_options(
        self,
        request: main_models.ViewInstanceRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewInstanceRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.terminal_session_token):
            body['TerminalSessionToken'] = request.terminal_session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ViewInstanceRecords',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewInstanceRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def view_instance_records_with_options_async(
        self,
        request: main_models.ViewInstanceRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ViewInstanceRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.terminal_session_token):
            body['TerminalSessionToken'] = request.terminal_session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ViewInstanceRecords',
            version = '2022-02-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ViewInstanceRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def view_instance_records(
        self,
        request: main_models.ViewInstanceRecordsRequest,
    ) -> main_models.ViewInstanceRecordsResponse:
        runtime = RuntimeOptions()
        return self.view_instance_records_with_options(request, runtime)

    async def view_instance_records_async(
        self,
        request: main_models.ViewInstanceRecordsRequest,
    ) -> main_models.ViewInstanceRecordsResponse:
        runtime = RuntimeOptions()
        return await self.view_instance_records_with_options_async(request, runtime)
