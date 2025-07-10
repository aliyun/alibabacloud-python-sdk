# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adb20190315 import models as adb_20190315_models
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
            'cn-qingdao': 'adb.aliyuncs.com',
            'cn-beijing': 'adb.aliyuncs.com',
            'cn-hangzhou': 'adb.aliyuncs.com',
            'cn-shanghai': 'adb.aliyuncs.com',
            'cn-shenzhen': 'adb.aliyuncs.com',
            'cn-hongkong': 'adb.aliyuncs.com',
            'ap-southeast-1': 'adb.aliyuncs.com',
            'us-west-1': 'adb.aliyuncs.com',
            'us-east-1': 'adb.aliyuncs.com',
            'cn-hangzhou-finance': 'adb.aliyuncs.com',
            'cn-north-2-gov-1': 'adb.aliyuncs.com',
            'ap-northeast-2-pop': 'adb.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'adb.aliyuncs.com',
            'cn-beijing-finance-pop': 'adb.aliyuncs.com',
            'cn-beijing-gov-1': 'adb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'adb.aliyuncs.com',
            'cn-edge-1': 'adb.aliyuncs.com',
            'cn-fujian': 'adb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'adb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'adb.aliyuncs.com',
            'cn-hangzhou-test-306': 'adb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'adb.aliyuncs.com',
            'cn-qingdao-nebula': 'adb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'adb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'adb.aliyuncs.com',
            'cn-shanghai-finance-1': 'adb.aliyuncs.com',
            'cn-shanghai-inner': 'adb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'adb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'adb.aliyuncs.com',
            'cn-shenzhen-inner': 'adb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'adb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'adb.aliyuncs.com',
            'cn-wuhan': 'adb.aliyuncs.com',
            'cn-yushanfang': 'adb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'adb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'adb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'adb.aliyuncs.com',
            'eu-west-1-oxs': 'adb.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'adb.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'adb.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('adb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_cluster_public_connection_with_options(
        self,
        request: adb_20190315_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.AllocateClusterPublicConnectionResponse:
        """
        @summary 申请公网链接
        
        @param request: AllocateClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: adb_20190315_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.AllocateClusterPublicConnectionResponse:
        """
        @summary 申请公网链接
        
        @param request: AllocateClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: adb_20190315_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20190315_models.AllocateClusterPublicConnectionResponse:
        """
        @summary 申请公网链接
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: adb_20190315_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20190315_models.AllocateClusterPublicConnectionResponse:
        """
        @summary 申请公网链接
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def apply_advice_by_id_with_options(
        self,
        request: adb_20190315_models.ApplyAdviceByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ApplyAdviceByIdResponse:
        """
        @summary ApplyAdviceById
        
        @param request: ApplyAdviceByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyAdviceByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAdviceById',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ApplyAdviceByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_advice_by_id_with_options_async(
        self,
        request: adb_20190315_models.ApplyAdviceByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ApplyAdviceByIdResponse:
        """
        @summary ApplyAdviceById
        
        @param request: ApplyAdviceByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyAdviceByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAdviceById',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ApplyAdviceByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_advice_by_id(
        self,
        request: adb_20190315_models.ApplyAdviceByIdRequest,
    ) -> adb_20190315_models.ApplyAdviceByIdResponse:
        """
        @summary ApplyAdviceById
        
        @param request: ApplyAdviceByIdRequest
        @return: ApplyAdviceByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_advice_by_id_with_options(request, runtime)

    async def apply_advice_by_id_async(
        self,
        request: adb_20190315_models.ApplyAdviceByIdRequest,
    ) -> adb_20190315_models.ApplyAdviceByIdResponse:
        """
        @summary ApplyAdviceById
        
        @param request: ApplyAdviceByIdRequest
        @return: ApplyAdviceByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_advice_by_id_with_options_async(request, runtime)

    def attach_user_eniwith_options(
        self,
        request: adb_20190315_models.AttachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.AttachUserENIResponse:
        """
        @summary 打通用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: AttachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachUserENI',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.AttachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_user_eniwith_options_async(
        self,
        request: adb_20190315_models.AttachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.AttachUserENIResponse:
        """
        @summary 打通用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: AttachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachUserENI',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.AttachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_user_eni(
        self,
        request: adb_20190315_models.AttachUserENIRequest,
    ) -> adb_20190315_models.AttachUserENIResponse:
        """
        @summary 打通用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: AttachUserENIRequest
        @return: AttachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_user_eniwith_options(request, runtime)

    async def attach_user_eni_async(
        self,
        request: adb_20190315_models.AttachUserENIRequest,
    ) -> adb_20190315_models.AttachUserENIResponse:
        """
        @summary 打通用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: AttachUserENIRequest
        @return: AttachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_user_eniwith_options_async(request, runtime)

    def batch_apply_advice_by_id_list_with_options(
        self,
        request: adb_20190315_models.BatchApplyAdviceByIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BatchApplyAdviceByIdListResponse:
        """
        @summary BatchApplyAdviceByIdList
        
        @param request: BatchApplyAdviceByIdListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchApplyAdviceByIdListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_id_list):
            query['AdviceIdList'] = request.advice_id_list
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchApplyAdviceByIdList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BatchApplyAdviceByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_apply_advice_by_id_list_with_options_async(
        self,
        request: adb_20190315_models.BatchApplyAdviceByIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BatchApplyAdviceByIdListResponse:
        """
        @summary BatchApplyAdviceByIdList
        
        @param request: BatchApplyAdviceByIdListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchApplyAdviceByIdListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_id_list):
            query['AdviceIdList'] = request.advice_id_list
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchApplyAdviceByIdList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BatchApplyAdviceByIdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_apply_advice_by_id_list(
        self,
        request: adb_20190315_models.BatchApplyAdviceByIdListRequest,
    ) -> adb_20190315_models.BatchApplyAdviceByIdListResponse:
        """
        @summary BatchApplyAdviceByIdList
        
        @param request: BatchApplyAdviceByIdListRequest
        @return: BatchApplyAdviceByIdListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_apply_advice_by_id_list_with_options(request, runtime)

    async def batch_apply_advice_by_id_list_async(
        self,
        request: adb_20190315_models.BatchApplyAdviceByIdListRequest,
    ) -> adb_20190315_models.BatchApplyAdviceByIdListResponse:
        """
        @summary BatchApplyAdviceByIdList
        
        @param request: BatchApplyAdviceByIdListRequest
        @return: BatchApplyAdviceByIdListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_apply_advice_by_id_list_with_options_async(request, runtime)

    def bind_dbresource_group_with_user_with_options(
        self,
        request: adb_20190315_models.BindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster with a database account.
        
        @description ## Precautions
        This operation is applicable only for elastic clusters of 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourceGroupWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_group_with_user_with_options_async(
        self,
        request: adb_20190315_models.BindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster with a database account.
        
        @description ## Precautions
        This operation is applicable only for elastic clusters of 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourceGroupWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_group_with_user(
        self,
        request: adb_20190315_models.BindDBResourceGroupWithUserRequest,
    ) -> adb_20190315_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster with a database account.
        
        @description ## Precautions
        This operation is applicable only for elastic clusters of 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourceGroupWithUserRequest
        @return: BindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_dbresource_group_with_user_with_options(request, runtime)

    async def bind_dbresource_group_with_user_async(
        self,
        request: adb_20190315_models.BindDBResourceGroupWithUserRequest,
    ) -> adb_20190315_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster with a database account.
        
        @description ## Precautions
        This operation is applicable only for elastic clusters of 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourceGroupWithUserRequest
        @return: BindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_dbresource_group_with_user_with_options_async(request, runtime)

    def bind_dbresource_pool_with_user_with_options(
        self,
        request: adb_20190315_models.BindDBResourcePoolWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BindDBResourcePoolWithUserResponse:
        """
        @summary 绑定资源组用户
        
        @description    This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourcePoolWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourcePoolWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourcePoolWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BindDBResourcePoolWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_pool_with_user_with_options_async(
        self,
        request: adb_20190315_models.BindDBResourcePoolWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.BindDBResourcePoolWithUserResponse:
        """
        @summary 绑定资源组用户
        
        @description    This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourcePoolWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourcePoolWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourcePoolWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.BindDBResourcePoolWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_pool_with_user(
        self,
        request: adb_20190315_models.BindDBResourcePoolWithUserRequest,
    ) -> adb_20190315_models.BindDBResourcePoolWithUserResponse:
        """
        @summary 绑定资源组用户
        
        @description    This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourcePoolWithUserRequest
        @return: BindDBResourcePoolWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_dbresource_pool_with_user_with_options(request, runtime)

    async def bind_dbresource_pool_with_user_async(
        self,
        request: adb_20190315_models.BindDBResourcePoolWithUserRequest,
    ) -> adb_20190315_models.BindDBResourcePoolWithUserResponse:
        """
        @summary 绑定资源组用户
        
        @description    This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be associated with a database account.
        
        @param request: BindDBResourcePoolWithUserRequest
        @return: BindDBResourcePoolWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_dbresource_pool_with_user_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: adb_20190315_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CancelActiveOperationTasksResponse:
        """
        @summary Cancels O\\&M events.
        
        @param request: CancelActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CancelActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_active_operation_tasks_with_options_async(
        self,
        request: adb_20190315_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CancelActiveOperationTasksResponse:
        """
        @summary Cancels O\\&M events.
        
        @param request: CancelActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CancelActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_active_operation_tasks(
        self,
        request: adb_20190315_models.CancelActiveOperationTasksRequest,
    ) -> adb_20190315_models.CancelActiveOperationTasksResponse:
        """
        @summary Cancels O\\&M events.
        
        @param request: CancelActiveOperationTasksRequest
        @return: CancelActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    async def cancel_active_operation_tasks_async(
        self,
        request: adb_20190315_models.CancelActiveOperationTasksRequest,
    ) -> adb_20190315_models.CancelActiveOperationTasksResponse:
        """
        @summary Cancels O\\&M events.
        
        @param request: CancelActiveOperationTasksRequest
        @return: CancelActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_active_operation_tasks_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: adb_20190315_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: adb_20190315_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: adb_20190315_models.CheckServiceLinkedRoleRequest,
    ) -> adb_20190315_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: adb_20190315_models.CheckServiceLinkedRoleRequest,
    ) -> adb_20190315_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        tmp_req: adb_20190315_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL cluster.
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        tmp_req: adb_20190315_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL cluster.
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: adb_20190315_models.CreateAccountRequest,
    ) -> adb_20190315_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: adb_20190315_models.CreateAccountRequest,
    ) -> adb_20190315_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: adb_20190315_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Warehouse Edition cluster.
        
        @description After you create a cluster, you are billed for the cluster specifications that you select. For more information about the billable items and pricing for Data Warehouse Edition  clusters, see [Billable items of Data Warehouse Edition](https://help.aliyun.com/document_detail/303131.html) and [Pricing for Data Warehouse Edition](https://help.aliyun.com/document_detail/135229.html).
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not UtilClient.is_unset(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not UtilClient.is_unset(request.kms_id):
            query['KmsId'] = request.kms_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
            action='CreateDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: adb_20190315_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Warehouse Edition cluster.
        
        @description After you create a cluster, you are billed for the cluster specifications that you select. For more information about the billable items and pricing for Data Warehouse Edition  clusters, see [Billable items of Data Warehouse Edition](https://help.aliyun.com/document_detail/303131.html) and [Pricing for Data Warehouse Edition](https://help.aliyun.com/document_detail/135229.html).
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not UtilClient.is_unset(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not UtilClient.is_unset(request.kms_id):
            query['KmsId'] = request.kms_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
            action='CreateDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: adb_20190315_models.CreateDBClusterRequest,
    ) -> adb_20190315_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Warehouse Edition cluster.
        
        @description After you create a cluster, you are billed for the cluster specifications that you select. For more information about the billable items and pricing for Data Warehouse Edition  clusters, see [Billable items of Data Warehouse Edition](https://help.aliyun.com/document_detail/303131.html) and [Pricing for Data Warehouse Edition](https://help.aliyun.com/document_detail/135229.html).
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: adb_20190315_models.CreateDBClusterRequest,
    ) -> adb_20190315_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Warehouse Edition cluster.
        
        @description After you create a cluster, you are billed for the cluster specifications that you select. For more information about the billable items and pricing for Data Warehouse Edition  clusters, see [Billable items of Data Warehouse Edition](https://help.aliyun.com/document_detail/303131.html) and [Pricing for Data Warehouse Edition](https://help.aliyun.com/document_detail/135229.html).
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbresource_group_with_options(
        self,
        tmp_req: adb_20190315_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param tmp_req: CreateDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.CreateDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.engine_params):
            request.engine_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_group_with_options_async(
        self,
        tmp_req: adb_20190315_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param tmp_req: CreateDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.CreateDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.engine_params):
            request.engine_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_group(
        self,
        request: adb_20190315_models.CreateDBResourceGroupRequest,
    ) -> adb_20190315_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: CreateDBResourceGroupRequest
        @return: CreateDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    async def create_dbresource_group_async(
        self,
        request: adb_20190315_models.CreateDBResourceGroupRequest,
    ) -> adb_20190315_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: CreateDBResourceGroupRequest
        @return: CreateDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbresource_group_with_options_async(request, runtime)

    def create_dbresource_pool_with_options(
        self,
        request: adb_20190315_models.CreateDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBResourcePoolResponse:
        """
        @summary 创建资源组
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: CreateDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_pool_with_options_async(
        self,
        request: adb_20190315_models.CreateDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateDBResourcePoolResponse:
        """
        @summary 创建资源组
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: CreateDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_pool(
        self,
        request: adb_20190315_models.CreateDBResourcePoolRequest,
    ) -> adb_20190315_models.CreateDBResourcePoolResponse:
        """
        @summary 创建资源组
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: CreateDBResourcePoolRequest
        @return: CreateDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_pool_with_options(request, runtime)

    async def create_dbresource_pool_async(
        self,
        request: adb_20190315_models.CreateDBResourcePoolRequest,
    ) -> adb_20190315_models.CreateDBResourcePoolResponse:
        """
        @summary 创建资源组
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: CreateDBResourcePoolRequest
        @return: CreateDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbresource_pool_with_options_async(request, runtime)

    def create_elastic_plan_with_options(
        self,
        request: adb_20190315_models.CreateElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateElasticPlanResponse:
        """
        @summary Creates a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: CreateElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not UtilClient.is_unset(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not UtilClient.is_unset(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not UtilClient.is_unset(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not UtilClient.is_unset(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not UtilClient.is_unset(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not UtilClient.is_unset(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not UtilClient.is_unset(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_plan_with_options_async(
        self,
        request: adb_20190315_models.CreateElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateElasticPlanResponse:
        """
        @summary Creates a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: CreateElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not UtilClient.is_unset(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not UtilClient.is_unset(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not UtilClient.is_unset(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not UtilClient.is_unset(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not UtilClient.is_unset(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not UtilClient.is_unset(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not UtilClient.is_unset(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_plan(
        self,
        request: adb_20190315_models.CreateElasticPlanRequest,
    ) -> adb_20190315_models.CreateElasticPlanResponse:
        """
        @summary Creates a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: CreateElasticPlanRequest
        @return: CreateElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_plan_with_options(request, runtime)

    async def create_elastic_plan_async(
        self,
        request: adb_20190315_models.CreateElasticPlanRequest,
    ) -> adb_20190315_models.CreateElasticPlanResponse:
        """
        @summary Creates a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: CreateElasticPlanRequest
        @return: CreateElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_elastic_plan_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: adb_20190315_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: adb_20190315_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: adb_20190315_models.CreateServiceLinkedRoleRequest,
    ) -> adb_20190315_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: adb_20190315_models.CreateServiceLinkedRoleRequest,
    ) -> adb_20190315_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: adb_20190315_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteAccountResponse:
        """
        @summary 删除高权限帐号
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: adb_20190315_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteAccountResponse:
        """
        @summary 删除高权限帐号
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: adb_20190315_models.DeleteAccountRequest,
    ) -> adb_20190315_models.DeleteAccountResponse:
        """
        @summary 删除高权限帐号
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: adb_20190315_models.DeleteAccountRequest,
    ) -> adb_20190315_models.DeleteAccountResponse:
        """
        @summary 删除高权限帐号
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backups_with_options(
        self,
        request: adb_20190315_models.DeleteBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteBackupsResponse:
        """
        @summary Manually deletes backup sets.
        
        @description    Deleting backup sets is an asynchronous operation and may require 10 to 20 minutes to complete.
        You can delete up to 100 backup sets at a time. If you want to delete more than 100 backup sets, call this operation twice.
        To ensure data security, the system forcibly retains one valid backup set. If you want to delete the last backup set, the system prohibits your operation.
        
        @param request: DeleteBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackups',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backups_with_options_async(
        self,
        request: adb_20190315_models.DeleteBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteBackupsResponse:
        """
        @summary Manually deletes backup sets.
        
        @description    Deleting backup sets is an asynchronous operation and may require 10 to 20 minutes to complete.
        You can delete up to 100 backup sets at a time. If you want to delete more than 100 backup sets, call this operation twice.
        To ensure data security, the system forcibly retains one valid backup set. If you want to delete the last backup set, the system prohibits your operation.
        
        @param request: DeleteBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackups',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backups(
        self,
        request: adb_20190315_models.DeleteBackupsRequest,
    ) -> adb_20190315_models.DeleteBackupsResponse:
        """
        @summary Manually deletes backup sets.
        
        @description    Deleting backup sets is an asynchronous operation and may require 10 to 20 minutes to complete.
        You can delete up to 100 backup sets at a time. If you want to delete more than 100 backup sets, call this operation twice.
        To ensure data security, the system forcibly retains one valid backup set. If you want to delete the last backup set, the system prohibits your operation.
        
        @param request: DeleteBackupsRequest
        @return: DeleteBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backups_with_options(request, runtime)

    async def delete_backups_async(
        self,
        request: adb_20190315_models.DeleteBackupsRequest,
    ) -> adb_20190315_models.DeleteBackupsResponse:
        """
        @summary Manually deletes backup sets.
        
        @description    Deleting backup sets is an asynchronous operation and may require 10 to 20 minutes to complete.
        You can delete up to 100 backup sets at a time. If you want to delete more than 100 backup sets, call this operation twice.
        To ensure data security, the system forcibly retains one valid backup set. If you want to delete the last backup set, the system prohibits your operation.
        
        @param request: DeleteBackupsRequest
        @return: DeleteBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backups_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: adb_20190315_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL cluster.
        
        @description    You cannot delete subscription clusters by calling API operations. After expiration, subscription clusters are automatically released. If you no longer need a cluster, you can unsubscribe from the cluster in the Expenses and Costs console. For information about cluster refunds, see [Refund policy](https://help.aliyun.com/document_detail/471477.html).
        After you delete a cluster, resources of the cluster are immediately released, and data of the cluster is no longer retained and cannot be restored. Proceed with caution.
        The cluster that you want to delete must be in the Running state.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: adb_20190315_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL cluster.
        
        @description    You cannot delete subscription clusters by calling API operations. After expiration, subscription clusters are automatically released. If you no longer need a cluster, you can unsubscribe from the cluster in the Expenses and Costs console. For information about cluster refunds, see [Refund policy](https://help.aliyun.com/document_detail/471477.html).
        After you delete a cluster, resources of the cluster are immediately released, and data of the cluster is no longer retained and cannot be restored. Proceed with caution.
        The cluster that you want to delete must be in the Running state.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: adb_20190315_models.DeleteDBClusterRequest,
    ) -> adb_20190315_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL cluster.
        
        @description    You cannot delete subscription clusters by calling API operations. After expiration, subscription clusters are automatically released. If you no longer need a cluster, you can unsubscribe from the cluster in the Expenses and Costs console. For information about cluster refunds, see [Refund policy](https://help.aliyun.com/document_detail/471477.html).
        After you delete a cluster, resources of the cluster are immediately released, and data of the cluster is no longer retained and cannot be restored. Proceed with caution.
        The cluster that you want to delete must be in the Running state.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: adb_20190315_models.DeleteDBClusterRequest,
    ) -> adb_20190315_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL cluster.
        
        @description    You cannot delete subscription clusters by calling API operations. After expiration, subscription clusters are automatically released. If you no longer need a cluster, you can unsubscribe from the cluster in the Expenses and Costs console. For information about cluster refunds, see [Refund policy](https://help.aliyun.com/document_detail/471477.html).
        After you delete a cluster, resources of the cluster are immediately released, and data of the cluster is no longer retained and cannot be restored. Proceed with caution.
        The cluster that you want to delete must be in the Running state.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbresource_group_with_options(
        self,
        request: adb_20190315_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description ### Precautions
        You can call this operation only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_group_with_options_async(
        self,
        request: adb_20190315_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description ### Precautions
        You can call this operation only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_group(
        self,
        request: adb_20190315_models.DeleteDBResourceGroupRequest,
    ) -> adb_20190315_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description ### Precautions
        You can call this operation only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourceGroupRequest
        @return: DeleteDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    async def delete_dbresource_group_async(
        self,
        request: adb_20190315_models.DeleteDBResourceGroupRequest,
    ) -> adb_20190315_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description ### Precautions
        You can call this operation only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourceGroupRequest
        @return: DeleteDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbresource_group_with_options_async(request, runtime)

    def delete_dbresource_pool_with_options(
        self,
        request: adb_20190315_models.DeleteDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBResourcePoolResponse:
        """
        @summary 删除资源组
        
        @description *Precautions**\
        This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_pool_with_options_async(
        self,
        request: adb_20190315_models.DeleteDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteDBResourcePoolResponse:
        """
        @summary 删除资源组
        
        @description *Precautions**\
        This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_pool(
        self,
        request: adb_20190315_models.DeleteDBResourcePoolRequest,
    ) -> adb_20190315_models.DeleteDBResourcePoolResponse:
        """
        @summary 删除资源组
        
        @description *Precautions**\
        This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourcePoolRequest
        @return: DeleteDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_pool_with_options(request, runtime)

    async def delete_dbresource_pool_async(
        self,
        request: adb_20190315_models.DeleteDBResourcePoolRequest,
    ) -> adb_20190315_models.DeleteDBResourcePoolResponse:
        """
        @summary 删除资源组
        
        @description *Precautions**\
        This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition that have 32 cores or more.
        The default resource group USER_DEFAULT cannot be deleted.
        
        @param request: DeleteDBResourcePoolRequest
        @return: DeleteDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbresource_pool_with_options_async(request, runtime)

    def delete_elastic_plan_with_options(
        self,
        request: adb_20190315_models.DeleteElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scheduled scaling plan. You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition clusters in elastic mode for Cluster Edition.
        
        @param request: DeleteElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_plan_with_options_async(
        self,
        request: adb_20190315_models.DeleteElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scheduled scaling plan. You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition clusters in elastic mode for Cluster Edition.
        
        @param request: DeleteElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DeleteElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_plan(
        self,
        request: adb_20190315_models.DeleteElasticPlanRequest,
    ) -> adb_20190315_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scheduled scaling plan. You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition clusters in elastic mode for Cluster Edition.
        
        @param request: DeleteElasticPlanRequest
        @return: DeleteElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_plan_with_options(request, runtime)

    async def delete_elastic_plan_async(
        self,
        request: adb_20190315_models.DeleteElasticPlanRequest,
    ) -> adb_20190315_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scheduled scaling plan. You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition clusters in elastic mode for Cluster Edition.
        
        @param request: DeleteElasticPlanRequest
        @return: DeleteElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_elastic_plan_with_options_async(request, runtime)

    def describe_abnormal_pattern_detection_with_options(
        self,
        request: adb_20190315_models.DescribeAbnormalPatternDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAbnormalPatternDetectionResponse:
        """
        @summary Queries abnormal SQL patterns within a time range.
        
        @param request: DescribeAbnormalPatternDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAbnormalPatternDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAbnormalPatternDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAbnormalPatternDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abnormal_pattern_detection_with_options_async(
        self,
        request: adb_20190315_models.DescribeAbnormalPatternDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAbnormalPatternDetectionResponse:
        """
        @summary Queries abnormal SQL patterns within a time range.
        
        @param request: DescribeAbnormalPatternDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAbnormalPatternDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAbnormalPatternDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAbnormalPatternDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abnormal_pattern_detection(
        self,
        request: adb_20190315_models.DescribeAbnormalPatternDetectionRequest,
    ) -> adb_20190315_models.DescribeAbnormalPatternDetectionResponse:
        """
        @summary Queries abnormal SQL patterns within a time range.
        
        @param request: DescribeAbnormalPatternDetectionRequest
        @return: DescribeAbnormalPatternDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_abnormal_pattern_detection_with_options(request, runtime)

    async def describe_abnormal_pattern_detection_async(
        self,
        request: adb_20190315_models.DescribeAbnormalPatternDetectionRequest,
    ) -> adb_20190315_models.DescribeAbnormalPatternDetectionResponse:
        """
        @summary Queries abnormal SQL patterns within a time range.
        
        @param request: DescribeAbnormalPatternDetectionRequest
        @return: DescribeAbnormalPatternDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_abnormal_pattern_detection_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: adb_20190315_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAccountsResponse:
        """
        @summary Queries a list of database accounts for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: adb_20190315_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAccountsResponse:
        """
        @summary Queries a list of database accounts for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: adb_20190315_models.DescribeAccountsRequest,
    ) -> adb_20190315_models.DescribeAccountsResponse:
        """
        @summary Queries a list of database accounts for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: adb_20190315_models.DescribeAccountsRequest,
    ) -> adb_20190315_models.DescribeAccountsResponse:
        """
        @summary Queries a list of database accounts for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: adb_20190315_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary Queries the configuration information about O\\&M tasks.
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationMaintainConf',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_maintain_conf_with_options_async(
        self,
        request: adb_20190315_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary Queries the configuration information about O\\&M tasks.
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationMaintainConf',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_maintain_conf(
        self,
        request: adb_20190315_models.DescribeActiveOperationMaintainConfRequest,
    ) -> adb_20190315_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary Queries the configuration information about O\\&M tasks.
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @return: DescribeActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    async def describe_active_operation_maintain_conf_async(
        self,
        request: adb_20190315_models.DescribeActiveOperationMaintainConfRequest,
    ) -> adb_20190315_models.DescribeActiveOperationMaintainConfResponse:
        """
        @summary Queries the configuration information about O\\&M tasks.
        
        @param request: DescribeActiveOperationMaintainConfRequest
        @return: DescribeActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_maintain_conf_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: adb_20190315_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries the information about O\\&M tasks.
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not UtilClient.is_unset(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not UtilClient.is_unset(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: adb_20190315_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries the information about O\\&M tasks.
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not UtilClient.is_unset(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not UtilClient.is_unset(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: adb_20190315_models.DescribeActiveOperationTasksRequest,
    ) -> adb_20190315_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries the information about O\\&M tasks.
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: adb_20190315_models.DescribeActiveOperationTasksRequest,
    ) -> adb_20190315_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries the information about O\\&M tasks.
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_advice_service_enabled_with_options(
        self,
        request: adb_20190315_models.DescribeAdviceServiceEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAdviceServiceEnabledResponse:
        """
        @summary Queries whether the suggestion feature is enabled for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAdviceServiceEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdviceServiceEnabledResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdviceServiceEnabled',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAdviceServiceEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advice_service_enabled_with_options_async(
        self,
        request: adb_20190315_models.DescribeAdviceServiceEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAdviceServiceEnabledResponse:
        """
        @summary Queries whether the suggestion feature is enabled for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAdviceServiceEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdviceServiceEnabledResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdviceServiceEnabled',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAdviceServiceEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advice_service_enabled(
        self,
        request: adb_20190315_models.DescribeAdviceServiceEnabledRequest,
    ) -> adb_20190315_models.DescribeAdviceServiceEnabledResponse:
        """
        @summary Queries whether the suggestion feature is enabled for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAdviceServiceEnabledRequest
        @return: DescribeAdviceServiceEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advice_service_enabled_with_options(request, runtime)

    async def describe_advice_service_enabled_async(
        self,
        request: adb_20190315_models.DescribeAdviceServiceEnabledRequest,
    ) -> adb_20190315_models.DescribeAdviceServiceEnabledResponse:
        """
        @summary Queries whether the suggestion feature is enabled for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAdviceServiceEnabledRequest
        @return: DescribeAdviceServiceEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advice_service_enabled_with_options_async(request, runtime)

    def describe_all_accounts_with_options(
        self,
        request: adb_20190315_models.DescribeAllAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAllAccountsResponse:
        """
        @summary Queries the information about an account or the list of accounts of a specific database within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAllAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllAccounts',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_accounts_with_options_async(
        self,
        request: adb_20190315_models.DescribeAllAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAllAccountsResponse:
        """
        @summary Queries the information about an account or the list of accounts of a specific database within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAllAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllAccounts',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_accounts(
        self,
        request: adb_20190315_models.DescribeAllAccountsRequest,
    ) -> adb_20190315_models.DescribeAllAccountsResponse:
        """
        @summary Queries the information about an account or the list of accounts of a specific database within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAllAccountsRequest
        @return: DescribeAllAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_accounts_with_options(request, runtime)

    async def describe_all_accounts_async(
        self,
        request: adb_20190315_models.DescribeAllAccountsRequest,
    ) -> adb_20190315_models.DescribeAllAccountsResponse:
        """
        @summary Queries the information about an account or the list of accounts of a specific database within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAllAccountsRequest
        @return: DescribeAllAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_accounts_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: adb_20190315_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in a cluster.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: adb_20190315_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in a cluster.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: adb_20190315_models.DescribeAllDataSourceRequest,
    ) -> adb_20190315_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in a cluster.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: adb_20190315_models.DescribeAllDataSourceRequest,
    ) -> adb_20190315_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in a cluster.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_applied_advices_with_options(
        self,
        request: adb_20190315_models.DescribeAppliedAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAppliedAdvicesResponse:
        """
        @summary Queries the applied optimization suggestions for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAppliedAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppliedAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppliedAdvices',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAppliedAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_applied_advices_with_options_async(
        self,
        request: adb_20190315_models.DescribeAppliedAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAppliedAdvicesResponse:
        """
        @summary Queries the applied optimization suggestions for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAppliedAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppliedAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppliedAdvices',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAppliedAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_applied_advices(
        self,
        request: adb_20190315_models.DescribeAppliedAdvicesRequest,
    ) -> adb_20190315_models.DescribeAppliedAdvicesResponse:
        """
        @summary Queries the applied optimization suggestions for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAppliedAdvicesRequest
        @return: DescribeAppliedAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_applied_advices_with_options(request, runtime)

    async def describe_applied_advices_async(
        self,
        request: adb_20190315_models.DescribeAppliedAdvicesRequest,
    ) -> adb_20190315_models.DescribeAppliedAdvicesResponse:
        """
        @summary Queries the applied optimization suggestions for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAppliedAdvicesRequest
        @return: DescribeAppliedAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_applied_advices_with_options_async(request, runtime)

    def describe_audit_log_config_with_options(
        self,
        request: adb_20190315_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the SQL audit settings of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeAuditLogConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_config_with_options_async(
        self,
        request: adb_20190315_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the SQL audit settings of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeAuditLogConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_config(
        self,
        request: adb_20190315_models.DescribeAuditLogConfigRequest,
    ) -> adb_20190315_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the SQL audit settings of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAuditLogConfigRequest
        @return: DescribeAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    async def describe_audit_log_config_async(
        self,
        request: adb_20190315_models.DescribeAuditLogConfigRequest,
    ) -> adb_20190315_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the SQL audit settings of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeAuditLogConfigRequest
        @return: DescribeAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_config_with_options_async(request, runtime)

    def describe_audit_log_records_with_options(
        self,
        request: adb_20190315_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL cluster.
        
        @description Before you call the DescribeAuditLogRecords operation to query the SQL audit logs of an AnalyticDB for MySQL cluster, you must enable SQL audit for the cluster. You can call the [DescribeAuditLogConfig](https://help.aliyun.com/document_detail/190628.html) operation to query the status of SQL audit. If SQL audit is disabled, you can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/190629.html) operation to enable SQL audit.
        SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: *INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        
        @param request: DescribeAuditLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.succeed):
            query['Succeed'] = request.succeed
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL cluster.
        
        @description Before you call the DescribeAuditLogRecords operation to query the SQL audit logs of an AnalyticDB for MySQL cluster, you must enable SQL audit for the cluster. You can call the [DescribeAuditLogConfig](https://help.aliyun.com/document_detail/190628.html) operation to query the status of SQL audit. If SQL audit is disabled, you can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/190629.html) operation to enable SQL audit.
        SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: *INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        
        @param request: DescribeAuditLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.succeed):
            query['Succeed'] = request.succeed
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAuditLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_records(
        self,
        request: adb_20190315_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20190315_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL cluster.
        
        @description Before you call the DescribeAuditLogRecords operation to query the SQL audit logs of an AnalyticDB for MySQL cluster, you must enable SQL audit for the cluster. You can call the [DescribeAuditLogConfig](https://help.aliyun.com/document_detail/190628.html) operation to query the status of SQL audit. If SQL audit is disabled, you can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/190629.html) operation to enable SQL audit.
        SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: *INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        
        @param request: DescribeAuditLogRecordsRequest
        @return: DescribeAuditLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_records_with_options(request, runtime)

    async def describe_audit_log_records_async(
        self,
        request: adb_20190315_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20190315_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL cluster.
        
        @description Before you call the DescribeAuditLogRecords operation to query the SQL audit logs of an AnalyticDB for MySQL cluster, you must enable SQL audit for the cluster. You can call the [DescribeAuditLogConfig](https://help.aliyun.com/document_detail/190628.html) operation to query the status of SQL audit. If SQL audit is disabled, you can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/190629.html) operation to enable SQL audit.
        SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: *INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        
        @param request: DescribeAuditLogRecordsRequest
        @return: DescribeAuditLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_records_with_options_async(request, runtime)

    def describe_auto_renew_attribute_with_options(
        self,
        request: adb_20190315_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoRenewAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_renew_attribute_with_options_async(
        self,
        request: adb_20190315_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoRenewAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_renew_attribute(
        self,
        request: adb_20190315_models.DescribeAutoRenewAttributeRequest,
    ) -> adb_20190315_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @return: DescribeAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    async def describe_auto_renew_attribute_async(
        self,
        request: adb_20190315_models.DescribeAutoRenewAttributeRequest,
    ) -> adb_20190315_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @return: DescribeAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_renew_attribute_with_options_async(request, runtime)

    def describe_available_advices_with_options(
        self,
        request: adb_20190315_models.DescribeAvailableAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAvailableAdvicesResponse:
        """
        @summary Queries the available suggestions for cluster optimization.
        
        @param request: DescribeAvailableAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableAdvices',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAvailableAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_advices_with_options_async(
        self,
        request: adb_20190315_models.DescribeAvailableAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAvailableAdvicesResponse:
        """
        @summary Queries the available suggestions for cluster optimization.
        
        @param request: DescribeAvailableAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not UtilClient.is_unset(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableAdvices',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAvailableAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_advices(
        self,
        request: adb_20190315_models.DescribeAvailableAdvicesRequest,
    ) -> adb_20190315_models.DescribeAvailableAdvicesResponse:
        """
        @summary Queries the available suggestions for cluster optimization.
        
        @param request: DescribeAvailableAdvicesRequest
        @return: DescribeAvailableAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_advices_with_options(request, runtime)

    async def describe_available_advices_async(
        self,
        request: adb_20190315_models.DescribeAvailableAdvicesRequest,
    ) -> adb_20190315_models.DescribeAvailableAdvicesResponse:
        """
        @summary Queries the available suggestions for cluster optimization.
        
        @param request: DescribeAvailableAdvicesRequest
        @return: DescribeAvailableAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_advices_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: adb_20190315_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the resources of clusters within zones of a region.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: adb_20190315_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the resources of clusters within zones of a region.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: adb_20190315_models.DescribeAvailableResourceRequest,
    ) -> adb_20190315_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the resources of clusters within zones of a region.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: adb_20190315_models.DescribeAvailableResourceRequest,
    ) -> adb_20190315_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the resources of clusters within zones of a region.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: adb_20190315_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBackupPolicyResponse:
        """
        @summary 查看备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: adb_20190315_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBackupPolicyResponse:
        """
        @summary 查看备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: adb_20190315_models.DescribeBackupPolicyRequest,
    ) -> adb_20190315_models.DescribeBackupPolicyResponse:
        """
        @summary 查看备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: adb_20190315_models.DescribeBackupPolicyRequest,
    ) -> adb_20190315_models.DescribeBackupPolicyResponse:
        """
        @summary 查看备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: adb_20190315_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBackupsResponse:
        """
        @summary Queries a list of backup sets for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cross_role):
            query['CrossRole'] = request.cross_role
        if not UtilClient.is_unset(request.cross_uid):
            query['CrossUid'] = request.cross_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeBackups',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: adb_20190315_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBackupsResponse:
        """
        @summary Queries a list of backup sets for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cross_role):
            query['CrossRole'] = request.cross_role
        if not UtilClient.is_unset(request.cross_uid):
            query['CrossUid'] = request.cross_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeBackups',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: adb_20190315_models.DescribeBackupsRequest,
    ) -> adb_20190315_models.DescribeBackupsResponse:
        """
        @summary Queries a list of backup sets for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: adb_20190315_models.DescribeBackupsRequest,
    ) -> adb_20190315_models.DescribeBackupsResponse:
        """
        @summary Queries a list of backup sets for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_bad_sql_detection_with_options(
        self,
        request: adb_20190315_models.DescribeBadSqlDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBadSqlDetectionResponse:
        """
        @summary Queries the bad SQL statements that affect cluster stability within a time range.
        
        @param request: DescribeBadSqlDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBadSqlDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBadSqlDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBadSqlDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bad_sql_detection_with_options_async(
        self,
        request: adb_20190315_models.DescribeBadSqlDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeBadSqlDetectionResponse:
        """
        @summary Queries the bad SQL statements that affect cluster stability within a time range.
        
        @param request: DescribeBadSqlDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBadSqlDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBadSqlDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeBadSqlDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bad_sql_detection(
        self,
        request: adb_20190315_models.DescribeBadSqlDetectionRequest,
    ) -> adb_20190315_models.DescribeBadSqlDetectionResponse:
        """
        @summary Queries the bad SQL statements that affect cluster stability within a time range.
        
        @param request: DescribeBadSqlDetectionRequest
        @return: DescribeBadSqlDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_bad_sql_detection_with_options(request, runtime)

    async def describe_bad_sql_detection_async(
        self,
        request: adb_20190315_models.DescribeBadSqlDetectionRequest,
    ) -> adb_20190315_models.DescribeBadSqlDetectionResponse:
        """
        @summary Queries the bad SQL statements that affect cluster stability within a time range.
        
        @param request: DescribeBadSqlDetectionRequest
        @return: DescribeBadSqlDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_bad_sql_detection_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: adb_20190315_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: adb_20190315_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: adb_20190315_models.DescribeColumnsRequest,
    ) -> adb_20190315_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: adb_20190315_models.DescribeColumnsRequest,
    ) -> adb_20190315_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table within an AnalyticDB for MySQL cluster.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_compute_resource_with_options(
        self,
        request: adb_20190315_models.DescribeComputeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeComputeResourceResponse:
        """
        @summary Queries the specifications of computing resources for AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeComputeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComputeResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.migrate):
            query['Migrate'] = request.migrate
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeResource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compute_resource_with_options_async(
        self,
        request: adb_20190315_models.DescribeComputeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeComputeResourceResponse:
        """
        @summary Queries the specifications of computing resources for AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeComputeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComputeResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.migrate):
            query['Migrate'] = request.migrate
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeResource',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compute_resource(
        self,
        request: adb_20190315_models.DescribeComputeResourceRequest,
    ) -> adb_20190315_models.DescribeComputeResourceResponse:
        """
        @summary Queries the specifications of computing resources for AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeComputeResourceRequest
        @return: DescribeComputeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_compute_resource_with_options(request, runtime)

    async def describe_compute_resource_async(
        self,
        request: adb_20190315_models.DescribeComputeResourceRequest,
    ) -> adb_20190315_models.DescribeComputeResourceResponse:
        """
        @summary Queries the specifications of computing resources for AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeComputeResourceRequest
        @return: DescribeComputeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_compute_resource_with_options_async(request, runtime)

    def describe_connection_count_records_with_options(
        self,
        request: adb_20190315_models.DescribeConnectionCountRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeConnectionCountRecordsResponse:
        """
        @summary Queries the current number of connections to an AnalyticDB for MySQL cluster.
        
        @param request: DescribeConnectionCountRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConnectionCountRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionCountRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeConnectionCountRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_connection_count_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeConnectionCountRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeConnectionCountRecordsResponse:
        """
        @summary Queries the current number of connections to an AnalyticDB for MySQL cluster.
        
        @param request: DescribeConnectionCountRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConnectionCountRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionCountRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeConnectionCountRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_connection_count_records(
        self,
        request: adb_20190315_models.DescribeConnectionCountRecordsRequest,
    ) -> adb_20190315_models.DescribeConnectionCountRecordsResponse:
        """
        @summary Queries the current number of connections to an AnalyticDB for MySQL cluster.
        
        @param request: DescribeConnectionCountRecordsRequest
        @return: DescribeConnectionCountRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_count_records_with_options(request, runtime)

    async def describe_connection_count_records_async(
        self,
        request: adb_20190315_models.DescribeConnectionCountRecordsRequest,
    ) -> adb_20190315_models.DescribeConnectionCountRecordsResponse:
        """
        @summary Queries the current number of connections to an AnalyticDB for MySQL cluster.
        
        @param request: DescribeConnectionCountRecordsRequest
        @return: DescribeConnectionCountRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_connection_count_records_with_options_async(request, runtime)

    def describe_controller_detection_with_options(
        self,
        request: adb_20190315_models.DescribeControllerDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeControllerDetectionResponse:
        """
        @summary Queries the diagnostic results of the access layer.
        
        @param request: DescribeControllerDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeControllerDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeControllerDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeControllerDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_controller_detection_with_options_async(
        self,
        request: adb_20190315_models.DescribeControllerDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeControllerDetectionResponse:
        """
        @summary Queries the diagnostic results of the access layer.
        
        @param request: DescribeControllerDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeControllerDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeControllerDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeControllerDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_controller_detection(
        self,
        request: adb_20190315_models.DescribeControllerDetectionRequest,
    ) -> adb_20190315_models.DescribeControllerDetectionResponse:
        """
        @summary Queries the diagnostic results of the access layer.
        
        @param request: DescribeControllerDetectionRequest
        @return: DescribeControllerDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_controller_detection_with_options(request, runtime)

    async def describe_controller_detection_async(
        self,
        request: adb_20190315_models.DescribeControllerDetectionRequest,
    ) -> adb_20190315_models.DescribeControllerDetectionResponse:
        """
        @summary Queries the diagnostic results of the access layer.
        
        @param request: DescribeControllerDetectionRequest
        @return: DescribeControllerDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_controller_detection_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries a list of IP address whitelists for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterAccessWhiteList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries a list of IP address whitelists for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterAccessWhiteList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: adb_20190315_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> adb_20190315_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries a list of IP address whitelists for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: adb_20190315_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> adb_20190315_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries a list of IP address whitelists for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: adb_20190315_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20190315_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: adb_20190315_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20190315_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_health_status_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary 查询集群健康检查状态
        
        @param request: DescribeDBClusterHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterHealthStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_health_status_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary 查询集群健康检查状态
        
        @param request: DescribeDBClusterHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterHealthStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_health_status(
        self,
        request: adb_20190315_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20190315_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary 查询集群健康检查状态
        
        @param request: DescribeDBClusterHealthStatusRequest
        @return: DescribeDBClusterHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_health_status_with_options(request, runtime)

    async def describe_dbcluster_health_status_async(
        self,
        request: adb_20190315_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20190315_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary 查询集群健康检查状态
        
        @param request: DescribeDBClusterHealthStatusRequest
        @return: DescribeDBClusterHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_health_status_with_options_async(request, runtime)

    def describe_dbcluster_net_info_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
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
            action='DescribeDBClusterNetInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_net_info_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
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
            action='DescribeDBClusterNetInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_net_info(
        self,
        request: adb_20190315_models.DescribeDBClusterNetInfoRequest,
    ) -> adb_20190315_models.DescribeDBClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterNetInfoRequest
        @return: DescribeDBClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_with_options(request, runtime)

    async def describe_dbcluster_net_info_async(
        self,
        request: adb_20190315_models.DescribeDBClusterNetInfoRequest,
    ) -> adb_20190315_models.DescribeDBClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterNetInfoRequest
        @return: DescribeDBClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_net_info_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description You can call this operation to query the performance data of a cluster over a time range based on its performance metrics. The data is collected every 30 seconds. This operation allows you to query information about slow queries, such as the SQL query duration, number of scanned rows, and amount of scanned data.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
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
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description You can call this operation to query the performance data of a cluster over a time range based on its performance metrics. The data is collected every 30 seconds. This operation allows you to query information about slow queries, such as the SQL query duration, number of scanned rows, and amount of scanned data.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
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
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: adb_20190315_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20190315_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description You can call this operation to query the performance data of a cluster over a time range based on its performance metrics. The data is collected every 30 seconds. This operation allows you to query information about slow queries, such as the SQL query duration, number of scanned rows, and amount of scanned data.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: adb_20190315_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20190315_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description You can call this operation to query the performance data of a cluster over a time range based on its performance metrics. The data is collected every 30 seconds. This operation allows you to query information about slow queries, such as the SQL query duration, number of scanned rows, and amount of scanned data.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbcluster_resource_pool_performance_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterResourcePoolPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse:
        """
        @summary Queries the monitoring information about resource groups within an AnalyticDB for MySQL cluster.
        
        @description > You can also view the monitoring information about resource groups within an AnalyticDB for MySQL cluster in elastic mode for Cluster Edition in the form of graphs in the console. For more information, see [View monitoring information](https://help.aliyun.com/document_detail/188721.html).
        
        @param request: DescribeDBClusterResourcePoolPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterResourcePoolPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterResourcePoolPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_resource_pool_performance_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterResourcePoolPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse:
        """
        @summary Queries the monitoring information about resource groups within an AnalyticDB for MySQL cluster.
        
        @description > You can also view the monitoring information about resource groups within an AnalyticDB for MySQL cluster in elastic mode for Cluster Edition in the form of graphs in the console. For more information, see [View monitoring information](https://help.aliyun.com/document_detail/188721.html).
        
        @param request: DescribeDBClusterResourcePoolPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterResourcePoolPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterResourcePoolPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_resource_pool_performance(
        self,
        request: adb_20190315_models.DescribeDBClusterResourcePoolPerformanceRequest,
    ) -> adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse:
        """
        @summary Queries the monitoring information about resource groups within an AnalyticDB for MySQL cluster.
        
        @description > You can also view the monitoring information about resource groups within an AnalyticDB for MySQL cluster in elastic mode for Cluster Edition in the form of graphs in the console. For more information, see [View monitoring information](https://help.aliyun.com/document_detail/188721.html).
        
        @param request: DescribeDBClusterResourcePoolPerformanceRequest
        @return: DescribeDBClusterResourcePoolPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_resource_pool_performance_with_options(request, runtime)

    async def describe_dbcluster_resource_pool_performance_async(
        self,
        request: adb_20190315_models.DescribeDBClusterResourcePoolPerformanceRequest,
    ) -> adb_20190315_models.DescribeDBClusterResourcePoolPerformanceResponse:
        """
        @summary Queries the monitoring information about resource groups within an AnalyticDB for MySQL cluster.
        
        @description > You can also view the monitoring information about resource groups within an AnalyticDB for MySQL cluster in elastic mode for Cluster Edition in the form of graphs in the console. For more information, see [View monitoring information](https://help.aliyun.com/document_detail/188721.html).
        
        @param request: DescribeDBClusterResourcePoolPerformanceRequest
        @return: DescribeDBClusterResourcePoolPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_resource_pool_performance_with_options_async(request, runtime)

    def describe_dbcluster_sslwith_options(
        self,
        request: adb_20190315_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterSSL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_sslwith_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterSSL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_ssl(
        self,
        request: adb_20190315_models.DescribeDBClusterSSLRequest,
    ) -> adb_20190315_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @return: DescribeDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_sslwith_options(request, runtime)

    async def describe_dbcluster_ssl_async(
        self,
        request: adb_20190315_models.DescribeDBClusterSSLRequest,
    ) -> adb_20190315_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @return: DescribeDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_sslwith_options_async(request, runtime)

    def describe_dbcluster_shard_number_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterShardNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterShardNumberResponse:
        """
        @summary Queries the number of shards in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterShardNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterShardNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterShardNumber',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterShardNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_shard_number_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterShardNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterShardNumberResponse:
        """
        @summary Queries the number of shards in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterShardNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterShardNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeDBClusterShardNumber',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterShardNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_shard_number(
        self,
        request: adb_20190315_models.DescribeDBClusterShardNumberRequest,
    ) -> adb_20190315_models.DescribeDBClusterShardNumberResponse:
        """
        @summary Queries the number of shards in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterShardNumberRequest
        @return: DescribeDBClusterShardNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_shard_number_with_options(request, runtime)

    async def describe_dbcluster_shard_number_async(
        self,
        request: adb_20190315_models.DescribeDBClusterShardNumberRequest,
    ) -> adb_20190315_models.DescribeDBClusterShardNumberResponse:
        """
        @summary Queries the number of shards in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDBClusterShardNumberRequest
        @return: DescribeDBClusterShardNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_shard_number_with_options_async(request, runtime)

    def describe_dbcluster_space_summary_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterSpaceSummary',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterSpaceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_space_summary_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterSpaceSummary',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterSpaceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_space_summary(
        self,
        request: adb_20190315_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> adb_20190315_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_space_summary_with_options(request, runtime)

    async def describe_dbcluster_space_summary_async(
        self,
        request: adb_20190315_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> adb_20190315_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_space_summary_with_options_async(request, runtime)

    def describe_dbcluster_status_with_options(
        self,
        request: adb_20190315_models.DescribeDBClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries the status of AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeDBClusterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDBClusterStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_status_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries the status of AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeDBClusterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDBClusterStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClusterStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_status(
        self,
        request: adb_20190315_models.DescribeDBClusterStatusRequest,
    ) -> adb_20190315_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries the status of AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeDBClusterStatusRequest
        @return: DescribeDBClusterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_status_with_options(request, runtime)

    async def describe_dbcluster_status_async(
        self,
        request: adb_20190315_models.DescribeDBClusterStatusRequest,
    ) -> adb_20190315_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries the status of AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        
        @param request: DescribeDBClusterStatusRequest
        @return: DescribeDBClusterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_status_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: adb_20190315_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClustersResponse:
        """
        @summary Queries a list of AnalyticDB for MySQL clusters within a region.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBClustersResponse:
        """
        @summary Queries a list of AnalyticDB for MySQL clusters within a region.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: adb_20190315_models.DescribeDBClustersRequest,
    ) -> adb_20190315_models.DescribeDBClustersResponse:
        """
        @summary Queries a list of AnalyticDB for MySQL clusters within a region.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: adb_20190315_models.DescribeDBClustersRequest,
    ) -> adb_20190315_models.DescribeDBClustersResponse:
        """
        @summary Queries a list of AnalyticDB for MySQL clusters within a region.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: adb_20190315_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: DescribeDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_group_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: DescribeDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_group(
        self,
        request: adb_20190315_models.DescribeDBResourceGroupRequest,
    ) -> adb_20190315_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: adb_20190315_models.DescribeDBResourceGroupRequest,
    ) -> adb_20190315_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about a resource group for an AnalyticDB for MySQL cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more.
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_dbresource_pool_with_options(
        self,
        request: adb_20190315_models.DescribeDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBResourcePoolResponse:
        """
        @summary 查询资源组详情
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: DescribeDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_pool_with_options_async(
        self,
        request: adb_20190315_models.DescribeDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDBResourcePoolResponse:
        """
        @summary 查询资源组详情
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: DescribeDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_pool(
        self,
        request: adb_20190315_models.DescribeDBResourcePoolRequest,
    ) -> adb_20190315_models.DescribeDBResourcePoolResponse:
        """
        @summary 查询资源组详情
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: DescribeDBResourcePoolRequest
        @return: DescribeDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_pool_with_options(request, runtime)

    async def describe_dbresource_pool_async(
        self,
        request: adb_20190315_models.DescribeDBResourcePoolRequest,
    ) -> adb_20190315_models.DescribeDBResourcePoolResponse:
        """
        @summary 查询资源组详情
        
        @description This operation is applicable only for elastic clusters of 32 cores or more.
        
        @param request: DescribeDBResourcePoolRequest
        @return: DescribeDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbresource_pool_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: adb_20190315_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of SQL statements that meet a condition of the resource group, database, username, and source IP address in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisDimensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of SQL statements that meet a condition of the resource group, database, username, and source IP address in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisDimensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: adb_20190315_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20190315_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of SQL statements that meet a condition of the resource group, database, username, and source IP address in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20190315_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of SQL statements that meet a condition of the resource group, database, username, and source IP address in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(
        self,
        request: adb_20190315_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        @summary Queries the monitoring information about queries within a time range.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisMonitorPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_monitor_performance_with_options_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        @summary Queries the monitoring information about queries within a time range.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisMonitorPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_monitor_performance(
        self,
        request: adb_20190315_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        @summary Queries the monitoring information about queries within a time range.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    async def describe_diagnosis_monitor_performance_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> adb_20190315_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        @summary Queries the monitoring information about queries within a time range.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_monitor_performance_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: adb_20190315_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a condition in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a condition in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: adb_20190315_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20190315_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a condition in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20190315_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a condition in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: adb_20190315_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: adb_20190315_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20190315_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20190315_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_diagnosis_tasks_with_options(
        self,
        request: adb_20190315_models.DescribeDiagnosisTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisTasksResponse:
        """
        @summary Queries the execution information about distributed tasks in a stage of a query.
        
        @param request: DescribeDiagnosisTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_tasks_with_options_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDiagnosisTasksResponse:
        """
        @summary Queries the execution information about distributed tasks in a stage of a query.
        
        @param request: DescribeDiagnosisTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDiagnosisTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_tasks(
        self,
        request: adb_20190315_models.DescribeDiagnosisTasksRequest,
    ) -> adb_20190315_models.DescribeDiagnosisTasksResponse:
        """
        @summary Queries the execution information about distributed tasks in a stage of a query.
        
        @param request: DescribeDiagnosisTasksRequest
        @return: DescribeDiagnosisTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_tasks_with_options(request, runtime)

    async def describe_diagnosis_tasks_async(
        self,
        request: adb_20190315_models.DescribeDiagnosisTasksRequest,
    ) -> adb_20190315_models.DescribeDiagnosisTasksResponse:
        """
        @summary Queries the execution information about distributed tasks in a stage of a query.
        
        @param request: DescribeDiagnosisTasksRequest
        @return: DescribeDiagnosisTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_tasks_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: adb_20190315_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries a list of download tasks for the last five SQL queries of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDownloadRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries a list of download tasks for the last five SQL queries of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDownloadRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: adb_20190315_models.DescribeDownloadRecordsRequest,
    ) -> adb_20190315_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries a list of download tasks for the last five SQL queries of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: adb_20190315_models.DescribeDownloadRecordsRequest,
    ) -> adb_20190315_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries a list of download tasks for the last five SQL queries of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_eiurange_with_options(
        self,
        request: adb_20190315_models.DescribeEIURangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeEIURangeResponse:
        """
        @summary Queries the range for the number of elastic I/O units (EIUs) for an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeEIURangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEIURangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEIURange',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeEIURangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eiurange_with_options_async(
        self,
        request: adb_20190315_models.DescribeEIURangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeEIURangeResponse:
        """
        @summary Queries the range for the number of elastic I/O units (EIUs) for an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeEIURangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEIURangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEIURange',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeEIURangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eiurange(
        self,
        request: adb_20190315_models.DescribeEIURangeRequest,
    ) -> adb_20190315_models.DescribeEIURangeResponse:
        """
        @summary Queries the range for the number of elastic I/O units (EIUs) for an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeEIURangeRequest
        @return: DescribeEIURangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_eiurange_with_options(request, runtime)

    async def describe_eiurange_async(
        self,
        request: adb_20190315_models.DescribeEIURangeRequest,
    ) -> adb_20190315_models.DescribeEIURangeResponse:
        """
        @summary Queries the range for the number of elastic I/O units (EIUs) for an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeEIURangeRequest
        @return: DescribeEIURangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_eiurange_with_options_async(request, runtime)

    def describe_elastic_daily_plan_with_options(
        self,
        request: adb_20190315_models.DescribeElasticDailyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeElasticDailyPlanResponse:
        """
        @summary 查看日资源弹性
        
        @description This operation is available only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticDailyPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticDailyPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_daily_plan_day):
            query['ElasticDailyPlanDay'] = request.elastic_daily_plan_day
        if not UtilClient.is_unset(request.elastic_daily_plan_status_list):
            query['ElasticDailyPlanStatusList'] = request.elastic_daily_plan_status_list
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticDailyPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticDailyPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_daily_plan_with_options_async(
        self,
        request: adb_20190315_models.DescribeElasticDailyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeElasticDailyPlanResponse:
        """
        @summary 查看日资源弹性
        
        @description This operation is available only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticDailyPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticDailyPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_daily_plan_day):
            query['ElasticDailyPlanDay'] = request.elastic_daily_plan_day
        if not UtilClient.is_unset(request.elastic_daily_plan_status_list):
            query['ElasticDailyPlanStatusList'] = request.elastic_daily_plan_status_list
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticDailyPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticDailyPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_daily_plan(
        self,
        request: adb_20190315_models.DescribeElasticDailyPlanRequest,
    ) -> adb_20190315_models.DescribeElasticDailyPlanResponse:
        """
        @summary 查看日资源弹性
        
        @description This operation is available only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticDailyPlanRequest
        @return: DescribeElasticDailyPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_daily_plan_with_options(request, runtime)

    async def describe_elastic_daily_plan_async(
        self,
        request: adb_20190315_models.DescribeElasticDailyPlanRequest,
    ) -> adb_20190315_models.DescribeElasticDailyPlanResponse:
        """
        @summary 查看日资源弹性
        
        @description This operation is available only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticDailyPlanRequest
        @return: DescribeElasticDailyPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_daily_plan_with_options_async(request, runtime)

    def describe_elastic_plan_with_options(
        self,
        request: adb_20190315_models.DescribeElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeElasticPlanResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL cluster. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_with_options_async(
        self,
        request: adb_20190315_models.DescribeElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeElasticPlanResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL cluster. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan(
        self,
        request: adb_20190315_models.DescribeElasticPlanRequest,
    ) -> adb_20190315_models.DescribeElasticPlanResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL cluster. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticPlanRequest
        @return: DescribeElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plan_with_options(request, runtime)

    async def describe_elastic_plan_async(
        self,
        request: adb_20190315_models.DescribeElasticPlanRequest,
    ) -> adb_20190315_models.DescribeElasticPlanResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL cluster. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: DescribeElasticPlanRequest
        @return: DescribeElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_plan_with_options_async(request, runtime)

    def describe_excessive_primary_keys_with_options(
        self,
        request: adb_20190315_models.DescribeExcessivePrimaryKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the tables that have excessive primary key fields in an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExcessivePrimaryKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
            action='DescribeExcessivePrimaryKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeExcessivePrimaryKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excessive_primary_keys_with_options_async(
        self,
        request: adb_20190315_models.DescribeExcessivePrimaryKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the tables that have excessive primary key fields in an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExcessivePrimaryKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
            action='DescribeExcessivePrimaryKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeExcessivePrimaryKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excessive_primary_keys(
        self,
        request: adb_20190315_models.DescribeExcessivePrimaryKeysRequest,
    ) -> adb_20190315_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the tables that have excessive primary key fields in an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @return: DescribeExcessivePrimaryKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_excessive_primary_keys_with_options(request, runtime)

    async def describe_excessive_primary_keys_async(
        self,
        request: adb_20190315_models.DescribeExcessivePrimaryKeysRequest,
    ) -> adb_20190315_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the tables that have excessive primary key fields in an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @return: DescribeExcessivePrimaryKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_excessive_primary_keys_with_options_async(request, runtime)

    def describe_executor_detection_with_options(
        self,
        request: adb_20190315_models.DescribeExecutorDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeExecutorDetectionResponse:
        """
        @summary Queries the diagnostic results of the compute layer.
        
        @param request: DescribeExecutorDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutorDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutorDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeExecutorDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_executor_detection_with_options_async(
        self,
        request: adb_20190315_models.DescribeExecutorDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeExecutorDetectionResponse:
        """
        @summary Queries the diagnostic results of the compute layer.
        
        @param request: DescribeExecutorDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutorDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutorDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeExecutorDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_executor_detection(
        self,
        request: adb_20190315_models.DescribeExecutorDetectionRequest,
    ) -> adb_20190315_models.DescribeExecutorDetectionResponse:
        """
        @summary Queries the diagnostic results of the compute layer.
        
        @param request: DescribeExecutorDetectionRequest
        @return: DescribeExecutorDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_executor_detection_with_options(request, runtime)

    async def describe_executor_detection_async(
        self,
        request: adb_20190315_models.DescribeExecutorDetectionRequest,
    ) -> adb_20190315_models.DescribeExecutorDetectionResponse:
        """
        @summary Queries the diagnostic results of the compute layer.
        
        @param request: DescribeExecutorDetectionRequest
        @return: DescribeExecutorDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_executor_detection_with_options_async(request, runtime)

    def describe_history_events_stat_with_options(
        self,
        request: adb_20190315_models.DescribeHistoryEventsStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeHistoryEventsStatResponse:
        """
        @summary Queries the information about historical events in the event center.
        
        @param request: DescribeHistoryEventsStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryEventsStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.archive_status):
            query['ArchiveStatus'] = request.archive_status
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryEventsStat',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeHistoryEventsStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_events_stat_with_options_async(
        self,
        request: adb_20190315_models.DescribeHistoryEventsStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeHistoryEventsStatResponse:
        """
        @summary Queries the information about historical events in the event center.
        
        @param request: DescribeHistoryEventsStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryEventsStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.archive_status):
            query['ArchiveStatus'] = request.archive_status
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryEventsStat',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeHistoryEventsStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_events_stat(
        self,
        request: adb_20190315_models.DescribeHistoryEventsStatRequest,
    ) -> adb_20190315_models.DescribeHistoryEventsStatResponse:
        """
        @summary Queries the information about historical events in the event center.
        
        @param request: DescribeHistoryEventsStatRequest
        @return: DescribeHistoryEventsStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_history_events_stat_with_options(request, runtime)

    async def describe_history_events_stat_async(
        self,
        request: adb_20190315_models.DescribeHistoryEventsStatRequest,
    ) -> adb_20190315_models.DescribeHistoryEventsStatResponse:
        """
        @summary Queries the information about historical events in the event center.
        
        @param request: DescribeHistoryEventsStatRequest
        @return: DescribeHistoryEventsStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_events_stat_with_options_async(request, runtime)

    def describe_inclined_nodes_with_options(
        self,
        request: adb_20190315_models.DescribeInclinedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeInclinedNodesResponse:
        """
        @summary Queries the disk usage of all storage nodes.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeInclinedNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInclinedNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
            action='DescribeInclinedNodes',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeInclinedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inclined_nodes_with_options_async(
        self,
        request: adb_20190315_models.DescribeInclinedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeInclinedNodesResponse:
        """
        @summary Queries the disk usage of all storage nodes.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeInclinedNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInclinedNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
            action='DescribeInclinedNodes',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeInclinedNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inclined_nodes(
        self,
        request: adb_20190315_models.DescribeInclinedNodesRequest,
    ) -> adb_20190315_models.DescribeInclinedNodesResponse:
        """
        @summary Queries the disk usage of all storage nodes.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeInclinedNodesRequest
        @return: DescribeInclinedNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_inclined_nodes_with_options(request, runtime)

    async def describe_inclined_nodes_async(
        self,
        request: adb_20190315_models.DescribeInclinedNodesRequest,
    ) -> adb_20190315_models.DescribeInclinedNodesResponse:
        """
        @summary Queries the disk usage of all storage nodes.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeInclinedNodesRequest
        @return: DescribeInclinedNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_inclined_nodes_with_options_async(request, runtime)

    def describe_inclined_tables_with_options(
        self,
        request: adb_20190315_models.DescribeInclinedTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeInclinedTablesResponse:
        """
        @summary Queries the information about skewed tables for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeInclinedTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInclinedTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInclinedTables',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeInclinedTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inclined_tables_with_options_async(
        self,
        request: adb_20190315_models.DescribeInclinedTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeInclinedTablesResponse:
        """
        @summary Queries the information about skewed tables for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeInclinedTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInclinedTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInclinedTables',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeInclinedTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inclined_tables(
        self,
        request: adb_20190315_models.DescribeInclinedTablesRequest,
    ) -> adb_20190315_models.DescribeInclinedTablesResponse:
        """
        @summary Queries the information about skewed tables for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeInclinedTablesRequest
        @return: DescribeInclinedTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_inclined_tables_with_options(request, runtime)

    async def describe_inclined_tables_async(
        self,
        request: adb_20190315_models.DescribeInclinedTablesRequest,
    ) -> adb_20190315_models.DescribeInclinedTablesResponse:
        """
        @summary Queries the information about skewed tables for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeInclinedTablesRequest
        @return: DescribeInclinedTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_inclined_tables_with_options_async(request, runtime)

    def describe_kernel_version_with_options(
        self,
        request: adb_20190315_models.DescribeKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeKernelVersionResponse:
        """
        @summary Queries the information about the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeKernelVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kernel_version_with_options_async(
        self,
        request: adb_20190315_models.DescribeKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeKernelVersionResponse:
        """
        @summary Queries the information about the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='DescribeKernelVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kernel_version(
        self,
        request: adb_20190315_models.DescribeKernelVersionRequest,
    ) -> adb_20190315_models.DescribeKernelVersionResponse:
        """
        @summary Queries the information about the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeKernelVersionRequest
        @return: DescribeKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_kernel_version_with_options(request, runtime)

    async def describe_kernel_version_async(
        self,
        request: adb_20190315_models.DescribeKernelVersionRequest,
    ) -> adb_20190315_models.DescribeKernelVersionResponse:
        """
        @summary Queries the information about the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeKernelVersionRequest
        @return: DescribeKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_kernel_version_with_options_async(request, runtime)

    def describe_kms_keys_with_options(
        self,
        request: adb_20190315_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeKmsKeysResponse:
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        
        @param request: DescribeKmsKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKmsKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_keys_with_options_async(
        self,
        request: adb_20190315_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeKmsKeysResponse:
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        
        @param request: DescribeKmsKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKmsKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_keys(
        self,
        request: adb_20190315_models.DescribeKmsKeysRequest,
    ) -> adb_20190315_models.DescribeKmsKeysResponse:
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        
        @param request: DescribeKmsKeysRequest
        @return: DescribeKmsKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    async def describe_kms_keys_async(
        self,
        request: adb_20190315_models.DescribeKmsKeysRequest,
    ) -> adb_20190315_models.DescribeKmsKeysResponse:
        """
        @summary Queries a list of Key Management Service (KMS) keys.
        
        @param request: DescribeKmsKeysRequest
        @return: DescribeKmsKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_kms_keys_with_options_async(request, runtime)

    def describe_load_tasks_records_with_options(
        self,
        request: adb_20190315_models.DescribeLoadTasksRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLoadTasksRecordsResponse:
        """
        @summary Queries the information about asynchronous import and export tasks of an AnalyticDB for MySQL cluster.
        
        @description For information about how to asynchronously submit import and export tasks, see [Asynchronously submit an import or export task](https://help.aliyun.com/document_detail/160291.html).
        
        @param request: DescribeLoadTasksRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadTasksRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadTasksRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLoadTasksRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_tasks_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeLoadTasksRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLoadTasksRecordsResponse:
        """
        @summary Queries the information about asynchronous import and export tasks of an AnalyticDB for MySQL cluster.
        
        @description For information about how to asynchronously submit import and export tasks, see [Asynchronously submit an import or export task](https://help.aliyun.com/document_detail/160291.html).
        
        @param request: DescribeLoadTasksRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadTasksRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadTasksRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLoadTasksRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_tasks_records(
        self,
        request: adb_20190315_models.DescribeLoadTasksRecordsRequest,
    ) -> adb_20190315_models.DescribeLoadTasksRecordsResponse:
        """
        @summary Queries the information about asynchronous import and export tasks of an AnalyticDB for MySQL cluster.
        
        @description For information about how to asynchronously submit import and export tasks, see [Asynchronously submit an import or export task](https://help.aliyun.com/document_detail/160291.html).
        
        @param request: DescribeLoadTasksRecordsRequest
        @return: DescribeLoadTasksRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_tasks_records_with_options(request, runtime)

    async def describe_load_tasks_records_async(
        self,
        request: adb_20190315_models.DescribeLoadTasksRecordsRequest,
    ) -> adb_20190315_models.DescribeLoadTasksRecordsResponse:
        """
        @summary Queries the information about asynchronous import and export tasks of an AnalyticDB for MySQL cluster.
        
        @description For information about how to asynchronously submit import and export tasks, see [Asynchronously submit an import or export task](https://help.aliyun.com/document_detail/160291.html).
        
        @param request: DescribeLoadTasksRecordsRequest
        @return: DescribeLoadTasksRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_tasks_records_with_options_async(request, runtime)

    def describe_log_hub_attribute_with_options(
        self,
        request: adb_20190315_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLogHubAttributeResponse:
        """
        @summary Queries the information about a log shipping job.
        
        @param request: DescribeLogHubAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogHubAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
            action='DescribeLogHubAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLogHubAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_hub_attribute_with_options_async(
        self,
        request: adb_20190315_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLogHubAttributeResponse:
        """
        @summary Queries the information about a log shipping job.
        
        @param request: DescribeLogHubAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogHubAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
            action='DescribeLogHubAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLogHubAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_hub_attribute(
        self,
        request: adb_20190315_models.DescribeLogHubAttributeRequest,
    ) -> adb_20190315_models.DescribeLogHubAttributeResponse:
        """
        @summary Queries the information about a log shipping job.
        
        @param request: DescribeLogHubAttributeRequest
        @return: DescribeLogHubAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    async def describe_log_hub_attribute_async(
        self,
        request: adb_20190315_models.DescribeLogHubAttributeRequest,
    ) -> adb_20190315_models.DescribeLogHubAttributeResponse:
        """
        @summary Queries the information about a log shipping job.
        
        @param request: DescribeLogHubAttributeRequest
        @return: DescribeLogHubAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_hub_attribute_with_options_async(request, runtime)

    def describe_log_store_keys_with_options(
        self,
        request: adb_20190315_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLogStoreKeysResponse:
        """
        @summary Queries a list of log keywords in a Logstore.
        
        @param request: DescribeLogStoreKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
            action='DescribeLogStoreKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLogStoreKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_keys_with_options_async(
        self,
        request: adb_20190315_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLogStoreKeysResponse:
        """
        @summary Queries a list of log keywords in a Logstore.
        
        @param request: DescribeLogStoreKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
            action='DescribeLogStoreKeys',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLogStoreKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_keys(
        self,
        request: adb_20190315_models.DescribeLogStoreKeysRequest,
    ) -> adb_20190315_models.DescribeLogStoreKeysResponse:
        """
        @summary Queries a list of log keywords in a Logstore.
        
        @param request: DescribeLogStoreKeysRequest
        @return: DescribeLogStoreKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    async def describe_log_store_keys_async(
        self,
        request: adb_20190315_models.DescribeLogStoreKeysRequest,
    ) -> adb_20190315_models.DescribeLogStoreKeysResponse:
        """
        @summary Queries a list of log keywords in a Logstore.
        
        @param request: DescribeLogStoreKeysRequest
        @return: DescribeLogStoreKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_keys_with_options_async(request, runtime)

    def describe_loghub_detail_with_options(
        self,
        request: adb_20190315_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLoghubDetailResponse:
        """
        @summary Queries the log collection information.
        
        @param request: DescribeLoghubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoghubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_name):
            query['ExportName'] = request.export_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoghubDetail',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLoghubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_loghub_detail_with_options_async(
        self,
        request: adb_20190315_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeLoghubDetailResponse:
        """
        @summary Queries the log collection information.
        
        @param request: DescribeLoghubDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoghubDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_name):
            query['ExportName'] = request.export_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoghubDetail',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeLoghubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_loghub_detail(
        self,
        request: adb_20190315_models.DescribeLoghubDetailRequest,
    ) -> adb_20190315_models.DescribeLoghubDetailResponse:
        """
        @summary Queries the log collection information.
        
        @param request: DescribeLoghubDetailRequest
        @return: DescribeLoghubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    async def describe_loghub_detail_async(
        self,
        request: adb_20190315_models.DescribeLoghubDetailRequest,
    ) -> adb_20190315_models.DescribeLoghubDetailResponse:
        """
        @summary Queries the log collection information.
        
        @param request: DescribeLoghubDetailRequest
        @return: DescribeLoghubDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_loghub_detail_with_options_async(request, runtime)

    def describe_maintenance_action_with_options(
        self,
        request: adb_20190315_models.DescribeMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeMaintenanceActionResponse:
        """
        @summary Queries the information about O&M events.
        
        @param request: DescribeMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaintenanceAction',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_maintenance_action_with_options_async(
        self,
        request: adb_20190315_models.DescribeMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeMaintenanceActionResponse:
        """
        @summary Queries the information about O&M events.
        
        @param request: DescribeMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaintenanceAction',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_maintenance_action(
        self,
        request: adb_20190315_models.DescribeMaintenanceActionRequest,
    ) -> adb_20190315_models.DescribeMaintenanceActionResponse:
        """
        @summary Queries the information about O&M events.
        
        @param request: DescribeMaintenanceActionRequest
        @return: DescribeMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_maintenance_action_with_options(request, runtime)

    async def describe_maintenance_action_async(
        self,
        request: adb_20190315_models.DescribeMaintenanceActionRequest,
    ) -> adb_20190315_models.DescribeMaintenanceActionResponse:
        """
        @summary Queries the information about O&M events.
        
        @param request: DescribeMaintenanceActionRequest
        @return: DescribeMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_maintenance_action_with_options_async(request, runtime)

    def describe_operator_permission_with_options(
        self,
        request: adb_20190315_models.DescribeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeOperatorPermissionResponse:
        """
        @summary Queries the details of the permissions granted to the service account of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operator_permission_with_options_async(
        self,
        request: adb_20190315_models.DescribeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeOperatorPermissionResponse:
        """
        @summary Queries the details of the permissions granted to the service account of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operator_permission(
        self,
        request: adb_20190315_models.DescribeOperatorPermissionRequest,
    ) -> adb_20190315_models.DescribeOperatorPermissionResponse:
        """
        @summary Queries the details of the permissions granted to the service account of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOperatorPermissionRequest
        @return: DescribeOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operator_permission_with_options(request, runtime)

    async def describe_operator_permission_async(
        self,
        request: adb_20190315_models.DescribeOperatorPermissionRequest,
    ) -> adb_20190315_models.DescribeOperatorPermissionResponse:
        """
        @summary Queries the details of the permissions granted to the service account of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOperatorPermissionRequest
        @return: DescribeOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_operator_permission_with_options_async(request, runtime)

    def describe_oversize_non_partition_table_infos_with_options(
        self,
        request: adb_20190315_models.DescribeOversizeNonPartitionTableInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse:
        """
        @summary Queries the information about oversized non-partitioned tables in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOversizeNonPartitionTableInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOversizeNonPartitionTableInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
            action='DescribeOversizeNonPartitionTableInfos',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oversize_non_partition_table_infos_with_options_async(
        self,
        request: adb_20190315_models.DescribeOversizeNonPartitionTableInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse:
        """
        @summary Queries the information about oversized non-partitioned tables in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOversizeNonPartitionTableInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOversizeNonPartitionTableInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
            action='DescribeOversizeNonPartitionTableInfos',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oversize_non_partition_table_infos(
        self,
        request: adb_20190315_models.DescribeOversizeNonPartitionTableInfosRequest,
    ) -> adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse:
        """
        @summary Queries the information about oversized non-partitioned tables in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOversizeNonPartitionTableInfosRequest
        @return: DescribeOversizeNonPartitionTableInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oversize_non_partition_table_infos_with_options(request, runtime)

    async def describe_oversize_non_partition_table_infos_async(
        self,
        request: adb_20190315_models.DescribeOversizeNonPartitionTableInfosRequest,
    ) -> adb_20190315_models.DescribeOversizeNonPartitionTableInfosResponse:
        """
        @summary Queries the information about oversized non-partitioned tables in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeOversizeNonPartitionTableInfosRequest
        @return: DescribeOversizeNonPartitionTableInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oversize_non_partition_table_infos_with_options_async(request, runtime)

    def describe_pattern_performance_with_options(
        self,
        request: adb_20190315_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the metrics of an SQL pattern such as the query duration and average memory usage within a period of time.
        
        @param request: DescribePatternPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePatternPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribePatternPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_performance_with_options_async(
        self,
        request: adb_20190315_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the metrics of an SQL pattern such as the query duration and average memory usage within a period of time.
        
        @param request: DescribePatternPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePatternPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternPerformance',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribePatternPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_performance(
        self,
        request: adb_20190315_models.DescribePatternPerformanceRequest,
    ) -> adb_20190315_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the metrics of an SQL pattern such as the query duration and average memory usage within a period of time.
        
        @param request: DescribePatternPerformanceRequest
        @return: DescribePatternPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pattern_performance_with_options(request, runtime)

    async def describe_pattern_performance_async(
        self,
        request: adb_20190315_models.DescribePatternPerformanceRequest,
    ) -> adb_20190315_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the metrics of an SQL pattern such as the query duration and average memory usage within a period of time.
        
        @param request: DescribePatternPerformanceRequest
        @return: DescribePatternPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pattern_performance_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: adb_20190315_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeProcessListResponse:
        """
        @summary Queries the queries that are being executed on a cluster.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.running_time):
            query['RunningTime'] = request.running_time
        if not UtilClient.is_unset(request.show_full):
            query['ShowFull'] = request.show_full
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: adb_20190315_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeProcessListResponse:
        """
        @summary Queries the queries that are being executed on a cluster.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.running_time):
            query['RunningTime'] = request.running_time
        if not UtilClient.is_unset(request.show_full):
            query['ShowFull'] = request.show_full
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: adb_20190315_models.DescribeProcessListRequest,
    ) -> adb_20190315_models.DescribeProcessListResponse:
        """
        @summary Queries the queries that are being executed on a cluster.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: adb_20190315_models.DescribeProcessListRequest,
    ) -> adb_20190315_models.DescribeProcessListResponse:
        """
        @summary Queries the queries that are being executed on a cluster.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_rds_analysis_resource_quotas_with_options(
        self,
        request: adb_20190315_models.DescribeRdsAnalysisResourceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse:
        """
        @summary Queries the information about specifications of MySQL analytic instances.
        
        @param request: DescribeRdsAnalysisResourceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsAnalysisResourceQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsAnalysisResourceQuotas',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_analysis_resource_quotas_with_options_async(
        self,
        request: adb_20190315_models.DescribeRdsAnalysisResourceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse:
        """
        @summary Queries the information about specifications of MySQL analytic instances.
        
        @param request: DescribeRdsAnalysisResourceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsAnalysisResourceQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsAnalysisResourceQuotas',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_analysis_resource_quotas(
        self,
        request: adb_20190315_models.DescribeRdsAnalysisResourceQuotasRequest,
    ) -> adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse:
        """
        @summary Queries the information about specifications of MySQL analytic instances.
        
        @param request: DescribeRdsAnalysisResourceQuotasRequest
        @return: DescribeRdsAnalysisResourceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_analysis_resource_quotas_with_options(request, runtime)

    async def describe_rds_analysis_resource_quotas_async(
        self,
        request: adb_20190315_models.DescribeRdsAnalysisResourceQuotasRequest,
    ) -> adb_20190315_models.DescribeRdsAnalysisResourceQuotasResponse:
        """
        @summary Queries the information about specifications of MySQL analytic instances.
        
        @param request: DescribeRdsAnalysisResourceQuotasRequest
        @return: DescribeRdsAnalysisResourceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_analysis_resource_quotas_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: adb_20190315_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions and zones for AnalyticDB for MySQL.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action='DescribeRegions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: adb_20190315_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions and zones for AnalyticDB for MySQL.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action='DescribeRegions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: adb_20190315_models.DescribeRegionsRequest,
    ) -> adb_20190315_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions and zones for AnalyticDB for MySQL.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: adb_20190315_models.DescribeRegionsRequest,
    ) -> adb_20190315_models.DescribeRegionsResponse:
        """
        @summary Queries a list of available regions and zones for AnalyticDB for MySQL.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_regions_mixed_with_options(
        self,
        request: adb_20190315_models.DescribeRegionsMixedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRegionsMixedResponse:
        """
        @summary Queries information about regions.
        
        @param request: DescribeRegionsMixedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsMixedResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeRegionsMixed',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRegionsMixedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_mixed_with_options_async(
        self,
        request: adb_20190315_models.DescribeRegionsMixedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeRegionsMixedResponse:
        """
        @summary Queries information about regions.
        
        @param request: DescribeRegionsMixedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsMixedResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeRegionsMixed',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeRegionsMixedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions_mixed(
        self,
        request: adb_20190315_models.DescribeRegionsMixedRequest,
    ) -> adb_20190315_models.DescribeRegionsMixedResponse:
        """
        @summary Queries information about regions.
        
        @param request: DescribeRegionsMixedRequest
        @return: DescribeRegionsMixedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_mixed_with_options(request, runtime)

    async def describe_regions_mixed_async(
        self,
        request: adb_20190315_models.DescribeRegionsMixedRequest,
    ) -> adb_20190315_models.DescribeRegionsMixedResponse:
        """
        @summary Queries information about regions.
        
        @param request: DescribeRegionsMixedRequest
        @return: DescribeRegionsMixedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_mixed_with_options_async(request, runtime)

    def describe_resubmit_config_with_options(
        self,
        request: adb_20190315_models.DescribeResubmitConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeResubmitConfigResponse:
        """
        @summary 查询Resubmit配置
        
        @param request: DescribeResubmitConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResubmitConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResubmitConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeResubmitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resubmit_config_with_options_async(
        self,
        request: adb_20190315_models.DescribeResubmitConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeResubmitConfigResponse:
        """
        @summary 查询Resubmit配置
        
        @param request: DescribeResubmitConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResubmitConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResubmitConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeResubmitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resubmit_config(
        self,
        request: adb_20190315_models.DescribeResubmitConfigRequest,
    ) -> adb_20190315_models.DescribeResubmitConfigResponse:
        """
        @summary 查询Resubmit配置
        
        @param request: DescribeResubmitConfigRequest
        @return: DescribeResubmitConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resubmit_config_with_options(request, runtime)

    async def describe_resubmit_config_async(
        self,
        request: adb_20190315_models.DescribeResubmitConfigRequest,
    ) -> adb_20190315_models.DescribeResubmitConfigResponse:
        """
        @summary 查询Resubmit配置
        
        @param request: DescribeResubmitConfigRequest
        @return: DescribeResubmitConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resubmit_config_with_options_async(request, runtime)

    def describe_sqaconfig_with_options(
        self,
        request: adb_20190315_models.DescribeSQAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQAConfigResponse:
        """
        @summary 查询SQA状态
        
        @param request: DescribeSQAConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQAConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQAConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqaconfig_with_options_async(
        self,
        request: adb_20190315_models.DescribeSQAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQAConfigResponse:
        """
        @summary 查询SQA状态
        
        @param request: DescribeSQAConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQAConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQAConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqaconfig(
        self,
        request: adb_20190315_models.DescribeSQAConfigRequest,
    ) -> adb_20190315_models.DescribeSQAConfigResponse:
        """
        @summary 查询SQA状态
        
        @param request: DescribeSQAConfigRequest
        @return: DescribeSQAConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqaconfig_with_options(request, runtime)

    async def describe_sqaconfig_async(
        self,
        request: adb_20190315_models.DescribeSQAConfigRequest,
    ) -> adb_20190315_models.DescribeSQAConfigResponse:
        """
        @summary 查询SQA状态
        
        @param request: DescribeSQAConfigRequest
        @return: DescribeSQAConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqaconfig_with_options_async(request, runtime)

    def describe_sqlpatterns_with_options(
        self,
        request: adb_20190315_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a period of time.
        
        @param request: DescribeSQLPatternsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPatternsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlpatterns_with_options_async(
        self,
        request: adb_20190315_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a period of time.
        
        @param request: DescribeSQLPatternsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPatternsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlpatterns(
        self,
        request: adb_20190315_models.DescribeSQLPatternsRequest,
    ) -> adb_20190315_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a period of time.
        
        @param request: DescribeSQLPatternsRequest
        @return: DescribeSQLPatternsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpatterns_with_options(request, runtime)

    async def describe_sqlpatterns_async(
        self,
        request: adb_20190315_models.DescribeSQLPatternsRequest,
    ) -> adb_20190315_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a period of time.
        
        @param request: DescribeSQLPatternsRequest
        @return: DescribeSQLPatternsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlpatterns_with_options_async(request, runtime)

    def describe_sqlplan_with_options(
        self,
        request: adb_20190315_models.DescribeSQLPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPlanResponse:
        """
        @summary Queries the plan information about an SQL statement such as a query statement or an extract-transform-load (ETL) task statement.
        
        @param request: DescribeSQLPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlplan_with_options_async(
        self,
        request: adb_20190315_models.DescribeSQLPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPlanResponse:
        """
        @summary Queries the plan information about an SQL statement such as a query statement or an extract-transform-load (ETL) task statement.
        
        @param request: DescribeSQLPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlplan(
        self,
        request: adb_20190315_models.DescribeSQLPlanRequest,
    ) -> adb_20190315_models.DescribeSQLPlanResponse:
        """
        @summary Queries the plan information about an SQL statement such as a query statement or an extract-transform-load (ETL) task statement.
        
        @param request: DescribeSQLPlanRequest
        @return: DescribeSQLPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplan_with_options(request, runtime)

    async def describe_sqlplan_async(
        self,
        request: adb_20190315_models.DescribeSQLPlanRequest,
    ) -> adb_20190315_models.DescribeSQLPlanResponse:
        """
        @summary Queries the plan information about an SQL statement such as a query statement or an extract-transform-load (ETL) task statement.
        
        @param request: DescribeSQLPlanRequest
        @return: DescribeSQLPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlplan_with_options_async(request, runtime)

    def describe_sqlplan_task_with_options(
        self,
        request: adb_20190315_models.DescribeSQLPlanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPlanTaskResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeSQLPlanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlanTask',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlplan_task_with_options_async(
        self,
        request: adb_20190315_models.DescribeSQLPlanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSQLPlanTaskResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeSQLPlanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlanTask',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSQLPlanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlplan_task(
        self,
        request: adb_20190315_models.DescribeSQLPlanTaskRequest,
    ) -> adb_20190315_models.DescribeSQLPlanTaskResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeSQLPlanTaskRequest
        @return: DescribeSQLPlanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplan_task_with_options(request, runtime)

    async def describe_sqlplan_task_async(
        self,
        request: adb_20190315_models.DescribeSQLPlanTaskRequest,
    ) -> adb_20190315_models.DescribeSQLPlanTaskResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeSQLPlanTaskRequest
        @return: DescribeSQLPlanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlplan_task_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: adb_20190315_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: adb_20190315_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: adb_20190315_models.DescribeSchemasRequest,
    ) -> adb_20190315_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: adb_20190315_models.DescribeSchemasRequest,
    ) -> adb_20190315_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: adb_20190315_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_id):
            query['ProcessID'] = request.process_id
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: adb_20190315_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_id):
            query['ProcessID'] = request.process_id
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: adb_20190315_models.DescribeSlowLogRecordsRequest,
    ) -> adb_20190315_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: adb_20190315_models.DescribeSlowLogRecordsRequest,
    ) -> adb_20190315_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_sql_pattern_with_options(
        self,
        request: adb_20190315_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSqlPatternResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a time range.
        
        @param request: DescribeSqlPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlPatternResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlPattern',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSqlPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_pattern_with_options_async(
        self,
        request: adb_20190315_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSqlPatternResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a time range.
        
        @param request: DescribeSqlPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlPatternResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlPattern',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSqlPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_pattern(
        self,
        request: adb_20190315_models.DescribeSqlPatternRequest,
    ) -> adb_20190315_models.DescribeSqlPatternResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a time range.
        
        @param request: DescribeSqlPatternRequest
        @return: DescribeSqlPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_pattern_with_options(request, runtime)

    async def describe_sql_pattern_async(
        self,
        request: adb_20190315_models.DescribeSqlPatternRequest,
    ) -> adb_20190315_models.DescribeSqlPatternResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL cluster within a time range.
        
        @param request: DescribeSqlPatternRequest
        @return: DescribeSqlPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_pattern_with_options_async(request, runtime)

    def describe_sync_available_dbcluster_list_with_options(
        self,
        request: adb_20190315_models.DescribeSyncAvailableDBClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSyncAvailableDBClusterListResponse:
        """
        @summary Queries a list of instances or clusters that are available for data synchronization.
        
        @param request: DescribeSyncAvailableDBClusterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncAvailableDBClusterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not UtilClient.is_unset(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncAvailableDBClusterList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSyncAvailableDBClusterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_available_dbcluster_list_with_options_async(
        self,
        request: adb_20190315_models.DescribeSyncAvailableDBClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSyncAvailableDBClusterListResponse:
        """
        @summary Queries a list of instances or clusters that are available for data synchronization.
        
        @param request: DescribeSyncAvailableDBClusterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncAvailableDBClusterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not UtilClient.is_unset(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncAvailableDBClusterList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSyncAvailableDBClusterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_available_dbcluster_list(
        self,
        request: adb_20190315_models.DescribeSyncAvailableDBClusterListRequest,
    ) -> adb_20190315_models.DescribeSyncAvailableDBClusterListResponse:
        """
        @summary Queries a list of instances or clusters that are available for data synchronization.
        
        @param request: DescribeSyncAvailableDBClusterListRequest
        @return: DescribeSyncAvailableDBClusterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_available_dbcluster_list_with_options(request, runtime)

    async def describe_sync_available_dbcluster_list_async(
        self,
        request: adb_20190315_models.DescribeSyncAvailableDBClusterListRequest,
    ) -> adb_20190315_models.DescribeSyncAvailableDBClusterListResponse:
        """
        @summary Queries a list of instances or clusters that are available for data synchronization.
        
        @param request: DescribeSyncAvailableDBClusterListRequest
        @return: DescribeSyncAvailableDBClusterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sync_available_dbcluster_list_with_options_async(request, runtime)

    def describe_sync_job_list_with_options(
        self,
        request: adb_20190315_models.DescribeSyncJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSyncJobListResponse:
        """
        @summary Queries a list of synchronization jobs in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSyncJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.get_source_detail):
            query['GetSourceDetail'] = request.get_source_detail
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
        if not UtilClient.is_unset(request.source_dbcluster_description):
            query['SourceDBClusterDescription'] = request.source_dbcluster_description
        if not UtilClient.is_unset(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not UtilClient.is_unset(request.source_dbtype):
            query['SourceDBType'] = request.source_dbtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncJobList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSyncJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_job_list_with_options_async(
        self,
        request: adb_20190315_models.DescribeSyncJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeSyncJobListResponse:
        """
        @summary Queries a list of synchronization jobs in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSyncJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.get_source_detail):
            query['GetSourceDetail'] = request.get_source_detail
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
        if not UtilClient.is_unset(request.source_dbcluster_description):
            query['SourceDBClusterDescription'] = request.source_dbcluster_description
        if not UtilClient.is_unset(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not UtilClient.is_unset(request.source_dbtype):
            query['SourceDBType'] = request.source_dbtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncJobList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeSyncJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_job_list(
        self,
        request: adb_20190315_models.DescribeSyncJobListRequest,
    ) -> adb_20190315_models.DescribeSyncJobListResponse:
        """
        @summary Queries a list of synchronization jobs in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSyncJobListRequest
        @return: DescribeSyncJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_job_list_with_options(request, runtime)

    async def describe_sync_job_list_async(
        self,
        request: adb_20190315_models.DescribeSyncJobListRequest,
    ) -> adb_20190315_models.DescribeSyncJobListResponse:
        """
        @summary Queries a list of synchronization jobs in an AnalyticDB for MySQL cluster.
        
        @param request: DescribeSyncJobListRequest
        @return: DescribeSyncJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sync_job_list_with_options_async(request, runtime)

    def describe_table_access_count_with_options(
        self,
        request: adb_20190315_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableAccessCountResponse:
        """
        @summary 查询表访问统计信息
        
        @param request: DescribeTableAccessCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableAccessCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableAccessCount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableAccessCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_access_count_with_options_async(
        self,
        request: adb_20190315_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableAccessCountResponse:
        """
        @summary 查询表访问统计信息
        
        @param request: DescribeTableAccessCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableAccessCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableAccessCount',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableAccessCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_access_count(
        self,
        request: adb_20190315_models.DescribeTableAccessCountRequest,
    ) -> adb_20190315_models.DescribeTableAccessCountResponse:
        """
        @summary 查询表访问统计信息
        
        @param request: DescribeTableAccessCountRequest
        @return: DescribeTableAccessCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_access_count_with_options(request, runtime)

    async def describe_table_access_count_async(
        self,
        request: adb_20190315_models.DescribeTableAccessCountRequest,
    ) -> adb_20190315_models.DescribeTableAccessCountResponse:
        """
        @summary 查询表访问统计信息
        
        @param request: DescribeTableAccessCountRequest
        @return: DescribeTableAccessCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_access_count_with_options_async(request, runtime)

    def describe_table_detail_with_options(
        self,
        request: adb_20190315_models.DescribeTableDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableDetailResponse:
        """
        @summary 查询表详情
        
        @param request: DescribeTableDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableDetail',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_detail_with_options_async(
        self,
        request: adb_20190315_models.DescribeTableDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableDetailResponse:
        """
        @summary 查询表详情
        
        @param request: DescribeTableDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableDetail',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_detail(
        self,
        request: adb_20190315_models.DescribeTableDetailRequest,
    ) -> adb_20190315_models.DescribeTableDetailResponse:
        """
        @summary 查询表详情
        
        @param request: DescribeTableDetailRequest
        @return: DescribeTableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_detail_with_options(request, runtime)

    async def describe_table_detail_async(
        self,
        request: adb_20190315_models.DescribeTableDetailRequest,
    ) -> adb_20190315_models.DescribeTableDetailResponse:
        """
        @summary 查询表详情
        
        @param request: DescribeTableDetailRequest
        @return: DescribeTableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_detail_with_options_async(request, runtime)

    def describe_table_partition_diagnose_with_options(
        self,
        request: adb_20190315_models.DescribeTablePartitionDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTablePartitionDiagnoseResponse:
        """
        @summary Queries the information about partition diagnostics.
        
        @param request: DescribeTablePartitionDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablePartitionDiagnoseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTablePartitionDiagnose',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablePartitionDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_partition_diagnose_with_options_async(
        self,
        request: adb_20190315_models.DescribeTablePartitionDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTablePartitionDiagnoseResponse:
        """
        @summary Queries the information about partition diagnostics.
        
        @param request: DescribeTablePartitionDiagnoseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablePartitionDiagnoseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTablePartitionDiagnose',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablePartitionDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_partition_diagnose(
        self,
        request: adb_20190315_models.DescribeTablePartitionDiagnoseRequest,
    ) -> adb_20190315_models.DescribeTablePartitionDiagnoseResponse:
        """
        @summary Queries the information about partition diagnostics.
        
        @param request: DescribeTablePartitionDiagnoseRequest
        @return: DescribeTablePartitionDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_partition_diagnose_with_options(request, runtime)

    async def describe_table_partition_diagnose_async(
        self,
        request: adb_20190315_models.DescribeTablePartitionDiagnoseRequest,
    ) -> adb_20190315_models.DescribeTablePartitionDiagnoseResponse:
        """
        @summary Queries the information about partition diagnostics.
        
        @param request: DescribeTablePartitionDiagnoseRequest
        @return: DescribeTablePartitionDiagnoseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_partition_diagnose_with_options_async(request, runtime)

    def describe_table_statistics_with_options(
        self,
        request: adb_20190315_models.DescribeTableStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableStatisticsResponse:
        """
        @summary Queries the information about table statistics for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTableStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableStatistics',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_statistics_with_options_async(
        self,
        request: adb_20190315_models.DescribeTableStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTableStatisticsResponse:
        """
        @summary Queries the information about table statistics for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTableStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTableStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableStatistics',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTableStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_statistics(
        self,
        request: adb_20190315_models.DescribeTableStatisticsRequest,
    ) -> adb_20190315_models.DescribeTableStatisticsResponse:
        """
        @summary Queries the information about table statistics for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTableStatisticsRequest
        @return: DescribeTableStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_statistics_with_options(request, runtime)

    async def describe_table_statistics_async(
        self,
        request: adb_20190315_models.DescribeTableStatisticsRequest,
    ) -> adb_20190315_models.DescribeTableStatisticsResponse:
        """
        @summary Queries the information about table statistics for an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTableStatisticsRequest
        @return: DescribeTableStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_statistics_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: adb_20190315_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: adb_20190315_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: adb_20190315_models.DescribeTablesRequest,
    ) -> adb_20190315_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: adb_20190315_models.DescribeTablesRequest,
    ) -> adb_20190315_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database of an AnalyticDB for MySQL cluster.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_task_info_with_options(
        self,
        request: adb_20190315_models.DescribeTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTaskInfoResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_info_with_options_async(
        self,
        request: adb_20190315_models.DescribeTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeTaskInfoResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskInfo',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_info(
        self,
        request: adb_20190315_models.DescribeTaskInfoRequest,
    ) -> adb_20190315_models.DescribeTaskInfoResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeTaskInfoRequest
        @return: DescribeTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_info_with_options(request, runtime)

    async def describe_task_info_async(
        self,
        request: adb_20190315_models.DescribeTaskInfoRequest,
    ) -> adb_20190315_models.DescribeTaskInfoResponse:
        """
        @summary Queries the information about a task.
        
        @param request: DescribeTaskInfoRequest
        @return: DescribeTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_info_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: adb_20190315_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVSwitchesResponse:
        """
        @summary Queries the vSwitches.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: adb_20190315_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVSwitchesResponse:
        """
        @summary Queries the vSwitches.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: adb_20190315_models.DescribeVSwitchesRequest,
    ) -> adb_20190315_models.DescribeVSwitchesResponse:
        """
        @summary Queries the vSwitches.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: adb_20190315_models.DescribeVSwitchesRequest,
    ) -> adb_20190315_models.DescribeVSwitchesResponse:
        """
        @summary Queries the vSwitches.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_vswitchs_with_options(
        self,
        request: adb_20190315_models.DescribeVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVSwitchsResponse:
        """
        @summary Queries a list of available vSwitches.
        
        @param request: DescribeVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitchs',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitchs_with_options_async(
        self,
        request: adb_20190315_models.DescribeVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVSwitchsResponse:
        """
        @summary Queries a list of available vSwitches.
        
        @param request: DescribeVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitchs',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitchs(
        self,
        request: adb_20190315_models.DescribeVSwitchsRequest,
    ) -> adb_20190315_models.DescribeVSwitchsResponse:
        """
        @summary Queries a list of available vSwitches.
        
        @param request: DescribeVSwitchsRequest
        @return: DescribeVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitchs_with_options(request, runtime)

    async def describe_vswitchs_async(
        self,
        request: adb_20190315_models.DescribeVSwitchsRequest,
    ) -> adb_20190315_models.DescribeVSwitchsResponse:
        """
        @summary Queries a list of available vSwitches.
        
        @param request: DescribeVSwitchsRequest
        @return: DescribeVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitchs_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: adb_20190315_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVpcsResponse:
        """
        @summary Queries a list of available virtual private clouds (VPCs).
        
        @param request: DescribeVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: adb_20190315_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeVpcsResponse:
        """
        @summary Queries a list of available virtual private clouds (VPCs).
        
        @param request: DescribeVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: adb_20190315_models.DescribeVpcsRequest,
    ) -> adb_20190315_models.DescribeVpcsResponse:
        """
        @summary Queries a list of available virtual private clouds (VPCs).
        
        @param request: DescribeVpcsRequest
        @return: DescribeVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: adb_20190315_models.DescribeVpcsRequest,
    ) -> adb_20190315_models.DescribeVpcsResponse:
        """
        @summary Queries a list of available virtual private clouds (VPCs).
        
        @param request: DescribeVpcsRequest
        @return: DescribeVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_worker_detection_with_options(
        self,
        request: adb_20190315_models.DescribeWorkerDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeWorkerDetectionResponse:
        """
        @summary Queries the diagnostic results of the storage layer.
        
        @param request: DescribeWorkerDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkerDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkerDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeWorkerDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_worker_detection_with_options_async(
        self,
        request: adb_20190315_models.DescribeWorkerDetectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DescribeWorkerDetectionResponse:
        """
        @summary Queries the diagnostic results of the storage layer.
        
        @param request: DescribeWorkerDetectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkerDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkerDetection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DescribeWorkerDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_worker_detection(
        self,
        request: adb_20190315_models.DescribeWorkerDetectionRequest,
    ) -> adb_20190315_models.DescribeWorkerDetectionResponse:
        """
        @summary Queries the diagnostic results of the storage layer.
        
        @param request: DescribeWorkerDetectionRequest
        @return: DescribeWorkerDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_worker_detection_with_options(request, runtime)

    async def describe_worker_detection_async(
        self,
        request: adb_20190315_models.DescribeWorkerDetectionRequest,
    ) -> adb_20190315_models.DescribeWorkerDetectionResponse:
        """
        @summary Queries the diagnostic results of the storage layer.
        
        @param request: DescribeWorkerDetectionRequest
        @return: DescribeWorkerDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_worker_detection_with_options_async(request, runtime)

    def detach_user_eniwith_options(
        self,
        request: adb_20190315_models.DetachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DetachUserENIResponse:
        """
        @summary 关闭用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: DetachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachUserENI',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DetachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_user_eniwith_options_async(
        self,
        request: adb_20190315_models.DetachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DetachUserENIResponse:
        """
        @summary 关闭用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: DetachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachUserENI',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DetachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_user_eni(
        self,
        request: adb_20190315_models.DetachUserENIRequest,
    ) -> adb_20190315_models.DetachUserENIResponse:
        """
        @summary 关闭用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: DetachUserENIRequest
        @return: DetachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_user_eniwith_options(request, runtime)

    async def detach_user_eni_async(
        self,
        request: adb_20190315_models.DetachUserENIRequest,
    ) -> adb_20190315_models.DetachUserENIResponse:
        """
        @summary 关闭用户ENI
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition.
        
        @param request: DetachUserENIRequest
        @return: DetachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_user_eniwith_options_async(request, runtime)

    def disable_advice_service_with_options(
        self,
        request: adb_20190315_models.DisableAdviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DisableAdviceServiceResponse:
        """
        @summary Disables the suggestion feature.
        
        @param request: DisableAdviceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAdviceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAdviceService',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DisableAdviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_advice_service_with_options_async(
        self,
        request: adb_20190315_models.DisableAdviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DisableAdviceServiceResponse:
        """
        @summary Disables the suggestion feature.
        
        @param request: DisableAdviceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAdviceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAdviceService',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DisableAdviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_advice_service(
        self,
        request: adb_20190315_models.DisableAdviceServiceRequest,
    ) -> adb_20190315_models.DisableAdviceServiceResponse:
        """
        @summary Disables the suggestion feature.
        
        @param request: DisableAdviceServiceRequest
        @return: DisableAdviceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_advice_service_with_options(request, runtime)

    async def disable_advice_service_async(
        self,
        request: adb_20190315_models.DisableAdviceServiceRequest,
    ) -> adb_20190315_models.DisableAdviceServiceResponse:
        """
        @summary Disables the suggestion feature.
        
        @param request: DisableAdviceServiceRequest
        @return: DisableAdviceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_advice_service_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: adb_20190315_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a condition for an AnalyticDB for MySQL cluster.
        
        @param request: DownloadDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: adb_20190315_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a condition for an AnalyticDB for MySQL cluster.
        
        @param request: DownloadDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: adb_20190315_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20190315_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a condition for an AnalyticDB for MySQL cluster.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: adb_20190315_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20190315_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a condition for an AnalyticDB for MySQL cluster.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def enable_advice_service_with_options(
        self,
        request: adb_20190315_models.EnableAdviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.EnableAdviceServiceResponse:
        """
        @summary 开通建议服务
        
        @param request: EnableAdviceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAdviceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdviceService',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.EnableAdviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_advice_service_with_options_async(
        self,
        request: adb_20190315_models.EnableAdviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.EnableAdviceServiceResponse:
        """
        @summary 开通建议服务
        
        @param request: EnableAdviceServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAdviceServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdviceService',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.EnableAdviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_advice_service(
        self,
        request: adb_20190315_models.EnableAdviceServiceRequest,
    ) -> adb_20190315_models.EnableAdviceServiceResponse:
        """
        @summary 开通建议服务
        
        @param request: EnableAdviceServiceRequest
        @return: EnableAdviceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_advice_service_with_options(request, runtime)

    async def enable_advice_service_async(
        self,
        request: adb_20190315_models.EnableAdviceServiceRequest,
    ) -> adb_20190315_models.EnableAdviceServiceResponse:
        """
        @summary 开通建议服务
        
        @param request: EnableAdviceServiceRequest
        @return: EnableAdviceServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_advice_service_with_options_async(request, runtime)

    def get_create_table_sqlwith_options(
        self,
        request: adb_20190315_models.GetCreateTableSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.GetCreateTableSQLResponse:
        """
        @summary Queries the table creation statement for tables.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: GetCreateTableSQLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateTableSQLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateTableSQL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.GetCreateTableSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_table_sqlwith_options_async(
        self,
        request: adb_20190315_models.GetCreateTableSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.GetCreateTableSQLResponse:
        """
        @summary Queries the table creation statement for tables.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: GetCreateTableSQLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateTableSQLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateTableSQL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.GetCreateTableSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_table_sql(
        self,
        request: adb_20190315_models.GetCreateTableSQLRequest,
    ) -> adb_20190315_models.GetCreateTableSQLResponse:
        """
        @summary Queries the table creation statement for tables.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: GetCreateTableSQLRequest
        @return: GetCreateTableSQLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_create_table_sqlwith_options(request, runtime)

    async def get_create_table_sql_async(
        self,
        request: adb_20190315_models.GetCreateTableSQLRequest,
    ) -> adb_20190315_models.GetCreateTableSQLResponse:
        """
        @summary Queries the table creation statement for tables.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: GetCreateTableSQLRequest
        @return: GetCreateTableSQLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_create_table_sqlwith_options_async(request, runtime)

    def grant_operator_permission_with_options(
        self,
        request: adb_20190315_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.GrantOperatorPermissionResponse:
        """
        @summary Grants permissions to the service account of an AnalyticDB for MySQL cluster.
        
        @description ###
        If you need Alibaba Cloud technical support to perform operations on your AnalyticDB for MySQL cluster, you must grant permissions to the service account of your cluster. When the validity period of the authorization ends, the granted permissions are automatically revoked.
        
        @param request: GrantOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.privileges):
            query['Privileges'] = request.privileges
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.GrantOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_operator_permission_with_options_async(
        self,
        request: adb_20190315_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.GrantOperatorPermissionResponse:
        """
        @summary Grants permissions to the service account of an AnalyticDB for MySQL cluster.
        
        @description ###
        If you need Alibaba Cloud technical support to perform operations on your AnalyticDB for MySQL cluster, you must grant permissions to the service account of your cluster. When the validity period of the authorization ends, the granted permissions are automatically revoked.
        
        @param request: GrantOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.privileges):
            query['Privileges'] = request.privileges
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.GrantOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_operator_permission(
        self,
        request: adb_20190315_models.GrantOperatorPermissionRequest,
    ) -> adb_20190315_models.GrantOperatorPermissionResponse:
        """
        @summary Grants permissions to the service account of an AnalyticDB for MySQL cluster.
        
        @description ###
        If you need Alibaba Cloud technical support to perform operations on your AnalyticDB for MySQL cluster, you must grant permissions to the service account of your cluster. When the validity period of the authorization ends, the granted permissions are automatically revoked.
        
        @param request: GrantOperatorPermissionRequest
        @return: GrantOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    async def grant_operator_permission_async(
        self,
        request: adb_20190315_models.GrantOperatorPermissionRequest,
    ) -> adb_20190315_models.GrantOperatorPermissionResponse:
        """
        @summary Grants permissions to the service account of an AnalyticDB for MySQL cluster.
        
        @description ###
        If you need Alibaba Cloud technical support to perform operations on your AnalyticDB for MySQL cluster, you must grant permissions to the service account of your cluster. When the validity period of the authorization ends, the granted permissions are automatically revoked.
        
        @param request: GrantOperatorPermissionRequest
        @return: GrantOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_operator_permission_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: adb_20190315_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: adb_20190315_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: adb_20190315_models.KillProcessRequest,
    ) -> adb_20190315_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: adb_20190315_models.KillProcessRequest,
    ) -> adb_20190315_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: adb_20190315_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to AnalyticDB for MySQL clusters, or the AnalyticDB for MySQL clusters that have tags added.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: adb_20190315_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to AnalyticDB for MySQL clusters, or the AnalyticDB for MySQL clusters that have tags added.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: adb_20190315_models.ListTagResourcesRequest,
    ) -> adb_20190315_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to AnalyticDB for MySQL clusters, or the AnalyticDB for MySQL clusters that have tags added.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: adb_20190315_models.ListTagResourcesRequest,
    ) -> adb_20190315_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to AnalyticDB for MySQL clusters, or the AnalyticDB for MySQL clusters that have tags added.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_dbcluster_with_options(
        self,
        request: adb_20190315_models.MigrateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.MigrateDBClusterResponse:
        """
        @summary Migrates data from a Data Warehouse Edition cluster to a Data Lakehouse Edition cluster in AnalyticDB for MySQL.
        
        @param request: MigrateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_form):
            query['ProductForm'] = request.product_form
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.shard_number):
            query['ShardNumber'] = request.shard_number
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.storage_resource_size):
            query['StorageResourceSize'] = request.storage_resource_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.MigrateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_dbcluster_with_options_async(
        self,
        request: adb_20190315_models.MigrateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.MigrateDBClusterResponse:
        """
        @summary Migrates data from a Data Warehouse Edition cluster to a Data Lakehouse Edition cluster in AnalyticDB for MySQL.
        
        @param request: MigrateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_form):
            query['ProductForm'] = request.product_form
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.shard_number):
            query['ShardNumber'] = request.shard_number
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.storage_resource_size):
            query['StorageResourceSize'] = request.storage_resource_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.MigrateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_dbcluster(
        self,
        request: adb_20190315_models.MigrateDBClusterRequest,
    ) -> adb_20190315_models.MigrateDBClusterResponse:
        """
        @summary Migrates data from a Data Warehouse Edition cluster to a Data Lakehouse Edition cluster in AnalyticDB for MySQL.
        
        @param request: MigrateDBClusterRequest
        @return: MigrateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbcluster_with_options(request, runtime)

    async def migrate_dbcluster_async(
        self,
        request: adb_20190315_models.MigrateDBClusterRequest,
    ) -> adb_20190315_models.MigrateDBClusterResponse:
        """
        @summary Migrates data from a Data Warehouse Edition cluster to a Data Lakehouse Edition cluster in AnalyticDB for MySQL.
        
        @param request: MigrateDBClusterRequest
        @return: MigrateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_dbcluster_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: adb_20190315_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL cluster.
        
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
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: adb_20190315_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL cluster.
        
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
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: adb_20190315_models.ModifyAccountDescriptionRequest,
    ) -> adb_20190315_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: adb_20190315_models.ModifyAccountDescriptionRequest,
    ) -> adb_20190315_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: adb_20190315_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary Changes the time configuration of O\\&M events.
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not UtilClient.is_unset(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationMaintainConf',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_maintain_conf_with_options_async(
        self,
        request: adb_20190315_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary Changes the time configuration of O\\&M events.
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationMaintainConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not UtilClient.is_unset(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationMaintainConf',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_maintain_conf(
        self,
        request: adb_20190315_models.ModifyActiveOperationMaintainConfRequest,
    ) -> adb_20190315_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary Changes the time configuration of O\\&M events.
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @return: ModifyActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    async def modify_active_operation_maintain_conf_async(
        self,
        request: adb_20190315_models.ModifyActiveOperationMaintainConfRequest,
    ) -> adb_20190315_models.ModifyActiveOperationMaintainConfResponse:
        """
        @summary Changes the time configuration of O\\&M events.
        
        @param request: ModifyActiveOperationMaintainConfRequest
        @return: ModifyActiveOperationMaintainConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_maintain_conf_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: adb_20190315_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyActiveOperationTasksResponse:
        """
        @summary Changes the execution time of O&M events.
        
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: adb_20190315_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyActiveOperationTasksResponse:
        """
        @summary Changes the execution time of O&M events.
        
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: adb_20190315_models.ModifyActiveOperationTasksRequest,
    ) -> adb_20190315_models.ModifyActiveOperationTasksResponse:
        """
        @summary Changes the execution time of O&M events.
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: adb_20190315_models.ModifyActiveOperationTasksRequest,
    ) -> adb_20190315_models.ModifyActiveOperationTasksResponse:
        """
        @summary Changes the execution time of O&M events.
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: adb_20190315_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAuditLogConfigResponse:
        """
        @summary 修改审计日志设置
        
        @param request: ModifyAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='ModifyAuditLogConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: adb_20190315_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAuditLogConfigResponse:
        """
        @summary 修改审计日志设置
        
        @param request: ModifyAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action='ModifyAuditLogConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: adb_20190315_models.ModifyAuditLogConfigRequest,
    ) -> adb_20190315_models.ModifyAuditLogConfigResponse:
        """
        @summary 修改审计日志设置
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: adb_20190315_models.ModifyAuditLogConfigRequest,
    ) -> adb_20190315_models.ModifyAuditLogConfigResponse:
        """
        @summary 修改审计日志设置
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_auto_renew_attribute_with_options(
        self,
        request: adb_20190315_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoRenewAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_renew_attribute_with_options_async(
        self,
        request: adb_20190315_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoRenewAttribute',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_renew_attribute(
        self,
        request: adb_20190315_models.ModifyAutoRenewAttributeRequest,
    ) -> adb_20190315_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @return: ModifyAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    async def modify_auto_renew_attribute_async(
        self,
        request: adb_20190315_models.ModifyAutoRenewAttributeRequest,
    ) -> adb_20190315_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal status of a subscription AnalyticDB for MySQL cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @return: ModifyAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_renew_attribute_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: adb_20190315_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyBackupPolicyResponse:
        """
        @summary 修改全量备份策略
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: adb_20190315_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyBackupPolicyResponse:
        """
        @summary 修改全量备份策略
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: adb_20190315_models.ModifyBackupPolicyRequest,
    ) -> adb_20190315_models.ModifyBackupPolicyResponse:
        """
        @summary 修改全量备份策略
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: adb_20190315_models.ModifyBackupPolicyRequest,
    ) -> adb_20190315_models.ModifyBackupPolicyResponse:
        """
        @summary 修改全量备份策略
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_connection_string_with_options(
        self,
        request: adb_20190315_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyClusterConnectionStringResponse:
        """
        @summary Changes the endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyClusterConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyClusterConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_connection_string_with_options_async(
        self,
        request: adb_20190315_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyClusterConnectionStringResponse:
        """
        @summary Changes the endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyClusterConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyClusterConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_connection_string(
        self,
        request: adb_20190315_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20190315_models.ModifyClusterConnectionStringResponse:
        """
        @summary Changes the endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyClusterConnectionStringRequest
        @return: ModifyClusterConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_connection_string_with_options(request, runtime)

    async def modify_cluster_connection_string_async(
        self,
        request: adb_20190315_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20190315_models.ModifyClusterConnectionStringResponse:
        """
        @summary Changes the endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyClusterConnectionStringRequest
        @return: ModifyClusterConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_connection_string_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterResponse:
        """
        @summary Changes the specifications of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not UtilClient.is_unset(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not UtilClient.is_unset(request.elastic_ioresource_size):
            query['ElasticIOResourceSize'] = request.elastic_ioresource_size
        if not UtilClient.is_unset(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
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
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterResponse:
        """
        @summary Changes the specifications of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not UtilClient.is_unset(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not UtilClient.is_unset(request.elastic_ioresource_size):
            query['ElasticIOResourceSize'] = request.elastic_ioresource_size
        if not UtilClient.is_unset(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
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
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: adb_20190315_models.ModifyDBClusterRequest,
    ) -> adb_20190315_models.ModifyDBClusterResponse:
        """
        @summary Changes the specifications of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: adb_20190315_models.ModifyDBClusterRequest,
    ) -> adb_20190315_models.ModifyDBClusterResponse:
        """
        @summary Changes the specifications of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelists of a cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelists of a cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: adb_20190315_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> adb_20190315_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelists of a cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: adb_20190315_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> adb_20190315_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelists of a cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterDescriptionResponse:
        """
        @summary 修改备注
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterDescriptionResponse:
        """
        @summary 修改备注
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: adb_20190315_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20190315_models.ModifyDBClusterDescriptionResponse:
        """
        @summary 修改备注
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: adb_20190315_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20190315_models.ModifyDBClusterDescriptionResponse:
        """
        @summary 修改备注
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Changes the maintenance window of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Changes the maintenance window of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: adb_20190315_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20190315_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Changes the maintenance window of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: adb_20190315_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20190315_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Changes the maintenance window of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbcluster_pay_type_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterPayType',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_pay_type_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterPayType',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_pay_type(
        self,
        request: adb_20190315_models.ModifyDBClusterPayTypeRequest,
    ) -> adb_20190315_models.ModifyDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterPayTypeRequest
        @return: ModifyDBClusterPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_pay_type_with_options(request, runtime)

    async def modify_dbcluster_pay_type_async(
        self,
        request: adb_20190315_models.ModifyDBClusterPayTypeRequest,
    ) -> adb_20190315_models.ModifyDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterPayTypeRequest
        @return: ModifyDBClusterPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_pay_type_with_options_async(request, runtime)

    def modify_dbcluster_resource_group_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterResourceGroupResponse:
        """
        @summary Modifies the resource group of an AnalyticDB for MySQL cluster.
        
        @description Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475#concept-zyn-3p1-dhb~~ "Resource Management provides a collection of resource management services that support enterprise IT administration. The services include Resource Directory, Resource Group, and Tag. Resource Directory allows you to build an organizational structure for resources based on your business requirements. Resource Group and Tag allow you to hierarchically manage the resources. Resource Sharing allows you to share the resources among your accounts.")
        
        @param request: ModifyDBClusterResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_resource_group_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterResourceGroupResponse:
        """
        @summary Modifies the resource group of an AnalyticDB for MySQL cluster.
        
        @description Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475#concept-zyn-3p1-dhb~~ "Resource Management provides a collection of resource management services that support enterprise IT administration. The services include Resource Directory, Resource Group, and Tag. Resource Directory allows you to build an organizational structure for resources based on your business requirements. Resource Group and Tag allow you to hierarchically manage the resources. Resource Sharing allows you to share the resources among your accounts.")
        
        @param request: ModifyDBClusterResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_resource_group(
        self,
        request: adb_20190315_models.ModifyDBClusterResourceGroupRequest,
    ) -> adb_20190315_models.ModifyDBClusterResourceGroupResponse:
        """
        @summary Modifies the resource group of an AnalyticDB for MySQL cluster.
        
        @description Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475#concept-zyn-3p1-dhb~~ "Resource Management provides a collection of resource management services that support enterprise IT administration. The services include Resource Directory, Resource Group, and Tag. Resource Directory allows you to build an organizational structure for resources based on your business requirements. Resource Group and Tag allow you to hierarchically manage the resources. Resource Sharing allows you to share the resources among your accounts.")
        
        @param request: ModifyDBClusterResourceGroupRequest
        @return: ModifyDBClusterResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_resource_group_with_options(request, runtime)

    async def modify_dbcluster_resource_group_async(
        self,
        request: adb_20190315_models.ModifyDBClusterResourceGroupRequest,
    ) -> adb_20190315_models.ModifyDBClusterResourceGroupResponse:
        """
        @summary Modifies the resource group of an AnalyticDB for MySQL cluster.
        
        @description Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475#concept-zyn-3p1-dhb~~ "Resource Management provides a collection of resource management services that support enterprise IT administration. The services include Resource Directory, Resource Group, and Tag. Resource Directory allows you to build an organizational structure for resources based on your business requirements. Resource Group and Tag allow you to hierarchically manage the resources. Resource Sharing allows you to share the resources among your accounts.")
        
        @param request: ModifyDBClusterResourceGroupRequest
        @return: ModifyDBClusterResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_resource_group_with_options_async(request, runtime)

    def modify_dbcluster_sslwith_options(
        self,
        request: adb_20190315_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterSSLResponse:
        """
        @summary Modifies the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterSSL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_sslwith_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterSSLResponse:
        """
        @summary Modifies the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterSSL',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_ssl(
        self,
        request: adb_20190315_models.ModifyDBClusterSSLRequest,
    ) -> adb_20190315_models.ModifyDBClusterSSLResponse:
        """
        @summary Modifies the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @return: ModifyDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_sslwith_options(request, runtime)

    async def modify_dbcluster_ssl_async(
        self,
        request: adb_20190315_models.ModifyDBClusterSSLRequest,
    ) -> adb_20190315_models.ModifyDBClusterSSLResponse:
        """
        @summary Modifies the SSL configurations of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @return: ModifyDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_sslwith_options_async(request, runtime)

    def modify_dbcluster_shard_number_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterShardNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterShardNumberResponse:
        """
        @summary Changes the number of shards for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterShardNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterShardNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
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
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterShardNumber',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterShardNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_shard_number_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterShardNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterShardNumberResponse:
        """
        @summary Changes the number of shards for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterShardNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterShardNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
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
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterShardNumber',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterShardNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_shard_number(
        self,
        request: adb_20190315_models.ModifyDBClusterShardNumberRequest,
    ) -> adb_20190315_models.ModifyDBClusterShardNumberResponse:
        """
        @summary Changes the number of shards for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterShardNumberRequest
        @return: ModifyDBClusterShardNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_shard_number_with_options(request, runtime)

    async def modify_dbcluster_shard_number_async(
        self,
        request: adb_20190315_models.ModifyDBClusterShardNumberRequest,
    ) -> adb_20190315_models.ModifyDBClusterShardNumberResponse:
        """
        @summary Changes the number of shards for an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterShardNumberRequest
        @return: ModifyDBClusterShardNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_shard_number_with_options_async(request, runtime)

    def modify_dbcluster_vip_with_options(
        self,
        request: adb_20190315_models.ModifyDBClusterVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterVipResponse:
        """
        @summary Changes the virtual IP address (VIP) that is used to connect to an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterVipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterVipResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterVip',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterVipResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_vip_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBClusterVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBClusterVipResponse:
        """
        @summary Changes the virtual IP address (VIP) that is used to connect to an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterVipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterVipResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterVip',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBClusterVipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_vip(
        self,
        request: adb_20190315_models.ModifyDBClusterVipRequest,
    ) -> adb_20190315_models.ModifyDBClusterVipResponse:
        """
        @summary Changes the virtual IP address (VIP) that is used to connect to an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterVipRequest
        @return: ModifyDBClusterVipResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_vip_with_options(request, runtime)

    async def modify_dbcluster_vip_async(
        self,
        request: adb_20190315_models.ModifyDBClusterVipRequest,
    ) -> adb_20190315_models.ModifyDBClusterVipResponse:
        """
        @summary Changes the virtual IP address (VIP) that is used to connect to an AnalyticDB for MySQL cluster.
        
        @param request: ModifyDBClusterVipRequest
        @return: ModifyDBClusterVipResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_vip_with_options_async(request, runtime)

    def modify_dbresource_group_with_options(
        self,
        tmp_req: adb_20190315_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the number of nodes or the query execution mode for a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more. The number of nodes cannot be modified for the default resource group USER_DEFAULT.
        
        @param tmp_req: ModifyDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.ModifyDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.engine_params):
            request.engine_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        if not UtilClient.is_unset(tmp_req.pool_user_list):
            request.pool_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pool_user_list, 'PoolUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_user_list_shrink):
            query['PoolUserList'] = request.pool_user_list_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_group_with_options_async(
        self,
        tmp_req: adb_20190315_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the number of nodes or the query execution mode for a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more. The number of nodes cannot be modified for the default resource group USER_DEFAULT.
        
        @param tmp_req: ModifyDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.ModifyDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.engine_params):
            request.engine_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        if not UtilClient.is_unset(tmp_req.pool_user_list):
            request.pool_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pool_user_list, 'PoolUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_user_list_shrink):
            query['PoolUserList'] = request.pool_user_list_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_group(
        self,
        request: adb_20190315_models.ModifyDBResourceGroupRequest,
    ) -> adb_20190315_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the number of nodes or the query execution mode for a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more. The number of nodes cannot be modified for the default resource group USER_DEFAULT.
        
        @param request: ModifyDBResourceGroupRequest
        @return: ModifyDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    async def modify_dbresource_group_async(
        self,
        request: adb_20190315_models.ModifyDBResourceGroupRequest,
    ) -> adb_20190315_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the number of nodes or the query execution mode for a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        
        @description This operation is suitable for the following editions:
        **Enterprise Edition**.
        **Basic Edition**.
        **Data Lakehouse Edition**.
        **Data Warehouse Edition in elastic mode**: 32 cores and 128 GB or more. The number of nodes cannot be modified for the default resource group USER_DEFAULT.
        
        @param request: ModifyDBResourceGroupRequest
        @return: ModifyDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbresource_group_with_options_async(request, runtime)

    def modify_dbresource_pool_with_options(
        self,
        request: adb_20190315_models.ModifyDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBResourcePoolResponse:
        """
        @summary Modifies the resources of a resource group. This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for elastic clusters of 32 cores or more.
        You cannot change the number of nodes for the USER_DEFAULT resource group.
        
        @param request: ModifyDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_pool_with_options_async(
        self,
        request: adb_20190315_models.ModifyDBResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyDBResourcePoolResponse:
        """
        @summary Modifies the resources of a resource group. This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for elastic clusters of 32 cores or more.
        You cannot change the number of nodes for the USER_DEFAULT resource group.
        
        @param request: ModifyDBResourcePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourcePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_num):
            query['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourcePool',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_pool(
        self,
        request: adb_20190315_models.ModifyDBResourcePoolRequest,
    ) -> adb_20190315_models.ModifyDBResourcePoolResponse:
        """
        @summary Modifies the resources of a resource group. This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for elastic clusters of 32 cores or more.
        You cannot change the number of nodes for the USER_DEFAULT resource group.
        
        @param request: ModifyDBResourcePoolRequest
        @return: ModifyDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_pool_with_options(request, runtime)

    async def modify_dbresource_pool_async(
        self,
        request: adb_20190315_models.ModifyDBResourcePoolRequest,
    ) -> adb_20190315_models.ModifyDBResourcePoolResponse:
        """
        @summary Modifies the resources of a resource group. This operation is available only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description ###
        You can call this operation only for elastic clusters of 32 cores or more.
        You cannot change the number of nodes for the USER_DEFAULT resource group.
        
        @param request: ModifyDBResourcePoolRequest
        @return: ModifyDBResourcePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbresource_pool_with_options_async(request, runtime)

    def modify_elastic_plan_with_options(
        self,
        request: adb_20190315_models.ModifyElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: ModifyElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not UtilClient.is_unset(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not UtilClient.is_unset(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not UtilClient.is_unset(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not UtilClient.is_unset(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not UtilClient.is_unset(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not UtilClient.is_unset(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not UtilClient.is_unset(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_plan_with_options_async(
        self,
        request: adb_20190315_models.ModifyElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: ModifyElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not UtilClient.is_unset(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not UtilClient.is_unset(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not UtilClient.is_unset(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not UtilClient.is_unset(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not UtilClient.is_unset(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not UtilClient.is_unset(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not UtilClient.is_unset(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not UtilClient.is_unset(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticPlan',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_plan(
        self,
        request: adb_20190315_models.ModifyElasticPlanRequest,
    ) -> adb_20190315_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: ModifyElasticPlanRequest
        @return: ModifyElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_plan_with_options(request, runtime)

    async def modify_elastic_plan_async(
        self,
        request: adb_20190315_models.ModifyElasticPlanRequest,
    ) -> adb_20190315_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scheduled scaling plan. This operation can be used only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @description You can call this operation only for AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters in elastic mode for Cluster Edition that have 32 cores or more.
        
        @param request: ModifyElasticPlanRequest
        @return: ModifyElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_plan_with_options_async(request, runtime)

    def modify_log_backup_policy_with_options(
        self,
        request: adb_20190315_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the log backup settings of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyLogBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_backup_policy_with_options_async(
        self,
        request: adb_20190315_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the log backup settings of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogBackupPolicy',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyLogBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_backup_policy(
        self,
        request: adb_20190315_models.ModifyLogBackupPolicyRequest,
    ) -> adb_20190315_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the log backup settings of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @return: ModifyLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_log_backup_policy_with_options(request, runtime)

    async def modify_log_backup_policy_async(
        self,
        request: adb_20190315_models.ModifyLogBackupPolicyRequest,
    ) -> adb_20190315_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the log backup settings of an AnalyticDB for MySQL cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @return: ModifyLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_backup_policy_with_options_async(request, runtime)

    def modify_log_hub_status_with_options(
        self,
        request: adb_20190315_models.ModifyLogHubStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyLogHubStatusResponse:
        """
        @summary Changes the status of a log shipping job.
        
        @param request: ModifyLogHubStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogHubStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogHubStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyLogHubStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_hub_status_with_options_async(
        self,
        request: adb_20190315_models.ModifyLogHubStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyLogHubStatusResponse:
        """
        @summary Changes the status of a log shipping job.
        
        @param request: ModifyLogHubStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogHubStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogHubStatus',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyLogHubStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_hub_status(
        self,
        request: adb_20190315_models.ModifyLogHubStatusRequest,
    ) -> adb_20190315_models.ModifyLogHubStatusResponse:
        """
        @summary Changes the status of a log shipping job.
        
        @param request: ModifyLogHubStatusRequest
        @return: ModifyLogHubStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_log_hub_status_with_options(request, runtime)

    async def modify_log_hub_status_async(
        self,
        request: adb_20190315_models.ModifyLogHubStatusRequest,
    ) -> adb_20190315_models.ModifyLogHubStatusResponse:
        """
        @summary Changes the status of a log shipping job.
        
        @param request: ModifyLogHubStatusRequest
        @return: ModifyLogHubStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_hub_status_with_options_async(request, runtime)

    def modify_maintenance_action_with_options(
        self,
        request: adb_20190315_models.ModifyMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyMaintenanceActionResponse:
        """
        @summary Changes the switchover time of O&M events.
        
        @param request: ModifyMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMaintenanceAction',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_maintenance_action_with_options_async(
        self,
        request: adb_20190315_models.ModifyMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyMaintenanceActionResponse:
        """
        @summary Changes the switchover time of O&M events.
        
        @param request: ModifyMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMaintenanceAction',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_maintenance_action(
        self,
        request: adb_20190315_models.ModifyMaintenanceActionRequest,
    ) -> adb_20190315_models.ModifyMaintenanceActionResponse:
        """
        @summary Changes the switchover time of O&M events.
        
        @param request: ModifyMaintenanceActionRequest
        @return: ModifyMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_maintenance_action_with_options(request, runtime)

    async def modify_maintenance_action_async(
        self,
        request: adb_20190315_models.ModifyMaintenanceActionRequest,
    ) -> adb_20190315_models.ModifyMaintenanceActionResponse:
        """
        @summary Changes the switchover time of O&M events.
        
        @param request: ModifyMaintenanceActionRequest
        @return: ModifyMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_maintenance_action_with_options_async(request, runtime)

    def modify_resubmit_config_with_options(
        self,
        tmp_req: adb_20190315_models.ModifyResubmitConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyResubmitConfigResponse:
        """
        @summary 修改Resubmit配置
        
        @param tmp_req: ModifyResubmitConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResubmitConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.ModifyResubmitConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResubmitConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyResubmitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resubmit_config_with_options_async(
        self,
        tmp_req: adb_20190315_models.ModifyResubmitConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifyResubmitConfigResponse:
        """
        @summary 修改Resubmit配置
        
        @param tmp_req: ModifyResubmitConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResubmitConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20190315_models.ModifyResubmitConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResubmitConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifyResubmitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resubmit_config(
        self,
        request: adb_20190315_models.ModifyResubmitConfigRequest,
    ) -> adb_20190315_models.ModifyResubmitConfigResponse:
        """
        @summary 修改Resubmit配置
        
        @param request: ModifyResubmitConfigRequest
        @return: ModifyResubmitConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_resubmit_config_with_options(request, runtime)

    async def modify_resubmit_config_async(
        self,
        request: adb_20190315_models.ModifyResubmitConfigRequest,
    ) -> adb_20190315_models.ModifyResubmitConfigResponse:
        """
        @summary 修改Resubmit配置
        
        @param request: ModifyResubmitConfigRequest
        @return: ModifyResubmitConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_resubmit_config_with_options_async(request, runtime)

    def modify_sqaconfig_with_options(
        self,
        request: adb_20190315_models.ModifySQAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifySQAConfigResponse:
        """
        @summary 修改SQA配置
        
        @param request: ModifySQAConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySQAConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqastatus):
            query['SQAStatus'] = request.sqastatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQAConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifySQAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqaconfig_with_options_async(
        self,
        request: adb_20190315_models.ModifySQAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifySQAConfigResponse:
        """
        @summary 修改SQA配置
        
        @param request: ModifySQAConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySQAConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqastatus):
            query['SQAStatus'] = request.sqastatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQAConfig',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifySQAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sqaconfig(
        self,
        request: adb_20190315_models.ModifySQAConfigRequest,
    ) -> adb_20190315_models.ModifySQAConfigResponse:
        """
        @summary 修改SQA配置
        
        @param request: ModifySQAConfigRequest
        @return: ModifySQAConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sqaconfig_with_options(request, runtime)

    async def modify_sqaconfig_async(
        self,
        request: adb_20190315_models.ModifySQAConfigRequest,
    ) -> adb_20190315_models.ModifySQAConfigResponse:
        """
        @summary 修改SQA配置
        
        @param request: ModifySQAConfigRequest
        @return: ModifySQAConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqaconfig_with_options_async(request, runtime)

    def modify_sync_job_with_options(
        self,
        request: adb_20190315_models.ModifySyncJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifySyncJobResponse:
        """
        @summary Modifies the synchronization jobs for an AnalyticDB for MySQL cluster.
        
        @param request: ModifySyncJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySyncJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not UtilClient.is_unset(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySyncJob',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifySyncJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sync_job_with_options_async(
        self,
        request: adb_20190315_models.ModifySyncJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ModifySyncJobResponse:
        """
        @summary Modifies the synchronization jobs for an AnalyticDB for MySQL cluster.
        
        @param request: ModifySyncJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySyncJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not UtilClient.is_unset(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not UtilClient.is_unset(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySyncJob',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ModifySyncJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sync_job(
        self,
        request: adb_20190315_models.ModifySyncJobRequest,
    ) -> adb_20190315_models.ModifySyncJobResponse:
        """
        @summary Modifies the synchronization jobs for an AnalyticDB for MySQL cluster.
        
        @param request: ModifySyncJobRequest
        @return: ModifySyncJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sync_job_with_options(request, runtime)

    async def modify_sync_job_async(
        self,
        request: adb_20190315_models.ModifySyncJobRequest,
    ) -> adb_20190315_models.ModifySyncJobResponse:
        """
        @summary Modifies the synchronization jobs for an AnalyticDB for MySQL cluster.
        
        @param request: ModifySyncJobRequest
        @return: ModifySyncJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_sync_job_with_options_async(request, runtime)

    def operate_log_hub_with_options(
        self,
        request: adb_20190315_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.OperateLogHubResponse:
        """
        @summary 修改LogHub投递规则
        
        @param request: OperateLogHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateLogHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create):
            query['Create'] = request.create
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.deliver_time):
            query['DeliverTime'] = request.deliver_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.filter_dirty_data):
            query['FilterDirtyData'] = request.filter_dirty_data
        if not UtilClient.is_unset(request.log_hub_stores):
            query['LogHubStores'] = request.log_hub_stores
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateLogHub',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.OperateLogHubResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_log_hub_with_options_async(
        self,
        request: adb_20190315_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.OperateLogHubResponse:
        """
        @summary 修改LogHub投递规则
        
        @param request: OperateLogHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateLogHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create):
            query['Create'] = request.create
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not UtilClient.is_unset(request.deliver_time):
            query['DeliverTime'] = request.deliver_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.filter_dirty_data):
            query['FilterDirtyData'] = request.filter_dirty_data
        if not UtilClient.is_unset(request.log_hub_stores):
            query['LogHubStores'] = request.log_hub_stores
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateLogHub',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.OperateLogHubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_log_hub(
        self,
        request: adb_20190315_models.OperateLogHubRequest,
    ) -> adb_20190315_models.OperateLogHubResponse:
        """
        @summary 修改LogHub投递规则
        
        @param request: OperateLogHubRequest
        @return: OperateLogHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    async def operate_log_hub_async(
        self,
        request: adb_20190315_models.OperateLogHubRequest,
    ) -> adb_20190315_models.OperateLogHubResponse:
        """
        @summary 修改LogHub投递规则
        
        @param request: OperateLogHubRequest
        @return: OperateLogHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_log_hub_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: adb_20190315_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: adb_20190315_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: adb_20190315_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20190315_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: adb_20190315_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20190315_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: adb_20190315_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL cluster.
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: adb_20190315_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL cluster.
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: adb_20190315_models.ResetAccountPasswordRequest,
    ) -> adb_20190315_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: adb_20190315_models.ResetAccountPasswordRequest,
    ) -> adb_20190315_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def revoke_operator_permission_with_options(
        self,
        request: adb_20190315_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.RevokeOperatorPermissionResponse:
        """
        @summary 取消服务帐号授权
        
        @param request: RevokeOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.RevokeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_operator_permission_with_options_async(
        self,
        request: adb_20190315_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.RevokeOperatorPermissionResponse:
        """
        @summary 取消服务帐号授权
        
        @param request: RevokeOperatorPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.RevokeOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_operator_permission(
        self,
        request: adb_20190315_models.RevokeOperatorPermissionRequest,
    ) -> adb_20190315_models.RevokeOperatorPermissionResponse:
        """
        @summary 取消服务帐号授权
        
        @param request: RevokeOperatorPermissionRequest
        @return: RevokeOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    async def revoke_operator_permission_async(
        self,
        request: adb_20190315_models.RevokeOperatorPermissionRequest,
    ) -> adb_20190315_models.RevokeOperatorPermissionResponse:
        """
        @summary 取消服务帐号授权
        
        @param request: RevokeOperatorPermissionRequest
        @return: RevokeOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_operator_permission_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: adb_20190315_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.TagResourcesResponse:
        """
        @summary Adds tags to an AnalyticDB for MySQL cluster.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: adb_20190315_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.TagResourcesResponse:
        """
        @summary Adds tags to an AnalyticDB for MySQL cluster.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: adb_20190315_models.TagResourcesRequest,
    ) -> adb_20190315_models.TagResourcesResponse:
        """
        @summary Adds tags to an AnalyticDB for MySQL cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: adb_20190315_models.TagResourcesRequest,
    ) -> adb_20190315_models.TagResourcesResponse:
        """
        @summary Adds tags to an AnalyticDB for MySQL cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unbind_dbresource_group_with_user_with_options(
        self,
        request: adb_20190315_models.UnbindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster from a database account.
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourceGroupWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UnbindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_group_with_user_with_options_async(
        self,
        request: adb_20190315_models.UnbindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster from a database account.
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourceGroupWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UnbindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_group_with_user(
        self,
        request: adb_20190315_models.UnbindDBResourceGroupWithUserRequest,
    ) -> adb_20190315_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster from a database account.
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @return: UnbindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_dbresource_group_with_user_with_options(request, runtime)

    async def unbind_dbresource_group_with_user_async(
        self,
        request: adb_20190315_models.UnbindDBResourceGroupWithUserRequest,
    ) -> adb_20190315_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates a resource group of an AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster from a database account.
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @return: UnbindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_dbresource_group_with_user_with_options_async(request, runtime)

    def unbind_dbresource_pool_with_user_with_options(
        self,
        request: adb_20190315_models.UnbindDBResourcePoolWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UnbindDBResourcePoolWithUserResponse:
        """
        @summary Disassociates a database account from a resource group. This operation can be called only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @param request: UnbindDBResourcePoolWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourcePoolWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourcePoolWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UnbindDBResourcePoolWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_pool_with_user_with_options_async(
        self,
        request: adb_20190315_models.UnbindDBResourcePoolWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UnbindDBResourcePoolWithUserResponse:
        """
        @summary Disassociates a database account from a resource group. This operation can be called only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @param request: UnbindDBResourcePoolWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourcePoolWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourcePoolWithUser',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UnbindDBResourcePoolWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_pool_with_user(
        self,
        request: adb_20190315_models.UnbindDBResourcePoolWithUserRequest,
    ) -> adb_20190315_models.UnbindDBResourcePoolWithUserResponse:
        """
        @summary Disassociates a database account from a resource group. This operation can be called only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @param request: UnbindDBResourcePoolWithUserRequest
        @return: UnbindDBResourcePoolWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_dbresource_pool_with_user_with_options(request, runtime)

    async def unbind_dbresource_pool_with_user_async(
        self,
        request: adb_20190315_models.UnbindDBResourcePoolWithUserRequest,
    ) -> adb_20190315_models.UnbindDBResourcePoolWithUserResponse:
        """
        @summary Disassociates a database account from a resource group. This operation can be called only for AnalyticDB for MySQL clusters in elastic mode for Cluster Edition.
        
        @param request: UnbindDBResourcePoolWithUserRequest
        @return: UnbindDBResourcePoolWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_dbresource_pool_with_user_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: adb_20190315_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UntagResourcesResponse:
        """
        @summary Removes all tags from AnalyticDB for MySQL clusters.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: adb_20190315_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UntagResourcesResponse:
        """
        @summary Removes all tags from AnalyticDB for MySQL clusters.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: adb_20190315_models.UntagResourcesRequest,
    ) -> adb_20190315_models.UntagResourcesResponse:
        """
        @summary Removes all tags from AnalyticDB for MySQL clusters.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: adb_20190315_models.UntagResourcesRequest,
    ) -> adb_20190315_models.UntagResourcesResponse:
        """
        @summary Removes all tags from AnalyticDB for MySQL clusters.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_kernel_version_with_options(
        self,
        request: adb_20190315_models.UpgradeKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UpgradeKernelVersionResponse:
        """
        @summary Updates the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: UpgradeKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeKernelVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UpgradeKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_kernel_version_with_options_async(
        self,
        request: adb_20190315_models.UpgradeKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20190315_models.UpgradeKernelVersionResponse:
        """
        @summary Updates the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: UpgradeKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeKernelVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20190315_models.UpgradeKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_kernel_version(
        self,
        request: adb_20190315_models.UpgradeKernelVersionRequest,
    ) -> adb_20190315_models.UpgradeKernelVersionResponse:
        """
        @summary Updates the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: UpgradeKernelVersionRequest
        @return: UpgradeKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_kernel_version_with_options(request, runtime)

    async def upgrade_kernel_version_async(
        self,
        request: adb_20190315_models.UpgradeKernelVersionRequest,
    ) -> adb_20190315_models.UpgradeKernelVersionResponse:
        """
        @summary Updates the minor version of an AnalyticDB for MySQL cluster.
        
        @param request: UpgradeKernelVersionRequest
        @return: UpgradeKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_kernel_version_with_options_async(request, runtime)
