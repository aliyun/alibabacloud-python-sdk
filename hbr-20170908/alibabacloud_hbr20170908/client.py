# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hbr20170908 import models as hbr_20170908_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'hbr.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbr.aliyuncs.com',
            'cn-beijing-gov-1': 'hbr.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbr.aliyuncs.com',
            'cn-edge-1': 'hbr.aliyuncs.com',
            'cn-fujian': 'hbr.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbr.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbr.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbr.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbr.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hbr.aliyuncs.com',
            'cn-qingdao-nebula': 'hbr.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-inner': 'hbr.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbr.aliyuncs.com',
            'cn-shenzhen-inner': 'hbr.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbr.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbr.aliyuncs.com',
            'cn-wuhan': 'hbr.aliyuncs.com',
            'cn-yushanfang': 'hbr.aliyuncs.com',
            'cn-zhangbei': 'hbr.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbr.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbr.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbr.aliyuncs.com',
            'eu-west-1-oxs': 'hbr.aliyuncs.com',
            'rus-west-1-pop': 'hbr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hbr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_container_cluster_with_options(
        self,
        request: hbr_20170908_models.AddContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.AddContainerClusterResponse:
        """
        @summary Registers a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AddContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.AddContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_container_cluster_with_options_async(
        self,
        request: hbr_20170908_models.AddContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.AddContainerClusterResponse:
        """
        @summary Registers a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AddContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.AddContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_container_cluster(
        self,
        request: hbr_20170908_models.AddContainerClusterRequest,
    ) -> hbr_20170908_models.AddContainerClusterResponse:
        """
        @summary Registers a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AddContainerClusterRequest
        @return: AddContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_container_cluster_with_options(request, runtime)

    async def add_container_cluster_async(
        self,
        request: hbr_20170908_models.AddContainerClusterRequest,
    ) -> hbr_20170908_models.AddContainerClusterResponse:
        """
        @summary Registers a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AddContainerClusterRequest
        @return: AddContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_container_cluster_with_options_async(request, runtime)

    def cancel_backup_job_with_options(
        self,
        request: hbr_20170908_models.CancelBackupJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CancelBackupJobResponse:
        """
        @summary Cancels a backup job.
        
        @param request: CancelBackupJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelBackupJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_backup_job_with_options_async(
        self,
        request: hbr_20170908_models.CancelBackupJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CancelBackupJobResponse:
        """
        @summary Cancels a backup job.
        
        @param request: CancelBackupJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelBackupJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelBackupJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_backup_job(
        self,
        request: hbr_20170908_models.CancelBackupJobRequest,
    ) -> hbr_20170908_models.CancelBackupJobResponse:
        """
        @summary Cancels a backup job.
        
        @param request: CancelBackupJobRequest
        @return: CancelBackupJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_backup_job_with_options(request, runtime)

    async def cancel_backup_job_async(
        self,
        request: hbr_20170908_models.CancelBackupJobRequest,
    ) -> hbr_20170908_models.CancelBackupJobResponse:
        """
        @summary Cancels a backup job.
        
        @param request: CancelBackupJobRequest
        @return: CancelBackupJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_backup_job_with_options_async(request, runtime)

    def cancel_restore_job_with_options(
        self,
        request: hbr_20170908_models.CancelRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CancelRestoreJobResponse:
        """
        @summary Cancels a restore job.
        
        @param request: CancelRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRestoreJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_restore_job_with_options_async(
        self,
        request: hbr_20170908_models.CancelRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CancelRestoreJobResponse:
        """
        @summary Cancels a restore job.
        
        @param request: CancelRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRestoreJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CancelRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_restore_job(
        self,
        request: hbr_20170908_models.CancelRestoreJobRequest,
    ) -> hbr_20170908_models.CancelRestoreJobResponse:
        """
        @summary Cancels a restore job.
        
        @param request: CancelRestoreJobRequest
        @return: CancelRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_restore_job_with_options(request, runtime)

    async def cancel_restore_job_async(
        self,
        request: hbr_20170908_models.CancelRestoreJobRequest,
    ) -> hbr_20170908_models.CancelRestoreJobResponse:
        """
        @summary Cancels a restore job.
        
        @param request: CancelRestoreJobRequest
        @return: CancelRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_restore_job_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: hbr_20170908_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @description    In the Cloud Backup console, you can use resource groups to manage resources such as backup vaults, Cloud Backup clients, and SAP HANA instances.
        A resource is a cloud service entity that you create on Alibaba Cloud, such as an Elastic Compute Service (ECS) instance, a backup vault, or an SAP HANA instance.
        You can sort resources owned by your Alibaba Cloud account into various resource groups. Resource groups facilitate resource management among multiple projects or applications within your Alibaba Cloud account and simplify permission management.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: hbr_20170908_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @description    In the Cloud Backup console, you can use resource groups to manage resources such as backup vaults, Cloud Backup clients, and SAP HANA instances.
        A resource is a cloud service entity that you create on Alibaba Cloud, such as an Elastic Compute Service (ECS) instance, a backup vault, or an SAP HANA instance.
        You can sort resources owned by your Alibaba Cloud account into various resource groups. Resource groups facilitate resource management among multiple projects or applications within your Alibaba Cloud account and simplify permission management.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: hbr_20170908_models.ChangeResourceGroupRequest,
    ) -> hbr_20170908_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @description    In the Cloud Backup console, you can use resource groups to manage resources such as backup vaults, Cloud Backup clients, and SAP HANA instances.
        A resource is a cloud service entity that you create on Alibaba Cloud, such as an Elastic Compute Service (ECS) instance, a backup vault, or an SAP HANA instance.
        You can sort resources owned by your Alibaba Cloud account into various resource groups. Resource groups facilitate resource management among multiple projects or applications within your Alibaba Cloud account and simplify permission management.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: hbr_20170908_models.ChangeResourceGroupRequest,
    ) -> hbr_20170908_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @description    In the Cloud Backup console, you can use resource groups to manage resources such as backup vaults, Cloud Backup clients, and SAP HANA instances.
        A resource is a cloud service entity that you create on Alibaba Cloud, such as an Elastic Compute Service (ECS) instance, a backup vault, or an SAP HANA instance.
        You can sort resources owned by your Alibaba Cloud account into various resource groups. Resource groups facilitate resource management among multiple projects or applications within your Alibaba Cloud account and simplify permission management.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_role_with_options(
        self,
        request: hbr_20170908_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CheckRoleResponse:
        """
        @summary Checks whether the user has permissions to access the current resource or page.
        
        @param request: CheckRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_role_type):
            query['CheckRoleType'] = request.check_role_type
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRole',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CheckRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_role_with_options_async(
        self,
        request: hbr_20170908_models.CheckRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CheckRoleResponse:
        """
        @summary Checks whether the user has permissions to access the current resource or page.
        
        @param request: CheckRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_role_type):
            query['CheckRoleType'] = request.check_role_type
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRole',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CheckRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_role(
        self,
        request: hbr_20170908_models.CheckRoleRequest,
    ) -> hbr_20170908_models.CheckRoleResponse:
        """
        @summary Checks whether the user has permissions to access the current resource or page.
        
        @param request: CheckRoleRequest
        @return: CheckRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_role_with_options(request, runtime)

    async def check_role_async(
        self,
        request: hbr_20170908_models.CheckRoleRequest,
    ) -> hbr_20170908_models.CheckRoleResponse:
        """
        @summary Checks whether the user has permissions to access the current resource or page.
        
        @param request: CheckRoleRequest
        @return: CheckRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_role_with_options_async(request, runtime)

    def create_backup_job_with_options(
        self,
        tmp_req: hbr_20170908_models.CreateBackupJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateBackupJobResponse:
        """
        @summary Creates a backup job.
        
        @param tmp_req: CreateBackupJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_cluster_id):
            query['ContainerClusterId'] = request.container_cluster_id
        if not UtilClient.is_unset(request.container_resources):
            query['ContainerResources'] = request.container_resources
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.exclude):
            query['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            query['Include'] = request.include
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_job_with_options_async(
        self,
        tmp_req: hbr_20170908_models.CreateBackupJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateBackupJobResponse:
        """
        @summary Creates a backup job.
        
        @param tmp_req: CreateBackupJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_cluster_id):
            query['ContainerClusterId'] = request.container_cluster_id
        if not UtilClient.is_unset(request.container_resources):
            query['ContainerResources'] = request.container_resources
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.exclude):
            query['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            query['Include'] = request.include
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_job(
        self,
        request: hbr_20170908_models.CreateBackupJobRequest,
    ) -> hbr_20170908_models.CreateBackupJobResponse:
        """
        @summary Creates a backup job.
        
        @param request: CreateBackupJobRequest
        @return: CreateBackupJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_job_with_options(request, runtime)

    async def create_backup_job_async(
        self,
        request: hbr_20170908_models.CreateBackupJobRequest,
    ) -> hbr_20170908_models.CreateBackupJobResponse:
        """
        @summary Creates a backup job.
        
        @param request: CreateBackupJobRequest
        @return: CreateBackupJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_job_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        tmp_req: hbr_20170908_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateBackupPlanResponse:
        """
        @summary Create a backup plan.
        
        @description - A backup plan associates data sources with backup policies and other necessary information for backups. After the execution of a backup plan, it generates a backup task that records the progress and results of the backup. If the backup task is successful, a backup snapshot is created. You can use the backup snapshot to create a recovery task.
        - A backup plan supports only one type of data source.
        - A backup plan supports only a single fixed interval backup cycle strategy.
        - A backup plan can back up to only one backup vault.
        
        @param tmp_req: CreateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_data_source_detail):
            request.dest_data_source_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_data_source_detail, 'DestDataSourceDetail', 'json')
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.dest_data_source_detail_shrink):
            query['DestDataSourceDetail'] = request.dest_data_source_detail_shrink
        if not UtilClient.is_unset(request.dest_data_source_id):
            query['DestDataSourceId'] = request.dest_data_source_id
        if not UtilClient.is_unset(request.dest_source_type):
            query['DestSourceType'] = request.dest_source_type
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        if not UtilClient.is_unset(request.speed_limit):
            body['SpeedLimit'] = request.speed_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        tmp_req: hbr_20170908_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateBackupPlanResponse:
        """
        @summary Create a backup plan.
        
        @description - A backup plan associates data sources with backup policies and other necessary information for backups. After the execution of a backup plan, it generates a backup task that records the progress and results of the backup. If the backup task is successful, a backup snapshot is created. You can use the backup snapshot to create a recovery task.
        - A backup plan supports only one type of data source.
        - A backup plan supports only a single fixed interval backup cycle strategy.
        - A backup plan can back up to only one backup vault.
        
        @param tmp_req: CreateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_data_source_detail):
            request.dest_data_source_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_data_source_detail, 'DestDataSourceDetail', 'json')
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.dest_data_source_detail_shrink):
            query['DestDataSourceDetail'] = request.dest_data_source_detail_shrink
        if not UtilClient.is_unset(request.dest_data_source_id):
            query['DestDataSourceId'] = request.dest_data_source_id
        if not UtilClient.is_unset(request.dest_source_type):
            query['DestSourceType'] = request.dest_source_type
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        if not UtilClient.is_unset(request.speed_limit):
            body['SpeedLimit'] = request.speed_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_plan(
        self,
        request: hbr_20170908_models.CreateBackupPlanRequest,
    ) -> hbr_20170908_models.CreateBackupPlanResponse:
        """
        @summary Create a backup plan.
        
        @description - A backup plan associates data sources with backup policies and other necessary information for backups. After the execution of a backup plan, it generates a backup task that records the progress and results of the backup. If the backup task is successful, a backup snapshot is created. You can use the backup snapshot to create a recovery task.
        - A backup plan supports only one type of data source.
        - A backup plan supports only a single fixed interval backup cycle strategy.
        - A backup plan can back up to only one backup vault.
        
        @param request: CreateBackupPlanRequest
        @return: CreateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: hbr_20170908_models.CreateBackupPlanRequest,
    ) -> hbr_20170908_models.CreateBackupPlanResponse:
        """
        @summary Create a backup plan.
        
        @description - A backup plan associates data sources with backup policies and other necessary information for backups. After the execution of a backup plan, it generates a backup task that records the progress and results of the backup. If the backup task is successful, a backup snapshot is created. You can use the backup snapshot to create a recovery task.
        - A backup plan supports only one type of data source.
        - A backup plan supports only a single fixed interval backup cycle strategy.
        - A backup plan can back up to only one backup vault.
        
        @param request: CreateBackupPlanRequest
        @return: CreateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_clients_with_options(
        self,
        request: hbr_20170908_models.CreateClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateClientsResponse:
        """
        @summary Installs one or more Cloud Backup clients on specified instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and pricing of Cloud Backup. For more information, see [Billing methods and billable items](https://help.aliyun.com/document_detail/89062.html).
        
        @param request: CreateClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_clients_with_options_async(
        self,
        request: hbr_20170908_models.CreateClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateClientsResponse:
        """
        @summary Installs one or more Cloud Backup clients on specified instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and pricing of Cloud Backup. For more information, see [Billing methods and billable items](https://help.aliyun.com/document_detail/89062.html).
        
        @param request: CreateClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_clients(
        self,
        request: hbr_20170908_models.CreateClientsRequest,
    ) -> hbr_20170908_models.CreateClientsResponse:
        """
        @summary Installs one or more Cloud Backup clients on specified instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and pricing of Cloud Backup. For more information, see [Billing methods and billable items](https://help.aliyun.com/document_detail/89062.html).
        
        @param request: CreateClientsRequest
        @return: CreateClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_clients_with_options(request, runtime)

    async def create_clients_async(
        self,
        request: hbr_20170908_models.CreateClientsRequest,
    ) -> hbr_20170908_models.CreateClientsResponse:
        """
        @summary Installs one or more Cloud Backup clients on specified instances.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and pricing of Cloud Backup. For more information, see [Billing methods and billable items](https://help.aliyun.com/document_detail/89062.html).
        
        @param request: CreateClientsRequest
        @return: CreateClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_clients_with_options_async(request, runtime)

    def create_hana_backup_plan_with_options(
        self,
        request: hbr_20170908_models.CreateHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaBackupPlanResponse:
        """
        @summary Creates a backup plan for an SAP HANA instance.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: CreateHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.CreateHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaBackupPlanResponse:
        """
        @summary Creates a backup plan for an SAP HANA instance.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: CreateHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_backup_plan(
        self,
        request: hbr_20170908_models.CreateHanaBackupPlanRequest,
    ) -> hbr_20170908_models.CreateHanaBackupPlanResponse:
        """
        @summary Creates a backup plan for an SAP HANA instance.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: CreateHanaBackupPlanRequest
        @return: CreateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_backup_plan_with_options(request, runtime)

    async def create_hana_backup_plan_async(
        self,
        request: hbr_20170908_models.CreateHanaBackupPlanRequest,
    ) -> hbr_20170908_models.CreateHanaBackupPlanResponse:
        """
        @summary Creates a backup plan for an SAP HANA instance.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: CreateHanaBackupPlanRequest
        @return: CreateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hana_backup_plan_with_options_async(request, runtime)

    def create_hana_instance_with_options(
        self,
        request: hbr_20170908_models.CreateHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaInstanceResponse:
        """
        @summary Registers an SAP HANA instance.
        
        @description To register an SAP HANA instance, you must configure the SAP HANA connection information. After the SAP HANA instance is registered, Cloud Backup installs a backup client on the node of the SAP HANA instance.
        
        @param request: CreateHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_instance_with_options_async(
        self,
        request: hbr_20170908_models.CreateHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaInstanceResponse:
        """
        @summary Registers an SAP HANA instance.
        
        @description To register an SAP HANA instance, you must configure the SAP HANA connection information. After the SAP HANA instance is registered, Cloud Backup installs a backup client on the node of the SAP HANA instance.
        
        @param request: CreateHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_instance(
        self,
        request: hbr_20170908_models.CreateHanaInstanceRequest,
    ) -> hbr_20170908_models.CreateHanaInstanceResponse:
        """
        @summary Registers an SAP HANA instance.
        
        @description To register an SAP HANA instance, you must configure the SAP HANA connection information. After the SAP HANA instance is registered, Cloud Backup installs a backup client on the node of the SAP HANA instance.
        
        @param request: CreateHanaInstanceRequest
        @return: CreateHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_instance_with_options(request, runtime)

    async def create_hana_instance_async(
        self,
        request: hbr_20170908_models.CreateHanaInstanceRequest,
    ) -> hbr_20170908_models.CreateHanaInstanceResponse:
        """
        @summary Registers an SAP HANA instance.
        
        @description To register an SAP HANA instance, you must configure the SAP HANA connection information. After the SAP HANA instance is registered, Cloud Backup installs a backup client on the node of the SAP HANA instance.
        
        @param request: CreateHanaInstanceRequest
        @return: CreateHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hana_instance_with_options_async(request, runtime)

    def create_hana_restore_with_options(
        self,
        request: hbr_20170908_models.CreateHanaRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaRestoreResponse:
        """
        @summary Creates a restore job for an SAP HANA database.
        
        @description If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](https://help.aliyun.com/document_detail/101178.html).
        
        @param request: CreateHanaRestoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaRestoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.check_access):
            query['CheckAccess'] = request.check_access
        if not UtilClient.is_unset(request.clear_log):
            query['ClearLog'] = request.clear_log
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.master_client_id):
            query['MasterClientId'] = request.master_client_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.sid_admin):
            query['SidAdmin'] = request.sid_admin
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_catalog):
            query['UseCatalog'] = request.use_catalog
        if not UtilClient.is_unset(request.use_delta):
            query['UseDelta'] = request.use_delta
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaRestore',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaRestoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_restore_with_options_async(
        self,
        request: hbr_20170908_models.CreateHanaRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateHanaRestoreResponse:
        """
        @summary Creates a restore job for an SAP HANA database.
        
        @description If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](https://help.aliyun.com/document_detail/101178.html).
        
        @param request: CreateHanaRestoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHanaRestoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.check_access):
            query['CheckAccess'] = request.check_access
        if not UtilClient.is_unset(request.clear_log):
            query['ClearLog'] = request.clear_log
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.master_client_id):
            query['MasterClientId'] = request.master_client_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.sid_admin):
            query['SidAdmin'] = request.sid_admin
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_catalog):
            query['UseCatalog'] = request.use_catalog
        if not UtilClient.is_unset(request.use_delta):
            query['UseDelta'] = request.use_delta
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHanaRestore',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateHanaRestoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_restore(
        self,
        request: hbr_20170908_models.CreateHanaRestoreRequest,
    ) -> hbr_20170908_models.CreateHanaRestoreResponse:
        """
        @summary Creates a restore job for an SAP HANA database.
        
        @description If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](https://help.aliyun.com/document_detail/101178.html).
        
        @param request: CreateHanaRestoreRequest
        @return: CreateHanaRestoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hana_restore_with_options(request, runtime)

    async def create_hana_restore_async(
        self,
        request: hbr_20170908_models.CreateHanaRestoreRequest,
    ) -> hbr_20170908_models.CreateHanaRestoreResponse:
        """
        @summary Creates a restore job for an SAP HANA database.
        
        @description If you call this operation to restore a database, the database is restored to a specified state. Proceed with caution. For more information, see [Restore databases to an SAP HANA instance](https://help.aliyun.com/document_detail/101178.html).
        
        @param request: CreateHanaRestoreRequest
        @return: CreateHanaRestoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hana_restore_with_options_async(request, runtime)

    def create_policy_bindings_with_options(
        self,
        tmp_req: hbr_20170908_models.CreatePolicyBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreatePolicyBindingsResponse:
        """
        @summary Binds one or more data sources to a backup policy.
        
        @description    You can bind data sources to only one policy in each request.
        Elastic Compute Service (ECS) instances can be bound to only one policy.
        
        @param tmp_req: CreatePolicyBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyBindingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_binding_list):
            request.policy_binding_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_binding_list, 'PolicyBindingList', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_binding_list_shrink):
            query['PolicyBindingList'] = request.policy_binding_list_shrink
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_bindings_with_options_async(
        self,
        tmp_req: hbr_20170908_models.CreatePolicyBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreatePolicyBindingsResponse:
        """
        @summary Binds one or more data sources to a backup policy.
        
        @description    You can bind data sources to only one policy in each request.
        Elastic Compute Service (ECS) instances can be bound to only one policy.
        
        @param tmp_req: CreatePolicyBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyBindingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_binding_list):
            request.policy_binding_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_binding_list, 'PolicyBindingList', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_binding_list_shrink):
            query['PolicyBindingList'] = request.policy_binding_list_shrink
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_bindings(
        self,
        request: hbr_20170908_models.CreatePolicyBindingsRequest,
    ) -> hbr_20170908_models.CreatePolicyBindingsResponse:
        """
        @summary Binds one or more data sources to a backup policy.
        
        @description    You can bind data sources to only one policy in each request.
        Elastic Compute Service (ECS) instances can be bound to only one policy.
        
        @param request: CreatePolicyBindingsRequest
        @return: CreatePolicyBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_bindings_with_options(request, runtime)

    async def create_policy_bindings_async(
        self,
        request: hbr_20170908_models.CreatePolicyBindingsRequest,
    ) -> hbr_20170908_models.CreatePolicyBindingsResponse:
        """
        @summary Binds one or more data sources to a backup policy.
        
        @description    You can bind data sources to only one policy in each request.
        Elastic Compute Service (ECS) instances can be bound to only one policy.
        
        @param request: CreatePolicyBindingsRequest
        @return: CreatePolicyBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_bindings_with_options_async(request, runtime)

    def create_policy_v2with_options(
        self,
        tmp_req: hbr_20170908_models.CreatePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreatePolicyV2Response:
        """
        @summary Creates a backup policy.
        
        @description A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        You can specify only one interval as a backup cycle in a backup policy.
        Each backup policy allows you to back up data to only one backup vault.
        
        @param tmp_req: CreatePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_v2with_options_async(
        self,
        tmp_req: hbr_20170908_models.CreatePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreatePolicyV2Response:
        """
        @summary Creates a backup policy.
        
        @description A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        You can specify only one interval as a backup cycle in a backup policy.
        Each backup policy allows you to back up data to only one backup vault.
        
        @param tmp_req: CreatePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreatePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_v2(
        self,
        request: hbr_20170908_models.CreatePolicyV2Request,
    ) -> hbr_20170908_models.CreatePolicyV2Response:
        """
        @summary Creates a backup policy.
        
        @description A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        You can specify only one interval as a backup cycle in a backup policy.
        Each backup policy allows you to back up data to only one backup vault.
        
        @param request: CreatePolicyV2Request
        @return: CreatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_v2with_options(request, runtime)

    async def create_policy_v2_async(
        self,
        request: hbr_20170908_models.CreatePolicyV2Request,
    ) -> hbr_20170908_models.CreatePolicyV2Response:
        """
        @summary Creates a backup policy.
        
        @description A backup policy records the information required for backup. After you execute a backup policy, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        A backup policy supports multiple data sources. The data sources can be only Elastic Compute Service (ECS) instances.
        You can specify only one interval as a backup cycle in a backup policy.
        Each backup policy allows you to back up data to only one backup vault.
        
        @param request: CreatePolicyV2Request
        @return: CreatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_v2with_options_async(request, runtime)

    def create_replication_vault_with_options(
        self,
        request: hbr_20170908_models.CreateReplicationVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateReplicationVaultResponse:
        """
        @summary Creates a mirror vault.
        
        @description After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.Call this operation in the region where the mirror vault resides, which is specified by the VaultRegionId parameter.
        
        @param request: CreateReplicationVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReplicationVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not UtilClient.is_unset(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not UtilClient.is_unset(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReplicationVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateReplicationVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_replication_vault_with_options_async(
        self,
        request: hbr_20170908_models.CreateReplicationVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateReplicationVaultResponse:
        """
        @summary Creates a mirror vault.
        
        @description After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.Call this operation in the region where the mirror vault resides, which is specified by the VaultRegionId parameter.
        
        @param request: CreateReplicationVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReplicationVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not UtilClient.is_unset(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not UtilClient.is_unset(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReplicationVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateReplicationVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_replication_vault(
        self,
        request: hbr_20170908_models.CreateReplicationVaultRequest,
    ) -> hbr_20170908_models.CreateReplicationVaultResponse:
        """
        @summary Creates a mirror vault.
        
        @description After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.Call this operation in the region where the mirror vault resides, which is specified by the VaultRegionId parameter.
        
        @param request: CreateReplicationVaultRequest
        @return: CreateReplicationVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_replication_vault_with_options(request, runtime)

    async def create_replication_vault_async(
        self,
        request: hbr_20170908_models.CreateReplicationVaultRequest,
    ) -> hbr_20170908_models.CreateReplicationVaultResponse:
        """
        @summary Creates a mirror vault.
        
        @description After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state.Call this operation in the region where the mirror vault resides, which is specified by the VaultRegionId parameter.
        
        @param request: CreateReplicationVaultRequest
        @return: CreateReplicationVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_replication_vault_with_options_async(request, runtime)

    def create_restore_job_with_options(
        self,
        tmp_req: hbr_20170908_models.CreateRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateRestoreJobResponse:
        """
        @summary Create a restore job.
        
        @description - Create a restore job based on the selected snapshot and the restore destination.
        - Currently, the data source type must match the restore destination data source type.
        
        @param tmp_req: CreateRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRestoreJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateRestoreJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.failback_detail):
            request.failback_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.failback_detail, 'FailbackDetail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        if not UtilClient.is_unset(tmp_req.udm_detail):
            request.udm_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.udm_detail, 'UdmDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.failback_detail_shrink):
            query['FailbackDetail'] = request.failback_detail_shrink
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not UtilClient.is_unset(request.target_container):
            query['TargetContainer'] = request.target_container
        if not UtilClient.is_unset(request.target_container_cluster_id):
            query['TargetContainerClusterId'] = request.target_container_cluster_id
        if not UtilClient.is_unset(request.target_create_time):
            query['TargetCreateTime'] = request.target_create_time
        if not UtilClient.is_unset(request.target_file_system_id):
            query['TargetFileSystemId'] = request.target_file_system_id
        if not UtilClient.is_unset(request.target_instance_name):
            query['TargetInstanceName'] = request.target_instance_name
        if not UtilClient.is_unset(request.target_prefix):
            query['TargetPrefix'] = request.target_prefix
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.target_time):
            query['TargetTime'] = request.target_time
        if not UtilClient.is_unset(request.udm_detail_shrink):
            query['UdmDetail'] = request.udm_detail_shrink
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_path):
            body['TargetPath'] = request.target_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_job_with_options_async(
        self,
        tmp_req: hbr_20170908_models.CreateRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateRestoreJobResponse:
        """
        @summary Create a restore job.
        
        @description - Create a restore job based on the selected snapshot and the restore destination.
        - Currently, the data source type must match the restore destination data source type.
        
        @param tmp_req: CreateRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRestoreJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.CreateRestoreJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.failback_detail):
            request.failback_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.failback_detail, 'FailbackDetail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        if not UtilClient.is_unset(tmp_req.udm_detail):
            request.udm_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.udm_detail, 'UdmDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.failback_detail_shrink):
            query['FailbackDetail'] = request.failback_detail_shrink
        if not UtilClient.is_unset(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not UtilClient.is_unset(request.target_container):
            query['TargetContainer'] = request.target_container
        if not UtilClient.is_unset(request.target_container_cluster_id):
            query['TargetContainerClusterId'] = request.target_container_cluster_id
        if not UtilClient.is_unset(request.target_create_time):
            query['TargetCreateTime'] = request.target_create_time
        if not UtilClient.is_unset(request.target_file_system_id):
            query['TargetFileSystemId'] = request.target_file_system_id
        if not UtilClient.is_unset(request.target_instance_name):
            query['TargetInstanceName'] = request.target_instance_name
        if not UtilClient.is_unset(request.target_prefix):
            query['TargetPrefix'] = request.target_prefix
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.target_time):
            query['TargetTime'] = request.target_time
        if not UtilClient.is_unset(request.udm_detail_shrink):
            query['UdmDetail'] = request.udm_detail_shrink
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_path):
            body['TargetPath'] = request.target_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRestoreJob',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_job(
        self,
        request: hbr_20170908_models.CreateRestoreJobRequest,
    ) -> hbr_20170908_models.CreateRestoreJobResponse:
        """
        @summary Create a restore job.
        
        @description - Create a restore job based on the selected snapshot and the restore destination.
        - Currently, the data source type must match the restore destination data source type.
        
        @param request: CreateRestoreJobRequest
        @return: CreateRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_restore_job_with_options(request, runtime)

    async def create_restore_job_async(
        self,
        request: hbr_20170908_models.CreateRestoreJobRequest,
    ) -> hbr_20170908_models.CreateRestoreJobResponse:
        """
        @summary Create a restore job.
        
        @description - Create a restore job based on the selected snapshot and the restore destination.
        - Currently, the data source type must match the restore destination data source type.
        
        @param request: CreateRestoreJobRequest
        @return: CreateRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_restore_job_with_options_async(request, runtime)

    def create_temp_file_upload_url_with_options(
        self,
        request: hbr_20170908_models.CreateTempFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateTempFileUploadUrlResponse:
        """
        @summary Generates the parameters and signature required for a file upload URL.
        
        @description 1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        
        @param request: CreateTempFileUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTempFileUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTempFileUploadUrl',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateTempFileUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_temp_file_upload_url_with_options_async(
        self,
        request: hbr_20170908_models.CreateTempFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateTempFileUploadUrlResponse:
        """
        @summary Generates the parameters and signature required for a file upload URL.
        
        @description 1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        
        @param request: CreateTempFileUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTempFileUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTempFileUploadUrl',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateTempFileUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_temp_file_upload_url(
        self,
        request: hbr_20170908_models.CreateTempFileUploadUrlRequest,
    ) -> hbr_20170908_models.CreateTempFileUploadUrlResponse:
        """
        @summary Generates the parameters and signature required for a file upload URL.
        
        @description 1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        
        @param request: CreateTempFileUploadUrlRequest
        @return: CreateTempFileUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_temp_file_upload_url_with_options(request, runtime)

    async def create_temp_file_upload_url_async(
        self,
        request: hbr_20170908_models.CreateTempFileUploadUrlRequest,
    ) -> hbr_20170908_models.CreateTempFileUploadUrlResponse:
        """
        @summary Generates the parameters and signature required for a file upload URL.
        
        @description 1.  You can directly upload a file to Object Storage Service (OSS) by using a form based on the returned value of this operation.
        2.  For more information about how to upload a file to OSS by using a form, see OSS documentation.
        3.  The system periodically deletes files that are uploaded to OSS.
        
        @param request: CreateTempFileUploadUrlRequest
        @return: CreateTempFileUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_temp_file_upload_url_with_options_async(request, runtime)

    def create_vault_with_options(
        self,
        request: hbr_20170908_models.CreateVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateVaultResponse:
        """
        @summary Creates a backup vault.
        
        @description    Each Alibaba Cloud account can create up to 100 backup vaults.
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        *\
        *Note** Before you call this operation, make sure that you fully understand the billing of Cloud Backup.
        
        @param request: CreateVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        if not UtilClient.is_unset(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vault_with_options_async(
        self,
        request: hbr_20170908_models.CreateVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.CreateVaultResponse:
        """
        @summary Creates a backup vault.
        
        @description    Each Alibaba Cloud account can create up to 100 backup vaults.
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        *\
        *Note** Before you call this operation, make sure that you fully understand the billing of Cloud Backup.
        
        @param request: CreateVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        if not UtilClient.is_unset(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.CreateVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vault(
        self,
        request: hbr_20170908_models.CreateVaultRequest,
    ) -> hbr_20170908_models.CreateVaultResponse:
        """
        @summary Creates a backup vault.
        
        @description    Each Alibaba Cloud account can create up to 100 backup vaults.
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        *\
        *Note** Before you call this operation, make sure that you fully understand the billing of Cloud Backup.
        
        @param request: CreateVaultRequest
        @return: CreateVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vault_with_options(request, runtime)

    async def create_vault_async(
        self,
        request: hbr_20170908_models.CreateVaultRequest,
    ) -> hbr_20170908_models.CreateVaultResponse:
        """
        @summary Creates a backup vault.
        
        @description    Each Alibaba Cloud account can create up to 100 backup vaults.
        After a backup vault is created, the backup vault is in the INITIALIZING state, and the system automatically runs an initialization task to initialize the backup vault. After the initialization task is completed, the backup vault is in the CREATED state. A backup job can use a backup vault to store backup data only if the backup vault is in the CREATED state.
        *\
        *Note** Before you call this operation, make sure that you fully understand the billing of Cloud Backup.
        
        @param request: CreateVaultRequest
        @return: CreateVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vault_with_options_async(request, runtime)

    def delete_air_ecs_instance_with_options(
        self,
        tmp_req: hbr_20170908_models.DeleteAirEcsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteAirEcsInstanceResponse:
        """
        @summary Removes the Elastic Compute Service (ECS) instance that is used for restoration only in ECS Backup Essential Edition.
        
        @param tmp_req: DeleteAirEcsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAirEcsInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeleteAirEcsInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uninstall_client_source_types):
            request.uninstall_client_source_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uninstall_client_source_types, 'UninstallClientSourceTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.uninstall_client_source_types_shrink):
            query['UninstallClientSourceTypes'] = request.uninstall_client_source_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAirEcsInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteAirEcsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_air_ecs_instance_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DeleteAirEcsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteAirEcsInstanceResponse:
        """
        @summary Removes the Elastic Compute Service (ECS) instance that is used for restoration only in ECS Backup Essential Edition.
        
        @param tmp_req: DeleteAirEcsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAirEcsInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeleteAirEcsInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uninstall_client_source_types):
            request.uninstall_client_source_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uninstall_client_source_types, 'UninstallClientSourceTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.uninstall_client_source_types_shrink):
            query['UninstallClientSourceTypes'] = request.uninstall_client_source_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAirEcsInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteAirEcsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_air_ecs_instance(
        self,
        request: hbr_20170908_models.DeleteAirEcsInstanceRequest,
    ) -> hbr_20170908_models.DeleteAirEcsInstanceResponse:
        """
        @summary Removes the Elastic Compute Service (ECS) instance that is used for restoration only in ECS Backup Essential Edition.
        
        @param request: DeleteAirEcsInstanceRequest
        @return: DeleteAirEcsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_air_ecs_instance_with_options(request, runtime)

    async def delete_air_ecs_instance_async(
        self,
        request: hbr_20170908_models.DeleteAirEcsInstanceRequest,
    ) -> hbr_20170908_models.DeleteAirEcsInstanceResponse:
        """
        @summary Removes the Elastic Compute Service (ECS) instance that is used for restoration only in ECS Backup Essential Edition.
        
        @param request: DeleteAirEcsInstanceRequest
        @return: DeleteAirEcsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_air_ecs_instance_with_options_async(request, runtime)

    def delete_backup_client_with_options(
        self,
        request: hbr_20170908_models.DeleteBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupClientResponse:
        """
        @summary Deletes a Cloud Backup client.
        
        @description    You cannot delete the active Cloud Backup clients that receive heartbeat packets within 1 hour. You can call the UninstallBackupClients operation to uninstall a Cloud Backup client. Then, the client becomes inactive.
        When you perform this operation, resources that are associated with the client are also deleted, including:
        Backup plans
        Backup jobs
        Snapshots
        
        @param request: DeleteBackupClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_client_with_options_async(
        self,
        request: hbr_20170908_models.DeleteBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupClientResponse:
        """
        @summary Deletes a Cloud Backup client.
        
        @description    You cannot delete the active Cloud Backup clients that receive heartbeat packets within 1 hour. You can call the UninstallBackupClients operation to uninstall a Cloud Backup client. Then, the client becomes inactive.
        When you perform this operation, resources that are associated with the client are also deleted, including:
        Backup plans
        Backup jobs
        Snapshots
        
        @param request: DeleteBackupClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_client(
        self,
        request: hbr_20170908_models.DeleteBackupClientRequest,
    ) -> hbr_20170908_models.DeleteBackupClientResponse:
        """
        @summary Deletes a Cloud Backup client.
        
        @description    You cannot delete the active Cloud Backup clients that receive heartbeat packets within 1 hour. You can call the UninstallBackupClients operation to uninstall a Cloud Backup client. Then, the client becomes inactive.
        When you perform this operation, resources that are associated with the client are also deleted, including:
        Backup plans
        Backup jobs
        Snapshots
        
        @param request: DeleteBackupClientRequest
        @return: DeleteBackupClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_client_with_options(request, runtime)

    async def delete_backup_client_async(
        self,
        request: hbr_20170908_models.DeleteBackupClientRequest,
    ) -> hbr_20170908_models.DeleteBackupClientResponse:
        """
        @summary Deletes a Cloud Backup client.
        
        @description    You cannot delete the active Cloud Backup clients that receive heartbeat packets within 1 hour. You can call the UninstallBackupClients operation to uninstall a Cloud Backup client. Then, the client becomes inactive.
        When you perform this operation, resources that are associated with the client are also deleted, including:
        Backup plans
        Backup jobs
        Snapshots
        
        @param request: DeleteBackupClientRequest
        @return: DeleteBackupClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_client_with_options_async(request, runtime)

    def delete_backup_client_resource_with_options(
        self,
        tmp_req: hbr_20170908_models.DeleteBackupClientResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupClientResourceResponse:
        """
        @summary Deletes the resources that are related to one or more HBR clients.
        
        @description This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        
        @param tmp_req: DeleteBackupClientResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupClientResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeleteBackupClientResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClientResource',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_client_resource_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DeleteBackupClientResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupClientResourceResponse:
        """
        @summary Deletes the resources that are related to one or more HBR clients.
        
        @description This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        
        @param tmp_req: DeleteBackupClientResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupClientResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeleteBackupClientResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupClientResource',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupClientResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_client_resource(
        self,
        request: hbr_20170908_models.DeleteBackupClientResourceRequest,
    ) -> hbr_20170908_models.DeleteBackupClientResourceResponse:
        """
        @summary Deletes the resources that are related to one or more HBR clients.
        
        @description This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        
        @param request: DeleteBackupClientResourceRequest
        @return: DeleteBackupClientResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_client_resource_with_options(request, runtime)

    async def delete_backup_client_resource_async(
        self,
        request: hbr_20170908_models.DeleteBackupClientResourceRequest,
    ) -> hbr_20170908_models.DeleteBackupClientResourceResponse:
        """
        @summary Deletes the resources that are related to one or more HBR clients.
        
        @description This operation deletes only the resources that are related to HBR clients. The resources include backup plans, backup jobs, and backup snapshots. The operation does not delete HBR clients.
        
        @param request: DeleteBackupClientResourceRequest
        @return: DeleteBackupClientResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_client_resource_with_options_async(request, runtime)

    def delete_backup_plan_with_options(
        self,
        request: hbr_20170908_models.DeleteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupPlanResponse:
        """
        @summary Deletes a backup plan.
        
        @description    If you delete a backup plan, the backup jobs are also deleted.
        If you delete a backup plan, the created snapshot files are not deleted.
        
        @param request: DeleteBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.require_no_running_jobs):
            query['RequireNoRunningJobs'] = request.require_no_running_jobs
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.DeleteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteBackupPlanResponse:
        """
        @summary Deletes a backup plan.
        
        @description    If you delete a backup plan, the backup jobs are also deleted.
        If you delete a backup plan, the created snapshot files are not deleted.
        
        @param request: DeleteBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.require_no_running_jobs):
            query['RequireNoRunningJobs'] = request.require_no_running_jobs
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_plan(
        self,
        request: hbr_20170908_models.DeleteBackupPlanRequest,
    ) -> hbr_20170908_models.DeleteBackupPlanResponse:
        """
        @summary Deletes a backup plan.
        
        @description    If you delete a backup plan, the backup jobs are also deleted.
        If you delete a backup plan, the created snapshot files are not deleted.
        
        @param request: DeleteBackupPlanRequest
        @return: DeleteBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_plan_with_options(request, runtime)

    async def delete_backup_plan_async(
        self,
        request: hbr_20170908_models.DeleteBackupPlanRequest,
    ) -> hbr_20170908_models.DeleteBackupPlanResponse:
        """
        @summary Deletes a backup plan.
        
        @description    If you delete a backup plan, the backup jobs are also deleted.
        If you delete a backup plan, the created snapshot files are not deleted.
        
        @param request: DeleteBackupPlanRequest
        @return: DeleteBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_plan_with_options_async(request, runtime)

    def delete_client_with_options(
        self,
        request: hbr_20170908_models.DeleteClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteClientResponse:
        """
        @param request: DeleteClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_with_options_async(
        self,
        request: hbr_20170908_models.DeleteClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteClientResponse:
        """
        @param request: DeleteClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client(
        self,
        request: hbr_20170908_models.DeleteClientRequest,
    ) -> hbr_20170908_models.DeleteClientResponse:
        """
        @param request: DeleteClientRequest
        @return: DeleteClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_client_with_options(request, runtime)

    async def delete_client_async(
        self,
        request: hbr_20170908_models.DeleteClientRequest,
    ) -> hbr_20170908_models.DeleteClientResponse:
        """
        @param request: DeleteClientRequest
        @return: DeleteClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_with_options_async(request, runtime)

    def delete_hana_backup_plan_with_options(
        self,
        request: hbr_20170908_models.DeleteHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteHanaBackupPlanResponse:
        """
        @summary Deletes an SAP HANA backup plan.
        
        @param request: DeleteHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hana_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.DeleteHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteHanaBackupPlanResponse:
        """
        @summary Deletes an SAP HANA backup plan.
        
        @param request: DeleteHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hana_backup_plan(
        self,
        request: hbr_20170908_models.DeleteHanaBackupPlanRequest,
    ) -> hbr_20170908_models.DeleteHanaBackupPlanResponse:
        """
        @summary Deletes an SAP HANA backup plan.
        
        @param request: DeleteHanaBackupPlanRequest
        @return: DeleteHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hana_backup_plan_with_options(request, runtime)

    async def delete_hana_backup_plan_async(
        self,
        request: hbr_20170908_models.DeleteHanaBackupPlanRequest,
    ) -> hbr_20170908_models.DeleteHanaBackupPlanResponse:
        """
        @summary Deletes an SAP HANA backup plan.
        
        @param request: DeleteHanaBackupPlanRequest
        @return: DeleteHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hana_backup_plan_with_options_async(request, runtime)

    def delete_hana_instance_with_options(
        self,
        request: hbr_20170908_models.DeleteHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteHanaInstanceResponse:
        """
        @summary Deletes an SAP HANA instance.
        
        @description If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the backup data of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        
        @param request: DeleteHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hana_instance_with_options_async(
        self,
        request: hbr_20170908_models.DeleteHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteHanaInstanceResponse:
        """
        @summary Deletes an SAP HANA instance.
        
        @description If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the backup data of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        
        @param request: DeleteHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hana_instance(
        self,
        request: hbr_20170908_models.DeleteHanaInstanceRequest,
    ) -> hbr_20170908_models.DeleteHanaInstanceResponse:
        """
        @summary Deletes an SAP HANA instance.
        
        @description If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the backup data of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        
        @param request: DeleteHanaInstanceRequest
        @return: DeleteHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hana_instance_with_options(request, runtime)

    async def delete_hana_instance_async(
        self,
        request: hbr_20170908_models.DeleteHanaInstanceRequest,
    ) -> hbr_20170908_models.DeleteHanaInstanceResponse:
        """
        @summary Deletes an SAP HANA instance.
        
        @description If you delete an SAP HANA instance, the existing backup data is also deleted and the running backup and restore jobs fail to be completed. Before you delete the SAP HANA instance, make sure that you no longer need the backup data of the instance and no backup or restore jobs are running for the instance. To delete an SAP HANA instance, you must specify the security identifier (SID) of the instance. The SID is three characters in length and starts with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        
        @param request: DeleteHanaInstanceRequest
        @return: DeleteHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hana_instance_with_options_async(request, runtime)

    def delete_policy_binding_with_options(
        self,
        tmp_req: hbr_20170908_models.DeletePolicyBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeletePolicyBindingResponse:
        """
        @summary Disassociates one or more data sources from a backup policy. After you disassociate the data sources from the backup policy, the backup policy no longer protects the data sources. Proceed with caution.
        
        @param tmp_req: DeletePolicyBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyBindingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeletePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_binding_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DeletePolicyBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeletePolicyBindingResponse:
        """
        @summary Disassociates one or more data sources from a backup policy. After you disassociate the data sources from the backup policy, the backup policy no longer protects the data sources. Proceed with caution.
        
        @param tmp_req: DeletePolicyBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyBindingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DeletePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_binding(
        self,
        request: hbr_20170908_models.DeletePolicyBindingRequest,
    ) -> hbr_20170908_models.DeletePolicyBindingResponse:
        """
        @summary Disassociates one or more data sources from a backup policy. After you disassociate the data sources from the backup policy, the backup policy no longer protects the data sources. Proceed with caution.
        
        @param request: DeletePolicyBindingRequest
        @return: DeletePolicyBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_binding_with_options(request, runtime)

    async def delete_policy_binding_async(
        self,
        request: hbr_20170908_models.DeletePolicyBindingRequest,
    ) -> hbr_20170908_models.DeletePolicyBindingResponse:
        """
        @summary Disassociates one or more data sources from a backup policy. After you disassociate the data sources from the backup policy, the backup policy no longer protects the data sources. Proceed with caution.
        
        @param request: DeletePolicyBindingRequest
        @return: DeletePolicyBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_binding_with_options_async(request, runtime)

    def delete_policy_v2with_options(
        self,
        request: hbr_20170908_models.DeletePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeletePolicyV2Response:
        """
        @summary Deletes a backup policy.
        
        @description If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        
        @param request: DeletePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_v2with_options_async(
        self,
        request: hbr_20170908_models.DeletePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeletePolicyV2Response:
        """
        @summary Deletes a backup policy.
        
        @description If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        
        @param request: DeletePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeletePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_v2(
        self,
        request: hbr_20170908_models.DeletePolicyV2Request,
    ) -> hbr_20170908_models.DeletePolicyV2Response:
        """
        @summary Deletes a backup policy.
        
        @description If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        
        @param request: DeletePolicyV2Request
        @return: DeletePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_v2with_options(request, runtime)

    async def delete_policy_v2_async(
        self,
        request: hbr_20170908_models.DeletePolicyV2Request,
    ) -> hbr_20170908_models.DeletePolicyV2Response:
        """
        @summary Deletes a backup policy.
        
        @description If you delete a backup policy, the backup policy is disassociated with all data sources. Proceed with caution.
        
        @param request: DeletePolicyV2Request
        @return: DeletePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_v2with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: hbr_20170908_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteSnapshotResponse:
        """
        @summary Deletes a backup snapshot.
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: hbr_20170908_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteSnapshotResponse:
        """
        @summary Deletes a backup snapshot.
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: hbr_20170908_models.DeleteSnapshotRequest,
    ) -> hbr_20170908_models.DeleteSnapshotResponse:
        """
        @summary Deletes a backup snapshot.
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: hbr_20170908_models.DeleteSnapshotRequest,
    ) -> hbr_20170908_models.DeleteSnapshotResponse:
        """
        @summary Deletes a backup snapshot.
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_udm_disk_with_options(
        self,
        request: hbr_20170908_models.DeleteUdmDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteUdmDiskResponse:
        """
        @summary Cancels a protected disk.
        
        @param request: DeleteUdmDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdmDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdmDisk',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteUdmDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udm_disk_with_options_async(
        self,
        request: hbr_20170908_models.DeleteUdmDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteUdmDiskResponse:
        """
        @summary Cancels a protected disk.
        
        @param request: DeleteUdmDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdmDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdmDisk',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteUdmDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udm_disk(
        self,
        request: hbr_20170908_models.DeleteUdmDiskRequest,
    ) -> hbr_20170908_models.DeleteUdmDiskResponse:
        """
        @summary Cancels a protected disk.
        
        @param request: DeleteUdmDiskRequest
        @return: DeleteUdmDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_udm_disk_with_options(request, runtime)

    async def delete_udm_disk_async(
        self,
        request: hbr_20170908_models.DeleteUdmDiskRequest,
    ) -> hbr_20170908_models.DeleteUdmDiskResponse:
        """
        @summary Cancels a protected disk.
        
        @param request: DeleteUdmDiskRequest
        @return: DeleteUdmDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_udm_disk_with_options_async(request, runtime)

    def delete_udm_ecs_instance_with_options(
        self,
        request: hbr_20170908_models.DeleteUdmEcsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteUdmEcsInstanceResponse:
        """
        @summary Stops protection for Elastic Compute Service (ECS) instance backup.
        
        @param request: DeleteUdmEcsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdmEcsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdmEcsInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteUdmEcsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udm_ecs_instance_with_options_async(
        self,
        request: hbr_20170908_models.DeleteUdmEcsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteUdmEcsInstanceResponse:
        """
        @summary Stops protection for Elastic Compute Service (ECS) instance backup.
        
        @param request: DeleteUdmEcsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdmEcsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdmEcsInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteUdmEcsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udm_ecs_instance(
        self,
        request: hbr_20170908_models.DeleteUdmEcsInstanceRequest,
    ) -> hbr_20170908_models.DeleteUdmEcsInstanceResponse:
        """
        @summary Stops protection for Elastic Compute Service (ECS) instance backup.
        
        @param request: DeleteUdmEcsInstanceRequest
        @return: DeleteUdmEcsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_udm_ecs_instance_with_options(request, runtime)

    async def delete_udm_ecs_instance_async(
        self,
        request: hbr_20170908_models.DeleteUdmEcsInstanceRequest,
    ) -> hbr_20170908_models.DeleteUdmEcsInstanceResponse:
        """
        @summary Stops protection for Elastic Compute Service (ECS) instance backup.
        
        @param request: DeleteUdmEcsInstanceRequest
        @return: DeleteUdmEcsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_udm_ecs_instance_with_options_async(request, runtime)

    def delete_vault_with_options(
        self,
        request: hbr_20170908_models.DeleteVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteVaultResponse:
        """
        @summary Deletes a backup vault.
        
        @description    You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include the Cloud Backup client of the old version, backup plans, backup jobs, snapshots, and restore jobs.
        
        @param request: DeleteVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vault_with_options_async(
        self,
        request: hbr_20170908_models.DeleteVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DeleteVaultResponse:
        """
        @summary Deletes a backup vault.
        
        @description    You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include the Cloud Backup client of the old version, backup plans, backup jobs, snapshots, and restore jobs.
        
        @param request: DeleteVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DeleteVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vault(
        self,
        request: hbr_20170908_models.DeleteVaultRequest,
    ) -> hbr_20170908_models.DeleteVaultResponse:
        """
        @summary Deletes a backup vault.
        
        @description    You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include the Cloud Backup client of the old version, backup plans, backup jobs, snapshots, and restore jobs.
        
        @param request: DeleteVaultRequest
        @return: DeleteVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vault_with_options(request, runtime)

    async def delete_vault_async(
        self,
        request: hbr_20170908_models.DeleteVaultRequest,
    ) -> hbr_20170908_models.DeleteVaultResponse:
        """
        @summary Deletes a backup vault.
        
        @description    You cannot delete a backup vault within 2 hours after the backup vault is created or a backup vault that is in the INITIALIZING state.
        After you delete a backup vault, all resources that are associated with the backup vault are deleted. The resources include the Cloud Backup client of the old version, backup plans, backup jobs, snapshots, and restore jobs.
        
        @param request: DeleteVaultRequest
        @return: DeleteVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vault_with_options_async(request, runtime)

    def describe_backup_clients_with_options(
        self,
        tmp_req: hbr_20170908_models.DescribeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupClientsResponse:
        """
        @summary Queries the information about one or more HBR clients that meet the specified conditions.
        
        @param tmp_req: DescribeBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            body['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_clients_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DescribeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupClientsResponse:
        """
        @summary Queries the information about one or more HBR clients that meet the specified conditions.
        
        @param tmp_req: DescribeBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            body['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_clients(
        self,
        request: hbr_20170908_models.DescribeBackupClientsRequest,
    ) -> hbr_20170908_models.DescribeBackupClientsResponse:
        """
        @summary Queries the information about one or more HBR clients that meet the specified conditions.
        
        @param request: DescribeBackupClientsRequest
        @return: DescribeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    async def describe_backup_clients_async(
        self,
        request: hbr_20170908_models.DescribeBackupClientsRequest,
    ) -> hbr_20170908_models.DescribeBackupClientsResponse:
        """
        @summary Queries the information about one or more HBR clients that meet the specified conditions.
        
        @param request: DescribeBackupClientsRequest
        @return: DescribeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_clients_with_options_async(request, runtime)

    def describe_backup_jobs_2with_options(
        self,
        request: hbr_20170908_models.DescribeBackupJobs2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupJobs2Response:
        """
        @summary Queries the information about one or more backup jobs that meet the specified conditions.
        
        @param request: DescribeBackupJobs2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupJobs2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupJobs2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_jobs_2with_options_async(
        self,
        request: hbr_20170908_models.DescribeBackupJobs2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupJobs2Response:
        """
        @summary Queries the information about one or more backup jobs that meet the specified conditions.
        
        @param request: DescribeBackupJobs2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupJobs2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupJobs2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_jobs_2(
        self,
        request: hbr_20170908_models.DescribeBackupJobs2Request,
    ) -> hbr_20170908_models.DescribeBackupJobs2Response:
        """
        @summary Queries the information about one or more backup jobs that meet the specified conditions.
        
        @param request: DescribeBackupJobs2Request
        @return: DescribeBackupJobs2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_jobs_2with_options(request, runtime)

    async def describe_backup_jobs_2_async(
        self,
        request: hbr_20170908_models.DescribeBackupJobs2Request,
    ) -> hbr_20170908_models.DescribeBackupJobs2Response:
        """
        @summary Queries the information about one or more backup jobs that meet the specified conditions.
        
        @param request: DescribeBackupJobs2Request
        @return: DescribeBackupJobs2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_jobs_2with_options_async(request, runtime)

    def describe_backup_plans_with_options(
        self,
        request: hbr_20170908_models.DescribeBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupPlansResponse:
        """
        @summary Queries the information about one or more backup plans that meet the specified conditions.
        
        @param request: DescribeBackupPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plans_with_options_async(
        self,
        request: hbr_20170908_models.DescribeBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeBackupPlansResponse:
        """
        @summary Queries the information about one or more backup plans that meet the specified conditions.
        
        @param request: DescribeBackupPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeBackupPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plans(
        self,
        request: hbr_20170908_models.DescribeBackupPlansRequest,
    ) -> hbr_20170908_models.DescribeBackupPlansResponse:
        """
        @summary Queries the information about one or more backup plans that meet the specified conditions.
        
        @param request: DescribeBackupPlansRequest
        @return: DescribeBackupPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plans_with_options(request, runtime)

    async def describe_backup_plans_async(
        self,
        request: hbr_20170908_models.DescribeBackupPlansRequest,
    ) -> hbr_20170908_models.DescribeBackupPlansResponse:
        """
        @summary Queries the information about one or more backup plans that meet the specified conditions.
        
        @param request: DescribeBackupPlansRequest
        @return: DescribeBackupPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plans_with_options_async(request, runtime)

    def describe_clients_with_options(
        self,
        request: hbr_20170908_models.DescribeClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeClientsResponse:
        """
        @summary Queries one or more Cloud Backup clients that meet the specified conditions.
        
        @description This operation is applicable only to SAP HANA backup. For Cloud Backup clients of other data sources, call the DescribeBackupClients operation.
        
        @param request: DescribeClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clients_with_options_async(
        self,
        request: hbr_20170908_models.DescribeClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeClientsResponse:
        """
        @summary Queries one or more Cloud Backup clients that meet the specified conditions.
        
        @description This operation is applicable only to SAP HANA backup. For Cloud Backup clients of other data sources, call the DescribeBackupClients operation.
        
        @param request: DescribeClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clients(
        self,
        request: hbr_20170908_models.DescribeClientsRequest,
    ) -> hbr_20170908_models.DescribeClientsResponse:
        """
        @summary Queries one or more Cloud Backup clients that meet the specified conditions.
        
        @description This operation is applicable only to SAP HANA backup. For Cloud Backup clients of other data sources, call the DescribeBackupClients operation.
        
        @param request: DescribeClientsRequest
        @return: DescribeClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_clients_with_options(request, runtime)

    async def describe_clients_async(
        self,
        request: hbr_20170908_models.DescribeClientsRequest,
    ) -> hbr_20170908_models.DescribeClientsResponse:
        """
        @summary Queries one or more Cloud Backup clients that meet the specified conditions.
        
        @description This operation is applicable only to SAP HANA backup. For Cloud Backup clients of other data sources, call the DescribeBackupClients operation.
        
        @param request: DescribeClientsRequest
        @return: DescribeClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_clients_with_options_async(request, runtime)

    def describe_container_cluster_with_options(
        self,
        request: hbr_20170908_models.DescribeContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeContainerClusterResponse:
        """
        @summary Queries one or more container clusters that meet the specified conditions.
        
        @description You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        
        @param request: DescribeContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_cluster_with_options_async(
        self,
        request: hbr_20170908_models.DescribeContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeContainerClusterResponse:
        """
        @summary Queries one or more container clusters that meet the specified conditions.
        
        @description You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        
        @param request: DescribeContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_cluster(
        self,
        request: hbr_20170908_models.DescribeContainerClusterRequest,
    ) -> hbr_20170908_models.DescribeContainerClusterResponse:
        """
        @summary Queries one or more container clusters that meet the specified conditions.
        
        @description You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        
        @param request: DescribeContainerClusterRequest
        @return: DescribeContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_cluster_with_options(request, runtime)

    async def describe_container_cluster_async(
        self,
        request: hbr_20170908_models.DescribeContainerClusterRequest,
    ) -> hbr_20170908_models.DescribeContainerClusterResponse:
        """
        @summary Queries one or more container clusters that meet the specified conditions.
        
        @description You can call this operation to query only Container Service for Kubernetes (ACK) clusters.
        
        @param request: DescribeContainerClusterRequest
        @return: DescribeContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_cluster_with_options_async(request, runtime)

    def describe_cross_accounts_with_options(
        self,
        request: hbr_20170908_models.DescribeCrossAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeCrossAccountsResponse:
        """
        @summary Queries the information about the accounts used in cross-account backup.
        
        @param request: DescribeCrossAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCrossAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossAccounts',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeCrossAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_accounts_with_options_async(
        self,
        request: hbr_20170908_models.DescribeCrossAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeCrossAccountsResponse:
        """
        @summary Queries the information about the accounts used in cross-account backup.
        
        @param request: DescribeCrossAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCrossAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossAccounts',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeCrossAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_accounts(
        self,
        request: hbr_20170908_models.DescribeCrossAccountsRequest,
    ) -> hbr_20170908_models.DescribeCrossAccountsResponse:
        """
        @summary Queries the information about the accounts used in cross-account backup.
        
        @param request: DescribeCrossAccountsRequest
        @return: DescribeCrossAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_accounts_with_options(request, runtime)

    async def describe_cross_accounts_async(
        self,
        request: hbr_20170908_models.DescribeCrossAccountsRequest,
    ) -> hbr_20170908_models.DescribeCrossAccountsResponse:
        """
        @summary Queries the information about the accounts used in cross-account backup.
        
        @param request: DescribeCrossAccountsRequest
        @return: DescribeCrossAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_accounts_with_options_async(request, runtime)

    def describe_hana_backup_plans_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupPlansResponse:
        """
        @summary Queries one or more SAP HANA backup plans that meet the specified conditions.
        
        @param request: DescribeHanaBackupPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backup_plans_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupPlansResponse:
        """
        @summary Queries one or more SAP HANA backup plans that meet the specified conditions.
        
        @param request: DescribeHanaBackupPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupPlans',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backup_plans(
        self,
        request: hbr_20170908_models.DescribeHanaBackupPlansRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupPlansResponse:
        """
        @summary Queries one or more SAP HANA backup plans that meet the specified conditions.
        
        @param request: DescribeHanaBackupPlansRequest
        @return: DescribeHanaBackupPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backup_plans_with_options(request, runtime)

    async def describe_hana_backup_plans_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupPlansRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupPlansResponse:
        """
        @summary Queries one or more SAP HANA backup plans that meet the specified conditions.
        
        @param request: DescribeHanaBackupPlansRequest
        @return: DescribeHanaBackupPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_backup_plans_with_options_async(request, runtime)

    def describe_hana_backup_setting_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaBackupSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupSettingResponse:
        """
        @summary Queries the backup parameters of an SAP HANA database.
        
        @description If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        
        @param request: DescribeHanaBackupSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backup_setting_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupSettingResponse:
        """
        @summary Queries the backup parameters of an SAP HANA database.
        
        @description If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        
        @param request: DescribeHanaBackupSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backup_setting(
        self,
        request: hbr_20170908_models.DescribeHanaBackupSettingRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupSettingResponse:
        """
        @summary Queries the backup parameters of an SAP HANA database.
        
        @description If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        
        @param request: DescribeHanaBackupSettingRequest
        @return: DescribeHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backup_setting_with_options(request, runtime)

    async def describe_hana_backup_setting_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupSettingRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupSettingResponse:
        """
        @summary Queries the backup parameters of an SAP HANA database.
        
        @description If you want to query the backup retention period of a database, you can call the DescribeHanaRetentionSetting operation.
        
        @param request: DescribeHanaBackupSettingRequest
        @return: DescribeHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_backup_setting_with_options_async(request, runtime)

    def describe_hana_backups_async_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaBackupsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupsAsyncResponse:
        """
        @summary Queries one or more SAP HANA backups that meet the specified conditions.
        
        @description After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the final result.
        
        @param request: DescribeHanaBackupsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupsAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.include_differential):
            query['IncludeDifferential'] = request.include_differential
        if not UtilClient.is_unset(request.include_incremental):
            query['IncludeIncremental'] = request.include_incremental
        if not UtilClient.is_unset(request.include_log):
            query['IncludeLog'] = request.include_log
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_backint):
            query['UseBackint'] = request.use_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupsAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backups_async_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupsAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaBackupsAsyncResponse:
        """
        @summary Queries one or more SAP HANA backups that meet the specified conditions.
        
        @description After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the final result.
        
        @param request: DescribeHanaBackupsAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaBackupsAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.include_differential):
            query['IncludeDifferential'] = request.include_differential
        if not UtilClient.is_unset(request.include_incremental):
            query['IncludeIncremental'] = request.include_incremental
        if not UtilClient.is_unset(request.include_log):
            query['IncludeLog'] = request.include_log
        if not UtilClient.is_unset(request.log_position):
            query['LogPosition'] = request.log_position
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not UtilClient.is_unset(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not UtilClient.is_unset(request.use_backint):
            query['UseBackint'] = request.use_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaBackupsAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaBackupsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backups_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupsAsyncRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupsAsyncResponse:
        """
        @summary Queries one or more SAP HANA backups that meet the specified conditions.
        
        @description After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the final result.
        
        @param request: DescribeHanaBackupsAsyncRequest
        @return: DescribeHanaBackupsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_backups_async_with_options(request, runtime)

    async def describe_hana_backups_async_async(
        self,
        request: hbr_20170908_models.DescribeHanaBackupsAsyncRequest,
    ) -> hbr_20170908_models.DescribeHanaBackupsAsyncResponse:
        """
        @summary Queries one or more SAP HANA backups that meet the specified conditions.
        
        @description After you call the DescribeHanaBackupsAsync operation to query the SAP HANA backups that meet the specified conditions, call the DescribeTask operation to query the final result.
        
        @param request: DescribeHanaBackupsAsyncRequest
        @return: DescribeHanaBackupsAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_backups_async_with_options_async(request, runtime)

    def describe_hana_databases_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaDatabasesResponse:
        """
        @summary Queries the information about SAP HANA databases.
        
        @description After you register an SAP HANA instance and install a Cloud Backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        
        @param request: DescribeHanaDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaDatabases',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_databases_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaDatabasesResponse:
        """
        @summary Queries the information about SAP HANA databases.
        
        @description After you register an SAP HANA instance and install a Cloud Backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        
        @param request: DescribeHanaDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaDatabases',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_databases(
        self,
        request: hbr_20170908_models.DescribeHanaDatabasesRequest,
    ) -> hbr_20170908_models.DescribeHanaDatabasesResponse:
        """
        @summary Queries the information about SAP HANA databases.
        
        @description After you register an SAP HANA instance and install a Cloud Backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        
        @param request: DescribeHanaDatabasesRequest
        @return: DescribeHanaDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_databases_with_options(request, runtime)

    async def describe_hana_databases_async(
        self,
        request: hbr_20170908_models.DescribeHanaDatabasesRequest,
    ) -> hbr_20170908_models.DescribeHanaDatabasesResponse:
        """
        @summary Queries the information about SAP HANA databases.
        
        @description After you register an SAP HANA instance and install a Cloud Backup client on the instance, you can call this operation to query the information about SAP HANA databases. You can call the StartHanaDatabaseAsync operation to start a database and call the StopHanaDatabaseAsync operation to stop a database.
        
        @param request: DescribeHanaDatabasesRequest
        @return: DescribeHanaDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_databases_with_options_async(request, runtime)

    def describe_hana_instances_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaInstancesResponse:
        """
        @summary Queries one or more SAP HANA instances that meet the specified conditions.
        
        @param request: DescribeHanaInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHanaInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_instances_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaInstancesResponse:
        """
        @summary Queries one or more SAP HANA instances that meet the specified conditions.
        
        @param request: DescribeHanaInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHanaInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_instances(
        self,
        request: hbr_20170908_models.DescribeHanaInstancesRequest,
    ) -> hbr_20170908_models.DescribeHanaInstancesResponse:
        """
        @summary Queries one or more SAP HANA instances that meet the specified conditions.
        
        @param request: DescribeHanaInstancesRequest
        @return: DescribeHanaInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_instances_with_options(request, runtime)

    async def describe_hana_instances_async(
        self,
        request: hbr_20170908_models.DescribeHanaInstancesRequest,
    ) -> hbr_20170908_models.DescribeHanaInstancesResponse:
        """
        @summary Queries one or more SAP HANA instances that meet the specified conditions.
        
        @param request: DescribeHanaInstancesRequest
        @return: DescribeHanaInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_instances_with_options_async(request, runtime)

    def describe_hana_restores_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaRestoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaRestoresResponse:
        """
        @summary Queries one or more SAP HANA restore jobs that meet the specified conditions.
        
        @param request: DescribeHanaRestoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaRestoresResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.restore_status):
            query['RestoreStatus'] = request.restore_status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRestores',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRestoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_restores_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaRestoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaRestoresResponse:
        """
        @summary Queries one or more SAP HANA restore jobs that meet the specified conditions.
        
        @param request: DescribeHanaRestoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaRestoresResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not UtilClient.is_unset(request.restore_status):
            query['RestoreStatus'] = request.restore_status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRestores',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRestoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_restores(
        self,
        request: hbr_20170908_models.DescribeHanaRestoresRequest,
    ) -> hbr_20170908_models.DescribeHanaRestoresResponse:
        """
        @summary Queries one or more SAP HANA restore jobs that meet the specified conditions.
        
        @param request: DescribeHanaRestoresRequest
        @return: DescribeHanaRestoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_restores_with_options(request, runtime)

    async def describe_hana_restores_async(
        self,
        request: hbr_20170908_models.DescribeHanaRestoresRequest,
    ) -> hbr_20170908_models.DescribeHanaRestoresResponse:
        """
        @summary Queries one or more SAP HANA restore jobs that meet the specified conditions.
        
        @param request: DescribeHanaRestoresRequest
        @return: DescribeHanaRestoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_restores_with_options_async(request, runtime)

    def describe_hana_retention_setting_with_options(
        self,
        request: hbr_20170908_models.DescribeHanaRetentionSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaRetentionSettingResponse:
        """
        @summary Queries the backup retention period of an SAP HANA database.
        
        @description    If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: DescribeHanaRetentionSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_retention_setting_with_options_async(
        self,
        request: hbr_20170908_models.DescribeHanaRetentionSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeHanaRetentionSettingResponse:
        """
        @summary Queries the backup retention period of an SAP HANA database.
        
        @description    If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: DescribeHanaRetentionSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeHanaRetentionSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_retention_setting(
        self,
        request: hbr_20170908_models.DescribeHanaRetentionSettingRequest,
    ) -> hbr_20170908_models.DescribeHanaRetentionSettingResponse:
        """
        @summary Queries the backup retention period of an SAP HANA database.
        
        @description    If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: DescribeHanaRetentionSettingRequest
        @return: DescribeHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hana_retention_setting_with_options(request, runtime)

    async def describe_hana_retention_setting_async(
        self,
        request: hbr_20170908_models.DescribeHanaRetentionSettingRequest,
    ) -> hbr_20170908_models.DescribeHanaRetentionSettingResponse:
        """
        @summary Queries the backup retention period of an SAP HANA database.
        
        @description    If you want to query the backup parameters of a database, you can call the DescribeHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: DescribeHanaRetentionSettingRequest
        @return: DescribeHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hana_retention_setting_with_options_async(request, runtime)

    def describe_ots_table_snapshots_with_options(
        self,
        request: hbr_20170908_models.DescribeOtsTableSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeOtsTableSnapshotsResponse:
        """
        @summary Queries the details about Tablestore instances that are backed up.
        
        @param request: DescribeOtsTableSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOtsTableSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not UtilClient.is_unset(request.ots_instances):
            body_flat['OtsInstances'] = request.ots_instances
        if not UtilClient.is_unset(request.snapshot_ids):
            body_flat['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOtsTableSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeOtsTableSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ots_table_snapshots_with_options_async(
        self,
        request: hbr_20170908_models.DescribeOtsTableSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeOtsTableSnapshotsResponse:
        """
        @summary Queries the details about Tablestore instances that are backed up.
        
        @param request: DescribeOtsTableSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOtsTableSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not UtilClient.is_unset(request.ots_instances):
            body_flat['OtsInstances'] = request.ots_instances
        if not UtilClient.is_unset(request.snapshot_ids):
            body_flat['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOtsTableSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeOtsTableSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ots_table_snapshots(
        self,
        request: hbr_20170908_models.DescribeOtsTableSnapshotsRequest,
    ) -> hbr_20170908_models.DescribeOtsTableSnapshotsResponse:
        """
        @summary Queries the details about Tablestore instances that are backed up.
        
        @param request: DescribeOtsTableSnapshotsRequest
        @return: DescribeOtsTableSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ots_table_snapshots_with_options(request, runtime)

    async def describe_ots_table_snapshots_async(
        self,
        request: hbr_20170908_models.DescribeOtsTableSnapshotsRequest,
    ) -> hbr_20170908_models.DescribeOtsTableSnapshotsResponse:
        """
        @summary Queries the details about Tablestore instances that are backed up.
        
        @param request: DescribeOtsTableSnapshotsRequest
        @return: DescribeOtsTableSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ots_table_snapshots_with_options_async(request, runtime)

    def describe_policies_v2with_options(
        self,
        request: hbr_20170908_models.DescribePoliciesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribePoliciesV2Response:
        """
        @summary Queries one or more backup policies.
        
        @param request: DescribePoliciesV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePoliciesV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePoliciesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_policies_v2with_options_async(
        self,
        request: hbr_20170908_models.DescribePoliciesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribePoliciesV2Response:
        """
        @summary Queries one or more backup policies.
        
        @param request: DescribePoliciesV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesV2Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePoliciesV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePoliciesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policies_v2(
        self,
        request: hbr_20170908_models.DescribePoliciesV2Request,
    ) -> hbr_20170908_models.DescribePoliciesV2Response:
        """
        @summary Queries one or more backup policies.
        
        @param request: DescribePoliciesV2Request
        @return: DescribePoliciesV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policies_v2with_options(request, runtime)

    async def describe_policies_v2_async(
        self,
        request: hbr_20170908_models.DescribePoliciesV2Request,
    ) -> hbr_20170908_models.DescribePoliciesV2Response:
        """
        @summary Queries one or more backup policies.
        
        @param request: DescribePoliciesV2Request
        @return: DescribePoliciesV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policies_v2with_options_async(request, runtime)

    def describe_policy_bindings_with_options(
        self,
        tmp_req: hbr_20170908_models.DescribePolicyBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribePolicyBindingsResponse:
        """
        @summary Query one or more data sources bound to a policy, or query one or more policies bound to a data source.
        
        @param tmp_req: DescribePolicyBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyBindingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_bindings_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DescribePolicyBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribePolicyBindingsResponse:
        """
        @summary Query one or more data sources bound to a policy, or query one or more policies bound to a data source.
        
        @param tmp_req: DescribePolicyBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyBindingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribePolicyBindingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_ids):
            request.data_source_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePolicyBindings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribePolicyBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_bindings(
        self,
        request: hbr_20170908_models.DescribePolicyBindingsRequest,
    ) -> hbr_20170908_models.DescribePolicyBindingsResponse:
        """
        @summary Query one or more data sources bound to a policy, or query one or more policies bound to a data source.
        
        @param request: DescribePolicyBindingsRequest
        @return: DescribePolicyBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_bindings_with_options(request, runtime)

    async def describe_policy_bindings_async(
        self,
        request: hbr_20170908_models.DescribePolicyBindingsRequest,
    ) -> hbr_20170908_models.DescribePolicyBindingsResponse:
        """
        @summary Query one or more data sources bound to a policy, or query one or more policies bound to a data source.
        
        @param request: DescribePolicyBindingsRequest
        @return: DescribePolicyBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_bindings_with_options_async(request, runtime)

    def describe_recoverable_ots_instances_with_options(
        self,
        request: hbr_20170908_models.DescribeRecoverableOtsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRecoverableOtsInstancesResponse:
        """
        @summary Queries the tables of a restorable Tablestore instance.
        
        @param request: DescribeRecoverableOtsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecoverableOtsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoverableOtsInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRecoverableOtsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recoverable_ots_instances_with_options_async(
        self,
        request: hbr_20170908_models.DescribeRecoverableOtsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRecoverableOtsInstancesResponse:
        """
        @summary Queries the tables of a restorable Tablestore instance.
        
        @param request: DescribeRecoverableOtsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecoverableOtsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoverableOtsInstances',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRecoverableOtsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recoverable_ots_instances(
        self,
        request: hbr_20170908_models.DescribeRecoverableOtsInstancesRequest,
    ) -> hbr_20170908_models.DescribeRecoverableOtsInstancesResponse:
        """
        @summary Queries the tables of a restorable Tablestore instance.
        
        @param request: DescribeRecoverableOtsInstancesRequest
        @return: DescribeRecoverableOtsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recoverable_ots_instances_with_options(request, runtime)

    async def describe_recoverable_ots_instances_async(
        self,
        request: hbr_20170908_models.DescribeRecoverableOtsInstancesRequest,
    ) -> hbr_20170908_models.DescribeRecoverableOtsInstancesResponse:
        """
        @summary Queries the tables of a restorable Tablestore instance.
        
        @param request: DescribeRecoverableOtsInstancesRequest
        @return: DescribeRecoverableOtsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_recoverable_ots_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> hbr_20170908_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> hbr_20170908_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_restore_jobs_2with_options(
        self,
        request: hbr_20170908_models.DescribeRestoreJobs2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRestoreJobs2Response:
        """
        @summary Queries one or more restore jobs that meet the specified conditions.
        
        @param request: DescribeRestoreJobs2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreJobs2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRestoreJobs2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_jobs_2with_options_async(
        self,
        request: hbr_20170908_models.DescribeRestoreJobs2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeRestoreJobs2Response:
        """
        @summary Queries one or more restore jobs that meet the specified conditions.
        
        @param request: DescribeRestoreJobs2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreJobs2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeRestoreJobs2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_jobs_2(
        self,
        request: hbr_20170908_models.DescribeRestoreJobs2Request,
    ) -> hbr_20170908_models.DescribeRestoreJobs2Response:
        """
        @summary Queries one or more restore jobs that meet the specified conditions.
        
        @param request: DescribeRestoreJobs2Request
        @return: DescribeRestoreJobs2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_jobs_2with_options(request, runtime)

    async def describe_restore_jobs_2_async(
        self,
        request: hbr_20170908_models.DescribeRestoreJobs2Request,
    ) -> hbr_20170908_models.DescribeRestoreJobs2Response:
        """
        @summary Queries one or more restore jobs that meet the specified conditions.
        
        @param request: DescribeRestoreJobs2Request
        @return: DescribeRestoreJobs2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_jobs_2with_options_async(request, runtime)

    def describe_task_with_options(
        self,
        request: hbr_20170908_models.DescribeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeTaskResponse:
        """
        @summary Queries an asynchronous job.
        
        @param request: DescribeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        request: hbr_20170908_models.DescribeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeTaskResponse:
        """
        @summary Queries an asynchronous job.
        
        @param request: DescribeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        request: hbr_20170908_models.DescribeTaskRequest,
    ) -> hbr_20170908_models.DescribeTaskResponse:
        """
        @summary Queries an asynchronous job.
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    async def describe_task_async(
        self,
        request: hbr_20170908_models.DescribeTaskRequest,
    ) -> hbr_20170908_models.DescribeTaskResponse:
        """
        @summary Queries an asynchronous job.
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_with_options_async(request, runtime)

    def describe_udm_snapshots_with_options(
        self,
        tmp_req: hbr_20170908_models.DescribeUdmSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeUdmSnapshotsResponse:
        """
        @summary Queries the backup snapshots of an Elastic Compute Service (ECS) instance.
        
        @param tmp_req: DescribeUdmSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUdmSnapshotsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeUdmSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_ids):
            request.snapshot_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_ids, 'SnapshotIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        body = {}
        if not UtilClient.is_unset(request.snapshot_ids_shrink):
            body['SnapshotIds'] = request.snapshot_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUdmSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeUdmSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_udm_snapshots_with_options_async(
        self,
        tmp_req: hbr_20170908_models.DescribeUdmSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeUdmSnapshotsResponse:
        """
        @summary Queries the backup snapshots of an Elastic Compute Service (ECS) instance.
        
        @param tmp_req: DescribeUdmSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUdmSnapshotsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.DescribeUdmSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_ids):
            request.snapshot_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_ids, 'SnapshotIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        body = {}
        if not UtilClient.is_unset(request.snapshot_ids_shrink):
            body['SnapshotIds'] = request.snapshot_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUdmSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeUdmSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_udm_snapshots(
        self,
        request: hbr_20170908_models.DescribeUdmSnapshotsRequest,
    ) -> hbr_20170908_models.DescribeUdmSnapshotsResponse:
        """
        @summary Queries the backup snapshots of an Elastic Compute Service (ECS) instance.
        
        @param request: DescribeUdmSnapshotsRequest
        @return: DescribeUdmSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_udm_snapshots_with_options(request, runtime)

    async def describe_udm_snapshots_async(
        self,
        request: hbr_20170908_models.DescribeUdmSnapshotsRequest,
    ) -> hbr_20170908_models.DescribeUdmSnapshotsResponse:
        """
        @summary Queries the backup snapshots of an Elastic Compute Service (ECS) instance.
        
        @param request: DescribeUdmSnapshotsRequest
        @return: DescribeUdmSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_udm_snapshots_with_options_async(request, runtime)

    def describe_vault_replication_regions_with_options(
        self,
        request: hbr_20170908_models.DescribeVaultReplicationRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeVaultReplicationRegionsResponse:
        """
        @summary Queries the regions that support cross-region replication.
        
        @param request: DescribeVaultReplicationRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVaultReplicationRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVaultReplicationRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultReplicationRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vault_replication_regions_with_options_async(
        self,
        request: hbr_20170908_models.DescribeVaultReplicationRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeVaultReplicationRegionsResponse:
        """
        @summary Queries the regions that support cross-region replication.
        
        @param request: DescribeVaultReplicationRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVaultReplicationRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVaultReplicationRegions',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultReplicationRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vault_replication_regions(
        self,
        request: hbr_20170908_models.DescribeVaultReplicationRegionsRequest,
    ) -> hbr_20170908_models.DescribeVaultReplicationRegionsResponse:
        """
        @summary Queries the regions that support cross-region replication.
        
        @param request: DescribeVaultReplicationRegionsRequest
        @return: DescribeVaultReplicationRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vault_replication_regions_with_options(request, runtime)

    async def describe_vault_replication_regions_async(
        self,
        request: hbr_20170908_models.DescribeVaultReplicationRegionsRequest,
    ) -> hbr_20170908_models.DescribeVaultReplicationRegionsResponse:
        """
        @summary Queries the regions that support cross-region replication.
        
        @param request: DescribeVaultReplicationRegionsRequest
        @return: DescribeVaultReplicationRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vault_replication_regions_with_options_async(request, runtime)

    def describe_vaults_with_options(
        self,
        request: hbr_20170908_models.DescribeVaultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeVaultsResponse:
        """
        @summary Queries the information about one or more backup vaults that meet the specified conditions.
        
        @param request: DescribeVaultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVaultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVaults',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vaults_with_options_async(
        self,
        request: hbr_20170908_models.DescribeVaultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DescribeVaultsResponse:
        """
        @summary Queries the information about one or more backup vaults that meet the specified conditions.
        
        @param request: DescribeVaultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVaultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not UtilClient.is_unset(request.vault_type):
            query['VaultType'] = request.vault_type
        body = {}
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVaults',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DescribeVaultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vaults(
        self,
        request: hbr_20170908_models.DescribeVaultsRequest,
    ) -> hbr_20170908_models.DescribeVaultsResponse:
        """
        @summary Queries the information about one or more backup vaults that meet the specified conditions.
        
        @param request: DescribeVaultsRequest
        @return: DescribeVaultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vaults_with_options(request, runtime)

    async def describe_vaults_async(
        self,
        request: hbr_20170908_models.DescribeVaultsRequest,
    ) -> hbr_20170908_models.DescribeVaultsResponse:
        """
        @summary Queries the information about one or more backup vaults that meet the specified conditions.
        
        @param request: DescribeVaultsRequest
        @return: DescribeVaultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vaults_with_options_async(request, runtime)

    def detach_nas_file_system_with_options(
        self,
        request: hbr_20170908_models.DetachNasFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DetachNasFileSystemResponse:
        """
        @summary Deletes an internal mount target created by Cloud Backup.
        
        @description    If the request is successful, the mount target is deleted.
        After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        
        @param request: DetachNasFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachNasFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachNasFileSystem',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DetachNasFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_nas_file_system_with_options_async(
        self,
        request: hbr_20170908_models.DetachNasFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DetachNasFileSystemResponse:
        """
        @summary Deletes an internal mount target created by Cloud Backup.
        
        @description    If the request is successful, the mount target is deleted.
        After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        
        @param request: DetachNasFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachNasFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachNasFileSystem',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DetachNasFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_nas_file_system(
        self,
        request: hbr_20170908_models.DetachNasFileSystemRequest,
    ) -> hbr_20170908_models.DetachNasFileSystemResponse:
        """
        @summary Deletes an internal mount target created by Cloud Backup.
        
        @description    If the request is successful, the mount target is deleted.
        After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        
        @param request: DetachNasFileSystemRequest
        @return: DetachNasFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_nas_file_system_with_options(request, runtime)

    async def detach_nas_file_system_async(
        self,
        request: hbr_20170908_models.DetachNasFileSystemRequest,
    ) -> hbr_20170908_models.DetachNasFileSystemResponse:
        """
        @summary Deletes an internal mount target created by Cloud Backup.
        
        @description    If the request is successful, the mount target is deleted.
        After you create a backup plan for an Apsara File Storage NAS file system, HBR automatically creates a mount target for the file system. You can call this operation to delete the mount target. In the **Status** column of the mount target of the NAS file system, the following information is displayed: **This mount target is created by an Alibaba Cloud internal service and cannot be operated. Service name: HBR**.
        
        @param request: DetachNasFileSystemRequest
        @return: DetachNasFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_nas_file_system_with_options_async(request, runtime)

    def disable_backup_plan_with_options(
        self,
        request: hbr_20170908_models.DisableBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DisableBackupPlanResponse:
        """
        @summary Disables a backup plan.
        
        @description After you call this operation, the backup plan is suspended. In the DescribeBackupPlans operation, the Disabled parameter is set to true.
        
        @param request: DisableBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.DisableBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DisableBackupPlanResponse:
        """
        @summary Disables a backup plan.
        
        @description After you call this operation, the backup plan is suspended. In the DescribeBackupPlans operation, the Disabled parameter is set to true.
        
        @param request: DisableBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_backup_plan(
        self,
        request: hbr_20170908_models.DisableBackupPlanRequest,
    ) -> hbr_20170908_models.DisableBackupPlanResponse:
        """
        @summary Disables a backup plan.
        
        @description After you call this operation, the backup plan is suspended. In the DescribeBackupPlans operation, the Disabled parameter is set to true.
        
        @param request: DisableBackupPlanRequest
        @return: DisableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_backup_plan_with_options(request, runtime)

    async def disable_backup_plan_async(
        self,
        request: hbr_20170908_models.DisableBackupPlanRequest,
    ) -> hbr_20170908_models.DisableBackupPlanResponse:
        """
        @summary Disables a backup plan.
        
        @description After you call this operation, the backup plan is suspended. In the DescribeBackupPlans operation, the Disabled parameter is set to true.
        
        @param request: DisableBackupPlanRequest
        @return: DisableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_backup_plan_with_options_async(request, runtime)

    def disable_hana_backup_plan_with_options(
        self,
        request: hbr_20170908_models.DisableHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DisableHanaBackupPlanResponse:
        """
        @summary Disables an SAP HANA backup plan.
        
        @description To enable the backup plan again, call the EnableHanaBackupPlan operation.
        
        @param request: DisableHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_hana_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.DisableHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.DisableHanaBackupPlanResponse:
        """
        @summary Disables an SAP HANA backup plan.
        
        @description To enable the backup plan again, call the EnableHanaBackupPlan operation.
        
        @param request: DisableHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.DisableHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_hana_backup_plan(
        self,
        request: hbr_20170908_models.DisableHanaBackupPlanRequest,
    ) -> hbr_20170908_models.DisableHanaBackupPlanResponse:
        """
        @summary Disables an SAP HANA backup plan.
        
        @description To enable the backup plan again, call the EnableHanaBackupPlan operation.
        
        @param request: DisableHanaBackupPlanRequest
        @return: DisableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_hana_backup_plan_with_options(request, runtime)

    async def disable_hana_backup_plan_async(
        self,
        request: hbr_20170908_models.DisableHanaBackupPlanRequest,
    ) -> hbr_20170908_models.DisableHanaBackupPlanResponse:
        """
        @summary Disables an SAP HANA backup plan.
        
        @description To enable the backup plan again, call the EnableHanaBackupPlan operation.
        
        @param request: DisableHanaBackupPlanRequest
        @return: DisableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_hana_backup_plan_with_options_async(request, runtime)

    def enable_backup_plan_with_options(
        self,
        request: hbr_20170908_models.EnableBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.EnableBackupPlanResponse:
        """
        @summary Enables a backup plan.
        
        @description After you call this operation, the backup plan is restarted (Disabled is set to false in the DescribeBackupPlans operation). Cloud Backup continues to perform backups based on the policy specified in the backup plan.
        
        @param request: EnableBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.EnableBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.EnableBackupPlanResponse:
        """
        @summary Enables a backup plan.
        
        @description After you call this operation, the backup plan is restarted (Disabled is set to false in the DescribeBackupPlans operation). Cloud Backup continues to perform backups based on the policy specified in the backup plan.
        
        @param request: EnableBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_backup_plan(
        self,
        request: hbr_20170908_models.EnableBackupPlanRequest,
    ) -> hbr_20170908_models.EnableBackupPlanResponse:
        """
        @summary Enables a backup plan.
        
        @description After you call this operation, the backup plan is restarted (Disabled is set to false in the DescribeBackupPlans operation). Cloud Backup continues to perform backups based on the policy specified in the backup plan.
        
        @param request: EnableBackupPlanRequest
        @return: EnableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_plan_with_options(request, runtime)

    async def enable_backup_plan_async(
        self,
        request: hbr_20170908_models.EnableBackupPlanRequest,
    ) -> hbr_20170908_models.EnableBackupPlanResponse:
        """
        @summary Enables a backup plan.
        
        @description After you call this operation, the backup plan is restarted (Disabled is set to false in the DescribeBackupPlans operation). Cloud Backup continues to perform backups based on the policy specified in the backup plan.
        
        @param request: EnableBackupPlanRequest
        @return: EnableBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_backup_plan_with_options_async(request, runtime)

    def enable_hana_backup_plan_with_options(
        self,
        request: hbr_20170908_models.EnableHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.EnableHanaBackupPlanResponse:
        """
        @summary Enables an SAP HANA backup plan.
        
        @description To disable the backup plan again, call the DisableHanaBackupPlan operation.
        
        @param request: EnableHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hana_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.EnableHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.EnableHanaBackupPlanResponse:
        """
        @summary Enables an SAP HANA backup plan.
        
        @description To disable the backup plan again, call the DisableHanaBackupPlan operation.
        
        @param request: EnableHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.EnableHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hana_backup_plan(
        self,
        request: hbr_20170908_models.EnableHanaBackupPlanRequest,
    ) -> hbr_20170908_models.EnableHanaBackupPlanResponse:
        """
        @summary Enables an SAP HANA backup plan.
        
        @description To disable the backup plan again, call the DisableHanaBackupPlan operation.
        
        @param request: EnableHanaBackupPlanRequest
        @return: EnableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_hana_backup_plan_with_options(request, runtime)

    async def enable_hana_backup_plan_async(
        self,
        request: hbr_20170908_models.EnableHanaBackupPlanRequest,
    ) -> hbr_20170908_models.EnableHanaBackupPlanResponse:
        """
        @summary Enables an SAP HANA backup plan.
        
        @description To disable the backup plan again, call the DisableHanaBackupPlan operation.
        
        @param request: EnableHanaBackupPlanRequest
        @return: EnableHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_hana_backup_plan_with_options_async(request, runtime)

    def execute_backup_plan_with_options(
        self,
        request: hbr_20170908_models.ExecuteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ExecuteBackupPlanResponse:
        """
        @summary Executes a backup plan.
        
        @param request: ExecuteBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecuteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.ExecuteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ExecuteBackupPlanResponse:
        """
        @summary Executes a backup plan.
        
        @param request: ExecuteBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecuteBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_backup_plan(
        self,
        request: hbr_20170908_models.ExecuteBackupPlanRequest,
    ) -> hbr_20170908_models.ExecuteBackupPlanResponse:
        """
        @summary Executes a backup plan.
        
        @param request: ExecuteBackupPlanRequest
        @return: ExecuteBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_backup_plan_with_options(request, runtime)

    async def execute_backup_plan_async(
        self,
        request: hbr_20170908_models.ExecuteBackupPlanRequest,
    ) -> hbr_20170908_models.ExecuteBackupPlanResponse:
        """
        @summary Executes a backup plan.
        
        @param request: ExecuteBackupPlanRequest
        @return: ExecuteBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_backup_plan_with_options_async(request, runtime)

    def execute_policy_v2with_options(
        self,
        request: hbr_20170908_models.ExecutePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ExecutePolicyV2Response:
        """
        @summary Execute a policy for one or all bound data sources.
        
        @param request: ExecutePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecutePolicyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecutePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecutePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def execute_policy_v2with_options_async(
        self,
        request: hbr_20170908_models.ExecutePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.ExecutePolicyV2Response:
        """
        @summary Execute a policy for one or all bound data sources.
        
        @param request: ExecutePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecutePolicyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecutePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.ExecutePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_policy_v2(
        self,
        request: hbr_20170908_models.ExecutePolicyV2Request,
    ) -> hbr_20170908_models.ExecutePolicyV2Response:
        """
        @summary Execute a policy for one or all bound data sources.
        
        @param request: ExecutePolicyV2Request
        @return: ExecutePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_policy_v2with_options(request, runtime)

    async def execute_policy_v2_async(
        self,
        request: hbr_20170908_models.ExecutePolicyV2Request,
    ) -> hbr_20170908_models.ExecutePolicyV2Response:
        """
        @summary Execute a policy for one or all bound data sources.
        
        @param request: ExecutePolicyV2Request
        @return: ExecutePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_policy_v2with_options_async(request, runtime)

    def generate_ram_policy_with_options(
        self,
        request: hbr_20170908_models.GenerateRamPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.GenerateRamPolicyResponse:
        """
        @summary Generates a Resource Access Management (RAM) policy.
        
        @param request: GenerateRamPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateRamPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.require_base_policy):
            query['RequireBasePolicy'] = request.require_base_policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateRamPolicy',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GenerateRamPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_ram_policy_with_options_async(
        self,
        request: hbr_20170908_models.GenerateRamPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.GenerateRamPolicyResponse:
        """
        @summary Generates a Resource Access Management (RAM) policy.
        
        @param request: GenerateRamPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateRamPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.require_base_policy):
            query['RequireBasePolicy'] = request.require_base_policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateRamPolicy',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GenerateRamPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_ram_policy(
        self,
        request: hbr_20170908_models.GenerateRamPolicyRequest,
    ) -> hbr_20170908_models.GenerateRamPolicyResponse:
        """
        @summary Generates a Resource Access Management (RAM) policy.
        
        @param request: GenerateRamPolicyRequest
        @return: GenerateRamPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_ram_policy_with_options(request, runtime)

    async def generate_ram_policy_async(
        self,
        request: hbr_20170908_models.GenerateRamPolicyRequest,
    ) -> hbr_20170908_models.GenerateRamPolicyResponse:
        """
        @summary Generates a Resource Access Management (RAM) policy.
        
        @param request: GenerateRamPolicyRequest
        @return: GenerateRamPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_ram_policy_with_options_async(request, runtime)

    def get_temp_file_download_link_with_options(
        self,
        request: hbr_20170908_models.GetTempFileDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.GetTempFileDownloadLinkResponse:
        """
        @summary Obtains download links of files such as job reports.
        
        @param request: GetTempFileDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTempFileDownloadLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.temp_file_key):
            query['TempFileKey'] = request.temp_file_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTempFileDownloadLink',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GetTempFileDownloadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_temp_file_download_link_with_options_async(
        self,
        request: hbr_20170908_models.GetTempFileDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.GetTempFileDownloadLinkResponse:
        """
        @summary Obtains download links of files such as job reports.
        
        @param request: GetTempFileDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTempFileDownloadLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.temp_file_key):
            query['TempFileKey'] = request.temp_file_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTempFileDownloadLink',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.GetTempFileDownloadLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_temp_file_download_link(
        self,
        request: hbr_20170908_models.GetTempFileDownloadLinkRequest,
    ) -> hbr_20170908_models.GetTempFileDownloadLinkResponse:
        """
        @summary Obtains download links of files such as job reports.
        
        @param request: GetTempFileDownloadLinkRequest
        @return: GetTempFileDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_temp_file_download_link_with_options(request, runtime)

    async def get_temp_file_download_link_async(
        self,
        request: hbr_20170908_models.GetTempFileDownloadLinkRequest,
    ) -> hbr_20170908_models.GetTempFileDownloadLinkResponse:
        """
        @summary Obtains download links of files such as job reports.
        
        @param request: GetTempFileDownloadLinkRequest
        @return: GetTempFileDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_temp_file_download_link_with_options_async(request, runtime)

    def install_backup_clients_with_options(
        self,
        tmp_req: hbr_20170908_models.InstallBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.InstallBackupClientsResponse:
        """
        @summary Installs an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        You can call the [DescribeTask](https://help.aliyun.com/document_detail/431265.html) operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        
        @param tmp_req: InstallBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.InstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.InstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_backup_clients_with_options_async(
        self,
        tmp_req: hbr_20170908_models.InstallBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.InstallBackupClientsResponse:
        """
        @summary Installs an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        You can call the [DescribeTask](https://help.aliyun.com/document_detail/431265.html) operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        
        @param tmp_req: InstallBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.InstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.InstallBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_backup_clients(
        self,
        request: hbr_20170908_models.InstallBackupClientsRequest,
    ) -> hbr_20170908_models.InstallBackupClientsResponse:
        """
        @summary Installs an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        You can call the [DescribeTask](https://help.aliyun.com/document_detail/431265.html) operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        
        @param request: InstallBackupClientsRequest
        @return: InstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_backup_clients_with_options(request, runtime)

    async def install_backup_clients_async(
        self,
        request: hbr_20170908_models.InstallBackupClientsRequest,
    ) -> hbr_20170908_models.InstallBackupClientsResponse:
        """
        @summary Installs an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to install an HBR client on an ECS instance.
        You can call the [DescribeTask](https://help.aliyun.com/document_detail/431265.html) operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 60 seconds after you call the InstallBackupClients operation to install HBR clients. Then, run the next queries at an interval of 30 seconds.
        
        @param request: InstallBackupClientsRequest
        @return: InstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_backup_clients_with_options_async(request, runtime)

    def open_hbr_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.OpenHbrServiceResponse:
        """
        @summary Activates Cloud Backup.
        
        @param request: OpenHbrServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenHbrServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenHbrService',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.OpenHbrServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_hbr_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.OpenHbrServiceResponse:
        """
        @summary Activates Cloud Backup.
        
        @param request: OpenHbrServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenHbrServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenHbrService',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.OpenHbrServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_hbr_service(self) -> hbr_20170908_models.OpenHbrServiceResponse:
        """
        @summary Activates Cloud Backup.
        
        @return: OpenHbrServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_hbr_service_with_options(runtime)

    async def open_hbr_service_async(self) -> hbr_20170908_models.OpenHbrServiceResponse:
        """
        @summary Activates Cloud Backup.
        
        @return: OpenHbrServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_hbr_service_with_options_async(runtime)

    def search_historical_snapshots_with_options(
        self,
        tmp_req: hbr_20170908_models.SearchHistoricalSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.SearchHistoricalSnapshotsResponse:
        """
        @summary Queries the information about one or more backup snapshots that meet the specified conditions.
        
        @param tmp_req: SearchHistoricalSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchHistoricalSnapshotsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.SearchHistoricalSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchHistoricalSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.SearchHistoricalSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_historical_snapshots_with_options_async(
        self,
        tmp_req: hbr_20170908_models.SearchHistoricalSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.SearchHistoricalSnapshotsResponse:
        """
        @summary Queries the information about one or more backup snapshots that meet the specified conditions.
        
        @param tmp_req: SearchHistoricalSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchHistoricalSnapshotsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.SearchHistoricalSnapshotsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchHistoricalSnapshots',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.SearchHistoricalSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_historical_snapshots(
        self,
        request: hbr_20170908_models.SearchHistoricalSnapshotsRequest,
    ) -> hbr_20170908_models.SearchHistoricalSnapshotsResponse:
        """
        @summary Queries the information about one or more backup snapshots that meet the specified conditions.
        
        @param request: SearchHistoricalSnapshotsRequest
        @return: SearchHistoricalSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_historical_snapshots_with_options(request, runtime)

    async def search_historical_snapshots_async(
        self,
        request: hbr_20170908_models.SearchHistoricalSnapshotsRequest,
    ) -> hbr_20170908_models.SearchHistoricalSnapshotsResponse:
        """
        @summary Queries the information about one or more backup snapshots that meet the specified conditions.
        
        @param request: SearchHistoricalSnapshotsRequest
        @return: SearchHistoricalSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_historical_snapshots_with_options_async(request, runtime)

    def start_hana_database_async_with_options(
        self,
        request: hbr_20170908_models.StartHanaDatabaseAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.StartHanaDatabaseAsyncResponse:
        """
        @summary Starts an SAP HANA database.
        
        @description To stop the database again, call the StopHanaDatabaseAsync operation.
        
        @param request: StartHanaDatabaseAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StartHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_hana_database_async_with_options_async(
        self,
        request: hbr_20170908_models.StartHanaDatabaseAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.StartHanaDatabaseAsyncResponse:
        """
        @summary Starts an SAP HANA database.
        
        @description To stop the database again, call the StopHanaDatabaseAsync operation.
        
        @param request: StartHanaDatabaseAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StartHanaDatabaseAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_hana_database_async(
        self,
        request: hbr_20170908_models.StartHanaDatabaseAsyncRequest,
    ) -> hbr_20170908_models.StartHanaDatabaseAsyncResponse:
        """
        @summary Starts an SAP HANA database.
        
        @description To stop the database again, call the StopHanaDatabaseAsync operation.
        
        @param request: StartHanaDatabaseAsyncRequest
        @return: StartHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_hana_database_async_with_options(request, runtime)

    async def start_hana_database_async_async(
        self,
        request: hbr_20170908_models.StartHanaDatabaseAsyncRequest,
    ) -> hbr_20170908_models.StartHanaDatabaseAsyncResponse:
        """
        @summary Starts an SAP HANA database.
        
        @description To stop the database again, call the StopHanaDatabaseAsync operation.
        
        @param request: StartHanaDatabaseAsyncRequest
        @return: StartHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_hana_database_async_with_options_async(request, runtime)

    def stop_hana_database_async_with_options(
        self,
        request: hbr_20170908_models.StopHanaDatabaseAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.StopHanaDatabaseAsyncResponse:
        """
        @summary Stops an SAP HANA database.
        
        @description To start the database again, call the StartHanaDatabaseAsync operation.
        
        @param request: StopHanaDatabaseAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StopHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_hana_database_async_with_options_async(
        self,
        request: hbr_20170908_models.StopHanaDatabaseAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.StopHanaDatabaseAsyncResponse:
        """
        @summary Stops an SAP HANA database.
        
        @description To start the database again, call the StartHanaDatabaseAsync operation.
        
        @param request: StopHanaDatabaseAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHanaDatabaseAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopHanaDatabaseAsync',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.StopHanaDatabaseAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_hana_database_async(
        self,
        request: hbr_20170908_models.StopHanaDatabaseAsyncRequest,
    ) -> hbr_20170908_models.StopHanaDatabaseAsyncResponse:
        """
        @summary Stops an SAP HANA database.
        
        @description To start the database again, call the StartHanaDatabaseAsync operation.
        
        @param request: StopHanaDatabaseAsyncRequest
        @return: StopHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_hana_database_async_with_options(request, runtime)

    async def stop_hana_database_async_async(
        self,
        request: hbr_20170908_models.StopHanaDatabaseAsyncRequest,
    ) -> hbr_20170908_models.StopHanaDatabaseAsyncResponse:
        """
        @summary Stops an SAP HANA database.
        
        @description To start the database again, call the StartHanaDatabaseAsync operation.
        
        @param request: StopHanaDatabaseAsyncRequest
        @return: StopHanaDatabaseAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_hana_database_async_with_options_async(request, runtime)

    def uninstall_backup_clients_with_options(
        self,
        tmp_req: hbr_20170908_models.UninstallBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UninstallBackupClientsResponse:
        """
        @summary Uninstalls a Cloud Backup client from one or more Elastic Compute Service (ECS) instance.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        
        @param tmp_req: UninstallBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UninstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_backup_clients_with_options_async(
        self,
        tmp_req: hbr_20170908_models.UninstallBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UninstallBackupClientsResponse:
        """
        @summary Uninstalls a Cloud Backup client from one or more Elastic Compute Service (ECS) instance.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        
        @param tmp_req: UninstallBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UninstallBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_backup_clients(
        self,
        request: hbr_20170908_models.UninstallBackupClientsRequest,
    ) -> hbr_20170908_models.UninstallBackupClientsResponse:
        """
        @summary Uninstalls a Cloud Backup client from one or more Elastic Compute Service (ECS) instance.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        
        @param request: UninstallBackupClientsRequest
        @return: UninstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_backup_clients_with_options(request, runtime)

    async def uninstall_backup_clients_async(
        self,
        request: hbr_20170908_models.UninstallBackupClientsRequest,
    ) -> hbr_20170908_models.UninstallBackupClientsResponse:
        """
        @summary Uninstalls a Cloud Backup client from one or more Elastic Compute Service (ECS) instance.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to uninstall a backup client from an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes. We recommend that you call the DescribeTask operation to run the first query 30 seconds after you call the UninstallBackupClients operation to uninstall backup clients. Then, run the next queries at an interval of 30 seconds.
        
        @param request: UninstallBackupClientsRequest
        @return: UninstallBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_backup_clients_with_options_async(request, runtime)

    def uninstall_client_with_options(
        self,
        request: hbr_20170908_models.UninstallClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UninstallClientResponse:
        """
        @summary Uninstalls an HBR client.
        
        @description If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        
        @param request: UninstallClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_client_with_options_async(
        self,
        request: hbr_20170908_models.UninstallClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UninstallClientResponse:
        """
        @summary Uninstalls an HBR client.
        
        @description If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        
        @param request: UninstallClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UninstallClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_client(
        self,
        request: hbr_20170908_models.UninstallClientRequest,
    ) -> hbr_20170908_models.UninstallClientResponse:
        """
        @summary Uninstalls an HBR client.
        
        @description If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        
        @param request: UninstallClientRequest
        @return: UninstallClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_client_with_options(request, runtime)

    async def uninstall_client_async(
        self,
        request: hbr_20170908_models.UninstallClientRequest,
    ) -> hbr_20170908_models.UninstallClientResponse:
        """
        @summary Uninstalls an HBR client.
        
        @description If you call this operation, the specified HBR client is uninstalled. To reinstall the HBR client, call the CreateClients operation.
        
        @param request: UninstallClientRequest
        @return: UninstallClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_client_with_options_async(request, runtime)

    def update_backup_plan_with_options(
        self,
        tmp_req: hbr_20170908_models.UpdateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateBackupPlanResponse:
        """
        @summary Updates a backup plan.
        
        @param tmp_req: UpdateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.update_paths):
            query['UpdatePaths'] = request.update_paths
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_plan_with_options_async(
        self,
        tmp_req: hbr_20170908_models.UpdateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateBackupPlanResponse:
        """
        @summary Updates a backup plan.
        
        @param tmp_req: UpdateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdateBackupPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detail):
            request.detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not UtilClient.is_unset(tmp_req.ots_detail):
            request.ots_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not UtilClient.is_unset(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not UtilClient.is_unset(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not UtilClient.is_unset(request.update_paths):
            query['UpdatePaths'] = request.update_paths
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not UtilClient.is_unset(request.exclude):
            body['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            body['Include'] = request.include
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not UtilClient.is_unset(request.rule):
            body['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_plan(
        self,
        request: hbr_20170908_models.UpdateBackupPlanRequest,
    ) -> hbr_20170908_models.UpdateBackupPlanResponse:
        """
        @summary Updates a backup plan.
        
        @param request: UpdateBackupPlanRequest
        @return: UpdateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_backup_plan_with_options(request, runtime)

    async def update_backup_plan_async(
        self,
        request: hbr_20170908_models.UpdateBackupPlanRequest,
    ) -> hbr_20170908_models.UpdateBackupPlanResponse:
        """
        @summary Updates a backup plan.
        
        @param request: UpdateBackupPlanRequest
        @return: UpdateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_backup_plan_with_options_async(request, runtime)

    def update_client_settings_with_options(
        self,
        request: hbr_20170908_models.UpdateClientSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateClientSettingsResponse:
        """
        @summary Updates the configurations of an HBR client.
        
        @description You can call this operation to update the configurations of both the old and new HBR clients.
        
        @param request: UpdateClientSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_on_partial_complete):
            query['AlertOnPartialComplete'] = request.alert_on_partial_complete
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.data_network_type):
            query['DataNetworkType'] = request.data_network_type
        if not UtilClient.is_unset(request.data_proxy_setting):
            query['DataProxySetting'] = request.data_proxy_setting
        if not UtilClient.is_unset(request.max_cpu_core):
            query['MaxCpuCore'] = request.max_cpu_core
        if not UtilClient.is_unset(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not UtilClient.is_unset(request.max_worker):
            query['MaxWorker'] = request.max_worker
        if not UtilClient.is_unset(request.proxy_host):
            query['ProxyHost'] = request.proxy_host
        if not UtilClient.is_unset(request.proxy_password):
            query['ProxyPassword'] = request.proxy_password
        if not UtilClient.is_unset(request.proxy_port):
            query['ProxyPort'] = request.proxy_port
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientSettings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateClientSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_settings_with_options_async(
        self,
        request: hbr_20170908_models.UpdateClientSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateClientSettingsResponse:
        """
        @summary Updates the configurations of an HBR client.
        
        @description You can call this operation to update the configurations of both the old and new HBR clients.
        
        @param request: UpdateClientSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_on_partial_complete):
            query['AlertOnPartialComplete'] = request.alert_on_partial_complete
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.data_network_type):
            query['DataNetworkType'] = request.data_network_type
        if not UtilClient.is_unset(request.data_proxy_setting):
            query['DataProxySetting'] = request.data_proxy_setting
        if not UtilClient.is_unset(request.max_cpu_core):
            query['MaxCpuCore'] = request.max_cpu_core
        if not UtilClient.is_unset(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not UtilClient.is_unset(request.max_worker):
            query['MaxWorker'] = request.max_worker
        if not UtilClient.is_unset(request.proxy_host):
            query['ProxyHost'] = request.proxy_host
        if not UtilClient.is_unset(request.proxy_password):
            query['ProxyPassword'] = request.proxy_password
        if not UtilClient.is_unset(request.proxy_port):
            query['ProxyPort'] = request.proxy_port
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_https):
            query['UseHttps'] = request.use_https
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientSettings',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateClientSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_settings(
        self,
        request: hbr_20170908_models.UpdateClientSettingsRequest,
    ) -> hbr_20170908_models.UpdateClientSettingsResponse:
        """
        @summary Updates the configurations of an HBR client.
        
        @description You can call this operation to update the configurations of both the old and new HBR clients.
        
        @param request: UpdateClientSettingsRequest
        @return: UpdateClientSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_client_settings_with_options(request, runtime)

    async def update_client_settings_async(
        self,
        request: hbr_20170908_models.UpdateClientSettingsRequest,
    ) -> hbr_20170908_models.UpdateClientSettingsResponse:
        """
        @summary Updates the configurations of an HBR client.
        
        @description You can call this operation to update the configurations of both the old and new HBR clients.
        
        @param request: UpdateClientSettingsRequest
        @return: UpdateClientSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_client_settings_with_options_async(request, runtime)

    def update_container_cluster_with_options(
        self,
        request: hbr_20170908_models.UpdateContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateContainerClusterResponse:
        """
        @summary Update container cluster information, including the container cluster name, network type, etc.
        
        @param request: UpdateContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.renew_token):
            query['RenewToken'] = request.renew_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_cluster_with_options_async(
        self,
        request: hbr_20170908_models.UpdateContainerClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateContainerClusterResponse:
        """
        @summary Update container cluster information, including the container cluster name, network type, etc.
        
        @param request: UpdateContainerClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.renew_token):
            query['RenewToken'] = request.renew_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerCluster',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container_cluster(
        self,
        request: hbr_20170908_models.UpdateContainerClusterRequest,
    ) -> hbr_20170908_models.UpdateContainerClusterResponse:
        """
        @summary Update container cluster information, including the container cluster name, network type, etc.
        
        @param request: UpdateContainerClusterRequest
        @return: UpdateContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_container_cluster_with_options(request, runtime)

    async def update_container_cluster_async(
        self,
        request: hbr_20170908_models.UpdateContainerClusterRequest,
    ) -> hbr_20170908_models.UpdateContainerClusterResponse:
        """
        @summary Update container cluster information, including the container cluster name, network type, etc.
        
        @param request: UpdateContainerClusterRequest
        @return: UpdateContainerClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_container_cluster_with_options_async(request, runtime)

    def update_hana_backup_plan_with_options(
        self,
        request: hbr_20170908_models.UpdateHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaBackupPlanResponse:
        """
        @summary Updates an SAP HANA backup plan.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: UpdateHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_backup_plan_with_options_async(
        self,
        request: hbr_20170908_models.UpdateHanaBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaBackupPlanResponse:
        """
        @summary Updates an SAP HANA backup plan.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: UpdateHanaBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupPlan',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_backup_plan(
        self,
        request: hbr_20170908_models.UpdateHanaBackupPlanRequest,
    ) -> hbr_20170908_models.UpdateHanaBackupPlanResponse:
        """
        @summary Updates an SAP HANA backup plan.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: UpdateHanaBackupPlanRequest
        @return: UpdateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_backup_plan_with_options(request, runtime)

    async def update_hana_backup_plan_async(
        self,
        request: hbr_20170908_models.UpdateHanaBackupPlanRequest,
    ) -> hbr_20170908_models.UpdateHanaBackupPlanResponse:
        """
        @summary Updates an SAP HANA backup plan.
        
        @description    A backup plan defines the data source, backup policy, and other configurations. After you execute a backup plan, a backup job is generated to record the backup progress and the backup result. If a backup job is completed, a backup snapshot is generated. You can use a backup snapshot to create a restore job.
        You can specify only one type of data source in a backup plan.
        You can specify only one interval as a backup cycle in a backup plan.
        Each backup plan allows you to back up data to only one backup vault.
        
        @param request: UpdateHanaBackupPlanRequest
        @return: UpdateHanaBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_hana_backup_plan_with_options_async(request, runtime)

    def update_hana_backup_setting_with_options(
        self,
        request: hbr_20170908_models.UpdateHanaBackupSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaBackupSettingResponse:
        """
        @summary Updates the backup parameters of an SAP HANA database.
        
        @description You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        
        @param request: UpdateHanaBackupSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_backup_parameter_file):
            query['CatalogBackupParameterFile'] = request.catalog_backup_parameter_file
        if not UtilClient.is_unset(request.catalog_backup_using_backint):
            query['CatalogBackupUsingBackint'] = request.catalog_backup_using_backint
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_backup_parameter_file):
            query['DataBackupParameterFile'] = request.data_backup_parameter_file
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.enable_auto_log_backup):
            query['EnableAutoLogBackup'] = request.enable_auto_log_backup
        if not UtilClient.is_unset(request.log_backup_parameter_file):
            query['LogBackupParameterFile'] = request.log_backup_parameter_file
        if not UtilClient.is_unset(request.log_backup_timeout):
            query['LogBackupTimeout'] = request.log_backup_timeout
        if not UtilClient.is_unset(request.log_backup_using_backint):
            query['LogBackupUsingBackint'] = request.log_backup_using_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_backup_setting_with_options_async(
        self,
        request: hbr_20170908_models.UpdateHanaBackupSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaBackupSettingResponse:
        """
        @summary Updates the backup parameters of an SAP HANA database.
        
        @description You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        
        @param request: UpdateHanaBackupSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaBackupSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_backup_parameter_file):
            query['CatalogBackupParameterFile'] = request.catalog_backup_parameter_file
        if not UtilClient.is_unset(request.catalog_backup_using_backint):
            query['CatalogBackupUsingBackint'] = request.catalog_backup_using_backint
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data_backup_parameter_file):
            query['DataBackupParameterFile'] = request.data_backup_parameter_file
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.enable_auto_log_backup):
            query['EnableAutoLogBackup'] = request.enable_auto_log_backup
        if not UtilClient.is_unset(request.log_backup_parameter_file):
            query['LogBackupParameterFile'] = request.log_backup_parameter_file
        if not UtilClient.is_unset(request.log_backup_timeout):
            query['LogBackupTimeout'] = request.log_backup_timeout
        if not UtilClient.is_unset(request.log_backup_using_backint):
            query['LogBackupUsingBackint'] = request.log_backup_using_backint
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaBackupSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaBackupSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_backup_setting(
        self,
        request: hbr_20170908_models.UpdateHanaBackupSettingRequest,
    ) -> hbr_20170908_models.UpdateHanaBackupSettingResponse:
        """
        @summary Updates the backup parameters of an SAP HANA database.
        
        @description You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        
        @param request: UpdateHanaBackupSettingRequest
        @return: UpdateHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_backup_setting_with_options(request, runtime)

    async def update_hana_backup_setting_async(
        self,
        request: hbr_20170908_models.UpdateHanaBackupSettingRequest,
    ) -> hbr_20170908_models.UpdateHanaBackupSettingResponse:
        """
        @summary Updates the backup parameters of an SAP HANA database.
        
        @description You can call the UpdateHanaRetentionSetting operation to update the backup retention period of a database.
        
        @param request: UpdateHanaBackupSettingRequest
        @return: UpdateHanaBackupSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_hana_backup_setting_with_options_async(request, runtime)

    def update_hana_instance_with_options(
        self,
        request: hbr_20170908_models.UpdateHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaInstanceResponse:
        """
        @summary Updates an SAP HANA instance.
        
        @param request: UpdateHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_instance_with_options_async(
        self,
        request: hbr_20170908_models.UpdateHanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaInstanceResponse:
        """
        @summary Updates an SAP HANA instance.
        
        @param request: UpdateHanaInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hana_name):
            query['HanaName'] = request.hana_name
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaInstance',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_instance(
        self,
        request: hbr_20170908_models.UpdateHanaInstanceRequest,
    ) -> hbr_20170908_models.UpdateHanaInstanceResponse:
        """
        @summary Updates an SAP HANA instance.
        
        @param request: UpdateHanaInstanceRequest
        @return: UpdateHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_instance_with_options(request, runtime)

    async def update_hana_instance_async(
        self,
        request: hbr_20170908_models.UpdateHanaInstanceRequest,
    ) -> hbr_20170908_models.UpdateHanaInstanceResponse:
        """
        @summary Updates an SAP HANA instance.
        
        @param request: UpdateHanaInstanceRequest
        @return: UpdateHanaInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_hana_instance_with_options_async(request, runtime)

    def update_hana_retention_setting_with_options(
        self,
        request: hbr_20170908_models.UpdateHanaRetentionSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaRetentionSettingResponse:
        """
        @summary Updates the backup retention period of an SAP HANA database.
        
        @description    If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: UpdateHanaRetentionSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_retention_setting_with_options_async(
        self,
        request: hbr_20170908_models.UpdateHanaRetentionSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateHanaRetentionSettingResponse:
        """
        @summary Updates the backup retention period of an SAP HANA database.
        
        @description    If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: UpdateHanaRetentionSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHanaRetentionSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.schedule):
            query['Schedule'] = request.schedule
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHanaRetentionSetting',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateHanaRetentionSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_retention_setting(
        self,
        request: hbr_20170908_models.UpdateHanaRetentionSettingRequest,
    ) -> hbr_20170908_models.UpdateHanaRetentionSettingResponse:
        """
        @summary Updates the backup retention period of an SAP HANA database.
        
        @description    If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: UpdateHanaRetentionSettingRequest
        @return: UpdateHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hana_retention_setting_with_options(request, runtime)

    async def update_hana_retention_setting_async(
        self,
        request: hbr_20170908_models.UpdateHanaRetentionSettingRequest,
    ) -> hbr_20170908_models.UpdateHanaRetentionSettingResponse:
        """
        @summary Updates the backup retention period of an SAP HANA database.
        
        @description    If you want to update the backup parameters of a database, you can call the UpdateHanaBackupSetting operation.
        Cloud Backup deletes the expired catalogs and data that are related to Backint and file backup. The deleted catalogs and data cannot be restored. We recommend that you set the retention period based on your business requirements.
        
        @param request: UpdateHanaRetentionSettingRequest
        @return: UpdateHanaRetentionSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_hana_retention_setting_with_options_async(request, runtime)

    def update_policy_binding_with_options(
        self,
        tmp_req: hbr_20170908_models.UpdatePolicyBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdatePolicyBindingResponse:
        """
        @summary Modifies the association between a backup policy and a data source.
        
        @param tmp_req: UpdatePolicyBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyBindingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_options):
            request.advanced_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_options, 'AdvancedOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_options_shrink):
            query['AdvancedOptions'] = request.advanced_options_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.exclude):
            query['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            query['Include'] = request.include
        if not UtilClient.is_unset(request.policy_binding_description):
            query['PolicyBindingDescription'] = request.policy_binding_description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_binding_with_options_async(
        self,
        tmp_req: hbr_20170908_models.UpdatePolicyBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdatePolicyBindingResponse:
        """
        @summary Modifies the association between a backup policy and a data source.
        
        @param tmp_req: UpdatePolicyBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyBindingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyBindingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_options):
            request.advanced_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_options, 'AdvancedOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_options_shrink):
            query['AdvancedOptions'] = request.advanced_options_shrink
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.exclude):
            query['Exclude'] = request.exclude
        if not UtilClient.is_unset(request.include):
            query['Include'] = request.include
        if not UtilClient.is_unset(request.policy_binding_description):
            query['PolicyBindingDescription'] = request.policy_binding_description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyBinding',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_binding(
        self,
        request: hbr_20170908_models.UpdatePolicyBindingRequest,
    ) -> hbr_20170908_models.UpdatePolicyBindingResponse:
        """
        @summary Modifies the association between a backup policy and a data source.
        
        @param request: UpdatePolicyBindingRequest
        @return: UpdatePolicyBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_policy_binding_with_options(request, runtime)

    async def update_policy_binding_async(
        self,
        request: hbr_20170908_models.UpdatePolicyBindingRequest,
    ) -> hbr_20170908_models.UpdatePolicyBindingResponse:
        """
        @summary Modifies the association between a backup policy and a data source.
        
        @param request: UpdatePolicyBindingRequest
        @return: UpdatePolicyBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_policy_binding_with_options_async(request, runtime)

    def update_policy_v2with_options(
        self,
        tmp_req: hbr_20170908_models.UpdatePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdatePolicyV2Response:
        """
        @summary Modifies a backup policy.
        
        @description If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        
        @param tmp_req: UpdatePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_v2with_options_async(
        self,
        tmp_req: hbr_20170908_models.UpdatePolicyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdatePolicyV2Response:
        """
        @summary Modifies a backup policy.
        
        @description If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        
        @param tmp_req: UpdatePolicyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpdatePolicyV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not UtilClient.is_unset(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePolicyV2',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdatePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_v2(
        self,
        request: hbr_20170908_models.UpdatePolicyV2Request,
    ) -> hbr_20170908_models.UpdatePolicyV2Response:
        """
        @summary Modifies a backup policy.
        
        @description If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        
        @param request: UpdatePolicyV2Request
        @return: UpdatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.update_policy_v2with_options(request, runtime)

    async def update_policy_v2_async(
        self,
        request: hbr_20170908_models.UpdatePolicyV2Request,
    ) -> hbr_20170908_models.UpdatePolicyV2Response:
        """
        @summary Modifies a backup policy.
        
        @description If you modify a backup policy, the modification takes effect on all data sources that are bound to the backup policy. Proceed with caution.
        
        @param request: UpdatePolicyV2Request
        @return: UpdatePolicyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_policy_v2with_options_async(request, runtime)

    def update_vault_with_options(
        self,
        request: hbr_20170908_models.UpdateVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateVaultResponse:
        """
        @summary Updates the configuration information about the backup vault.
        
        @param request: UpdateVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vault_with_options_async(
        self,
        request: hbr_20170908_models.UpdateVaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpdateVaultResponse:
        """
        @summary Updates the configuration information about the backup vault.
        
        @param request: UpdateVaultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVaultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        if not UtilClient.is_unset(request.vault_name):
            query['VaultName'] = request.vault_name
        if not UtilClient.is_unset(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVault',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpdateVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vault(
        self,
        request: hbr_20170908_models.UpdateVaultRequest,
    ) -> hbr_20170908_models.UpdateVaultResponse:
        """
        @summary Updates the configuration information about the backup vault.
        
        @param request: UpdateVaultRequest
        @return: UpdateVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vault_with_options(request, runtime)

    async def update_vault_async(
        self,
        request: hbr_20170908_models.UpdateVaultRequest,
    ) -> hbr_20170908_models.UpdateVaultResponse:
        """
        @summary Updates the configuration information about the backup vault.
        
        @param request: UpdateVaultRequest
        @return: UpdateVaultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_vault_with_options_async(request, runtime)

    def upgrade_backup_clients_with_options(
        self,
        tmp_req: hbr_20170908_models.UpgradeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpgradeBackupClientsResponse:
        """
        @summary Upgrades an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes.
        
        @param tmp_req: UpgradeBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpgradeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_backup_clients_with_options_async(
        self,
        tmp_req: hbr_20170908_models.UpgradeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpgradeBackupClientsResponse:
        """
        @summary Upgrades an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes.
        
        @param tmp_req: UpgradeBackupClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeBackupClientsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hbr_20170908_models.UpgradeBackupClientsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_ids):
            request.client_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not UtilClient.is_unset(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not UtilClient.is_unset(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not UtilClient.is_unset(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupClients',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_backup_clients(
        self,
        request: hbr_20170908_models.UpgradeBackupClientsRequest,
    ) -> hbr_20170908_models.UpgradeBackupClientsResponse:
        """
        @summary Upgrades an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes.
        
        @param request: UpgradeBackupClientsRequest
        @return: UpgradeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_clients_with_options(request, runtime)

    async def upgrade_backup_clients_async(
        self,
        request: hbr_20170908_models.UpgradeBackupClientsRequest,
    ) -> hbr_20170908_models.UpgradeBackupClientsResponse:
        """
        @summary Upgrades an HBR client on one or more Elastic Compute Service (ECS) instances.
        
        @description    This operation creates an asynchronous job at the backend and calls Cloud Assistant to upgrade an HBR client that is installed on an ECS instance.
        You can call the DescribeTask operation to query the execution result of an asynchronous job.
        The timeout period of an asynchronous job is 15 minutes.
        
        @param request: UpgradeBackupClientsRequest
        @return: UpgradeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_backup_clients_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: hbr_20170908_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpgradeClientResponse:
        """
        @summary Upgrades the Cloud Backup client.
        
        @description You can call this operation to upgrade a Cloud Backup client to the latest version. After the Cloud Backup client is upgraded, the version of the client cannot be rolled back.
        
        @param request: UpgradeClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_client_with_options_async(
        self,
        request: hbr_20170908_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbr_20170908_models.UpgradeClientResponse:
        """
        @summary Upgrades the Cloud Backup client.
        
        @description You can call this operation to upgrade a Cloud Backup client to the latest version. After the Cloud Backup client is upgraded, the version of the client cannot be rolled back.
        
        @param request: UpgradeClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClientResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2017-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbr_20170908_models.UpgradeClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_client(
        self,
        request: hbr_20170908_models.UpgradeClientRequest,
    ) -> hbr_20170908_models.UpgradeClientResponse:
        """
        @summary Upgrades the Cloud Backup client.
        
        @description You can call this operation to upgrade a Cloud Backup client to the latest version. After the Cloud Backup client is upgraded, the version of the client cannot be rolled back.
        
        @param request: UpgradeClientRequest
        @return: UpgradeClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: hbr_20170908_models.UpgradeClientRequest,
    ) -> hbr_20170908_models.UpgradeClientResponse:
        """
        @summary Upgrades the Cloud Backup client.
        
        @description You can call this operation to upgrade a Cloud Backup client to the latest version. After the Cloud Backup client is upgraded, the version of the client cannot be rolled back.
        
        @param request: UpgradeClientRequest
        @return: UpgradeClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)
