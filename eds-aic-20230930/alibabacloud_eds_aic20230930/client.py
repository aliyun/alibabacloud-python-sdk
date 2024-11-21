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
        @summary 绑定密钥对
        
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
        @summary 绑定密钥对
        
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
        @summary 绑定密钥对
        
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
        @summary 绑定密钥对
        
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
        @summary 为用户授权/解授权安卓实例
        
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
        @summary 为用户授权/解授权安卓实例
        
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
        @summary 为用户授权/解授权安卓实例
        
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
        @summary 为用户授权/解授权安卓实例
        
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
        @summary 数据备份
        
        @param request: BackupFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
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
        @summary 数据备份
        
        @param request: BackupFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
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
        @summary 数据备份
        
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
        @summary 数据备份
        
        @param request: BackupFileRequest
        @return: BackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.backup_file_with_options_async(request, runtime)

    def check_resource_stock_with_options(
        self,
        request: eds_aic_20230930_models.CheckResourceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CheckResourceStockResponse:
        """
        @summary 检查资源库存
        
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
        @summary 检查资源库存
        
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
        @summary 检查资源库存
        
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
        @summary 检查资源库存
        
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
        @summary 创建安卓实例组
        
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
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
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
        @summary 创建安卓实例组
        
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
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_group_name):
            query['InstanceGroupName'] = request.instance_group_name
        if not UtilClient.is_unset(request.instance_group_spec):
            query['InstanceGroupSpec'] = request.instance_group_spec
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
        @summary 创建安卓实例组
        
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
        @summary 创建安卓实例组
        
        @param request: CreateAndroidInstanceGroupRequest
        @return: CreateAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_android_instance_group_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: eds_aic_20230930_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
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
        request: eds_aic_20230930_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
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
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: eds_aic_20230930_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.CreateCustomImageResponse:
        """
        @summary 创建自定义镜像
        
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
        @summary 创建自定义镜像
        
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
        @summary 创建自定义镜像
        
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
        @summary 创建自定义镜像
        
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
        @summary 创建密钥对
        
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
        @summary 创建密钥对
        
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
        @summary 创建密钥对
        
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
        @summary 创建密钥对
        
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
        @summary 创建策略
        
        @param tmp_req: CreatePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreatePolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
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
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
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
        @summary 创建策略
        
        @param tmp_req: CreatePolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.CreatePolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
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
        if not UtilClient.is_unset(request.resolution_height):
            body['ResolutionHeight'] = request.resolution_height
        if not UtilClient.is_unset(request.resolution_width):
            body['ResolutionWidth'] = request.resolution_width
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
        @summary 创建策略
        
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
        @summary 创建策略
        
        @param request: CreatePolicyGroupRequest
        @return: CreatePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def delete_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.DeleteAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteAndroidInstanceGroupResponse:
        """
        @summary 删除安卓实例组
        
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
        @summary 删除安卓实例组
        
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
        @summary 删除安卓实例组
        
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
        @summary 删除安卓实例组
        
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
        @summary 删除app
        
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
        @summary 删除app
        
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
        @summary 删除app
        
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
        @summary 删除app
        
        @param request: DeleteAppsRequest
        @return: DeleteAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_apps_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        tmp_req: eds_aic_20230930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DeleteImagesResponse:
        """
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
        @summary 删除密钥对
        
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
        @summary 删除密钥对
        
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
        @summary 删除密钥对
        
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
        @summary 删除密钥对
        
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
        @summary 删除策略
        
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
        @summary 删除策略
        
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
        @summary 删除策略
        
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
        @summary 删除策略
        
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
        @summary 查询实例组
        
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
        @summary 查询实例组
        
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
        @summary 查询实例组
        
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
        @summary 查询实例组
        
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
        @summary 查询安卓实例列表
        
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
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        @summary 查询安卓实例列表
        
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
        if not UtilClient.is_unset(request.sale_mode):
            query['SaleMode'] = request.sale_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        @summary 查询安卓实例列表
        
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
        @summary 查询安卓实例列表
        
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
        @summary 查询app
        
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
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.installation_status):
            query['InstallationStatus'] = request.installation_status
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
        @summary 查询app
        
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
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.installation_status):
            query['InstallationStatus'] = request.installation_status
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
        @summary 查询app
        
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
        @summary 查询app
        
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
        @param request: DescribeBackupFilesRequest
        @return: DescribeBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_files_with_options_async(request, runtime)

    def describe_image_list_with_options(
        self,
        request: eds_aic_20230930_models.DescribeImageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DescribeImageListResponse:
        """
        @param request: DescribeImageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageListResponse
        """
        UtilClient.validate_model(request)
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
        @param request: DescribeImageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageListResponse
        """
        UtilClient.validate_model(request)
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
        @summary 查询命令结果
        
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
        @summary 查询命令结果
        
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
        @summary 查询命令结果
        
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
        @summary 查询命令结果
        
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
        @summary 查询密钥对
        
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
        @summary 查询密钥对
        
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
        @summary 查询密钥对
        
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
        @summary 查询密钥对
        
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
        @summary 查询地域
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
        @summary 查询地域
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
        @summary 查询地域
        
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
        @summary 查询地域
        
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
        @summary 查询规格
        
        @param request: DescribeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        @summary 查询规格
        
        @param request: DescribeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        @summary 查询规格
        
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
        @summary 查询规格
        
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
        @summary 查询异步任务
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
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
        @summary 查询异步任务
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
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
        @summary 查询异步任务
        
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
        @summary 查询异步任务
        
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
        @summary 解绑密钥对
        
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
        @summary 解绑密钥对
        
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
        @summary 解绑密钥对
        
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
        @summary 解绑密钥对
        
        @param request: DetachKeyPairRequest
        @return: DetachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def distribute_image_with_options(
        self,
        request: eds_aic_20230930_models.DistributeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.DistributeImageResponse:
        """
        @summary 自定义镜像分发
        
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
        @summary 自定义镜像分发
        
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
        @summary 自定义镜像分发
        
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
        @summary 自定义镜像分发
        
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
        @summary 实例组缩容
        
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
        @summary 实例组缩容
        
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
        @summary 实例组缩容
        
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
        @summary 实例组缩容
        
        @param request: DowngradeAndroidInstanceGroupRequest
        @return: DowngradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.downgrade_android_instance_group_with_options_async(request, runtime)

    def fetch_file_with_options(
        self,
        request: eds_aic_20230930_models.FetchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.FetchFileResponse:
        """
        @summary 云手机拉取文件到OSS
        
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
        @summary 云手机拉取文件到OSS
        
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
        @summary 云手机拉取文件到OSS
        
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
        @summary 云手机拉取文件到OSS
        
        @param request: FetchFileRequest
        @return: FetchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_file_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: eds_aic_20230930_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ImportKeyPairResponse:
        """
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
        @summary 安装app到实例组
        
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
        @summary 安装app到实例组
        
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
        @summary 安装app到实例组
        
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
        @summary 安装app到实例组
        
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
        @summary 查询Policy列表
        
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
        @summary 查询Policy列表
        
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
        @summary 查询Policy列表
        
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
        @summary 查询Policy列表
        
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
        @summary 修改安卓实例信息
        
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
        @summary 修改安卓实例信息
        
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
        @summary 修改安卓实例信息
        
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
        @summary 修改安卓实例信息
        
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
        @summary 修改安卓实例组
        
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
        @summary 修改安卓实例组
        
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
        @summary 修改安卓实例组
        
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
        @summary 修改安卓实例组
        
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
        @summary 修改app
        
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
        @summary 修改app
        
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
        @summary 修改app
        
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
        @summary 修改app
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_key_pair_name_with_options(
        self,
        request: eds_aic_20230930_models.ModifyKeyPairNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ModifyKeyPairNameResponse:
        """
        @summary 修改密钥对名称
        
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
        @summary 修改密钥对名称
        
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
        @summary 修改密钥对名称
        
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
        @summary 修改密钥对名称
        
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
        @summary 修改policy
        
        @param tmp_req: ModifyPolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyPolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
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
        @summary 修改policy
        
        @param tmp_req: ModifyPolicyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_aic_20230930_models.ModifyPolicyGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.net_redirect_policy):
            request.net_redirect_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net_redirect_policy, 'NetRedirectPolicy', 'json')
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
        @summary 修改policy
        
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
        @summary 修改policy
        
        @param request: ModifyPolicyGroupRequest
        @return: ModifyPolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def reboot_android_instances_in_group_with_options(
        self,
        request: eds_aic_20230930_models.RebootAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.RebootAndroidInstancesInGroupResponse:
        """
        @summary 重启安卓实例
        
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
        @summary 重启安卓实例
        
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
        @summary 重启安卓实例
        
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
        @summary 重启安卓实例
        
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
        @summary 数据恢复
        
        @param request: RecoveryFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoveryFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
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
        @summary 数据恢复
        
        @param request: RecoveryFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoveryFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_id_list):
            query['AndroidInstanceIdList'] = request.android_instance_id_list
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
        @summary 数据恢复
        
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
        @summary 数据恢复
        
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
        @summary 续费安卓实例组
        
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
        @summary 续费安卓实例组
        
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
        @summary 续费安卓实例组
        
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
        @summary 续费安卓实例组
        
        @param request: RenewAndroidInstanceGroupsRequest
        @return: RenewAndroidInstanceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_android_instance_groups_with_options_async(request, runtime)

    def reset_android_instances_in_group_with_options(
        self,
        request: eds_aic_20230930_models.ResetAndroidInstancesInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.ResetAndroidInstancesInGroupResponse:
        """
        @summary 重置安卓实例
        
        @param request: ResetAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
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
        @summary 重置安卓实例
        
        @param request: ResetAndroidInstancesInGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAndroidInstancesInGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
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
        @summary 重置安卓实例
        
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
        @summary 重置安卓实例
        
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
        @summary 通过eds agent通道下发命令
        
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
        @summary 通过eds agent通道下发命令
        
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
        @summary 通过eds agent通道下发命令
        
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
        @summary 通过eds agent通道下发命令
        
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
        @summary 推送文件到云手机
        
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
        @summary 推送文件到云手机
        
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
        @summary 推送文件到云手机
        
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
        @summary 推送文件到云手机
        
        @param request: SendFileRequest
        @return: SendFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def start_android_instance_with_options(
        self,
        request: eds_aic_20230930_models.StartAndroidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.StartAndroidInstanceResponse:
        """
        @summary 实例开机
        
        @param request: StartAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
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
        @summary 实例开机
        
        @param request: StartAndroidInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAndroidInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_instance_ids):
            query['AndroidInstanceIds'] = request.android_instance_ids
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
        @summary 实例开机
        
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
        @summary 实例开机
        
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
        @summary 实例关机
        
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
        @summary 实例关机
        
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
        @summary 实例关机
        
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
        @summary 实例关机
        
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
        @summary 卸载app
        
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
        @summary 卸载app
        
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
        @summary 卸载app
        
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
        @summary 卸载app
        
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
        @summary 修改自定义镜像名称
        
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
        @summary 修改自定义镜像名称
        
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
        @summary 修改自定义镜像名称
        
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
        @summary 修改自定义镜像名称
        
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
        @summary 实例组变更镜像
        
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
        @summary 实例组变更镜像
        
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
        @summary 实例组变更镜像
        
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
        @summary 实例组变更镜像
        
        @param request: UpdateInstanceGroupImageRequest
        @return: UpdateInstanceGroupImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_group_image_with_options_async(request, runtime)

    def upgrade_android_instance_group_with_options(
        self,
        request: eds_aic_20230930_models.UpgradeAndroidInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_aic_20230930_models.UpgradeAndroidInstanceGroupResponse:
        """
        @summary 安卓实例组扩容
        
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
        @summary 安卓实例组扩容
        
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
        @summary 安卓实例组扩容
        
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
        @summary 安卓实例组扩容
        
        @param request: UpgradeAndroidInstanceGroupRequest
        @return: UpgradeAndroidInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_android_instance_group_with_options_async(request, runtime)
