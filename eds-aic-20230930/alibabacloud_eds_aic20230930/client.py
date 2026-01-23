# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eds_aic20230930 import models as main_models
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
        self._endpoint = self.get_endpoint('eds-aic', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_key_pair_with_options(
        self,
        request: main_models.AttachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_key_pair_with_options_async(
        self,
        request: main_models.AttachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_key_pair(
        self,
        request: main_models.AttachKeyPairRequest,
    ) -> main_models.AttachKeyPairResponse:
        runtime = RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    async def attach_key_pair_async(
        self,
        request: main_models.AttachKeyPairRequest,
    ) -> main_models.AttachKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.attach_key_pair_with_options_async(request, runtime)

    def authorize_android_instance_with_options(
        self,
        request: main_models.AuthorizeAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.authorize_user_id):
            query['AuthorizeUserId'] = request.authorize_user_id
        if not DaraCore.is_null(request.un_authorize_user_id):
            query['UnAuthorizeUserId'] = request.un_authorize_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_android_instance_with_options_async(
        self,
        request: main_models.AuthorizeAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.authorize_user_id):
            query['AuthorizeUserId'] = request.authorize_user_id
        if not DaraCore.is_null(request.un_authorize_user_id):
            query['UnAuthorizeUserId'] = request.un_authorize_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_android_instance(
        self,
        request: main_models.AuthorizeAndroidInstanceRequest,
    ) -> main_models.AuthorizeAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.authorize_android_instance_with_options(request, runtime)

    async def authorize_android_instance_async(
        self,
        request: main_models.AuthorizeAndroidInstanceRequest,
    ) -> main_models.AuthorizeAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.authorize_android_instance_with_options_async(request, runtime)

    def backup_android_instance_with_options(
        self,
        request: main_models.BackupAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def backup_android_instance_with_options_async(
        self,
        request: main_models.BackupAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backup_android_instance(
        self,
        request: main_models.BackupAndroidInstanceRequest,
    ) -> main_models.BackupAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.backup_android_instance_with_options(request, runtime)

    async def backup_android_instance_async(
        self,
        request: main_models.BackupAndroidInstanceRequest,
    ) -> main_models.BackupAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.backup_android_instance_with_options_async(request, runtime)

    def backup_app_with_options(
        self,
        request: main_models.BackupAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def backup_app_with_options_async(
        self,
        request: main_models.BackupAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backup_app(
        self,
        request: main_models.BackupAppRequest,
    ) -> main_models.BackupAppResponse:
        runtime = RuntimeOptions()
        return self.backup_app_with_options(request, runtime)

    async def backup_app_async(
        self,
        request: main_models.BackupAppRequest,
    ) -> main_models.BackupAppResponse:
        runtime = RuntimeOptions()
        return await self.backup_app_with_options_async(request, runtime)

    def backup_file_with_options(
        self,
        request: main_models.BackupFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_source_file_path_list):
            query['ExcludeSourceFilePathList'] = request.exclude_source_file_path_list
        if not DaraCore.is_null(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not DaraCore.is_null(request.source_file_path_list):
            query['SourceFilePathList'] = request.source_file_path_list
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def backup_file_with_options_async(
        self,
        request: main_models.BackupFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BackupFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.exclude_source_file_path_list):
            query['ExcludeSourceFilePathList'] = request.exclude_source_file_path_list
        if not DaraCore.is_null(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not DaraCore.is_null(request.source_file_path_list):
            query['SourceFilePathList'] = request.source_file_path_list
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BackupFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backup_file(
        self,
        request: main_models.BackupFileRequest,
    ) -> main_models.BackupFileResponse:
        runtime = RuntimeOptions()
        return self.backup_file_with_options(request, runtime)

    async def backup_file_async(
        self,
        request: main_models.BackupFileRequest,
    ) -> main_models.BackupFileResponse:
        runtime = RuntimeOptions()
        return await self.backup_file_with_options_async(request, runtime)

    def batch_get_acp_connection_ticket_with_options(
        self,
        request: main_models.BatchGetAcpConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetAcpConnectionTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_tasks):
            query['InstanceTasks'] = request.instance_tasks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetAcpConnectionTicket',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetAcpConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_acp_connection_ticket_with_options_async(
        self,
        request: main_models.BatchGetAcpConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetAcpConnectionTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_tasks):
            query['InstanceTasks'] = request.instance_tasks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetAcpConnectionTicket',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetAcpConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_acp_connection_ticket(
        self,
        request: main_models.BatchGetAcpConnectionTicketRequest,
    ) -> main_models.BatchGetAcpConnectionTicketResponse:
        runtime = RuntimeOptions()
        return self.batch_get_acp_connection_ticket_with_options(request, runtime)

    async def batch_get_acp_connection_ticket_async(
        self,
        request: main_models.BatchGetAcpConnectionTicketRequest,
    ) -> main_models.BatchGetAcpConnectionTicketResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_acp_connection_ticket_with_options_async(request, runtime)

    def change_cloud_phone_node_with_options(
        self,
        request: main_models.ChangeCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeCloudPhoneNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.display_config):
            query['DisplayConfig'] = request.display_config
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        if not DaraCore.is_null(request.swap_size):
            query['SwapSize'] = request.swap_size
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cloud_phone_node_with_options_async(
        self,
        request: main_models.ChangeCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeCloudPhoneNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.display_config):
            query['DisplayConfig'] = request.display_config
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        if not DaraCore.is_null(request.swap_size):
            query['SwapSize'] = request.swap_size
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cloud_phone_node(
        self,
        request: main_models.ChangeCloudPhoneNodeRequest,
    ) -> main_models.ChangeCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return self.change_cloud_phone_node_with_options(request, runtime)

    async def change_cloud_phone_node_async(
        self,
        request: main_models.ChangeCloudPhoneNodeRequest,
    ) -> main_models.ChangeCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return await self.change_cloud_phone_node_with_options_async(request, runtime)

    def check_resource_stock_with_options(
        self,
        request: main_models.CheckResourceStockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourceStockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acp_spec_id):
            query['AcpSpecId'] = request.acp_spec_id
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourceStock',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourceStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_stock_with_options_async(
        self,
        request: main_models.CheckResourceStockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourceStockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acp_spec_id):
            query['AcpSpecId'] = request.acp_spec_id
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourceStock',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourceStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_stock(
        self,
        request: main_models.CheckResourceStockRequest,
    ) -> main_models.CheckResourceStockResponse:
        runtime = RuntimeOptions()
        return self.check_resource_stock_with_options(request, runtime)

    async def check_resource_stock_async(
        self,
        request: main_models.CheckResourceStockRequest,
    ) -> main_models.CheckResourceStockResponse:
        runtime = RuntimeOptions()
        return await self.check_resource_stock_with_options_async(request, runtime)

    def create_android_instance_group_with_options(
        self,
        tmp_req: main_models.CreateAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndroidInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateAndroidInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_info):
            request.network_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_info, 'NetworkInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_package_type):
            query['BandwidthPackageType'] = request.bandwidth_package_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not DaraCore.is_null(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
        if not DaraCore.is_null(request.ipv_6bandwidth):
            query['Ipv6Bandwidth'] = request.ipv_6bandwidth
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.network_info_shrink):
            query['NetworkInfo'] = request.network_info_shrink
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.number_of_instances):
            query['NumberOfInstances'] = request.number_of_instances
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_android_instance_group_with_options_async(
        self,
        tmp_req: main_models.CreateAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndroidInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateAndroidInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_info):
            request.network_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_info, 'NetworkInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_package_type):
            query['BandwidthPackageType'] = request.bandwidth_package_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not DaraCore.is_null(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
        if not DaraCore.is_null(request.ipv_6bandwidth):
            query['Ipv6Bandwidth'] = request.ipv_6bandwidth
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.network_info_shrink):
            query['NetworkInfo'] = request.network_info_shrink
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.number_of_instances):
            query['NumberOfInstances'] = request.number_of_instances
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_android_instance_group(
        self,
        request: main_models.CreateAndroidInstanceGroupRequest,
    ) -> main_models.CreateAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_android_instance_group_with_options(request, runtime)

    async def create_android_instance_group_async(
        self,
        request: main_models.CreateAndroidInstanceGroupRequest,
    ) -> main_models.CreateAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_android_instance_group_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        tmp_req: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        tmp_req.validate()
        request = main_models.CreateAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_app_info):
            request.custom_app_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_app_info, 'CustomAppInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.custom_app_info_shrink):
            query['CustomAppInfo'] = request.custom_app_info_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not DaraCore.is_null(request.install_param):
            query['InstallParam'] = request.install_param
        if not DaraCore.is_null(request.oss_app_url):
            query['OssAppUrl'] = request.oss_app_url
        if not DaraCore.is_null(request.sign_apk):
            query['SignApk'] = request.sign_apk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        tmp_req: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        tmp_req.validate()
        request = main_models.CreateAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_app_info):
            request.custom_app_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_app_info, 'CustomAppInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.custom_app_info_shrink):
            query['CustomAppInfo'] = request.custom_app_info_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not DaraCore.is_null(request.install_param):
            query['InstallParam'] = request.install_param
        if not DaraCore.is_null(request.oss_app_url):
            query['OssAppUrl'] = request.oss_app_url
        if not DaraCore.is_null(request.sign_apk):
            query['SignApk'] = request.sign_apk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_cloud_phone_node_with_options(
        self,
        tmp_req: main_models.CreateCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudPhoneNodeResponse:
        tmp_req.validate()
        request = main_models.CreateCloudPhoneNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_config):
            request.display_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        if not DaraCore.is_null(tmp_req.network_info):
            request.network_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_info, 'NetworkInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_package_type):
            query['BandwidthPackageType'] = request.bandwidth_package_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_single_img_disk):
            query['IsSingleImgDisk'] = request.is_single_img_disk
        if not DaraCore.is_null(request.network_id):
            query['NetworkId'] = request.network_id
        if not DaraCore.is_null(request.network_info_shrink):
            query['NetworkInfo'] = request.network_info_shrink
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.resolution_height):
            query['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            query['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.server_share_data_volume):
            query['ServerShareDataVolume'] = request.server_share_data_volume
        if not DaraCore.is_null(request.server_type):
            query['ServerType'] = request.server_type
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        if not DaraCore.is_null(request.swap_size):
            query['SwapSize'] = request.swap_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        if not DaraCore.is_null(request.use_template):
            query['UseTemplate'] = request.use_template
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        body = {}
        if not DaraCore.is_null(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_phone_node_with_options_async(
        self,
        tmp_req: main_models.CreateCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudPhoneNodeResponse:
        tmp_req.validate()
        request = main_models.CreateCloudPhoneNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_config):
            request.display_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        if not DaraCore.is_null(tmp_req.network_info):
            request.network_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_info, 'NetworkInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_package_type):
            query['BandwidthPackageType'] = request.bandwidth_package_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_single_img_disk):
            query['IsSingleImgDisk'] = request.is_single_img_disk
        if not DaraCore.is_null(request.network_id):
            query['NetworkId'] = request.network_id
        if not DaraCore.is_null(request.network_info_shrink):
            query['NetworkInfo'] = request.network_info_shrink
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.resolution_height):
            query['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            query['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.server_share_data_volume):
            query['ServerShareDataVolume'] = request.server_share_data_volume
        if not DaraCore.is_null(request.server_type):
            query['ServerType'] = request.server_type
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        if not DaraCore.is_null(request.swap_size):
            query['SwapSize'] = request.swap_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        if not DaraCore.is_null(request.use_template):
            query['UseTemplate'] = request.use_template
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        body = {}
        if not DaraCore.is_null(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_phone_node(
        self,
        request: main_models.CreateCloudPhoneNodeRequest,
    ) -> main_models.CreateCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_phone_node_with_options(request, runtime)

    async def create_cloud_phone_node_async(
        self,
        request: main_models.CreateCloudPhoneNodeRequest,
    ) -> main_models.CreateCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_phone_node_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: main_models.CreateCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: main_models.CreateCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_image(
        self,
        request: main_models.CreateCustomImageRequest,
    ) -> main_models.CreateCustomImageResponse:
        runtime = RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    async def create_custom_image_async(
        self,
        request: main_models.CreateCustomImageRequest,
    ) -> main_models.CreateCustomImageResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_image_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: main_models.CreateKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: main_models.CreateKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_pair(
        self,
        request: main_models.CreateKeyPairRequest,
    ) -> main_models.CreateKeyPairResponse:
        runtime = RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: main_models.CreateKeyPairRequest,
    ) -> main_models.CreateKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_policy_group_with_options(
        self,
        tmp_req: main_models.CreatePolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyGroupResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not DaraCore.is_null(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not DaraCore.is_null(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not DaraCore.is_null(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not DaraCore.is_null(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not DaraCore.is_null(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not DaraCore.is_null(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_group_with_options_async(
        self,
        tmp_req: main_models.CreatePolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyGroupResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not DaraCore.is_null(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not DaraCore.is_null(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not DaraCore.is_null(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not DaraCore.is_null(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not DaraCore.is_null(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not DaraCore.is_null(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_group(
        self,
        request: main_models.CreatePolicyGroupRequest,
    ) -> main_models.CreatePolicyGroupResponse:
        runtime = RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    async def create_policy_group_async(
        self,
        request: main_models.CreatePolicyGroupRequest,
    ) -> main_models.CreatePolicyGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def create_screenshot_with_options(
        self,
        request: main_models.CreateScreenshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScreenshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.screenshot_id):
            query['ScreenshotId'] = request.screenshot_id
        if not DaraCore.is_null(request.skip_check_policy_config):
            query['SkipCheckPolicyConfig'] = request.skip_check_policy_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScreenshot',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScreenshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_screenshot_with_options_async(
        self,
        request: main_models.CreateScreenshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScreenshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.screenshot_id):
            query['ScreenshotId'] = request.screenshot_id
        if not DaraCore.is_null(request.skip_check_policy_config):
            query['SkipCheckPolicyConfig'] = request.skip_check_policy_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScreenshot',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScreenshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_screenshot(
        self,
        request: main_models.CreateScreenshotRequest,
    ) -> main_models.CreateScreenshotResponse:
        runtime = RuntimeOptions()
        return self.create_screenshot_with_options(request, runtime)

    async def create_screenshot_async(
        self,
        request: main_models.CreateScreenshotRequest,
    ) -> main_models.CreateScreenshotResponse:
        runtime = RuntimeOptions()
        return await self.create_screenshot_with_options_async(request, runtime)

    def create_system_property_template_with_options(
        self,
        tmp_req: main_models.CreateSystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSystemPropertyTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateSystemPropertyTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.system_property_info):
            request.system_property_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_property_info, 'SystemPropertyInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_auto):
            query['EnableAuto'] = request.enable_auto
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.system_property_info_shrink):
            query['SystemPropertyInfo'] = request.system_property_info_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSystemPropertyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_system_property_template_with_options_async(
        self,
        tmp_req: main_models.CreateSystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSystemPropertyTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateSystemPropertyTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.system_property_info):
            request.system_property_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_property_info, 'SystemPropertyInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_auto):
            query['EnableAuto'] = request.enable_auto
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.system_property_info_shrink):
            query['SystemPropertyInfo'] = request.system_property_info_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSystemPropertyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_system_property_template(
        self,
        request: main_models.CreateSystemPropertyTemplateRequest,
    ) -> main_models.CreateSystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_system_property_template_with_options(request, runtime)

    async def create_system_property_template_async(
        self,
        request: main_models.CreateSystemPropertyTemplateRequest,
    ) -> main_models.CreateSystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_system_property_template_with_options_async(request, runtime)

    def delete_android_instance_group_with_options(
        self,
        request: main_models.DeleteAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_android_instance_group_with_options_async(
        self,
        request: main_models.DeleteAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_android_instance_group(
        self,
        request: main_models.DeleteAndroidInstanceGroupRequest,
    ) -> main_models.DeleteAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_android_instance_group_with_options(request, runtime)

    async def delete_android_instance_group_async(
        self,
        request: main_models.DeleteAndroidInstanceGroupRequest,
    ) -> main_models.DeleteAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_android_instance_group_with_options_async(request, runtime)

    def delete_apps_with_options(
        self,
        request: main_models.DeleteAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApps',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apps_with_options_async(
        self,
        request: main_models.DeleteAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApps',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apps(
        self,
        request: main_models.DeleteAppsRequest,
    ) -> main_models.DeleteAppsResponse:
        runtime = RuntimeOptions()
        return self.delete_apps_with_options(request, runtime)

    async def delete_apps_async(
        self,
        request: main_models.DeleteAppsRequest,
    ) -> main_models.DeleteAppsResponse:
        runtime = RuntimeOptions()
        return await self.delete_apps_with_options_async(request, runtime)

    def delete_backup_file_with_options(
        self,
        request: main_models.DeleteBackupFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_file_id_list):
            query['BackupFileIdList'] = request.backup_file_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_file_with_options_async(
        self,
        request: main_models.DeleteBackupFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_file_id_list):
            query['BackupFileIdList'] = request.backup_file_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_file(
        self,
        request: main_models.DeleteBackupFileRequest,
    ) -> main_models.DeleteBackupFileResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    async def delete_backup_file_async(
        self,
        request: main_models.DeleteBackupFileRequest,
    ) -> main_models.DeleteBackupFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_file_with_options_async(request, runtime)

    def delete_cloud_phone_nodes_with_options(
        self,
        request: main_models.DeleteCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudPhoneNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_phone_nodes_with_options_async(
        self,
        request: main_models.DeleteCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudPhoneNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_phone_nodes(
        self,
        request: main_models.DeleteCloudPhoneNodesRequest,
    ) -> main_models.DeleteCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_phone_nodes_with_options(request, runtime)

    async def delete_cloud_phone_nodes_async(
        self,
        request: main_models.DeleteCloudPhoneNodesRequest,
    ) -> main_models.DeleteCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_phone_nodes_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        tmp_req: main_models.DeleteImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImagesResponse:
        tmp_req.validate()
        request = main_models.DeleteImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_ids):
            request.image_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        body = {}
        if not DaraCore.is_null(request.image_ids_shrink):
            body['ImageIds'] = request.image_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImages',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_with_options_async(
        self,
        tmp_req: main_models.DeleteImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImagesResponse:
        tmp_req.validate()
        request = main_models.DeleteImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_ids):
            request.image_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        body = {}
        if not DaraCore.is_null(request.image_ids_shrink):
            body['ImageIds'] = request.image_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImages',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images(
        self,
        request: main_models.DeleteImagesRequest,
    ) -> main_models.DeleteImagesResponse:
        runtime = RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: main_models.DeleteImagesRequest,
    ) -> main_models.DeleteImagesResponse:
        runtime = RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: main_models.DeleteKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyPairs',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: main_models.DeleteKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyPairs',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: main_models.DeleteKeyPairsRequest,
    ) -> main_models.DeleteKeyPairsResponse:
        runtime = RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: main_models.DeleteKeyPairsRequest,
    ) -> main_models.DeleteKeyPairsResponse:
        runtime = RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_policy_group_with_options(
        self,
        request: main_models.DeletePolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_group_with_options_async(
        self,
        request: main_models.DeletePolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_group(
        self,
        request: main_models.DeletePolicyGroupRequest,
    ) -> main_models.DeletePolicyGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_group_with_options(request, runtime)

    async def delete_policy_group_async(
        self,
        request: main_models.DeletePolicyGroupRequest,
    ) -> main_models.DeletePolicyGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_group_with_options_async(request, runtime)

    def delete_system_property_templates_with_options(
        self,
        request: main_models.DeleteSystemPropertyTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSystemPropertyTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSystemPropertyTemplates',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSystemPropertyTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_system_property_templates_with_options_async(
        self,
        request: main_models.DeleteSystemPropertyTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSystemPropertyTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSystemPropertyTemplates',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSystemPropertyTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_system_property_templates(
        self,
        request: main_models.DeleteSystemPropertyTemplatesRequest,
    ) -> main_models.DeleteSystemPropertyTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_system_property_templates_with_options(request, runtime)

    async def delete_system_property_templates_async(
        self,
        request: main_models.DeleteSystemPropertyTemplatesRequest,
    ) -> main_models.DeleteSystemPropertyTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_system_property_templates_with_options_async(request, runtime)

    def describe_android_instance_groups_with_options(
        self,
        request: main_models.DescribeAndroidInstanceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAndroidInstanceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAndroidInstanceGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAndroidInstanceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_android_instance_groups_with_options_async(
        self,
        request: main_models.DescribeAndroidInstanceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAndroidInstanceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAndroidInstanceGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAndroidInstanceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_android_instance_groups(
        self,
        request: main_models.DescribeAndroidInstanceGroupsRequest,
    ) -> main_models.DescribeAndroidInstanceGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_android_instance_groups_with_options(request, runtime)

    async def describe_android_instance_groups_async(
        self,
        request: main_models.DescribeAndroidInstanceGroupsRequest,
    ) -> main_models.DescribeAndroidInstanceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_android_instance_groups_with_options_async(request, runtime)

    def describe_android_instances_with_options(
        self,
        request: main_models.DescribeAndroidInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAndroidInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not DaraCore.is_null(request.app_manage_policy_id):
            query['AppManagePolicyId'] = request.app_manage_policy_id
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.qos_rule_ids):
            query['QosRuleIds'] = request.qos_rule_ids
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAndroidInstances',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAndroidInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_android_instances_with_options_async(
        self,
        request: main_models.DescribeAndroidInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAndroidInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not DaraCore.is_null(request.app_manage_policy_id):
            query['AppManagePolicyId'] = request.app_manage_policy_id
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.qos_rule_ids):
            query['QosRuleIds'] = request.qos_rule_ids
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAndroidInstances',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAndroidInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_android_instances(
        self,
        request: main_models.DescribeAndroidInstancesRequest,
    ) -> main_models.DescribeAndroidInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_android_instances_with_options(request, runtime)

    async def describe_android_instances_async(
        self,
        request: main_models.DescribeAndroidInstancesRequest,
    ) -> main_models.DescribeAndroidInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_android_instances_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.installation_status):
            query['InstallationStatus'] = request.installation_status
        if not DaraCore.is_null(request.md5):
            query['MD5'] = request.md5
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.installation_status):
            query['InstallationStatus'] = request.installation_status
        if not DaraCore.is_null(request.md5):
            query['MD5'] = request.md5
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_backup_files_with_options(
        self,
        request: main_models.DescribeBackupFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not DaraCore.is_null(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupFiles',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_files_with_options_async(
        self,
        request: main_models.DescribeBackupFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not DaraCore.is_null(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupFiles',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_files(
        self,
        request: main_models.DescribeBackupFilesRequest,
    ) -> main_models.DescribeBackupFilesResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_files_with_options(request, runtime)

    async def describe_backup_files_async(
        self,
        request: main_models.DescribeBackupFilesRequest,
    ) -> main_models.DescribeBackupFilesResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_files_with_options_async(request, runtime)

    def describe_buckets_with_options(
        self,
        request: main_models.DescribeBucketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBucketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBuckets',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_buckets_with_options_async(
        self,
        request: main_models.DescribeBucketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBucketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBuckets',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_buckets(
        self,
        request: main_models.DescribeBucketsRequest,
    ) -> main_models.DescribeBucketsResponse:
        runtime = RuntimeOptions()
        return self.describe_buckets_with_options(request, runtime)

    async def describe_buckets_async(
        self,
        request: main_models.DescribeBucketsRequest,
    ) -> main_models.DescribeBucketsResponse:
        runtime = RuntimeOptions()
        return await self.describe_buckets_with_options_async(request, runtime)

    def describe_cloud_phone_nodes_with_options(
        self,
        request: main_models.DescribeCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudPhoneNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.node_name_list):
            query['NodeNameList'] = request.node_name_list
        if not DaraCore.is_null(request.server_type):
            query['ServerType'] = request.server_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_phone_nodes_with_options_async(
        self,
        request: main_models.DescribeCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudPhoneNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.node_name_list):
            query['NodeNameList'] = request.node_name_list
        if not DaraCore.is_null(request.server_type):
            query['ServerType'] = request.server_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_phone_nodes(
        self,
        request: main_models.DescribeCloudPhoneNodesRequest,
    ) -> main_models.DescribeCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_phone_nodes_with_options(request, runtime)

    async def describe_cloud_phone_nodes_async(
        self,
        request: main_models.DescribeCloudPhoneNodesRequest,
    ) -> main_models.DescribeCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_phone_nodes_with_options_async(request, runtime)

    def describe_display_config_with_options(
        self,
        request: main_models.DescribeDisplayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisplayConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisplayConfig',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisplayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_display_config_with_options_async(
        self,
        request: main_models.DescribeDisplayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisplayConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisplayConfig',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisplayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_display_config(
        self,
        request: main_models.DescribeDisplayConfigRequest,
    ) -> main_models.DescribeDisplayConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_display_config_with_options(request, runtime)

    async def describe_display_config_async(
        self,
        request: main_models.DescribeDisplayConfigRequest,
    ) -> main_models.DescribeDisplayConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_display_config_with_options_async(request, runtime)

    def describe_image_list_with_options(
        self,
        request: main_models.DescribeImageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_biz_tags):
            query['ImageBizTags'] = request.image_biz_tags
        if not DaraCore.is_null(request.image_package_type):
            query['ImagePackageType'] = request.image_package_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.system_type):
            query['SystemType'] = request.system_type
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.image_type):
            body['ImageType'] = request.image_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_list_with_options_async(
        self,
        request: main_models.DescribeImageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_biz_tags):
            query['ImageBizTags'] = request.image_biz_tags
        if not DaraCore.is_null(request.image_package_type):
            query['ImagePackageType'] = request.image_package_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.system_type):
            query['SystemType'] = request.system_type
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.image_type):
            body['ImageType'] = request.image_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_list(
        self,
        request: main_models.DescribeImageListRequest,
    ) -> main_models.DescribeImageListResponse:
        runtime = RuntimeOptions()
        return self.describe_image_list_with_options(request, runtime)

    async def describe_image_list_async(
        self,
        request: main_models.DescribeImageListRequest,
    ) -> main_models.DescribeImageListResponse:
        runtime = RuntimeOptions()
        return await self.describe_image_list_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.invocation_id):
            query['InvocationId'] = request.invocation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.invocation_id):
            query['InvocationId'] = request.invocation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_key_pairs_with_options(
        self,
        request: main_models.DescribeKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKeyPairs',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_pairs_with_options_async(
        self,
        request: main_models.DescribeKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKeyPairs',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key_pairs(
        self,
        request: main_models.DescribeKeyPairsRequest,
    ) -> main_models.DescribeKeyPairsResponse:
        runtime = RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    async def describe_key_pairs_async(
        self,
        request: main_models.DescribeKeyPairsRequest,
    ) -> main_models.DescribeKeyPairsResponse:
        runtime = RuntimeOptions()
        return await self.describe_key_pairs_with_options_async(request, runtime)

    def describe_metric_last_with_options(
        self,
        request: main_models.DescribeMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricLastResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricLast',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_last_with_options_async(
        self,
        request: main_models.DescribeMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricLastResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricLast',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_last(
        self,
        request: main_models.DescribeMetricLastRequest,
    ) -> main_models.DescribeMetricLastResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_last_with_options(request, runtime)

    async def describe_metric_last_async(
        self,
        request: main_models.DescribeMetricLastRequest,
    ) -> main_models.DescribeMetricLastResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_last_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.process_infos):
            body['ProcessInfos'] = request.process_infos
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.process_infos):
            body['ProcessInfos'] = request.process_infos
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_list(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_metric_top_with_options(
        self,
        request: main_models.DescribeMetricTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricTopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricTop',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_top_with_options_async(
        self,
        request: main_models.DescribeMetricTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricTopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.metric_names):
            body['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricTop',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_top(
        self,
        request: main_models.DescribeMetricTopRequest,
    ) -> main_models.DescribeMetricTopResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_top_with_options(request, runtime)

    async def describe_metric_top_async(
        self,
        request: main_models.DescribeMetricTopRequest,
    ) -> main_models.DescribeMetricTopResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_top_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-09-30',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-09-30',
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

    def describe_spec_with_options(
        self,
        request: main_models.DescribeSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.matrix_spec):
            query['MatrixSpec'] = request.matrix_spec
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.spec_ids):
            query['SpecIds'] = request.spec_ids
        if not DaraCore.is_null(request.spec_status):
            query['SpecStatus'] = request.spec_status
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSpec',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spec_with_options_async(
        self,
        request: main_models.DescribeSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.matrix_spec):
            query['MatrixSpec'] = request.matrix_spec
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.spec_ids):
            query['SpecIds'] = request.spec_ids
        if not DaraCore.is_null(request.spec_status):
            query['SpecStatus'] = request.spec_status
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSpec',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spec(
        self,
        request: main_models.DescribeSpecRequest,
    ) -> main_models.DescribeSpecResponse:
        runtime = RuntimeOptions()
        return self.describe_spec_with_options(request, runtime)

    async def describe_spec_async(
        self,
        request: main_models.DescribeSpecRequest,
    ) -> main_models.DescribeSpecResponse:
        runtime = RuntimeOptions()
        return await self.describe_spec_with_options_async(request, runtime)

    def describe_system_property_templates_with_options(
        self,
        request: main_models.DescribeSystemPropertyTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemPropertyTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemPropertyTemplates',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemPropertyTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_property_templates_with_options_async(
        self,
        request: main_models.DescribeSystemPropertyTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemPropertyTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemPropertyTemplates',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemPropertyTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_property_templates(
        self,
        request: main_models.DescribeSystemPropertyTemplatesRequest,
    ) -> main_models.DescribeSystemPropertyTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_system_property_templates_with_options(request, runtime)

    async def describe_system_property_templates_async(
        self,
        request: main_models.DescribeSystemPropertyTemplatesRequest,
    ) -> main_models.DescribeSystemPropertyTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_property_templates_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: main_models.DescribeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_statuses):
            query['TaskStatuses'] = request.task_statuses
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_types):
            query['TaskTypes'] = request.task_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTasks',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: main_models.DescribeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_statuses):
            query['TaskStatuses'] = request.task_statuses
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_types):
            query['TaskTypes'] = request.task_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTasks',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: main_models.DetachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: main_models.DetachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_key_pair(
        self,
        request: main_models.DetachKeyPairRequest,
    ) -> main_models.DetachKeyPairResponse:
        runtime = RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: main_models.DetachKeyPairRequest,
    ) -> main_models.DetachKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def disconnect_android_instance_with_options(
        self,
        request: main_models.DisconnectAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisconnectAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisconnectAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisconnectAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disconnect_android_instance_with_options_async(
        self,
        request: main_models.DisconnectAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisconnectAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisconnectAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisconnectAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disconnect_android_instance(
        self,
        request: main_models.DisconnectAndroidInstanceRequest,
    ) -> main_models.DisconnectAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.disconnect_android_instance_with_options(request, runtime)

    async def disconnect_android_instance_async(
        self,
        request: main_models.DisconnectAndroidInstanceRequest,
    ) -> main_models.DisconnectAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.disconnect_android_instance_with_options_async(request, runtime)

    def distribute_image_with_options(
        self,
        request: main_models.DistributeImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DistributeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.distribute_region_list):
            body['DistributeRegionList'] = request.distribute_region_list
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DistributeImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DistributeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def distribute_image_with_options_async(
        self,
        request: main_models.DistributeImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DistributeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.distribute_region_list):
            body['DistributeRegionList'] = request.distribute_region_list
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DistributeImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DistributeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def distribute_image(
        self,
        request: main_models.DistributeImageRequest,
    ) -> main_models.DistributeImageResponse:
        runtime = RuntimeOptions()
        return self.distribute_image_with_options(request, runtime)

    async def distribute_image_async(
        self,
        request: main_models.DistributeImageRequest,
    ) -> main_models.DistributeImageResponse:
        runtime = RuntimeOptions()
        return await self.distribute_image_with_options_async(request, runtime)

    def downgrade_android_instance_group_with_options(
        self,
        request: main_models.DowngradeAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_android_instance_group_with_options_async(
        self,
        request: main_models.DowngradeAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_android_instance_group(
        self,
        request: main_models.DowngradeAndroidInstanceGroupRequest,
    ) -> main_models.DowngradeAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.downgrade_android_instance_group_with_options(request, runtime)

    async def downgrade_android_instance_group_async(
        self,
        request: main_models.DowngradeAndroidInstanceGroupRequest,
    ) -> main_models.DowngradeAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.downgrade_android_instance_group_with_options_async(request, runtime)

    def end_coordination_with_options(
        self,
        request: main_models.EndCoordinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndCoordinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coordinator_user_id):
            query['CoordinatorUserId'] = request.coordinator_user_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndCoordination',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndCoordinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_coordination_with_options_async(
        self,
        request: main_models.EndCoordinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndCoordinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coordinator_user_id):
            query['CoordinatorUserId'] = request.coordinator_user_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndCoordination',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndCoordinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_coordination(
        self,
        request: main_models.EndCoordinationRequest,
    ) -> main_models.EndCoordinationResponse:
        runtime = RuntimeOptions()
        return self.end_coordination_with_options(request, runtime)

    async def end_coordination_async(
        self,
        request: main_models.EndCoordinationRequest,
    ) -> main_models.EndCoordinationResponse:
        runtime = RuntimeOptions()
        return await self.end_coordination_with_options_async(request, runtime)

    def expand_data_volume_with_options(
        self,
        request: main_models.ExpandDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpandDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpandDataVolume',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_data_volume_with_options_async(
        self,
        request: main_models.ExpandDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpandDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpandDataVolume',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_data_volume(
        self,
        request: main_models.ExpandDataVolumeRequest,
    ) -> main_models.ExpandDataVolumeResponse:
        runtime = RuntimeOptions()
        return self.expand_data_volume_with_options(request, runtime)

    async def expand_data_volume_async(
        self,
        request: main_models.ExpandDataVolumeRequest,
    ) -> main_models.ExpandDataVolumeResponse:
        runtime = RuntimeOptions()
        return await self.expand_data_volume_with_options_async(request, runtime)

    def expand_phone_data_volume_with_options(
        self,
        request: main_models.ExpandPhoneDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpandPhoneDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpandPhoneDataVolume',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandPhoneDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_phone_data_volume_with_options_async(
        self,
        request: main_models.ExpandPhoneDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpandPhoneDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.phone_data_volume):
            query['PhoneDataVolume'] = request.phone_data_volume
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExpandPhoneDataVolume',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpandPhoneDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_phone_data_volume(
        self,
        request: main_models.ExpandPhoneDataVolumeRequest,
    ) -> main_models.ExpandPhoneDataVolumeResponse:
        runtime = RuntimeOptions()
        return self.expand_phone_data_volume_with_options(request, runtime)

    async def expand_phone_data_volume_async(
        self,
        request: main_models.ExpandPhoneDataVolumeRequest,
    ) -> main_models.ExpandPhoneDataVolumeResponse:
        runtime = RuntimeOptions()
        return await self.expand_phone_data_volume_with_options_async(request, runtime)

    def fetch_file_with_options(
        self,
        request: main_models.FetchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_file_with_options_async(
        self,
        request: main_models.FetchFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_file(
        self,
        request: main_models.FetchFileRequest,
    ) -> main_models.FetchFileResponse:
        runtime = RuntimeOptions()
        return self.fetch_file_with_options(request, runtime)

    async def fetch_file_async(
        self,
        request: main_models.FetchFileRequest,
    ) -> main_models.FetchFileResponse:
        runtime = RuntimeOptions()
        return await self.fetch_file_with_options_async(request, runtime)

    def generate_coordination_code_with_options(
        self,
        request: main_models.GenerateCoordinationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCoordinationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCoordinationCode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCoordinationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_coordination_code_with_options_async(
        self,
        request: main_models.GenerateCoordinationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCoordinationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateCoordinationCode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCoordinationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_coordination_code(
        self,
        request: main_models.GenerateCoordinationCodeRequest,
    ) -> main_models.GenerateCoordinationCodeResponse:
        runtime = RuntimeOptions()
        return self.generate_coordination_code_with_options(request, runtime)

    async def generate_coordination_code_async(
        self,
        request: main_models.GenerateCoordinationCodeRequest,
    ) -> main_models.GenerateCoordinationCodeResponse:
        runtime = RuntimeOptions()
        return await self.generate_coordination_code_with_options_async(request, runtime)

    def get_instance_properties_with_options(
        self,
        request: main_models.GetInstancePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstancePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceProperties',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstancePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_properties_with_options_async(
        self,
        request: main_models.GetInstancePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstancePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceProperties',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstancePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_properties(
        self,
        request: main_models.GetInstancePropertiesRequest,
    ) -> main_models.GetInstancePropertiesResponse:
        runtime = RuntimeOptions()
        return self.get_instance_properties_with_options(request, runtime)

    async def get_instance_properties_async(
        self,
        request: main_models.GetInstancePropertiesRequest,
    ) -> main_models.GetInstancePropertiesResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_properties_with_options_async(request, runtime)

    def get_network_blacklist_with_options(
        self,
        request: main_models.GetNetworkBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkBlacklist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_blacklist_with_options_async(
        self,
        request: main_models.GetNetworkBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkBlacklist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_blacklist(
        self,
        request: main_models.GetNetworkBlacklistRequest,
    ) -> main_models.GetNetworkBlacklistResponse:
        runtime = RuntimeOptions()
        return self.get_network_blacklist_with_options(request, runtime)

    async def get_network_blacklist_async(
        self,
        request: main_models.GetNetworkBlacklistRequest,
    ) -> main_models.GetNetworkBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.get_network_blacklist_with_options_async(request, runtime)

    def import_image_with_options(
        self,
        request: main_models.ImportImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_description):
            query['ImageDescription'] = request.image_description
        if not DaraCore.is_null(request.image_file_url):
            query['ImageFileURL'] = request.image_file_url
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_image_with_options_async(
        self,
        request: main_models.ImportImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_description):
            query['ImageDescription'] = request.image_description
        if not DaraCore.is_null(request.image_file_url):
            query['ImageFileURL'] = request.image_file_url
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_image(
        self,
        request: main_models.ImportImageRequest,
    ) -> main_models.ImportImageResponse:
        runtime = RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    async def import_image_async(
        self,
        request: main_models.ImportImageRequest,
    ) -> main_models.ImportImageResponse:
        runtime = RuntimeOptions()
        return await self.import_image_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: main_models.ImportKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: main_models.ImportKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyPair',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: main_models.ImportKeyPairRequest,
    ) -> main_models.ImportKeyPairResponse:
        runtime = RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: main_models.ImportKeyPairRequest,
    ) -> main_models.ImportKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def install_app_with_options(
        self,
        request: main_models.InstallAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_app_with_options_async(
        self,
        request: main_models.InstallAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_app(
        self,
        request: main_models.InstallAppRequest,
    ) -> main_models.InstallAppResponse:
        runtime = RuntimeOptions()
        return self.install_app_with_options(request, runtime)

    async def install_app_async(
        self,
        request: main_models.InstallAppRequest,
    ) -> main_models.InstallAppResponse:
        runtime = RuntimeOptions()
        return await self.install_app_with_options_async(request, runtime)

    def install_monitor_agent_with_options(
        self,
        request: main_models.InstallMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallMonitorAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            body['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallMonitorAgent',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallMonitorAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_monitor_agent_with_options_async(
        self,
        request: main_models.InstallMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallMonitorAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            body['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallMonitorAgent',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallMonitorAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_monitor_agent(
        self,
        request: main_models.InstallMonitorAgentRequest,
    ) -> main_models.InstallMonitorAgentResponse:
        runtime = RuntimeOptions()
        return self.install_monitor_agent_with_options(request, runtime)

    async def install_monitor_agent_async(
        self,
        request: main_models.InstallMonitorAgentRequest,
    ) -> main_models.InstallMonitorAgentResponse:
        runtime = RuntimeOptions()
        return await self.install_monitor_agent_with_options_async(request, runtime)

    def instance_healer_with_options(
        self,
        request: main_models.InstanceHealerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstanceHealerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstanceHealer',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstanceHealerResponse(),
            self.call_api(params, req, runtime)
        )

    async def instance_healer_with_options_async(
        self,
        request: main_models.InstanceHealerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstanceHealerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstanceHealer',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstanceHealerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def instance_healer(
        self,
        request: main_models.InstanceHealerRequest,
    ) -> main_models.InstanceHealerResponse:
        runtime = RuntimeOptions()
        return self.instance_healer_with_options(request, runtime)

    async def instance_healer_async(
        self,
        request: main_models.InstanceHealerRequest,
    ) -> main_models.InstanceHealerResponse:
        runtime = RuntimeOptions()
        return await self.instance_healer_with_options_async(request, runtime)

    def list_instance_adb_attributes_with_options(
        self,
        request: main_models.ListInstanceAdbAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAdbAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not DaraCore.is_null(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAdbAttributes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAdbAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_adb_attributes_with_options_async(
        self,
        request: main_models.ListInstanceAdbAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAdbAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not DaraCore.is_null(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAdbAttributes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAdbAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_adb_attributes(
        self,
        request: main_models.ListInstanceAdbAttributesRequest,
    ) -> main_models.ListInstanceAdbAttributesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_adb_attributes_with_options(request, runtime)

    async def list_instance_adb_attributes_async(
        self,
        request: main_models.ListInstanceAdbAttributesRequest,
    ) -> main_models.ListInstanceAdbAttributesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_adb_attributes_with_options_async(request, runtime)

    def list_policy_groups_with_options(
        self,
        request: main_models.ListPolicyGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_group_ids):
            body['PolicyGroupIds'] = request.policy_group_ids
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_groups_with_options_async(
        self,
        request: main_models.ListPolicyGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_group_ids):
            body['PolicyGroupIds'] = request.policy_group_ids
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_groups(
        self,
        request: main_models.ListPolicyGroupsRequest,
    ) -> main_models.ListPolicyGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_policy_groups_with_options(request, runtime)

    async def list_policy_groups_async(
        self,
        request: main_models.ListPolicyGroupsRequest,
    ) -> main_models.ListPolicyGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_android_instance_with_options(
        self,
        request: main_models.ModifyAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.new_android_instance_name):
            query['NewAndroidInstanceName'] = request.new_android_instance_name
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_android_instance_with_options_async(
        self,
        request: main_models.ModifyAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not DaraCore.is_null(request.down_bandwidth_limit):
            query['DownBandwidthLimit'] = request.down_bandwidth_limit
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.new_android_instance_name):
            query['NewAndroidInstanceName'] = request.new_android_instance_name
        if not DaraCore.is_null(request.up_bandwidth_limit):
            query['UpBandwidthLimit'] = request.up_bandwidth_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_android_instance(
        self,
        request: main_models.ModifyAndroidInstanceRequest,
    ) -> main_models.ModifyAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_android_instance_with_options(request, runtime)

    async def modify_android_instance_async(
        self,
        request: main_models.ModifyAndroidInstanceRequest,
    ) -> main_models.ModifyAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_android_instance_with_options_async(request, runtime)

    def modify_android_instance_group_with_options(
        self,
        request: main_models.ModifyAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.new_instance_group_name):
            query['NewInstanceGroupName'] = request.new_instance_group_name
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_android_instance_group_with_options_async(
        self,
        request: main_models.ModifyAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.new_instance_group_name):
            query['NewInstanceGroupName'] = request.new_instance_group_name
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_android_instance_group(
        self,
        request: main_models.ModifyAndroidInstanceGroupRequest,
    ) -> main_models.ModifyAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_android_instance_group_with_options(request, runtime)

    async def modify_android_instance_group_async(
        self,
        request: main_models.ModifyAndroidInstanceGroupRequest,
    ) -> main_models.ModifyAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_android_instance_group_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.icon_url):
            query['IconUrl'] = request.icon_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_cloud_phone_node_with_options(
        self,
        request: main_models.ModifyCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudPhoneNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_phone_node_with_options_async(
        self,
        request: main_models.ModifyCloudPhoneNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudPhoneNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.stream_mode):
            query['StreamMode'] = request.stream_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudPhoneNode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_phone_node(
        self,
        request: main_models.ModifyCloudPhoneNodeRequest,
    ) -> main_models.ModifyCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return self.modify_cloud_phone_node_with_options(request, runtime)

    async def modify_cloud_phone_node_async(
        self,
        request: main_models.ModifyCloudPhoneNodeRequest,
    ) -> main_models.ModifyCloudPhoneNodeResponse:
        runtime = RuntimeOptions()
        return await self.modify_cloud_phone_node_with_options_async(request, runtime)

    def modify_display_config_with_options(
        self,
        tmp_req: main_models.ModifyDisplayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDisplayConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyDisplayConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_config):
            request.display_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDisplayConfig',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDisplayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_display_config_with_options_async(
        self,
        tmp_req: main_models.ModifyDisplayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDisplayConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyDisplayConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.display_config):
            request.display_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDisplayConfig',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDisplayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_display_config(
        self,
        request: main_models.ModifyDisplayConfigRequest,
    ) -> main_models.ModifyDisplayConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_display_config_with_options(request, runtime)

    async def modify_display_config_async(
        self,
        request: main_models.ModifyDisplayConfigRequest,
    ) -> main_models.ModifyDisplayConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_display_config_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        request: main_models.ModifyInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceChargeType',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        request: main_models.ModifyInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceChargeType',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: main_models.ModifyInstanceChargeTypeRequest,
    ) -> main_models.ModifyInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: main_models.ModifyInstanceChargeTypeRequest,
    ) -> main_models.ModifyInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_key_pair_name_with_options(
        self,
        request: main_models.ModifyKeyPairNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyKeyPairNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.new_key_pair_name):
            query['NewKeyPairName'] = request.new_key_pair_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyKeyPairName',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyKeyPairNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_key_pair_name_with_options_async(
        self,
        request: main_models.ModifyKeyPairNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyKeyPairNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not DaraCore.is_null(request.new_key_pair_name):
            query['NewKeyPairName'] = request.new_key_pair_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyKeyPairName',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyKeyPairNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_key_pair_name(
        self,
        request: main_models.ModifyKeyPairNameRequest,
    ) -> main_models.ModifyKeyPairNameResponse:
        runtime = RuntimeOptions()
        return self.modify_key_pair_name_with_options(request, runtime)

    async def modify_key_pair_name_async(
        self,
        request: main_models.ModifyKeyPairNameRequest,
    ) -> main_models.ModifyKeyPairNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_key_pair_name_with_options_async(request, runtime)

    def modify_policy_group_with_options(
        self,
        tmp_req: main_models.ModifyPolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not DaraCore.is_null(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not DaraCore.is_null(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not DaraCore.is_null(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not DaraCore.is_null(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not DaraCore.is_null(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not DaraCore.is_null(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not DaraCore.is_null(request.policy_group_id):
            body['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_group_with_options_async(
        self,
        tmp_req: main_models.ModifyPolicyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not DaraCore.is_null(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not DaraCore.is_null(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not DaraCore.is_null(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not DaraCore.is_null(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not DaraCore.is_null(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not DaraCore.is_null(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not DaraCore.is_null(request.policy_group_id):
            body['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not DaraCore.is_null(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not DaraCore.is_null(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not DaraCore.is_null(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_group(
        self,
        request: main_models.ModifyPolicyGroupRequest,
    ) -> main_models.ModifyPolicyGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    async def modify_policy_group_async(
        self,
        request: main_models.ModifyPolicyGroupRequest,
    ) -> main_models.ModifyPolicyGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def modify_system_property_template_with_options(
        self,
        tmp_req: main_models.ModifySystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySystemPropertyTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifySystemPropertyTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.system_property_info):
            request.system_property_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_property_info, 'SystemPropertyInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_auto):
            query['EnableAuto'] = request.enable_auto
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.system_property_info_shrink):
            query['SystemPropertyInfo'] = request.system_property_info_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySystemPropertyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_system_property_template_with_options_async(
        self,
        tmp_req: main_models.ModifySystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySystemPropertyTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifySystemPropertyTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.system_property_info):
            request.system_property_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_property_info, 'SystemPropertyInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.enable_auto):
            query['EnableAuto'] = request.enable_auto
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.system_property_info_shrink):
            query['SystemPropertyInfo'] = request.system_property_info_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySystemPropertyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_system_property_template(
        self,
        request: main_models.ModifySystemPropertyTemplateRequest,
    ) -> main_models.ModifySystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_system_property_template_with_options(request, runtime)

    async def modify_system_property_template_async(
        self,
        request: main_models.ModifySystemPropertyTemplateRequest,
    ) -> main_models.ModifySystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_system_property_template_with_options_async(request, runtime)

    def operate_app_with_options(
        self,
        request: main_models.OperateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_with_options_async(
        self,
        request: main_models.OperateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app(
        self,
        request: main_models.OperateAppRequest,
    ) -> main_models.OperateAppResponse:
        runtime = RuntimeOptions()
        return self.operate_app_with_options(request, runtime)

    async def operate_app_async(
        self,
        request: main_models.OperateAppRequest,
    ) -> main_models.OperateAppResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_with_options_async(request, runtime)

    def reboot_android_instances_in_group_with_options(
        self,
        request: main_models.RebootAndroidInstancesInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootAndroidInstancesInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootAndroidInstancesInGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootAndroidInstancesInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_android_instances_in_group_with_options_async(
        self,
        request: main_models.RebootAndroidInstancesInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootAndroidInstancesInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootAndroidInstancesInGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootAndroidInstancesInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_android_instances_in_group(
        self,
        request: main_models.RebootAndroidInstancesInGroupRequest,
    ) -> main_models.RebootAndroidInstancesInGroupResponse:
        runtime = RuntimeOptions()
        return self.reboot_android_instances_in_group_with_options(request, runtime)

    async def reboot_android_instances_in_group_async(
        self,
        request: main_models.RebootAndroidInstancesInGroupRequest,
    ) -> main_models.RebootAndroidInstancesInGroupResponse:
        runtime = RuntimeOptions()
        return await self.reboot_android_instances_in_group_with_options_async(request, runtime)

    def recover_android_instance_with_options(
        self,
        request: main_models.RecoverAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_android_instance_with_options_async(
        self,
        request: main_models.RecoverAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_android_instance(
        self,
        request: main_models.RecoverAndroidInstanceRequest,
    ) -> main_models.RecoverAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.recover_android_instance_with_options(request, runtime)

    async def recover_android_instance_async(
        self,
        request: main_models.RecoverAndroidInstanceRequest,
    ) -> main_models.RecoverAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.recover_android_instance_with_options_async(request, runtime)

    def recover_app_with_options(
        self,
        request: main_models.RecoverAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_app_with_options_async(
        self,
        request: main_models.RecoverAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_app(
        self,
        request: main_models.RecoverAppRequest,
    ) -> main_models.RecoverAppResponse:
        runtime = RuntimeOptions()
        return self.recover_app_with_options(request, runtime)

    async def recover_app_async(
        self,
        request: main_models.RecoverAppRequest,
    ) -> main_models.RecoverAppResponse:
        runtime = RuntimeOptions()
        return await self.recover_app_with_options_async(request, runtime)

    def recovery_file_with_options(
        self,
        request: main_models.RecoveryFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoveryFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoveryFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoveryFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_file_with_options_async(
        self,
        request: main_models.RecoveryFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoveryFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not DaraCore.is_null(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not DaraCore.is_null(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoveryFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoveryFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_file(
        self,
        request: main_models.RecoveryFileRequest,
    ) -> main_models.RecoveryFileResponse:
        runtime = RuntimeOptions()
        return self.recovery_file_with_options(request, runtime)

    async def recovery_file_async(
        self,
        request: main_models.RecoveryFileRequest,
    ) -> main_models.RecoveryFileResponse:
        runtime = RuntimeOptions()
        return await self.recovery_file_with_options_async(request, runtime)

    def renew_android_instance_groups_with_options(
        self,
        request: main_models.RenewAndroidInstanceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAndroidInstanceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAndroidInstanceGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAndroidInstanceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_android_instance_groups_with_options_async(
        self,
        request: main_models.RenewAndroidInstanceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAndroidInstanceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAndroidInstanceGroups',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAndroidInstanceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_android_instance_groups(
        self,
        request: main_models.RenewAndroidInstanceGroupsRequest,
    ) -> main_models.RenewAndroidInstanceGroupsResponse:
        runtime = RuntimeOptions()
        return self.renew_android_instance_groups_with_options(request, runtime)

    async def renew_android_instance_groups_async(
        self,
        request: main_models.RenewAndroidInstanceGroupsRequest,
    ) -> main_models.RenewAndroidInstanceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.renew_android_instance_groups_with_options_async(request, runtime)

    def renew_cloud_phone_nodes_with_options(
        self,
        request: main_models.RenewCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewCloudPhoneNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_cloud_phone_nodes_with_options_async(
        self,
        request: main_models.RenewCloudPhoneNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewCloudPhoneNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewCloudPhoneNodes',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_cloud_phone_nodes(
        self,
        request: main_models.RenewCloudPhoneNodesRequest,
    ) -> main_models.RenewCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return self.renew_cloud_phone_nodes_with_options(request, runtime)

    async def renew_cloud_phone_nodes_async(
        self,
        request: main_models.RenewCloudPhoneNodesRequest,
    ) -> main_models.RenewCloudPhoneNodesResponse:
        runtime = RuntimeOptions()
        return await self.renew_cloud_phone_nodes_with_options_async(request, runtime)

    def reset_android_instances_in_group_with_options(
        self,
        request: main_models.ResetAndroidInstancesInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAndroidInstancesInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.setting_reset_type):
            query['SettingResetType'] = request.setting_reset_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAndroidInstancesInGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAndroidInstancesInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_android_instances_in_group_with_options_async(
        self,
        request: main_models.ResetAndroidInstancesInGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAndroidInstancesInGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not DaraCore.is_null(request.setting_reset_type):
            query['SettingResetType'] = request.setting_reset_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAndroidInstancesInGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAndroidInstancesInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_android_instances_in_group(
        self,
        request: main_models.ResetAndroidInstancesInGroupRequest,
    ) -> main_models.ResetAndroidInstancesInGroupResponse:
        runtime = RuntimeOptions()
        return self.reset_android_instances_in_group_with_options(request, runtime)

    async def reset_android_instances_in_group_async(
        self,
        request: main_models.ResetAndroidInstancesInGroupRequest,
    ) -> main_models.ResetAndroidInstancesInGroupResponse:
        runtime = RuntimeOptions()
        return await self.reset_android_instances_in_group_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        request: main_models.SendFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not DaraCore.is_null(request.target_file_name):
            query['TargetFileName'] = request.target_file_name
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_file_with_options_async(
        self,
        request: main_models.SendFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not DaraCore.is_null(request.target_file_name):
            query['TargetFileName'] = request.target_file_name
        if not DaraCore.is_null(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendFile',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_file(
        self,
        request: main_models.SendFileRequest,
    ) -> main_models.SendFileResponse:
        runtime = RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: main_models.SendFileRequest,
    ) -> main_models.SendFileResponse:
        runtime = RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def send_system_property_template_with_options(
        self,
        request: main_models.SendSystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendSystemPropertyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSystemPropertyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_system_property_template_with_options_async(
        self,
        request: main_models.SendSystemPropertyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendSystemPropertyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSystemPropertyTemplate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSystemPropertyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_system_property_template(
        self,
        request: main_models.SendSystemPropertyTemplateRequest,
    ) -> main_models.SendSystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return self.send_system_property_template_with_options(request, runtime)

    async def send_system_property_template_async(
        self,
        request: main_models.SendSystemPropertyTemplateRequest,
    ) -> main_models.SendSystemPropertyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.send_system_property_template_with_options_async(request, runtime)

    def set_adb_secure_with_options(
        self,
        request: main_models.SetAdbSecureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAdbSecureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAdbSecure',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAdbSecureResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_adb_secure_with_options_async(
        self,
        request: main_models.SetAdbSecureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAdbSecureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAdbSecure',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAdbSecureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_adb_secure(
        self,
        request: main_models.SetAdbSecureRequest,
    ) -> main_models.SetAdbSecureResponse:
        runtime = RuntimeOptions()
        return self.set_adb_secure_with_options(request, runtime)

    async def set_adb_secure_async(
        self,
        request: main_models.SetAdbSecureRequest,
    ) -> main_models.SetAdbSecureResponse:
        runtime = RuntimeOptions()
        return await self.set_adb_secure_with_options_async(request, runtime)

    def set_network_blacklist_with_options(
        self,
        request: main_models.SetNetworkBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetNetworkBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_blacklist):
            query['DomainBlacklist'] = request.domain_blacklist
        if not DaraCore.is_null(request.ip_blacklist):
            query['IpBlacklist'] = request.ip_blacklist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetNetworkBlacklist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetNetworkBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_network_blacklist_with_options_async(
        self,
        request: main_models.SetNetworkBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetNetworkBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_blacklist):
            query['DomainBlacklist'] = request.domain_blacklist
        if not DaraCore.is_null(request.ip_blacklist):
            query['IpBlacklist'] = request.ip_blacklist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetNetworkBlacklist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetNetworkBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_network_blacklist(
        self,
        request: main_models.SetNetworkBlacklistRequest,
    ) -> main_models.SetNetworkBlacklistResponse:
        runtime = RuntimeOptions()
        return self.set_network_blacklist_with_options(request, runtime)

    async def set_network_blacklist_async(
        self,
        request: main_models.SetNetworkBlacklistRequest,
    ) -> main_models.SetNetworkBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.set_network_blacklist_with_options_async(request, runtime)

    def start_android_instance_with_options(
        self,
        request: main_models.StartAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_android_instance_with_options_async(
        self,
        request: main_models.StartAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_android_instance(
        self,
        request: main_models.StartAndroidInstanceRequest,
    ) -> main_models.StartAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_android_instance_with_options(request, runtime)

    async def start_android_instance_async(
        self,
        request: main_models.StartAndroidInstanceRequest,
    ) -> main_models.StartAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_android_instance_with_options_async(request, runtime)

    def start_instance_adb_with_options(
        self,
        request: main_models.StartInstanceAdbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceAdbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstanceAdb',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceAdbResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_adb_with_options_async(
        self,
        request: main_models.StartInstanceAdbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceAdbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstanceAdb',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceAdbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance_adb(
        self,
        request: main_models.StartInstanceAdbRequest,
    ) -> main_models.StartInstanceAdbResponse:
        runtime = RuntimeOptions()
        return self.start_instance_adb_with_options(request, runtime)

    async def start_instance_adb_async(
        self,
        request: main_models.StartInstanceAdbRequest,
    ) -> main_models.StartInstanceAdbResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_adb_with_options_async(request, runtime)

    def stop_android_instance_with_options(
        self,
        request: main_models.StopAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_android_instance_with_options_async(
        self,
        request: main_models.StopAndroidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAndroidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAndroidInstance',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_android_instance(
        self,
        request: main_models.StopAndroidInstanceRequest,
    ) -> main_models.StopAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_android_instance_with_options(request, runtime)

    async def stop_android_instance_async(
        self,
        request: main_models.StopAndroidInstanceRequest,
    ) -> main_models.StopAndroidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_android_instance_with_options_async(request, runtime)

    def stop_instance_adb_with_options(
        self,
        request: main_models.StopInstanceAdbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceAdbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstanceAdb',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceAdbResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_adb_with_options_async(
        self,
        request: main_models.StopInstanceAdbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceAdbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstanceAdb',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceAdbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance_adb(
        self,
        request: main_models.StopInstanceAdbRequest,
    ) -> main_models.StopInstanceAdbResponse:
        runtime = RuntimeOptions()
        return self.stop_instance_adb_with_options(request, runtime)

    async def stop_instance_adb_async(
        self,
        request: main_models.StopInstanceAdbRequest,
    ) -> main_models.StopInstanceAdbResponse:
        runtime = RuntimeOptions()
        return await self.stop_instance_adb_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def uninstall_app_with_options(
        self,
        request: main_models.UninstallAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_app_with_options_async(
        self,
        request: main_models.UninstallAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallApp',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_app(
        self,
        request: main_models.UninstallAppRequest,
    ) -> main_models.UninstallAppResponse:
        runtime = RuntimeOptions()
        return self.uninstall_app_with_options(request, runtime)

    async def uninstall_app_async(
        self,
        request: main_models.UninstallAppRequest,
    ) -> main_models.UninstallAppResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_app_with_options_async(request, runtime)

    def uninstall_monitor_agent_with_options(
        self,
        request: main_models.UninstallMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallMonitorAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            body['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallMonitorAgent',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallMonitorAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_monitor_agent_with_options_async(
        self,
        request: main_models.UninstallMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallMonitorAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not DaraCore.is_null(request.sale_mode):
            body['SaleMode'] = request.sale_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UninstallMonitorAgent',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallMonitorAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_monitor_agent(
        self,
        request: main_models.UninstallMonitorAgentRequest,
    ) -> main_models.UninstallMonitorAgentResponse:
        runtime = RuntimeOptions()
        return self.uninstall_monitor_agent_with_options(request, runtime)

    async def uninstall_monitor_agent_async(
        self,
        request: main_models.UninstallMonitorAgentRequest,
    ) -> main_models.UninstallMonitorAgentResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_monitor_agent_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_image_name_with_options(
        self,
        request: main_models.UpdateCustomImageNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomImageNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomImageName',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomImageNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_image_name_with_options_async(
        self,
        request: main_models.UpdateCustomImageNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomImageNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomImageName',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomImageNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_image_name(
        self,
        request: main_models.UpdateCustomImageNameRequest,
    ) -> main_models.UpdateCustomImageNameResponse:
        runtime = RuntimeOptions()
        return self.update_custom_image_name_with_options(request, runtime)

    async def update_custom_image_name_async(
        self,
        request: main_models.UpdateCustomImageNameRequest,
    ) -> main_models.UpdateCustomImageNameResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_image_name_with_options_async(request, runtime)

    def update_instance_group_image_with_options(
        self,
        request: main_models.UpdateInstanceGroupImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceGroupImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_group_ids):
            body['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceGroupImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceGroupImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_group_image_with_options_async(
        self,
        request: main_models.UpdateInstanceGroupImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceGroupImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_group_ids):
            body['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceGroupImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceGroupImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_group_image(
        self,
        request: main_models.UpdateInstanceGroupImageRequest,
    ) -> main_models.UpdateInstanceGroupImageResponse:
        runtime = RuntimeOptions()
        return self.update_instance_group_image_with_options(request, runtime)

    async def update_instance_group_image_async(
        self,
        request: main_models.UpdateInstanceGroupImageRequest,
    ) -> main_models.UpdateInstanceGroupImageResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_group_image_with_options_async(request, runtime)

    def update_instance_image_with_options(
        self,
        request: main_models.UpdateInstanceImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.reset):
            query['Reset'] = request.reset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_image_with_options_async(
        self,
        request: main_models.UpdateInstanceImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_param_validation):
            query['IgnoreParamValidation'] = request.ignore_param_validation
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.reset):
            query['Reset'] = request.reset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceImage',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_image(
        self,
        request: main_models.UpdateInstanceImageRequest,
    ) -> main_models.UpdateInstanceImageResponse:
        runtime = RuntimeOptions()
        return self.update_instance_image_with_options(request, runtime)

    async def update_instance_image_async(
        self,
        request: main_models.UpdateInstanceImageRequest,
    ) -> main_models.UpdateInstanceImageResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_image_with_options_async(request, runtime)

    def upgrade_android_instance_group_with_options(
        self,
        request: main_models.UpgradeAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.increase_number_of_instance):
            query['IncreaseNumberOfInstance'] = request.increase_number_of_instance
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_android_instance_group_with_options_async(
        self,
        request: main_models.UpgradeAndroidInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAndroidInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.increase_number_of_instance):
            query['IncreaseNumberOfInstance'] = request.increase_number_of_instance
        if not DaraCore.is_null(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAndroidInstanceGroup',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_android_instance_group(
        self,
        request: main_models.UpgradeAndroidInstanceGroupRequest,
    ) -> main_models.UpgradeAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.upgrade_android_instance_group_with_options(request, runtime)

    async def upgrade_android_instance_group_async(
        self,
        request: main_models.UpgradeAndroidInstanceGroupRequest,
    ) -> main_models.UpgradeAndroidInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_android_instance_group_with_options_async(request, runtime)
