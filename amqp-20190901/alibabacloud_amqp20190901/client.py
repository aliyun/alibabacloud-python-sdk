# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_amqp20190901 import models as amqp_20190901_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_with_options(
        self,
        request: amqp_20190901_models.BindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.BindResponse:
        """
        @summary 路由绑定
        
        @param request: BindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.argument):
            query['Argument'] = request.argument
        if not UtilClient.is_unset(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dst_name):
            query['DstName'] = request.dst_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_name):
            query['SrcName'] = request.src_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Bind',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.BindResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_with_options_async(
        self,
        request: amqp_20190901_models.BindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.BindResponse:
        """
        @summary 路由绑定
        
        @param request: BindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.argument):
            query['Argument'] = request.argument
        if not UtilClient.is_unset(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dst_name):
            query['DstName'] = request.dst_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_name):
            query['SrcName'] = request.src_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Bind',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.BindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind(
        self,
        request: amqp_20190901_models.BindRequest,
    ) -> amqp_20190901_models.BindResponse:
        """
        @summary 路由绑定
        
        @param request: BindRequest
        @return: BindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_with_options(request, runtime)

    async def bind_async(
        self,
        request: amqp_20190901_models.BindRequest,
    ) -> amqp_20190901_models.BindResponse:
        """
        @summary 路由绑定
        
        @param request: BindRequest
        @return: BindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_with_options_async(request, runtime)

    def cancel_user_setting_with_options(
        self,
        request: amqp_20190901_models.CancelUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CancelUserSettingResponse:
        """
        @summary 删除用户配置
        
        @param request: CancelUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CancelUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_user_setting_with_options_async(
        self,
        request: amqp_20190901_models.CancelUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CancelUserSettingResponse:
        """
        @summary 删除用户配置
        
        @param request: CancelUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CancelUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_user_setting(
        self,
        request: amqp_20190901_models.CancelUserSettingRequest,
    ) -> amqp_20190901_models.CancelUserSettingResponse:
        """
        @summary 删除用户配置
        
        @param request: CancelUserSettingRequest
        @return: CancelUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_user_setting_with_options(request, runtime)

    async def cancel_user_setting_async(
        self,
        request: amqp_20190901_models.CancelUserSettingRequest,
    ) -> amqp_20190901_models.CancelUserSettingResponse:
        """
        @summary 删除用户配置
        
        @param request: CancelUserSettingRequest
        @return: CancelUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_user_setting_with_options_async(request, runtime)

    def configure_user_setting_with_options(
        self,
        request: amqp_20190901_models.ConfigureUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConfigureUserSettingResponse:
        """
        @summary 新增用户配置
        
        @param request: ConfigureUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logstore):
            query['Logstore'] = request.logstore
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.put_type):
            query['PutType'] = request.put_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConfigureUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_user_setting_with_options_async(
        self,
        request: amqp_20190901_models.ConfigureUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConfigureUserSettingResponse:
        """
        @summary 新增用户配置
        
        @param request: ConfigureUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logstore):
            query['Logstore'] = request.logstore
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.put_type):
            query['PutType'] = request.put_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConfigureUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_user_setting(
        self,
        request: amqp_20190901_models.ConfigureUserSettingRequest,
    ) -> amqp_20190901_models.ConfigureUserSettingResponse:
        """
        @summary 新增用户配置
        
        @param request: ConfigureUserSettingRequest
        @return: ConfigureUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_user_setting_with_options(request, runtime)

    async def configure_user_setting_async(
        self,
        request: amqp_20190901_models.ConfigureUserSettingRequest,
    ) -> amqp_20190901_models.ConfigureUserSettingResponse:
        """
        @summary 新增用户配置
        
        @param request: ConfigureUserSettingRequest
        @return: ConfigureUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_user_setting_with_options_async(request, runtime)

    def console_clear_pretend_status_with_options(
        self,
        request: amqp_20190901_models.ConsoleClearPretendStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConsoleClearPretendStatusResponse:
        """
        @summary 清除售后视角状态
        
        @param request: ConsoleClearPretendStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConsoleClearPretendStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleClearPretendStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConsoleClearPretendStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_clear_pretend_status_with_options_async(
        self,
        request: amqp_20190901_models.ConsoleClearPretendStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConsoleClearPretendStatusResponse:
        """
        @summary 清除售后视角状态
        
        @param request: ConsoleClearPretendStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConsoleClearPretendStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleClearPretendStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConsoleClearPretendStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_clear_pretend_status(
        self,
        request: amqp_20190901_models.ConsoleClearPretendStatusRequest,
    ) -> amqp_20190901_models.ConsoleClearPretendStatusResponse:
        """
        @summary 清除售后视角状态
        
        @param request: ConsoleClearPretendStatusRequest
        @return: ConsoleClearPretendStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.console_clear_pretend_status_with_options(request, runtime)

    async def console_clear_pretend_status_async(
        self,
        request: amqp_20190901_models.ConsoleClearPretendStatusRequest,
    ) -> amqp_20190901_models.ConsoleClearPretendStatusResponse:
        """
        @summary 清除售后视角状态
        
        @param request: ConsoleClearPretendStatusRequest
        @return: ConsoleClearPretendStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.console_clear_pretend_status_with_options_async(request, runtime)

    def console_save_pretend_status_with_options(
        self,
        request: amqp_20190901_models.ConsoleSavePretendStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConsoleSavePretendStatusResponse:
        """
        @summary 保存售后视角状态
        
        @param request: ConsoleSavePretendStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConsoleSavePretendStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleSavePretendStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConsoleSavePretendStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_save_pretend_status_with_options_async(
        self,
        request: amqp_20190901_models.ConsoleSavePretendStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ConsoleSavePretendStatusResponse:
        """
        @summary 保存售后视角状态
        
        @param request: ConsoleSavePretendStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConsoleSavePretendStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleSavePretendStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ConsoleSavePretendStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_save_pretend_status(
        self,
        request: amqp_20190901_models.ConsoleSavePretendStatusRequest,
    ) -> amqp_20190901_models.ConsoleSavePretendStatusResponse:
        """
        @summary 保存售后视角状态
        
        @param request: ConsoleSavePretendStatusRequest
        @return: ConsoleSavePretendStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.console_save_pretend_status_with_options(request, runtime)

    async def console_save_pretend_status_async(
        self,
        request: amqp_20190901_models.ConsoleSavePretendStatusRequest,
    ) -> amqp_20190901_models.ConsoleSavePretendStatusResponse:
        """
        @summary 保存售后视角状态
        
        @param request: ConsoleSavePretendStatusRequest
        @return: ConsoleSavePretendStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.console_save_pretend_status_with_options_async(request, runtime)

    def create_cloud_monitor_slrwith_options(
        self,
        request: amqp_20190901_models.CreateCloudMonitorSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateCloudMonitorSLRResponse:
        """
        @summary 创建云监控相关角色
        
        @param request: CreateCloudMonitorSLRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudMonitorSLRResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudMonitorSLR',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateCloudMonitorSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_monitor_slrwith_options_async(
        self,
        request: amqp_20190901_models.CreateCloudMonitorSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateCloudMonitorSLRResponse:
        """
        @summary 创建云监控相关角色
        
        @param request: CreateCloudMonitorSLRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudMonitorSLRResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudMonitorSLR',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateCloudMonitorSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_monitor_slr(
        self,
        request: amqp_20190901_models.CreateCloudMonitorSLRRequest,
    ) -> amqp_20190901_models.CreateCloudMonitorSLRResponse:
        """
        @summary 创建云监控相关角色
        
        @param request: CreateCloudMonitorSLRRequest
        @return: CreateCloudMonitorSLRResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_monitor_slrwith_options(request, runtime)

    async def create_cloud_monitor_slr_async(
        self,
        request: amqp_20190901_models.CreateCloudMonitorSLRRequest,
    ) -> amqp_20190901_models.CreateCloudMonitorSLRResponse:
        """
        @summary 创建云监控相关角色
        
        @param request: CreateCloudMonitorSLRRequest
        @return: CreateCloudMonitorSLRResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_monitor_slrwith_options_async(request, runtime)

    def create_exchange_with_options(
        self,
        request: amqp_20190901_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateExchangeResponse:
        """
        @summary 创建Exchange
        
        @param request: CreateExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExchangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alternate_exchange):
            query['AlternateExchange'] = request.alternate_exchange
        if not UtilClient.is_unset(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            query['ExchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internal):
            query['Internal'] = request.internal
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not UtilClient.is_unset(request.xdelayed_type):
            query['XDelayedType'] = request.xdelayed_type
        if not UtilClient.is_unset(request.xhash_header):
            query['XHashHeader'] = request.xhash_header
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_exchange_with_options_async(
        self,
        request: amqp_20190901_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateExchangeResponse:
        """
        @summary 创建Exchange
        
        @param request: CreateExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExchangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alternate_exchange):
            query['AlternateExchange'] = request.alternate_exchange
        if not UtilClient.is_unset(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            query['ExchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internal):
            query['Internal'] = request.internal
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not UtilClient.is_unset(request.xdelayed_type):
            query['XDelayedType'] = request.xdelayed_type
        if not UtilClient.is_unset(request.xhash_header):
            query['XHashHeader'] = request.xhash_header
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_exchange(
        self,
        request: amqp_20190901_models.CreateExchangeRequest,
    ) -> amqp_20190901_models.CreateExchangeResponse:
        """
        @summary 创建Exchange
        
        @param request: CreateExchangeRequest
        @return: CreateExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    async def create_exchange_async(
        self,
        request: amqp_20190901_models.CreateExchangeRequest,
    ) -> amqp_20190901_models.CreateExchangeResponse:
        """
        @summary 创建Exchange
        
        @param request: CreateExchangeRequest
        @return: CreateExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_exchange_with_options_async(request, runtime)

    def create_log_delivery_slrwith_options(
        self,
        request: amqp_20190901_models.CreateLogDeliverySLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateLogDeliverySLRResponse:
        """
        @summary 创建日志相关角色
        
        @param request: CreateLogDeliverySLRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogDeliverySLRResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogDeliverySLR',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateLogDeliverySLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_delivery_slrwith_options_async(
        self,
        request: amqp_20190901_models.CreateLogDeliverySLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateLogDeliverySLRResponse:
        """
        @summary 创建日志相关角色
        
        @param request: CreateLogDeliverySLRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogDeliverySLRResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogDeliverySLR',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateLogDeliverySLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_delivery_slr(
        self,
        request: amqp_20190901_models.CreateLogDeliverySLRRequest,
    ) -> amqp_20190901_models.CreateLogDeliverySLRResponse:
        """
        @summary 创建日志相关角色
        
        @param request: CreateLogDeliverySLRRequest
        @return: CreateLogDeliverySLRResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_log_delivery_slrwith_options(request, runtime)

    async def create_log_delivery_slr_async(
        self,
        request: amqp_20190901_models.CreateLogDeliverySLRRequest,
    ) -> amqp_20190901_models.CreateLogDeliverySLRResponse:
        """
        @summary 创建日志相关角色
        
        @param request: CreateLogDeliverySLRRequest
        @return: CreateLogDeliverySLRResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_log_delivery_slrwith_options_async(request, runtime)

    def create_queue_with_options(
        self,
        request: amqp_20190901_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateQueueResponse:
        """
        @summary 创建队列
        
        @param request: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not UtilClient.is_unset(request.auto_expire):
            query['AutoExpire'] = request.auto_expire
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dead_letter_exchange):
            query['DeadLetterExchange'] = request.dead_letter_exchange
        if not UtilClient.is_unset(request.dead_letter_routing_key):
            query['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not UtilClient.is_unset(request.exclusive):
            query['Exclusive'] = request.exclusive
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_length):
            query['MaxLength'] = request.max_length
        if not UtilClient.is_unset(request.maximun_prioty):
            query['MaximunPrioty'] = request.maximun_prioty
        if not UtilClient.is_unset(request.message_ttl):
            query['MessageTTL'] = request.message_ttl
        if not UtilClient.is_unset(request.ordered):
            query['Ordered'] = request.ordered
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.retry_inherit):
            query['RetryInherit'] = request.retry_inherit
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_times):
            query['RetryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.single_active_consumer):
            query['SingleActiveConsumer'] = request.single_active_consumer
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        request: amqp_20190901_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateQueueResponse:
        """
        @summary 创建队列
        
        @param request: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete):
            query['AutoDelete'] = request.auto_delete
        if not UtilClient.is_unset(request.auto_expire):
            query['AutoExpire'] = request.auto_expire
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dead_letter_exchange):
            query['DeadLetterExchange'] = request.dead_letter_exchange
        if not UtilClient.is_unset(request.dead_letter_routing_key):
            query['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not UtilClient.is_unset(request.exclusive):
            query['Exclusive'] = request.exclusive
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_length):
            query['MaxLength'] = request.max_length
        if not UtilClient.is_unset(request.maximun_prioty):
            query['MaximunPrioty'] = request.maximun_prioty
        if not UtilClient.is_unset(request.message_ttl):
            query['MessageTTL'] = request.message_ttl
        if not UtilClient.is_unset(request.ordered):
            query['Ordered'] = request.ordered
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.retry_inherit):
            query['RetryInherit'] = request.retry_inherit
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_times):
            query['RetryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.single_active_consumer):
            query['SingleActiveConsumer'] = request.single_active_consumer
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: amqp_20190901_models.CreateQueueRequest,
    ) -> amqp_20190901_models.CreateQueueResponse:
        """
        @summary 创建队列
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: amqp_20190901_models.CreateQueueRequest,
    ) -> amqp_20190901_models.CreateQueueResponse:
        """
        @summary 创建队列
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_vhost_with_options(
        self,
        request: amqp_20190901_models.CreateVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateVhostResponse:
        """
        @summary 创建Vhost
        
        @param request: CreateVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vhost_with_options_async(
        self,
        request: amqp_20190901_models.CreateVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.CreateVhostResponse:
        """
        @summary 创建Vhost
        
        @param request: CreateVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.CreateVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vhost(
        self,
        request: amqp_20190901_models.CreateVhostRequest,
    ) -> amqp_20190901_models.CreateVhostResponse:
        """
        @summary 创建Vhost
        
        @param request: CreateVhostRequest
        @return: CreateVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vhost_with_options(request, runtime)

    async def create_vhost_async(
        self,
        request: amqp_20190901_models.CreateVhostRequest,
    ) -> amqp_20190901_models.CreateVhostResponse:
        """
        @summary 创建Vhost
        
        @param request: CreateVhostRequest
        @return: CreateVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vhost_with_options_async(request, runtime)

    def dashboard_check_service_status_with_options(
        self,
        request: amqp_20190901_models.DashboardCheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DashboardCheckServiceStatusResponse:
        """
        @summary prometheus Dashboard 检查相关服务开通状态
        
        @param request: DashboardCheckServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DashboardCheckServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DashboardCheckServiceStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DashboardCheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def dashboard_check_service_status_with_options_async(
        self,
        request: amqp_20190901_models.DashboardCheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DashboardCheckServiceStatusResponse:
        """
        @summary prometheus Dashboard 检查相关服务开通状态
        
        @param request: DashboardCheckServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DashboardCheckServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DashboardCheckServiceStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DashboardCheckServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dashboard_check_service_status(
        self,
        request: amqp_20190901_models.DashboardCheckServiceStatusRequest,
    ) -> amqp_20190901_models.DashboardCheckServiceStatusResponse:
        """
        @summary prometheus Dashboard 检查相关服务开通状态
        
        @param request: DashboardCheckServiceStatusRequest
        @return: DashboardCheckServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dashboard_check_service_status_with_options(request, runtime)

    async def dashboard_check_service_status_async(
        self,
        request: amqp_20190901_models.DashboardCheckServiceStatusRequest,
    ) -> amqp_20190901_models.DashboardCheckServiceStatusResponse:
        """
        @summary prometheus Dashboard 检查相关服务开通状态
        
        @param request: DashboardCheckServiceStatusRequest
        @return: DashboardCheckServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dashboard_check_service_status_with_options_async(request, runtime)

    def dashboard_list_with_options(
        self,
        request: amqp_20190901_models.DashboardListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DashboardListResponse:
        """
        @summary 获取 arms grafana 大盘 http url
        
        @param request: DashboardListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DashboardListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DashboardList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DashboardListResponse(),
            self.call_api(params, req, runtime)
        )

    async def dashboard_list_with_options_async(
        self,
        request: amqp_20190901_models.DashboardListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DashboardListResponse:
        """
        @summary 获取 arms grafana 大盘 http url
        
        @param request: DashboardListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DashboardListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DashboardList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DashboardListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dashboard_list(
        self,
        request: amqp_20190901_models.DashboardListRequest,
    ) -> amqp_20190901_models.DashboardListResponse:
        """
        @summary 获取 arms grafana 大盘 http url
        
        @param request: DashboardListRequest
        @return: DashboardListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dashboard_list_with_options(request, runtime)

    async def dashboard_list_async(
        self,
        request: amqp_20190901_models.DashboardListRequest,
    ) -> amqp_20190901_models.DashboardListResponse:
        """
        @summary 获取 arms grafana 大盘 http url
        
        @param request: DashboardListRequest
        @return: DashboardListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dashboard_list_with_options_async(request, runtime)

    def delete_exchange_with_options(
        self,
        tmp_req: amqp_20190901_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteExchangeResponse:
        """
        @summary 删除Exchange
        
        @param tmp_req: DeleteExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExchangeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteExchangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exchange_names):
            request.exchange_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exchange_with_options_async(
        self,
        tmp_req: amqp_20190901_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteExchangeResponse:
        """
        @summary 删除Exchange
        
        @param tmp_req: DeleteExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExchangeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteExchangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exchange_names):
            request.exchange_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exchange(
        self,
        request: amqp_20190901_models.DeleteExchangeRequest,
    ) -> amqp_20190901_models.DeleteExchangeResponse:
        """
        @summary 删除Exchange
        
        @param request: DeleteExchangeRequest
        @return: DeleteExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    async def delete_exchange_async(
        self,
        request: amqp_20190901_models.DeleteExchangeRequest,
    ) -> amqp_20190901_models.DeleteExchangeResponse:
        """
        @summary 删除Exchange
        
        @param request: DeleteExchangeRequest
        @return: DeleteExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_exchange_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: amqp_20190901_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: amqp_20190901_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: amqp_20190901_models.DeleteInstanceRequest,
    ) -> amqp_20190901_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: amqp_20190901_models.DeleteInstanceRequest,
    ) -> amqp_20190901_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        tmp_req: amqp_20190901_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteQueueResponse:
        """
        @summary 删除队列
        
        @param tmp_req: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        tmp_req: amqp_20190901_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteQueueResponse:
        """
        @summary 删除队列
        
        @param tmp_req: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queue(
        self,
        request: amqp_20190901_models.DeleteQueueRequest,
    ) -> amqp_20190901_models.DeleteQueueResponse:
        """
        @summary 删除队列
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: amqp_20190901_models.DeleteQueueRequest,
    ) -> amqp_20190901_models.DeleteQueueResponse:
        """
        @summary 删除队列
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_static_account_with_options(
        self,
        request: amqp_20190901_models.DeleteStaticAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteStaticAccountResponse:
        """
        @summary 删除静态账户
        
        @param request: DeleteStaticAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStaticAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStaticAccount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteStaticAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_static_account_with_options_async(
        self,
        request: amqp_20190901_models.DeleteStaticAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteStaticAccountResponse:
        """
        @summary 删除静态账户
        
        @param request: DeleteStaticAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStaticAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStaticAccount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteStaticAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_static_account(
        self,
        request: amqp_20190901_models.DeleteStaticAccountRequest,
    ) -> amqp_20190901_models.DeleteStaticAccountResponse:
        """
        @summary 删除静态账户
        
        @param request: DeleteStaticAccountRequest
        @return: DeleteStaticAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_static_account_with_options(request, runtime)

    async def delete_static_account_async(
        self,
        request: amqp_20190901_models.DeleteStaticAccountRequest,
    ) -> amqp_20190901_models.DeleteStaticAccountResponse:
        """
        @summary 删除静态账户
        
        @param request: DeleteStaticAccountRequest
        @return: DeleteStaticAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_static_account_with_options_async(request, runtime)

    def delete_vhost_with_options(
        self,
        tmp_req: amqp_20190901_models.DeleteVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteVhostResponse:
        """
        @summary 删除Vhost
        
        @param tmp_req: DeleteVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVhostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteVhostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vhost_names):
            request.vhost_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not UtilClient.is_unset(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vhost_with_options_async(
        self,
        tmp_req: amqp_20190901_models.DeleteVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DeleteVhostResponse:
        """
        @summary 删除Vhost
        
        @param tmp_req: DeleteVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVhostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.DeleteVhostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vhost_names):
            request.vhost_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        if not UtilClient.is_unset(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DeleteVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vhost(
        self,
        request: amqp_20190901_models.DeleteVhostRequest,
    ) -> amqp_20190901_models.DeleteVhostResponse:
        """
        @summary 删除Vhost
        
        @param request: DeleteVhostRequest
        @return: DeleteVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vhost_with_options(request, runtime)

    async def delete_vhost_async(
        self,
        request: amqp_20190901_models.DeleteVhostRequest,
    ) -> amqp_20190901_models.DeleteVhostResponse:
        """
        @summary 删除Vhost
        
        @param request: DeleteVhostRequest
        @return: DeleteVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vhost_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: amqp_20190901_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: amqp_20190901_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: amqp_20190901_models.DescribeRegionsRequest,
    ) -> amqp_20190901_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: amqp_20190901_models.DescribeRegionsRequest,
    ) -> amqp_20190901_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def export_with_options(
        self,
        request: amqp_20190901_models.ExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ExportResponse:
        """
        @summary 导出元数据
        
        @param request: ExportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Export',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_with_options_async(
        self,
        request: amqp_20190901_models.ExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ExportResponse:
        """
        @summary 导出元数据
        
        @param request: ExportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Export',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export(
        self,
        request: amqp_20190901_models.ExportRequest,
    ) -> amqp_20190901_models.ExportResponse:
        """
        @summary 导出元数据
        
        @param request: ExportRequest
        @return: ExportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_with_options(request, runtime)

    async def export_async(
        self,
        request: amqp_20190901_models.ExportRequest,
    ) -> amqp_20190901_models.ExportResponse:
        """
        @summary 导出元数据
        
        @param request: ExportRequest
        @return: ExportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_with_options_async(request, runtime)

    def fetch_static_account_with_options(
        self,
        request: amqp_20190901_models.FetchStaticAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.FetchStaticAccountResponse:
        """
        @summary 更新静态账户
        
        @param request: FetchStaticAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchStaticAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_access_key):
            query['AccountAccessKey'] = request.account_access_key
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.skey):
            query['SKey'] = request.skey
        if not UtilClient.is_unset(request.secret_sign):
            query['SecretSign'] = request.secret_sign
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchStaticAccount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.FetchStaticAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_static_account_with_options_async(
        self,
        request: amqp_20190901_models.FetchStaticAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.FetchStaticAccountResponse:
        """
        @summary 更新静态账户
        
        @param request: FetchStaticAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchStaticAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_access_key):
            query['AccountAccessKey'] = request.account_access_key
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.create_time_stamp):
            query['CreateTimeStamp'] = request.create_time_stamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.skey):
            query['SKey'] = request.skey
        if not UtilClient.is_unset(request.secret_sign):
            query['SecretSign'] = request.secret_sign
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchStaticAccount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.FetchStaticAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_static_account(
        self,
        request: amqp_20190901_models.FetchStaticAccountRequest,
    ) -> amqp_20190901_models.FetchStaticAccountResponse:
        """
        @summary 更新静态账户
        
        @param request: FetchStaticAccountRequest
        @return: FetchStaticAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_static_account_with_options(request, runtime)

    async def fetch_static_account_async(
        self,
        request: amqp_20190901_models.FetchStaticAccountRequest,
    ) -> amqp_20190901_models.FetchStaticAccountResponse:
        """
        @summary 更新静态账户
        
        @param request: FetchStaticAccountRequest
        @return: FetchStaticAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_static_account_with_options_async(request, runtime)

    def get_ack_info_by_interval_with_options(
        self,
        request: amqp_20190901_models.GetAckInfoByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetAckInfoByIntervalResponse:
        """
        @summary 根据耗时查询ack信息
        
        @param request: GetAckInfoByIntervalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAckInfoByIntervalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_sec):
            query['IntervalSec'] = request.interval_sec
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAckInfoByInterval',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetAckInfoByIntervalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ack_info_by_interval_with_options_async(
        self,
        request: amqp_20190901_models.GetAckInfoByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetAckInfoByIntervalResponse:
        """
        @summary 根据耗时查询ack信息
        
        @param request: GetAckInfoByIntervalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAckInfoByIntervalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_sec):
            query['IntervalSec'] = request.interval_sec
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAckInfoByInterval',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetAckInfoByIntervalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ack_info_by_interval(
        self,
        request: amqp_20190901_models.GetAckInfoByIntervalRequest,
    ) -> amqp_20190901_models.GetAckInfoByIntervalResponse:
        """
        @summary 根据耗时查询ack信息
        
        @param request: GetAckInfoByIntervalRequest
        @return: GetAckInfoByIntervalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ack_info_by_interval_with_options(request, runtime)

    async def get_ack_info_by_interval_async(
        self,
        request: amqp_20190901_models.GetAckInfoByIntervalRequest,
    ) -> amqp_20190901_models.GetAckInfoByIntervalResponse:
        """
        @summary 根据耗时查询ack信息
        
        @param request: GetAckInfoByIntervalRequest
        @return: GetAckInfoByIntervalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ack_info_by_interval_with_options_async(request, runtime)

    def get_ack_info_of_message_with_options(
        self,
        request: amqp_20190901_models.GetAckInfoOfMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetAckInfoOfMessageResponse:
        """
        @summary 获取一个PushMessage（PullMessage）对应的Ack行为
        
        @param request: GetAckInfoOfMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAckInfoOfMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.consume_status):
            query['ConsumeStatus'] = request.consume_status
        if not UtilClient.is_unset(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAckInfoOfMessage',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetAckInfoOfMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ack_info_of_message_with_options_async(
        self,
        request: amqp_20190901_models.GetAckInfoOfMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetAckInfoOfMessageResponse:
        """
        @summary 获取一个PushMessage（PullMessage）对应的Ack行为
        
        @param request: GetAckInfoOfMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAckInfoOfMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.consume_status):
            query['ConsumeStatus'] = request.consume_status
        if not UtilClient.is_unset(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAckInfoOfMessage',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetAckInfoOfMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ack_info_of_message(
        self,
        request: amqp_20190901_models.GetAckInfoOfMessageRequest,
    ) -> amqp_20190901_models.GetAckInfoOfMessageResponse:
        """
        @summary 获取一个PushMessage（PullMessage）对应的Ack行为
        
        @param request: GetAckInfoOfMessageRequest
        @return: GetAckInfoOfMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ack_info_of_message_with_options(request, runtime)

    async def get_ack_info_of_message_async(
        self,
        request: amqp_20190901_models.GetAckInfoOfMessageRequest,
    ) -> amqp_20190901_models.GetAckInfoOfMessageResponse:
        """
        @summary 获取一个PushMessage（PullMessage）对应的Ack行为
        
        @param request: GetAckInfoOfMessageRequest
        @return: GetAckInfoOfMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ack_info_of_message_with_options_async(request, runtime)

    def get_binding_count_with_options(
        self,
        request: amqp_20190901_models.GetBindingCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetBindingCountResponse:
        """
        @summary 获取绑定数量
        
        @param request: GetBindingCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.upstream):
            query['Upstream'] = request.upstream
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBindingCount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetBindingCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_count_with_options_async(
        self,
        request: amqp_20190901_models.GetBindingCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetBindingCountResponse:
        """
        @summary 获取绑定数量
        
        @param request: GetBindingCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.upstream):
            query['Upstream'] = request.upstream
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBindingCount',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetBindingCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding_count(
        self,
        request: amqp_20190901_models.GetBindingCountRequest,
    ) -> amqp_20190901_models.GetBindingCountResponse:
        """
        @summary 获取绑定数量
        
        @param request: GetBindingCountRequest
        @return: GetBindingCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_binding_count_with_options(request, runtime)

    async def get_binding_count_async(
        self,
        request: amqp_20190901_models.GetBindingCountRequest,
    ) -> amqp_20190901_models.GetBindingCountResponse:
        """
        @summary 获取绑定数量
        
        @param request: GetBindingCountRequest
        @return: GetBindingCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_binding_count_with_options_async(request, runtime)

    def get_binding_error_by_task_id_with_options(
        self,
        request: amqp_20190901_models.GetBindingErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetBindingErrorByTaskIdResponse:
        """
        @summary 获取绑定错误
        
        @param request: GetBindingErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBindingErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetBindingErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_error_by_task_id_with_options_async(
        self,
        request: amqp_20190901_models.GetBindingErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetBindingErrorByTaskIdResponse:
        """
        @summary 获取绑定错误
        
        @param request: GetBindingErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBindingErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetBindingErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding_error_by_task_id(
        self,
        request: amqp_20190901_models.GetBindingErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetBindingErrorByTaskIdResponse:
        """
        @summary 获取绑定错误
        
        @param request: GetBindingErrorByTaskIdRequest
        @return: GetBindingErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_binding_error_by_task_id_with_options(request, runtime)

    async def get_binding_error_by_task_id_async(
        self,
        request: amqp_20190901_models.GetBindingErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetBindingErrorByTaskIdResponse:
        """
        @summary 获取绑定错误
        
        @param request: GetBindingErrorByTaskIdRequest
        @return: GetBindingErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_binding_error_by_task_id_with_options_async(request, runtime)

    def get_common_buy_url_with_options(
        self,
        request: amqp_20190901_models.GetCommonBuyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetCommonBuyUrlResponse:
        """
        @param request: GetCommonBuyUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommonBuyUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonBuyUrl',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetCommonBuyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_buy_url_with_options_async(
        self,
        request: amqp_20190901_models.GetCommonBuyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetCommonBuyUrlResponse:
        """
        @param request: GetCommonBuyUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommonBuyUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonBuyUrl',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetCommonBuyUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_common_buy_url(
        self,
        request: amqp_20190901_models.GetCommonBuyUrlRequest,
    ) -> amqp_20190901_models.GetCommonBuyUrlResponse:
        """
        @param request: GetCommonBuyUrlRequest
        @return: GetCommonBuyUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_common_buy_url_with_options(request, runtime)

    async def get_common_buy_url_async(
        self,
        request: amqp_20190901_models.GetCommonBuyUrlRequest,
    ) -> amqp_20190901_models.GetCommonBuyUrlResponse:
        """
        @param request: GetCommonBuyUrlRequest
        @return: GetCommonBuyUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_common_buy_url_with_options_async(request, runtime)

    def get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options(
        self,
        request: amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        """
        @summary 通过rocketMqMsgId查询消息消费轨迹
        
        @param request: GetConsumeTraceByQueueAndRocketMqMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumeTraceByQueueAndRocketMqMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumeTraceByQueueAndRocketMqMsgId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options_async(
        self,
        request: amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        """
        @summary 通过rocketMqMsgId查询消息消费轨迹
        
        @param request: GetConsumeTraceByQueueAndRocketMqMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumeTraceByQueueAndRocketMqMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumeTraceByQueueAndRocketMqMsgId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consume_trace_by_queue_and_rocket_mq_msg_id(
        self,
        request: amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
    ) -> amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        """
        @summary 通过rocketMqMsgId查询消息消费轨迹
        
        @param request: GetConsumeTraceByQueueAndRocketMqMsgIdRequest
        @return: GetConsumeTraceByQueueAndRocketMqMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options(request, runtime)

    async def get_consume_trace_by_queue_and_rocket_mq_msg_id_async(
        self,
        request: amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdRequest,
    ) -> amqp_20190901_models.GetConsumeTraceByQueueAndRocketMqMsgIdResponse:
        """
        @summary 通过rocketMqMsgId查询消息消费轨迹
        
        @param request: GetConsumeTraceByQueueAndRocketMqMsgIdRequest
        @return: GetConsumeTraceByQueueAndRocketMqMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_consume_trace_by_queue_and_rocket_mq_msg_id_with_options_async(request, runtime)

    def get_exchange_error_by_task_id_with_options(
        self,
        request: amqp_20190901_models.GetExchangeErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetExchangeErrorByTaskIdResponse:
        """
        @summary 获取Exchange错误
        
        @param request: GetExchangeErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExchangeErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExchangeErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetExchangeErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_exchange_error_by_task_id_with_options_async(
        self,
        request: amqp_20190901_models.GetExchangeErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetExchangeErrorByTaskIdResponse:
        """
        @summary 获取Exchange错误
        
        @param request: GetExchangeErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExchangeErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExchangeErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetExchangeErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_exchange_error_by_task_id(
        self,
        request: amqp_20190901_models.GetExchangeErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetExchangeErrorByTaskIdResponse:
        """
        @summary 获取Exchange错误
        
        @param request: GetExchangeErrorByTaskIdRequest
        @return: GetExchangeErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_exchange_error_by_task_id_with_options(request, runtime)

    async def get_exchange_error_by_task_id_async(
        self,
        request: amqp_20190901_models.GetExchangeErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetExchangeErrorByTaskIdResponse:
        """
        @summary 获取Exchange错误
        
        @param request: GetExchangeErrorByTaskIdRequest
        @return: GetExchangeErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_exchange_error_by_task_id_with_options_async(request, runtime)

    def get_exchange_rate_with_options(
        self,
        tmp_req: amqp_20190901_models.GetExchangeRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetExchangeRateResponse:
        """
        @summary 获取Exchange Rate
        
        @param tmp_req: GetExchangeRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExchangeRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetExchangeRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exchange_names):
            request.exchange_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExchangeRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetExchangeRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_exchange_rate_with_options_async(
        self,
        tmp_req: amqp_20190901_models.GetExchangeRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetExchangeRateResponse:
        """
        @summary 获取Exchange Rate
        
        @param tmp_req: GetExchangeRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExchangeRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetExchangeRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exchange_names):
            request.exchange_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exchange_names, 'ExchangeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_names_shrink):
            query['ExchangeNames'] = request.exchange_names_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExchangeRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetExchangeRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_exchange_rate(
        self,
        request: amqp_20190901_models.GetExchangeRateRequest,
    ) -> amqp_20190901_models.GetExchangeRateResponse:
        """
        @summary 获取Exchange Rate
        
        @param request: GetExchangeRateRequest
        @return: GetExchangeRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_exchange_rate_with_options(request, runtime)

    async def get_exchange_rate_async(
        self,
        request: amqp_20190901_models.GetExchangeRateRequest,
    ) -> amqp_20190901_models.GetExchangeRateResponse:
        """
        @summary 获取Exchange Rate
        
        @param request: GetExchangeRateRequest
        @return: GetExchangeRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_exchange_rate_with_options_async(request, runtime)

    def get_msg_id_list_by_queue_with_options(
        self,
        request: amqp_20190901_models.GetMsgIdListByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetMsgIdListByQueueResponse:
        """
        @summary 通过queueName查询一段时间内的消息id列表
        
        @param request: GetMsgIdListByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMsgIdListByQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMsgIdListByQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetMsgIdListByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_msg_id_list_by_queue_with_options_async(
        self,
        request: amqp_20190901_models.GetMsgIdListByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetMsgIdListByQueueResponse:
        """
        @summary 通过queueName查询一段时间内的消息id列表
        
        @param request: GetMsgIdListByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMsgIdListByQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMsgIdListByQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetMsgIdListByQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_msg_id_list_by_queue(
        self,
        request: amqp_20190901_models.GetMsgIdListByQueueRequest,
    ) -> amqp_20190901_models.GetMsgIdListByQueueResponse:
        """
        @summary 通过queueName查询一段时间内的消息id列表
        
        @param request: GetMsgIdListByQueueRequest
        @return: GetMsgIdListByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_msg_id_list_by_queue_with_options(request, runtime)

    async def get_msg_id_list_by_queue_async(
        self,
        request: amqp_20190901_models.GetMsgIdListByQueueRequest,
    ) -> amqp_20190901_models.GetMsgIdListByQueueResponse:
        """
        @summary 通过queueName查询一段时间内的消息id列表
        
        @param request: GetMsgIdListByQueueRequest
        @return: GetMsgIdListByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_msg_id_list_by_queue_with_options_async(request, runtime)

    def get_queue_consumers_with_options(
        self,
        request: amqp_20190901_models.GetQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueConsumersResponse:
        """
        @summary GetQueueConsumers
        
        @param request: GetQueueConsumersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueConsumersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueConsumers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_consumers_with_options_async(
        self,
        request: amqp_20190901_models.GetQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueConsumersResponse:
        """
        @summary GetQueueConsumers
        
        @param request: GetQueueConsumersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueConsumersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueConsumers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_consumers(
        self,
        request: amqp_20190901_models.GetQueueConsumersRequest,
    ) -> amqp_20190901_models.GetQueueConsumersResponse:
        """
        @summary GetQueueConsumers
        
        @param request: GetQueueConsumersRequest
        @return: GetQueueConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_consumers_with_options(request, runtime)

    async def get_queue_consumers_async(
        self,
        request: amqp_20190901_models.GetQueueConsumersRequest,
    ) -> amqp_20190901_models.GetQueueConsumersResponse:
        """
        @summary GetQueueConsumers
        
        @param request: GetQueueConsumersRequest
        @return: GetQueueConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_consumers_with_options_async(request, runtime)

    def get_queue_error_by_task_id_with_options(
        self,
        request: amqp_20190901_models.GetQueueErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueErrorByTaskIdResponse:
        """
        @summary 获取队列错误
        
        @param request: GetQueueErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_error_by_task_id_with_options_async(
        self,
        request: amqp_20190901_models.GetQueueErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueErrorByTaskIdResponse:
        """
        @summary 获取队列错误
        
        @param request: GetQueueErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_error_by_task_id(
        self,
        request: amqp_20190901_models.GetQueueErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetQueueErrorByTaskIdResponse:
        """
        @summary 获取队列错误
        
        @param request: GetQueueErrorByTaskIdRequest
        @return: GetQueueErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_error_by_task_id_with_options(request, runtime)

    async def get_queue_error_by_task_id_async(
        self,
        request: amqp_20190901_models.GetQueueErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetQueueErrorByTaskIdResponse:
        """
        @summary 获取队列错误
        
        @param request: GetQueueErrorByTaskIdRequest
        @return: GetQueueErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_error_by_task_id_with_options_async(request, runtime)

    def get_queue_rate_with_options(
        self,
        tmp_req: amqp_20190901_models.GetQueueRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueRateResponse:
        """
        @summary 获取Queue Rate
        
        @param tmp_req: GetQueueRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetQueueRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_rate_with_options_async(
        self,
        tmp_req: amqp_20190901_models.GetQueueRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetQueueRateResponse:
        """
        @summary 获取Queue Rate
        
        @param tmp_req: GetQueueRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetQueueRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetQueueRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_rate(
        self,
        request: amqp_20190901_models.GetQueueRateRequest,
    ) -> amqp_20190901_models.GetQueueRateResponse:
        """
        @summary 获取Queue Rate
        
        @param request: GetQueueRateRequest
        @return: GetQueueRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_rate_with_options(request, runtime)

    async def get_queue_rate_async(
        self,
        request: amqp_20190901_models.GetQueueRateRequest,
    ) -> amqp_20190901_models.GetQueueRateResponse:
        """
        @summary 获取Queue Rate
        
        @param request: GetQueueRateRequest
        @return: GetQueueRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_rate_with_options_async(request, runtime)

    def get_send_trace_by_connection_and_channel_and_delivery_tag_with_options(
        self,
        request: amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        """
        @summary 根据connectionId,channelId,deliveryTag查询SendMessage
        
        @param request: GetSendTraceByConnectionAndChannelAndDeliveryTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByConnectionAndChannelAndDeliveryTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            query['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByConnectionAndChannelAndDeliveryTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_connection_and_channel_and_delivery_tag_with_options_async(
        self,
        request: amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        """
        @summary 根据connectionId,channelId,deliveryTag查询SendMessage
        
        @param request: GetSendTraceByConnectionAndChannelAndDeliveryTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByConnectionAndChannelAndDeliveryTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_id):
            query['ConnectionId'] = request.connection_id
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.delivery_tag):
            query['DeliveryTag'] = request.delivery_tag
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByConnectionAndChannelAndDeliveryTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_connection_and_channel_and_delivery_tag(
        self,
        request: amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
    ) -> amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        """
        @summary 根据connectionId,channelId,deliveryTag查询SendMessage
        
        @param request: GetSendTraceByConnectionAndChannelAndDeliveryTagRequest
        @return: GetSendTraceByConnectionAndChannelAndDeliveryTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_send_trace_by_connection_and_channel_and_delivery_tag_with_options(request, runtime)

    async def get_send_trace_by_connection_and_channel_and_delivery_tag_async(
        self,
        request: amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagRequest,
    ) -> amqp_20190901_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponse:
        """
        @summary 根据connectionId,channelId,deliveryTag查询SendMessage
        
        @param request: GetSendTraceByConnectionAndChannelAndDeliveryTagRequest
        @return: GetSendTraceByConnectionAndChannelAndDeliveryTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_send_trace_by_connection_and_channel_and_delivery_tag_with_options_async(request, runtime)

    def get_send_trace_by_msg_id_with_options(
        self,
        request: amqp_20190901_models.GetSendTraceByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByMsgIdResponse:
        """
        @summary 通过用户msgId查询消息发送轨迹
        
        @param request: GetSendTraceByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByMsgId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_msg_id_with_options_async(
        self,
        request: amqp_20190901_models.GetSendTraceByMsgIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByMsgIdResponse:
        """
        @summary 通过用户msgId查询消息发送轨迹
        
        @param request: GetSendTraceByMsgIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByMsgIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.msg_id):
            query['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByMsgId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_msg_id(
        self,
        request: amqp_20190901_models.GetSendTraceByMsgIdRequest,
    ) -> amqp_20190901_models.GetSendTraceByMsgIdResponse:
        """
        @summary 通过用户msgId查询消息发送轨迹
        
        @param request: GetSendTraceByMsgIdRequest
        @return: GetSendTraceByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_send_trace_by_msg_id_with_options(request, runtime)

    async def get_send_trace_by_msg_id_async(
        self,
        request: amqp_20190901_models.GetSendTraceByMsgIdRequest,
    ) -> amqp_20190901_models.GetSendTraceByMsgIdResponse:
        """
        @summary 通过用户msgId查询消息发送轨迹
        
        @param request: GetSendTraceByMsgIdRequest
        @return: GetSendTraceByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_send_trace_by_msg_id_with_options_async(request, runtime)

    def get_send_trace_by_queue_with_options(
        self,
        request: amqp_20190901_models.GetSendTraceByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByQueueResponse:
        """
        @summary 根据queue 查询SendMessage
        
        @param request: GetSendTraceByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_send_trace_by_queue_with_options_async(
        self,
        request: amqp_20190901_models.GetSendTraceByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetSendTraceByQueueResponse:
        """
        @summary 根据queue 查询SendMessage
        
        @param request: GetSendTraceByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSendTraceByQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSendTraceByQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetSendTraceByQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_send_trace_by_queue(
        self,
        request: amqp_20190901_models.GetSendTraceByQueueRequest,
    ) -> amqp_20190901_models.GetSendTraceByQueueResponse:
        """
        @summary 根据queue 查询SendMessage
        
        @param request: GetSendTraceByQueueRequest
        @return: GetSendTraceByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_send_trace_by_queue_with_options(request, runtime)

    async def get_send_trace_by_queue_async(
        self,
        request: amqp_20190901_models.GetSendTraceByQueueRequest,
    ) -> amqp_20190901_models.GetSendTraceByQueueResponse:
        """
        @summary 根据queue 查询SendMessage
        
        @param request: GetSendTraceByQueueRequest
        @return: GetSendTraceByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_send_trace_by_queue_with_options_async(request, runtime)

    def get_statistics_by_vhost_with_options(
        self,
        request: amqp_20190901_models.GetStatisticsByVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetStatisticsByVhostResponse:
        """
        @summary GetStatisticsByVhost
        
        @param request: GetStatisticsByVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStatisticsByVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatisticsByVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetStatisticsByVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_statistics_by_vhost_with_options_async(
        self,
        request: amqp_20190901_models.GetStatisticsByVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetStatisticsByVhostResponse:
        """
        @summary GetStatisticsByVhost
        
        @param request: GetStatisticsByVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStatisticsByVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatisticsByVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetStatisticsByVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_statistics_by_vhost(
        self,
        request: amqp_20190901_models.GetStatisticsByVhostRequest,
    ) -> amqp_20190901_models.GetStatisticsByVhostResponse:
        """
        @summary GetStatisticsByVhost
        
        @param request: GetStatisticsByVhostRequest
        @return: GetStatisticsByVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_statistics_by_vhost_with_options(request, runtime)

    async def get_statistics_by_vhost_async(
        self,
        request: amqp_20190901_models.GetStatisticsByVhostRequest,
    ) -> amqp_20190901_models.GetStatisticsByVhostResponse:
        """
        @summary GetStatisticsByVhost
        
        @param request: GetStatisticsByVhostRequest
        @return: GetStatisticsByVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_statistics_by_vhost_with_options_async(request, runtime)

    def get_task_by_uid_with_options(
        self,
        request: amqp_20190901_models.GetTaskByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetTaskByUidResponse:
        """
        @summary 获取任务
        
        @param request: GetTaskByUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskByUidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskByUid',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetTaskByUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_by_uid_with_options_async(
        self,
        request: amqp_20190901_models.GetTaskByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetTaskByUidResponse:
        """
        @summary 获取任务
        
        @param request: GetTaskByUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskByUidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskByUid',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetTaskByUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_by_uid(
        self,
        request: amqp_20190901_models.GetTaskByUidRequest,
    ) -> amqp_20190901_models.GetTaskByUidResponse:
        """
        @summary 获取任务
        
        @param request: GetTaskByUidRequest
        @return: GetTaskByUidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_by_uid_with_options(request, runtime)

    async def get_task_by_uid_async(
        self,
        request: amqp_20190901_models.GetTaskByUidRequest,
    ) -> amqp_20190901_models.GetTaskByUidResponse:
        """
        @summary 获取任务
        
        @param request: GetTaskByUidRequest
        @return: GetTaskByUidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_by_uid_with_options_async(request, runtime)

    def get_tps_by_time_with_options(
        self,
        request: amqp_20190901_models.GetTpsByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetTpsByTimeResponse:
        """
        @summary 查询一段时间内某个实例或是vhost或是queue的tps
        
        @param request: GetTpsByTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTpsByTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTpsByTime',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetTpsByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tps_by_time_with_options_async(
        self,
        request: amqp_20190901_models.GetTpsByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetTpsByTimeResponse:
        """
        @summary 查询一段时间内某个实例或是vhost或是queue的tps
        
        @param request: GetTpsByTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTpsByTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTpsByTime',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetTpsByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tps_by_time(
        self,
        request: amqp_20190901_models.GetTpsByTimeRequest,
    ) -> amqp_20190901_models.GetTpsByTimeResponse:
        """
        @summary 查询一段时间内某个实例或是vhost或是queue的tps
        
        @param request: GetTpsByTimeRequest
        @return: GetTpsByTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tps_by_time_with_options(request, runtime)

    async def get_tps_by_time_async(
        self,
        request: amqp_20190901_models.GetTpsByTimeRequest,
    ) -> amqp_20190901_models.GetTpsByTimeResponse:
        """
        @summary 查询一段时间内某个实例或是vhost或是queue的tps
        
        @param request: GetTpsByTimeRequest
        @return: GetTpsByTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_tps_by_time_with_options_async(request, runtime)

    def get_user_setting_with_options(
        self,
        request: amqp_20190901_models.GetUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetUserSettingResponse:
        """
        @summary 获取用户配置
        
        @param request: GetUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_setting_with_options_async(
        self,
        request: amqp_20190901_models.GetUserSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetUserSettingResponse:
        """
        @summary 获取用户配置
        
        @param request: GetUserSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserSetting',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetUserSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_setting(
        self,
        request: amqp_20190901_models.GetUserSettingRequest,
    ) -> amqp_20190901_models.GetUserSettingResponse:
        """
        @summary 获取用户配置
        
        @param request: GetUserSettingRequest
        @return: GetUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_setting_with_options(request, runtime)

    async def get_user_setting_async(
        self,
        request: amqp_20190901_models.GetUserSettingRequest,
    ) -> amqp_20190901_models.GetUserSettingResponse:
        """
        @summary 获取用户配置
        
        @param request: GetUserSettingRequest
        @return: GetUserSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_setting_with_options_async(request, runtime)

    def get_vhost_error_by_task_id_with_options(
        self,
        request: amqp_20190901_models.GetVhostErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetVhostErrorByTaskIdResponse:
        """
        @summary 获取Vhost错误
        
        @param request: GetVhostErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVhostErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVhostErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetVhostErrorByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vhost_error_by_task_id_with_options_async(
        self,
        request: amqp_20190901_models.GetVhostErrorByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetVhostErrorByTaskIdResponse:
        """
        @summary 获取Vhost错误
        
        @param request: GetVhostErrorByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVhostErrorByTaskIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVhostErrorByTaskId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetVhostErrorByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vhost_error_by_task_id(
        self,
        request: amqp_20190901_models.GetVhostErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetVhostErrorByTaskIdResponse:
        """
        @summary 获取Vhost错误
        
        @param request: GetVhostErrorByTaskIdRequest
        @return: GetVhostErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vhost_error_by_task_id_with_options(request, runtime)

    async def get_vhost_error_by_task_id_async(
        self,
        request: amqp_20190901_models.GetVhostErrorByTaskIdRequest,
    ) -> amqp_20190901_models.GetVhostErrorByTaskIdResponse:
        """
        @summary 获取Vhost错误
        
        @param request: GetVhostErrorByTaskIdRequest
        @return: GetVhostErrorByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vhost_error_by_task_id_with_options_async(request, runtime)

    def get_vhost_rate_with_options(
        self,
        tmp_req: amqp_20190901_models.GetVhostRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetVhostRateResponse:
        """
        @summary 获取Vhost Rate
        
        @param tmp_req: GetVhostRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVhostRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetVhostRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vhost_names):
            request.vhost_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVhostRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetVhostRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vhost_rate_with_options_async(
        self,
        tmp_req: amqp_20190901_models.GetVhostRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.GetVhostRateResponse:
        """
        @summary 获取Vhost Rate
        
        @param tmp_req: GetVhostRateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVhostRateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.GetVhostRateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vhost_names):
            request.vhost_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vhost_names, 'VhostNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_names_shrink):
            query['VhostNames'] = request.vhost_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVhostRate',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.GetVhostRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vhost_rate(
        self,
        request: amqp_20190901_models.GetVhostRateRequest,
    ) -> amqp_20190901_models.GetVhostRateResponse:
        """
        @summary 获取Vhost Rate
        
        @param request: GetVhostRateRequest
        @return: GetVhostRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vhost_rate_with_options(request, runtime)

    async def get_vhost_rate_async(
        self,
        request: amqp_20190901_models.GetVhostRateRequest,
    ) -> amqp_20190901_models.GetVhostRateResponse:
        """
        @summary 获取Vhost Rate
        
        @param request: GetVhostRateRequest
        @return: GetVhostRateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vhost_rate_with_options_async(request, runtime)

    def import_definition_asynchronous_with_options(
        self,
        request: amqp_20190901_models.ImportDefinitionAsynchronousRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ImportDefinitionAsynchronousResponse:
        """
        @summary 异步导入元数据
        
        @param request: ImportDefinitionAsynchronousRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDefinitionAsynchronousResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.import_type):
            query['ImportType'] = request.import_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.oss_url):
            query['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDefinitionAsynchronous',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ImportDefinitionAsynchronousResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_definition_asynchronous_with_options_async(
        self,
        request: amqp_20190901_models.ImportDefinitionAsynchronousRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ImportDefinitionAsynchronousResponse:
        """
        @summary 异步导入元数据
        
        @param request: ImportDefinitionAsynchronousRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportDefinitionAsynchronousResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.import_type):
            query['ImportType'] = request.import_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.oss_url):
            query['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDefinitionAsynchronous',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ImportDefinitionAsynchronousResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_definition_asynchronous(
        self,
        request: amqp_20190901_models.ImportDefinitionAsynchronousRequest,
    ) -> amqp_20190901_models.ImportDefinitionAsynchronousResponse:
        """
        @summary 异步导入元数据
        
        @param request: ImportDefinitionAsynchronousRequest
        @return: ImportDefinitionAsynchronousResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_definition_asynchronous_with_options(request, runtime)

    async def import_definition_asynchronous_async(
        self,
        request: amqp_20190901_models.ImportDefinitionAsynchronousRequest,
    ) -> amqp_20190901_models.ImportDefinitionAsynchronousResponse:
        """
        @summary 异步导入元数据
        
        @param request: ImportDefinitionAsynchronousRequest
        @return: ImportDefinitionAsynchronousResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_definition_asynchronous_with_options_async(request, runtime)

    def instance_preivew_with_options(
        self,
        request: amqp_20190901_models.InstancePreivewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.InstancePreivewResponse:
        """
        @summary 获取实例列表
        
        @param request: InstancePreivewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstancePreivewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstancePreivew',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.InstancePreivewResponse(),
            self.call_api(params, req, runtime)
        )

    async def instance_preivew_with_options_async(
        self,
        request: amqp_20190901_models.InstancePreivewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.InstancePreivewResponse:
        """
        @summary 获取实例列表
        
        @param request: InstancePreivewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstancePreivewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstancePreivew',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.InstancePreivewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def instance_preivew(
        self,
        request: amqp_20190901_models.InstancePreivewRequest,
    ) -> amqp_20190901_models.InstancePreivewResponse:
        """
        @summary 获取实例列表
        
        @param request: InstancePreivewRequest
        @return: InstancePreivewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.instance_preivew_with_options(request, runtime)

    async def instance_preivew_async(
        self,
        request: amqp_20190901_models.InstancePreivewRequest,
    ) -> amqp_20190901_models.InstancePreivewResponse:
        """
        @summary 获取实例列表
        
        @param request: InstancePreivewRequest
        @return: InstancePreivewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.instance_preivew_with_options_async(request, runtime)

    def list_exchange_with_options(
        self,
        request: amqp_20190901_models.ListExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeResponse:
        """
        @summary 获取Exchange列表
        
        @param request: ListExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name_prefix):
            query['ExchangeNamePrefix'] = request.exchange_name_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_with_options_async(
        self,
        request: amqp_20190901_models.ListExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeResponse:
        """
        @summary 获取Exchange列表
        
        @param request: ListExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name_prefix):
            query['ExchangeNamePrefix'] = request.exchange_name_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchange',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange(
        self,
        request: amqp_20190901_models.ListExchangeRequest,
    ) -> amqp_20190901_models.ListExchangeResponse:
        """
        @summary 获取Exchange列表
        
        @param request: ListExchangeRequest
        @return: ListExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_with_options(request, runtime)

    async def list_exchange_async(
        self,
        request: amqp_20190901_models.ListExchangeRequest,
    ) -> amqp_20190901_models.ListExchangeResponse:
        """
        @summary 获取Exchange列表
        
        @param request: ListExchangeRequest
        @return: ListExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_exchange_with_options_async(request, runtime)

    def list_exchange_downstream_bindings_with_options(
        self,
        request: amqp_20190901_models.ListExchangeDownstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeDownstreamBindingsResponse:
        """
        @summary 获取Exchange下游列表
        
        @param request: ListExchangeDownstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeDownstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeDownstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeDownstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_downstream_bindings_with_options_async(
        self,
        request: amqp_20190901_models.ListExchangeDownstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeDownstreamBindingsResponse:
        """
        @summary 获取Exchange下游列表
        
        @param request: ListExchangeDownstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeDownstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeDownstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeDownstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange_downstream_bindings(
        self,
        request: amqp_20190901_models.ListExchangeDownstreamBindingsRequest,
    ) -> amqp_20190901_models.ListExchangeDownstreamBindingsResponse:
        """
        @summary 获取Exchange下游列表
        
        @param request: ListExchangeDownstreamBindingsRequest
        @return: ListExchangeDownstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_downstream_bindings_with_options(request, runtime)

    async def list_exchange_downstream_bindings_async(
        self,
        request: amqp_20190901_models.ListExchangeDownstreamBindingsRequest,
    ) -> amqp_20190901_models.ListExchangeDownstreamBindingsResponse:
        """
        @summary 获取Exchange下游列表
        
        @param request: ListExchangeDownstreamBindingsRequest
        @return: ListExchangeDownstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_exchange_downstream_bindings_with_options_async(request, runtime)

    def list_exchange_upstream_bindings_with_options(
        self,
        request: amqp_20190901_models.ListExchangeUpstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeUpstreamBindingsResponse:
        """
        @summary 获取Exchange上游绑定列表
        
        @param request: ListExchangeUpstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeUpstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeUpstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeUpstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_upstream_bindings_with_options_async(
        self,
        request: amqp_20190901_models.ListExchangeUpstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListExchangeUpstreamBindingsResponse:
        """
        @summary 获取Exchange上游绑定列表
        
        @param request: ListExchangeUpstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeUpstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeUpstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListExchangeUpstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange_upstream_bindings(
        self,
        request: amqp_20190901_models.ListExchangeUpstreamBindingsRequest,
    ) -> amqp_20190901_models.ListExchangeUpstreamBindingsResponse:
        """
        @summary 获取Exchange上游绑定列表
        
        @param request: ListExchangeUpstreamBindingsRequest
        @return: ListExchangeUpstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_upstream_bindings_with_options(request, runtime)

    async def list_exchange_upstream_bindings_async(
        self,
        request: amqp_20190901_models.ListExchangeUpstreamBindingsRequest,
    ) -> amqp_20190901_models.ListExchangeUpstreamBindingsResponse:
        """
        @summary 获取Exchange上游绑定列表
        
        @param request: ListExchangeUpstreamBindingsRequest
        @return: ListExchangeUpstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_exchange_upstream_bindings_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: amqp_20190901_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListInstanceResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: amqp_20190901_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListInstanceResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: amqp_20190901_models.ListInstanceRequest,
    ) -> amqp_20190901_models.ListInstanceResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: amqp_20190901_models.ListInstanceRequest,
    ) -> amqp_20190901_models.ListInstanceResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_instance_alarm_with_options(
        self,
        request: amqp_20190901_models.ListInstanceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListInstanceAlarmResponse:
        """
        @summary 获取实例告警
        
        @param request: ListInstanceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAlarm',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListInstanceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_alarm_with_options_async(
        self,
        request: amqp_20190901_models.ListInstanceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListInstanceAlarmResponse:
        """
        @summary 获取实例告警
        
        @param request: ListInstanceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAlarm',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListInstanceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_alarm(
        self,
        request: amqp_20190901_models.ListInstanceAlarmRequest,
    ) -> amqp_20190901_models.ListInstanceAlarmResponse:
        """
        @summary 获取实例告警
        
        @param request: ListInstanceAlarmRequest
        @return: ListInstanceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_alarm_with_options(request, runtime)

    async def list_instance_alarm_async(
        self,
        request: amqp_20190901_models.ListInstanceAlarmRequest,
    ) -> amqp_20190901_models.ListInstanceAlarmResponse:
        """
        @summary 获取实例告警
        
        @param request: ListInstanceAlarmRequest
        @return: ListInstanceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_alarm_with_options_async(request, runtime)

    def list_logstore_with_options(
        self,
        request: amqp_20190901_models.ListLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListLogstoreResponse:
        """
        @summary 获取日志Logstore
        
        @param request: ListLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogstore',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logstore_with_options_async(
        self,
        request: amqp_20190901_models.ListLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListLogstoreResponse:
        """
        @summary 获取日志Logstore
        
        @param request: ListLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogstore',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logstore(
        self,
        request: amqp_20190901_models.ListLogstoreRequest,
    ) -> amqp_20190901_models.ListLogstoreResponse:
        """
        @summary 获取日志Logstore
        
        @param request: ListLogstoreRequest
        @return: ListLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_logstore_with_options(request, runtime)

    async def list_logstore_async(
        self,
        request: amqp_20190901_models.ListLogstoreRequest,
    ) -> amqp_20190901_models.ListLogstoreResponse:
        """
        @summary 获取日志Logstore
        
        @param request: ListLogstoreRequest
        @return: ListLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_logstore_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: amqp_20190901_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListProjectResponse:
        """
        @summary 获取日志Project
        
        @param request: ListProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: amqp_20190901_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListProjectResponse:
        """
        @summary 获取日志Project
        
        @param request: ListProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: amqp_20190901_models.ListProjectRequest,
    ) -> amqp_20190901_models.ListProjectResponse:
        """
        @summary 获取日志Project
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: amqp_20190901_models.ListProjectRequest,
    ) -> amqp_20190901_models.ListProjectResponse:
        """
        @summary 获取日志Project
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def list_queue_with_options(
        self,
        request: amqp_20190901_models.ListQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListQueueResponse:
        """
        @summary 获取队列列表
        
        @param request: ListQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name_prefix):
            query['QueueNamePrefix'] = request.queue_name_prefix
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_with_options_async(
        self,
        request: amqp_20190901_models.ListQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListQueueResponse:
        """
        @summary 获取队列列表
        
        @param request: ListQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name_prefix):
            query['QueueNamePrefix'] = request.queue_name_prefix
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue(
        self,
        request: amqp_20190901_models.ListQueueRequest,
    ) -> amqp_20190901_models.ListQueueResponse:
        """
        @summary 获取队列列表
        
        @param request: ListQueueRequest
        @return: ListQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_with_options(request, runtime)

    async def list_queue_async(
        self,
        request: amqp_20190901_models.ListQueueRequest,
    ) -> amqp_20190901_models.ListQueueResponse:
        """
        @summary 获取队列列表
        
        @param request: ListQueueRequest
        @return: ListQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_with_options_async(request, runtime)

    def list_queue_upstream_bindings_with_options(
        self,
        request: amqp_20190901_models.ListQueueUpstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListQueueUpstreamBindingsResponse:
        """
        @summary 获取队列上游绑定列表
        
        @param request: ListQueueUpstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueUpstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueUpstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListQueueUpstreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_upstream_bindings_with_options_async(
        self,
        request: amqp_20190901_models.ListQueueUpstreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListQueueUpstreamBindingsResponse:
        """
        @summary 获取队列上游绑定列表
        
        @param request: ListQueueUpstreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueUpstreamBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueUpstreamBindings',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListQueueUpstreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue_upstream_bindings(
        self,
        request: amqp_20190901_models.ListQueueUpstreamBindingsRequest,
    ) -> amqp_20190901_models.ListQueueUpstreamBindingsResponse:
        """
        @summary 获取队列上游绑定列表
        
        @param request: ListQueueUpstreamBindingsRequest
        @return: ListQueueUpstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_upstream_bindings_with_options(request, runtime)

    async def list_queue_upstream_bindings_async(
        self,
        request: amqp_20190901_models.ListQueueUpstreamBindingsRequest,
    ) -> amqp_20190901_models.ListQueueUpstreamBindingsResponse:
        """
        @summary 获取队列上游绑定列表
        
        @param request: ListQueueUpstreamBindingsRequest
        @return: ListQueueUpstreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_upstream_bindings_with_options_async(request, runtime)

    def list_static_accounts_with_options(
        self,
        request: amqp_20190901_models.ListStaticAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListStaticAccountsResponse:
        """
        @summary 获取静态账户列表
        
        @param request: ListStaticAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStaticAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStaticAccounts',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListStaticAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_static_accounts_with_options_async(
        self,
        request: amqp_20190901_models.ListStaticAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListStaticAccountsResponse:
        """
        @summary 获取静态账户列表
        
        @param request: ListStaticAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStaticAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStaticAccounts',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListStaticAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_static_accounts(
        self,
        request: amqp_20190901_models.ListStaticAccountsRequest,
    ) -> amqp_20190901_models.ListStaticAccountsResponse:
        """
        @summary 获取静态账户列表
        
        @param request: ListStaticAccountsRequest
        @return: ListStaticAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_static_accounts_with_options(request, runtime)

    async def list_static_accounts_async(
        self,
        request: amqp_20190901_models.ListStaticAccountsRequest,
    ) -> amqp_20190901_models.ListStaticAccountsResponse:
        """
        @summary 获取静态账户列表
        
        @param request: ListStaticAccountsRequest
        @return: ListStaticAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_static_accounts_with_options_async(request, runtime)

    def list_vhost_with_options(
        self,
        request: amqp_20190901_models.ListVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListVhostResponse:
        """
        @summary 获取Vhost列表
        
        @param request: ListVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name_prefix):
            query['VhostNamePrefix'] = request.vhost_name_prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vhost_with_options_async(
        self,
        request: amqp_20190901_models.ListVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ListVhostResponse:
        """
        @summary 获取Vhost列表
        
        @param request: ListVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVhostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.vhost_name_prefix):
            query['VhostNamePrefix'] = request.vhost_name_prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVhost',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ListVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vhost(
        self,
        request: amqp_20190901_models.ListVhostRequest,
    ) -> amqp_20190901_models.ListVhostResponse:
        """
        @summary 获取Vhost列表
        
        @param request: ListVhostRequest
        @return: ListVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vhost_with_options(request, runtime)

    async def list_vhost_async(
        self,
        request: amqp_20190901_models.ListVhostRequest,
    ) -> amqp_20190901_models.ListVhostResponse:
        """
        @summary 获取Vhost列表
        
        @param request: ListVhostRequest
        @return: ListVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vhost_with_options_async(request, runtime)

    def metadata_with_options(
        self,
        request: amqp_20190901_models.MetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.MetadataResponse:
        """
        @summary 获取元数据
        
        @param request: MetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Metadata',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.MetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def metadata_with_options_async(
        self,
        request: amqp_20190901_models.MetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.MetadataResponse:
        """
        @summary 获取元数据
        
        @param request: MetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Metadata',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.MetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def metadata(
        self,
        request: amqp_20190901_models.MetadataRequest,
    ) -> amqp_20190901_models.MetadataResponse:
        """
        @summary 获取元数据
        
        @param request: MetadataRequest
        @return: MetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.metadata_with_options(request, runtime)

    async def metadata_async(
        self,
        request: amqp_20190901_models.MetadataRequest,
    ) -> amqp_20190901_models.MetadataResponse:
        """
        @summary 获取元数据
        
        @param request: MetadataRequest
        @return: MetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.metadata_with_options_async(request, runtime)

    def purge_queue_with_options(
        self,
        tmp_req: amqp_20190901_models.PurgeQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.PurgeQueueResponse:
        """
        @summary 清空队列
        
        @param tmp_req: PurgeQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PurgeQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.PurgeQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.PurgeQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_queue_with_options_async(
        self,
        tmp_req: amqp_20190901_models.PurgeQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.PurgeQueueResponse:
        """
        @summary 清空队列
        
        @param tmp_req: PurgeQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PurgeQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = amqp_20190901_models.PurgeQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.collina):
            query['Collina'] = request.collina
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.umid_token):
            query['UmidToken'] = request.umid_token
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeQueue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.PurgeQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_queue(
        self,
        request: amqp_20190901_models.PurgeQueueRequest,
    ) -> amqp_20190901_models.PurgeQueueResponse:
        """
        @summary 清空队列
        
        @param request: PurgeQueueRequest
        @return: PurgeQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.purge_queue_with_options(request, runtime)

    async def purge_queue_async(
        self,
        request: amqp_20190901_models.PurgeQueueRequest,
    ) -> amqp_20190901_models.PurgeQueueResponse:
        """
        @summary 清空队列
        
        @param request: PurgeQueueRequest
        @return: PurgeQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.purge_queue_with_options_async(request, runtime)

    def query_message_by_message_id_with_options(
        self,
        request: amqp_20190901_models.QueryMessageByMessageIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.QueryMessageByMessageIdResponse:
        """
        @summary 根据Message Id查询消息
        
        @param request: QueryMessageByMessageIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageByMessageIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageByMessageId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.QueryMessageByMessageIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_by_message_id_with_options_async(
        self,
        request: amqp_20190901_models.QueryMessageByMessageIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.QueryMessageByMessageIdResponse:
        """
        @summary 根据Message Id查询消息
        
        @param request: QueryMessageByMessageIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageByMessageIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageByMessageId',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.QueryMessageByMessageIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_by_message_id(
        self,
        request: amqp_20190901_models.QueryMessageByMessageIdRequest,
    ) -> amqp_20190901_models.QueryMessageByMessageIdResponse:
        """
        @summary 根据Message Id查询消息
        
        @param request: QueryMessageByMessageIdRequest
        @return: QueryMessageByMessageIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_message_by_message_id_with_options(request, runtime)

    async def query_message_by_message_id_async(
        self,
        request: amqp_20190901_models.QueryMessageByMessageIdRequest,
    ) -> amqp_20190901_models.QueryMessageByMessageIdResponse:
        """
        @summary 根据Message Id查询消息
        
        @param request: QueryMessageByMessageIdRequest
        @return: QueryMessageByMessageIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_message_by_message_id_with_options_async(request, runtime)

    def query_message_by_queue_name_with_options(
        self,
        request: amqp_20190901_models.QueryMessageByQueueNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.QueryMessageByQueueNameResponse:
        """
        @summary 根据队列查询消息
        
        @param request: QueryMessageByQueueNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageByQueueNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageByQueueName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.QueryMessageByQueueNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_by_queue_name_with_options_async(
        self,
        request: amqp_20190901_models.QueryMessageByQueueNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.QueryMessageByQueueNameResponse:
        """
        @summary 根据队列查询消息
        
        @param request: QueryMessageByQueueNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageByQueueNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageByQueueName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.QueryMessageByQueueNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_by_queue_name(
        self,
        request: amqp_20190901_models.QueryMessageByQueueNameRequest,
    ) -> amqp_20190901_models.QueryMessageByQueueNameResponse:
        """
        @summary 根据队列查询消息
        
        @param request: QueryMessageByQueueNameRequest
        @return: QueryMessageByQueueNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_message_by_queue_name_with_options(request, runtime)

    async def query_message_by_queue_name_async(
        self,
        request: amqp_20190901_models.QueryMessageByQueueNameRequest,
    ) -> amqp_20190901_models.QueryMessageByQueueNameResponse:
        """
        @summary 根据队列查询消息
        
        @param request: QueryMessageByQueueNameRequest
        @return: QueryMessageByQueueNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_message_by_queue_name_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: amqp_20190901_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ReleaseInstanceResponse:
        """
        @summary 实例释放
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: amqp_20190901_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.ReleaseInstanceResponse:
        """
        @summary 实例释放
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: amqp_20190901_models.ReleaseInstanceRequest,
    ) -> amqp_20190901_models.ReleaseInstanceResponse:
        """
        @summary 实例释放
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: amqp_20190901_models.ReleaseInstanceRequest,
    ) -> amqp_20190901_models.ReleaseInstanceResponse:
        """
        @summary 实例释放
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: amqp_20190901_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.SendMessageResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.props):
            query['Props'] = request.props
        if not UtilClient.is_unset(request.routing_key):
            query['RoutingKey'] = request.routing_key
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: amqp_20190901_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.SendMessageResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.exchange_name):
            query['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.props):
            query['Props'] = request.props
        if not UtilClient.is_unset(request.routing_key):
            query['RoutingKey'] = request.routing_key
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: amqp_20190901_models.SendMessageRequest,
    ) -> amqp_20190901_models.SendMessageResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageRequest
        @return: SendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: amqp_20190901_models.SendMessageRequest,
    ) -> amqp_20190901_models.SendMessageResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageRequest
        @return: SendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def send_message_copy_with_options(
        self,
        request: amqp_20190901_models.SendMessageCopyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.SendMessageCopyResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageCopyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageCopyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_token):
            query['ProcessToken'] = request.process_token
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessageCopy',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.SendMessageCopyResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_copy_with_options_async(
        self,
        request: amqp_20190901_models.SendMessageCopyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.SendMessageCopyResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageCopyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendMessageCopyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_token):
            query['ProcessToken'] = request.process_token
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessageCopy',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.SendMessageCopyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message_copy(
        self,
        request: amqp_20190901_models.SendMessageCopyRequest,
    ) -> amqp_20190901_models.SendMessageCopyResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageCopyRequest
        @return: SendMessageCopyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_message_copy_with_options(request, runtime)

    async def send_message_copy_async(
        self,
        request: amqp_20190901_models.SendMessageCopyRequest,
    ) -> amqp_20190901_models.SendMessageCopyResponse:
        """
        @summary 发送消息
        
        @param request: SendMessageCopyRequest
        @return: SendMessageCopyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_message_copy_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: amqp_20190901_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UnbindResponse:
        """
        @summary 取消绑定
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dst_name):
            query['DstName'] = request.dst_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_name):
            query['SrcName'] = request.src_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Unbind',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UnbindResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: amqp_20190901_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UnbindResponse:
        """
        @summary 取消绑定
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_key):
            query['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            query['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.dst_name):
            query['DstName'] = request.dst_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_name):
            query['SrcName'] = request.src_name
        if not UtilClient.is_unset(request.vhost_name):
            query['VhostName'] = request.vhost_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Unbind',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UnbindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind(
        self,
        request: amqp_20190901_models.UnbindRequest,
    ) -> amqp_20190901_models.UnbindResponse:
        """
        @summary 取消绑定
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: amqp_20190901_models.UnbindRequest,
    ) -> amqp_20190901_models.UnbindResponse:
        """
        @summary 取消绑定
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: amqp_20190901_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: amqp_20190901_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: amqp_20190901_models.UpdateInstanceRequest,
    ) -> amqp_20190901_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: amqp_20190901_models.UpdateInstanceRequest,
    ) -> amqp_20190901_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_instance_retry_strategy_with_options(
        self,
        request: amqp_20190901_models.UpdateInstanceRetryStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateInstanceRetryStrategyResponse:
        """
        @summary 修改实例的重试策略
        
        @param request: UpdateInstanceRetryStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceRetryStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_times):
            query['RetryTimes'] = request.retry_times
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceRetryStrategy',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateInstanceRetryStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_retry_strategy_with_options_async(
        self,
        request: amqp_20190901_models.UpdateInstanceRetryStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateInstanceRetryStrategyResponse:
        """
        @summary 修改实例的重试策略
        
        @param request: UpdateInstanceRetryStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceRetryStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.retry_times):
            query['RetryTimes'] = request.retry_times
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceRetryStrategy',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateInstanceRetryStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_retry_strategy(
        self,
        request: amqp_20190901_models.UpdateInstanceRetryStrategyRequest,
    ) -> amqp_20190901_models.UpdateInstanceRetryStrategyResponse:
        """
        @summary 修改实例的重试策略
        
        @param request: UpdateInstanceRetryStrategyRequest
        @return: UpdateInstanceRetryStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_retry_strategy_with_options(request, runtime)

    async def update_instance_retry_strategy_async(
        self,
        request: amqp_20190901_models.UpdateInstanceRetryStrategyRequest,
    ) -> amqp_20190901_models.UpdateInstanceRetryStrategyResponse:
        """
        @summary 修改实例的重试策略
        
        @param request: UpdateInstanceRetryStrategyRequest
        @return: UpdateInstanceRetryStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_retry_strategy_with_options_async(request, runtime)

    def update_serverless_switch_with_options(
        self,
        request: amqp_20190901_models.UpdateServerlessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateServerlessSwitchResponse:
        """
        @summary 更新serverless开关
        
        @param request: UpdateServerlessSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerlessSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.serverless_switch):
            query['ServerlessSwitch'] = request.serverless_switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerlessSwitch',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateServerlessSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_serverless_switch_with_options_async(
        self,
        request: amqp_20190901_models.UpdateServerlessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpdateServerlessSwitchResponse:
        """
        @summary 更新serverless开关
        
        @param request: UpdateServerlessSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerlessSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.serverless_switch):
            query['ServerlessSwitch'] = request.serverless_switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerlessSwitch',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpdateServerlessSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_serverless_switch(
        self,
        request: amqp_20190901_models.UpdateServerlessSwitchRequest,
    ) -> amqp_20190901_models.UpdateServerlessSwitchResponse:
        """
        @summary 更新serverless开关
        
        @param request: UpdateServerlessSwitchRequest
        @return: UpdateServerlessSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_serverless_switch_with_options(request, runtime)

    async def update_serverless_switch_async(
        self,
        request: amqp_20190901_models.UpdateServerlessSwitchRequest,
    ) -> amqp_20190901_models.UpdateServerlessSwitchResponse:
        """
        @summary 更新serverless开关
        
        @param request: UpdateServerlessSwitchRequest
        @return: UpdateServerlessSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_serverless_switch_with_options_async(request, runtime)

    def upgrade_limits_with_options(
        self,
        request: amqp_20190901_models.UpgradeLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpgradeLimitsResponse:
        """
        @summary 升级实例配额
        
        @param request: UpgradeLimitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLimitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLimits',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpgradeLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_limits_with_options_async(
        self,
        request: amqp_20190901_models.UpgradeLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_20190901_models.UpgradeLimitsResponse:
        """
        @summary 升级实例配额
        
        @param request: UpgradeLimitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeLimitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_session_id):
            query['ConsoleSessionId'] = request.console_session_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLimits',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_20190901_models.UpgradeLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_limits(
        self,
        request: amqp_20190901_models.UpgradeLimitsRequest,
    ) -> amqp_20190901_models.UpgradeLimitsResponse:
        """
        @summary 升级实例配额
        
        @param request: UpgradeLimitsRequest
        @return: UpgradeLimitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_limits_with_options(request, runtime)

    async def upgrade_limits_async(
        self,
        request: amqp_20190901_models.UpgradeLimitsRequest,
    ) -> amqp_20190901_models.UpgradeLimitsResponse:
        """
        @summary 升级实例配额
        
        @param request: UpgradeLimitsRequest
        @return: UpgradeLimitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_limits_with_options_async(request, runtime)
