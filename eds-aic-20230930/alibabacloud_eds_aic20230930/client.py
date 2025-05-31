# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eds_aic20230930 import models as eds_aic_20230930_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_key_pair_with_options(
        self,
        request: eds_aic_20230930_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.AttachKeyPairResponse:
        """
        @summary Attaches an Android Debug Bridge (ADB) key pair to one or more cloud phone instances.
        
        @description    You can attach to an ADB key pair only to cloud phone instances in the Running state.
        After you attach an ADB key pair, make sure the private key of the ADB key pair is copied to the ~/.android directory (macOS or Linux operating systems) or the C:\\Users\\Username.android directory (Windows operating systems). In addition, you must run the adb kill-server command to restart the ADB process to ensure correct ADB connection. Otherwise, ADB connection may fail due to authentication exceptions.
        
        @param request: AttachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.AttachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_key_pair_with_options_async(
        self,
        request: eds_aic_20230930_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.AttachKeyPairResponse:
        """
        @summary Attaches an Android Debug Bridge (ADB) key pair to one or more cloud phone instances.
        
        @description    You can attach to an ADB key pair only to cloud phone instances in the Running state.
        After you attach an ADB key pair, make sure the private key of the ADB key pair is copied to the ~/.android directory (macOS or Linux operating systems) or the C:\\Users\\Username.android directory (Windows operating systems). In addition, you must run the adb kill-server command to restart the ADB process to ensure correct ADB connection. Otherwise, ADB connection may fail due to authentication exceptions.
        
        @param request: AttachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.AttachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_key_pair(
        self,
        request: eds_aic_20230930_models.AttachKeyPairRequest,
    ) -> eds_aic_20230930_models.AttachKeyPairResponse:
        """
        @summary Attaches an Android Debug Bridge (ADB) key pair to one or more cloud phone instances.
        
        @description    You can attach to an ADB key pair only to cloud phone instances in the Running state.
        After you attach an ADB key pair, make sure the private key of the ADB key pair is copied to the ~/.android directory (macOS or Linux operating systems) or the C:\\Users\\Username.android directory (Windows operating systems). In addition, you must run the adb kill-server command to restart the ADB process to ensure correct ADB connection. Otherwise, ADB connection may fail due to authentication exceptions.
        
        @param request: AttachKeyPairRequest
        @return: AttachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    async def attach_key_pair_async(
        self,
        request: eds_aic_20230930_models.AttachKeyPairRequest,
    ) -> eds_aic_20230930_models.AttachKeyPairResponse:
        """
        @summary Attaches an Android Debug Bridge (ADB) key pair to one or more cloud phone instances.
        
        @description    You can attach to an ADB key pair only to cloud phone instances in the Running state.
        After you attach an ADB key pair, make sure the private key of the ADB key pair is copied to the ~/.android directory (macOS or Linux operating systems) or the C:\\Users\\Username.android directory (Windows operating systems). In addition, you must run the adb kill-server command to restart the ADB process to ensure correct ADB connection. Otherwise, ADB connection may fail due to authentication exceptions.
        
        @param request: AttachKeyPairRequest
        @return: AttachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_key_pair_with_options_async(request, runtime)

    def authorize_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.AuthorizeAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.AuthorizeAndroidInstanceResponse:
        """
        @summary Authorize/unauthorize Android instances for users.
        
        @description Instance states that support user assignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed.
        Instance states that support unassignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed, Expired, Overdue, Deleted.
        
        @param request: AuthorizeAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.authorize_user_id):
            query['AuthorizeUserId'] = request.authorize_user_id
        if not UtilClient.is_unset(request.un_authorize_user_id):
            query['UnAuthorizeUserId'] = request.un_authorize_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.AuthorizeAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_android_instance_with_options_async(
        self,
        request: eds_aic_20230930_models.AuthorizeAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.AuthorizeAndroidInstanceResponse:
        """
        @summary Authorize/unauthorize Android instances for users.
        
        @description Instance states that support user assignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed.
        Instance states that support unassignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed, Expired, Overdue, Deleted.
        
        @param request: AuthorizeAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.authorize_user_id):
            query['AuthorizeUserId'] = request.authorize_user_id
        if not UtilClient.is_unset(request.un_authorize_user_id):
            query['UnAuthorizeUserId'] = request.un_authorize_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.AuthorizeAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_android_instance(
        self,
        request: eds_aic_20230930_models.AuthorizeAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.AuthorizeAndroidInstanceResponse:
        """
        @summary Authorize/unauthorize Android instances for users.
        
        @description Instance states that support user assignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed.
        Instance states that support unassignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed, Expired, Overdue, Deleted.
        
        @param request: AuthorizeAndroidInstanceRequest
        @return: AuthorizeAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_android_instance_with_options(request, runtime)

    async def authorize_android_instance_async(
        self,
        request: eds_aic_20230930_models.AuthorizeAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.AuthorizeAndroidInstanceResponse:
        """
        @summary Authorize/unauthorize Android instances for users.
        
        @description Instance states that support user assignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed.
        Instance states that support unassignment: Available, Shutting Down, Stopped, Starting, Backing Up, Restoring, Backup Failed, Restore Failed, Expired, Overdue, Deleted.
        
        @param request: AuthorizeAndroidInstanceRequest
        @return: AuthorizeAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_android_instance_with_options_async(request, runtime)

    def backup_file_with_options(
        self,
        request: eds_aic_20230930_models.BackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.BackupFileResponse:
        """
        @summary Generates and uploads backup files.
        
        @description Currently, this operation allows you to upload only backup files generated by cloud phones to Object Storage Service (OSS) buckets.
        
        @param request: BackupFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not UtilClient.is_unset(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not UtilClient.is_unset(request.source_file_path_list):
            query['SourceFilePathList'] = request.source_file_path_list
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackupFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.BackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def backup_file_with_options_async(
        self,
        request: eds_aic_20230930_models.BackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.BackupFileResponse:
        """
        @summary Generates and uploads backup files.
        
        @description Currently, this operation allows you to upload only backup files generated by cloud phones to Object Storage Service (OSS) buckets.
        
        @param request: BackupFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not UtilClient.is_unset(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source_app_list):
            query['SourceAppList'] = request.source_app_list
        if not UtilClient.is_unset(request.source_file_path_list):
            query['SourceFilePathList'] = request.source_file_path_list
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BackupFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.BackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backup_file(
        self,
        request: eds_aic_20230930_models.BackupFileRequest,
    ) -> eds_aic_20230930_models.BackupFileResponse:
        """
        @summary Generates and uploads backup files.
        
        @description Currently, this operation allows you to upload only backup files generated by cloud phones to Object Storage Service (OSS) buckets.
        
        @param request: BackupFileRequest
        @return: BackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.backup_file_with_options(request, runtime)

    async def backup_file_async(
        self,
        request: eds_aic_20230930_models.BackupFileRequest,
    ) -> eds_aic_20230930_models.BackupFileResponse:
        """
        @summary Generates and uploads backup files.
        
        @description Currently, this operation allows you to upload only backup files generated by cloud phones to Object Storage Service (OSS) buckets.
        
        @param request: BackupFileRequest
        @return: BackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.backup_file_with_options_async(request, runtime)

    def batch_get_acp_connection_ticket_with_options(
        self,
        request: eds_aic_20230930_models.BatchGetAcpConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse:
        """
        @summary Retrieves connection tickets in batch.
        
        @param request: BatchGetAcpConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetAcpConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_tasks):
            query['InstanceTasks'] = request.instance_tasks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetAcpConnectionTicket',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_acp_connection_ticket_with_options_async(
        self,
        request: eds_aic_20230930_models.BatchGetAcpConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse:
        """
        @summary Retrieves connection tickets in batch.
        
        @param request: BatchGetAcpConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetAcpConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_tasks):
            query['InstanceTasks'] = request.instance_tasks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetAcpConnectionTicket',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_acp_connection_ticket(
        self,
        request: eds_aic_20230930_models.BatchGetAcpConnectionTicketRequest,
    ) -> eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse:
        """
        @summary Retrieves connection tickets in batch.
        
        @param request: BatchGetAcpConnectionTicketRequest
        @return: BatchGetAcpConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_acp_connection_ticket_with_options(request, runtime)

    async def batch_get_acp_connection_ticket_async(
        self,
        request: eds_aic_20230930_models.BatchGetAcpConnectionTicketRequest,
    ) -> eds_aic_20230930_models.BatchGetAcpConnectionTicketResponse:
        """
        @summary Retrieves connection tickets in batch.
        
        @param request: BatchGetAcpConnectionTicketRequest
        @return: BatchGetAcpConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_acp_connection_ticket_with_options_async(request, runtime)

    def change_cloud_phone_node_with_options(
        self,
        request: eds_aic_20230930_models.ChangeCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ChangeCloudPhoneNodeResponse:
        """
        @summary 修改云手机矩阵的配置
        
        @param request: ChangeCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCloudPhoneNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ChangeCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cloud_phone_node_with_options_async(
        self,
        request: eds_aic_20230930_models.ChangeCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ChangeCloudPhoneNodeResponse:
        """
        @summary 修改云手机矩阵的配置
        
        @param request: ChangeCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCloudPhoneNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ChangeCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cloud_phone_node(
        self,
        request: eds_aic_20230930_models.ChangeCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.ChangeCloudPhoneNodeResponse:
        """
        @summary 修改云手机矩阵的配置
        
        @param request: ChangeCloudPhoneNodeRequest
        @return: ChangeCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_cloud_phone_node_with_options(request, runtime)

    async def change_cloud_phone_node_async(
        self,
        request: eds_aic_20230930_models.ChangeCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.ChangeCloudPhoneNodeResponse:
        """
        @summary 修改云手机矩阵的配置
        
        @param request: ChangeCloudPhoneNodeRequest
        @return: ChangeCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_cloud_phone_node_with_options_async(request, runtime)

    def check_resource_stock_with_options(
        self,
        request: eds_aic_20230930_models.CheckResourceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CheckResourceStockResponse:
        """
        @summary Check the resource inventory.
        
        @param request: CheckResourceStockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourceStockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acp_spec_id):
            query['AcpSpecId'] = request.acp_spec_id
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResourceStock',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CheckResourceStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_stock_with_options_async(
        self,
        request: eds_aic_20230930_models.CheckResourceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CheckResourceStockResponse:
        """
        @summary Check the resource inventory.
        
        @param request: CheckResourceStockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourceStockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acp_spec_id):
            query['AcpSpecId'] = request.acp_spec_id
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResourceStock',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CheckResourceStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_stock(
        self,
        request: eds_aic_20230930_models.CheckResourceStockRequest,
    ) -> eds_aic_20230930_models.CheckResourceStockResponse:
        """
        @summary Check the resource inventory.
        
        @param request: CheckResourceStockRequest
        @return: CheckResourceStockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_resource_stock_with_options(request, runtime)

    async def check_resource_stock_async(
        self,
        request: eds_aic_20230930_models.CheckResourceStockRequest,
    ) -> eds_aic_20230930_models.CheckResourceStockResponse:
        """
        @summary Check the resource inventory.
        
        @param request: CheckResourceStockRequest
        @return: CheckResourceStockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_resource_stock_with_options_async(request, runtime)

    def create_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.CreateAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAndroidInstanceGroupResponse:
        """
        @summary Creates pay-as-you-go or subscription instance groups.
        
        @description Before creating an instance group, ensure you understand the [billing methods](https://help.aliyun.com/document_detail/2807121.html) supported by Cloud Phone.
        If the billing method of an instance group is PrePaid, AutoPay is set to false by default. In this case, you need to go to [Expenses and Costs](https://usercenter2-intl.aliyun.com/order/list) to manually complete the payment.
        You can also set AutoPay to true based on your business requirements.
        
        @param request: CreateAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
        if not UtilClient.is_unset(request.ipv_6bandwidth):
            query['Ipv6Bandwidth'] = request.ipv_6bandwidth
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.number_of_instances):
            query['NumberOfInstances'] = request.number_of_instances
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_android_instance_group_with_options_async(
        self,
        request: eds_aic_20230930_models.CreateAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAndroidInstanceGroupResponse:
        """
        @summary Creates pay-as-you-go or subscription instance groups.
        
        @description Before creating an instance group, ensure you understand the [billing methods](https://help.aliyun.com/document_detail/2807121.html) supported by Cloud Phone.
        If the billing method of an instance group is PrePaid, AutoPay is set to false by default. In this case, you need to go to [Expenses and Costs](https://usercenter2-intl.aliyun.com/order/list) to manually complete the payment.
        You can also set AutoPay to true based on your business requirements.
        
        @param request: CreateAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
        if not UtilClient.is_unset(request.ipv_6bandwidth):
            query['Ipv6Bandwidth'] = request.ipv_6bandwidth
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.number_of_instances):
            query['NumberOfInstances'] = request.number_of_instances
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_android_instance_group(
        self,
        request: eds_aic_20230930_models.CreateAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.CreateAndroidInstanceGroupResponse:
        """
        @summary Creates pay-as-you-go or subscription instance groups.
        
        @description Before creating an instance group, ensure you understand the [billing methods](https://help.aliyun.com/document_detail/2807121.html) supported by Cloud Phone.
        If the billing method of an instance group is PrePaid, AutoPay is set to false by default. In this case, you need to go to [Expenses and Costs](https://usercenter2-intl.aliyun.com/order/list) to manually complete the payment.
        You can also set AutoPay to true based on your business requirements.
        
        @param request: CreateAndroidInstanceGroupRequest
        @return: CreateAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_android_instance_group_with_options(request, runtime)

    async def create_android_instance_group_async(
        self,
        request: eds_aic_20230930_models.CreateAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.CreateAndroidInstanceGroupResponse:
        """
        @summary Creates pay-as-you-go or subscription instance groups.
        
        @description Before creating an instance group, ensure you understand the [billing methods](https://help.aliyun.com/document_detail/2807121.html) supported by Cloud Phone.
        If the billing method of an instance group is PrePaid, AutoPay is set to false by default. In this case, you need to go to [Expenses and Costs](https://usercenter2-intl.aliyun.com/order/list) to manually complete the payment.
        You can also set AutoPay to true based on your business requirements.
        
        @param request: CreateAndroidInstanceGroupRequest
        @return: CreateAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_android_instance_group_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        tmp_req: eds_aic_20230930_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @summary Creates an Android application.
        
        @description When creating an app, you can provide app information to the system in one of the following ways:
        Way 1: Apps from the Application Center
        You can use one of the following methods:
        Method 1: Pass in the `FileName` and `FilePath` parameters at the same time.
        Method 2: Pass in the `OssAppUrl` parameter
        Rule: If your app is from the Alibaba Cloud Workspace Application Center, you must use either Method 1 or Method 2. If both are used, Method 1 takes priority.
        Condition: Before you proceed, log on to the [Elastic Desktop Service (EDS) Enterprise console](https://eds.console.aliyun.com/osshelp) and follow the on-screen instructions to upload the app file to the Application Center to obtain the values of the `FileName`, `FilePath`, and `OssAppUrl` parameters.
        Way 2: Custom apps
        Pass in the `CustomAppInfo` parameter.
        Rule: If you pass in the `CustomAppInfo` parameter, all six fields within it are required.
        >  If Way 1 and Way 2 are adopted simultaneously, the information from Way 2 takes priority.
        
        @param tmp_req: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_app_info):
            request.custom_app_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_app_info, 'CustomAppInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.custom_app_info_shrink):
            query['CustomAppInfo'] = request.custom_app_info_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not UtilClient.is_unset(request.install_param):
            query['InstallParam'] = request.install_param
        if not UtilClient.is_unset(request.oss_app_url):
            query['OssAppUrl'] = request.oss_app_url
        if not UtilClient.is_unset(request.sign_apk):
            query['SignApk'] = request.sign_apk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @summary Creates an Android application.
        
        @description When creating an app, you can provide app information to the system in one of the following ways:
        Way 1: Apps from the Application Center
        You can use one of the following methods:
        Method 1: Pass in the `FileName` and `FilePath` parameters at the same time.
        Method 2: Pass in the `OssAppUrl` parameter
        Rule: If your app is from the Alibaba Cloud Workspace Application Center, you must use either Method 1 or Method 2. If both are used, Method 1 takes priority.
        Condition: Before you proceed, log on to the [Elastic Desktop Service (EDS) Enterprise console](https://eds.console.aliyun.com/osshelp) and follow the on-screen instructions to upload the app file to the Application Center to obtain the values of the `FileName`, `FilePath`, and `OssAppUrl` parameters.
        Way 2: Custom apps
        Pass in the `CustomAppInfo` parameter.
        Rule: If you pass in the `CustomAppInfo` parameter, all six fields within it are required.
        >  If Way 1 and Way 2 are adopted simultaneously, the information from Way 2 takes priority.
        
        @param tmp_req: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_app_info):
            request.custom_app_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_app_info, 'CustomAppInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.custom_app_info_shrink):
            query['CustomAppInfo'] = request.custom_app_info_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.icon_url):
            query['IconUrl'] = request.icon_url
        if not UtilClient.is_unset(request.install_param):
            query['InstallParam'] = request.install_param
        if not UtilClient.is_unset(request.oss_app_url):
            query['OssAppUrl'] = request.oss_app_url
        if not UtilClient.is_unset(request.sign_apk):
            query['SignApk'] = request.sign_apk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: eds_aic_20230930_models.CreateAppRequest,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @summary Creates an Android application.
        
        @description When creating an app, you can provide app information to the system in one of the following ways:
        Way 1: Apps from the Application Center
        You can use one of the following methods:
        Method 1: Pass in the `FileName` and `FilePath` parameters at the same time.
        Method 2: Pass in the `OssAppUrl` parameter
        Rule: If your app is from the Alibaba Cloud Workspace Application Center, you must use either Method 1 or Method 2. If both are used, Method 1 takes priority.
        Condition: Before you proceed, log on to the [Elastic Desktop Service (EDS) Enterprise console](https://eds.console.aliyun.com/osshelp) and follow the on-screen instructions to upload the app file to the Application Center to obtain the values of the `FileName`, `FilePath`, and `OssAppUrl` parameters.
        Way 2: Custom apps
        Pass in the `CustomAppInfo` parameter.
        Rule: If you pass in the `CustomAppInfo` parameter, all six fields within it are required.
        >  If Way 1 and Way 2 are adopted simultaneously, the information from Way 2 takes priority.
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: eds_aic_20230930_models.CreateAppRequest,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @summary Creates an Android application.
        
        @description When creating an app, you can provide app information to the system in one of the following ways:
        Way 1: Apps from the Application Center
        You can use one of the following methods:
        Method 1: Pass in the `FileName` and `FilePath` parameters at the same time.
        Method 2: Pass in the `OssAppUrl` parameter
        Rule: If your app is from the Alibaba Cloud Workspace Application Center, you must use either Method 1 or Method 2. If both are used, Method 1 takes priority.
        Condition: Before you proceed, log on to the [Elastic Desktop Service (EDS) Enterprise console](https://eds.console.aliyun.com/osshelp) and follow the on-screen instructions to upload the app file to the Application Center to obtain the values of the `FileName`, `FilePath`, and `OssAppUrl` parameters.
        Way 2: Custom apps
        Pass in the `CustomAppInfo` parameter.
        Rule: If you pass in the `CustomAppInfo` parameter, all six fields within it are required.
        >  If Way 1 and Way 2 are adopted simultaneously, the information from Way 2 takes priority.
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_cloud_phone_node_with_options(
        self,
        tmp_req: eds_aic_20230930_models.CreateCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateCloudPhoneNodeResponse:
        """
        @summary Creates a cloud phone matrix.
        
        @param tmp_req: CreateCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudPhoneNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreateCloudPhoneNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.display_config):
            request.display_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not UtilClient.is_unset(request.resolution_height):
            query['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            query['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.server_share_data_volume):
            query['ServerShareDataVolume'] = request.server_share_data_volume
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        body = {}
        if not UtilClient.is_unset(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_phone_node_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.CreateCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateCloudPhoneNodeResponse:
        """
        @summary Creates a cloud phone matrix.
        
        @param tmp_req: CreateCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudPhoneNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreateCloudPhoneNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.display_config):
            request.display_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not UtilClient.is_unset(request.resolution_height):
            query['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            query['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.server_share_data_volume):
            query['ServerShareDataVolume'] = request.server_share_data_volume
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        body = {}
        if not UtilClient.is_unset(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_phone_node(
        self,
        request: eds_aic_20230930_models.CreateCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.CreateCloudPhoneNodeResponse:
        """
        @summary Creates a cloud phone matrix.
        
        @param request: CreateCloudPhoneNodeRequest
        @return: CreateCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_phone_node_with_options(request, runtime)

    async def create_cloud_phone_node_async(
        self,
        request: eds_aic_20230930_models.CreateCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.CreateCloudPhoneNodeResponse:
        """
        @summary Creates a cloud phone matrix.
        
        @param request: CreateCloudPhoneNodeRequest
        @return: CreateCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_phone_node_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: eds_aic_20230930_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateCustomImageResponse:
        """
        @summary Creates a custom image from a cloud phone instance.
        
        @param request: CreateCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: eds_aic_20230930_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateCustomImageResponse:
        """
        @summary Creates a custom image from a cloud phone instance.
        
        @param request: CreateCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_image(
        self,
        request: eds_aic_20230930_models.CreateCustomImageRequest,
    ) -> eds_aic_20230930_models.CreateCustomImageResponse:
        """
        @summary Creates a custom image from a cloud phone instance.
        
        @param request: CreateCustomImageRequest
        @return: CreateCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    async def create_custom_image_async(
        self,
        request: eds_aic_20230930_models.CreateCustomImageRequest,
    ) -> eds_aic_20230930_models.CreateCustomImageResponse:
        """
        @summary Creates a custom image from a cloud phone instance.
        
        @param request: CreateCustomImageRequest
        @return: CreateCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_image_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: eds_aic_20230930_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateKeyPairResponse:
        """
        @summary Creates an Android Debug Bridge (ADB) key pair. The system retains the public key and provides a PEM-encoded private key in PKCS#8 format, adhering to the ADB connection specification. You must securely store the private key.
        
        @description In addition to using the CreateKeyPair operation to generate a key pair, you can also create one by using the ADB tool and upload it to the Cloud Phone console. The usage of this key pair is identical to that of a system-generated key pair.
        Each tenant can create up to 500 key pairs.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: eds_aic_20230930_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateKeyPairResponse:
        """
        @summary Creates an Android Debug Bridge (ADB) key pair. The system retains the public key and provides a PEM-encoded private key in PKCS#8 format, adhering to the ADB connection specification. You must securely store the private key.
        
        @description In addition to using the CreateKeyPair operation to generate a key pair, you can also create one by using the ADB tool and upload it to the Cloud Phone console. The usage of this key pair is identical to that of a system-generated key pair.
        Each tenant can create up to 500 key pairs.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_pair(
        self,
        request: eds_aic_20230930_models.CreateKeyPairRequest,
    ) -> eds_aic_20230930_models.CreateKeyPairResponse:
        """
        @summary Creates an Android Debug Bridge (ADB) key pair. The system retains the public key and provides a PEM-encoded private key in PKCS#8 format, adhering to the ADB connection specification. You must securely store the private key.
        
        @description In addition to using the CreateKeyPair operation to generate a key pair, you can also create one by using the ADB tool and upload it to the Cloud Phone console. The usage of this key pair is identical to that of a system-generated key pair.
        Each tenant can create up to 500 key pairs.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: eds_aic_20230930_models.CreateKeyPairRequest,
    ) -> eds_aic_20230930_models.CreateKeyPairResponse:
        """
        @summary Creates an Android Debug Bridge (ADB) key pair. The system retains the public key and provides a PEM-encoded private key in PKCS#8 format, adhering to the ADB connection specification. You must securely store the private key.
        
        @description In addition to using the CreateKeyPair operation to generate a key pair, you can also create one by using the ADB tool and upload it to the Cloud Phone console. The usage of this key pair is identical to that of a system-generated key pair.
        Each tenant can create up to 500 key pairs.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_policy_group_with_options(
        self,
        tmp_req: eds_aic_20230930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreatePolicyGroupResponse:
        """
        @summary Creates a policy.
        
        @param tmp_req: CreatePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreatePolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not UtilClient.is_unset(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreatePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_group_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreatePolicyGroupResponse:
        """
        @summary Creates a policy.
        
        @param tmp_req: CreatePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreatePolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not UtilClient.is_unset(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreatePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_group(
        self,
        request: eds_aic_20230930_models.CreatePolicyGroupRequest,
    ) -> eds_aic_20230930_models.CreatePolicyGroupResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyGroupRequest
        @return: CreatePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    async def create_policy_group_async(
        self,
        request: eds_aic_20230930_models.CreatePolicyGroupRequest,
    ) -> eds_aic_20230930_models.CreatePolicyGroupResponse:
        """
        @summary Creates a policy.
        
        @param request: CreatePolicyGroupRequest
        @return: CreatePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def create_screenshot_with_options(
        self,
        request: eds_aic_20230930_models.CreateScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateScreenshotResponse:
        """
        @summary Creates a screenshot of a cloud phone instance.
        
        @description You can call this operation to create a screenshot of a cloud phone instance and upload it to the default Object Storage Service (OSS) bucket. The operation returns a task ID, which you can use with the DescribeTasks operation to get the download link for the screenshot.
        
        @param request: CreateScreenshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScreenshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.skip_check_policy_config):
            query['SkipCheckPolicyConfig'] = request.skip_check_policy_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScreenshot',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateScreenshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_screenshot_with_options_async(
        self,
        request: eds_aic_20230930_models.CreateScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateScreenshotResponse:
        """
        @summary Creates a screenshot of a cloud phone instance.
        
        @description You can call this operation to create a screenshot of a cloud phone instance and upload it to the default Object Storage Service (OSS) bucket. The operation returns a task ID, which you can use with the DescribeTasks operation to get the download link for the screenshot.
        
        @param request: CreateScreenshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScreenshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.skip_check_policy_config):
            query['SkipCheckPolicyConfig'] = request.skip_check_policy_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScreenshot',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.CreateScreenshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_screenshot(
        self,
        request: eds_aic_20230930_models.CreateScreenshotRequest,
    ) -> eds_aic_20230930_models.CreateScreenshotResponse:
        """
        @summary Creates a screenshot of a cloud phone instance.
        
        @description You can call this operation to create a screenshot of a cloud phone instance and upload it to the default Object Storage Service (OSS) bucket. The operation returns a task ID, which you can use with the DescribeTasks operation to get the download link for the screenshot.
        
        @param request: CreateScreenshotRequest
        @return: CreateScreenshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_screenshot_with_options(request, runtime)

    async def create_screenshot_async(
        self,
        request: eds_aic_20230930_models.CreateScreenshotRequest,
    ) -> eds_aic_20230930_models.CreateScreenshotResponse:
        """
        @summary Creates a screenshot of a cloud phone instance.
        
        @description You can call this operation to create a screenshot of a cloud phone instance and upload it to the default Object Storage Service (OSS) bucket. The operation returns a task ID, which you can use with the DescribeTasks operation to get the download link for the screenshot.
        
        @param request: CreateScreenshotRequest
        @return: CreateScreenshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_screenshot_with_options_async(request, runtime)

    def delete_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.DeleteAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse:
        """
        @summary Delete an instance group.
        
        @description You can delete only pay-as-you-go instance groups.
        You can delete subscription instance groups only after they expire.
        
        @param request: DeleteAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_android_instance_group_with_options_async(
        self,
        request: eds_aic_20230930_models.DeleteAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse:
        """
        @summary Delete an instance group.
        
        @description You can delete only pay-as-you-go instance groups.
        You can delete subscription instance groups only after they expire.
        
        @param request: DeleteAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_android_instance_group(
        self,
        request: eds_aic_20230930_models.DeleteAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse:
        """
        @summary Delete an instance group.
        
        @description You can delete only pay-as-you-go instance groups.
        You can delete subscription instance groups only after they expire.
        
        @param request: DeleteAndroidInstanceGroupRequest
        @return: DeleteAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_android_instance_group_with_options(request, runtime)

    async def delete_android_instance_group_async(
        self,
        request: eds_aic_20230930_models.DeleteAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse:
        """
        @summary Delete an instance group.
        
        @description You can delete only pay-as-you-go instance groups.
        You can delete subscription instance groups only after they expire.
        
        @param request: DeleteAndroidInstanceGroupRequest
        @return: DeleteAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_android_instance_group_with_options_async(request, runtime)

    def delete_apps_with_options(
        self,
        request: eds_aic_20230930_models.DeleteAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteAppsResponse:
        """
        @summary Deletes an application. Before you delete an application, make sure that the application is not installed on any instances.
        
        @param request: DeleteAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApps',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apps_with_options_async(
        self,
        request: eds_aic_20230930_models.DeleteAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteAppsResponse:
        """
        @summary Deletes an application. Before you delete an application, make sure that the application is not installed on any instances.
        
        @param request: DeleteAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApps',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apps(
        self,
        request: eds_aic_20230930_models.DeleteAppsRequest,
    ) -> eds_aic_20230930_models.DeleteAppsResponse:
        """
        @summary Deletes an application. Before you delete an application, make sure that the application is not installed on any instances.
        
        @param request: DeleteAppsRequest
        @return: DeleteAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_apps_with_options(request, runtime)

    async def delete_apps_async(
        self,
        request: eds_aic_20230930_models.DeleteAppsRequest,
    ) -> eds_aic_20230930_models.DeleteAppsResponse:
        """
        @summary Deletes an application. Before you delete an application, make sure that the application is not installed on any instances.
        
        @param request: DeleteAppsRequest
        @return: DeleteAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_apps_with_options_async(request, runtime)

    def delete_cloud_phone_nodes_with_options(
        self,
        request: eds_aic_20230930_models.DeleteCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteCloudPhoneNodesResponse:
        """
        @summary Deletes a cloud phone matrix.
        
        @description Before you proceed, make sure that the cloud phone matrix that you want to delete expired.
        
        @param request: DeleteCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_phone_nodes_with_options_async(
        self,
        request: eds_aic_20230930_models.DeleteCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteCloudPhoneNodesResponse:
        """
        @summary Deletes a cloud phone matrix.
        
        @description Before you proceed, make sure that the cloud phone matrix that you want to delete expired.
        
        @param request: DeleteCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_phone_nodes(
        self,
        request: eds_aic_20230930_models.DeleteCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.DeleteCloudPhoneNodesResponse:
        """
        @summary Deletes a cloud phone matrix.
        
        @description Before you proceed, make sure that the cloud phone matrix that you want to delete expired.
        
        @param request: DeleteCloudPhoneNodesRequest
        @return: DeleteCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_phone_nodes_with_options(request, runtime)

    async def delete_cloud_phone_nodes_async(
        self,
        request: eds_aic_20230930_models.DeleteCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.DeleteCloudPhoneNodesResponse:
        """
        @summary Deletes a cloud phone matrix.
        
        @description Before you proceed, make sure that the cloud phone matrix that you want to delete expired.
        
        @param request: DeleteCloudPhoneNodesRequest
        @return: DeleteCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_phone_nodes_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        tmp_req: eds_aic_20230930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteImagesResponse:
        """
        @summary Deletes a custom image.
        
        @description You cannot delete an image that is currently in use by an instance group.
        
        @param tmp_req: DeleteImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.DeleteImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_ids):
            request.image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_ids_shrink):
            body['ImageIds'] = request.image_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteImagesResponse:
        """
        @summary Deletes a custom image.
        
        @description You cannot delete an image that is currently in use by an instance group.
        
        @param tmp_req: DeleteImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.DeleteImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_ids):
            request.image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.image_ids_shrink):
            body['ImageIds'] = request.image_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images(
        self,
        request: eds_aic_20230930_models.DeleteImagesRequest,
    ) -> eds_aic_20230930_models.DeleteImagesResponse:
        """
        @summary Deletes a custom image.
        
        @description You cannot delete an image that is currently in use by an instance group.
        
        @param request: DeleteImagesRequest
        @return: DeleteImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: eds_aic_20230930_models.DeleteImagesRequest,
    ) -> eds_aic_20230930_models.DeleteImagesResponse:
        """
        @summary Deletes a custom image.
        
        @description You cannot delete an image that is currently in use by an instance group.
        
        @param request: DeleteImagesRequest
        @return: DeleteImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: eds_aic_20230930_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteKeyPairsResponse:
        """
        @summary Deletes Android Debug Bridge (ADB) key pairs.
        
        @description    If a cloud phone instance is currently associated with the ADB key pair you intend to delete, the ADB key pair cannot be deleted.
        Once an ADB key pair is deleted, it cannot be retrieved or queried by using the DescribeKeyPairs operation.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: eds_aic_20230930_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteKeyPairsResponse:
        """
        @summary Deletes Android Debug Bridge (ADB) key pairs.
        
        @description    If a cloud phone instance is currently associated with the ADB key pair you intend to delete, the ADB key pair cannot be deleted.
        Once an ADB key pair is deleted, it cannot be retrieved or queried by using the DescribeKeyPairs operation.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: eds_aic_20230930_models.DeleteKeyPairsRequest,
    ) -> eds_aic_20230930_models.DeleteKeyPairsResponse:
        """
        @summary Deletes Android Debug Bridge (ADB) key pairs.
        
        @description    If a cloud phone instance is currently associated with the ADB key pair you intend to delete, the ADB key pair cannot be deleted.
        Once an ADB key pair is deleted, it cannot be retrieved or queried by using the DescribeKeyPairs operation.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: eds_aic_20230930_models.DeleteKeyPairsRequest,
    ) -> eds_aic_20230930_models.DeleteKeyPairsResponse:
        """
        @summary Deletes Android Debug Bridge (ADB) key pairs.
        
        @description    If a cloud phone instance is currently associated with the ADB key pair you intend to delete, the ADB key pair cannot be deleted.
        Once an ADB key pair is deleted, it cannot be retrieved or queried by using the DescribeKeyPairs operation.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_policy_group_with_options(
        self,
        request: eds_aic_20230930_models.DeletePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeletePolicyGroupResponse:
        """
        @summary Deletes a policy.
        
        @param request: DeletePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeletePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_group_with_options_async(
        self,
        request: eds_aic_20230930_models.DeletePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeletePolicyGroupResponse:
        """
        @summary Deletes a policy.
        
        @param request: DeletePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DeletePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_group(
        self,
        request: eds_aic_20230930_models.DeletePolicyGroupRequest,
    ) -> eds_aic_20230930_models.DeletePolicyGroupResponse:
        """
        @summary Deletes a policy.
        
        @param request: DeletePolicyGroupRequest
        @return: DeletePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_group_with_options(request, runtime)

    async def delete_policy_group_async(
        self,
        request: eds_aic_20230930_models.DeletePolicyGroupRequest,
    ) -> eds_aic_20230930_models.DeletePolicyGroupResponse:
        """
        @summary Deletes a policy.
        
        @param request: DeletePolicyGroupRequest
        @return: DeletePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_group_with_options_async(request, runtime)

    def describe_android_instance_groups_with_options(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstanceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse:
        """
        @summary Queries the details of an instance group.
        
        @param request: DescribeAndroidInstanceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAndroidInstanceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAndroidInstanceGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_android_instance_groups_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstanceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse:
        """
        @summary Queries the details of an instance group.
        
        @param request: DescribeAndroidInstanceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAndroidInstanceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAndroidInstanceGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_android_instance_groups(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstanceGroupsRequest,
    ) -> eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse:
        """
        @summary Queries the details of an instance group.
        
        @param request: DescribeAndroidInstanceGroupsRequest
        @return: DescribeAndroidInstanceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_android_instance_groups_with_options(request, runtime)

    async def describe_android_instance_groups_async(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstanceGroupsRequest,
    ) -> eds_aic_20230930_models.DescribeAndroidInstanceGroupsResponse:
        """
        @summary Queries the details of an instance group.
        
        @param request: DescribeAndroidInstanceGroupsRequest
        @return: DescribeAndroidInstanceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_android_instance_groups_with_options_async(request, runtime)

    def describe_android_instances_with_options(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAndroidInstancesResponse:
        """
        @summary Queries cloud phone instances.
        
        @param request: DescribeAndroidInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAndroidInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not UtilClient.is_unset(request.app_manage_policy_id):
            query['AppManagePolicyId'] = request.app_manage_policy_id
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not UtilClient.is_unset(request.qos_rule_ids):
            query['QosRuleIds'] = request.qos_rule_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAndroidInstances',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAndroidInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_android_instances_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAndroidInstancesResponse:
        """
        @summary Queries cloud phone instances.
        
        @param request: DescribeAndroidInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAndroidInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not UtilClient.is_unset(request.app_manage_policy_id):
            query['AppManagePolicyId'] = request.app_manage_policy_id
        if not UtilClient.is_unset(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not UtilClient.is_unset(request.qos_rule_ids):
            query['QosRuleIds'] = request.qos_rule_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAndroidInstances',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAndroidInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_android_instances(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstancesRequest,
    ) -> eds_aic_20230930_models.DescribeAndroidInstancesResponse:
        """
        @summary Queries cloud phone instances.
        
        @param request: DescribeAndroidInstancesRequest
        @return: DescribeAndroidInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_android_instances_with_options(request, runtime)

    async def describe_android_instances_async(
        self,
        request: eds_aic_20230930_models.DescribeAndroidInstancesRequest,
    ) -> eds_aic_20230930_models.DescribeAndroidInstancesResponse:
        """
        @summary Queries cloud phone instances.
        
        @param request: DescribeAndroidInstancesRequest
        @return: DescribeAndroidInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_android_instances_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: eds_aic_20230930_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAppsResponse:
        """
        @summary Queries applications.
        
        @param request: DescribeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.installation_status):
            query['InstallationStatus'] = request.installation_status
        if not UtilClient.is_unset(request.md5):
            query['MD5'] = request.md5
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeAppsResponse:
        """
        @summary Queries applications.
        
        @param request: DescribeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.installation_status):
            query['InstallationStatus'] = request.installation_status
        if not UtilClient.is_unset(request.md5):
            query['MD5'] = request.md5
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: eds_aic_20230930_models.DescribeAppsRequest,
    ) -> eds_aic_20230930_models.DescribeAppsResponse:
        """
        @summary Queries applications.
        
        @param request: DescribeAppsRequest
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: eds_aic_20230930_models.DescribeAppsRequest,
    ) -> eds_aic_20230930_models.DescribeAppsResponse:
        """
        @summary Queries applications.
        
        @param request: DescribeAppsRequest
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_backup_files_with_options(
        self,
        request: eds_aic_20230930_models.DescribeBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeBackupFilesResponse:
        """
        @summary Queries backup files.
        
        @description Currently, this operation allows you to query only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: DescribeBackupFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not UtilClient.is_unset(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not UtilClient.is_unset(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupFiles',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_files_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeBackupFilesResponse:
        """
        @summary Queries backup files.
        
        @description Currently, this operation allows you to query only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: DescribeBackupFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not UtilClient.is_unset(request.android_instance_name):
            query['AndroidInstanceName'] = request.android_instance_name
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not UtilClient.is_unset(request.backup_file_name):
            query['BackupFileName'] = request.backup_file_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupFiles',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_files(
        self,
        request: eds_aic_20230930_models.DescribeBackupFilesRequest,
    ) -> eds_aic_20230930_models.DescribeBackupFilesResponse:
        """
        @summary Queries backup files.
        
        @description Currently, this operation allows you to query only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: DescribeBackupFilesRequest
        @return: DescribeBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_files_with_options(request, runtime)

    async def describe_backup_files_async(
        self,
        request: eds_aic_20230930_models.DescribeBackupFilesRequest,
    ) -> eds_aic_20230930_models.DescribeBackupFilesResponse:
        """
        @summary Queries backup files.
        
        @description Currently, this operation allows you to query only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: DescribeBackupFilesRequest
        @return: DescribeBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_files_with_options_async(request, runtime)

    def describe_cloud_phone_nodes_with_options(
        self,
        request: eds_aic_20230930_models.DescribeCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeCloudPhoneNodesResponse:
        """
        @summary Queries the details of a cloud phone matrix.
        
        @param request: DescribeCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_phone_nodes_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeCloudPhoneNodesResponse:
        """
        @summary Queries the details of a cloud phone matrix.
        
        @param request: DescribeCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_phone_nodes(
        self,
        request: eds_aic_20230930_models.DescribeCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.DescribeCloudPhoneNodesResponse:
        """
        @summary Queries the details of a cloud phone matrix.
        
        @param request: DescribeCloudPhoneNodesRequest
        @return: DescribeCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_phone_nodes_with_options(request, runtime)

    async def describe_cloud_phone_nodes_async(
        self,
        request: eds_aic_20230930_models.DescribeCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.DescribeCloudPhoneNodesResponse:
        """
        @summary Queries the details of a cloud phone matrix.
        
        @param request: DescribeCloudPhoneNodesRequest
        @return: DescribeCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_phone_nodes_with_options_async(request, runtime)

    def describe_display_config_with_options(
        self,
        request: eds_aic_20230930_models.DescribeDisplayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeDisplayConfigResponse:
        """
        @summary 查询显示设置
        
        @param request: DescribeDisplayConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisplayConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisplayConfig',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeDisplayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_display_config_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeDisplayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeDisplayConfigResponse:
        """
        @summary 查询显示设置
        
        @param request: DescribeDisplayConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDisplayConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisplayConfig',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeDisplayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_display_config(
        self,
        request: eds_aic_20230930_models.DescribeDisplayConfigRequest,
    ) -> eds_aic_20230930_models.DescribeDisplayConfigResponse:
        """
        @summary 查询显示设置
        
        @param request: DescribeDisplayConfigRequest
        @return: DescribeDisplayConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_display_config_with_options(request, runtime)

    async def describe_display_config_async(
        self,
        request: eds_aic_20230930_models.DescribeDisplayConfigRequest,
    ) -> eds_aic_20230930_models.DescribeDisplayConfigResponse:
        """
        @summary 查询显示设置
        
        @param request: DescribeDisplayConfigRequest
        @return: DescribeDisplayConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_display_config_with_options_async(request, runtime)

    def describe_image_list_with_options(
        self,
        request: eds_aic_20230930_models.DescribeImageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeImageListResponse:
        """
        @summary Queries images.
        
        @param request: DescribeImageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_package_type):
            query['ImagePackageType'] = request.image_package_type
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_type):
            body['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImageList',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeImageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_list_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeImageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeImageListResponse:
        """
        @summary Queries images.
        
        @param request: DescribeImageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_package_type):
            query['ImagePackageType'] = request.image_package_type
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_type):
            body['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImageList',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeImageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_list(
        self,
        request: eds_aic_20230930_models.DescribeImageListRequest,
    ) -> eds_aic_20230930_models.DescribeImageListResponse:
        """
        @summary Queries images.
        
        @param request: DescribeImageListRequest
        @return: DescribeImageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_list_with_options(request, runtime)

    async def describe_image_list_async(
        self,
        request: eds_aic_20230930_models.DescribeImageListRequest,
    ) -> eds_aic_20230930_models.DescribeImageListResponse:
        """
        @summary Queries images.
        
        @param request: DescribeImageListRequest
        @return: DescribeImageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_list_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: eds_aic_20230930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution results of commands.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.invocation_id):
            query['InvocationId'] = request.invocation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution results of commands.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.invocation_id):
            query['InvocationId'] = request.invocation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: eds_aic_20230930_models.DescribeInvocationsRequest,
    ) -> eds_aic_20230930_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution results of commands.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: eds_aic_20230930_models.DescribeInvocationsRequest,
    ) -> eds_aic_20230930_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution results of commands.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_key_pairs_with_options(
        self,
        request: eds_aic_20230930_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeKeyPairsResponse:
        """
        @summary Queries one or more key pairs.
        
        @param request: DescribeKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyPairs',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_pairs_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeKeyPairsResponse:
        """
        @summary Queries one or more key pairs.
        
        @param request: DescribeKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_ids):
            query['KeyPairIds'] = request.key_pair_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyPairs',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key_pairs(
        self,
        request: eds_aic_20230930_models.DescribeKeyPairsRequest,
    ) -> eds_aic_20230930_models.DescribeKeyPairsResponse:
        """
        @summary Queries one or more key pairs.
        
        @param request: DescribeKeyPairsRequest
        @return: DescribeKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    async def describe_key_pairs_async(
        self,
        request: eds_aic_20230930_models.DescribeKeyPairsRequest,
    ) -> eds_aic_20230930_models.DescribeKeyPairsResponse:
        """
        @summary Queries one or more key pairs.
        
        @param request: DescribeKeyPairsRequest
        @return: DescribeKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_pairs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: eds_aic_20230930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeRegionsResponse:
        """
        @summary Query available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeRegionsResponse:
        """
        @summary Query available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: eds_aic_20230930_models.DescribeRegionsRequest,
    ) -> eds_aic_20230930_models.DescribeRegionsResponse:
        """
        @summary Query available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: eds_aic_20230930_models.DescribeRegionsRequest,
    ) -> eds_aic_20230930_models.DescribeRegionsResponse:
        """
        @summary Query available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_spec_with_options(
        self,
        request: eds_aic_20230930_models.DescribeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeSpecResponse:
        """
        @summary Query available specifications.
        
        @param request: DescribeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.matrix_spec):
            query['MatrixSpec'] = request.matrix_spec
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.spec_ids):
            query['SpecIds'] = request.spec_ids
        if not UtilClient.is_unset(request.spec_status):
            query['SpecStatus'] = request.spec_status
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpec',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spec_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeSpecResponse:
        """
        @summary Query available specifications.
        
        @param request: DescribeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.matrix_spec):
            query['MatrixSpec'] = request.matrix_spec
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.spec_ids):
            query['SpecIds'] = request.spec_ids
        if not UtilClient.is_unset(request.spec_status):
            query['SpecStatus'] = request.spec_status
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpec',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spec(
        self,
        request: eds_aic_20230930_models.DescribeSpecRequest,
    ) -> eds_aic_20230930_models.DescribeSpecResponse:
        """
        @summary Query available specifications.
        
        @param request: DescribeSpecRequest
        @return: DescribeSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_spec_with_options(request, runtime)

    async def describe_spec_async(
        self,
        request: eds_aic_20230930_models.DescribeSpecRequest,
    ) -> eds_aic_20230930_models.DescribeSpecResponse:
        """
        @summary Query available specifications.
        
        @param request: DescribeSpecRequest
        @return: DescribeSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_spec_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: eds_aic_20230930_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeTasksResponse:
        """
        @summary Queries tasks created for a cloud phone instance.
        
        @description    You can call the DescribeTasks operation to query the tasks created for one or more cloud phone instances.
        The system currently supports various tasks, including starting, stopping, restarting, and resetting cloud phone instances; backing up and restoring data; installing apps; and executing remote commands.
        You can use the Level field to specify the type of task. If Level is set to 1, it represents a batch task. If Level is set to 2, it represents an instance-level task.
        *Example**\
        Assume you restart two cloud phone instances with the instance IDs acp-25nt4kk9whhok\\\\*\\*\\* and acp-j2taq887orj8l\\*\\*\\*\\*, and the returned request ID is B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you want to check the operation outcomes of the two cloud phone instances, you can call the DescribeTasks operation. You need to set the InvokeId request parameter to B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you only want to check the cloud phone instance with the ID acp-25nt4kk9whhok\\*\\*\\*\\*, you must set the ParentTaskId request parameter to the ID of the batch task and the AndroidInstanceId request parameter to acp-25nt4kk9whhok\\*\\*\\*\\* when calling the DescribeTasks operation.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_statuses):
            query['TaskStatuses'] = request.task_statuses
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_types):
            query['TaskTypes'] = request.task_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: eds_aic_20230930_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeTasksResponse:
        """
        @summary Queries tasks created for a cloud phone instance.
        
        @description    You can call the DescribeTasks operation to query the tasks created for one or more cloud phone instances.
        The system currently supports various tasks, including starting, stopping, restarting, and resetting cloud phone instances; backing up and restoring data; installing apps; and executing remote commands.
        You can use the Level field to specify the type of task. If Level is set to 1, it represents a batch task. If Level is set to 2, it represents an instance-level task.
        *Example**\
        Assume you restart two cloud phone instances with the instance IDs acp-25nt4kk9whhok\\\\*\\*\\* and acp-j2taq887orj8l\\*\\*\\*\\*, and the returned request ID is B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you want to check the operation outcomes of the two cloud phone instances, you can call the DescribeTasks operation. You need to set the InvokeId request parameter to B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you only want to check the cloud phone instance with the ID acp-25nt4kk9whhok\\*\\*\\*\\*, you must set the ParentTaskId request parameter to the ID of the batch task and the AndroidInstanceId request parameter to acp-25nt4kk9whhok\\*\\*\\*\\* when calling the DescribeTasks operation.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_statuses):
            query['TaskStatuses'] = request.task_statuses
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_types):
            query['TaskTypes'] = request.task_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: eds_aic_20230930_models.DescribeTasksRequest,
    ) -> eds_aic_20230930_models.DescribeTasksResponse:
        """
        @summary Queries tasks created for a cloud phone instance.
        
        @description    You can call the DescribeTasks operation to query the tasks created for one or more cloud phone instances.
        The system currently supports various tasks, including starting, stopping, restarting, and resetting cloud phone instances; backing up and restoring data; installing apps; and executing remote commands.
        You can use the Level field to specify the type of task. If Level is set to 1, it represents a batch task. If Level is set to 2, it represents an instance-level task.
        *Example**\
        Assume you restart two cloud phone instances with the instance IDs acp-25nt4kk9whhok\\\\*\\*\\* and acp-j2taq887orj8l\\*\\*\\*\\*, and the returned request ID is B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you want to check the operation outcomes of the two cloud phone instances, you can call the DescribeTasks operation. You need to set the InvokeId request parameter to B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you only want to check the cloud phone instance with the ID acp-25nt4kk9whhok\\*\\*\\*\\*, you must set the ParentTaskId request parameter to the ID of the batch task and the AndroidInstanceId request parameter to acp-25nt4kk9whhok\\*\\*\\*\\* when calling the DescribeTasks operation.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: eds_aic_20230930_models.DescribeTasksRequest,
    ) -> eds_aic_20230930_models.DescribeTasksResponse:
        """
        @summary Queries tasks created for a cloud phone instance.
        
        @description    You can call the DescribeTasks operation to query the tasks created for one or more cloud phone instances.
        The system currently supports various tasks, including starting, stopping, restarting, and resetting cloud phone instances; backing up and restoring data; installing apps; and executing remote commands.
        You can use the Level field to specify the type of task. If Level is set to 1, it represents a batch task. If Level is set to 2, it represents an instance-level task.
        *Example**\
        Assume you restart two cloud phone instances with the instance IDs acp-25nt4kk9whhok\\\\*\\*\\* and acp-j2taq887orj8l\\*\\*\\*\\*, and the returned request ID is B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you want to check the operation outcomes of the two cloud phone instances, you can call the DescribeTasks operation. You need to set the InvokeId request parameter to B8ED2BA9-0C6A-5643-818F-B5D60A64\\*\\*\\*\\*. If you only want to check the cloud phone instance with the ID acp-25nt4kk9whhok\\*\\*\\*\\*, you must set the ParentTaskId request parameter to the ID of the batch task and the AndroidInstanceId request parameter to acp-25nt4kk9whhok\\*\\*\\*\\* when calling the DescribeTasks operation.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: eds_aic_20230930_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DetachKeyPairResponse:
        """
        @summary Detaches an Android Debug Bridge (ADB) key pair from one or more cloud phone instances.
        
        @description    After you detach an ADB key pair from a cloud phone instance, the ADB connection will fail. This occurs because the system can no longer authenticate using a valid ADB public key, leading to authentication errors.
        
        @param request: DetachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DetachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: eds_aic_20230930_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DetachKeyPairResponse:
        """
        @summary Detaches an Android Debug Bridge (ADB) key pair from one or more cloud phone instances.
        
        @description    After you detach an ADB key pair from a cloud phone instance, the ADB connection will fail. This occurs because the system can no longer authenticate using a valid ADB public key, leading to authentication errors.
        
        @param request: DetachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DetachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_key_pair(
        self,
        request: eds_aic_20230930_models.DetachKeyPairRequest,
    ) -> eds_aic_20230930_models.DetachKeyPairResponse:
        """
        @summary Detaches an Android Debug Bridge (ADB) key pair from one or more cloud phone instances.
        
        @description    After you detach an ADB key pair from a cloud phone instance, the ADB connection will fail. This occurs because the system can no longer authenticate using a valid ADB public key, leading to authentication errors.
        
        @param request: DetachKeyPairRequest
        @return: DetachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: eds_aic_20230930_models.DetachKeyPairRequest,
    ) -> eds_aic_20230930_models.DetachKeyPairResponse:
        """
        @summary Detaches an Android Debug Bridge (ADB) key pair from one or more cloud phone instances.
        
        @description    After you detach an ADB key pair from a cloud phone instance, the ADB connection will fail. This occurs because the system can no longer authenticate using a valid ADB public key, leading to authentication errors.
        
        @param request: DetachKeyPairRequest
        @return: DetachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def disconnect_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.DisconnectAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DisconnectAndroidInstanceResponse:
        """
        @summary 实例断开连接
        
        @param request: DisconnectAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisconnectAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisconnectAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DisconnectAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disconnect_android_instance_with_options_async(
        self,
        request: eds_aic_20230930_models.DisconnectAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DisconnectAndroidInstanceResponse:
        """
        @summary 实例断开连接
        
        @param request: DisconnectAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisconnectAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisconnectAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DisconnectAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disconnect_android_instance(
        self,
        request: eds_aic_20230930_models.DisconnectAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.DisconnectAndroidInstanceResponse:
        """
        @summary 实例断开连接
        
        @param request: DisconnectAndroidInstanceRequest
        @return: DisconnectAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disconnect_android_instance_with_options(request, runtime)

    async def disconnect_android_instance_async(
        self,
        request: eds_aic_20230930_models.DisconnectAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.DisconnectAndroidInstanceResponse:
        """
        @summary 实例断开连接
        
        @param request: DisconnectAndroidInstanceRequest
        @return: DisconnectAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disconnect_android_instance_with_options_async(request, runtime)

    def distribute_image_with_options(
        self,
        request: eds_aic_20230930_models.DistributeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DistributeImageResponse:
        """
        @summary Distributes an image.
        
        @description After you distribute an image in supported regions, the distribution cannot be canceled.
        
        @param request: DistributeImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DistributeImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribute_region_list):
            body['DistributeRegionList'] = request.distribute_region_list
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DistributeImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DistributeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def distribute_image_with_options_async(
        self,
        request: eds_aic_20230930_models.DistributeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DistributeImageResponse:
        """
        @summary Distributes an image.
        
        @description After you distribute an image in supported regions, the distribution cannot be canceled.
        
        @param request: DistributeImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DistributeImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distribute_region_list):
            body['DistributeRegionList'] = request.distribute_region_list
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DistributeImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DistributeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def distribute_image(
        self,
        request: eds_aic_20230930_models.DistributeImageRequest,
    ) -> eds_aic_20230930_models.DistributeImageResponse:
        """
        @summary Distributes an image.
        
        @description After you distribute an image in supported regions, the distribution cannot be canceled.
        
        @param request: DistributeImageRequest
        @return: DistributeImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.distribute_image_with_options(request, runtime)

    async def distribute_image_async(
        self,
        request: eds_aic_20230930_models.DistributeImageRequest,
    ) -> eds_aic_20230930_models.DistributeImageResponse:
        """
        @summary Distributes an image.
        
        @description After you distribute an image in supported regions, the distribution cannot be canceled.
        
        @param request: DistributeImageRequest
        @return: DistributeImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.distribute_image_with_options_async(request, runtime)

    def downgrade_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.DowngradeAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse:
        """
        @summary Downgrades an instance group. Currently, this operation allows you to only delete specific cloud phone instances from an instance group.
        
        @description This operation only allows you to scale down an instance group.
        
        @param request: DowngradeAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_android_instance_group_with_options_async(
        self,
        request: eds_aic_20230930_models.DowngradeAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse:
        """
        @summary Downgrades an instance group. Currently, this operation allows you to only delete specific cloud phone instances from an instance group.
        
        @description This operation only allows you to scale down an instance group.
        
        @param request: DowngradeAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_android_instance_group(
        self,
        request: eds_aic_20230930_models.DowngradeAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse:
        """
        @summary Downgrades an instance group. Currently, this operation allows you to only delete specific cloud phone instances from an instance group.
        
        @description This operation only allows you to scale down an instance group.
        
        @param request: DowngradeAndroidInstanceGroupRequest
        @return: DowngradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.downgrade_android_instance_group_with_options(request, runtime)

    async def downgrade_android_instance_group_async(
        self,
        request: eds_aic_20230930_models.DowngradeAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.DowngradeAndroidInstanceGroupResponse:
        """
        @summary Downgrades an instance group. Currently, this operation allows you to only delete specific cloud phone instances from an instance group.
        
        @description This operation only allows you to scale down an instance group.
        
        @param request: DowngradeAndroidInstanceGroupRequest
        @return: DowngradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.downgrade_android_instance_group_with_options_async(request, runtime)

    def end_coordination_with_options(
        self,
        request: eds_aic_20230930_models.EndCoordinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.EndCoordinationResponse:
        """
        @summary 结束协同
        
        @param request: EndCoordinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndCoordinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coordinator_user_id):
            query['CoordinatorUserId'] = request.coordinator_user_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndCoordination',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.EndCoordinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_coordination_with_options_async(
        self,
        request: eds_aic_20230930_models.EndCoordinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.EndCoordinationResponse:
        """
        @summary 结束协同
        
        @param request: EndCoordinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndCoordinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coordinator_user_id):
            query['CoordinatorUserId'] = request.coordinator_user_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndCoordination',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.EndCoordinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_coordination(
        self,
        request: eds_aic_20230930_models.EndCoordinationRequest,
    ) -> eds_aic_20230930_models.EndCoordinationResponse:
        """
        @summary 结束协同
        
        @param request: EndCoordinationRequest
        @return: EndCoordinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.end_coordination_with_options(request, runtime)

    async def end_coordination_async(
        self,
        request: eds_aic_20230930_models.EndCoordinationRequest,
    ) -> eds_aic_20230930_models.EndCoordinationResponse:
        """
        @summary 结束协同
        
        @param request: EndCoordinationRequest
        @return: EndCoordinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.end_coordination_with_options_async(request, runtime)

    def expand_data_volume_with_options(
        self,
        request: eds_aic_20230930_models.ExpandDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ExpandDataVolumeResponse:
        """
        @summary 存储扩容
        
        @param request: ExpandDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExpandDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandDataVolume',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ExpandDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_data_volume_with_options_async(
        self,
        request: eds_aic_20230930_models.ExpandDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ExpandDataVolumeResponse:
        """
        @summary 存储扩容
        
        @param request: ExpandDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExpandDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.share_data_volume):
            query['ShareDataVolume'] = request.share_data_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpandDataVolume',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ExpandDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_data_volume(
        self,
        request: eds_aic_20230930_models.ExpandDataVolumeRequest,
    ) -> eds_aic_20230930_models.ExpandDataVolumeResponse:
        """
        @summary 存储扩容
        
        @param request: ExpandDataVolumeRequest
        @return: ExpandDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.expand_data_volume_with_options(request, runtime)

    async def expand_data_volume_async(
        self,
        request: eds_aic_20230930_models.ExpandDataVolumeRequest,
    ) -> eds_aic_20230930_models.ExpandDataVolumeResponse:
        """
        @summary 存储扩容
        
        @param request: ExpandDataVolumeRequest
        @return: ExpandDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.expand_data_volume_with_options_async(request, runtime)

    def fetch_file_with_options(
        self,
        request: eds_aic_20230930_models.FetchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.FetchFileResponse:
        """
        @summary Pulls a file from a cloud phone instance and stores it in Object Storage Service (OSS).
        
        @description Currently, this operation allows you to retrieve files or folders from cloud phone instances and save them directly to OSS.
        
        @param request: FetchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        if not UtilClient.is_unset(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.FetchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_file_with_options_async(
        self,
        request: eds_aic_20230930_models.FetchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.FetchFileResponse:
        """
        @summary Pulls a file from a cloud phone instance and stores it in Object Storage Service (OSS).
        
        @description Currently, this operation allows you to retrieve files or folders from cloud phone instances and save them directly to OSS.
        
        @param request: FetchFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        if not UtilClient.is_unset(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.FetchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_file(
        self,
        request: eds_aic_20230930_models.FetchFileRequest,
    ) -> eds_aic_20230930_models.FetchFileResponse:
        """
        @summary Pulls a file from a cloud phone instance and stores it in Object Storage Service (OSS).
        
        @description Currently, this operation allows you to retrieve files or folders from cloud phone instances and save them directly to OSS.
        
        @param request: FetchFileRequest
        @return: FetchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_file_with_options(request, runtime)

    async def fetch_file_async(
        self,
        request: eds_aic_20230930_models.FetchFileRequest,
    ) -> eds_aic_20230930_models.FetchFileResponse:
        """
        @summary Pulls a file from a cloud phone instance and stores it in Object Storage Service (OSS).
        
        @description Currently, this operation allows you to retrieve files or folders from cloud phone instances and save them directly to OSS.
        
        @param request: FetchFileRequest
        @return: FetchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_file_with_options_async(request, runtime)

    def generate_coordination_code_with_options(
        self,
        request: eds_aic_20230930_models.GenerateCoordinationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.GenerateCoordinationCodeResponse:
        """
        @summary Generates a collaboration code for the cloud phone being accessed by using the current convenience account, and shares this code with other convenience accounts to allow them to access the same cloud phone.
        
        @description You can call this operation to generate a collaboration code for a cloud phone accessed by your current account and share this code with other convenience users to allow them to access the same cloud phone over the desktop, mobile, or web client.
        
        @param request: GenerateCoordinationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCoordinationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateCoordinationCode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.GenerateCoordinationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_coordination_code_with_options_async(
        self,
        request: eds_aic_20230930_models.GenerateCoordinationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.GenerateCoordinationCodeResponse:
        """
        @summary Generates a collaboration code for the cloud phone being accessed by using the current convenience account, and shares this code with other convenience accounts to allow them to access the same cloud phone.
        
        @description You can call this operation to generate a collaboration code for a cloud phone accessed by your current account and share this code with other convenience users to allow them to access the same cloud phone over the desktop, mobile, or web client.
        
        @param request: GenerateCoordinationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCoordinationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateCoordinationCode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.GenerateCoordinationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_coordination_code(
        self,
        request: eds_aic_20230930_models.GenerateCoordinationCodeRequest,
    ) -> eds_aic_20230930_models.GenerateCoordinationCodeResponse:
        """
        @summary Generates a collaboration code for the cloud phone being accessed by using the current convenience account, and shares this code with other convenience accounts to allow them to access the same cloud phone.
        
        @description You can call this operation to generate a collaboration code for a cloud phone accessed by your current account and share this code with other convenience users to allow them to access the same cloud phone over the desktop, mobile, or web client.
        
        @param request: GenerateCoordinationCodeRequest
        @return: GenerateCoordinationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_coordination_code_with_options(request, runtime)

    async def generate_coordination_code_async(
        self,
        request: eds_aic_20230930_models.GenerateCoordinationCodeRequest,
    ) -> eds_aic_20230930_models.GenerateCoordinationCodeResponse:
        """
        @summary Generates a collaboration code for the cloud phone being accessed by using the current convenience account, and shares this code with other convenience accounts to allow them to access the same cloud phone.
        
        @description You can call this operation to generate a collaboration code for a cloud phone accessed by your current account and share this code with other convenience users to allow them to access the same cloud phone over the desktop, mobile, or web client.
        
        @param request: GenerateCoordinationCodeRequest
        @return: GenerateCoordinationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_coordination_code_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: eds_aic_20230930_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ImportKeyPairResponse:
        """
        @summary Imports the public key of an Android Debug Bridge (ADB) key pair.
        
        @description To avoid authorization errors that could cause ADB connection failures, you must import the public key of an ADB key pair.
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: eds_aic_20230930_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ImportKeyPairResponse:
        """
        @summary Imports the public key of an Android Debug Bridge (ADB) key pair.
        
        @description To avoid authorization errors that could cause ADB connection failures, you must import the public key of an ADB key pair.
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: eds_aic_20230930_models.ImportKeyPairRequest,
    ) -> eds_aic_20230930_models.ImportKeyPairResponse:
        """
        @summary Imports the public key of an Android Debug Bridge (ADB) key pair.
        
        @description To avoid authorization errors that could cause ADB connection failures, you must import the public key of an ADB key pair.
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: eds_aic_20230930_models.ImportKeyPairRequest,
    ) -> eds_aic_20230930_models.ImportKeyPairResponse:
        """
        @summary Imports the public key of an Android Debug Bridge (ADB) key pair.
        
        @description To avoid authorization errors that could cause ADB connection failures, you must import the public key of an ADB key pair.
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def install_app_with_options(
        self,
        request: eds_aic_20230930_models.InstallAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.InstallAppResponse:
        """
        @summary Installs an app on multiple cloud phone instances at the same time.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: InstallAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.InstallAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_app_with_options_async(
        self,
        request: eds_aic_20230930_models.InstallAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.InstallAppResponse:
        """
        @summary Installs an app on multiple cloud phone instances at the same time.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: InstallAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.InstallAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_app(
        self,
        request: eds_aic_20230930_models.InstallAppRequest,
    ) -> eds_aic_20230930_models.InstallAppResponse:
        """
        @summary Installs an app on multiple cloud phone instances at the same time.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: InstallAppRequest
        @return: InstallAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_app_with_options(request, runtime)

    async def install_app_async(
        self,
        request: eds_aic_20230930_models.InstallAppRequest,
    ) -> eds_aic_20230930_models.InstallAppResponse:
        """
        @summary Installs an app on multiple cloud phone instances at the same time.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: InstallAppRequest
        @return: InstallAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_app_with_options_async(request, runtime)

    def list_policy_groups_with_options(
        self,
        request: eds_aic_20230930_models.ListPolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ListPolicyGroupsResponse:
        """
        @summary Queries policies.
        
        @param request: ListPolicyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_ids):
            body['PolicyGroupIds'] = request.policy_group_ids
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPolicyGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ListPolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_groups_with_options_async(
        self,
        request: eds_aic_20230930_models.ListPolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ListPolicyGroupsResponse:
        """
        @summary Queries policies.
        
        @param request: ListPolicyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_ids):
            body['PolicyGroupIds'] = request.policy_group_ids
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPolicyGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ListPolicyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_groups(
        self,
        request: eds_aic_20230930_models.ListPolicyGroupsRequest,
    ) -> eds_aic_20230930_models.ListPolicyGroupsResponse:
        """
        @summary Queries policies.
        
        @param request: ListPolicyGroupsRequest
        @return: ListPolicyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_groups_with_options(request, runtime)

    async def list_policy_groups_async(
        self,
        request: eds_aic_20230930_models.ListPolicyGroupsRequest,
    ) -> eds_aic_20230930_models.ListPolicyGroupsResponse:
        """
        @summary Queries policies.
        
        @param request: ListPolicyGroupsRequest
        @return: ListPolicyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_groups_with_options_async(request, runtime)

    def modify_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceResponse:
        """
        @summary Modifies attributes of a cloud phone instance. Currently, this operation allows you to modify only the name of a cloud phone instance.
        
        @param request: ModifyAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not UtilClient.is_unset(request.new_android_instance_name):
            query['NewAndroidInstanceName'] = request.new_android_instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_android_instance_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceResponse:
        """
        @summary Modifies attributes of a cloud phone instance. Currently, this operation allows you to modify only the name of a cloud phone instance.
        
        @param request: ModifyAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id):
            query['AndroidInstanceId'] = request.android_instance_id
        if not UtilClient.is_unset(request.new_android_instance_name):
            query['NewAndroidInstanceName'] = request.new_android_instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_android_instance(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceResponse:
        """
        @summary Modifies attributes of a cloud phone instance. Currently, this operation allows you to modify only the name of a cloud phone instance.
        
        @param request: ModifyAndroidInstanceRequest
        @return: ModifyAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_android_instance_with_options(request, runtime)

    async def modify_android_instance_async(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceResponse:
        """
        @summary Modifies attributes of a cloud phone instance. Currently, this operation allows you to modify only the name of a cloud phone instance.
        
        @param request: ModifyAndroidInstanceRequest
        @return: ModifyAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_android_instance_with_options_async(request, runtime)

    def modify_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse:
        """
        @summary Modifies attributes of an instance group.
        
        @param request: ModifyAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.new_instance_group_name):
            query['NewInstanceGroupName'] = request.new_instance_group_name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_android_instance_group_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse:
        """
        @summary Modifies attributes of an instance group.
        
        @param request: ModifyAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        if not UtilClient.is_unset(request.new_instance_group_name):
            query['NewInstanceGroupName'] = request.new_instance_group_name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_android_instance_group(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse:
        """
        @summary Modifies attributes of an instance group.
        
        @param request: ModifyAndroidInstanceGroupRequest
        @return: ModifyAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_android_instance_group_with_options(request, runtime)

    async def modify_android_instance_group_async(
        self,
        request: eds_aic_20230930_models.ModifyAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.ModifyAndroidInstanceGroupResponse:
        """
        @summary Modifies attributes of an instance group.
        
        @param request: ModifyAndroidInstanceGroupRequest
        @return: ModifyAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_android_instance_group_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: eds_aic_20230930_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAppResponse:
        """
        @summary Modify attributes of an application.
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon_url):
            query['IconUrl'] = request.icon_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyAppResponse:
        """
        @summary Modify attributes of an application.
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon_url):
            query['IconUrl'] = request.icon_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: eds_aic_20230930_models.ModifyAppRequest,
    ) -> eds_aic_20230930_models.ModifyAppResponse:
        """
        @summary Modify attributes of an application.
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: eds_aic_20230930_models.ModifyAppRequest,
    ) -> eds_aic_20230930_models.ModifyAppResponse:
        """
        @summary Modify attributes of an application.
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_cloud_phone_node_with_options(
        self,
        request: eds_aic_20230930_models.ModifyCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyCloudPhoneNodeResponse:
        """
        @summary Modifies a cloud phone matrix. Currently, you can only modify the name of a cloud phone matrix.
        
        @param request: ModifyCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCloudPhoneNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyCloudPhoneNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_phone_node_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyCloudPhoneNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyCloudPhoneNodeResponse:
        """
        @summary Modifies a cloud phone matrix. Currently, you can only modify the name of a cloud phone matrix.
        
        @param request: ModifyCloudPhoneNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCloudPhoneNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudPhoneNode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyCloudPhoneNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_phone_node(
        self,
        request: eds_aic_20230930_models.ModifyCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.ModifyCloudPhoneNodeResponse:
        """
        @summary Modifies a cloud phone matrix. Currently, you can only modify the name of a cloud phone matrix.
        
        @param request: ModifyCloudPhoneNodeRequest
        @return: ModifyCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_phone_node_with_options(request, runtime)

    async def modify_cloud_phone_node_async(
        self,
        request: eds_aic_20230930_models.ModifyCloudPhoneNodeRequest,
    ) -> eds_aic_20230930_models.ModifyCloudPhoneNodeResponse:
        """
        @summary Modifies a cloud phone matrix. Currently, you can only modify the name of a cloud phone matrix.
        
        @param request: ModifyCloudPhoneNodeRequest
        @return: ModifyCloudPhoneNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cloud_phone_node_with_options_async(request, runtime)

    def modify_display_config_with_options(
        self,
        tmp_req: eds_aic_20230930_models.ModifyDisplayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyDisplayConfigResponse:
        """
        @summary 修改显示设置
        
        @param tmp_req: ModifyDisplayConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDisplayConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyDisplayConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.display_config):
            request.display_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDisplayConfig',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyDisplayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_display_config_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.ModifyDisplayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyDisplayConfigResponse:
        """
        @summary 修改显示设置
        
        @param tmp_req: ModifyDisplayConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDisplayConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyDisplayConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.display_config):
            request.display_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.display_config, 'DisplayConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            body['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.display_config_shrink):
            body['DisplayConfig'] = request.display_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDisplayConfig',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyDisplayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_display_config(
        self,
        request: eds_aic_20230930_models.ModifyDisplayConfigRequest,
    ) -> eds_aic_20230930_models.ModifyDisplayConfigResponse:
        """
        @summary 修改显示设置
        
        @param request: ModifyDisplayConfigRequest
        @return: ModifyDisplayConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_display_config_with_options(request, runtime)

    async def modify_display_config_async(
        self,
        request: eds_aic_20230930_models.ModifyDisplayConfigRequest,
    ) -> eds_aic_20230930_models.ModifyDisplayConfigResponse:
        """
        @summary 修改显示设置
        
        @param request: ModifyDisplayConfigRequest
        @return: ModifyDisplayConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_display_config_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        request: eds_aic_20230930_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyInstanceChargeTypeResponse:
        """
        @summary Modifies the billing method. Currently, this operation only allows you to change the billing method from pay-as-you-go to subscription.
        
        @param request: ModifyInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceChargeType',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyInstanceChargeTypeResponse:
        """
        @summary Modifies the billing method. Currently, this operation only allows you to change the billing method from pay-as-you-go to subscription.
        
        @param request: ModifyInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceChargeType',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: eds_aic_20230930_models.ModifyInstanceChargeTypeRequest,
    ) -> eds_aic_20230930_models.ModifyInstanceChargeTypeResponse:
        """
        @summary Modifies the billing method. Currently, this operation only allows you to change the billing method from pay-as-you-go to subscription.
        
        @param request: ModifyInstanceChargeTypeRequest
        @return: ModifyInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: eds_aic_20230930_models.ModifyInstanceChargeTypeRequest,
    ) -> eds_aic_20230930_models.ModifyInstanceChargeTypeResponse:
        """
        @summary Modifies the billing method. Currently, this operation only allows you to change the billing method from pay-as-you-go to subscription.
        
        @param request: ModifyInstanceChargeTypeRequest
        @return: ModifyInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_key_pair_name_with_options(
        self,
        request: eds_aic_20230930_models.ModifyKeyPairNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyKeyPairNameResponse:
        """
        @summary Modifies Android Debug Bridge (ADB) key pairs.
        
        @param request: ModifyKeyPairNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyKeyPairNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.new_key_pair_name):
            query['NewKeyPairName'] = request.new_key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyKeyPairName',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyKeyPairNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_key_pair_name_with_options_async(
        self,
        request: eds_aic_20230930_models.ModifyKeyPairNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyKeyPairNameResponse:
        """
        @summary Modifies Android Debug Bridge (ADB) key pairs.
        
        @param request: ModifyKeyPairNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyKeyPairNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.new_key_pair_name):
            query['NewKeyPairName'] = request.new_key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyKeyPairName',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyKeyPairNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_key_pair_name(
        self,
        request: eds_aic_20230930_models.ModifyKeyPairNameRequest,
    ) -> eds_aic_20230930_models.ModifyKeyPairNameResponse:
        """
        @summary Modifies Android Debug Bridge (ADB) key pairs.
        
        @param request: ModifyKeyPairNameRequest
        @return: ModifyKeyPairNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_key_pair_name_with_options(request, runtime)

    async def modify_key_pair_name_async(
        self,
        request: eds_aic_20230930_models.ModifyKeyPairNameRequest,
    ) -> eds_aic_20230930_models.ModifyKeyPairNameResponse:
        """
        @summary Modifies Android Debug Bridge (ADB) key pairs.
        
        @param request: ModifyKeyPairNameRequest
        @return: ModifyKeyPairNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_key_pair_name_with_options_async(request, runtime)

    def modify_policy_group_with_options(
        self,
        tmp_req: eds_aic_20230930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyPolicyGroupResponse:
        """
        @summary Modifies a policy.
        
        @param tmp_req: ModifyPolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyPolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not UtilClient.is_unset(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not UtilClient.is_unset(request.policy_group_id):
            body['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_group_with_options_async(
        self,
        tmp_req: eds_aic_20230930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyPolicyGroupResponse:
        """
        @summary Modifies a policy.
        
        @param tmp_req: ModifyPolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyPolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_redirect):
            body['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.clipboard):
            body['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.html_5file_transfer):
            body['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            body['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.lock_resolution):
            body['LockResolution'] = request.lock_resolution
        if not UtilClient.is_unset(request.net_redirect_policy_shrink):
            body['NetRedirectPolicy'] = request.net_redirect_policy_shrink
        if not UtilClient.is_unset(request.policy_group_id):
            body['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.policy_group_name):
            body['PolicyGroupName'] = request.policy_group_name
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
        if not UtilClient.is_unset(request.watermark_shrink):
            body['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPolicyGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ModifyPolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_group(
        self,
        request: eds_aic_20230930_models.ModifyPolicyGroupRequest,
    ) -> eds_aic_20230930_models.ModifyPolicyGroupResponse:
        """
        @summary Modifies a policy.
        
        @param request: ModifyPolicyGroupRequest
        @return: ModifyPolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    async def modify_policy_group_async(
        self,
        request: eds_aic_20230930_models.ModifyPolicyGroupRequest,
    ) -> eds_aic_20230930_models.ModifyPolicyGroupResponse:
        """
        @summary Modifies a policy.
        
        @param request: ModifyPolicyGroupRequest
        @return: ModifyPolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def operate_app_with_options(
        self,
        request: eds_aic_20230930_models.OperateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.OperateAppResponse:
        """
        @summary Operates apps in a cloud phone, such as opening, closing, and reopening apps.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: OperateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.OperateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_with_options_async(
        self,
        request: eds_aic_20230930_models.OperateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.OperateAppResponse:
        """
        @summary Operates apps in a cloud phone, such as opening, closing, and reopening apps.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: OperateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.OperateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app(
        self,
        request: eds_aic_20230930_models.OperateAppRequest,
    ) -> eds_aic_20230930_models.OperateAppResponse:
        """
        @summary Operates apps in a cloud phone, such as opening, closing, and reopening apps.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: OperateAppRequest
        @return: OperateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_app_with_options(request, runtime)

    async def operate_app_async(
        self,
        request: eds_aic_20230930_models.OperateAppRequest,
    ) -> eds_aic_20230930_models.OperateAppResponse:
        """
        @summary Operates apps in a cloud phone, such as opening, closing, and reopening apps.
        
        @description This operation runs asynchronously. To check the operation result, visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: OperateAppRequest
        @return: OperateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_app_with_options_async(request, runtime)

    def reboot_android_instances_in_group_with_options(
        self,
        request: eds_aic_20230930_models.RebootAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse:
        """
        @summary Restarts one or more cloud phone instances.
        
        @description Before you restart a cloud phone instance, make sure it is in one of the following states: *Available, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: RebootAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAndroidInstancesInGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_android_instances_in_group_with_options_async(
        self,
        request: eds_aic_20230930_models.RebootAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse:
        """
        @summary Restarts one or more cloud phone instances.
        
        @description Before you restart a cloud phone instance, make sure it is in one of the following states: *Available, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: RebootAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAndroidInstancesInGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_android_instances_in_group(
        self,
        request: eds_aic_20230930_models.RebootAndroidInstancesInGroupRequest,
    ) -> eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse:
        """
        @summary Restarts one or more cloud phone instances.
        
        @description Before you restart a cloud phone instance, make sure it is in one of the following states: *Available, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: RebootAndroidInstancesInGroupRequest
        @return: RebootAndroidInstancesInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_android_instances_in_group_with_options(request, runtime)

    async def reboot_android_instances_in_group_async(
        self,
        request: eds_aic_20230930_models.RebootAndroidInstancesInGroupRequest,
    ) -> eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse:
        """
        @summary Restarts one or more cloud phone instances.
        
        @description Before you restart a cloud phone instance, make sure it is in one of the following states: *Available, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: RebootAndroidInstancesInGroupRequest
        @return: RebootAndroidInstancesInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_android_instances_in_group_with_options_async(request, runtime)

    def recovery_file_with_options(
        self,
        request: eds_aic_20230930_models.RecoveryFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RecoveryFileResponse:
        """
        @summary Restores backup files.
        
        @description Currently, this operation allows you to restore only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: RecoveryFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoveryFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not UtilClient.is_unset(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RecoveryFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_file_with_options_async(
        self,
        request: eds_aic_20230930_models.RecoveryFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RecoveryFileResponse:
        """
        @summary Restores backup files.
        
        @description Currently, this operation allows you to restore only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: RecoveryFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoveryFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.backup_all):
            query['BackupAll'] = request.backup_all
        if not UtilClient.is_unset(request.backup_file_id):
            query['BackupFileId'] = request.backup_file_id
        if not UtilClient.is_unset(request.backup_file_path):
            query['BackupFilePath'] = request.backup_file_path
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RecoveryFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_file(
        self,
        request: eds_aic_20230930_models.RecoveryFileRequest,
    ) -> eds_aic_20230930_models.RecoveryFileResponse:
        """
        @summary Restores backup files.
        
        @description Currently, this operation allows you to restore only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: RecoveryFileRequest
        @return: RecoveryFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recovery_file_with_options(request, runtime)

    async def recovery_file_async(
        self,
        request: eds_aic_20230930_models.RecoveryFileRequest,
    ) -> eds_aic_20230930_models.RecoveryFileResponse:
        """
        @summary Restores backup files.
        
        @description Currently, this operation allows you to restore only backup files generated by cloud phones that are stored in Object Storage Service (OSS) buckets.
        
        @param request: RecoveryFileRequest
        @return: RecoveryFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recovery_file_with_options_async(request, runtime)

    def renew_android_instance_groups_with_options(
        self,
        request: eds_aic_20230930_models.RenewAndroidInstanceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse:
        """
        @summary Renews instance groups.
        
        @param request: RenewAndroidInstanceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAndroidInstanceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAndroidInstanceGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_android_instance_groups_with_options_async(
        self,
        request: eds_aic_20230930_models.RenewAndroidInstanceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse:
        """
        @summary Renews instance groups.
        
        @param request: RenewAndroidInstanceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAndroidInstanceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_group_ids):
            query['InstanceGroupIds'] = request.instance_group_ids
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAndroidInstanceGroups',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_android_instance_groups(
        self,
        request: eds_aic_20230930_models.RenewAndroidInstanceGroupsRequest,
    ) -> eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse:
        """
        @summary Renews instance groups.
        
        @param request: RenewAndroidInstanceGroupsRequest
        @return: RenewAndroidInstanceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_android_instance_groups_with_options(request, runtime)

    async def renew_android_instance_groups_async(
        self,
        request: eds_aic_20230930_models.RenewAndroidInstanceGroupsRequest,
    ) -> eds_aic_20230930_models.RenewAndroidInstanceGroupsResponse:
        """
        @summary Renews instance groups.
        
        @param request: RenewAndroidInstanceGroupsRequest
        @return: RenewAndroidInstanceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_android_instance_groups_with_options_async(request, runtime)

    def renew_cloud_phone_nodes_with_options(
        self,
        request: eds_aic_20230930_models.RenewCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RenewCloudPhoneNodesResponse:
        """
        @summary Renews a cloud mobile matrix.
        
        @param request: RenewCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RenewCloudPhoneNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_cloud_phone_nodes_with_options_async(
        self,
        request: eds_aic_20230930_models.RenewCloudPhoneNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RenewCloudPhoneNodesResponse:
        """
        @summary Renews a cloud mobile matrix.
        
        @param request: RenewCloudPhoneNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewCloudPhoneNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewCloudPhoneNodes',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RenewCloudPhoneNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_cloud_phone_nodes(
        self,
        request: eds_aic_20230930_models.RenewCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.RenewCloudPhoneNodesResponse:
        """
        @summary Renews a cloud mobile matrix.
        
        @param request: RenewCloudPhoneNodesRequest
        @return: RenewCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_cloud_phone_nodes_with_options(request, runtime)

    async def renew_cloud_phone_nodes_async(
        self,
        request: eds_aic_20230930_models.RenewCloudPhoneNodesRequest,
    ) -> eds_aic_20230930_models.RenewCloudPhoneNodesResponse:
        """
        @summary Renews a cloud mobile matrix.
        
        @param request: RenewCloudPhoneNodesRequest
        @return: RenewCloudPhoneNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_cloud_phone_nodes_with_options_async(request, runtime)

    def reset_android_instances_in_group_with_options(
        self,
        request: eds_aic_20230930_models.ResetAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse:
        """
        @summary Resets one or more cloud phone instances.
        
        @description Before you reset a cloud phone instance, make sure it is in one of the following states: *Available, Stopped, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: ResetAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.setting_reset_type):
            query['SettingResetType'] = request.setting_reset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAndroidInstancesInGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_android_instances_in_group_with_options_async(
        self,
        request: eds_aic_20230930_models.ResetAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse:
        """
        @summary Resets one or more cloud phone instances.
        
        @description Before you reset a cloud phone instance, make sure it is in one of the following states: *Available, Stopped, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: ResetAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.setting_reset_type):
            query['SettingResetType'] = request.setting_reset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAndroidInstancesInGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_android_instances_in_group(
        self,
        request: eds_aic_20230930_models.ResetAndroidInstancesInGroupRequest,
    ) -> eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse:
        """
        @summary Resets one or more cloud phone instances.
        
        @description Before you reset a cloud phone instance, make sure it is in one of the following states: *Available, Stopped, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: ResetAndroidInstancesInGroupRequest
        @return: ResetAndroidInstancesInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_android_instances_in_group_with_options(request, runtime)

    async def reset_android_instances_in_group_async(
        self,
        request: eds_aic_20230930_models.ResetAndroidInstancesInGroupRequest,
    ) -> eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse:
        """
        @summary Resets one or more cloud phone instances.
        
        @description Before you reset a cloud phone instance, make sure it is in one of the following states: *Available, Stopped, Abnormal, Backup failure, and Restoration failure**.
        
        @param request: ResetAndroidInstancesInGroupRequest
        @return: ResetAndroidInstancesInGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_android_instances_in_group_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: eds_aic_20230930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RunCommandResponse:
        """
        @summary Executes a command on a cloud phone instance.
        
        @param request: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: eds_aic_20230930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RunCommandResponse:
        """
        @summary Executes a command on a cloud phone instance.
        
        @param request: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: eds_aic_20230930_models.RunCommandRequest,
    ) -> eds_aic_20230930_models.RunCommandResponse:
        """
        @summary Executes a command on a cloud phone instance.
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: eds_aic_20230930_models.RunCommandRequest,
    ) -> eds_aic_20230930_models.RunCommandResponse:
        """
        @summary Executes a command on a cloud phone instance.
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        request: eds_aic_20230930_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.SendFileResponse:
        """
        @summary Pushes files from Object Storage Service (OSS) buckets to cloud phone instances.
        
        @description Currently, this operation allows you to only push files or folders from OSS buckets to cloud phone instances.
        
        @param request: SendFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not UtilClient.is_unset(request.target_file_name):
            query['TargetFileName'] = request.target_file_name
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        if not UtilClient.is_unset(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_file_with_options_async(
        self,
        request: eds_aic_20230930_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.SendFileResponse:
        """
        @summary Pushes files from Object Storage Service (OSS) buckets to cloud phone instances.
        
        @description Currently, this operation allows you to only push files or folders from OSS buckets to cloud phone instances.
        
        @param request: SendFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
        if not UtilClient.is_unset(request.source_file_path):
            query['SourceFilePath'] = request.source_file_path
        if not UtilClient.is_unset(request.target_file_name):
            query['TargetFileName'] = request.target_file_name
        if not UtilClient.is_unset(request.upload_endpoint):
            query['UploadEndpoint'] = request.upload_endpoint
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        if not UtilClient.is_unset(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.SendFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_file(
        self,
        request: eds_aic_20230930_models.SendFileRequest,
    ) -> eds_aic_20230930_models.SendFileResponse:
        """
        @summary Pushes files from Object Storage Service (OSS) buckets to cloud phone instances.
        
        @description Currently, this operation allows you to only push files or folders from OSS buckets to cloud phone instances.
        
        @param request: SendFileRequest
        @return: SendFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: eds_aic_20230930_models.SendFileRequest,
    ) -> eds_aic_20230930_models.SendFileResponse:
        """
        @summary Pushes files from Object Storage Service (OSS) buckets to cloud phone instances.
        
        @description Currently, this operation allows you to only push files or folders from OSS buckets to cloud phone instances.
        
        @param request: SendFileRequest
        @return: SendFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def set_adb_secure_with_options(
        self,
        request: eds_aic_20230930_models.SetAdbSecureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.SetAdbSecureResponse:
        """
        @summary Sets the authentication status for cloud phone instances. If you enable Android Debug Bridge (ADB) authentication for cloud phone instances, the system will verify the validity of the ADB key pairs provided by end users when they connect to the instances over ADB. To ensure successful authentication and a proper connection, we recommend that you attach ADB key pairs to cloud phone instances. If you disable ADB authentication for cloud phone instances, the system will no longer verify the validity of any ADB key pairs. As a result, end users can connect to the cloud phone instances over ADB without authentication, provided the network connection is functioning properly.
        
        @description Before you call this operation, make sure that the desired cloud phone instance is in the Running state.
        
        @param request: SetAdbSecureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAdbSecureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAdbSecure',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.SetAdbSecureResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_adb_secure_with_options_async(
        self,
        request: eds_aic_20230930_models.SetAdbSecureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.SetAdbSecureResponse:
        """
        @summary Sets the authentication status for cloud phone instances. If you enable Android Debug Bridge (ADB) authentication for cloud phone instances, the system will verify the validity of the ADB key pairs provided by end users when they connect to the instances over ADB. To ensure successful authentication and a proper connection, we recommend that you attach ADB key pairs to cloud phone instances. If you disable ADB authentication for cloud phone instances, the system will no longer verify the validity of any ADB key pairs. As a result, end users can connect to the cloud phone instances over ADB without authentication, provided the network connection is functioning properly.
        
        @description Before you call this operation, make sure that the desired cloud phone instance is in the Running state.
        
        @param request: SetAdbSecureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAdbSecureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAdbSecure',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.SetAdbSecureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_adb_secure(
        self,
        request: eds_aic_20230930_models.SetAdbSecureRequest,
    ) -> eds_aic_20230930_models.SetAdbSecureResponse:
        """
        @summary Sets the authentication status for cloud phone instances. If you enable Android Debug Bridge (ADB) authentication for cloud phone instances, the system will verify the validity of the ADB key pairs provided by end users when they connect to the instances over ADB. To ensure successful authentication and a proper connection, we recommend that you attach ADB key pairs to cloud phone instances. If you disable ADB authentication for cloud phone instances, the system will no longer verify the validity of any ADB key pairs. As a result, end users can connect to the cloud phone instances over ADB without authentication, provided the network connection is functioning properly.
        
        @description Before you call this operation, make sure that the desired cloud phone instance is in the Running state.
        
        @param request: SetAdbSecureRequest
        @return: SetAdbSecureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_adb_secure_with_options(request, runtime)

    async def set_adb_secure_async(
        self,
        request: eds_aic_20230930_models.SetAdbSecureRequest,
    ) -> eds_aic_20230930_models.SetAdbSecureResponse:
        """
        @summary Sets the authentication status for cloud phone instances. If you enable Android Debug Bridge (ADB) authentication for cloud phone instances, the system will verify the validity of the ADB key pairs provided by end users when they connect to the instances over ADB. To ensure successful authentication and a proper connection, we recommend that you attach ADB key pairs to cloud phone instances. If you disable ADB authentication for cloud phone instances, the system will no longer verify the validity of any ADB key pairs. As a result, end users can connect to the cloud phone instances over ADB without authentication, provided the network connection is functioning properly.
        
        @description Before you call this operation, make sure that the desired cloud phone instance is in the Running state.
        
        @param request: SetAdbSecureRequest
        @return: SetAdbSecureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_adb_secure_with_options_async(request, runtime)

    def start_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.StartAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.StartAndroidInstanceResponse:
        """
        @summary Start instances.
        
        @description Only supports starting when the instance is in the *Stopped, Backup Failed, or Recovery Failed** state.
        
        @param request: StartAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.StartAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_android_instance_with_options_async(
        self,
        request: eds_aic_20230930_models.StartAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.StartAndroidInstanceResponse:
        """
        @summary Start instances.
        
        @description Only supports starting when the instance is in the *Stopped, Backup Failed, or Recovery Failed** state.
        
        @param request: StartAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.StartAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_android_instance(
        self,
        request: eds_aic_20230930_models.StartAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.StartAndroidInstanceResponse:
        """
        @summary Start instances.
        
        @description Only supports starting when the instance is in the *Stopped, Backup Failed, or Recovery Failed** state.
        
        @param request: StartAndroidInstanceRequest
        @return: StartAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_android_instance_with_options(request, runtime)

    async def start_android_instance_async(
        self,
        request: eds_aic_20230930_models.StartAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.StartAndroidInstanceResponse:
        """
        @summary Start instances.
        
        @description Only supports starting when the instance is in the *Stopped, Backup Failed, or Recovery Failed** state.
        
        @param request: StartAndroidInstanceRequest
        @return: StartAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_android_instance_with_options_async(request, runtime)

    def stop_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.StopAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.StopAndroidInstanceResponse:
        """
        @summary Stops a cloud phone instance.
        
        @description Before you stop a cloud phone instance, make sure it is in one of the following states: *Available, Backup failure, and Restoration failure**.
        
        @param request: StopAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.StopAndroidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_android_instance_with_options_async(
        self,
        request: eds_aic_20230930_models.StopAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.StopAndroidInstanceResponse:
        """
        @summary Stops a cloud phone instance.
        
        @description Before you stop a cloud phone instance, make sure it is in one of the following states: *Available, Backup failure, and Restoration failure**.
        
        @param request: StopAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAndroidInstance',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.StopAndroidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_android_instance(
        self,
        request: eds_aic_20230930_models.StopAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.StopAndroidInstanceResponse:
        """
        @summary Stops a cloud phone instance.
        
        @description Before you stop a cloud phone instance, make sure it is in one of the following states: *Available, Backup failure, and Restoration failure**.
        
        @param request: StopAndroidInstanceRequest
        @return: StopAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_android_instance_with_options(request, runtime)

    async def stop_android_instance_async(
        self,
        request: eds_aic_20230930_models.StopAndroidInstanceRequest,
    ) -> eds_aic_20230930_models.StopAndroidInstanceResponse:
        """
        @summary Stops a cloud phone instance.
        
        @description Before you stop a cloud phone instance, make sure it is in one of the following states: *Available, Backup failure, and Restoration failure**.
        
        @param request: StopAndroidInstanceRequest
        @return: StopAndroidInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_android_instance_with_options_async(request, runtime)

    def uninstall_app_with_options(
        self,
        request: eds_aic_20230930_models.UninstallAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UninstallAppResponse:
        """
        @summary Uninstalls an app from multiple cloud phone instances.
        
        @description This operation runs asynchronously. To check the operation result, you can visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: UninstallAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UninstallAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_app_with_options_async(
        self,
        request: eds_aic_20230930_models.UninstallAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UninstallAppResponse:
        """
        @summary Uninstalls an app from multiple cloud phone instances.
        
        @description This operation runs asynchronously. To check the operation result, you can visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: UninstallAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id_list):
            query['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.instance_group_id_list):
            query['InstanceGroupIdList'] = request.instance_group_id_list
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallApp',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UninstallAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_app(
        self,
        request: eds_aic_20230930_models.UninstallAppRequest,
    ) -> eds_aic_20230930_models.UninstallAppResponse:
        """
        @summary Uninstalls an app from multiple cloud phone instances.
        
        @description This operation runs asynchronously. To check the operation result, you can visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: UninstallAppRequest
        @return: UninstallAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_app_with_options(request, runtime)

    async def uninstall_app_async(
        self,
        request: eds_aic_20230930_models.UninstallAppRequest,
    ) -> eds_aic_20230930_models.UninstallAppResponse:
        """
        @summary Uninstalls an app from multiple cloud phone instances.
        
        @description This operation runs asynchronously. To check the operation result, you can visit the Task Center. To retrieve task details, call the [DescribeTasks](~~DescribeTasks~~) operation.
        
        @param request: UninstallAppRequest
        @return: UninstallAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_app_with_options_async(request, runtime)

    def update_custom_image_name_with_options(
        self,
        request: eds_aic_20230930_models.UpdateCustomImageNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateCustomImageNameResponse:
        """
        @summary Updates the name of a custom image.
        
        @param request: UpdateCustomImageNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomImageNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomImageName',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateCustomImageNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_image_name_with_options_async(
        self,
        request: eds_aic_20230930_models.UpdateCustomImageNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateCustomImageNameResponse:
        """
        @summary Updates the name of a custom image.
        
        @param request: UpdateCustomImageNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomImageNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomImageName',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateCustomImageNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_image_name(
        self,
        request: eds_aic_20230930_models.UpdateCustomImageNameRequest,
    ) -> eds_aic_20230930_models.UpdateCustomImageNameResponse:
        """
        @summary Updates the name of a custom image.
        
        @param request: UpdateCustomImageNameRequest
        @return: UpdateCustomImageNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_image_name_with_options(request, runtime)

    async def update_custom_image_name_async(
        self,
        request: eds_aic_20230930_models.UpdateCustomImageNameRequest,
    ) -> eds_aic_20230930_models.UpdateCustomImageNameResponse:
        """
        @summary Updates the name of a custom image.
        
        @param request: UpdateCustomImageNameRequest
        @return: UpdateCustomImageNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_image_name_with_options_async(request, runtime)

    def update_instance_group_image_with_options(
        self,
        request: eds_aic_20230930_models.UpdateInstanceGroupImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateInstanceGroupImageResponse:
        """
        @summary Changes the image of an instance group.
        
        @description Before you call this operation, make sure the image is in the Available state and the region of the image is included in the region list of the desired instance group. In addition, the instance group itself is available.
        
        @param request: UpdateInstanceGroupImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceGroupImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_ids):
            body['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceGroupImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateInstanceGroupImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_group_image_with_options_async(
        self,
        request: eds_aic_20230930_models.UpdateInstanceGroupImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateInstanceGroupImageResponse:
        """
        @summary Changes the image of an instance group.
        
        @description Before you call this operation, make sure the image is in the Available state and the region of the image is included in the region list of the desired instance group. In addition, the instance group itself is available.
        
        @param request: UpdateInstanceGroupImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceGroupImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_ids):
            body['InstanceGroupIds'] = request.instance_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceGroupImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateInstanceGroupImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_group_image(
        self,
        request: eds_aic_20230930_models.UpdateInstanceGroupImageRequest,
    ) -> eds_aic_20230930_models.UpdateInstanceGroupImageResponse:
        """
        @summary Changes the image of an instance group.
        
        @description Before you call this operation, make sure the image is in the Available state and the region of the image is included in the region list of the desired instance group. In addition, the instance group itself is available.
        
        @param request: UpdateInstanceGroupImageRequest
        @return: UpdateInstanceGroupImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_group_image_with_options(request, runtime)

    async def update_instance_group_image_async(
        self,
        request: eds_aic_20230930_models.UpdateInstanceGroupImageRequest,
    ) -> eds_aic_20230930_models.UpdateInstanceGroupImageResponse:
        """
        @summary Changes the image of an instance group.
        
        @description Before you call this operation, make sure the image is in the Available state and the region of the image is included in the region list of the desired instance group. In addition, the instance group itself is available.
        
        @param request: UpdateInstanceGroupImageRequest
        @return: UpdateInstanceGroupImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_group_image_with_options_async(request, runtime)

    def update_instance_image_with_options(
        self,
        request: eds_aic_20230930_models.UpdateInstanceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateInstanceImageResponse:
        """
        @summary 更新实例镜像
        
        @param request: UpdateInstanceImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateInstanceImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_image_with_options_async(
        self,
        request: eds_aic_20230930_models.UpdateInstanceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpdateInstanceImageResponse:
        """
        @summary 更新实例镜像
        
        @param request: UpdateInstanceImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceImage',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpdateInstanceImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_image(
        self,
        request: eds_aic_20230930_models.UpdateInstanceImageRequest,
    ) -> eds_aic_20230930_models.UpdateInstanceImageResponse:
        """
        @summary 更新实例镜像
        
        @param request: UpdateInstanceImageRequest
        @return: UpdateInstanceImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_image_with_options(request, runtime)

    async def update_instance_image_async(
        self,
        request: eds_aic_20230930_models.UpdateInstanceImageRequest,
    ) -> eds_aic_20230930_models.UpdateInstanceImageResponse:
        """
        @summary 更新实例镜像
        
        @param request: UpdateInstanceImageRequest
        @return: UpdateInstanceImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_image_with_options_async(request, runtime)

    def upgrade_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.UpgradeAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse:
        """
        @summary Upgrades an instance group. Currently, this operation allows you to only increase the number of instances in an instance group.
        
        @description Currently, this operation allows you to only increase the size of an instance group.
        
        @param request: UpgradeAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.increase_number_of_instance):
            query['IncreaseNumberOfInstance'] = request.increase_number_of_instance
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_android_instance_group_with_options_async(
        self,
        request: eds_aic_20230930_models.UpgradeAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse:
        """
        @summary Upgrades an instance group. Currently, this operation allows you to only increase the number of instances in an instance group.
        
        @description Currently, this operation allows you to only increase the size of an instance group.
        
        @param request: UpgradeAndroidInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAndroidInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.increase_number_of_instance):
            query['IncreaseNumberOfInstance'] = request.increase_number_of_instance
        if not UtilClient.is_unset(request.instance_group_id):
            query['InstanceGroupId'] = request.instance_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAndroidInstanceGroup',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_android_instance_group(
        self,
        request: eds_aic_20230930_models.UpgradeAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse:
        """
        @summary Upgrades an instance group. Currently, this operation allows you to only increase the number of instances in an instance group.
        
        @description Currently, this operation allows you to only increase the size of an instance group.
        
        @param request: UpgradeAndroidInstanceGroupRequest
        @return: UpgradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_android_instance_group_with_options(request, runtime)

    async def upgrade_android_instance_group_async(
        self,
        request: eds_aic_20230930_models.UpgradeAndroidInstanceGroupRequest,
    ) -> eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse:
        """
        @summary Upgrades an instance group. Currently, this operation allows you to only increase the number of instances in an instance group.
        
        @description Currently, this operation allows you to only increase the size of an instance group.
        
        @param request: UpgradeAndroidInstanceGroupRequest
        @return: UpgradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_android_instance_group_with_options_async(request, runtime)
