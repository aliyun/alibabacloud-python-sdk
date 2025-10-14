# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardbx20200202 import models as polardbx_20200202_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'polardbx.aliyuncs.com',
            'ap-northeast-2-pop': 'polardbx.aliyuncs.com',
            'ap-south-1': 'polardbx.aliyuncs.com',
            'ap-southeast-2': 'polardbx.aliyuncs.com',
            'ap-southeast-3': 'polardbx.aliyuncs.com',
            'ap-southeast-5': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-1': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-pop': 'polardbx.aliyuncs.com',
            'cn-beijing-gov-1': 'polardbx.aliyuncs.com',
            'cn-beijing-nu16-b01': 'polardbx.aliyuncs.com',
            'cn-edge-1': 'polardbx.aliyuncs.com',
            'cn-fujian': 'polardbx.aliyuncs.com',
            'cn-haidian-cm12-c01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-finance': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'polardbx.aliyuncs.com',
            'cn-hangzhou-test-306': 'polardbx.aliyuncs.com',
            'cn-hongkong-finance-pop': 'polardbx.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'polardbx.aliyuncs.com',
            'cn-north-2-gov-1': 'polardbx.aliyuncs.com',
            'cn-qingdao-nebula': 'polardbx.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardbx.aliyuncs.com',
            'cn-shanghai-inner': 'polardbx.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-inner': 'polardbx.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardbx.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardbx.aliyuncs.com',
            'cn-wuhan': 'polardbx.aliyuncs.com',
            'cn-wulanchabu': 'polardbx.aliyuncs.com',
            'cn-yushanfang': 'polardbx.aliyuncs.com',
            'cn-zhangbei': 'polardbx.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'polardbx.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'polardbx.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'polardbx.aliyuncs.com',
            'eu-central-1': 'polardbx.aliyuncs.com',
            'eu-west-1': 'polardbx.aliyuncs.com',
            'eu-west-1-oxs': 'polardbx.aliyuncs.com',
            'me-east-1': 'polardbx.aliyuncs.com',
            'rus-west-1-pop': 'polardbx.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('polardbx', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def align_storage_primary_azone_with_options(
        self,
        request: polardbx_20200202_models.AlignStoragePrimaryAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AlignStoragePrimaryAzoneResponse:
        """
        @param request: AlignStoragePrimaryAzoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AlignStoragePrimaryAzoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_instance_name):
            query['StorageInstanceName'] = request.storage_instance_name
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AlignStoragePrimaryAzone',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AlignStoragePrimaryAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def align_storage_primary_azone_with_options_async(
        self,
        request: polardbx_20200202_models.AlignStoragePrimaryAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AlignStoragePrimaryAzoneResponse:
        """
        @param request: AlignStoragePrimaryAzoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AlignStoragePrimaryAzoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_instance_name):
            query['StorageInstanceName'] = request.storage_instance_name
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AlignStoragePrimaryAzone',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AlignStoragePrimaryAzoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def align_storage_primary_azone(
        self,
        request: polardbx_20200202_models.AlignStoragePrimaryAzoneRequest,
    ) -> polardbx_20200202_models.AlignStoragePrimaryAzoneResponse:
        """
        @param request: AlignStoragePrimaryAzoneRequest
        @return: AlignStoragePrimaryAzoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.align_storage_primary_azone_with_options(request, runtime)

    async def align_storage_primary_azone_async(
        self,
        request: polardbx_20200202_models.AlignStoragePrimaryAzoneRequest,
    ) -> polardbx_20200202_models.AlignStoragePrimaryAzoneResponse:
        """
        @param request: AlignStoragePrimaryAzoneRequest
        @return: AlignStoragePrimaryAzoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.align_storage_primary_azone_with_options_async(request, runtime)

    def allocate_cold_data_volume_with_options(
        self,
        request: polardbx_20200202_models.AllocateColdDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateColdDataVolumeResponse:
        """
        @summary 开通冷存储
        
        @param request: AllocateColdDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateColdDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateColdDataVolume',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateColdDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cold_data_volume_with_options_async(
        self,
        request: polardbx_20200202_models.AllocateColdDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateColdDataVolumeResponse:
        """
        @summary 开通冷存储
        
        @param request: AllocateColdDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateColdDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateColdDataVolume',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateColdDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cold_data_volume(
        self,
        request: polardbx_20200202_models.AllocateColdDataVolumeRequest,
    ) -> polardbx_20200202_models.AllocateColdDataVolumeResponse:
        """
        @summary 开通冷存储
        
        @param request: AllocateColdDataVolumeRequest
        @return: AllocateColdDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cold_data_volume_with_options(request, runtime)

    async def allocate_cold_data_volume_async(
        self,
        request: polardbx_20200202_models.AllocateColdDataVolumeRequest,
    ) -> polardbx_20200202_models.AllocateColdDataVolumeResponse:
        """
        @summary 开通冷存储
        
        @param request: AllocateColdDataVolumeRequest
        @return: AllocateColdDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cold_data_volume_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        """
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        """
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        """
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        """
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def attach_columnar_instance_with_options(
        self,
        request: polardbx_20200202_models.AttachColumnarInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AttachColumnarInstanceResponse:
        """
        @param request: AttachColumnarInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachColumnarInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachColumnarInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AttachColumnarInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_columnar_instance_with_options_async(
        self,
        request: polardbx_20200202_models.AttachColumnarInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AttachColumnarInstanceResponse:
        """
        @param request: AttachColumnarInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachColumnarInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachColumnarInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AttachColumnarInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_columnar_instance(
        self,
        request: polardbx_20200202_models.AttachColumnarInstanceRequest,
    ) -> polardbx_20200202_models.AttachColumnarInstanceResponse:
        """
        @param request: AttachColumnarInstanceRequest
        @return: AttachColumnarInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_columnar_instance_with_options(request, runtime)

    async def attach_columnar_instance_async(
        self,
        request: polardbx_20200202_models.AttachColumnarInstanceRequest,
    ) -> polardbx_20200202_models.AttachColumnarInstanceResponse:
        """
        @param request: AttachColumnarInstanceRequest
        @return: AttachColumnarInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_columnar_instance_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        """
        @summary 取消主动运维任务
        
        @param request: CancelActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_active_operation_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        """
        @summary 取消主动运维任务
        
        @param request: CancelActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_active_operation_tasks(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        """
        @summary 取消主动运维任务
        
        @param request: CancelActiveOperationTasksRequest
        @return: CancelActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    async def cancel_active_operation_tasks_async(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        """
        @summary 取消主动运维任务
        
        @param request: CancelActiveOperationTasksRequest
        @return: CancelActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_active_operation_tasks_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: polardbx_20200202_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: polardbx_20200202_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: polardbx_20200202_models.ChangeResourceGroupRequest,
    ) -> polardbx_20200202_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: polardbx_20200202_models.ChangeResourceGroupRequest,
    ) -> polardbx_20200202_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        """
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        """
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        """
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        """
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def check_sql_audit_sls_status_with_options(
        self,
        request: polardbx_20200202_models.CheckSqlAuditSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckSqlAuditSlsStatusResponse:
        """
        @param request: CheckSqlAuditSlsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSqlAuditSlsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSqlAuditSlsStatus',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckSqlAuditSlsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sql_audit_sls_status_with_options_async(
        self,
        request: polardbx_20200202_models.CheckSqlAuditSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckSqlAuditSlsStatusResponse:
        """
        @param request: CheckSqlAuditSlsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSqlAuditSlsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSqlAuditSlsStatus',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckSqlAuditSlsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sql_audit_sls_status(
        self,
        request: polardbx_20200202_models.CheckSqlAuditSlsStatusRequest,
    ) -> polardbx_20200202_models.CheckSqlAuditSlsStatusResponse:
        """
        @param request: CheckSqlAuditSlsStatusRequest
        @return: CheckSqlAuditSlsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_sql_audit_sls_status_with_options(request, runtime)

    async def check_sql_audit_sls_status_async(
        self,
        request: polardbx_20200202_models.CheckSqlAuditSlsStatusRequest,
    ) -> polardbx_20200202_models.CheckSqlAuditSlsStatusResponse:
        """
        @param request: CheckSqlAuditSlsStatusRequest
        @return: CheckSqlAuditSlsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_sql_audit_sls_status_with_options_async(request, runtime)

    def close_engine_migration_with_options(
        self,
        request: polardbx_20200202_models.CloseEngineMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CloseEngineMigrationResponse:
        """
        @summary 取消实例迁移
        
        @param request: CloseEngineMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseEngineMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEngineMigration',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CloseEngineMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_engine_migration_with_options_async(
        self,
        request: polardbx_20200202_models.CloseEngineMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CloseEngineMigrationResponse:
        """
        @summary 取消实例迁移
        
        @param request: CloseEngineMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseEngineMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEngineMigration',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CloseEngineMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_engine_migration(
        self,
        request: polardbx_20200202_models.CloseEngineMigrationRequest,
    ) -> polardbx_20200202_models.CloseEngineMigrationResponse:
        """
        @summary 取消实例迁移
        
        @param request: CloseEngineMigrationRequest
        @return: CloseEngineMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_engine_migration_with_options(request, runtime)

    async def close_engine_migration_async(
        self,
        request: polardbx_20200202_models.CloseEngineMigrationRequest,
    ) -> polardbx_20200202_models.CloseEngineMigrationResponse:
        """
        @summary 取消实例迁移
        
        @param request: CloseEngineMigrationRequest
        @return: CloseEngineMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_engine_migration_with_options_async(request, runtime)

    def confirm_no_connection_with_options(
        self,
        request: polardbx_20200202_models.ConfirmNoConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ConfirmNoConnectionResponse:
        """
        @summary 回滚切换时确认无连接
        
        @param request: ConfirmNoConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmNoConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmNoConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ConfirmNoConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_no_connection_with_options_async(
        self,
        request: polardbx_20200202_models.ConfirmNoConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ConfirmNoConnectionResponse:
        """
        @summary 回滚切换时确认无连接
        
        @param request: ConfirmNoConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmNoConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmNoConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ConfirmNoConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_no_connection(
        self,
        request: polardbx_20200202_models.ConfirmNoConnectionRequest,
    ) -> polardbx_20200202_models.ConfirmNoConnectionResponse:
        """
        @summary 回滚切换时确认无连接
        
        @param request: ConfirmNoConnectionRequest
        @return: ConfirmNoConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_no_connection_with_options(request, runtime)

    async def confirm_no_connection_async(
        self,
        request: polardbx_20200202_models.ConfirmNoConnectionRequest,
    ) -> polardbx_20200202_models.ConfirmNoConnectionResponse:
        """
        @summary 回滚切换时确认无连接
        
        @param request: ConfirmNoConnectionRequest
        @return: ConfirmNoConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.confirm_no_connection_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        """
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        """
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        """
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        """
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        """
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        """
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        """
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        """
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_custom_endpoint_with_options(
        self,
        request: polardbx_20200202_models.CreateCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateCustomEndpointResponse:
        """
        @summary 创建自定义endpoint
        
        @param request: CreateCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_endpoint_with_options_async(
        self,
        request: polardbx_20200202_models.CreateCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateCustomEndpointResponse:
        """
        @summary 创建自定义endpoint
        
        @param request: CreateCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_endpoint(
        self,
        request: polardbx_20200202_models.CreateCustomEndpointRequest,
    ) -> polardbx_20200202_models.CreateCustomEndpointResponse:
        """
        @summary 创建自定义endpoint
        
        @param request: CreateCustomEndpointRequest
        @return: CreateCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_endpoint_with_options(request, runtime)

    async def create_custom_endpoint_async(
        self,
        request: polardbx_20200202_models.CreateCustomEndpointRequest,
    ) -> polardbx_20200202_models.CreateCustomEndpointResponse:
        """
        @summary 创建自定义endpoint
        
        @param request: CreateCustomEndpointRequest
        @return: CreateCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_endpoint_with_options_async(request, runtime)

    def create_dbwith_options(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBResponse:
        """
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.charset):
            query['Charset'] = request.charset
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_description):
            query['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbwith_options_async(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBResponse:
        """
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.charset):
            query['Charset'] = request.charset
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_description):
            query['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_db(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
    ) -> polardbx_20200202_models.CreateDBResponse:
        """
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    async def create_db_async(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
    ) -> polardbx_20200202_models.CreateDBResponse:
        """
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbwith_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: polardbx_20200202_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        """
        @summary 创建实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = polardbx_20200202_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra_params):
            request.extra_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra_params, 'ExtraParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cn_class):
            query['CnClass'] = request.cn_class
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_count):
            query['DBNodeCount'] = request.dbnode_count
        if not UtilClient.is_unset(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not UtilClient.is_unset(request.dn_class):
            query['DnClass'] = request.dn_class
        if not UtilClient.is_unset(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.extra_params_shrink):
            query['ExtraParams'] = request.extra_params_shrink
        if not UtilClient.is_unset(request.is_columnar_read_dbinstance):
            query['IsColumnarReadDBInstance'] = request.is_columnar_read_dbinstance
        if not UtilClient.is_unset(request.is_read_dbinstance):
            query['IsReadDBInstance'] = request.is_read_dbinstance
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.primary_dbinstance_name):
            query['PrimaryDBInstanceName'] = request.primary_dbinstance_name
        if not UtilClient.is_unset(request.primary_zone):
            query['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.secondary_zone):
            query['SecondaryZone'] = request.secondary_zone
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
        if not UtilClient.is_unset(request.tertiary_zone):
            query['TertiaryZone'] = request.tertiary_zone
        if not UtilClient.is_unset(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        tmp_req: polardbx_20200202_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        """
        @summary 创建实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = polardbx_20200202_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra_params):
            request.extra_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra_params, 'ExtraParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cn_class):
            query['CnClass'] = request.cn_class
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_count):
            query['DBNodeCount'] = request.dbnode_count
        if not UtilClient.is_unset(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not UtilClient.is_unset(request.dn_class):
            query['DnClass'] = request.dn_class
        if not UtilClient.is_unset(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.extra_params_shrink):
            query['ExtraParams'] = request.extra_params_shrink
        if not UtilClient.is_unset(request.is_columnar_read_dbinstance):
            query['IsColumnarReadDBInstance'] = request.is_columnar_read_dbinstance
        if not UtilClient.is_unset(request.is_read_dbinstance):
            query['IsReadDBInstance'] = request.is_read_dbinstance
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.primary_dbinstance_name):
            query['PrimaryDBInstanceName'] = request.primary_dbinstance_name
        if not UtilClient.is_unset(request.primary_zone):
            query['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.secondary_zone):
            query['SecondaryZone'] = request.secondary_zone
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
        if not UtilClient.is_unset(request.tertiary_zone):
            query['TertiaryZone'] = request.tertiary_zone
        if not UtilClient.is_unset(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_data_import_task_with_options(
        self,
        request: polardbx_20200202_models.CreateDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDataImportTaskResponse:
        """
        @summary 创建评估升级的数据迁移任务
        
        @param request: CreateDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_db):
            query['SrcDb'] = request.src_db
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.CreateDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDataImportTaskResponse:
        """
        @summary 创建评估升级的数据迁移任务
        
        @param request: CreateDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_db):
            query['SrcDb'] = request.src_db
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_import_task(
        self,
        request: polardbx_20200202_models.CreateDataImportTaskRequest,
    ) -> polardbx_20200202_models.CreateDataImportTaskResponse:
        """
        @summary 创建评估升级的数据迁移任务
        
        @param request: CreateDataImportTaskRequest
        @return: CreateDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_import_task_with_options(request, runtime)

    async def create_data_import_task_async(
        self,
        request: polardbx_20200202_models.CreateDataImportTaskRequest,
    ) -> polardbx_20200202_models.CreateDataImportTaskResponse:
        """
        @summary 创建评估升级的数据迁移任务
        
        @param request: CreateDataImportTaskRequest
        @return: CreateDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_import_task_with_options_async(request, runtime)

    def create_gdn_instance_with_options(
        self,
        request: polardbx_20200202_models.CreateGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateGdnInstanceResponse:
        """
        @summary 创建GDN实例
        
        @param request: CreateGdnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGdnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gdn_mode):
            query['GdnMode'] = request.gdn_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpl_conflict_strategy):
            query['RplConflictStrategy'] = request.rpl_conflict_strategy
        if not UtilClient.is_unset(request.rpl_dml_strategy):
            query['RplDmlStrategy'] = request.rpl_dml_strategy
        if not UtilClient.is_unset(request.rpl_sync_ddl):
            query['RplSyncDdl'] = request.rpl_sync_ddl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGdnInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gdn_instance_with_options_async(
        self,
        request: polardbx_20200202_models.CreateGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateGdnInstanceResponse:
        """
        @summary 创建GDN实例
        
        @param request: CreateGdnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGdnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gdn_mode):
            query['GdnMode'] = request.gdn_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpl_conflict_strategy):
            query['RplConflictStrategy'] = request.rpl_conflict_strategy
        if not UtilClient.is_unset(request.rpl_dml_strategy):
            query['RplDmlStrategy'] = request.rpl_dml_strategy
        if not UtilClient.is_unset(request.rpl_sync_ddl):
            query['RplSyncDdl'] = request.rpl_sync_ddl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGdnInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateGdnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gdn_instance(
        self,
        request: polardbx_20200202_models.CreateGdnInstanceRequest,
    ) -> polardbx_20200202_models.CreateGdnInstanceResponse:
        """
        @summary 创建GDN实例
        
        @param request: CreateGdnInstanceRequest
        @return: CreateGdnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gdn_instance_with_options(request, runtime)

    async def create_gdn_instance_async(
        self,
        request: polardbx_20200202_models.CreateGdnInstanceRequest,
    ) -> polardbx_20200202_models.CreateGdnInstanceResponse:
        """
        @summary 创建GDN实例
        
        @param request: CreateGdnInstanceRequest
        @return: CreateGdnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_gdn_instance_with_options_async(request, runtime)

    def create_rpl_inspection_task_with_options(
        self,
        request: polardbx_20200202_models.CreateRplInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateRplInspectionTaskResponse:
        """
        @summary 创建评估预检任务
        
        @param request: CreateRplInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRplInspectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRplInspectionTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateRplInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rpl_inspection_task_with_options_async(
        self,
        request: polardbx_20200202_models.CreateRplInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateRplInspectionTaskResponse:
        """
        @summary 创建评估预检任务
        
        @param request: CreateRplInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRplInspectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRplInspectionTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateRplInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rpl_inspection_task(
        self,
        request: polardbx_20200202_models.CreateRplInspectionTaskRequest,
    ) -> polardbx_20200202_models.CreateRplInspectionTaskResponse:
        """
        @summary 创建评估预检任务
        
        @param request: CreateRplInspectionTaskRequest
        @return: CreateRplInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rpl_inspection_task_with_options(request, runtime)

    async def create_rpl_inspection_task_async(
        self,
        request: polardbx_20200202_models.CreateRplInspectionTaskRequest,
    ) -> polardbx_20200202_models.CreateRplInspectionTaskResponse:
        """
        @summary 创建评估预检任务
        
        @param request: CreateRplInspectionTaskRequest
        @return: CreateRplInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rpl_inspection_task_with_options_async(request, runtime)

    def create_sqlevaluate_task_with_options(
        self,
        request: polardbx_20200202_models.CreateSQLEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSQLEvaluateTaskResponse:
        """
        @summary 创建评估升级的兼容性评估任务
        
        @param request: CreateSQLEvaluateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSQLEvaluateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_desc):
            query['SlinkTaskDesc'] = request.slink_task_desc
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_db):
            query['SrcDb'] = request.src_db
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not UtilClient.is_unset(request.src_res_type):
            query['SrcResType'] = request.src_res_type
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLEvaluateTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSQLEvaluateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sqlevaluate_task_with_options_async(
        self,
        request: polardbx_20200202_models.CreateSQLEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSQLEvaluateTaskResponse:
        """
        @summary 创建评估升级的兼容性评估任务
        
        @param request: CreateSQLEvaluateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSQLEvaluateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_db):
            query['DstDb'] = request.dst_db
        if not UtilClient.is_unset(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not UtilClient.is_unset(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not UtilClient.is_unset(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_desc):
            query['SlinkTaskDesc'] = request.slink_task_desc
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_db):
            query['SrcDb'] = request.src_db
        if not UtilClient.is_unset(request.src_password):
            query['SrcPassword'] = request.src_password
        if not UtilClient.is_unset(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not UtilClient.is_unset(request.src_res_type):
            query['SrcResType'] = request.src_res_type
        if not UtilClient.is_unset(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLEvaluateTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSQLEvaluateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sqlevaluate_task(
        self,
        request: polardbx_20200202_models.CreateSQLEvaluateTaskRequest,
    ) -> polardbx_20200202_models.CreateSQLEvaluateTaskResponse:
        """
        @summary 创建评估升级的兼容性评估任务
        
        @param request: CreateSQLEvaluateTaskRequest
        @return: CreateSQLEvaluateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sqlevaluate_task_with_options(request, runtime)

    async def create_sqlevaluate_task_async(
        self,
        request: polardbx_20200202_models.CreateSQLEvaluateTaskRequest,
    ) -> polardbx_20200202_models.CreateSQLEvaluateTaskResponse:
        """
        @summary 创建评估升级的兼容性评估任务
        
        @param request: CreateSQLEvaluateTaskRequest
        @return: CreateSQLEvaluateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sqlevaluate_task_with_options_async(request, runtime)

    def create_storage_pool_with_options(
        self,
        request: polardbx_20200202_models.CreateStoragePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateStoragePoolResponse:
        """
        @summary 创建 PolarDB-X 存储资源池
        
        @param request: CreateStoragePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoragePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_pool_dnlist):
            query['StoragePoolDNList'] = request.storage_pool_dnlist
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStoragePool',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateStoragePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_pool_with_options_async(
        self,
        request: polardbx_20200202_models.CreateStoragePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateStoragePoolResponse:
        """
        @summary 创建 PolarDB-X 存储资源池
        
        @param request: CreateStoragePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoragePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_pool_dnlist):
            query['StoragePoolDNList'] = request.storage_pool_dnlist
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStoragePool',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateStoragePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_pool(
        self,
        request: polardbx_20200202_models.CreateStoragePoolRequest,
    ) -> polardbx_20200202_models.CreateStoragePoolResponse:
        """
        @summary 创建 PolarDB-X 存储资源池
        
        @param request: CreateStoragePoolRequest
        @return: CreateStoragePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_storage_pool_with_options(request, runtime)

    async def create_storage_pool_async(
        self,
        request: polardbx_20200202_models.CreateStoragePoolRequest,
    ) -> polardbx_20200202_models.CreateStoragePoolResponse:
        """
        @summary 创建 PolarDB-X 存储资源池
        
        @param request: CreateStoragePoolRequest
        @return: CreateStoragePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_pool_with_options_async(request, runtime)

    def create_structure_import_task_with_options(
        self,
        request: polardbx_20200202_models.CreateStructureImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateStructureImportTaskResponse:
        """
        @summary 创建评估升级的结构迁移任务
        
        @param request: CreateStructureImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStructureImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStructureImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateStructureImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_structure_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.CreateStructureImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateStructureImportTaskResponse:
        """
        @summary 创建评估升级的结构迁移任务
        
        @param request: CreateStructureImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStructureImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStructureImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateStructureImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_structure_import_task(
        self,
        request: polardbx_20200202_models.CreateStructureImportTaskRequest,
    ) -> polardbx_20200202_models.CreateStructureImportTaskResponse:
        """
        @summary 创建评估升级的结构迁移任务
        
        @param request: CreateStructureImportTaskRequest
        @return: CreateStructureImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_structure_import_task_with_options(request, runtime)

    async def create_structure_import_task_async(
        self,
        request: polardbx_20200202_models.CreateStructureImportTaskRequest,
    ) -> polardbx_20200202_models.CreateStructureImportTaskResponse:
        """
        @summary 创建评估升级的结构迁移任务
        
        @param request: CreateStructureImportTaskRequest
        @return: CreateStructureImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_structure_import_task_with_options_async(request, runtime)

    def create_super_account_with_options(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        """
        @param request: CreateSuperAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSuperAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSuperAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSuperAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_super_account_with_options_async(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        """
        @param request: CreateSuperAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSuperAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSuperAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSuperAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_super_account(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        """
        @param request: CreateSuperAccountRequest
        @return: CreateSuperAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_super_account_with_options(request, runtime)

    async def create_super_account_async(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        """
        @param request: CreateSuperAccountRequest
        @return: CreateSuperAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_super_account_with_options_async(request, runtime)

    def create_transform_operation_with_options(
        self,
        request: polardbx_20200202_models.CreateTransformOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateTransformOperationResponse:
        """
        @summary 创建标准版迁移到企业版的操作任务
        
        @param request: CreateTransformOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTransformOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransformOperation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateTransformOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transform_operation_with_options_async(
        self,
        request: polardbx_20200202_models.CreateTransformOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateTransformOperationResponse:
        """
        @summary 创建标准版迁移到企业版的操作任务
        
        @param request: CreateTransformOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTransformOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransformOperation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateTransformOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transform_operation(
        self,
        request: polardbx_20200202_models.CreateTransformOperationRequest,
    ) -> polardbx_20200202_models.CreateTransformOperationResponse:
        """
        @summary 创建标准版迁移到企业版的操作任务
        
        @param request: CreateTransformOperationRequest
        @return: CreateTransformOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transform_operation_with_options(request, runtime)

    async def create_transform_operation_async(
        self,
        request: polardbx_20200202_models.CreateTransformOperationRequest,
    ) -> polardbx_20200202_models.CreateTransformOperationResponse:
        """
        @summary 创建标准版迁移到企业版的操作任务
        
        @param request: CreateTransformOperationRequest
        @return: CreateTransformOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_transform_operation_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        """
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        """
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        """
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        """
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_custom_endpoint_with_options(
        self,
        request: polardbx_20200202_models.DeleteCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteCustomEndpointResponse:
        """
        @summary 删除自定义endpoint
        
        @param request: DeleteCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_endpoint_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteCustomEndpointResponse:
        """
        @summary 删除自定义endpoint
        
        @param request: DeleteCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_endpoint(
        self,
        request: polardbx_20200202_models.DeleteCustomEndpointRequest,
    ) -> polardbx_20200202_models.DeleteCustomEndpointResponse:
        """
        @summary 删除自定义endpoint
        
        @param request: DeleteCustomEndpointRequest
        @return: DeleteCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_endpoint_with_options(request, runtime)

    async def delete_custom_endpoint_async(
        self,
        request: polardbx_20200202_models.DeleteCustomEndpointRequest,
    ) -> polardbx_20200202_models.DeleteCustomEndpointResponse:
        """
        @summary 删除自定义endpoint
        
        @param request: DeleteCustomEndpointRequest
        @return: DeleteCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_endpoint_with_options_async(request, runtime)

    def delete_dbwith_options(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        """
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbwith_options_async(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        """
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_db(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        """
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    async def delete_db_async(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        """
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbwith_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        """
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        """
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        """
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        """
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_evaluate_and_import_task_with_options(
        self,
        request: polardbx_20200202_models.DeleteEvaluateAndImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse:
        """
        @summary 删除评估导入任务
        
        @param request: DeleteEvaluateAndImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEvaluateAndImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEvaluateAndImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluate_and_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteEvaluateAndImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse:
        """
        @summary 删除评估导入任务
        
        @param request: DeleteEvaluateAndImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEvaluateAndImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEvaluateAndImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluate_and_import_task(
        self,
        request: polardbx_20200202_models.DeleteEvaluateAndImportTaskRequest,
    ) -> polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse:
        """
        @summary 删除评估导入任务
        
        @param request: DeleteEvaluateAndImportTaskRequest
        @return: DeleteEvaluateAndImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_evaluate_and_import_task_with_options(request, runtime)

    async def delete_evaluate_and_import_task_async(
        self,
        request: polardbx_20200202_models.DeleteEvaluateAndImportTaskRequest,
    ) -> polardbx_20200202_models.DeleteEvaluateAndImportTaskResponse:
        """
        @summary 删除评估导入任务
        
        @param request: DeleteEvaluateAndImportTaskRequest
        @return: DeleteEvaluateAndImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_evaluate_and_import_task_with_options_async(request, runtime)

    def delete_gdn_instance_with_options(
        self,
        request: polardbx_20200202_models.DeleteGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteGdnInstanceResponse:
        """
        @summary 删除GDN实例
        
        @param request: DeleteGdnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGdnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdn_instance_name):
            query['GdnInstanceName'] = request.gdn_instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGdnInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gdn_instance_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteGdnInstanceResponse:
        """
        @summary 删除GDN实例
        
        @param request: DeleteGdnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGdnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdn_instance_name):
            query['GdnInstanceName'] = request.gdn_instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGdnInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteGdnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gdn_instance(
        self,
        request: polardbx_20200202_models.DeleteGdnInstanceRequest,
    ) -> polardbx_20200202_models.DeleteGdnInstanceResponse:
        """
        @summary 删除GDN实例
        
        @param request: DeleteGdnInstanceRequest
        @return: DeleteGdnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gdn_instance_with_options(request, runtime)

    async def delete_gdn_instance_async(
        self,
        request: polardbx_20200202_models.DeleteGdnInstanceRequest,
    ) -> polardbx_20200202_models.DeleteGdnInstanceResponse:
        """
        @summary 删除GDN实例
        
        @param request: DeleteGdnInstanceRequest
        @return: DeleteGdnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gdn_instance_with_options_async(request, runtime)

    def describe_account_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        """
        @param request: DescribeAccountListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAccountListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        """
        @param request: DescribeAccountListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAccountListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_list(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        """
        @param request: DescribeAccountListRequest
        @return: DescribeAccountListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_list_with_options(request, runtime)

    async def describe_account_list_async(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        """
        @param request: DescribeAccountListRequest
        @return: DescribeAccountListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_list_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary 展示全局运维窗口配置
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationMaintainConf',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_maintain_conf_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary 展示全局运维窗口配置
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationMaintainConf',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_maintain_conf(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary 展示全局运维窗口配置
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @return: DescribeActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    async def describe_active_operation_maintain_conf_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary 展示全局运维窗口配置
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @return: DescribeActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_maintain_conf_with_options_async(request, runtime)

    def describe_active_operation_task_count_with_options(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary 获取主动运维任务数量
        
        @param request: DescribeActiveOperationTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskCount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_count_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary 获取主动运维任务数量
        
        @param request: DescribeActiveOperationTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskCount',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTaskCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_count(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary 获取主动运维任务数量
        
        @param request: DescribeActiveOperationTaskCountRequest
        @return: DescribeActiveOperationTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    async def describe_active_operation_task_count_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary 获取主动运维任务数量
        
        @param request: DescribeActiveOperationTaskCountRequest
        @return: DescribeActiveOperationTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_count_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTasksResponse:
        """
        @summary 获取待执行自动运维任务列表
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTasksResponse:
        """
        @summary 获取待执行自动运维任务列表
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTasksResponse:
        """
        @summary 获取待执行自动运维任务列表
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTasksResponse:
        """
        @summary 获取待执行自动运维任务列表
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_archive_table_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeArchiveTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeArchiveTableListResponse:
        """
        @summary 冷存储表列表
        
        @param request: DescribeArchiveTableListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeArchiveTableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeArchiveTableList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeArchiveTableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_archive_table_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeArchiveTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeArchiveTableListResponse:
        """
        @summary 冷存储表列表
        
        @param request: DescribeArchiveTableListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeArchiveTableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeArchiveTableList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeArchiveTableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_archive_table_list(
        self,
        request: polardbx_20200202_models.DescribeArchiveTableListRequest,
    ) -> polardbx_20200202_models.DescribeArchiveTableListResponse:
        """
        @summary 冷存储表列表
        
        @param request: DescribeArchiveTableListRequest
        @return: DescribeArchiveTableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_archive_table_list_with_options(request, runtime)

    async def describe_archive_table_list_async(
        self,
        request: polardbx_20200202_models.DescribeArchiveTableListRequest,
    ) -> polardbx_20200202_models.DescribeArchiveTableListResponse:
        """
        @summary 冷存储表列表
        
        @param request: DescribeArchiveTableListRequest
        @return: DescribeArchiveTableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_archive_table_list_with_options_async(request, runtime)

    def describe_available_cross_regions_with_options(
        self,
        request: polardbx_20200202_models.DescribeAvailableCrossRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAvailableCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeAvailableCrossRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableCrossRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAvailableCrossRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_cross_regions_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeAvailableCrossRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAvailableCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeAvailableCrossRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableCrossRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAvailableCrossRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_cross_regions(
        self,
        request: polardbx_20200202_models.DescribeAvailableCrossRegionsRequest,
    ) -> polardbx_20200202_models.DescribeAvailableCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeAvailableCrossRegionsRequest
        @return: DescribeAvailableCrossRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_regions_with_options(request, runtime)

    async def describe_available_cross_regions_async(
        self,
        request: polardbx_20200202_models.DescribeAvailableCrossRegionsRequest,
    ) -> polardbx_20200202_models.DescribeAvailableCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeAvailableCrossRegionsRequest
        @return: DescribeAvailableCrossRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_cross_regions_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_set_with_options(
        self,
        request: polardbx_20200202_models.DescribeBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetResponse:
        """
        @summary 备份集详情
        
        @param request: DescribeBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetResponse:
        """
        @summary 备份集详情
        
        @param request: DescribeBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set(
        self,
        request: polardbx_20200202_models.DescribeBackupSetRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetResponse:
        """
        @summary 备份集详情
        
        @param request: DescribeBackupSetRequest
        @return: DescribeBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_with_options(request, runtime)

    async def describe_backup_set_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetResponse:
        """
        @summary 备份集详情
        
        @param request: DescribeBackupSetRequest
        @return: DescribeBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_with_options_async(request, runtime)

    def describe_backup_set_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        """
        @param request: DescribeBackupSetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        """
        @param request: DescribeBackupSetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set_list(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        """
        @param request: DescribeBackupSetListRequest
        @return: DescribeBackupSetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_list_with_options(request, runtime)

    async def describe_backup_set_list_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        """
        @param request: DescribeBackupSetListRequest
        @return: DescribeBackupSetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_list_with_options_async(request, runtime)

    def describe_binary_log_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        """
        @param request: DescribeBinaryLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBinaryLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBinaryLogList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBinaryLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_binary_log_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        """
        @param request: DescribeBinaryLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBinaryLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBinaryLogList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBinaryLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_binary_log_list(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        """
        @param request: DescribeBinaryLogListRequest
        @return: DescribeBinaryLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_binary_log_list_with_options(request, runtime)

    async def describe_binary_log_list_async(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        """
        @param request: DescribeBinaryLogListRequest
        @return: DescribeBinaryLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_binary_log_list_with_options_async(request, runtime)

    def describe_cdc_class_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeCdcClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcClassListResponse:
        """
        @summary 查询多流规格列表
        
        @param request: DescribeCdcClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcClassList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcClassListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_class_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCdcClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcClassListResponse:
        """
        @summary 查询多流规格列表
        
        @param request: DescribeCdcClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcClassList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcClassListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_class_list(
        self,
        request: polardbx_20200202_models.DescribeCdcClassListRequest,
    ) -> polardbx_20200202_models.DescribeCdcClassListResponse:
        """
        @summary 查询多流规格列表
        
        @param request: DescribeCdcClassListRequest
        @return: DescribeCdcClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdc_class_list_with_options(request, runtime)

    async def describe_cdc_class_list_async(
        self,
        request: polardbx_20200202_models.DescribeCdcClassListRequest,
    ) -> polardbx_20200202_models.DescribeCdcClassListResponse:
        """
        @summary 查询多流规格列表
        
        @param request: DescribeCdcClassListRequest
        @return: DescribeCdcClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdc_class_list_with_options_async(request, runtime)

    def describe_cdc_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeCdcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcInfoResponse:
        """
        @summary 查询CDC信息
        
        @param request: DescribeCdcInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCdcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcInfoResponse:
        """
        @summary 查询CDC信息
        
        @param request: DescribeCdcInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_info(
        self,
        request: polardbx_20200202_models.DescribeCdcInfoRequest,
    ) -> polardbx_20200202_models.DescribeCdcInfoResponse:
        """
        @summary 查询CDC信息
        
        @param request: DescribeCdcInfoRequest
        @return: DescribeCdcInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdc_info_with_options(request, runtime)

    async def describe_cdc_info_async(
        self,
        request: polardbx_20200202_models.DescribeCdcInfoRequest,
    ) -> polardbx_20200202_models.DescribeCdcInfoResponse:
        """
        @summary 查询CDC信息
        
        @param request: DescribeCdcInfoRequest
        @return: DescribeCdcInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdc_info_with_options_async(request, runtime)

    def describe_cdc_version_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeCdcVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcVersionListResponse:
        """
        @summary 获取CDC版本列表
        
        @param request: DescribeCdcVersionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcVersionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcVersionList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_version_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCdcVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCdcVersionListResponse:
        """
        @summary 获取CDC版本列表
        
        @param request: DescribeCdcVersionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdcVersionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdcVersionList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCdcVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_version_list(
        self,
        request: polardbx_20200202_models.DescribeCdcVersionListRequest,
    ) -> polardbx_20200202_models.DescribeCdcVersionListResponse:
        """
        @summary 获取CDC版本列表
        
        @param request: DescribeCdcVersionListRequest
        @return: DescribeCdcVersionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdc_version_list_with_options(request, runtime)

    async def describe_cdc_version_list_async(
        self,
        request: polardbx_20200202_models.DescribeCdcVersionListRequest,
    ) -> polardbx_20200202_models.DescribeCdcVersionListResponse:
        """
        @summary 获取CDC版本列表
        
        @param request: DescribeCdcVersionListRequest
        @return: DescribeCdcVersionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdc_version_list_with_options_async(request, runtime)

    def describe_character_set_with_options(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        """
        @param request: DescribeCharacterSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharacterSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCharacterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_character_set_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        """
        @param request: DescribeCharacterSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharacterSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCharacterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_character_set(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        """
        @param request: DescribeCharacterSetRequest
        @return: DescribeCharacterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_with_options(request, runtime)

    async def describe_character_set_async(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        """
        @param request: DescribeCharacterSetRequest
        @return: DescribeCharacterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_with_options_async(request, runtime)

    def describe_cold_data_basic_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeColdDataBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColdDataBasicInfoResponse:
        """
        @summary 冷存储基础信息
        
        @param request: DescribeColdDataBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColdDataBasicInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColdDataBasicInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColdDataBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cold_data_basic_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeColdDataBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColdDataBasicInfoResponse:
        """
        @summary 冷存储基础信息
        
        @param request: DescribeColdDataBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColdDataBasicInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColdDataBasicInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColdDataBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cold_data_basic_info(
        self,
        request: polardbx_20200202_models.DescribeColdDataBasicInfoRequest,
    ) -> polardbx_20200202_models.DescribeColdDataBasicInfoResponse:
        """
        @summary 冷存储基础信息
        
        @param request: DescribeColdDataBasicInfoRequest
        @return: DescribeColdDataBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cold_data_basic_info_with_options(request, runtime)

    async def describe_cold_data_basic_info_async(
        self,
        request: polardbx_20200202_models.DescribeColdDataBasicInfoRequest,
    ) -> polardbx_20200202_models.DescribeColdDataBasicInfoResponse:
        """
        @summary 冷存储基础信息
        
        @param request: DescribeColdDataBasicInfoRequest
        @return: DescribeColdDataBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cold_data_basic_info_with_options_async(request, runtime)

    def describe_columnar_class_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeColumnarClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarClassListResponse:
        """
        @summary 查询列存规格列表
        
        @param request: DescribeColumnarClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarClassList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarClassListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_class_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarClassListResponse:
        """
        @summary 查询列存规格列表
        
        @param request: DescribeColumnarClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarClassList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarClassListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_class_list(
        self,
        request: polardbx_20200202_models.DescribeColumnarClassListRequest,
    ) -> polardbx_20200202_models.DescribeColumnarClassListResponse:
        """
        @summary 查询列存规格列表
        
        @param request: DescribeColumnarClassListRequest
        @return: DescribeColumnarClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columnar_class_list_with_options(request, runtime)

    async def describe_columnar_class_list_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarClassListRequest,
    ) -> polardbx_20200202_models.DescribeColumnarClassListResponse:
        """
        @summary 查询列存规格列表
        
        @param request: DescribeColumnarClassListRequest
        @return: DescribeColumnarClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columnar_class_list_with_options_async(request, runtime)

    def describe_columnar_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeColumnarInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarInfoResponse:
        """
        @summary 查询Columnar信息
        
        @param request: DescribeColumnarInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarInfoResponse:
        """
        @summary 查询Columnar信息
        
        @param request: DescribeColumnarInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_info(
        self,
        request: polardbx_20200202_models.DescribeColumnarInfoRequest,
    ) -> polardbx_20200202_models.DescribeColumnarInfoResponse:
        """
        @summary 查询Columnar信息
        
        @param request: DescribeColumnarInfoRequest
        @return: DescribeColumnarInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columnar_info_with_options(request, runtime)

    async def describe_columnar_info_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarInfoRequest,
    ) -> polardbx_20200202_models.DescribeColumnarInfoResponse:
        """
        @summary 查询Columnar信息
        
        @param request: DescribeColumnarInfoRequest
        @return: DescribeColumnarInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columnar_info_with_options_async(request, runtime)

    def describe_columnar_version_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeColumnarVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarVersionListResponse:
        """
        @summary 获取Columnar版本列表
        
        @param request: DescribeColumnarVersionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarVersionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarVersionList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_version_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeColumnarVersionListResponse:
        """
        @summary 获取Columnar版本列表
        
        @param request: DescribeColumnarVersionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnarVersionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnarVersionList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeColumnarVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_version_list(
        self,
        request: polardbx_20200202_models.DescribeColumnarVersionListRequest,
    ) -> polardbx_20200202_models.DescribeColumnarVersionListResponse:
        """
        @summary 获取Columnar版本列表
        
        @param request: DescribeColumnarVersionListRequest
        @return: DescribeColumnarVersionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columnar_version_list_with_options(request, runtime)

    async def describe_columnar_version_list_async(
        self,
        request: polardbx_20200202_models.DescribeColumnarVersionListRequest,
    ) -> polardbx_20200202_models.DescribeColumnarVersionListResponse:
        """
        @summary 获取Columnar版本列表
        
        @param request: DescribeColumnarVersionListRequest
        @return: DescribeColumnarVersionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columnar_version_list_with_options_async(request, runtime)

    def describe_component_propeties_with_options(
        self,
        request: polardbx_20200202_models.DescribeComponentPropetiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeComponentPropetiesResponse:
        """
        @summary 查询PolarDB-X 实例指定组件的属性列表
        
        @param request: DescribeComponentPropetiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentPropetiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPropeties',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeComponentPropetiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_propeties_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeComponentPropetiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeComponentPropetiesResponse:
        """
        @summary 查询PolarDB-X 实例指定组件的属性列表
        
        @param request: DescribeComponentPropetiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentPropetiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPropeties',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeComponentPropetiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_propeties(
        self,
        request: polardbx_20200202_models.DescribeComponentPropetiesRequest,
    ) -> polardbx_20200202_models.DescribeComponentPropetiesResponse:
        """
        @summary 查询PolarDB-X 实例指定组件的属性列表
        
        @param request: DescribeComponentPropetiesRequest
        @return: DescribeComponentPropetiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_component_propeties_with_options(request, runtime)

    async def describe_component_propeties_async(
        self,
        request: polardbx_20200202_models.DescribeComponentPropetiesRequest,
    ) -> polardbx_20200202_models.DescribeComponentPropetiesResponse:
        """
        @summary 查询PolarDB-X 实例指定组件的属性列表
        
        @param request: DescribeComponentPropetiesRequest
        @return: DescribeComponentPropetiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_propeties_with_options_async(request, runtime)

    def describe_custom_endpoint_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeCustomEndpointListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCustomEndpointListResponse:
        """
        @summary 查询自定义连接信息
        
        @param request: DescribeCustomEndpointListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomEndpointListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_delete_cn):
            query['CheckDeleteCN'] = request.check_delete_cn
        if not UtilClient.is_unset(request.custom_endpoint_ids):
            query['CustomEndpointIds'] = request.custom_endpoint_ids
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEndpointList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCustomEndpointListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_endpoint_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCustomEndpointListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCustomEndpointListResponse:
        """
        @summary 查询自定义连接信息
        
        @param request: DescribeCustomEndpointListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomEndpointListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_delete_cn):
            query['CheckDeleteCN'] = request.check_delete_cn
        if not UtilClient.is_unset(request.custom_endpoint_ids):
            query['CustomEndpointIds'] = request.custom_endpoint_ids
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEndpointList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCustomEndpointListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_endpoint_list(
        self,
        request: polardbx_20200202_models.DescribeCustomEndpointListRequest,
    ) -> polardbx_20200202_models.DescribeCustomEndpointListResponse:
        """
        @summary 查询自定义连接信息
        
        @param request: DescribeCustomEndpointListRequest
        @return: DescribeCustomEndpointListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_endpoint_list_with_options(request, runtime)

    async def describe_custom_endpoint_list_async(
        self,
        request: polardbx_20200202_models.DescribeCustomEndpointListRequest,
    ) -> polardbx_20200202_models.DescribeCustomEndpointListResponse:
        """
        @summary 查询自定义连接信息
        
        @param request: DescribeCustomEndpointListRequest
        @return: DescribeCustomEndpointListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_endpoint_list_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 获取实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 获取实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 获取实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 获取实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_config_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例配置信息
        
        @param request: DescribeDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfig',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_config_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例配置信息
        
        @param request: DescribeDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfig',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_config(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例配置信息
        
        @param request: DescribeDBInstanceConfigRequest
        @return: DescribeDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_config_with_options(request, runtime)

    async def describe_dbinstance_config_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例配置信息
        
        @param request: DescribeDBInstanceConfigRequest
        @return: DescribeDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_config_with_options_async(request, runtime)

    def describe_dbinstance_hawith_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceHAResponse:
        """
        @summary 查询实例的HA信息
        
        @param request: DescribeDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHA',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_hawith_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceHAResponse:
        """
        @summary 查询实例的HA信息
        
        @param request: DescribeDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHA',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ha(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceHARequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceHAResponse:
        """
        @summary 查询实例的HA信息
        
        @param request: DescribeDBInstanceHARequest
        @return: DescribeDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_hawith_options(request, runtime)

    async def describe_dbinstance_ha_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceHARequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceHAResponse:
        """
        @summary 查询实例的HA信息
        
        @param request: DescribeDBInstanceHARequest
        @return: DescribeDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_hawith_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        """
        @param request: DescribeDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        """
        @param request: DescribeDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        """
        @param request: DescribeDBInstanceSSLRequest
        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        """
        @param request: DescribeDBInstanceSSLRequest
        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_tdewith_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        """
        @param request: DescribeDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_tdewith_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        """
        @param request: DescribeDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_tde(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        """
        @param request: DescribeDBInstanceTDERequest
        @return: DescribeDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    async def describe_dbinstance_tde_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        """
        @param request: DescribeDBInstanceTDERequest
        @return: DescribeDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdewith_options_async(request, runtime)

    def describe_dbinstance_topology_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        """
        @summary 查询实例拓扑
        
        @param request: DescribeDBInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTopologyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.minute_simple):
            query['MinuteSimple'] = request.minute_simple
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTopology',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_topology_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        """
        @summary 查询实例拓扑
        
        @param request: DescribeDBInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTopologyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.minute_simple):
            query['MinuteSimple'] = request.minute_simple
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTopology',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_topology(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        """
        @summary 查询实例拓扑
        
        @param request: DescribeDBInstanceTopologyRequest
        @return: DescribeDBInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_topology_with_options(request, runtime)

    async def describe_dbinstance_topology_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        """
        @summary 查询实例拓扑
        
        @param request: DescribeDBInstanceTopologyRequest
        @return: DescribeDBInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_topology_with_options_async(request, runtime)

    def describe_dbinstance_via_endpoint_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceViaEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse:
        """
        @summary 通过Endpoint查询实例
        
        @param request: DescribeDBInstanceViaEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceViaEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceViaEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_via_endpoint_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceViaEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse:
        """
        @summary 通过Endpoint查询实例
        
        @param request: DescribeDBInstanceViaEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceViaEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceViaEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_via_endpoint(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceViaEndpointRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse:
        """
        @summary 通过Endpoint查询实例
        
        @param request: DescribeDBInstanceViaEndpointRequest
        @return: DescribeDBInstanceViaEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_via_endpoint_with_options(request, runtime)

    async def describe_dbinstance_via_endpoint_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceViaEndpointRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceViaEndpointResponse:
        """
        @summary 通过Endpoint查询实例
        
        @param request: DescribeDBInstanceViaEndpointRequest
        @return: DescribeDBInstanceViaEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_via_endpoint_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        """
        @summary 获取PolarDB-X实例列表
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_version):
            query['DbVersion'] = request.db_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.must_has_cdc):
            query['MustHasCdc'] = request.must_has_cdc
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        """
        @summary 获取PolarDB-X实例列表
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_version):
            query['DbVersion'] = request.db_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.must_has_cdc):
            query['MustHasCdc'] = request.must_has_cdc
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        """
        @summary 获取PolarDB-X实例列表
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        """
        @summary 获取PolarDB-X实例列表
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbnode_performance_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        """
        @summary 性能监控数据接口
        
        @param request: DescribeDBNodePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.dbnode_role):
            query['DBNodeRole'] = request.dbnode_role
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBNodePerformance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBNodePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbnode_performance_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        """
        @summary 性能监控数据接口
        
        @param request: DescribeDBNodePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.dbnode_role):
            query['DBNodeRole'] = request.dbnode_role
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBNodePerformance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBNodePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbnode_performance(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        """
        @summary 性能监控数据接口
        
        @param request: DescribeDBNodePerformanceRequest
        @return: DescribeDBNodePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    async def describe_dbnode_performance_async(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        """
        @summary 性能监控数据接口
        
        @param request: DescribeDBNodePerformanceRequest
        @return: DescribeDBNodePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnode_performance_with_options_async(request, runtime)

    def describe_data_import_task_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeDataImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDataImportTaskInfoResponse:
        """
        @summary 导入任务详情
        
        @param request: DescribeDataImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not UtilClient.is_unset(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not UtilClient.is_unset(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataImportTaskInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDataImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_import_task_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDataImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDataImportTaskInfoResponse:
        """
        @summary 导入任务详情
        
        @param request: DescribeDataImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not UtilClient.is_unset(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not UtilClient.is_unset(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataImportTaskInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDataImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_import_task_info(
        self,
        request: polardbx_20200202_models.DescribeDataImportTaskInfoRequest,
    ) -> polardbx_20200202_models.DescribeDataImportTaskInfoResponse:
        """
        @summary 导入任务详情
        
        @param request: DescribeDataImportTaskInfoRequest
        @return: DescribeDataImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_task_info_with_options(request, runtime)

    async def describe_data_import_task_info_async(
        self,
        request: polardbx_20200202_models.DescribeDataImportTaskInfoRequest,
    ) -> polardbx_20200202_models.DescribeDataImportTaskInfoResponse:
        """
        @summary 导入任务详情
        
        @param request: DescribeDataImportTaskInfoRequest
        @return: DescribeDataImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_import_task_info_with_options_async(request, runtime)

    def describe_db_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        """
        @param request: DescribeDbListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDbListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_db_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        """
        @param request: DescribeDbListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDbListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_db_list(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        """
        @param request: DescribeDbListRequest
        @return: DescribeDbListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_db_list_with_options(request, runtime)

    async def describe_db_list_async(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        """
        @param request: DescribeDbListRequest
        @return: DescribeDbListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_list_with_options_async(request, runtime)

    def describe_distribute_table_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        """
        @param request: DescribeDistributeTableListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributeTableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributeTableList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDistributeTableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribute_table_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        """
        @param request: DescribeDistributeTableListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistributeTableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistributeTableList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDistributeTableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribute_table_list(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        """
        @param request: DescribeDistributeTableListRequest
        @return: DescribeDistributeTableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_distribute_table_list_with_options(request, runtime)

    async def describe_distribute_table_list_async(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        """
        @param request: DescribeDistributeTableListRequest
        @return: DescribeDistributeTableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_distribute_table_list_with_options_async(request, runtime)

    def describe_enabled_cross_regions_with_options(
        self,
        request: polardbx_20200202_models.DescribeEnabledCrossRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEnabledCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeEnabledCrossRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnabledCrossRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnabledCrossRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEnabledCrossRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enabled_cross_regions_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeEnabledCrossRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEnabledCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeEnabledCrossRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnabledCrossRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnabledCrossRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEnabledCrossRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enabled_cross_regions(
        self,
        request: polardbx_20200202_models.DescribeEnabledCrossRegionsRequest,
    ) -> polardbx_20200202_models.DescribeEnabledCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeEnabledCrossRegionsRequest
        @return: DescribeEnabledCrossRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_enabled_cross_regions_with_options(request, runtime)

    async def describe_enabled_cross_regions_async(
        self,
        request: polardbx_20200202_models.DescribeEnabledCrossRegionsRequest,
    ) -> polardbx_20200202_models.DescribeEnabledCrossRegionsResponse:
        """
        @summary 获取已开启跨地域备份的地域
        
        @param request: DescribeEnabledCrossRegionsRequest
        @return: DescribeEnabledCrossRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_enabled_cross_regions_with_options_async(request, runtime)

    def describe_evaluate_and_import_task_with_options(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse:
        """
        @summary 查询单个评估迁移任务详情
        
        @param request: DescribeEvaluateAndImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEvaluateAndImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluateAndImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_evaluate_and_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse:
        """
        @summary 查询单个评估迁移任务详情
        
        @param request: DescribeEvaluateAndImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEvaluateAndImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluateAndImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_evaluate_and_import_task(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTaskRequest,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse:
        """
        @summary 查询单个评估迁移任务详情
        
        @param request: DescribeEvaluateAndImportTaskRequest
        @return: DescribeEvaluateAndImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_and_import_task_with_options(request, runtime)

    async def describe_evaluate_and_import_task_async(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTaskRequest,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTaskResponse:
        """
        @summary 查询单个评估迁移任务详情
        
        @param request: DescribeEvaluateAndImportTaskRequest
        @return: DescribeEvaluateAndImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_and_import_task_with_options_async(request, runtime)

    def describe_evaluate_and_import_tasks_with_options(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse:
        """
        @summary 请求评估导入任务列表
        
        @param request: DescribeEvaluateAndImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEvaluateAndImportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluateAndImportTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_evaluate_and_import_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse:
        """
        @summary 请求评估导入任务列表
        
        @param request: DescribeEvaluateAndImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEvaluateAndImportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluateAndImportTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_evaluate_and_import_tasks(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTasksRequest,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse:
        """
        @summary 请求评估导入任务列表
        
        @param request: DescribeEvaluateAndImportTasksRequest
        @return: DescribeEvaluateAndImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_and_import_tasks_with_options(request, runtime)

    async def describe_evaluate_and_import_tasks_async(
        self,
        request: polardbx_20200202_models.DescribeEvaluateAndImportTasksRequest,
    ) -> polardbx_20200202_models.DescribeEvaluateAndImportTasksResponse:
        """
        @summary 请求评估导入任务列表
        
        @param request: DescribeEvaluateAndImportTasksRequest
        @return: DescribeEvaluateAndImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_and_import_tasks_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        """
        @summary 历史事件
        
        @param request: DescribeEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        """
        @summary 历史事件
        
        @param request: DescribeEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        """
        @summary 历史事件
        
        @param request: DescribeEventsRequest
        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        """
        @summary 历史事件
        
        @param request: DescribeEventsRequest
        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_gdn_instances_with_options(
        self,
        request: polardbx_20200202_models.DescribeGdnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeGdnInstancesResponse:
        """
        @summary 获取GDN实例列表
        
        @param request: DescribeGdnInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGdnInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_type):
            query['FilterType'] = request.filter_type
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGdnInstances',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeGdnInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gdn_instances_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeGdnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeGdnInstancesResponse:
        """
        @summary 获取GDN实例列表
        
        @param request: DescribeGdnInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGdnInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_type):
            query['FilterType'] = request.filter_type
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGdnInstances',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeGdnInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gdn_instances(
        self,
        request: polardbx_20200202_models.DescribeGdnInstancesRequest,
    ) -> polardbx_20200202_models.DescribeGdnInstancesResponse:
        """
        @summary 获取GDN实例列表
        
        @param request: DescribeGdnInstancesRequest
        @return: DescribeGdnInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gdn_instances_with_options(request, runtime)

    async def describe_gdn_instances_async(
        self,
        request: polardbx_20200202_models.DescribeGdnInstancesRequest,
    ) -> polardbx_20200202_models.DescribeGdnInstancesResponse:
        """
        @summary 获取GDN实例列表
        
        @param request: DescribeGdnInstancesRequest
        @return: DescribeGdnInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gdn_instances_with_options_async(request, runtime)

    def describe_open_backup_set_with_options(
        self,
        request: polardbx_20200202_models.DescribeOpenBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeOpenBackupSetResponse:
        """
        @summary 开放商业备份集
        
        @param request: DescribeOpenBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenBackupSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenBackupSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeOpenBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_backup_set_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeOpenBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeOpenBackupSetResponse:
        """
        @summary 开放商业备份集
        
        @param request: DescribeOpenBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenBackupSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenBackupSet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeOpenBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_backup_set(
        self,
        request: polardbx_20200202_models.DescribeOpenBackupSetRequest,
    ) -> polardbx_20200202_models.DescribeOpenBackupSetResponse:
        """
        @summary 开放商业备份集
        
        @param request: DescribeOpenBackupSetRequest
        @return: DescribeOpenBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_open_backup_set_with_options(request, runtime)

    async def describe_open_backup_set_async(
        self,
        request: polardbx_20200202_models.DescribeOpenBackupSetRequest,
    ) -> polardbx_20200202_models.DescribeOpenBackupSetResponse:
        """
        @summary 开放商业备份集
        
        @param request: DescribeOpenBackupSetRequest
        @return: DescribeOpenBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_backup_set_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: polardbx_20200202_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterGroupsResponse:
        """
        @summary 查询参数模版列表
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterGroupsResponse:
        """
        @summary 查询参数模版列表
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: polardbx_20200202_models.DescribeParameterGroupsRequest,
    ) -> polardbx_20200202_models.DescribeParameterGroupsResponse:
        """
        @summary 查询参数模版列表
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: polardbx_20200202_models.DescribeParameterGroupsRequest,
    ) -> polardbx_20200202_models.DescribeParameterGroupsResponse:
        """
        @summary 查询参数模版列表
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        """
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        """
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        """
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        """
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        """
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        """
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        """
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        """
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_polarx_data_nodes_with_options(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        """
        @summary 查询数据节点列表
        
        @param request: DescribePolarxDataNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolarxDataNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolarxDataNodes',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDataNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_polarx_data_nodes_with_options_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        """
        @summary 查询数据节点列表
        
        @param request: DescribePolarxDataNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolarxDataNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolarxDataNodes',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDataNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_polarx_data_nodes(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        """
        @summary 查询数据节点列表
        
        @param request: DescribePolarxDataNodesRequest
        @return: DescribePolarxDataNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_polarx_data_nodes_with_options(request, runtime)

    async def describe_polarx_data_nodes_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        """
        @summary 查询数据节点列表
        
        @param request: DescribePolarxDataNodesRequest
        @return: DescribePolarxDataNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_polarx_data_nodes_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: polardbx_20200202_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRdsVpcsResponse:
        """
        @param request: DescribeRdsVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcs',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRdsVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vpcs_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRdsVpcsResponse:
        """
        @param request: DescribeRdsVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcs',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRdsVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vpcs(
        self,
        request: polardbx_20200202_models.DescribeRdsVpcsRequest,
    ) -> polardbx_20200202_models.DescribeRdsVpcsResponse:
        """
        @param request: DescribeRdsVpcsRequest
        @return: DescribeRdsVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: polardbx_20200202_models.DescribeRdsVpcsRequest,
    ) -> polardbx_20200202_models.DescribeRdsVpcsResponse:
        """
        @param request: DescribeRdsVpcsRequest
        @return: DescribeRdsVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_rds_vswitches_with_options(
        self,
        request: polardbx_20200202_models.DescribeRdsVswitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRdsVswitchesResponse:
        """
        @summary 查询Vswitch信息
        
        @param request: DescribeRdsVswitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVswitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVswitches',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRdsVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitches_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeRdsVswitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRdsVswitchesResponse:
        """
        @summary 查询Vswitch信息
        
        @param request: DescribeRdsVswitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVswitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVswitches',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRdsVswitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitches(
        self,
        request: polardbx_20200202_models.DescribeRdsVswitchesRequest,
    ) -> polardbx_20200202_models.DescribeRdsVswitchesResponse:
        """
        @summary 查询Vswitch信息
        
        @param request: DescribeRdsVswitchesRequest
        @return: DescribeRdsVswitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitches_with_options(request, runtime)

    async def describe_rds_vswitches_async(
        self,
        request: polardbx_20200202_models.DescribeRdsVswitchesRequest,
    ) -> polardbx_20200202_models.DescribeRdsVswitchesResponse:
        """
        @summary 查询Vswitch信息
        
        @param request: DescribeRdsVswitchesRequest
        @return: DescribeRdsVswitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vswitches_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> polardbx_20200202_models.DescribeRegionsResponse:
        """
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> polardbx_20200202_models.DescribeRegionsResponse:
        """
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_rpl_inspection_task_with_options(
        self,
        request: polardbx_20200202_models.DescribeRplInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRplInspectionTaskResponse:
        """
        @summary 查询预检任务结果
        
        @param request: DescribeRplInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRplInspectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not UtilClient.is_unset(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not UtilClient.is_unset(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRplInspectionTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRplInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rpl_inspection_task_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeRplInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRplInspectionTaskResponse:
        """
        @summary 查询预检任务结果
        
        @param request: DescribeRplInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRplInspectionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not UtilClient.is_unset(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not UtilClient.is_unset(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRplInspectionTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRplInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rpl_inspection_task(
        self,
        request: polardbx_20200202_models.DescribeRplInspectionTaskRequest,
    ) -> polardbx_20200202_models.DescribeRplInspectionTaskResponse:
        """
        @summary 查询预检任务结果
        
        @param request: DescribeRplInspectionTaskRequest
        @return: DescribeRplInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rpl_inspection_task_with_options(request, runtime)

    async def describe_rpl_inspection_task_async(
        self,
        request: polardbx_20200202_models.DescribeRplInspectionTaskRequest,
    ) -> polardbx_20200202_models.DescribeRplInspectionTaskResponse:
        """
        @summary 查询预检任务结果
        
        @param request: DescribeRplInspectionTaskRequest
        @return: DescribeRplInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rpl_inspection_task_with_options_async(request, runtime)

    def describe_scale_out_migrate_task_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        """
        @param request: DescribeScaleOutMigrateTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScaleOutMigrateTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScaleOutMigrateTaskList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scale_out_migrate_task_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        """
        @param request: DescribeScaleOutMigrateTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScaleOutMigrateTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScaleOutMigrateTaskList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scale_out_migrate_task_list(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        """
        @param request: DescribeScaleOutMigrateTaskListRequest
        @return: DescribeScaleOutMigrateTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scale_out_migrate_task_list_with_options(request, runtime)

    async def describe_scale_out_migrate_task_list_async(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        """
        @param request: DescribeScaleOutMigrateTaskListRequest
        @return: DescribeScaleOutMigrateTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scale_out_migrate_task_list_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        """
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        """
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ips(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        """
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        """
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_show_storage_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeShowStorageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeShowStorageInfoResponse:
        """
        @summary 查询 PolarDB-X 存储节点信息
        
        @param request: DescribeShowStorageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeShowStorageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShowStorageInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeShowStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_show_storage_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeShowStorageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeShowStorageInfoResponse:
        """
        @summary 查询 PolarDB-X 存储节点信息
        
        @param request: DescribeShowStorageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeShowStorageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShowStorageInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeShowStorageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_show_storage_info(
        self,
        request: polardbx_20200202_models.DescribeShowStorageInfoRequest,
    ) -> polardbx_20200202_models.DescribeShowStorageInfoResponse:
        """
        @summary 查询 PolarDB-X 存储节点信息
        
        @param request: DescribeShowStorageInfoRequest
        @return: DescribeShowStorageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_show_storage_info_with_options(request, runtime)

    async def describe_show_storage_info_async(
        self,
        request: polardbx_20200202_models.DescribeShowStorageInfoRequest,
    ) -> polardbx_20200202_models.DescribeShowStorageInfoResponse:
        """
        @summary 查询 PolarDB-X 存储节点信息
        
        @param request: DescribeShowStorageInfoRequest
        @return: DescribeShowStorageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_show_storage_info_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: polardbx_20200202_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSlowLogRecordsResponse:
        """
        @summary 慢SQL明细
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSlowLogRecordsResponse:
        """
        @summary 慢SQL明细
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: polardbx_20200202_models.DescribeSlowLogRecordsRequest,
    ) -> polardbx_20200202_models.DescribeSlowLogRecordsResponse:
        """
        @summary 慢SQL明细
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: polardbx_20200202_models.DescribeSlowLogRecordsRequest,
    ) -> polardbx_20200202_models.DescribeSlowLogRecordsResponse:
        """
        @summary 慢SQL明细
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_sql_audit_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeSqlAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSqlAuditInfoResponse:
        """
        @param request: DescribeSqlAuditInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlAuditInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlAuditInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSqlAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_audit_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeSqlAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSqlAuditInfoResponse:
        """
        @param request: DescribeSqlAuditInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlAuditInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlAuditInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSqlAuditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_audit_info(
        self,
        request: polardbx_20200202_models.DescribeSqlAuditInfoRequest,
    ) -> polardbx_20200202_models.DescribeSqlAuditInfoResponse:
        """
        @param request: DescribeSqlAuditInfoRequest
        @return: DescribeSqlAuditInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_audit_info_with_options(request, runtime)

    async def describe_sql_audit_info_async(
        self,
        request: polardbx_20200202_models.DescribeSqlAuditInfoRequest,
    ) -> polardbx_20200202_models.DescribeSqlAuditInfoResponse:
        """
        @param request: DescribeSqlAuditInfoRequest
        @return: DescribeSqlAuditInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_audit_info_with_options_async(request, runtime)

    def describe_sql_flashback_task_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeSqlFlashbackTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse:
        """
        @summary SQL闪回任务列表查询
        
        @param request: DescribeSqlFlashbackTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlFlashbackTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlFlashbackTaskList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_flashback_task_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeSqlFlashbackTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse:
        """
        @summary SQL闪回任务列表查询
        
        @param request: DescribeSqlFlashbackTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlFlashbackTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlFlashbackTaskList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_flashback_task_list(
        self,
        request: polardbx_20200202_models.DescribeSqlFlashbackTaskListRequest,
    ) -> polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse:
        """
        @summary SQL闪回任务列表查询
        
        @param request: DescribeSqlFlashbackTaskListRequest
        @return: DescribeSqlFlashbackTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_flashback_task_list_with_options(request, runtime)

    async def describe_sql_flashback_task_list_async(
        self,
        request: polardbx_20200202_models.DescribeSqlFlashbackTaskListRequest,
    ) -> polardbx_20200202_models.DescribeSqlFlashbackTaskListResponse:
        """
        @summary SQL闪回任务列表查询
        
        @param request: DescribeSqlFlashbackTaskListRequest
        @return: DescribeSqlFlashbackTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_flashback_task_list_with_options_async(request, runtime)

    def describe_storage_pool_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeStoragePoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeStoragePoolInfoResponse:
        """
        @summary 查询 PolarDB-X 存储资源池信息
        
        @param request: DescribeStoragePoolInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoragePoolInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStoragePoolInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeStoragePoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_pool_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeStoragePoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeStoragePoolInfoResponse:
        """
        @summary 查询 PolarDB-X 存储资源池信息
        
        @param request: DescribeStoragePoolInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoragePoolInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStoragePoolInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeStoragePoolInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_pool_info(
        self,
        request: polardbx_20200202_models.DescribeStoragePoolInfoRequest,
    ) -> polardbx_20200202_models.DescribeStoragePoolInfoResponse:
        """
        @summary 查询 PolarDB-X 存储资源池信息
        
        @param request: DescribeStoragePoolInfoRequest
        @return: DescribeStoragePoolInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_pool_info_with_options(request, runtime)

    async def describe_storage_pool_info_async(
        self,
        request: polardbx_20200202_models.DescribeStoragePoolInfoRequest,
    ) -> polardbx_20200202_models.DescribeStoragePoolInfoResponse:
        """
        @summary 查询 PolarDB-X 存储资源池信息
        
        @param request: DescribeStoragePoolInfoRequest
        @return: DescribeStoragePoolInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_pool_info_with_options_async(request, runtime)

    def describe_structure_import_task_info_with_options(
        self,
        request: polardbx_20200202_models.DescribeStructureImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeStructureImportTaskInfoResponse:
        """
        @summary 查询结构迁移任务结果
        
        @param request: DescribeStructureImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStructureImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStructureImportTaskInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeStructureImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_structure_import_task_info_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeStructureImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeStructureImportTaskInfoResponse:
        """
        @summary 查询结构迁移任务结果
        
        @param request: DescribeStructureImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStructureImportTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStructureImportTaskInfo',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeStructureImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_structure_import_task_info(
        self,
        request: polardbx_20200202_models.DescribeStructureImportTaskInfoRequest,
    ) -> polardbx_20200202_models.DescribeStructureImportTaskInfoResponse:
        """
        @summary 查询结构迁移任务结果
        
        @param request: DescribeStructureImportTaskInfoRequest
        @return: DescribeStructureImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_structure_import_task_info_with_options(request, runtime)

    async def describe_structure_import_task_info_async(
        self,
        request: polardbx_20200202_models.DescribeStructureImportTaskInfoRequest,
    ) -> polardbx_20200202_models.DescribeStructureImportTaskInfoResponse:
        """
        @summary 查询结构迁移任务结果
        
        @param request: DescribeStructureImportTaskInfoRequest
        @return: DescribeStructureImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_structure_import_task_info_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: polardbx_20200202_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTagsResponse:
        """
        @summary 标签列表查询
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTagsResponse:
        """
        @summary 标签列表查询
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: polardbx_20200202_models.DescribeTagsRequest,
    ) -> polardbx_20200202_models.DescribeTagsResponse:
        """
        @summary 标签列表查询
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: polardbx_20200202_models.DescribeTagsRequest,
    ) -> polardbx_20200202_models.DescribeTagsResponse:
        """
        @summary 标签列表查询
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_transform_status_with_options(
        self,
        request: polardbx_20200202_models.DescribeTransformStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTransformStatusResponse:
        """
        @summary 查询标准版迁移到企业版的任务状态
        
        @param request: DescribeTransformStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransformStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.query_report):
            query['QueryReport'] = request.query_report
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransformStatus',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTransformStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transform_status_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeTransformStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTransformStatusResponse:
        """
        @summary 查询标准版迁移到企业版的任务状态
        
        @param request: DescribeTransformStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransformStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.query_report):
            query['QueryReport'] = request.query_report
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransformStatus',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTransformStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transform_status(
        self,
        request: polardbx_20200202_models.DescribeTransformStatusRequest,
    ) -> polardbx_20200202_models.DescribeTransformStatusResponse:
        """
        @summary 查询标准版迁移到企业版的任务状态
        
        @param request: DescribeTransformStatusRequest
        @return: DescribeTransformStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_transform_status_with_options(request, runtime)

    async def describe_transform_status_async(
        self,
        request: polardbx_20200202_models.DescribeTransformStatusRequest,
    ) -> polardbx_20200202_models.DescribeTransformStatusResponse:
        """
        @summary 查询标准版迁移到企业版的任务状态
        
        @param request: DescribeTransformStatusRequest
        @return: DescribeTransformStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_transform_status_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        """
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        """
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        """
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        """
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def disable_rights_separation_with_options(
        self,
        request: polardbx_20200202_models.DisableRightsSeparationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DisableRightsSeparationResponse:
        """
        @param request: DisableRightsSeparationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRightsSeparationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dba_account_name):
            query['DbaAccountName'] = request.dba_account_name
        if not UtilClient.is_unset(request.dba_account_password):
            query['DbaAccountPassword'] = request.dba_account_password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRightsSeparation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DisableRightsSeparationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rights_separation_with_options_async(
        self,
        request: polardbx_20200202_models.DisableRightsSeparationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DisableRightsSeparationResponse:
        """
        @param request: DisableRightsSeparationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRightsSeparationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dba_account_name):
            query['DbaAccountName'] = request.dba_account_name
        if not UtilClient.is_unset(request.dba_account_password):
            query['DbaAccountPassword'] = request.dba_account_password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRightsSeparation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DisableRightsSeparationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rights_separation(
        self,
        request: polardbx_20200202_models.DisableRightsSeparationRequest,
    ) -> polardbx_20200202_models.DisableRightsSeparationResponse:
        """
        @param request: DisableRightsSeparationRequest
        @return: DisableRightsSeparationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_rights_separation_with_options(request, runtime)

    async def disable_rights_separation_async(
        self,
        request: polardbx_20200202_models.DisableRightsSeparationRequest,
    ) -> polardbx_20200202_models.DisableRightsSeparationResponse:
        """
        @param request: DisableRightsSeparationRequest
        @return: DisableRightsSeparationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_rights_separation_with_options_async(request, runtime)

    def disable_sql_audit_with_options(
        self,
        request: polardbx_20200202_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DisableSqlAuditResponse:
        """
        @param request: DisableSqlAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSqlAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlAudit',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DisableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sql_audit_with_options_async(
        self,
        request: polardbx_20200202_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DisableSqlAuditResponse:
        """
        @param request: DisableSqlAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSqlAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlAudit',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DisableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sql_audit(
        self,
        request: polardbx_20200202_models.DisableSqlAuditRequest,
    ) -> polardbx_20200202_models.DisableSqlAuditResponse:
        """
        @param request: DisableSqlAuditRequest
        @return: DisableSqlAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    async def disable_sql_audit_async(
        self,
        request: polardbx_20200202_models.DisableSqlAuditRequest,
    ) -> polardbx_20200202_models.DisableSqlAuditResponse:
        """
        @param request: DisableSqlAuditRequest
        @return: DisableSqlAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_sql_audit_with_options_async(request, runtime)

    def enable_rights_separation_with_options(
        self,
        request: polardbx_20200202_models.EnableRightsSeparationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.EnableRightsSeparationResponse:
        """
        @summary 开启三权分立
        
        @param request: EnableRightsSeparationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRightsSeparationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_description):
            query['AuditAccountDescription'] = request.audit_account_description
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_description):
            query['SecurityAccountDescription'] = request.security_account_description
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRightsSeparation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.EnableRightsSeparationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rights_separation_with_options_async(
        self,
        request: polardbx_20200202_models.EnableRightsSeparationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.EnableRightsSeparationResponse:
        """
        @summary 开启三权分立
        
        @param request: EnableRightsSeparationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRightsSeparationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_description):
            query['AuditAccountDescription'] = request.audit_account_description
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_description):
            query['SecurityAccountDescription'] = request.security_account_description
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRightsSeparation',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.EnableRightsSeparationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rights_separation(
        self,
        request: polardbx_20200202_models.EnableRightsSeparationRequest,
    ) -> polardbx_20200202_models.EnableRightsSeparationResponse:
        """
        @summary 开启三权分立
        
        @param request: EnableRightsSeparationRequest
        @return: EnableRightsSeparationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_rights_separation_with_options(request, runtime)

    async def enable_rights_separation_async(
        self,
        request: polardbx_20200202_models.EnableRightsSeparationRequest,
    ) -> polardbx_20200202_models.EnableRightsSeparationResponse:
        """
        @summary 开启三权分立
        
        @param request: EnableRightsSeparationRequest
        @return: EnableRightsSeparationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_rights_separation_with_options_async(request, runtime)

    def enable_sql_audit_with_options(
        self,
        request: polardbx_20200202_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.EnableSqlAuditResponse:
        """
        @param request: EnableSqlAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSqlAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.expire_after_days):
            query['ExpireAfterDays'] = request.expire_after_days
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlAudit',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.EnableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_audit_with_options_async(
        self,
        request: polardbx_20200202_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.EnableSqlAuditResponse:
        """
        @param request: EnableSqlAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSqlAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not UtilClient.is_unset(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.expire_after_days):
            query['ExpireAfterDays'] = request.expire_after_days
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlAudit',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.EnableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sql_audit(
        self,
        request: polardbx_20200202_models.EnableSqlAuditRequest,
    ) -> polardbx_20200202_models.EnableSqlAuditResponse:
        """
        @param request: EnableSqlAuditRequest
        @return: EnableSqlAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    async def enable_sql_audit_async(
        self,
        request: polardbx_20200202_models.EnableSqlAuditRequest,
    ) -> polardbx_20200202_models.EnableSqlAuditResponse:
        """
        @param request: EnableSqlAuditRequest
        @return: EnableSqlAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_audit_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: polardbx_20200202_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: polardbx_20200202_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: polardbx_20200202_models.ListTagResourcesRequest,
    ) -> polardbx_20200202_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: polardbx_20200202_models.ListTagResourcesRequest,
    ) -> polardbx_20200202_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.MigrateDBInstanceResponse:
        """
        @param request: MigrateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.tertiary_zone_id):
            query['TertiaryZoneId'] = request.tertiary_zone_id
        if not UtilClient.is_unset(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.MigrateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.MigrateDBInstanceResponse:
        """
        @param request: MigrateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.tertiary_zone_id):
            query['TertiaryZoneId'] = request.tertiary_zone_id
        if not UtilClient.is_unset(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.MigrateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_dbinstance(
        self,
        request: polardbx_20200202_models.MigrateDBInstanceRequest,
    ) -> polardbx_20200202_models.MigrateDBInstanceResponse:
        """
        @param request: MigrateDBInstanceRequest
        @return: MigrateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    async def migrate_dbinstance_async(
        self,
        request: polardbx_20200202_models.MigrateDBInstanceRequest,
    ) -> polardbx_20200202_models.MigrateDBInstanceResponse:
        """
        @param request: MigrateDBInstanceRequest
        @return: MigrateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_dbinstance_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        """
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        """
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        """
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        """
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_privilege_with_options(
        self,
        request: polardbx_20200202_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountPrivilegeResponse:
        """
        @param request: ModifyAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privilege_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountPrivilegeResponse:
        """
        @param request: ModifyAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privilege(
        self,
        request: polardbx_20200202_models.ModifyAccountPrivilegeRequest,
    ) -> polardbx_20200202_models.ModifyAccountPrivilegeResponse:
        """
        @param request: ModifyAccountPrivilegeRequest
        @return: ModifyAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    async def modify_account_privilege_async(
        self,
        request: polardbx_20200202_models.ModifyAccountPrivilegeRequest,
    ) -> polardbx_20200202_models.ModifyAccountPrivilegeResponse:
        """
        @param request: ModifyAccountPrivilegeRequest
        @return: ModifyAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_privilege_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary 修改全局运维窗口信息
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationMaintainConf',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_maintain_conf_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary 修改全局运维窗口信息
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationMaintainConf',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_maintain_conf(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary 修改全局运维窗口信息
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @return: ModifyActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    async def modify_active_operation_maintain_conf_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary 修改全局运维窗口信息
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @return: ModifyActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_maintain_conf_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        """
        @summary 修改主动运维任务
        
        @param request: ModifyActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        """
        @summary 修改主动运维任务
        
        @param request: ModifyActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        """
        @summary 修改主动运维任务
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        """
        @summary 修改主动运维任务
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_cdc_class_with_options(
        self,
        request: polardbx_20200202_models.ModifyCdcClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCdcClassResponse:
        """
        @summary CDC变配
        
        @description ***\
        
        @param request: ModifyCdcClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdcClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdcnode_count):
            query['CDCNodeCount'] = request.cdcnode_count
        if not UtilClient.is_unset(request.cdc_class):
            query['CdcClass'] = request.cdc_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCdcClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCdcClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdc_class_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyCdcClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCdcClassResponse:
        """
        @summary CDC变配
        
        @description ***\
        
        @param request: ModifyCdcClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdcClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdcnode_count):
            query['CDCNodeCount'] = request.cdcnode_count
        if not UtilClient.is_unset(request.cdc_class):
            query['CdcClass'] = request.cdc_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCdcClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCdcClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdc_class(
        self,
        request: polardbx_20200202_models.ModifyCdcClassRequest,
    ) -> polardbx_20200202_models.ModifyCdcClassResponse:
        """
        @summary CDC变配
        
        @description ***\
        
        @param request: ModifyCdcClassRequest
        @return: ModifyCdcClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cdc_class_with_options(request, runtime)

    async def modify_cdc_class_async(
        self,
        request: polardbx_20200202_models.ModifyCdcClassRequest,
    ) -> polardbx_20200202_models.ModifyCdcClassResponse:
        """
        @summary CDC变配
        
        @description ***\
        
        @param request: ModifyCdcClassRequest
        @return: ModifyCdcClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdc_class_with_options_async(request, runtime)

    def modify_columnar_class_with_options(
        self,
        request: polardbx_20200202_models.ModifyColumnarClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyColumnarClassResponse:
        """
        @summary Columnar变配
        
        @description ***\
        
        @param request: ModifyColumnarClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyColumnarClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columnar_class):
            query['ColumnarClass'] = request.columnar_class
        if not UtilClient.is_unset(request.columnar_node_count):
            query['ColumnarNodeCount'] = request.columnar_node_count
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyColumnarClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyColumnarClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_columnar_class_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyColumnarClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyColumnarClassResponse:
        """
        @summary Columnar变配
        
        @description ***\
        
        @param request: ModifyColumnarClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyColumnarClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columnar_class):
            query['ColumnarClass'] = request.columnar_class
        if not UtilClient.is_unset(request.columnar_node_count):
            query['ColumnarNodeCount'] = request.columnar_node_count
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyColumnarClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyColumnarClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_columnar_class(
        self,
        request: polardbx_20200202_models.ModifyColumnarClassRequest,
    ) -> polardbx_20200202_models.ModifyColumnarClassResponse:
        """
        @summary Columnar变配
        
        @description ***\
        
        @param request: ModifyColumnarClassRequest
        @return: ModifyColumnarClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_columnar_class_with_options(request, runtime)

    async def modify_columnar_class_async(
        self,
        request: polardbx_20200202_models.ModifyColumnarClassRequest,
    ) -> polardbx_20200202_models.ModifyColumnarClassResponse:
        """
        @summary Columnar变配
        
        @description ***\
        
        @param request: ModifyColumnarClassRequest
        @return: ModifyColumnarClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_columnar_class_with_options_async(request, runtime)

    def modify_custom_endpoint_with_options(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCustomEndpointResponse:
        """
        @summary 修复自定连接基本信息
        
        @param request: ModifyCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_endpoint_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCustomEndpointResponse:
        """
        @summary 修复自定连接基本信息
        
        @param request: ModifyCustomEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomEndpoint',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_endpoint(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointRequest,
    ) -> polardbx_20200202_models.ModifyCustomEndpointResponse:
        """
        @summary 修复自定连接基本信息
        
        @param request: ModifyCustomEndpointRequest
        @return: ModifyCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_endpoint_with_options(request, runtime)

    async def modify_custom_endpoint_async(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointRequest,
    ) -> polardbx_20200202_models.ModifyCustomEndpointResponse:
        """
        @summary 修复自定连接基本信息
        
        @param request: ModifyCustomEndpointRequest
        @return: ModifyCustomEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_custom_endpoint_with_options_async(request, runtime)

    def modify_custom_endpoint_net_with_options(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointNetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCustomEndpointNetResponse:
        """
        @summary 修复自定连接的网络信息
        
        @param request: ModifyCustomEndpointNetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomEndpointNetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conn_prefix):
            query['ConnPrefix'] = request.conn_prefix
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomEndpointNet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCustomEndpointNetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_endpoint_net_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointNetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyCustomEndpointNetResponse:
        """
        @summary 修复自定连接的网络信息
        
        @param request: ModifyCustomEndpointNetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCustomEndpointNetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conn_prefix):
            query['ConnPrefix'] = request.conn_prefix
        if not UtilClient.is_unset(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomEndpointNet',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyCustomEndpointNetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_endpoint_net(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointNetRequest,
    ) -> polardbx_20200202_models.ModifyCustomEndpointNetResponse:
        """
        @summary 修复自定连接的网络信息
        
        @param request: ModifyCustomEndpointNetRequest
        @return: ModifyCustomEndpointNetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_endpoint_net_with_options(request, runtime)

    async def modify_custom_endpoint_net_async(
        self,
        request: polardbx_20200202_models.ModifyCustomEndpointNetRequest,
    ) -> polardbx_20200202_models.ModifyCustomEndpointNetResponse:
        """
        @summary 修复自定连接的网络信息
        
        @param request: ModifyCustomEndpointNetRequest
        @return: ModifyCustomEndpointNetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_custom_endpoint_net_with_options_async(request, runtime)

    def modify_dbinstance_class_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        """
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cn_class):
            query['CnClass'] = request.cn_class
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dn_class):
            query['DnClass'] = request.dn_class
        if not UtilClient.is_unset(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specified_dnscale):
            query['SpecifiedDNScale'] = request.specified_dnscale
        if not UtilClient.is_unset(request.specified_dnspec_map_json):
            query['SpecifiedDNSpecMapJson'] = request.specified_dnspec_map_json
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_dbinstance_class):
            query['TargetDBInstanceClass'] = request.target_dbinstance_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_class_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        """
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cn_class):
            query['CnClass'] = request.cn_class
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dn_class):
            query['DnClass'] = request.dn_class
        if not UtilClient.is_unset(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specified_dnscale):
            query['SpecifiedDNScale'] = request.specified_dnscale
        if not UtilClient.is_unset(request.specified_dnspec_map_json):
            query['SpecifiedDNSpecMapJson'] = request.specified_dnspec_map_json
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_dbinstance_class):
            query['TargetDBInstanceClass'] = request.target_dbinstance_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_class(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        """
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    async def modify_dbinstance_class_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        """
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_class_with_options_async(request, runtime)

    def modify_dbinstance_config_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBInstanceConfigRequest
        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBInstanceConfigRequest
        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary 修改实例链接串
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.new_port):
            query['NewPort'] = request.new_port
        if not UtilClient.is_unset(request.new_prefix):
            query['NewPrefix'] = request.new_prefix
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary 修改实例链接串
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.new_port):
            query['NewPort'] = request.new_port
        if not UtilClient.is_unset(request.new_prefix):
            query['NewPrefix'] = request.new_prefix
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConnectionStringRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary 修改实例链接串
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConnectionStringRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary 修改实例链接串
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        """
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        """
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        """
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        """
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_vip_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceVipResponse:
        """
        @description ***\
        
        @param request: ModifyDBInstanceVipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceVipResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceVip',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceVipResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_vip_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceVipResponse:
        """
        @description ***\
        
        @param request: ModifyDBInstanceVipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceVipResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceVip',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceVipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_vip(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceVipRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceVipResponse:
        """
        @description ***\
        
        @param request: ModifyDBInstanceVipRequest
        @return: ModifyDBInstanceVipResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_vip_with_options(request, runtime)

    async def modify_dbinstance_vip_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceVipRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceVipResponse:
        """
        @description ***\
        
        @param request: ModifyDBInstanceVipRequest
        @return: ModifyDBInstanceVipResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_vip_with_options_async(request, runtime)

    def modify_database_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        """
        @param request: ModifyDatabaseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_description):
            query['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDatabaseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        """
        @param request: ModifyDatabaseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.db_description):
            query['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseDescription',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDatabaseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_description(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        """
        @param request: ModifyDatabaseDescriptionRequest
        @return: ModifyDatabaseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    async def modify_database_description_async(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        """
        @param request: ModifyDatabaseDescriptionRequest
        @return: ModifyDatabaseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_description_with_options_async(request, runtime)

    def modify_engine_migration_with_options(
        self,
        request: polardbx_20200202_models.ModifyEngineMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyEngineMigrationResponse:
        """
        @summary ModifyEngineMigration
        
        @description ***\
        
        @param request: ModifyEngineMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEngineMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.new_master_dbinstance_name):
            query['NewMasterDBInstanceName'] = request.new_master_dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEngineMigration',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyEngineMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_engine_migration_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyEngineMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyEngineMigrationResponse:
        """
        @summary ModifyEngineMigration
        
        @description ***\
        
        @param request: ModifyEngineMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEngineMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.new_master_dbinstance_name):
            query['NewMasterDBInstanceName'] = request.new_master_dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEngineMigration',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyEngineMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_engine_migration(
        self,
        request: polardbx_20200202_models.ModifyEngineMigrationRequest,
    ) -> polardbx_20200202_models.ModifyEngineMigrationResponse:
        """
        @summary ModifyEngineMigration
        
        @description ***\
        
        @param request: ModifyEngineMigrationRequest
        @return: ModifyEngineMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_engine_migration_with_options(request, runtime)

    async def modify_engine_migration_async(
        self,
        request: polardbx_20200202_models.ModifyEngineMigrationRequest,
    ) -> polardbx_20200202_models.ModifyEngineMigrationResponse:
        """
        @summary ModifyEngineMigration
        
        @description ***\
        
        @param request: ModifyEngineMigrationRequest
        @return: ModifyEngineMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_engine_migration_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        """
        @param request: ModifyParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        """
        @param request: ModifyParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameter(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        """
        @param request: ModifyParameterRequest
        @return: ModifyParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        """
        @param request: ModifyParameterRequest
        @return: ModifyParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        """
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        """
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        """
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        """
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def pre_check_sql_flashback_task_with_options(
        self,
        request: polardbx_20200202_models.PreCheckSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse:
        """
        @summary SQL闪回任务预检
        
        @param request: PreCheckSqlFlashbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreCheckSqlFlashbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreCheckSqlFlashbackTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pre_check_sql_flashback_task_with_options_async(
        self,
        request: polardbx_20200202_models.PreCheckSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse:
        """
        @summary SQL闪回任务预检
        
        @param request: PreCheckSqlFlashbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreCheckSqlFlashbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreCheckSqlFlashbackTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pre_check_sql_flashback_task(
        self,
        request: polardbx_20200202_models.PreCheckSqlFlashbackTaskRequest,
    ) -> polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse:
        """
        @summary SQL闪回任务预检
        
        @param request: PreCheckSqlFlashbackTaskRequest
        @return: PreCheckSqlFlashbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pre_check_sql_flashback_task_with_options(request, runtime)

    async def pre_check_sql_flashback_task_async(
        self,
        request: polardbx_20200202_models.PreCheckSqlFlashbackTaskRequest,
    ) -> polardbx_20200202_models.PreCheckSqlFlashbackTaskResponse:
        """
        @summary SQL闪回任务预检
        
        @param request: PreCheckSqlFlashbackTaskRequest
        @return: PreCheckSqlFlashbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pre_check_sql_flashback_task_with_options_async(request, runtime)

    def refresh_import_meta_with_options(
        self,
        request: polardbx_20200202_models.RefreshImportMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RefreshImportMetaResponse:
        """
        @summary 刷新评估升级任务的导入元数据
        
        @param request: RefreshImportMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshImportMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshImportMeta',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RefreshImportMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_import_meta_with_options_async(
        self,
        request: polardbx_20200202_models.RefreshImportMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RefreshImportMetaResponse:
        """
        @summary 刷新评估升级任务的导入元数据
        
        @param request: RefreshImportMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshImportMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshImportMeta',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RefreshImportMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_import_meta(
        self,
        request: polardbx_20200202_models.RefreshImportMetaRequest,
    ) -> polardbx_20200202_models.RefreshImportMetaResponse:
        """
        @summary 刷新评估升级任务的导入元数据
        
        @param request: RefreshImportMetaRequest
        @return: RefreshImportMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_import_meta_with_options(request, runtime)

    async def refresh_import_meta_async(
        self,
        request: polardbx_20200202_models.RefreshImportMetaRequest,
    ) -> polardbx_20200202_models.RefreshImportMetaResponse:
        """
        @summary 刷新评估升级任务的导入元数据
        
        @param request: RefreshImportMetaRequest
        @return: RefreshImportMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_import_meta_with_options_async(request, runtime)

    def release_cold_data_volume_with_options(
        self,
        request: polardbx_20200202_models.ReleaseColdDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseColdDataVolumeResponse:
        """
        @summary 关闭冷存储
        
        @param request: ReleaseColdDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseColdDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseColdDataVolume',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseColdDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cold_data_volume_with_options_async(
        self,
        request: polardbx_20200202_models.ReleaseColdDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseColdDataVolumeResponse:
        """
        @summary 关闭冷存储
        
        @param request: ReleaseColdDataVolumeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseColdDataVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseColdDataVolume',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseColdDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cold_data_volume(
        self,
        request: polardbx_20200202_models.ReleaseColdDataVolumeRequest,
    ) -> polardbx_20200202_models.ReleaseColdDataVolumeResponse:
        """
        @summary 关闭冷存储
        
        @param request: ReleaseColdDataVolumeRequest
        @return: ReleaseColdDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_cold_data_volume_with_options(request, runtime)

    async def release_cold_data_volume_async(
        self,
        request: polardbx_20200202_models.ReleaseColdDataVolumeRequest,
    ) -> polardbx_20200202_models.ReleaseColdDataVolumeResponse:
        """
        @summary 关闭冷存储
        
        @param request: ReleaseColdDataVolumeRequest
        @return: ReleaseColdDataVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_cold_data_volume_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        """
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        """
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        """
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        """
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ResetAccountPasswordResponse:
        """
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ResetAccountPasswordResponse:
        """
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRequest,
    ) -> polardbx_20200202_models.ResetAccountPasswordResponse:
        """
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRequest,
    ) -> polardbx_20200202_models.ResetAccountPasswordResponse:
        """
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def reset_account_password_restrict_with_options(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRestrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ResetAccountPasswordRestrictResponse:
        """
        @description ***\
        
        @param request: ResetAccountPasswordRestrictRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordRestrictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPasswordRestrict',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ResetAccountPasswordRestrictResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_restrict_with_options_async(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRestrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ResetAccountPasswordRestrictResponse:
        """
        @description ***\
        
        @param request: ResetAccountPasswordRestrictRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordRestrictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not UtilClient.is_unset(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPasswordRestrict',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ResetAccountPasswordRestrictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password_restrict(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRestrictRequest,
    ) -> polardbx_20200202_models.ResetAccountPasswordRestrictResponse:
        """
        @description ***\
        
        @param request: ResetAccountPasswordRestrictRequest
        @return: ResetAccountPasswordRestrictResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_restrict_with_options(request, runtime)

    async def reset_account_password_restrict_async(
        self,
        request: polardbx_20200202_models.ResetAccountPasswordRestrictRequest,
    ) -> polardbx_20200202_models.ResetAccountPasswordRestrictResponse:
        """
        @description ***\
        
        @param request: ResetAccountPasswordRestrictRequest
        @return: ResetAccountPasswordRestrictResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_restrict_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        """
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        """
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        """
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        """
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restart_data_import_task_with_options(
        self,
        request: polardbx_20200202_models.RestartDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDataImportTaskResponse:
        """
        @summary 重启数据导入任务
        
        @param request: RestartDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_data_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.RestartDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDataImportTaskResponse:
        """
        @summary 重启数据导入任务
        
        @param request: RestartDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_data_import_task(
        self,
        request: polardbx_20200202_models.RestartDataImportTaskRequest,
    ) -> polardbx_20200202_models.RestartDataImportTaskResponse:
        """
        @summary 重启数据导入任务
        
        @param request: RestartDataImportTaskRequest
        @return: RestartDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_data_import_task_with_options(request, runtime)

    async def restart_data_import_task_async(
        self,
        request: polardbx_20200202_models.RestartDataImportTaskRequest,
    ) -> polardbx_20200202_models.RestartDataImportTaskResponse:
        """
        @summary 重启数据导入任务
        
        @param request: RestartDataImportTaskRequest
        @return: RestartDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_data_import_task_with_options_async(request, runtime)

    def skip_current_step_with_options(
        self,
        request: polardbx_20200202_models.SkipCurrentStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SkipCurrentStepResponse:
        """
        @summary 跳过评估迁移的当前步骤
        
        @param request: SkipCurrentStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipCurrentStepResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_step):
            query['CurrentStep'] = request.current_step
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipCurrentStep',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SkipCurrentStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_current_step_with_options_async(
        self,
        request: polardbx_20200202_models.SkipCurrentStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SkipCurrentStepResponse:
        """
        @summary 跳过评估迁移的当前步骤
        
        @param request: SkipCurrentStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SkipCurrentStepResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_step):
            query['CurrentStep'] = request.current_step
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipCurrentStep',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SkipCurrentStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_current_step(
        self,
        request: polardbx_20200202_models.SkipCurrentStepRequest,
    ) -> polardbx_20200202_models.SkipCurrentStepResponse:
        """
        @summary 跳过评估迁移的当前步骤
        
        @param request: SkipCurrentStepRequest
        @return: SkipCurrentStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.skip_current_step_with_options(request, runtime)

    async def skip_current_step_async(
        self,
        request: polardbx_20200202_models.SkipCurrentStepRequest,
    ) -> polardbx_20200202_models.SkipCurrentStepResponse:
        """
        @summary 跳过评估迁移的当前步骤
        
        @param request: SkipCurrentStepRequest
        @return: SkipCurrentStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.skip_current_step_with_options_async(request, runtime)

    def start_switch_database_with_options(
        self,
        request: polardbx_20200202_models.StartSwitchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.StartSwitchDatabaseResponse:
        """
        @summary 开始评估迁移切换
        
        @param request: StartSwitchDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSwitchDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_main_connect_string):
            query['DstMainConnectString'] = request.dst_main_connect_string
        if not UtilClient.is_unset(request.dst_main_port):
            query['DstMainPort'] = request.dst_main_port
        if not UtilClient.is_unset(request.is_modify_endpoint):
            query['IsModifyEndpoint'] = request.is_modify_endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_main_connect_string):
            query['SrcMainConnectString'] = request.src_main_connect_string
        if not UtilClient.is_unset(request.src_main_port):
            query['SrcMainPort'] = request.src_main_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSwitchDatabase',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.StartSwitchDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_switch_database_with_options_async(
        self,
        request: polardbx_20200202_models.StartSwitchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.StartSwitchDatabaseResponse:
        """
        @summary 开始评估迁移切换
        
        @param request: StartSwitchDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSwitchDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dst_main_connect_string):
            query['DstMainConnectString'] = request.dst_main_connect_string
        if not UtilClient.is_unset(request.dst_main_port):
            query['DstMainPort'] = request.dst_main_port
        if not UtilClient.is_unset(request.is_modify_endpoint):
            query['IsModifyEndpoint'] = request.is_modify_endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not UtilClient.is_unset(request.src_main_connect_string):
            query['SrcMainConnectString'] = request.src_main_connect_string
        if not UtilClient.is_unset(request.src_main_port):
            query['SrcMainPort'] = request.src_main_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSwitchDatabase',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.StartSwitchDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_switch_database(
        self,
        request: polardbx_20200202_models.StartSwitchDatabaseRequest,
    ) -> polardbx_20200202_models.StartSwitchDatabaseResponse:
        """
        @summary 开始评估迁移切换
        
        @param request: StartSwitchDatabaseRequest
        @return: StartSwitchDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_switch_database_with_options(request, runtime)

    async def start_switch_database_async(
        self,
        request: polardbx_20200202_models.StartSwitchDatabaseRequest,
    ) -> polardbx_20200202_models.StartSwitchDatabaseResponse:
        """
        @summary 开始评估迁移切换
        
        @param request: StartSwitchDatabaseRequest
        @return: StartSwitchDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_switch_database_with_options_async(request, runtime)

    def stop_data_import_task_with_options(
        self,
        request: polardbx_20200202_models.StopDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.StopDataImportTaskResponse:
        """
        @summary 暂停数据导入任务
        
        @param request: StopDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.StopDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_import_task_with_options_async(
        self,
        request: polardbx_20200202_models.StopDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.StopDataImportTaskResponse:
        """
        @summary 暂停数据导入任务
        
        @param request: StopDataImportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDataImportTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.StopDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_import_task(
        self,
        request: polardbx_20200202_models.StopDataImportTaskRequest,
    ) -> polardbx_20200202_models.StopDataImportTaskResponse:
        """
        @summary 暂停数据导入任务
        
        @param request: StopDataImportTaskRequest
        @return: StopDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_data_import_task_with_options(request, runtime)

    async def stop_data_import_task_async(
        self,
        request: polardbx_20200202_models.StopDataImportTaskRequest,
    ) -> polardbx_20200202_models.StopDataImportTaskResponse:
        """
        @summary 暂停数据导入任务
        
        @param request: StopDataImportTaskRequest
        @return: StopDataImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_data_import_task_with_options_async(request, runtime)

    def submit_sql_flashback_task_with_options(
        self,
        request: polardbx_20200202_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SubmitSqlFlashbackTaskResponse:
        """
        @summary 提交SQL闪回任务
        
        @param request: SubmitSqlFlashbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSqlFlashbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSqlFlashbackTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SubmitSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sql_flashback_task_with_options_async(
        self,
        request: polardbx_20200202_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SubmitSqlFlashbackTaskResponse:
        """
        @summary 提交SQL闪回任务
        
        @param request: SubmitSqlFlashbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSqlFlashbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not UtilClient.is_unset(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSqlFlashbackTask',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SubmitSqlFlashbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sql_flashback_task(
        self,
        request: polardbx_20200202_models.SubmitSqlFlashbackTaskRequest,
    ) -> polardbx_20200202_models.SubmitSqlFlashbackTaskResponse:
        """
        @summary 提交SQL闪回任务
        
        @param request: SubmitSqlFlashbackTaskRequest
        @return: SubmitSqlFlashbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    async def submit_sql_flashback_task_async(
        self,
        request: polardbx_20200202_models.SubmitSqlFlashbackTaskRequest,
    ) -> polardbx_20200202_models.SubmitSqlFlashbackTaskResponse:
        """
        @summary 提交SQL闪回任务
        
        @param request: SubmitSqlFlashbackTaskRequest
        @return: SubmitSqlFlashbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_sql_flashback_task_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: polardbx_20200202_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SwitchDBInstanceHAResponse:
        """
        @param request: SwitchDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_primary_azone_id):
            query['TargetPrimaryAzoneId'] = request.target_primary_azone_id
        if not UtilClient.is_unset(request.target_primary_region_id):
            query['TargetPrimaryRegionId'] = request.target_primary_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: polardbx_20200202_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SwitchDBInstanceHAResponse:
        """
        @param request: SwitchDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_primary_azone_id):
            query['TargetPrimaryAzoneId'] = request.target_primary_azone_id
        if not UtilClient.is_unset(request.target_primary_region_id):
            query['TargetPrimaryRegionId'] = request.target_primary_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SwitchDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: polardbx_20200202_models.SwitchDBInstanceHARequest,
    ) -> polardbx_20200202_models.SwitchDBInstanceHAResponse:
        """
        @param request: SwitchDBInstanceHARequest
        @return: SwitchDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: polardbx_20200202_models.SwitchDBInstanceHARequest,
    ) -> polardbx_20200202_models.SwitchDBInstanceHAResponse:
        """
        @param request: SwitchDBInstanceHARequest
        @return: SwitchDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

    def switch_gdn_member_role_with_options(
        self,
        request: polardbx_20200202_models.SwitchGdnMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SwitchGdnMemberRoleResponse:
        """
        @summary GDN主备切换
        
        @param request: SwitchGdnMemberRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchGdnMemberRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.task_timeout):
            query['TaskTimeout'] = request.task_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGdnMemberRole',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SwitchGdnMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_gdn_member_role_with_options_async(
        self,
        request: polardbx_20200202_models.SwitchGdnMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.SwitchGdnMemberRoleResponse:
        """
        @summary GDN主备切换
        
        @param request: SwitchGdnMemberRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchGdnMemberRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.task_timeout):
            query['TaskTimeout'] = request.task_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGdnMemberRole',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.SwitchGdnMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_gdn_member_role(
        self,
        request: polardbx_20200202_models.SwitchGdnMemberRoleRequest,
    ) -> polardbx_20200202_models.SwitchGdnMemberRoleResponse:
        """
        @summary GDN主备切换
        
        @param request: SwitchGdnMemberRoleRequest
        @return: SwitchGdnMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_gdn_member_role_with_options(request, runtime)

    async def switch_gdn_member_role_async(
        self,
        request: polardbx_20200202_models.SwitchGdnMemberRoleRequest,
    ) -> polardbx_20200202_models.SwitchGdnMemberRoleResponse:
        """
        @summary GDN主备切换
        
        @param request: SwitchGdnMemberRoleRequest
        @return: SwitchGdnMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_gdn_member_role_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: polardbx_20200202_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: polardbx_20200202_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: polardbx_20200202_models.TagResourcesRequest,
    ) -> polardbx_20200202_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: polardbx_20200202_models.TagResourcesRequest,
    ) -> polardbx_20200202_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: polardbx_20200202_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: polardbx_20200202_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: polardbx_20200202_models.UntagResourcesRequest,
    ) -> polardbx_20200202_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: polardbx_20200202_models.UntagResourcesRequest,
    ) -> polardbx_20200202_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_backup_policy_with_options(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        """
        @param request: UpdateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_begin):
            query['BackupPlanBegin'] = request.backup_plan_begin
        if not UtilClient.is_unset(request.backup_set_retention):
            query['BackupSetRetention'] = request.backup_set_retention
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.backup_way):
            query['BackupWay'] = request.backup_way
        if not UtilClient.is_unset(request.cold_data_backup_interval):
            query['ColdDataBackupInterval'] = request.cold_data_backup_interval
        if not UtilClient.is_unset(request.cold_data_backup_retention):
            query['ColdDataBackupRetention'] = request.cold_data_backup_retention
        if not UtilClient.is_unset(request.cross_region_data_backup_retention):
            query['CrossRegionDataBackupRetention'] = request.cross_region_data_backup_retention
        if not UtilClient.is_unset(request.cross_region_log_backup_retention):
            query['CrossRegionLogBackupRetention'] = request.cross_region_log_backup_retention
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not UtilClient.is_unset(request.force_clean_on_high_space_usage):
            query['ForceCleanOnHighSpaceUsage'] = request.force_clean_on_high_space_usage
        if not UtilClient.is_unset(request.is_cross_region_data_backup_enabled):
            query['IsCrossRegionDataBackupEnabled'] = request.is_cross_region_data_backup_enabled
        if not UtilClient.is_unset(request.is_cross_region_log_backup_enabled):
            query['IsCrossRegionLogBackupEnabled'] = request.is_cross_region_log_backup_enabled
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.local_log_retention):
            query['LocalLogRetention'] = request.local_log_retention
        if not UtilClient.is_unset(request.local_log_retention_number):
            query['LocalLogRetentionNumber'] = request.local_log_retention_number
        if not UtilClient.is_unset(request.log_local_retention_space):
            query['LogLocalRetentionSpace'] = request.log_local_retention_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_log_retention):
            query['RemoveLogRetention'] = request.remove_log_retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBackupPolicy',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_policy_with_options_async(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        """
        @param request: UpdateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_begin):
            query['BackupPlanBegin'] = request.backup_plan_begin
        if not UtilClient.is_unset(request.backup_set_retention):
            query['BackupSetRetention'] = request.backup_set_retention
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.backup_way):
            query['BackupWay'] = request.backup_way
        if not UtilClient.is_unset(request.cold_data_backup_interval):
            query['ColdDataBackupInterval'] = request.cold_data_backup_interval
        if not UtilClient.is_unset(request.cold_data_backup_retention):
            query['ColdDataBackupRetention'] = request.cold_data_backup_retention
        if not UtilClient.is_unset(request.cross_region_data_backup_retention):
            query['CrossRegionDataBackupRetention'] = request.cross_region_data_backup_retention
        if not UtilClient.is_unset(request.cross_region_log_backup_retention):
            query['CrossRegionLogBackupRetention'] = request.cross_region_log_backup_retention
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not UtilClient.is_unset(request.force_clean_on_high_space_usage):
            query['ForceCleanOnHighSpaceUsage'] = request.force_clean_on_high_space_usage
        if not UtilClient.is_unset(request.is_cross_region_data_backup_enabled):
            query['IsCrossRegionDataBackupEnabled'] = request.is_cross_region_data_backup_enabled
        if not UtilClient.is_unset(request.is_cross_region_log_backup_enabled):
            query['IsCrossRegionLogBackupEnabled'] = request.is_cross_region_log_backup_enabled
        if not UtilClient.is_unset(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not UtilClient.is_unset(request.local_log_retention):
            query['LocalLogRetention'] = request.local_log_retention
        if not UtilClient.is_unset(request.local_log_retention_number):
            query['LocalLogRetentionNumber'] = request.local_log_retention_number
        if not UtilClient.is_unset(request.log_local_retention_space):
            query['LogLocalRetentionSpace'] = request.log_local_retention_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_log_retention):
            query['RemoveLogRetention'] = request.remove_log_retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBackupPolicy',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_policy(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        """
        @param request: UpdateBackupPolicyRequest
        @return: UpdateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_backup_policy_with_options(request, runtime)

    async def update_backup_policy_async(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        """
        @param request: UpdateBackupPolicyRequest
        @return: UpdateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_backup_policy_with_options_async(request, runtime)

    def update_dbinstance_sslwith_options(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        """
        @param request: UpdateDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_common_name):
            query['CertCommonName'] = request.cert_common_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstanceSSL',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_sslwith_options_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        """
        @param request: UpdateDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_common_name):
            query['CertCommonName'] = request.cert_common_name
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstanceSSL',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_ssl(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        """
        @param request: UpdateDBInstanceSSLRequest
        @return: UpdateDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_sslwith_options(request, runtime)

    async def update_dbinstance_ssl_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        """
        @param request: UpdateDBInstanceSSLRequest
        @return: UpdateDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_sslwith_options_async(request, runtime)

    def update_dbinstance_tdewith_options(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        """
        @param request: UpdateDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstanceTDE',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_tdewith_options_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        """
        @param request: UpdateDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstanceTDE',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_tde(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        """
        @param request: UpdateDBInstanceTDERequest
        @return: UpdateDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_tdewith_options(request, runtime)

    async def update_dbinstance_tde_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        """
        @param request: UpdateDBInstanceTDERequest
        @return: UpdateDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_tdewith_options_async(request, runtime)

    def update_polar_dbxinstance_node_with_options(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        """
        @summary 扩缩容实例节点数
        
        @param request: UpdatePolarDBXInstanceNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolarDBXInstanceNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_dnspec):
            query['AddDNSpec'] = request.add_dnspec
        if not UtilClient.is_unset(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not UtilClient.is_unset(request.db_instance_node_count):
            query['DbInstanceNodeCount'] = request.db_instance_node_count
        if not UtilClient.is_unset(request.delete_dnids):
            query['DeleteDNIds'] = request.delete_dnids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolarDBXInstanceNode',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_polar_dbxinstance_node_with_options_async(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        """
        @summary 扩缩容实例节点数
        
        @param request: UpdatePolarDBXInstanceNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolarDBXInstanceNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_dnspec):
            query['AddDNSpec'] = request.add_dnspec
        if not UtilClient.is_unset(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not UtilClient.is_unset(request.db_instance_node_count):
            query['DbInstanceNodeCount'] = request.db_instance_node_count
        if not UtilClient.is_unset(request.delete_dnids):
            query['DeleteDNIds'] = request.delete_dnids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolarDBXInstanceNode',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_polar_dbxinstance_node(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        """
        @summary 扩缩容实例节点数
        
        @param request: UpdatePolarDBXInstanceNodeRequest
        @return: UpdatePolarDBXInstanceNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_polar_dbxinstance_node_with_options(request, runtime)

    async def update_polar_dbxinstance_node_async(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        """
        @summary 扩缩容实例节点数
        
        @param request: UpdatePolarDBXInstanceNodeRequest
        @return: UpdatePolarDBXInstanceNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_polar_dbxinstance_node_with_options_async(request, runtime)

    def upgrade_cdcversion_with_options(
        self,
        request: polardbx_20200202_models.UpgradeCDCVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeCDCVersionResponse:
        """
        @summary 升级CDC版本
        
        @param request: UpgradeCDCVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeCDCVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdc_db_version):
            query['CdcDbVersion'] = request.cdc_db_version
        if not UtilClient.is_unset(request.cdc_minor_version):
            query['CdcMinorVersion'] = request.cdc_minor_version
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCDCVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeCDCVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cdcversion_with_options_async(
        self,
        request: polardbx_20200202_models.UpgradeCDCVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeCDCVersionResponse:
        """
        @summary 升级CDC版本
        
        @param request: UpgradeCDCVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeCDCVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdc_db_version):
            query['CdcDbVersion'] = request.cdc_db_version
        if not UtilClient.is_unset(request.cdc_minor_version):
            query['CdcMinorVersion'] = request.cdc_minor_version
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCDCVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeCDCVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cdcversion(
        self,
        request: polardbx_20200202_models.UpgradeCDCVersionRequest,
    ) -> polardbx_20200202_models.UpgradeCDCVersionResponse:
        """
        @summary 升级CDC版本
        
        @param request: UpgradeCDCVersionRequest
        @return: UpgradeCDCVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cdcversion_with_options(request, runtime)

    async def upgrade_cdcversion_async(
        self,
        request: polardbx_20200202_models.UpgradeCDCVersionRequest,
    ) -> polardbx_20200202_models.UpgradeCDCVersionResponse:
        """
        @summary 升级CDC版本
        
        @param request: UpgradeCDCVersionRequest
        @return: UpgradeCDCVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cdcversion_with_options_async(request, runtime)

    def upgrade_columnar_version_with_options(
        self,
        request: polardbx_20200202_models.UpgradeColumnarVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeColumnarVersionResponse:
        """
        @summary 升级Columnar版本
        
        @param request: UpgradeColumnarVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeColumnarVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columnar_version):
            query['ColumnarVersion'] = request.columnar_version
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeColumnarVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeColumnarVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_columnar_version_with_options_async(
        self,
        request: polardbx_20200202_models.UpgradeColumnarVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeColumnarVersionResponse:
        """
        @summary 升级Columnar版本
        
        @param request: UpgradeColumnarVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeColumnarVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columnar_version):
            query['ColumnarVersion'] = request.columnar_version
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeColumnarVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeColumnarVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_columnar_version(
        self,
        request: polardbx_20200202_models.UpgradeColumnarVersionRequest,
    ) -> polardbx_20200202_models.UpgradeColumnarVersionResponse:
        """
        @summary 升级Columnar版本
        
        @param request: UpgradeColumnarVersionRequest
        @return: UpgradeColumnarVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_columnar_version_with_options(request, runtime)

    async def upgrade_columnar_version_async(
        self,
        request: polardbx_20200202_models.UpgradeColumnarVersionRequest,
    ) -> polardbx_20200202_models.UpgradeColumnarVersionResponse:
        """
        @summary 升级Columnar版本
        
        @param request: UpgradeColumnarVersionRequest
        @return: UpgradeColumnarVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_columnar_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @param request: UpgradeDBInstanceKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @param request: UpgradeDBInstanceKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2020-02-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @param request: UpgradeDBInstanceKernelVersionRequest
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @param request: UpgradeDBInstanceKernelVersionRequest
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
