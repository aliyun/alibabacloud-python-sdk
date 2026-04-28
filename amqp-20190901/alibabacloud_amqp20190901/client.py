# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_amqp20190901 import models as main_models
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
        self._endpoint = self.get_endpoint('amqp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_with_options(
        self,
        request: main_models.BindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.argument):
            query['Argument'] = request.argument
        if not DaraCore.is_null(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dst_name):
            query['DstName'] = request.dst_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_name):
            query['SrcName'] = request.src_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Bind',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_with_options_async(
        self,
        request: main_models.BindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.argument):
            query['Argument'] = request.argument
        if not DaraCore.is_null(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dst_name):
            query['DstName'] = request.dst_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_name):
            query['SrcName'] = request.src_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Bind',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind(
        self,
        request: main_models.BindRequest,
    ) -> main_models.BindResponse:
        runtime = RuntimeOptions()
        return self.bind_with_options(request, runtime)

    async def bind_async(
        self,
        request: main_models.BindRequest,
    ) -> main_models.BindResponse:
        runtime = RuntimeOptions()
        return await self.bind_with_options_async(request, runtime)

    def cancel_user_setting_with_options(
        self,
        request: main_models.CancelUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_user_setting_with_options_async(
        self,
        request: main_models.CancelUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_user_setting(
        self,
        request: main_models.CancelUserSettingRequest,
    ) -> main_models.CancelUserSettingResponse:
        runtime = RuntimeOptions()
        return self.cancel_user_setting_with_options(request, runtime)

    async def cancel_user_setting_async(
        self,
        request: main_models.CancelUserSettingRequest,
    ) -> main_models.CancelUserSettingResponse:
        runtime = RuntimeOptions()
        return await self.cancel_user_setting_with_options_async(request, runtime)

    def configure_user_setting_with_options(
        self,
        request: main_models.ConfigureUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logstore):
            query['Logstore'] = request.logstore
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.put_type):
            query['PutType'] = request.put_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_user_setting_with_options_async(
        self,
        request: main_models.ConfigureUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logstore):
            query['Logstore'] = request.logstore
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.put_type):
            query['PutType'] = request.put_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_user_setting(
        self,
        request: main_models.ConfigureUserSettingRequest,
    ) -> main_models.ConfigureUserSettingResponse:
        runtime = RuntimeOptions()
        return self.configure_user_setting_with_options(request, runtime)

    async def configure_user_setting_async(
        self,
        request: main_models.ConfigureUserSettingRequest,
    ) -> main_models.ConfigureUserSettingResponse:
        runtime = RuntimeOptions()
        return await self.configure_user_setting_with_options_async(request, runtime)

    def console_clear_pretend_status_with_options(
        self,
        request: main_models.ConsoleClearPretendStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConsoleClearPretendStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConsoleClearPretendStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConsoleClearPretendStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_clear_pretend_status_with_options_async(
        self,
        request: main_models.ConsoleClearPretendStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConsoleClearPretendStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConsoleClearPretendStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConsoleClearPretendStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_clear_pretend_status(
        self,
        request: main_models.ConsoleClearPretendStatusRequest,
    ) -> main_models.ConsoleClearPretendStatusResponse:
        runtime = RuntimeOptions()
        return self.console_clear_pretend_status_with_options(request, runtime)

    async def console_clear_pretend_status_async(
        self,
        request: main_models.ConsoleClearPretendStatusRequest,
    ) -> main_models.ConsoleClearPretendStatusResponse:
        runtime = RuntimeOptions()
        return await self.console_clear_pretend_status_with_options_async(request, runtime)

    def console_save_pretend_status_with_options(
        self,
        request: main_models.ConsoleSavePretendStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConsoleSavePretendStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConsoleSavePretendStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConsoleSavePretendStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_save_pretend_status_with_options_async(
        self,
        request: main_models.ConsoleSavePretendStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConsoleSavePretendStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConsoleSavePretendStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConsoleSavePretendStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_save_pretend_status(
        self,
        request: main_models.ConsoleSavePretendStatusRequest,
    ) -> main_models.ConsoleSavePretendStatusResponse:
        runtime = RuntimeOptions()
        return self.console_save_pretend_status_with_options(request, runtime)

    async def console_save_pretend_status_async(
        self,
        request: main_models.ConsoleSavePretendStatusRequest,
    ) -> main_models.ConsoleSavePretendStatusResponse:
        runtime = RuntimeOptions()
        return await self.console_save_pretend_status_with_options_async(request, runtime)

    def create_cloud_monitor_slrwith_options(
        self,
        request: main_models.CreateCloudMonitorSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudMonitorSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudMonitorSLR',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudMonitorSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_monitor_slrwith_options_async(
        self,
        request: main_models.CreateCloudMonitorSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudMonitorSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudMonitorSLR',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudMonitorSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_monitor_slr(
        self,
        request: main_models.CreateCloudMonitorSLRRequest,
    ) -> main_models.CreateCloudMonitorSLRResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_monitor_slrwith_options(request, runtime)

    async def create_cloud_monitor_slr_async(
        self,
        request: main_models.CreateCloudMonitorSLRRequest,
    ) -> main_models.CreateCloudMonitorSLRResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_monitor_slrwith_options_async(request, runtime)

    def create_exchange_with_options(
        self,
        request: main_models.CreateExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExchangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alternate_exchange):
            query['AlternateExchange'] = request.alternate_exchange
        if not DaraCore.is_null(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_type):
            query['ExchangeType'] = request.exchange_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.internal):
            query['Internal'] = request.internal
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not DaraCore.is_null(request.xdelayed_type):
            query['XDelayedType'] = request.xdelayed_type
        if not DaraCore.is_null(request.xhash_header):
            query['XHashHeader'] = request.xhash_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_exchange_with_options_async(
        self,
        request: main_models.CreateExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExchangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alternate_exchange):
            query['AlternateExchange'] = request.alternate_exchange
        if not DaraCore.is_null(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_type):
            query['ExchangeType'] = request.exchange_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.internal):
            query['Internal'] = request.internal
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not DaraCore.is_null(request.xdelayed_type):
            query['XDelayedType'] = request.xdelayed_type
        if not DaraCore.is_null(request.xhash_header):
            query['XHashHeader'] = request.xhash_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_exchange(
        self,
        request: main_models.CreateExchangeRequest,
    ) -> main_models.CreateExchangeResponse:
        runtime = RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    async def create_exchange_async(
        self,
        request: main_models.CreateExchangeRequest,
    ) -> main_models.CreateExchangeResponse:
        runtime = RuntimeOptions()
        return await self.create_exchange_with_options_async(request, runtime)

    def create_log_delivery_slrwith_options(
        self,
        request: main_models.CreateLogDeliverySLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogDeliverySLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogDeliverySLR',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogDeliverySLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_delivery_slrwith_options_async(
        self,
        request: main_models.CreateLogDeliverySLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogDeliverySLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogDeliverySLR',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogDeliverySLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_delivery_slr(
        self,
        request: main_models.CreateLogDeliverySLRRequest,
    ) -> main_models.CreateLogDeliverySLRResponse:
        runtime = RuntimeOptions()
        return self.create_log_delivery_slrwith_options(request, runtime)

    async def create_log_delivery_slr_async(
        self,
        request: main_models.CreateLogDeliverySLRRequest,
    ) -> main_models.CreateLogDeliverySLRResponse:
        runtime = RuntimeOptions()
        return await self.create_log_delivery_slrwith_options_async(request, runtime)

    def create_queue_with_options(
        self,
        request: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not DaraCore.is_null(request.auto_expire):
            query['AutoExpire'] = request.auto_expire
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dead_letter_exchange):
            query['DeadLetterExchange'] = request.dead_letter_exchange
        if not DaraCore.is_null(request.dead_letter_routing_key):
            query['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not DaraCore.is_null(request.exclusive):
            query['Exclusive'] = request.exclusive
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_length):
            query['MaxLength'] = request.max_length
        if not DaraCore.is_null(request.maximun_prioty):
            query['MaximunPrioty'] = request.maximun_prioty
        if not DaraCore.is_null(request.message_ttl):
            query['MessageTTL'] = request.message_ttl
        if not DaraCore.is_null(request.ordered):
            query['Ordered'] = request.ordered
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.retry_inherit):
            query['RetryInherit'] = request.retry_inherit
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_times):
            query['RetryTimes'] = request.retry_times
        if not DaraCore.is_null(request.single_active_consumer):
            query['SingleActiveConsumer'] = request.single_active_consumer
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        request: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not DaraCore.is_null(request.auto_expire):
            query['AutoExpire'] = request.auto_expire
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dead_letter_exchange):
            query['DeadLetterExchange'] = request.dead_letter_exchange
        if not DaraCore.is_null(request.dead_letter_routing_key):
            query['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not DaraCore.is_null(request.exclusive):
            query['Exclusive'] = request.exclusive
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_length):
            query['MaxLength'] = request.max_length
        if not DaraCore.is_null(request.maximun_prioty):
            query['MaximunPrioty'] = request.maximun_prioty
        if not DaraCore.is_null(request.message_ttl):
            query['MessageTTL'] = request.message_ttl
        if not DaraCore.is_null(request.ordered):
            query['Ordered'] = request.ordered
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.retry_inherit):
            query['RetryInherit'] = request.retry_inherit
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_times):
            query['RetryTimes'] = request.retry_times
        if not DaraCore.is_null(request.single_active_consumer):
            query['SingleActiveConsumer'] = request.single_active_consumer
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_vhost_with_options(
        self,
        request: main_models.CreateVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vhost_with_options_async(
        self,
        request: main_models.CreateVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vhost(
        self,
        request: main_models.CreateVhostRequest,
    ) -> main_models.CreateVhostResponse:
        runtime = RuntimeOptions()
        return self.create_vhost_with_options(request, runtime)

    async def create_vhost_async(
        self,
        request: main_models.CreateVhostRequest,
    ) -> main_models.CreateVhostResponse:
        runtime = RuntimeOptions()
        return await self.create_vhost_with_options_async(request, runtime)

    def dashboard_check_service_status_with_options(
        self,
        request: main_models.DashboardCheckServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DashboardCheckServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DashboardCheckServiceStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashboardCheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def dashboard_check_service_status_with_options_async(
        self,
        request: main_models.DashboardCheckServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DashboardCheckServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DashboardCheckServiceStatus',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashboardCheckServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dashboard_check_service_status(
        self,
        request: main_models.DashboardCheckServiceStatusRequest,
    ) -> main_models.DashboardCheckServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.dashboard_check_service_status_with_options(request, runtime)

    async def dashboard_check_service_status_async(
        self,
        request: main_models.DashboardCheckServiceStatusRequest,
    ) -> main_models.DashboardCheckServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.dashboard_check_service_status_with_options_async(request, runtime)

    def dashboard_list_with_options(
        self,
        request: main_models.DashboardListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DashboardListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DashboardList',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashboardListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dashboard_list_with_options_async(
        self,
        request: main_models.DashboardListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DashboardListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DashboardList',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DashboardListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dashboard_list(
        self,
        request: main_models.DashboardListRequest,
    ) -> main_models.DashboardListResponse:
        runtime = RuntimeOptions()
        return self.dashboard_list_with_options(request, runtime)

    async def dashboard_list_async(
        self,
        request: main_models.DashboardListRequest,
    ) -> main_models.DashboardListResponse:
        runtime = RuntimeOptions()
        return await self.dashboard_list_with_options_async(request, runtime)

    def delete_exchange_with_options(
        self,
        tmp_req: main_models.DeleteExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExchangeResponse:
        tmp_req.validate()
        request = main_models.DeleteExchangeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exchange_names):
            request.exchange_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exchange_with_options_async(
        self,
        tmp_req: main_models.DeleteExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExchangeResponse:
        tmp_req.validate()
        request = main_models.DeleteExchangeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exchange_names):
            request.exchange_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exchange(
        self,
        request: main_models.DeleteExchangeRequest,
    ) -> main_models.DeleteExchangeResponse:
        runtime = RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    async def delete_exchange_async(
        self,
        request: main_models.DeleteExchangeRequest,
    ) -> main_models.DeleteExchangeResponse:
        runtime = RuntimeOptions()
        return await self.delete_exchange_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        tmp_req: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        tmp_req.validate()
        request = main_models.DeleteQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        tmp_req: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        tmp_req.validate()
        request = main_models.DeleteQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queue(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_static_account_with_options(
        self,
        request: main_models.DeleteStaticAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStaticAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStaticAccount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStaticAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_static_account_with_options_async(
        self,
        request: main_models.DeleteStaticAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStaticAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStaticAccount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStaticAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_static_account(
        self,
        request: main_models.DeleteStaticAccountRequest,
    ) -> main_models.DeleteStaticAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_static_account_with_options(request, runtime)

    async def delete_static_account_async(
        self,
        request: main_models.DeleteStaticAccountRequest,
    ) -> main_models.DeleteStaticAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_static_account_with_options_async(request, runtime)

    def delete_vhost_with_options(
        self,
        tmp_req: main_models.DeleteVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVhostResponse:
        tmp_req.validate()
        request = main_models.DeleteVhostShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vhost_names):
            request.vhost_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not DaraCore.is_null(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vhost_with_options_async(
        self,
        tmp_req: main_models.DeleteVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVhostResponse:
        tmp_req.validate()
        request = main_models.DeleteVhostShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vhost_names):
            request.vhost_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not DaraCore.is_null(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vhost(
        self,
        request: main_models.DeleteVhostRequest,
    ) -> main_models.DeleteVhostResponse:
        runtime = RuntimeOptions()
        return self.delete_vhost_with_options(request, runtime)

    async def delete_vhost_async(
        self,
        request: main_models.DeleteVhostRequest,
    ) -> main_models.DeleteVhostResponse:
        runtime = RuntimeOptions()
        return await self.delete_vhost_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def export_with_options(
        self,
        request: main_models.ExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Export',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_with_options_async(
        self,
        request: main_models.ExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Export',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export(
        self,
        request: main_models.ExportRequest,
    ) -> main_models.ExportResponse:
        runtime = RuntimeOptions()
        return self.export_with_options(request, runtime)

    async def export_async(
        self,
        request: main_models.ExportRequest,
    ) -> main_models.ExportResponse:
        runtime = RuntimeOptions()
        return await self.export_with_options_async(request, runtime)

    def fetch_static_account_with_options(
        self,
        request: main_models.FetchStaticAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchStaticAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_access_key):
            query['AccountAccessKey'] = request.account_access_key
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.skey):
            query['SKey'] = request.skey
        if not DaraCore.is_null(request.secret_sign):
            query['SecretSign'] = request.secret_sign
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchStaticAccount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchStaticAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_static_account_with_options_async(
        self,
        request: main_models.FetchStaticAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchStaticAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_access_key):
            query['AccountAccessKey'] = request.account_access_key
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.skey):
            query['SKey'] = request.skey
        if not DaraCore.is_null(request.secret_sign):
            query['SecretSign'] = request.secret_sign
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchStaticAccount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchStaticAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_static_account(
        self,
        request: main_models.FetchStaticAccountRequest,
    ) -> main_models.FetchStaticAccountResponse:
        runtime = RuntimeOptions()
        return self.fetch_static_account_with_options(request, runtime)

    async def fetch_static_account_async(
        self,
        request: main_models.FetchStaticAccountRequest,
    ) -> main_models.FetchStaticAccountResponse:
        runtime = RuntimeOptions()
        return await self.fetch_static_account_with_options_async(request, runtime)

    def get_ack_info_by_interval_with_options(
        self,
        request: main_models.GetAckInfoByIntervalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAckInfoByIntervalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval_sec):
            query['IntervalSec'] = request.interval_sec
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAckInfoByInterval',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAckInfoByIntervalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ack_info_by_interval_with_options_async(
        self,
        request: main_models.GetAckInfoByIntervalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAckInfoByIntervalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval_sec):
            query['IntervalSec'] = request.interval_sec
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAckInfoByInterval',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAckInfoByIntervalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ack_info_by_interval(
        self,
        request: main_models.GetAckInfoByIntervalRequest,
    ) -> main_models.GetAckInfoByIntervalResponse:
        runtime = RuntimeOptions()
        return self.get_ack_info_by_interval_with_options(request, runtime)

    async def get_ack_info_by_interval_async(
        self,
        request: main_models.GetAckInfoByIntervalRequest,
    ) -> main_models.GetAckInfoByIntervalResponse:
        runtime = RuntimeOptions()
        return await self.get_ack_info_by_interval_with_options_async(request, runtime)

    def get_ack_info_of_message_with_options(
        self,
        request: main_models.GetAckInfoOfMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAckInfoOfMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.consume_status):
            query['ConsumeStatus'] = request.consume_status
        if not DaraCore.is_null(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAckInfoOfMessage',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAckInfoOfMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ack_info_of_message_with_options_async(
        self,
        request: main_models.GetAckInfoOfMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAckInfoOfMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.consume_status):
            query['ConsumeStatus'] = request.consume_status
        if not DaraCore.is_null(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAckInfoOfMessage',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAckInfoOfMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ack_info_of_message(
        self,
        request: main_models.GetAckInfoOfMessageRequest,
    ) -> main_models.GetAckInfoOfMessageResponse:
        runtime = RuntimeOptions()
        return self.get_ack_info_of_message_with_options(request, runtime)

    async def get_ack_info_of_message_async(
        self,
        request: main_models.GetAckInfoOfMessageRequest,
    ) -> main_models.GetAckInfoOfMessageResponse:
        runtime = RuntimeOptions()
        return await self.get_ack_info_of_message_with_options_async(request, runtime)

    def get_binding_count_with_options(
        self,
        request: main_models.GetBindingCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.upstream):
            query['Upstream'] = request.upstream
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBindingCount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_count_with_options_async(
        self,
        request: main_models.GetBindingCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.upstream):
            query['Upstream'] = request.upstream
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBindingCount',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding_count(
        self,
        request: main_models.GetBindingCountRequest,
    ) -> main_models.GetBindingCountResponse:
        runtime = RuntimeOptions()
        return self.get_binding_count_with_options(request, runtime)

    async def get_binding_count_async(
        self,
        request: main_models.GetBindingCountRequest,
    ) -> main_models.GetBindingCountResponse:
        runtime = RuntimeOptions()
        return await self.get_binding_count_with_options_async(request, runtime)

    def get_binding_error_by_task_id_with_options(
        self,
        request: main_models.GetBindingErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBindingErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_error_by_task_id_with_options_async(
        self,
        request: main_models.GetBindingErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBindingErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding_error_by_task_id(
        self,
        request: main_models.GetBindingErrorByTaskIdRequest,
    ) -> main_models.GetBindingErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_binding_error_by_task_id_with_options(request, runtime)

    async def get_binding_error_by_task_id_async(
        self,
        request: main_models.GetBindingErrorByTaskIdRequest,
    ) -> main_models.GetBindingErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_binding_error_by_task_id_with_options_async(request, runtime)

    def get_common_buy_url_with_options(
        self,
        request: main_models.GetCommonBuyUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommonBuyUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommonBuyUrl',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommonBuyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_buy_url_with_options_async(
        self,
        request: main_models.GetCommonBuyUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommonBuyUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommonBuyUrl',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommonBuyUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_common_buy_url(
        self,
        request: main_models.GetCommonBuyUrlRequest,
    ) -> main_models.GetCommonBuyUrlResponse:
        runtime = RuntimeOptions()
        return self.get_common_buy_url_with_options(request, runtime)

    async def get_common_buy_url_async(
        self,
        request: main_models.GetCommonBuyUrlRequest,
    ) -> main_models.GetCommonBuyUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_common_buy_url_with_options_async(request, runtime)

    def get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options(
        self,
        request: main_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeTraceByQueueAndRocketMqMsgId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options_async(
        self,
        request: main_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeTraceByQueueAndRocketMqMsgId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consume_trace_by_queue_and_rocket_mq_msg_id(
        self,
        request: main_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
    ) -> main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        runtime = RuntimeOptions()
        return self.get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options(request, runtime)

    async def get_consume_trace_by_queue_and_rocket_mq_msg_id_async(
        self,
        request: main_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
    ) -> main_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        runtime = RuntimeOptions()
        return await self.get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options_async(request, runtime)

    def get_exchange_error_by_task_id_with_options(
        self,
        request: main_models.GetExchangeErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExchangeErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExchangeErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExchangeErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_exchange_error_by_task_id_with_options_async(
        self,
        request: main_models.GetExchangeErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExchangeErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExchangeErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExchangeErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_exchange_error_by_task_id(
        self,
        request: main_models.GetExchangeErrorByTaskIdRequest,
    ) -> main_models.GetExchangeErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_exchange_error_by_task_id_with_options(request, runtime)

    async def get_exchange_error_by_task_id_async(
        self,
        request: main_models.GetExchangeErrorByTaskIdRequest,
    ) -> main_models.GetExchangeErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_exchange_error_by_task_id_with_options_async(request, runtime)

    def get_exchange_rate_with_options(
        self,
        tmp_req: main_models.GetExchangeRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExchangeRateResponse:
        tmp_req.validate()
        request = main_models.GetExchangeRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exchange_names):
            request.exchange_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExchangeRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExchangeRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_exchange_rate_with_options_async(
        self,
        tmp_req: main_models.GetExchangeRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExchangeRateResponse:
        tmp_req.validate()
        request = main_models.GetExchangeRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exchange_names):
            request.exchange_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExchangeRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExchangeRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_exchange_rate(
        self,
        request: main_models.GetExchangeRateRequest,
    ) -> main_models.GetExchangeRateResponse:
        runtime = RuntimeOptions()
        return self.get_exchange_rate_with_options(request, runtime)

    async def get_exchange_rate_async(
        self,
        request: main_models.GetExchangeRateRequest,
    ) -> main_models.GetExchangeRateResponse:
        runtime = RuntimeOptions()
        return await self.get_exchange_rate_with_options_async(request, runtime)

    def get_msg_id_list_by_queue_with_options(
        self,
        request: main_models.GetMsgIdListByQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMsgIdListByQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMsgIdListByQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMsgIdListByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_msg_id_list_by_queue_with_options_async(
        self,
        request: main_models.GetMsgIdListByQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMsgIdListByQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMsgIdListByQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMsgIdListByQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_msg_id_list_by_queue(
        self,
        request: main_models.GetMsgIdListByQueueRequest,
    ) -> main_models.GetMsgIdListByQueueResponse:
        runtime = RuntimeOptions()
        return self.get_msg_id_list_by_queue_with_options(request, runtime)

    async def get_msg_id_list_by_queue_async(
        self,
        request: main_models.GetMsgIdListByQueueRequest,
    ) -> main_models.GetMsgIdListByQueueResponse:
        runtime = RuntimeOptions()
        return await self.get_msg_id_list_by_queue_with_options_async(request, runtime)

    def get_queue_consumers_with_options(
        self,
        request: main_models.GetQueueConsumersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueConsumers',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_consumers_with_options_async(
        self,
        request: main_models.GetQueueConsumersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueConsumers',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_consumers(
        self,
        request: main_models.GetQueueConsumersRequest,
    ) -> main_models.GetQueueConsumersResponse:
        runtime = RuntimeOptions()
        return self.get_queue_consumers_with_options(request, runtime)

    async def get_queue_consumers_async(
        self,
        request: main_models.GetQueueConsumersRequest,
    ) -> main_models.GetQueueConsumersResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_consumers_with_options_async(request, runtime)

    def get_queue_error_by_task_id_with_options(
        self,
        request: main_models.GetQueueErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_error_by_task_id_with_options_async(
        self,
        request: main_models.GetQueueErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_error_by_task_id(
        self,
        request: main_models.GetQueueErrorByTaskIdRequest,
    ) -> main_models.GetQueueErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_queue_error_by_task_id_with_options(request, runtime)

    async def get_queue_error_by_task_id_async(
        self,
        request: main_models.GetQueueErrorByTaskIdRequest,
    ) -> main_models.GetQueueErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_error_by_task_id_with_options_async(request, runtime)

    def get_queue_rate_with_options(
        self,
        tmp_req: main_models.GetQueueRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueRateResponse:
        tmp_req.validate()
        request = main_models.GetQueueRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_rate_with_options_async(
        self,
        tmp_req: main_models.GetQueueRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueRateResponse:
        tmp_req.validate()
        request = main_models.GetQueueRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_rate(
        self,
        request: main_models.GetQueueRateRequest,
    ) -> main_models.GetQueueRateResponse:
        runtime = RuntimeOptions()
        return self.get_queue_rate_with_options(request, runtime)

    async def get_queue_rate_async(
        self,
        request: main_models.GetQueueRateRequest,
    ) -> main_models.GetQueueRateResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_rate_with_options_async(request, runtime)

    def get_send_trace_by_connection_and_channel_and_delivery_tag_with_options(
        self,
        request: main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            query['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByConnectionAndChannelAndDeliveryTag',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_connection_and_channel_and_delivery_tag_with_options_async(
        self,
        request: main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_id):
            query['ConnectionId'] = request.connection_id
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByConnectionAndChannelAndDeliveryTag',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_connection_and_channel_and_delivery_tag(
        self,
        request: main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
    ) -> main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        runtime = RuntimeOptions()
        return self.get_send_trace_by_connection_and_channel_and_delivery_tag_with_options(request, runtime)

    async def get_send_trace_by_connection_and_channel_and_delivery_tag_async(
        self,
        request: main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
    ) -> main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        runtime = RuntimeOptions()
        return await self.get_send_trace_by_connection_and_channel_and_delivery_tag_with_options_async(request, runtime)

    def get_send_trace_by_msg_id_with_options(
        self,
        request: main_models.GetSendTraceByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByMsgId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_msg_id_with_options_async(
        self,
        request: main_models.GetSendTraceByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByMsgId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_msg_id(
        self,
        request: main_models.GetSendTraceByMsgIdRequest,
    ) -> main_models.GetSendTraceByMsgIdResponse:
        runtime = RuntimeOptions()
        return self.get_send_trace_by_msg_id_with_options(request, runtime)

    async def get_send_trace_by_msg_id_async(
        self,
        request: main_models.GetSendTraceByMsgIdRequest,
    ) -> main_models.GetSendTraceByMsgIdResponse:
        runtime = RuntimeOptions()
        return await self.get_send_trace_by_msg_id_with_options_async(request, runtime)

    def get_send_trace_by_queue_with_options(
        self,
        request: main_models.GetSendTraceByQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_queue_with_options_async(
        self,
        request: main_models.GetSendTraceByQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSendTraceByQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSendTraceByQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSendTraceByQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_queue(
        self,
        request: main_models.GetSendTraceByQueueRequest,
    ) -> main_models.GetSendTraceByQueueResponse:
        runtime = RuntimeOptions()
        return self.get_send_trace_by_queue_with_options(request, runtime)

    async def get_send_trace_by_queue_async(
        self,
        request: main_models.GetSendTraceByQueueRequest,
    ) -> main_models.GetSendTraceByQueueResponse:
        runtime = RuntimeOptions()
        return await self.get_send_trace_by_queue_with_options_async(request, runtime)

    def get_statistics_by_vhost_with_options(
        self,
        request: main_models.GetStatisticsByVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStatisticsByVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStatisticsByVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStatisticsByVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_statistics_by_vhost_with_options_async(
        self,
        request: main_models.GetStatisticsByVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStatisticsByVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStatisticsByVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStatisticsByVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_statistics_by_vhost(
        self,
        request: main_models.GetStatisticsByVhostRequest,
    ) -> main_models.GetStatisticsByVhostResponse:
        runtime = RuntimeOptions()
        return self.get_statistics_by_vhost_with_options(request, runtime)

    async def get_statistics_by_vhost_async(
        self,
        request: main_models.GetStatisticsByVhostRequest,
    ) -> main_models.GetStatisticsByVhostResponse:
        runtime = RuntimeOptions()
        return await self.get_statistics_by_vhost_with_options_async(request, runtime)

    def get_task_by_uid_with_options(
        self,
        request: main_models.GetTaskByUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskByUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskByUid',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskByUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_by_uid_with_options_async(
        self,
        request: main_models.GetTaskByUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskByUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskByUid',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskByUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_by_uid(
        self,
        request: main_models.GetTaskByUidRequest,
    ) -> main_models.GetTaskByUidResponse:
        runtime = RuntimeOptions()
        return self.get_task_by_uid_with_options(request, runtime)

    async def get_task_by_uid_async(
        self,
        request: main_models.GetTaskByUidRequest,
    ) -> main_models.GetTaskByUidResponse:
        runtime = RuntimeOptions()
        return await self.get_task_by_uid_with_options_async(request, runtime)

    def get_tps_by_time_with_options(
        self,
        request: main_models.GetTpsByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTpsByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTpsByTime',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTpsByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tps_by_time_with_options_async(
        self,
        request: main_models.GetTpsByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTpsByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTpsByTime',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTpsByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tps_by_time(
        self,
        request: main_models.GetTpsByTimeRequest,
    ) -> main_models.GetTpsByTimeResponse:
        runtime = RuntimeOptions()
        return self.get_tps_by_time_with_options(request, runtime)

    async def get_tps_by_time_async(
        self,
        request: main_models.GetTpsByTimeRequest,
    ) -> main_models.GetTpsByTimeResponse:
        runtime = RuntimeOptions()
        return await self.get_tps_by_time_with_options_async(request, runtime)

    def get_user_setting_with_options(
        self,
        request: main_models.GetUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_setting_with_options_async(
        self,
        request: main_models.GetUserSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserSetting',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_setting(
        self,
        request: main_models.GetUserSettingRequest,
    ) -> main_models.GetUserSettingResponse:
        runtime = RuntimeOptions()
        return self.get_user_setting_with_options(request, runtime)

    async def get_user_setting_async(
        self,
        request: main_models.GetUserSettingRequest,
    ) -> main_models.GetUserSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_user_setting_with_options_async(request, runtime)

    def get_vhost_error_by_task_id_with_options(
        self,
        request: main_models.GetVhostErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVhostErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVhostErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVhostErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vhost_error_by_task_id_with_options_async(
        self,
        request: main_models.GetVhostErrorByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVhostErrorByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVhostErrorByTaskId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVhostErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vhost_error_by_task_id(
        self,
        request: main_models.GetVhostErrorByTaskIdRequest,
    ) -> main_models.GetVhostErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_vhost_error_by_task_id_with_options(request, runtime)

    async def get_vhost_error_by_task_id_async(
        self,
        request: main_models.GetVhostErrorByTaskIdRequest,
    ) -> main_models.GetVhostErrorByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_vhost_error_by_task_id_with_options_async(request, runtime)

    def get_vhost_rate_with_options(
        self,
        tmp_req: main_models.GetVhostRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVhostRateResponse:
        tmp_req.validate()
        request = main_models.GetVhostRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vhost_names):
            request.vhost_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVhostRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVhostRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vhost_rate_with_options_async(
        self,
        tmp_req: main_models.GetVhostRateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVhostRateResponse:
        tmp_req.validate()
        request = main_models.GetVhostRateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vhost_names):
            request.vhost_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVhostRate',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVhostRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vhost_rate(
        self,
        request: main_models.GetVhostRateRequest,
    ) -> main_models.GetVhostRateResponse:
        runtime = RuntimeOptions()
        return self.get_vhost_rate_with_options(request, runtime)

    async def get_vhost_rate_async(
        self,
        request: main_models.GetVhostRateRequest,
    ) -> main_models.GetVhostRateResponse:
        runtime = RuntimeOptions()
        return await self.get_vhost_rate_with_options_async(request, runtime)

    def import_definition_asynchronous_with_options(
        self,
        request: main_models.ImportDefinitionAsynchronousRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDefinitionAsynchronousResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.oss_url):
            query['OssUrl'] = request.oss_url
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportDefinitionAsynchronous',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDefinitionAsynchronousResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_definition_asynchronous_with_options_async(
        self,
        request: main_models.ImportDefinitionAsynchronousRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportDefinitionAsynchronousResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.oss_url):
            query['OssUrl'] = request.oss_url
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportDefinitionAsynchronous',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDefinitionAsynchronousResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_definition_asynchronous(
        self,
        request: main_models.ImportDefinitionAsynchronousRequest,
    ) -> main_models.ImportDefinitionAsynchronousResponse:
        runtime = RuntimeOptions()
        return self.import_definition_asynchronous_with_options(request, runtime)

    async def import_definition_asynchronous_async(
        self,
        request: main_models.ImportDefinitionAsynchronousRequest,
    ) -> main_models.ImportDefinitionAsynchronousResponse:
        runtime = RuntimeOptions()
        return await self.import_definition_asynchronous_with_options_async(request, runtime)

    def instance_preivew_with_options(
        self,
        request: main_models.InstancePreivewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstancePreivewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstancePreivew',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstancePreivewResponse(),
            self.call_api(params, req, runtime)
        )

    async def instance_preivew_with_options_async(
        self,
        request: main_models.InstancePreivewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstancePreivewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstancePreivew',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstancePreivewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def instance_preivew(
        self,
        request: main_models.InstancePreivewRequest,
    ) -> main_models.InstancePreivewResponse:
        runtime = RuntimeOptions()
        return self.instance_preivew_with_options(request, runtime)

    async def instance_preivew_async(
        self,
        request: main_models.InstancePreivewRequest,
    ) -> main_models.InstancePreivewResponse:
        runtime = RuntimeOptions()
        return await self.instance_preivew_with_options_async(request, runtime)

    def list_exchange_with_options(
        self,
        request: main_models.ListExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name_prefix):
            query['ExchangeNamePrefix'] = request.exchange_name_prefix
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_with_options_async(
        self,
        request: main_models.ListExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name_prefix):
            query['ExchangeNamePrefix'] = request.exchange_name_prefix
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchange',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange(
        self,
        request: main_models.ListExchangeRequest,
    ) -> main_models.ListExchangeResponse:
        runtime = RuntimeOptions()
        return self.list_exchange_with_options(request, runtime)

    async def list_exchange_async(
        self,
        request: main_models.ListExchangeRequest,
    ) -> main_models.ListExchangeResponse:
        runtime = RuntimeOptions()
        return await self.list_exchange_with_options_async(request, runtime)

    def list_exchange_downstream_bindings_with_options(
        self,
        request: main_models.ListExchangeDownstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeDownstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeDownstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeDownstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_downstream_bindings_with_options_async(
        self,
        request: main_models.ListExchangeDownstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeDownstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeDownstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeDownstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange_downstream_bindings(
        self,
        request: main_models.ListExchangeDownstreamBindingsRequest,
    ) -> main_models.ListExchangeDownstreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_exchange_downstream_bindings_with_options(request, runtime)

    async def list_exchange_downstream_bindings_async(
        self,
        request: main_models.ListExchangeDownstreamBindingsRequest,
    ) -> main_models.ListExchangeDownstreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_exchange_downstream_bindings_with_options_async(request, runtime)

    def list_exchange_upstream_bindings_with_options(
        self,
        request: main_models.ListExchangeUpstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeUpstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeUpstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeUpstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_upstream_bindings_with_options_async(
        self,
        request: main_models.ListExchangeUpstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeUpstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeUpstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeUpstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange_upstream_bindings(
        self,
        request: main_models.ListExchangeUpstreamBindingsRequest,
    ) -> main_models.ListExchangeUpstreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_exchange_upstream_bindings_with_options(request, runtime)

    async def list_exchange_upstream_bindings_async(
        self,
        request: main_models.ListExchangeUpstreamBindingsRequest,
    ) -> main_models.ListExchangeUpstreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_exchange_upstream_bindings_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_instance_alarm_with_options(
        self,
        request: main_models.ListInstanceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAlarm',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_alarm_with_options_async(
        self,
        request: main_models.ListInstanceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAlarm',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_alarm(
        self,
        request: main_models.ListInstanceAlarmRequest,
    ) -> main_models.ListInstanceAlarmResponse:
        runtime = RuntimeOptions()
        return self.list_instance_alarm_with_options(request, runtime)

    async def list_instance_alarm_async(
        self,
        request: main_models.ListInstanceAlarmRequest,
    ) -> main_models.ListInstanceAlarmResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_alarm_with_options_async(request, runtime)

    def list_logstore_with_options(
        self,
        request: main_models.ListLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstore',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logstore_with_options_async(
        self,
        request: main_models.ListLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstore',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logstore(
        self,
        request: main_models.ListLogstoreRequest,
    ) -> main_models.ListLogstoreResponse:
        runtime = RuntimeOptions()
        return self.list_logstore_with_options(request, runtime)

    async def list_logstore_async(
        self,
        request: main_models.ListLogstoreRequest,
    ) -> main_models.ListLogstoreResponse:
        runtime = RuntimeOptions()
        return await self.list_logstore_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: main_models.ListProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: main_models.ListProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def list_queue_with_options(
        self,
        request: main_models.ListQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name_prefix):
            query['QueueNamePrefix'] = request.queue_name_prefix
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_with_options_async(
        self,
        request: main_models.ListQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name_prefix):
            query['QueueNamePrefix'] = request.queue_name_prefix
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue(
        self,
        request: main_models.ListQueueRequest,
    ) -> main_models.ListQueueResponse:
        runtime = RuntimeOptions()
        return self.list_queue_with_options(request, runtime)

    async def list_queue_async(
        self,
        request: main_models.ListQueueRequest,
    ) -> main_models.ListQueueResponse:
        runtime = RuntimeOptions()
        return await self.list_queue_with_options_async(request, runtime)

    def list_queue_upstream_bindings_with_options(
        self,
        request: main_models.ListQueueUpstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueUpstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueUpstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueUpstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_upstream_bindings_with_options_async(
        self,
        request: main_models.ListQueueUpstreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueUpstreamBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueUpstreamBindings',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueUpstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue_upstream_bindings(
        self,
        request: main_models.ListQueueUpstreamBindingsRequest,
    ) -> main_models.ListQueueUpstreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_queue_upstream_bindings_with_options(request, runtime)

    async def list_queue_upstream_bindings_async(
        self,
        request: main_models.ListQueueUpstreamBindingsRequest,
    ) -> main_models.ListQueueUpstreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_queue_upstream_bindings_with_options_async(request, runtime)

    def list_static_accounts_with_options(
        self,
        request: main_models.ListStaticAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStaticAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStaticAccounts',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStaticAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_static_accounts_with_options_async(
        self,
        request: main_models.ListStaticAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStaticAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStaticAccounts',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStaticAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_static_accounts(
        self,
        request: main_models.ListStaticAccountsRequest,
    ) -> main_models.ListStaticAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_static_accounts_with_options(request, runtime)

    async def list_static_accounts_async(
        self,
        request: main_models.ListStaticAccountsRequest,
    ) -> main_models.ListStaticAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_static_accounts_with_options_async(request, runtime)

    def list_vhost_with_options(
        self,
        request: main_models.ListVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name_prefix):
            query['VhostNamePrefix'] = request.vhost_name_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vhost_with_options_async(
        self,
        request: main_models.ListVhostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVhostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.vhost_name_prefix):
            query['VhostNamePrefix'] = request.vhost_name_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVhost',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vhost(
        self,
        request: main_models.ListVhostRequest,
    ) -> main_models.ListVhostResponse:
        runtime = RuntimeOptions()
        return self.list_vhost_with_options(request, runtime)

    async def list_vhost_async(
        self,
        request: main_models.ListVhostRequest,
    ) -> main_models.ListVhostResponse:
        runtime = RuntimeOptions()
        return await self.list_vhost_with_options_async(request, runtime)

    def metadata_with_options(
        self,
        request: main_models.MetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Metadata',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def metadata_with_options_async(
        self,
        request: main_models.MetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Metadata',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def metadata(
        self,
        request: main_models.MetadataRequest,
    ) -> main_models.MetadataResponse:
        runtime = RuntimeOptions()
        return self.metadata_with_options(request, runtime)

    async def metadata_async(
        self,
        request: main_models.MetadataRequest,
    ) -> main_models.MetadataResponse:
        runtime = RuntimeOptions()
        return await self.metadata_with_options_async(request, runtime)

    def purge_queue_with_options(
        self,
        tmp_req: main_models.PurgeQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurgeQueueResponse:
        tmp_req.validate()
        request = main_models.PurgeQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PurgeQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurgeQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_queue_with_options_async(
        self,
        tmp_req: main_models.PurgeQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurgeQueueResponse:
        tmp_req.validate()
        request = main_models.PurgeQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.collina):
            query['Collina'] = request.collina
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PurgeQueue',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurgeQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_queue(
        self,
        request: main_models.PurgeQueueRequest,
    ) -> main_models.PurgeQueueResponse:
        runtime = RuntimeOptions()
        return self.purge_queue_with_options(request, runtime)

    async def purge_queue_async(
        self,
        request: main_models.PurgeQueueRequest,
    ) -> main_models.PurgeQueueResponse:
        runtime = RuntimeOptions()
        return await self.purge_queue_with_options_async(request, runtime)

    def query_message_by_message_id_with_options(
        self,
        request: main_models.QueryMessageByMessageIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageByMessageIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessageByMessageId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageByMessageIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_by_message_id_with_options_async(
        self,
        request: main_models.QueryMessageByMessageIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageByMessageIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessageByMessageId',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageByMessageIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_by_message_id(
        self,
        request: main_models.QueryMessageByMessageIdRequest,
    ) -> main_models.QueryMessageByMessageIdResponse:
        runtime = RuntimeOptions()
        return self.query_message_by_message_id_with_options(request, runtime)

    async def query_message_by_message_id_async(
        self,
        request: main_models.QueryMessageByMessageIdRequest,
    ) -> main_models.QueryMessageByMessageIdResponse:
        runtime = RuntimeOptions()
        return await self.query_message_by_message_id_with_options_async(request, runtime)

    def query_message_by_queue_name_with_options(
        self,
        request: main_models.QueryMessageByQueueNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageByQueueNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessageByQueueName',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageByQueueNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_by_queue_name_with_options_async(
        self,
        request: main_models.QueryMessageByQueueNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageByQueueNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessageByQueueName',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageByQueueNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_by_queue_name(
        self,
        request: main_models.QueryMessageByQueueNameRequest,
    ) -> main_models.QueryMessageByQueueNameResponse:
        runtime = RuntimeOptions()
        return self.query_message_by_queue_name_with_options(request, runtime)

    async def query_message_by_queue_name_async(
        self,
        request: main_models.QueryMessageByQueueNameRequest,
    ) -> main_models.QueryMessageByQueueNameResponse:
        runtime = RuntimeOptions()
        return await self.query_message_by_queue_name_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: main_models.SendMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.props):
            query['Props'] = request.props
        if not DaraCore.is_null(request.routing_key):
            query['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: main_models.SendMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.props):
            query['Props'] = request.props
        if not DaraCore.is_null(request.routing_key):
            query['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def send_message_copy_with_options(
        self,
        request: main_models.SendMessageCopyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageCopyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_token):
            query['ProcessToken'] = request.process_token
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessageCopy',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageCopyResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_copy_with_options_async(
        self,
        request: main_models.SendMessageCopyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageCopyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_token):
            query['ProcessToken'] = request.process_token
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessageCopy',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageCopyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message_copy(
        self,
        request: main_models.SendMessageCopyRequest,
    ) -> main_models.SendMessageCopyResponse:
        runtime = RuntimeOptions()
        return self.send_message_copy_with_options(request, runtime)

    async def send_message_copy_async(
        self,
        request: main_models.SendMessageCopyRequest,
    ) -> main_models.SendMessageCopyResponse:
        runtime = RuntimeOptions()
        return await self.send_message_copy_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dst_name):
            query['DstName'] = request.dst_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_name):
            query['SrcName'] = request.src_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.dst_name):
            query['DstName'] = request.dst_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_name):
            query['SrcName'] = request.src_name
        if not DaraCore.is_null(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_instance_retry_strategy_with_options(
        self,
        request: main_models.UpdateInstanceRetryStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceRetryStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_times):
            query['RetryTimes'] = request.retry_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceRetryStrategy',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceRetryStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_retry_strategy_with_options_async(
        self,
        request: main_models.UpdateInstanceRetryStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceRetryStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not DaraCore.is_null(request.retry_times):
            query['RetryTimes'] = request.retry_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceRetryStrategy',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceRetryStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_retry_strategy(
        self,
        request: main_models.UpdateInstanceRetryStrategyRequest,
    ) -> main_models.UpdateInstanceRetryStrategyResponse:
        runtime = RuntimeOptions()
        return self.update_instance_retry_strategy_with_options(request, runtime)

    async def update_instance_retry_strategy_async(
        self,
        request: main_models.UpdateInstanceRetryStrategyRequest,
    ) -> main_models.UpdateInstanceRetryStrategyResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_retry_strategy_with_options_async(request, runtime)

    def update_serverless_switch_with_options(
        self,
        request: main_models.UpdateServerlessSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerlessSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.serverless_switch):
            query['ServerlessSwitch'] = request.serverless_switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerlessSwitch',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerlessSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_serverless_switch_with_options_async(
        self,
        request: main_models.UpdateServerlessSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerlessSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.serverless_switch):
            query['ServerlessSwitch'] = request.serverless_switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerlessSwitch',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerlessSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_serverless_switch(
        self,
        request: main_models.UpdateServerlessSwitchRequest,
    ) -> main_models.UpdateServerlessSwitchResponse:
        runtime = RuntimeOptions()
        return self.update_serverless_switch_with_options(request, runtime)

    async def update_serverless_switch_async(
        self,
        request: main_models.UpdateServerlessSwitchRequest,
    ) -> main_models.UpdateServerlessSwitchResponse:
        runtime = RuntimeOptions()
        return await self.update_serverless_switch_with_options_async(request, runtime)

    def upgrade_limits_with_options(
        self,
        request: main_models.UpgradeLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLimits',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_limits_with_options_async(
        self,
        request: main_models.UpgradeLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeLimits',
            version = '2019-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_limits(
        self,
        request: main_models.UpgradeLimitsRequest,
    ) -> main_models.UpgradeLimitsResponse:
        runtime = RuntimeOptions()
        return self.upgrade_limits_with_options(request, runtime)

    async def upgrade_limits_async(
        self,
        request: main_models.UpgradeLimitsRequest,
    ) -> main_models.UpgradeLimitsResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_limits_with_options_async(request, runtime)
