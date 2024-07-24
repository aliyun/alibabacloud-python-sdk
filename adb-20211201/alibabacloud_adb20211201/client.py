# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adb20211201 import models as adb_20211201_models
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
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def attach_user_eniwith_options(
        self,
        request: adb_20211201_models.AttachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AttachUserENIResponse:
        """
        @summary Attaches an elastic network interface (ENI) to an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AttachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachUserENI',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AttachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_user_eniwith_options_async(
        self,
        request: adb_20211201_models.AttachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AttachUserENIResponse:
        """
        @summary Attaches an elastic network interface (ENI) to an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AttachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachUserENI',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AttachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_user_eni(
        self,
        request: adb_20211201_models.AttachUserENIRequest,
    ) -> adb_20211201_models.AttachUserENIResponse:
        """
        @summary Attaches an elastic network interface (ENI) to an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AttachUserENIRequest
        @return: AttachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_user_eniwith_options(request, runtime)

    async def attach_user_eni_async(
        self,
        request: adb_20211201_models.AttachUserENIRequest,
    ) -> adb_20211201_models.AttachUserENIResponse:
        """
        @summary Attaches an elastic network interface (ENI) to an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: AttachUserENIRequest
        @return: AttachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_user_eniwith_options_async(request, runtime)

    def bind_account_with_options(
        self,
        request: adb_20211201_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindAccountResponse:
        """
        @summary Associates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_with_options_async(
        self,
        request: adb_20211201_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindAccountResponse:
        """
        @summary Associates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account(
        self,
        request: adb_20211201_models.BindAccountRequest,
    ) -> adb_20211201_models.BindAccountResponse:
        """
        @summary Associates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindAccountRequest
        @return: BindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_account_with_options(request, runtime)

    async def bind_account_async(
        self,
        request: adb_20211201_models.BindAccountRequest,
    ) -> adb_20211201_models.BindAccountResponse:
        """
        @summary Associates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindAccountRequest
        @return: BindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_account_with_options_async(request, runtime)

    def bind_dbresource_group_with_user_with_options(
        self,
        request: adb_20211201_models.BindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group with a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourceGroupWithUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_group_with_user_with_options_async(
        self,
        request: adb_20211201_models.BindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group with a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDBResourceGroupWithUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_group_with_user(
        self,
        request: adb_20211201_models.BindDBResourceGroupWithUserRequest,
    ) -> adb_20211201_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group with a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindDBResourceGroupWithUserRequest
        @return: BindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_dbresource_group_with_user_with_options(request, runtime)

    async def bind_dbresource_group_with_user_async(
        self,
        request: adb_20211201_models.BindDBResourceGroupWithUserRequest,
    ) -> adb_20211201_models.BindDBResourceGroupWithUserResponse:
        """
        @summary Associates a resource group with a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: BindDBResourceGroupWithUserRequest
        @return: BindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_dbresource_group_with_user_with_options_async(request, runtime)

    def check_bind_ram_user_with_options(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        """
        @summary Queries whether a database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster is associated with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckBindRamUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckBindRamUserResponse
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
            action='CheckBindRamUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckBindRamUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_bind_ram_user_with_options_async(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        """
        @summary Queries whether a database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster is associated with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckBindRamUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckBindRamUserResponse
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
            action='CheckBindRamUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckBindRamUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_bind_ram_user(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        """
        @summary Queries whether a database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster is associated with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckBindRamUserRequest
        @return: CheckBindRamUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_bind_ram_user_with_options(request, runtime)

    async def check_bind_ram_user_async(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        """
        @summary Queries whether a database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster is associated with a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckBindRamUserRequest
        @return: CheckBindRamUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_bind_ram_user_with_options_async(request, runtime)

    def check_sample_data_set_with_options(
        self,
        request: adb_20211201_models.CheckSampleDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckSampleDataSetResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckSampleDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSampleDataSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSampleDataSet',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckSampleDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sample_data_set_with_options_async(
        self,
        request: adb_20211201_models.CheckSampleDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckSampleDataSetResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckSampleDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSampleDataSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSampleDataSet',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckSampleDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sample_data_set(
        self,
        request: adb_20211201_models.CheckSampleDataSetRequest,
    ) -> adb_20211201_models.CheckSampleDataSetResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckSampleDataSetRequest
        @return: CheckSampleDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_sample_data_set_with_options(request, runtime)

    async def check_sample_data_set_async(
        self,
        request: adb_20211201_models.CheckSampleDataSetRequest,
    ) -> adb_20211201_models.CheckSampleDataSetResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CheckSampleDataSetRequest
        @return: CheckSampleDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_sample_data_set_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: adb_20211201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: adb_20211201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: adb_20211201_models.CreateAccountRequest,
    ) -> adb_20211201_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: adb_20211201_models.CreateAccountRequest,
    ) -> adb_20211201_models.CreateAccountResponse:
        """
        @summary Creates a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.kms_id):
            query['KmsId'] = request.kms_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_form):
            query['ProductForm'] = request.product_form
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.restore_to_time):
            query['RestoreToTime'] = request.restore_to_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.kms_id):
            query['KmsId'] = request.kms_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_form):
            query['ProductForm'] = request.product_form
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.restore_to_time):
            query['RestoreToTime'] = request.restore_to_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        """
        @summary Creates an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbresource_group_with_options(
        self,
        tmp_req: adb_20211201_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param tmp_req: CreateDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.CreateDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_group_with_options_async(
        self,
        tmp_req: adb_20211201_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param tmp_req: CreateDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.CreateDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_group(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: CreateDBResourceGroupRequest
        @return: CreateDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    async def create_dbresource_group_async(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        """
        @summary Creates a resource group for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: CreateDBResourceGroupRequest
        @return: CreateDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbresource_group_with_options_async(request, runtime)

    def create_elastic_plan_with_options(
        self,
        request: adb_20211201_models.CreateElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateElasticPlanResponse:
        """
        @summary Creates a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_scale):
            query['AutoScale'] = request.auto_scale
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_size):
            query['TargetSize'] = request.target_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_plan_with_options_async(
        self,
        request: adb_20211201_models.CreateElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateElasticPlanResponse:
        """
        @summary Creates a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_scale):
            query['AutoScale'] = request.auto_scale
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_size):
            query['TargetSize'] = request.target_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_plan(
        self,
        request: adb_20211201_models.CreateElasticPlanRequest,
    ) -> adb_20211201_models.CreateElasticPlanResponse:
        """
        @summary Creates a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateElasticPlanRequest
        @return: CreateElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_plan_with_options(request, runtime)

    async def create_elastic_plan_async(
        self,
        request: adb_20211201_models.CreateElasticPlanRequest,
    ) -> adb_20211201_models.CreateElasticPlanResponse:
        """
        @summary Creates a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: CreateElasticPlanRequest
        @return: CreateElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_elastic_plan_with_options_async(request, runtime)

    def create_oss_sub_directory_with_options(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        """
        @summary Creates an Object Storage Service (OSS) subdirectory.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateOssSubDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssSubDirectoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssSubDirectory',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateOssSubDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_sub_directory_with_options_async(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        """
        @summary Creates an Object Storage Service (OSS) subdirectory.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateOssSubDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssSubDirectoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssSubDirectory',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateOssSubDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_sub_directory(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        """
        @summary Creates an Object Storage Service (OSS) subdirectory.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateOssSubDirectoryRequest
        @return: CreateOssSubDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oss_sub_directory_with_options(request, runtime)

    async def create_oss_sub_directory_async(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        """
        @summary Creates an Object Storage Service (OSS) subdirectory.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateOssSubDirectoryRequest
        @return: CreateOssSubDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oss_sub_directory_with_options_async(request, runtime)

    def create_performance_view_with_options(
        self,
        tmp_req: adb_20211201_models.CreatePerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreatePerformanceViewResponse:
        """
        @param tmp_req: CreatePerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePerformanceViewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.CreatePerformanceViewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_detail):
            request.view_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_from_view_type):
            query['CreateFromViewType'] = request.create_from_view_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.fill_origin_view_keys):
            query['FillOriginViewKeys'] = request.fill_origin_view_keys
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
        if not UtilClient.is_unset(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreatePerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_performance_view_with_options_async(
        self,
        tmp_req: adb_20211201_models.CreatePerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreatePerformanceViewResponse:
        """
        @param tmp_req: CreatePerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePerformanceViewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.CreatePerformanceViewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_detail):
            request.view_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_from_view_type):
            query['CreateFromViewType'] = request.create_from_view_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.fill_origin_view_keys):
            query['FillOriginViewKeys'] = request.fill_origin_view_keys
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
        if not UtilClient.is_unset(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreatePerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_performance_view(
        self,
        request: adb_20211201_models.CreatePerformanceViewRequest,
    ) -> adb_20211201_models.CreatePerformanceViewResponse:
        """
        @param request: CreatePerformanceViewRequest
        @return: CreatePerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_performance_view_with_options(request, runtime)

    async def create_performance_view_async(
        self,
        request: adb_20211201_models.CreatePerformanceViewRequest,
    ) -> adb_20211201_models.CreatePerformanceViewResponse:
        """
        @param request: CreatePerformanceViewRequest
        @return: CreatePerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_performance_view_with_options_async(request, runtime)

    def create_spark_template_with_options(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        """
        @summary Creates a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateSparkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSparkTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_spark_template_with_options_async(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        """
        @summary Creates a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateSparkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSparkTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_spark_template(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        """
        @summary Creates a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateSparkTemplateRequest
        @return: CreateSparkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_spark_template_with_options(request, runtime)

    async def create_spark_template_async(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        """
        @summary Creates a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: CreateSparkTemplateRequest
        @return: CreateSparkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_spark_template_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
    ) -> adb_20211201_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
    ) -> adb_20211201_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        You can call this operation to delete only subscription clusters.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        You can call this operation to delete only subscription clusters.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        You can call this operation to delete only subscription clusters.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        """
        @summary Deletes an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        You can call this operation to delete only subscription clusters.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbresource_group_with_options(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_group(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBResourceGroupRequest
        @return: DeleteDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    async def delete_dbresource_group_async(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        """
        @summary Deletes a resource group from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteDBResourceGroupRequest
        @return: DeleteDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbresource_group_with_options_async(request, runtime)

    def delete_elastic_plan_with_options(
        self,
        request: adb_20211201_models.DeleteElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scaling plan from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_plan_with_options_async(
        self,
        request: adb_20211201_models.DeleteElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scaling plan from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_plan(
        self,
        request: adb_20211201_models.DeleteElasticPlanRequest,
    ) -> adb_20211201_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scaling plan from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteElasticPlanRequest
        @return: DeleteElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_plan_with_options(request, runtime)

    async def delete_elastic_plan_async(
        self,
        request: adb_20211201_models.DeleteElasticPlanRequest,
    ) -> adb_20211201_models.DeleteElasticPlanResponse:
        """
        @summary Deletes a scaling plan from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DeleteElasticPlanRequest
        @return: DeleteElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_elastic_plan_with_options_async(request, runtime)

    def delete_performance_view_with_options(
        self,
        request: adb_20211201_models.DeletePerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeletePerformanceViewResponse:
        """
        @param request: DeletePerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePerformanceViewResponse
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
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeletePerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_performance_view_with_options_async(
        self,
        request: adb_20211201_models.DeletePerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeletePerformanceViewResponse:
        """
        @param request: DeletePerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePerformanceViewResponse
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
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeletePerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_performance_view(
        self,
        request: adb_20211201_models.DeletePerformanceViewRequest,
    ) -> adb_20211201_models.DeletePerformanceViewResponse:
        """
        @param request: DeletePerformanceViewRequest
        @return: DeletePerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_performance_view_with_options(request, runtime)

    async def delete_performance_view_async(
        self,
        request: adb_20211201_models.DeletePerformanceViewRequest,
    ) -> adb_20211201_models.DeletePerformanceViewResponse:
        """
        @param request: DeletePerformanceViewRequest
        @return: DeletePerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_performance_view_with_options_async(request, runtime)

    def delete_process_instance_with_options(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        """
        @summary Deletes a worflow instance from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteProcessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProcessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.project_code):
            query['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProcessInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteProcessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_process_instance_with_options_async(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        """
        @summary Deletes a worflow instance from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteProcessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProcessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.project_code):
            query['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProcessInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteProcessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_process_instance(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        """
        @summary Deletes a worflow instance from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteProcessInstanceRequest
        @return: DeleteProcessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_process_instance_with_options(request, runtime)

    async def delete_process_instance_async(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        """
        @summary Deletes a worflow instance from an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteProcessInstanceRequest
        @return: DeleteProcessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_process_instance_with_options_async(request, runtime)

    def delete_spark_template_with_options(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        """
        @summary Deletes Spark template files.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: DeleteSparkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSparkTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_with_options_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        """
        @summary Deletes Spark template files.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: DeleteSparkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSparkTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        """
        @summary Deletes Spark template files.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: DeleteSparkTemplateRequest
        @return: DeleteSparkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_spark_template_with_options(request, runtime)

    async def delete_spark_template_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        """
        @summary Deletes Spark template files.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: DeleteSparkTemplateRequest
        @return: DeleteSparkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_spark_template_with_options_async(request, runtime)

    def delete_spark_template_file_with_options(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        """
        @summary Deletes Spark template files.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_file_with_options_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        """
        @summary Deletes Spark template files.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template_file(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        """
        @summary Deletes Spark template files.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteSparkTemplateFileRequest
        @return: DeleteSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_spark_template_file_with_options(request, runtime)

    async def delete_spark_template_file_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        """
        @summary Deletes Spark template files.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DeleteSparkTemplateFileRequest
        @return: DeleteSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_spark_template_file_with_options_async(request, runtime)

    def describe_account_all_privileges_with_options(
        self,
        request: adb_20211201_models.DescribeAccountAllPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountAllPrivilegesResponse:
        """
        @summary Queries the permissions of a database account on all permission levels.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountAllPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAllPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAllPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountAllPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_all_privileges_with_options_async(
        self,
        request: adb_20211201_models.DescribeAccountAllPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountAllPrivilegesResponse:
        """
        @summary Queries the permissions of a database account on all permission levels.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountAllPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAllPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAllPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountAllPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_all_privileges(
        self,
        request: adb_20211201_models.DescribeAccountAllPrivilegesRequest,
    ) -> adb_20211201_models.DescribeAccountAllPrivilegesResponse:
        """
        @summary Queries the permissions of a database account on all permission levels.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountAllPrivilegesRequest
        @return: DescribeAccountAllPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_all_privileges_with_options(request, runtime)

    async def describe_account_all_privileges_async(
        self,
        request: adb_20211201_models.DescribeAccountAllPrivilegesRequest,
    ) -> adb_20211201_models.DescribeAccountAllPrivilegesResponse:
        """
        @summary Queries the permissions of a database account on all permission levels.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountAllPrivilegesRequest
        @return: DescribeAccountAllPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_all_privileges_with_options_async(request, runtime)

    def describe_account_privilege_objects_with_options(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegeObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountPrivilegeObjectsResponse:
        """
        @summary Queries the databases, tables, and columns on which a database account has permissions.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountPrivilegeObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountPrivilegeObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountPrivilegeObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountPrivilegeObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_privilege_objects_with_options_async(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegeObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountPrivilegeObjectsResponse:
        """
        @summary Queries the databases, tables, and columns on which a database account has permissions.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountPrivilegeObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountPrivilegeObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountPrivilegeObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountPrivilegeObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_privilege_objects(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegeObjectsRequest,
    ) -> adb_20211201_models.DescribeAccountPrivilegeObjectsResponse:
        """
        @summary Queries the databases, tables, and columns on which a database account has permissions.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountPrivilegeObjectsRequest
        @return: DescribeAccountPrivilegeObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_privilege_objects_with_options(request, runtime)

    async def describe_account_privilege_objects_async(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegeObjectsRequest,
    ) -> adb_20211201_models.DescribeAccountPrivilegeObjectsResponse:
        """
        @summary Queries the databases, tables, and columns on which a database account has permissions.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountPrivilegeObjectsRequest
        @return: DescribeAccountPrivilegeObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_privilege_objects_with_options_async(request, runtime)

    def describe_account_privileges_with_options(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountPrivilegesResponse:
        """
        @summary 获取某一ADB账户的权限
        
        @param request: DescribeAccountPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_privileges_with_options_async(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountPrivilegesResponse:
        """
        @summary 获取某一ADB账户的权限
        
        @param request: DescribeAccountPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_privileges(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegesRequest,
    ) -> adb_20211201_models.DescribeAccountPrivilegesResponse:
        """
        @summary 获取某一ADB账户的权限
        
        @param request: DescribeAccountPrivilegesRequest
        @return: DescribeAccountPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_privileges_with_options(request, runtime)

    async def describe_account_privileges_async(
        self,
        request: adb_20211201_models.DescribeAccountPrivilegesRequest,
    ) -> adb_20211201_models.DescribeAccountPrivilegesResponse:
        """
        @summary 获取某一ADB账户的权限
        
        @param request: DescribeAccountPrivilegesRequest
        @return: DescribeAccountPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_privileges_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_adb_my_sql_columns_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        """
        @summary Queries the information about table columns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_columns_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        """
        @summary Queries the information about table columns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_columns(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        """
        @summary Queries the information about table columns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlColumnsRequest
        @return: DescribeAdbMySqlColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_columns_with_options(request, runtime)

    async def describe_adb_my_sql_columns_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        """
        @summary Queries the information about table columns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlColumnsRequest
        @return: DescribeAdbMySqlColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_columns_with_options_async(request, runtime)

    def describe_adb_my_sql_schemas_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        """
        @summary Queries a list of databases for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlSchemasResponse
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
            action='DescribeAdbMySqlSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_schemas_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        """
        @summary Queries a list of databases for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlSchemasResponse
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
            action='DescribeAdbMySqlSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_schemas(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        """
        @summary Queries a list of databases for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlSchemasRequest
        @return: DescribeAdbMySqlSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_schemas_with_options(request, runtime)

    async def describe_adb_my_sql_schemas_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        """
        @summary Queries a list of databases for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlSchemasRequest
        @return: DescribeAdbMySqlSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_schemas_with_options_async(request, runtime)

    def describe_adb_my_sql_tables_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        """
        @summary Queries a list of tables for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_tables_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        """
        @summary Queries a list of tables for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbMySqlTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_tables(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        """
        @summary Queries a list of tables for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlTablesRequest
        @return: DescribeAdbMySqlTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_tables_with_options(request, runtime)

    async def describe_adb_my_sql_tables_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        """
        @summary Queries a list of tables for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAdbMySqlTablesRequest
        @return: DescribeAdbMySqlTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_tables_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: adb_20211201_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: adb_20211201_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: adb_20211201_models.DescribeAllDataSourceRequest,
    ) -> adb_20211201_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: adb_20211201_models.DescribeAllDataSourceRequest,
    ) -> adb_20211201_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_aps_action_logs_with_options(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        """
        @summary Queries the logs of a real-time data ingestion job for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsActionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApsActionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
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
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApsActionLogs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsActionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_action_logs_with_options_async(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        """
        @summary Queries the logs of a real-time data ingestion job for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsActionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApsActionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
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
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApsActionLogs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsActionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_action_logs(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        """
        @summary Queries the logs of a real-time data ingestion job for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsActionLogsRequest
        @return: DescribeApsActionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_aps_action_logs_with_options(request, runtime)

    async def describe_aps_action_logs_async(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        """
        @summary Queries the logs of a real-time data ingestion job for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsActionLogsRequest
        @return: DescribeApsActionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_aps_action_logs_with_options_async(request, runtime)

    def describe_aps_resource_groups_with_options(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        """
        @summary Queries the information about resource groups of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApsResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApsResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_resource_groups_with_options_async(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        """
        @summary Queries the information about resource groups of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApsResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApsResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_resource_groups(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        """
        @summary Queries the information about resource groups of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsResourceGroupsRequest
        @return: DescribeApsResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_aps_resource_groups_with_options(request, runtime)

    async def describe_aps_resource_groups_async(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        """
        @summary Queries the information about resource groups of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeApsResourceGroupsRequest
        @return: DescribeApsResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_aps_resource_groups_with_options_async(request, runtime)

    def describe_audit_log_records_with_options(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: **INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: **INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_records(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: **INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAuditLogRecordsRequest
        @return: DescribeAuditLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_records_with_options(request, runtime)

    async def describe_audit_log_records_async(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        """
        @summary Queries the SQL audit logs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried. The following operations are not recorded in SQL audit logs: **INSERT INTO VALUES**, **REPLACE INTO VALUES**, and **UPSERT INTO VALUES**.
        For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeAuditLogRecordsRequest
        @return: DescribeAuditLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_records_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_access_white_list_with_options(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_access_white_list_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_access_white_list(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterAccessWhiteListRequest
        @return: DescribeClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_access_white_list_with_options(request, runtime)

    async def describe_cluster_access_white_list_async(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterAccessWhiteListRequest
        @return: DescribeClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_access_white_list_with_options_async(request, runtime)

    def describe_cluster_net_info_with_options(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_net_info_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_net_info(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterNetInfoRequest
        @return: DescribeClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_net_info_with_options(request, runtime)

    async def describe_cluster_net_info_async(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary Queries the network information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeClusterNetInfoRequest
        @return: DescribeClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_net_info_with_options_async(request, runtime)

    def describe_cluster_resource_detail_with_options(
        self,
        request: adb_20211201_models.DescribeClusterResourceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterResourceDetailResponse:
        """
        @summary 获取集群资源统计
        
        @param request: DescribeClusterResourceDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourceDetail',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterResourceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resource_detail_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterResourceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterResourceDetailResponse:
        """
        @summary 获取集群资源统计
        
        @param request: DescribeClusterResourceDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourceDetail',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterResourceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resource_detail(
        self,
        request: adb_20211201_models.DescribeClusterResourceDetailRequest,
    ) -> adb_20211201_models.DescribeClusterResourceDetailResponse:
        """
        @summary 获取集群资源统计
        
        @param request: DescribeClusterResourceDetailRequest
        @return: DescribeClusterResourceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_resource_detail_with_options(request, runtime)

    async def describe_cluster_resource_detail_async(
        self,
        request: adb_20211201_models.DescribeClusterResourceDetailRequest,
    ) -> adb_20211201_models.DescribeClusterResourceDetailResponse:
        """
        @summary 获取集群资源统计
        
        @param request: DescribeClusterResourceDetailRequest
        @return: DescribeClusterResourceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_resource_detail_with_options_async(request, runtime)

    def describe_cluster_resource_usage_with_options(
        self,
        request: adb_20211201_models.DescribeClusterResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterResourceUsageResponse:
        """
        @summary 获取实例资源统计
        
        @param request: DescribeClusterResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resource_usage_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterResourceUsageResponse:
        """
        @summary 获取实例资源统计
        
        @param request: DescribeClusterResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resource_usage(
        self,
        request: adb_20211201_models.DescribeClusterResourceUsageRequest,
    ) -> adb_20211201_models.DescribeClusterResourceUsageResponse:
        """
        @summary 获取实例资源统计
        
        @param request: DescribeClusterResourceUsageRequest
        @return: DescribeClusterResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_resource_usage_with_options(request, runtime)

    async def describe_cluster_resource_usage_async(
        self,
        request: adb_20211201_models.DescribeClusterResourceUsageRequest,
    ) -> adb_20211201_models.DescribeClusterResourceUsageResponse:
        """
        @summary 获取实例资源统计
        
        @param request: DescribeClusterResourceUsageRequest
        @return: DescribeClusterResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_resource_usage_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: adb_20211201_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: adb_20211201_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: adb_20211201_models.DescribeColumnsRequest,
    ) -> adb_20211201_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: adb_20211201_models.DescribeColumnsRequest,
    ) -> adb_20211201_models.DescribeColumnsResponse:
        """
        @summary Queries a list of columns in a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_compute_resource_usage_with_options(
        self,
        request: adb_20211201_models.DescribeComputeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeComputeResourceUsageResponse:
        """
        @summary 获取实例计算资源使用统计
        
        @param request: DescribeComputeResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComputeResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeComputeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compute_resource_usage_with_options_async(
        self,
        request: adb_20211201_models.DescribeComputeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeComputeResourceUsageResponse:
        """
        @summary 获取实例计算资源使用统计
        
        @param request: DescribeComputeResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComputeResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeComputeResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compute_resource_usage(
        self,
        request: adb_20211201_models.DescribeComputeResourceUsageRequest,
    ) -> adb_20211201_models.DescribeComputeResourceUsageResponse:
        """
        @summary 获取实例计算资源使用统计
        
        @param request: DescribeComputeResourceUsageRequest
        @return: DescribeComputeResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_compute_resource_usage_with_options(request, runtime)

    async def describe_compute_resource_usage_async(
        self,
        request: adb_20211201_models.DescribeComputeResourceUsageRequest,
    ) -> adb_20211201_models.DescribeComputeResourceUsageResponse:
        """
        @summary 获取实例计算资源使用统计
        
        @param request: DescribeComputeResourceUsageRequest
        @return: DescribeComputeResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_compute_resource_usage_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_health_status_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary Queries the health status of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_health_status_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary Queries the health status of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_health_status(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary Queries the health status of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDBClusterHealthStatusRequest
        @return: DescribeDBClusterHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_health_status_with_options(request, runtime)

    async def describe_dbcluster_health_status_async(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        """
        @summary Queries the health status of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDBClusterHealthStatusRequest
        @return: DescribeDBClusterHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_health_status_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbcluster_space_summary_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSpaceSummaryResponse
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
            action='DescribeDBClusterSpaceSummary',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterSpaceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_space_summary_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSpaceSummaryResponse
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
            action='DescribeDBClusterSpaceSummary',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterSpaceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_space_summary(
        self,
        request: adb_20211201_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> adb_20211201_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_space_summary_with_options(request, runtime)

    async def describe_dbcluster_space_summary_async(
        self,
        request: adb_20211201_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> adb_20211201_models.DescribeDBClusterSpaceSummaryResponse:
        """
        @summary Queries the storage overview information of an AnalyticDB for MySQL cluster, such as the total data size, hot data size, cold data size, and data growth.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterSpaceSummaryRequest
        @return: DescribeDBClusterSpaceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_space_summary_with_options_async(request, runtime)

    def describe_dbcluster_status_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries a list of states for AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterStatus',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_status_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries a list of states for AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterStatus',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_status(
        self,
        request: adb_20211201_models.DescribeDBClusterStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries a list of states for AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterStatusRequest
        @return: DescribeDBClusterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_status_with_options(request, runtime)

    async def describe_dbcluster_status_async(
        self,
        request: adb_20211201_models.DescribeDBClusterStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterStatusResponse:
        """
        @summary Queries a list of states for AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClusterStatusRequest
        @return: DescribeDBClusterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_status_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters in a region.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters in a region.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters in a region.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters in a region.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about resource groups for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about resource groups for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_group(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about resource groups for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary Queries the information about resource groups for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of resource groups, databases, usernames, and source IP addresses about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of resource groups, databases, usernames, and source IP addresses about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of resource groups, databases, usernames, and source IP addresses about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        """
        @summary Queries the deduplicated statistics of resource groups, databases, usernames, and source IP addresses about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        """
        @summary Queries the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        """
        @summary Queries the execution information about an SQL statement, including the execution plan, execution information, resource usage, and self-diagnostics results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries the last five SQL query download tasks of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries the last five SQL query download tasks of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries the last five SQL query download tasks of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        """
        @summary Queries the last five SQL query download tasks of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_elastic_plan_attribute_with_options(
        self,
        request: adb_20211201_models.DescribeElasticPlanAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanAttributeResponse:
        """
        @summary Queries the information about a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see DescribeElasticPlanAttribute.
        
        @param request: DescribeElasticPlanAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_attribute_with_options_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanAttributeResponse:
        """
        @summary Queries the information about a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see DescribeElasticPlanAttribute.
        
        @param request: DescribeElasticPlanAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_attribute(
        self,
        request: adb_20211201_models.DescribeElasticPlanAttributeRequest,
    ) -> adb_20211201_models.DescribeElasticPlanAttributeResponse:
        """
        @summary Queries the information about a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see DescribeElasticPlanAttribute.
        
        @param request: DescribeElasticPlanAttributeRequest
        @return: DescribeElasticPlanAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plan_attribute_with_options(request, runtime)

    async def describe_elastic_plan_attribute_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanAttributeRequest,
    ) -> adb_20211201_models.DescribeElasticPlanAttributeResponse:
        """
        @summary Queries the information about a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see DescribeElasticPlanAttribute.
        
        @param request: DescribeElasticPlanAttributeRequest
        @return: DescribeElasticPlanAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_plan_attribute_with_options_async(request, runtime)

    def describe_elastic_plan_jobs_with_options(
        self,
        request: adb_20211201_models.DescribeElasticPlanJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanJobsResponse:
        """
        @summary Queries a list of scaling plan jobs for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeElasticPlanJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanJobs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_jobs_with_options_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanJobsResponse:
        """
        @summary Queries a list of scaling plan jobs for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeElasticPlanJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanJobs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_jobs(
        self,
        request: adb_20211201_models.DescribeElasticPlanJobsRequest,
    ) -> adb_20211201_models.DescribeElasticPlanJobsResponse:
        """
        @summary Queries a list of scaling plan jobs for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeElasticPlanJobsRequest
        @return: DescribeElasticPlanJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plan_jobs_with_options(request, runtime)

    async def describe_elastic_plan_jobs_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanJobsRequest,
    ) -> adb_20211201_models.DescribeElasticPlanJobsResponse:
        """
        @summary Queries a list of scaling plan jobs for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: DescribeElasticPlanJobsRequest
        @return: DescribeElasticPlanJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_plan_jobs_with_options_async(request, runtime)

    def describe_elastic_plan_specifications_with_options(
        self,
        request: adb_20211201_models.DescribeElasticPlanSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanSpecificationsResponse:
        """
        @summary Queries the resource specifications that are supported by different types of scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeElasticPlanSpecificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanSpecificationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanSpecifications',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_specifications_with_options_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlanSpecificationsResponse:
        """
        @summary Queries the resource specifications that are supported by different types of scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeElasticPlanSpecificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlanSpecificationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlanSpecifications',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlanSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_specifications(
        self,
        request: adb_20211201_models.DescribeElasticPlanSpecificationsRequest,
    ) -> adb_20211201_models.DescribeElasticPlanSpecificationsResponse:
        """
        @summary Queries the resource specifications that are supported by different types of scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeElasticPlanSpecificationsRequest
        @return: DescribeElasticPlanSpecificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plan_specifications_with_options(request, runtime)

    async def describe_elastic_plan_specifications_async(
        self,
        request: adb_20211201_models.DescribeElasticPlanSpecificationsRequest,
    ) -> adb_20211201_models.DescribeElasticPlanSpecificationsResponse:
        """
        @summary Queries the resource specifications that are supported by different types of scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeElasticPlanSpecificationsRequest
        @return: DescribeElasticPlanSpecificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_plan_specifications_with_options_async(request, runtime)

    def describe_elastic_plans_with_options(
        self,
        request: adb_20211201_models.DescribeElasticPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlansResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeElasticPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlans',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plans_with_options_async(
        self,
        request: adb_20211201_models.DescribeElasticPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeElasticPlansResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeElasticPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticPlans',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeElasticPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plans(
        self,
        request: adb_20211201_models.DescribeElasticPlansRequest,
    ) -> adb_20211201_models.DescribeElasticPlansResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeElasticPlansRequest
        @return: DescribeElasticPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_plans_with_options(request, runtime)

    async def describe_elastic_plans_async(
        self,
        request: adb_20211201_models.DescribeElasticPlansRequest,
    ) -> adb_20211201_models.DescribeElasticPlansResponse:
        """
        @summary Queries scaling plans of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeElasticPlansRequest
        @return: DescribeElasticPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_plans_with_options_async(request, runtime)

    def describe_enabled_privileges_with_options(
        self,
        request: adb_20211201_models.DescribeEnabledPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeEnabledPrivilegesResponse:
        """
        @summary Queries the permission level and permissions supported for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeEnabledPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnabledPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnabledPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeEnabledPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enabled_privileges_with_options_async(
        self,
        request: adb_20211201_models.DescribeEnabledPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeEnabledPrivilegesResponse:
        """
        @summary Queries the permission level and permissions supported for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeEnabledPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnabledPrivilegesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnabledPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeEnabledPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enabled_privileges(
        self,
        request: adb_20211201_models.DescribeEnabledPrivilegesRequest,
    ) -> adb_20211201_models.DescribeEnabledPrivilegesResponse:
        """
        @summary Queries the permission level and permissions supported for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeEnabledPrivilegesRequest
        @return: DescribeEnabledPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_enabled_privileges_with_options(request, runtime)

    async def describe_enabled_privileges_async(
        self,
        request: adb_20211201_models.DescribeEnabledPrivilegesRequest,
    ) -> adb_20211201_models.DescribeEnabledPrivilegesResponse:
        """
        @summary Queries the permission level and permissions supported for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeEnabledPrivilegesRequest
        @return: DescribeEnabledPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_enabled_privileges_with_options_async(request, runtime)

    def describe_excessive_primary_keys_with_options(
        self,
        request: adb_20211201_models.DescribeExcessivePrimaryKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the information about tables that have excessive primary key fields in an AnalyticDB for MySQL Data Lakehouse Edition (V5.0) cluster.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeExcessivePrimaryKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excessive_primary_keys_with_options_async(
        self,
        request: adb_20211201_models.DescribeExcessivePrimaryKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the information about tables that have excessive primary key fields in an AnalyticDB for MySQL Data Lakehouse Edition (V5.0) cluster.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeExcessivePrimaryKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excessive_primary_keys(
        self,
        request: adb_20211201_models.DescribeExcessivePrimaryKeysRequest,
    ) -> adb_20211201_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the information about tables that have excessive primary key fields in an AnalyticDB for MySQL Data Lakehouse Edition (V5.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @return: DescribeExcessivePrimaryKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_excessive_primary_keys_with_options(request, runtime)

    async def describe_excessive_primary_keys_async(
        self,
        request: adb_20211201_models.DescribeExcessivePrimaryKeysRequest,
    ) -> adb_20211201_models.DescribeExcessivePrimaryKeysResponse:
        """
        @summary Queries the information about tables that have excessive primary key fields in an AnalyticDB for MySQL Data Lakehouse Edition (V5.0) cluster.
        
        @param request: DescribeExcessivePrimaryKeysRequest
        @return: DescribeExcessivePrimaryKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_excessive_primary_keys_with_options_async(request, runtime)

    def describe_job_resource_usage_with_options(
        self,
        request: adb_20211201_models.DescribeJobResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeJobResourceUsageResponse:
        """
        @summary 获取作业资源使用统计
        
        @param request: DescribeJobResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_resource_usage_with_options_async(
        self,
        request: adb_20211201_models.DescribeJobResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeJobResourceUsageResponse:
        """
        @summary 获取作业资源使用统计
        
        @param request: DescribeJobResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeJobResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_resource_usage(
        self,
        request: adb_20211201_models.DescribeJobResourceUsageRequest,
    ) -> adb_20211201_models.DescribeJobResourceUsageResponse:
        """
        @summary 获取作业资源使用统计
        
        @param request: DescribeJobResourceUsageRequest
        @return: DescribeJobResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_resource_usage_with_options(request, runtime)

    async def describe_job_resource_usage_async(
        self,
        request: adb_20211201_models.DescribeJobResourceUsageRequest,
    ) -> adb_20211201_models.DescribeJobResourceUsageResponse:
        """
        @summary 获取作业资源使用统计
        
        @param request: DescribeJobResourceUsageRequest
        @return: DescribeJobResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_resource_usage_with_options_async(request, runtime)

    def describe_pattern_performance_with_options(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the information about performance metrics of an SQL pattern such as the query duration and average memory usage for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePatternPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_performance_with_options_async(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the information about performance metrics of an SQL pattern such as the query duration and average memory usage for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePatternPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_performance(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the information about performance metrics of an SQL pattern such as the query duration and average memory usage for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribePatternPerformanceRequest
        @return: DescribePatternPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pattern_performance_with_options(request, runtime)

    async def describe_pattern_performance_async(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        """
        @summary Queries the information about performance metrics of an SQL pattern such as the query duration and average memory usage for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribePatternPerformanceRequest
        @return: DescribePatternPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pattern_performance_with_options_async(request, runtime)

    def describe_performance_view_attribute_with_options(
        self,
        request: adb_20211201_models.DescribePerformanceViewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePerformanceViewAttributeResponse:
        """
        @param request: DescribePerformanceViewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerformanceViewAttributeResponse
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
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePerformanceViewAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePerformanceViewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_performance_view_attribute_with_options_async(
        self,
        request: adb_20211201_models.DescribePerformanceViewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePerformanceViewAttributeResponse:
        """
        @param request: DescribePerformanceViewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerformanceViewAttributeResponse
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
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePerformanceViewAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePerformanceViewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_performance_view_attribute(
        self,
        request: adb_20211201_models.DescribePerformanceViewAttributeRequest,
    ) -> adb_20211201_models.DescribePerformanceViewAttributeResponse:
        """
        @param request: DescribePerformanceViewAttributeRequest
        @return: DescribePerformanceViewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_performance_view_attribute_with_options(request, runtime)

    async def describe_performance_view_attribute_async(
        self,
        request: adb_20211201_models.DescribePerformanceViewAttributeRequest,
    ) -> adb_20211201_models.DescribePerformanceViewAttributeResponse:
        """
        @param request: DescribePerformanceViewAttributeRequest
        @return: DescribePerformanceViewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_performance_view_attribute_with_options_async(request, runtime)

    def describe_performance_views_with_options(
        self,
        request: adb_20211201_models.DescribePerformanceViewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePerformanceViewsResponse:
        """
        @param request: DescribePerformanceViewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerformanceViewsResponse
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
            action='DescribePerformanceViews',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePerformanceViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_performance_views_with_options_async(
        self,
        request: adb_20211201_models.DescribePerformanceViewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePerformanceViewsResponse:
        """
        @param request: DescribePerformanceViewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerformanceViewsResponse
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
            action='DescribePerformanceViews',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePerformanceViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_performance_views(
        self,
        request: adb_20211201_models.DescribePerformanceViewsRequest,
    ) -> adb_20211201_models.DescribePerformanceViewsResponse:
        """
        @param request: DescribePerformanceViewsRequest
        @return: DescribePerformanceViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_performance_views_with_options(request, runtime)

    async def describe_performance_views_async(
        self,
        request: adb_20211201_models.DescribePerformanceViewsRequest,
    ) -> adb_20211201_models.DescribePerformanceViewsResponse:
        """
        @param request: DescribePerformanceViewsRequest
        @return: DescribePerformanceViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_performance_views_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions and zones in which AnalyticDB for MySQL Data Lakehouse Edition (V3.0) is available.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions and zones in which AnalyticDB for MySQL Data Lakehouse Edition (V3.0) is available.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions and zones in which AnalyticDB for MySQL Data Lakehouse Edition (V3.0) is available.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions and zones in which AnalyticDB for MySQL Data Lakehouse Edition (V3.0) is available.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_sqlpatterns_with_options(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlpatterns_with_options_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlpatterns(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSQLPatternsRequest
        @return: DescribeSQLPatternsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpatterns_with_options(request, runtime)

    async def describe_sqlpatterns_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        """
        @summary Queries a list of SQL patterns for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSQLPatternsRequest
        @return: DescribeSQLPatternsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlpatterns_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: adb_20211201_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
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
            action='DescribeSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: adb_20211201_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
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
            action='DescribeSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: adb_20211201_models.DescribeSchemasRequest,
    ) -> adb_20211201_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: adb_20211201_models.DescribeSchemasRequest,
    ) -> adb_20211201_models.DescribeSchemasResponse:
        """
        @summary Queries a list of databases in an AnalyticDB for MySQL cluster.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_spark_code_log_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        """
        @summary Queries the execution logs of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_log_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        """
        @summary Queries the execution logs of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_log(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        """
        @summary Queries the execution logs of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeLogRequest
        @return: DescribeSparkCodeLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_log_with_options(request, runtime)

    async def describe_spark_code_log_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        """
        @summary Queries the execution logs of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeLogRequest
        @return: DescribeSparkCodeLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_log_with_options_async(request, runtime)

    def describe_spark_code_output_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        """
        @summary Queries the execution result of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeOutputResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeOutput',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_output_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        """
        @summary Queries the execution result of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeOutputResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeOutput',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_output(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        """
        @summary Queries the execution result of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeOutputRequest
        @return: DescribeSparkCodeOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_output_with_options(request, runtime)

    async def describe_spark_code_output_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        """
        @summary Queries the execution result of Spark code.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeOutputRequest
        @return: DescribeSparkCodeOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_output_with_options_async(request, runtime)

    def describe_spark_code_web_ui_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeWebUiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeWebUiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeWebUi',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeWebUiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_web_ui_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeWebUiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSparkCodeWebUiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeWebUi',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeWebUiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_web_ui(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeWebUiRequest
        @return: DescribeSparkCodeWebUiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_web_ui_with_options(request, runtime)

    async def describe_spark_code_web_ui_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeSparkCodeWebUiRequest
        @return: DescribeSparkCodeWebUiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_web_ui_with_options_async(request, runtime)

    def describe_sql_pattern_with_options(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        """
        @summary Queries the information about SQL patterns of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSqlPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_pattern_with_options_async(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        """
        @summary Queries the information about SQL patterns of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSqlPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_pattern(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        """
        @summary Queries the information about SQL patterns of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeSqlPatternRequest
        @return: DescribeSqlPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_pattern_with_options(request, runtime)

    async def describe_sql_pattern_async(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        """
        @summary Queries the information about SQL patterns of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster within a time range.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeSqlPatternRequest
        @return: DescribeSqlPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_pattern_with_options_async(request, runtime)

    def describe_storage_resource_usage_with_options(
        self,
        request: adb_20211201_models.DescribeStorageResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeStorageResourceUsageResponse:
        """
        @summary Queries the storage resource usage of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeStorageResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStorageResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeStorageResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_resource_usage_with_options_async(
        self,
        request: adb_20211201_models.DescribeStorageResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeStorageResourceUsageResponse:
        """
        @summary Queries the storage resource usage of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeStorageResourceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStorageResourceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageResourceUsage',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeStorageResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_resource_usage(
        self,
        request: adb_20211201_models.DescribeStorageResourceUsageRequest,
    ) -> adb_20211201_models.DescribeStorageResourceUsageResponse:
        """
        @summary Queries the storage resource usage of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeStorageResourceUsageRequest
        @return: DescribeStorageResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_resource_usage_with_options(request, runtime)

    async def describe_storage_resource_usage_async(
        self,
        request: adb_20211201_models.DescribeStorageResourceUsageRequest,
    ) -> adb_20211201_models.DescribeStorageResourceUsageResponse:
        """
        @summary Queries the storage resource usage of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: DescribeStorageResourceUsageRequest
        @return: DescribeStorageResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_resource_usage_with_options_async(request, runtime)

    def describe_table_access_count_with_options(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        """
        @summary Queries the number of accesses to a table or all tables in an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster on a date.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTableAccessCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_access_count_with_options_async(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        """
        @summary Queries the number of accesses to a table or all tables in an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster on a date.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTableAccessCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_access_count(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        """
        @summary Queries the number of accesses to a table or all tables in an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster on a date.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTableAccessCountRequest
        @return: DescribeTableAccessCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_table_access_count_with_options(request, runtime)

    async def describe_table_access_count_async(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        """
        @summary Queries the number of accesses to a table or all tables in an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster on a date.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTableAccessCountRequest
        @return: DescribeTableAccessCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_access_count_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: adb_20211201_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: adb_20211201_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: adb_20211201_models.DescribeTablesRequest,
    ) -> adb_20211201_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: adb_20211201_models.DescribeTablesRequest,
    ) -> adb_20211201_models.DescribeTablesResponse:
        """
        @summary Queries a list of tables in a database.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_user_quota_with_options(
        self,
        request: adb_20211201_models.DescribeUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeUserQuotaResponse:
        """
        @summary 查询配额
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserQuota',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_quota_with_options_async(
        self,
        request: adb_20211201_models.DescribeUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeUserQuotaResponse:
        """
        @summary 查询配额
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserQuota',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_quota(
        self,
        request: adb_20211201_models.DescribeUserQuotaRequest,
    ) -> adb_20211201_models.DescribeUserQuotaResponse:
        """
        @summary 查询配额
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeUserQuotaRequest
        @return: DescribeUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_quota_with_options(request, runtime)

    async def describe_user_quota_async(
        self,
        request: adb_20211201_models.DescribeUserQuotaRequest,
    ) -> adb_20211201_models.DescribeUserQuotaResponse:
        """
        @summary 查询配额
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DescribeUserQuotaRequest
        @return: DescribeUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_quota_with_options_async(request, runtime)

    def detach_user_eniwith_options(
        self,
        request: adb_20211201_models.DetachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DetachUserENIResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DetachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachUserENI',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DetachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_user_eniwith_options_async(
        self,
        request: adb_20211201_models.DetachUserENIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DetachUserENIResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DetachUserENIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachUserENIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachUserENI',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DetachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_user_eni(
        self,
        request: adb_20211201_models.DetachUserENIRequest,
    ) -> adb_20211201_models.DetachUserENIResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DetachUserENIRequest
        @return: DetachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_user_eniwith_options(request, runtime)

    async def detach_user_eni_async(
        self,
        request: adb_20211201_models.DetachUserENIRequest,
    ) -> adb_20211201_models.DetachUserENIResponse:
        """
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DetachUserENIRequest
        @return: DetachUserENIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_user_eniwith_options_async(request, runtime)

    def disable_elastic_plan_with_options(
        self,
        request: adb_20211201_models.DisableElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DisableElasticPlanResponse:
        """
        @summary Disables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DisableElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DisableElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_elastic_plan_with_options_async(
        self,
        request: adb_20211201_models.DisableElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DisableElasticPlanResponse:
        """
        @summary Disables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DisableElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DisableElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_elastic_plan(
        self,
        request: adb_20211201_models.DisableElasticPlanRequest,
    ) -> adb_20211201_models.DisableElasticPlanResponse:
        """
        @summary Disables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DisableElasticPlanRequest
        @return: DisableElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_elastic_plan_with_options(request, runtime)

    async def disable_elastic_plan_async(
        self,
        request: adb_20211201_models.DisableElasticPlanRequest,
    ) -> adb_20211201_models.DisableElasticPlanResponse:
        """
        @summary Disables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: DisableElasticPlanRequest
        @return: DisableElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_elastic_plan_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        """
        @summary Downloads the diagnostic information about SQL statements that meet a query condition for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def enable_elastic_plan_with_options(
        self,
        request: adb_20211201_models.EnableElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.EnableElasticPlanResponse:
        """
        @summary Enables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: EnableElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.EnableElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_elastic_plan_with_options_async(
        self,
        request: adb_20211201_models.EnableElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.EnableElasticPlanResponse:
        """
        @summary Enables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: EnableElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.EnableElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_elastic_plan(
        self,
        request: adb_20211201_models.EnableElasticPlanRequest,
    ) -> adb_20211201_models.EnableElasticPlanResponse:
        """
        @summary Enables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: EnableElasticPlanRequest
        @return: EnableElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_elastic_plan_with_options(request, runtime)

    async def enable_elastic_plan_async(
        self,
        request: adb_20211201_models.EnableElasticPlanRequest,
    ) -> adb_20211201_models.EnableElasticPlanResponse:
        """
        @summary Enables a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: EnableElasticPlanRequest
        @return: EnableElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_elastic_plan_with_options_async(request, runtime)

    def exist_running_sqlengine_with_options(
        self,
        request: adb_20211201_models.ExistRunningSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ExistRunningSQLEngineResponse:
        """
        @summary Queries whether a running SQL engine exists.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ExistRunningSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExistRunningSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExistRunningSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ExistRunningSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def exist_running_sqlengine_with_options_async(
        self,
        request: adb_20211201_models.ExistRunningSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ExistRunningSQLEngineResponse:
        """
        @summary Queries whether a running SQL engine exists.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ExistRunningSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExistRunningSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExistRunningSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ExistRunningSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exist_running_sqlengine(
        self,
        request: adb_20211201_models.ExistRunningSQLEngineRequest,
    ) -> adb_20211201_models.ExistRunningSQLEngineResponse:
        """
        @summary Queries whether a running SQL engine exists.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ExistRunningSQLEngineRequest
        @return: ExistRunningSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exist_running_sqlengine_with_options(request, runtime)

    async def exist_running_sqlengine_async(
        self,
        request: adb_20211201_models.ExistRunningSQLEngineRequest,
    ) -> adb_20211201_models.ExistRunningSQLEngineResponse:
        """
        @summary Queries whether a running SQL engine exists.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ExistRunningSQLEngineRequest
        @return: ExistRunningSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exist_running_sqlengine_with_options_async(request, runtime)

    def get_database_objects_with_options(
        self,
        request: adb_20211201_models.GetDatabaseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetDatabaseObjectsResponse:
        """
        @summary Queries the information about databases.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetDatabaseObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_schema_name):
            query['FilterSchemaName'] = request.filter_schema_name
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
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
            action='GetDatabaseObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetDatabaseObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_objects_with_options_async(
        self,
        request: adb_20211201_models.GetDatabaseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetDatabaseObjectsResponse:
        """
        @summary Queries the information about databases.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetDatabaseObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_schema_name):
            query['FilterSchemaName'] = request.filter_schema_name
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
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
            action='GetDatabaseObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetDatabaseObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_objects(
        self,
        request: adb_20211201_models.GetDatabaseObjectsRequest,
    ) -> adb_20211201_models.GetDatabaseObjectsResponse:
        """
        @summary Queries the information about databases.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetDatabaseObjectsRequest
        @return: GetDatabaseObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_database_objects_with_options(request, runtime)

    async def get_database_objects_async(
        self,
        request: adb_20211201_models.GetDatabaseObjectsRequest,
    ) -> adb_20211201_models.GetDatabaseObjectsResponse:
        """
        @summary Queries the information about databases.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetDatabaseObjectsRequest
        @return: GetDatabaseObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_database_objects_with_options_async(request, runtime)

    def get_spark_app_attempt_log_with_options(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        """
        @summary Queries the information about the retry log of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppAttemptLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppAttemptLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppAttemptLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppAttemptLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_attempt_log_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        """
        @summary Queries the information about the retry log of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppAttemptLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppAttemptLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppAttemptLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppAttemptLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_attempt_log(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        """
        @summary Queries the information about the retry log of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppAttemptLogRequest
        @return: GetSparkAppAttemptLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_attempt_log_with_options(request, runtime)

    async def get_spark_app_attempt_log_async(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        """
        @summary Queries the information about the retry log of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppAttemptLogRequest
        @return: GetSparkAppAttemptLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_attempt_log_with_options_async(request, runtime)

    def get_spark_app_info_with_options(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        """
        @summary Queries the information about an Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_info_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        """
        @summary Queries the information about an Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_info(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        """
        @summary Queries the information about an Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkAppInfoRequest
        @return: GetSparkAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_info_with_options(request, runtime)

    async def get_spark_app_info_async(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        """
        @summary Queries the information about an Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkAppInfoRequest
        @return: GetSparkAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_info_with_options_async(request, runtime)

    def get_spark_app_log_with_options(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        """
        @summary Queries the logs of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_log_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        """
        @summary Queries the logs of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_log(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        """
        @summary Queries the logs of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppLogRequest
        @return: GetSparkAppLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_log_with_options(request, runtime)

    async def get_spark_app_log_async(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        """
        @summary Queries the logs of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppLogRequest
        @return: GetSparkAppLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_log_with_options_async(request, runtime)

    def get_spark_app_metrics_with_options(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary Queries the metrics of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_metrics_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary Queries the metrics of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_metrics(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary Queries the metrics of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppMetricsRequest
        @return: GetSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_metrics_with_options(request, runtime)

    async def get_spark_app_metrics_async(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary Queries the metrics of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppMetricsRequest
        @return: GetSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_metrics_with_options_async(request, runtime)

    def get_spark_app_state_with_options(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        """
        @summary Queries the status of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_state_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        """
        @summary Queries the status of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_state(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        """
        @summary Queries the status of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppStateRequest
        @return: GetSparkAppStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_state_with_options(request, runtime)

    async def get_spark_app_state_async(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        """
        @summary Queries the status of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppStateRequest
        @return: GetSparkAppStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_state_with_options_async(request, runtime)

    def get_spark_app_web_ui_address_with_options(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppWebUiAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppWebUiAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppWebUiAddress',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppWebUiAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_web_ui_address_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppWebUiAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppWebUiAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppWebUiAddress',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppWebUiAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_web_ui_address(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppWebUiAddressRequest
        @return: GetSparkAppWebUiAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_web_ui_address_with_options(request, runtime)

    async def get_spark_app_web_ui_address_async(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        """
        @summary Queries the URL of the web UI for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkAppWebUiAddressRequest
        @return: GetSparkAppWebUiAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_web_ui_address_with_options_async(request, runtime)

    def get_spark_config_log_path_with_options(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        """
        @summary Queries the Spark log configuration of an AnalyticDB for MySQL cluster, including the default Spark log path.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkConfigLogPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkConfigLogPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkConfigLogPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkConfigLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_config_log_path_with_options_async(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        """
        @summary Queries the Spark log configuration of an AnalyticDB for MySQL cluster, including the default Spark log path.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkConfigLogPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkConfigLogPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkConfigLogPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkConfigLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_config_log_path(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        """
        @summary Queries the Spark log configuration of an AnalyticDB for MySQL cluster, including the default Spark log path.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkConfigLogPathRequest
        @return: GetSparkConfigLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_config_log_path_with_options(request, runtime)

    async def get_spark_config_log_path_async(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        """
        @summary Queries the Spark log configuration of an AnalyticDB for MySQL cluster, including the default Spark log path.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkConfigLogPathRequest
        @return: GetSparkConfigLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_config_log_path_with_options_async(request, runtime)

    def get_spark_definitions_with_options(
        self,
        request: adb_20211201_models.GetSparkDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkDefinitionsResponse:
        """
        @summary Queries the common definitions of Spark applications.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkDefinitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkDefinitions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_definitions_with_options_async(
        self,
        request: adb_20211201_models.GetSparkDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkDefinitionsResponse:
        """
        @summary Queries the common definitions of Spark applications.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkDefinitionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkDefinitions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_definitions(
        self,
        request: adb_20211201_models.GetSparkDefinitionsRequest,
    ) -> adb_20211201_models.GetSparkDefinitionsResponse:
        """
        @summary Queries the common definitions of Spark applications.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkDefinitionsRequest
        @return: GetSparkDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_definitions_with_options(request, runtime)

    async def get_spark_definitions_async(
        self,
        request: adb_20211201_models.GetSparkDefinitionsRequest,
    ) -> adb_20211201_models.GetSparkDefinitionsResponse:
        """
        @summary Queries the common definitions of Spark applications.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: GetSparkDefinitionsRequest
        @return: GetSparkDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_definitions_with_options_async(request, runtime)

    def get_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        """
        @summary Queries the results of a Spark log analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        """
        @summary Queries the results of a Spark log analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_log_analyze_task(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        """
        @summary Queries the results of a Spark log analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkLogAnalyzeTaskRequest
        @return: GetSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_log_analyze_task_with_options(request, runtime)

    async def get_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        """
        @summary Queries the results of a Spark log analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkLogAnalyzeTaskRequest
        @return: GetSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_log_analyze_task_with_options_async(request, runtime)

    def get_spark_sqlengine_state_with_options(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        """
        @summary Queries the state information about the Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkSQLEngineStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSQLEngineStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSQLEngineState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkSQLEngineStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_sqlengine_state_with_options_async(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        """
        @summary Queries the state information about the Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkSQLEngineStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSQLEngineStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSQLEngineState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkSQLEngineStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_sqlengine_state(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        """
        @summary Queries the state information about the Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkSQLEngineStateRequest
        @return: GetSparkSQLEngineStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_sqlengine_state_with_options(request, runtime)

    async def get_spark_sqlengine_state_async(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        """
        @summary Queries the state information about the Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkSQLEngineStateRequest
        @return: GetSparkSQLEngineStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_sqlengine_state_with_options_async(request, runtime)

    def get_spark_template_file_content_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        """
        @summary Queries the content of a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFileContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFileContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFileContent',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFileContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_file_content_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        """
        @summary Queries the content of a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFileContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFileContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFileContent',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFileContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_file_content(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        """
        @summary Queries the content of a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFileContentRequest
        @return: GetSparkTemplateFileContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_file_content_with_options(request, runtime)

    async def get_spark_template_file_content_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        """
        @summary Queries the content of a Spark application template.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFileContentRequest
        @return: GetSparkTemplateFileContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_file_content_with_options_async(request, runtime)

    def get_spark_template_folder_tree_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    You can call this operation to query the directory structure but not application data in the directory. To query the directory structure that contains application data, call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/612467.html) operation.
        General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFolderTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFolderTreeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFolderTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFolderTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_folder_tree_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    You can call this operation to query the directory structure but not application data in the directory. To query the directory structure that contains application data, call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/612467.html) operation.
        General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFolderTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFolderTreeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFolderTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFolderTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_folder_tree(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    You can call this operation to query the directory structure but not application data in the directory. To query the directory structure that contains application data, call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/612467.html) operation.
        General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFolderTreeRequest
        @return: GetSparkTemplateFolderTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_folder_tree_with_options(request, runtime)

    async def get_spark_template_folder_tree_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    You can call this operation to query the directory structure but not application data in the directory. To query the directory structure that contains application data, call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/612467.html) operation.
        General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFolderTreeRequest
        @return: GetSparkTemplateFolderTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_folder_tree_with_options_async(request, runtime)

    def get_spark_template_full_tree_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFullTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFullTreeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFullTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFullTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_full_tree_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFullTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkTemplateFullTreeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFullTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFullTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_full_tree(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFullTreeRequest
        @return: GetSparkTemplateFullTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_full_tree_with_options(request, runtime)

    async def get_spark_template_full_tree_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        """
        @summary Queries the directory structure of Spark applications.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetSparkTemplateFullTreeRequest
        @return: GetSparkTemplateFullTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_full_tree_with_options_async(request, runtime)

    def get_table_with_options(
        self,
        request: adb_20211201_models.GetTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableResponse:
        """
        @summary 获取表
        
        @param request: GetTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: adb_20211201_models.GetTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableResponse:
        """
        @summary 获取表
        
        @param request: GetTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: adb_20211201_models.GetTableRequest,
    ) -> adb_20211201_models.GetTableResponse:
        """
        @summary 获取表
        
        @param request: GetTableRequest
        @return: GetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_with_options(request, runtime)

    async def get_table_async(
        self,
        request: adb_20211201_models.GetTableRequest,
    ) -> adb_20211201_models.GetTableResponse:
        """
        @summary 获取表
        
        @param request: GetTableRequest
        @return: GetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_with_options_async(request, runtime)

    def get_table_columns_with_options(
        self,
        request: adb_20211201_models.GetTableColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableColumnsResponse:
        """
        @summary Queries the information about columns.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_columns_with_options_async(
        self,
        request: adb_20211201_models.GetTableColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableColumnsResponse:
        """
        @summary Queries the information about columns.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_columns(
        self,
        request: adb_20211201_models.GetTableColumnsRequest,
    ) -> adb_20211201_models.GetTableColumnsResponse:
        """
        @summary Queries the information about columns.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableColumnsRequest
        @return: GetTableColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_columns_with_options(request, runtime)

    async def get_table_columns_async(
        self,
        request: adb_20211201_models.GetTableColumnsRequest,
    ) -> adb_20211201_models.GetTableColumnsResponse:
        """
        @summary Queries the information about columns.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableColumnsRequest
        @return: GetTableColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_columns_with_options_async(request, runtime)

    def get_table_ddlwith_options(
        self,
        request: adb_20211201_models.GetTableDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableDDLResponse:
        """
        @summary Queries the statement that is used to create a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableDDLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableDDLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableDDLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_ddlwith_options_async(
        self,
        request: adb_20211201_models.GetTableDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableDDLResponse:
        """
        @summary Queries the statement that is used to create a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableDDLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableDDLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableDDLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_ddl(
        self,
        request: adb_20211201_models.GetTableDDLRequest,
    ) -> adb_20211201_models.GetTableDDLResponse:
        """
        @summary Queries the statement that is used to create a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableDDLRequest
        @return: GetTableDDLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_ddlwith_options(request, runtime)

    async def get_table_ddl_async(
        self,
        request: adb_20211201_models.GetTableDDLRequest,
    ) -> adb_20211201_models.GetTableDDLResponse:
        """
        @summary Queries the statement that is used to create a table.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetTableDDLRequest
        @return: GetTableDDLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_ddlwith_options_async(request, runtime)

    def get_table_objects_with_options(
        self,
        request: adb_20211201_models.GetTableObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableObjectsResponse:
        """
        @summary 获取table概要信息
        
        @param request: GetTableObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_description):
            query['FilterDescription'] = request.filter_description
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_tbl_name):
            query['FilterTblName'] = request.filter_tbl_name
        if not UtilClient.is_unset(request.filter_tbl_type):
            query['FilterTblType'] = request.filter_tbl_type
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_objects_with_options_async(
        self,
        request: adb_20211201_models.GetTableObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetTableObjectsResponse:
        """
        @summary 获取table概要信息
        
        @param request: GetTableObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_description):
            query['FilterDescription'] = request.filter_description
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_tbl_name):
            query['FilterTblName'] = request.filter_tbl_name
        if not UtilClient.is_unset(request.filter_tbl_type):
            query['FilterTblType'] = request.filter_tbl_type
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetTableObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_objects(
        self,
        request: adb_20211201_models.GetTableObjectsRequest,
    ) -> adb_20211201_models.GetTableObjectsResponse:
        """
        @summary 获取table概要信息
        
        @param request: GetTableObjectsRequest
        @return: GetTableObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_objects_with_options(request, runtime)

    async def get_table_objects_async(
        self,
        request: adb_20211201_models.GetTableObjectsRequest,
    ) -> adb_20211201_models.GetTableObjectsResponse:
        """
        @summary 获取table概要信息
        
        @param request: GetTableObjectsRequest
        @return: GetTableObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_objects_with_options_async(request, runtime)

    def get_view_ddlwith_options(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewDDLResponse:
        """
        @summary Queries the statement that is used to create a view.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewDDLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetViewDDLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewDDLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_view_ddlwith_options_async(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewDDLResponse:
        """
        @summary Queries the statement that is used to create a view.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewDDLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetViewDDLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewDDLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_view_ddl(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
    ) -> adb_20211201_models.GetViewDDLResponse:
        """
        @summary Queries the statement that is used to create a view.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewDDLRequest
        @return: GetViewDDLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_view_ddlwith_options(request, runtime)

    async def get_view_ddl_async(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
    ) -> adb_20211201_models.GetViewDDLResponse:
        """
        @summary Queries the statement that is used to create a view.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewDDLRequest
        @return: GetViewDDLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_view_ddlwith_options_async(request, runtime)

    def get_view_objects_with_options(
        self,
        request: adb_20211201_models.GetViewObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewObjectsResponse:
        """
        @summary Queries the information about views.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetViewObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not UtilClient.is_unset(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_view_objects_with_options_async(
        self,
        request: adb_20211201_models.GetViewObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewObjectsResponse:
        """
        @summary Queries the information about views.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetViewObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not UtilClient.is_unset(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not UtilClient.is_unset(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewObjects',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_view_objects(
        self,
        request: adb_20211201_models.GetViewObjectsRequest,
    ) -> adb_20211201_models.GetViewObjectsResponse:
        """
        @summary Queries the information about views.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewObjectsRequest
        @return: GetViewObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_view_objects_with_options(request, runtime)

    async def get_view_objects_async(
        self,
        request: adb_20211201_models.GetViewObjectsRequest,
    ) -> adb_20211201_models.GetViewObjectsResponse:
        """
        @summary Queries the information about views.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: GetViewObjectsRequest
        @return: GetViewObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_view_objects_with_options_async(request, runtime)

    def kill_spark_app_with_options(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkAppResponse:
        """
        @summary Terminates a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_app_with_options_async(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkAppResponse:
        """
        @summary Terminates a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_app(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
    ) -> adb_20211201_models.KillSparkAppResponse:
        """
        @summary Terminates a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkAppRequest
        @return: KillSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_app_with_options(request, runtime)

    async def kill_spark_app_async(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
    ) -> adb_20211201_models.KillSparkAppResponse:
        """
        @summary Terminates a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkAppRequest
        @return: KillSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_app_with_options_async(request, runtime)

    def kill_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        """
        @summary Terminates a Spark log analysis task and queries the information about the analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        """
        @summary Terminates a Spark log analysis task and queries the information about the analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_log_analyze_task(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        """
        @summary Terminates a Spark log analysis task and queries the information about the analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkLogAnalyzeTaskRequest
        @return: KillSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_log_analyze_task_with_options(request, runtime)

    async def kill_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        """
        @summary Terminates a Spark log analysis task and queries the information about the analysis task.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkLogAnalyzeTaskRequest
        @return: KillSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_log_analyze_task_with_options_async(request, runtime)

    def kill_spark_sqlengine_with_options(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        """
        @summary Shuts down a Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_sqlengine_with_options_async(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        """
        @summary Shuts down a Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_sqlengine(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        """
        @summary Shuts down a Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkSQLEngineRequest
        @return: KillSparkSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_sqlengine_with_options(request, runtime)

    async def kill_spark_sqlengine_async(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        """
        @summary Shuts down a Spark SQL engine.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: KillSparkSQLEngineRequest
        @return: KillSparkSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_sqlengine_with_options_async(request, runtime)

    def list_spark_app_attempts_with_options(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        """
        @summary Queries the information about retry attempts of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkAppAttemptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkAppAttemptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkAppAttempts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_app_attempts_with_options_async(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        """
        @summary Queries the information about retry attempts of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkAppAttemptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkAppAttemptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkAppAttempts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_app_attempts(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        """
        @summary Queries the information about retry attempts of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkAppAttemptsRequest
        @return: ListSparkAppAttemptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_app_attempts_with_options(request, runtime)

    async def list_spark_app_attempts_async(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        """
        @summary Queries the information about retry attempts of a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkAppAttemptsRequest
        @return: ListSparkAppAttemptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_app_attempts_with_options_async(request, runtime)

    def list_spark_apps_with_options(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        """
        @summary Queries the Spark applications that run on an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: ListSparkAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkApps',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_apps_with_options_async(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        """
        @summary Queries the Spark applications that run on an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: ListSparkAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkApps',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_apps(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        """
        @summary Queries the Spark applications that run on an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: ListSparkAppsRequest
        @return: ListSparkAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_apps_with_options(request, runtime)

    async def list_spark_apps_async(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        """
        @summary Queries the Spark applications that run on an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @param request: ListSparkAppsRequest
        @return: ListSparkAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_apps_with_options_async(request, runtime)

    def list_spark_log_analyze_tasks_with_options(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        """
        @summary Queries a list of Spark log analysis tasks.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkLogAnalyzeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkLogAnalyzeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkLogAnalyzeTasks',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkLogAnalyzeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_log_analyze_tasks_with_options_async(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        """
        @summary Queries a list of Spark log analysis tasks.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkLogAnalyzeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkLogAnalyzeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkLogAnalyzeTasks',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkLogAnalyzeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_log_analyze_tasks(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        """
        @summary Queries a list of Spark log analysis tasks.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkLogAnalyzeTasksRequest
        @return: ListSparkLogAnalyzeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_log_analyze_tasks_with_options(request, runtime)

    async def list_spark_log_analyze_tasks_async(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        """
        @summary Queries a list of Spark log analysis tasks.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkLogAnalyzeTasksRequest
        @return: ListSparkLogAnalyzeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_log_analyze_tasks_with_options_async(request, runtime)

    def list_spark_template_file_ids_with_options(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        """
        @summary Queries all Spark template file IDs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkTemplateFileIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkTemplateFileIdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkTemplateFileIds',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkTemplateFileIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_template_file_ids_with_options_async(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        """
        @summary Queries all Spark template file IDs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkTemplateFileIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkTemplateFileIdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkTemplateFileIds',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkTemplateFileIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_template_file_ids(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        """
        @summary Queries all Spark template file IDs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkTemplateFileIdsRequest
        @return: ListSparkTemplateFileIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_template_file_ids_with_options(request, runtime)

    async def list_spark_template_file_ids_async(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        """
        @summary Queries all Spark template file IDs of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: ListSparkTemplateFileIdsRequest
        @return: ListSparkTemplateFileIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_template_file_ids_with_options_async(request, runtime)

    def load_sample_data_set_with_options(
        self,
        request: adb_20211201_models.LoadSampleDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.LoadSampleDataSetResponse:
        """
        @summary Loads a built-in dataset.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: LoadSampleDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadSampleDataSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoadSampleDataSet',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.LoadSampleDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_sample_data_set_with_options_async(
        self,
        request: adb_20211201_models.LoadSampleDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.LoadSampleDataSetResponse:
        """
        @summary Loads a built-in dataset.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: LoadSampleDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadSampleDataSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoadSampleDataSet',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.LoadSampleDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_sample_data_set(
        self,
        request: adb_20211201_models.LoadSampleDataSetRequest,
    ) -> adb_20211201_models.LoadSampleDataSetResponse:
        """
        @summary Loads a built-in dataset.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: LoadSampleDataSetRequest
        @return: LoadSampleDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.load_sample_data_set_with_options(request, runtime)

    async def load_sample_data_set_async(
        self,
        request: adb_20211201_models.LoadSampleDataSetRequest,
    ) -> adb_20211201_models.LoadSampleDataSetResponse:
        """
        @summary Loads a built-in dataset.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: LoadSampleDataSetRequest
        @return: LoadSampleDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.load_sample_data_set_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_privileges_with_options(
        self,
        tmp_req: adb_20211201_models.ModifyAccountPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountPrivilegesResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param tmp_req: ModifyAccountPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyAccountPrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_privileges):
            request.account_privileges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_privileges, 'AccountPrivileges', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privileges_shrink):
            query['AccountPrivileges'] = request.account_privileges_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privileges_with_options_async(
        self,
        tmp_req: adb_20211201_models.ModifyAccountPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountPrivilegesResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param tmp_req: ModifyAccountPrivilegesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyAccountPrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_privileges):
            request.account_privileges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_privileges, 'AccountPrivileges', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privileges_shrink):
            query['AccountPrivileges'] = request.account_privileges_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivileges',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privileges(
        self,
        request: adb_20211201_models.ModifyAccountPrivilegesRequest,
    ) -> adb_20211201_models.ModifyAccountPrivilegesResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAccountPrivilegesRequest
        @return: ModifyAccountPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privileges_with_options(request, runtime)

    async def modify_account_privileges_async(
        self,
        request: adb_20211201_models.ModifyAccountPrivilegesRequest,
    ) -> adb_20211201_models.ModifyAccountPrivilegesResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAccountPrivilegesRequest
        @return: ModifyAccountPrivilegesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_privileges_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the SQL audit configuration of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the SQL audit configuration of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the SQL audit configuration of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the SQL audit configuration of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup policy of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup policy of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup policy of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup policy of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_access_white_list_with_options(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAccessWhiteListResponse
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
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_access_white_list_with_options_async(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAccessWhiteListResponse
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
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_access_white_list(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyClusterAccessWhiteListRequest
        @return: ModifyClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_access_white_list_with_options(request, runtime)

    async def modify_cluster_access_white_list_async(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyClusterAccessWhiteListRequest
        @return: ModifyClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_access_white_list_with_options_async(request, runtime)

    def modify_cluster_connection_string_with_options(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        """
        @summary Modifies the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_connection_string_with_options_async(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        """
        @summary Modifies the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_connection_string(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        """
        @summary Modifies the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyClusterConnectionStringRequest
        @return: ModifyClusterConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_connection_string_with_options(request, runtime)

    async def modify_cluster_connection_string_async(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        """
        @summary Modifies the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyClusterConnectionStringRequest
        @return: ModifyClusterConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_connection_string_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        """
        @summary Changes the configurations of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        During a scaling event, you are not allowed to execute the `SUBMIT JOB` statement to submit asynchronous jobs. If your business requires asynchronous jobs, perform scaling during appropriate periods.
        When you scale a cluster, data in the cluster is migrated for redistribution. The amount of time that is required to migrate data is proportional to the data volume. During a scaling event, the services provided by the cluster are not interrupted. When you downgrade cluster specifications, data migration may require up to dozens of hours to complete. Proceed with caution especially if your cluster contains a large amount of data.
        If the cluster has a built-in dataset loaded, make sure that the cluster has reserved storage resources of at least 24 AnalyticDB compute units (ACUs). Otherwise, the built-in dataset cannot be used.
        When the scaling process is about to end, transient connections may occur. We recommend that you scale your cluster during off-peak hours or make sure that your application is configured to automatically reconnect to your cluster.
        You can change an AnalyticDB for MySQL cluster from Data Warehouse Edition (V3.0) to Data Lakehouse Edition (V3.0), but not the other way around. For more information, see Change a cluster from Data Warehouse Edition to Data Lakehouse Edition. For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        """
        @summary Changes the configurations of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        During a scaling event, you are not allowed to execute the `SUBMIT JOB` statement to submit asynchronous jobs. If your business requires asynchronous jobs, perform scaling during appropriate periods.
        When you scale a cluster, data in the cluster is migrated for redistribution. The amount of time that is required to migrate data is proportional to the data volume. During a scaling event, the services provided by the cluster are not interrupted. When you downgrade cluster specifications, data migration may require up to dozens of hours to complete. Proceed with caution especially if your cluster contains a large amount of data.
        If the cluster has a built-in dataset loaded, make sure that the cluster has reserved storage resources of at least 24 AnalyticDB compute units (ACUs). Otherwise, the built-in dataset cannot be used.
        When the scaling process is about to end, transient connections may occur. We recommend that you scale your cluster during off-peak hours or make sure that your application is configured to automatically reconnect to your cluster.
        You can change an AnalyticDB for MySQL cluster from Data Warehouse Edition (V3.0) to Data Lakehouse Edition (V3.0), but not the other way around. For more information, see Change a cluster from Data Warehouse Edition to Data Lakehouse Edition. For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not UtilClient.is_unset(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        """
        @summary Changes the configurations of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        During a scaling event, you are not allowed to execute the `SUBMIT JOB` statement to submit asynchronous jobs. If your business requires asynchronous jobs, perform scaling during appropriate periods.
        When you scale a cluster, data in the cluster is migrated for redistribution. The amount of time that is required to migrate data is proportional to the data volume. During a scaling event, the services provided by the cluster are not interrupted. When you downgrade cluster specifications, data migration may require up to dozens of hours to complete. Proceed with caution especially if your cluster contains a large amount of data.
        If the cluster has a built-in dataset loaded, make sure that the cluster has reserved storage resources of at least 24 AnalyticDB compute units (ACUs). Otherwise, the built-in dataset cannot be used.
        When the scaling process is about to end, transient connections may occur. We recommend that you scale your cluster during off-peak hours or make sure that your application is configured to automatically reconnect to your cluster.
        You can change an AnalyticDB for MySQL cluster from Data Warehouse Edition (V3.0) to Data Lakehouse Edition (V3.0), but not the other way around. For more information, see Change a cluster from Data Warehouse Edition to Data Lakehouse Edition. For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        """
        @summary Changes the configurations of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description ### [](#)
        During a scaling event, you are not allowed to execute the `SUBMIT JOB` statement to submit asynchronous jobs. If your business requires asynchronous jobs, perform scaling during appropriate periods.
        When you scale a cluster, data in the cluster is migrated for redistribution. The amount of time that is required to migrate data is proportional to the data volume. During a scaling event, the services provided by the cluster are not interrupted. When you downgrade cluster specifications, data migration may require up to dozens of hours to complete. Proceed with caution especially if your cluster contains a large amount of data.
        If the cluster has a built-in dataset loaded, make sure that the cluster has reserved storage resources of at least 24 AnalyticDB compute units (ACUs). Otherwise, the built-in dataset cannot be used.
        When the scaling process is about to end, transient connections may occur. We recommend that you scale your cluster during off-peak hours or make sure that your application is configured to automatically reconnect to your cluster.
        You can change an AnalyticDB for MySQL cluster from Data Warehouse Edition (V3.0) to Data Lakehouse Edition (V3.0), but not the other way around. For more information, see Change a cluster from Data Warehouse Edition to Data Lakehouse Edition. For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the description of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster to facilitate the maintenance and management of the cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the description of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster to facilitate the maintenance and management of the cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the description of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster to facilitate the maintenance and management of the cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the description of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster to facilitate the maintenance and management of the cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbresource_group_with_options(
        self,
        tmp_req: adb_20211201_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the amount of reserved computing resources for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param tmp_req: ModifyDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_group_with_options_async(
        self,
        tmp_req: adb_20211201_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the amount of reserved computing resources for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param tmp_req: ModifyDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBResourceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyDBResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rules):
            request.rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_group(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the amount of reserved computing resources for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBResourceGroupRequest
        @return: ModifyDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    async def modify_dbresource_group_async(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        """
        @summary Modifies the amount of reserved computing resources for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ModifyDBResourceGroupRequest
        @return: ModifyDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbresource_group_with_options_async(request, runtime)

    def modify_elastic_plan_with_options(
        self,
        request: adb_20211201_models.ModifyElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_size):
            query['TargetSize'] = request.target_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_plan_with_options_async(
        self,
        request: adb_20211201_models.ModifyElasticPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyElasticPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_size):
            query['TargetSize'] = request.target_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticPlan',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_plan(
        self,
        request: adb_20211201_models.ModifyElasticPlanRequest,
    ) -> adb_20211201_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyElasticPlanRequest
        @return: ModifyElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_plan_with_options(request, runtime)

    async def modify_elastic_plan_async(
        self,
        request: adb_20211201_models.ModifyElasticPlanRequest,
    ) -> adb_20211201_models.ModifyElasticPlanResponse:
        """
        @summary Modifies a scaling plan for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: ModifyElasticPlanRequest
        @return: ModifyElasticPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_plan_with_options_async(request, runtime)

    def modify_performance_view_with_options(
        self,
        tmp_req: adb_20211201_models.ModifyPerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyPerformanceViewResponse:
        """
        @param tmp_req: ModifyPerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPerformanceViewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyPerformanceViewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_detail):
            request.view_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
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
        if not UtilClient.is_unset(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyPerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_performance_view_with_options_async(
        self,
        tmp_req: adb_20211201_models.ModifyPerformanceViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyPerformanceViewResponse:
        """
        @param tmp_req: ModifyPerformanceViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPerformanceViewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_20211201_models.ModifyPerformanceViewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_detail):
            request.view_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
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
        if not UtilClient.is_unset(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPerformanceView',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyPerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_performance_view(
        self,
        request: adb_20211201_models.ModifyPerformanceViewRequest,
    ) -> adb_20211201_models.ModifyPerformanceViewResponse:
        """
        @param request: ModifyPerformanceViewRequest
        @return: ModifyPerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_performance_view_with_options(request, runtime)

    async def modify_performance_view_async(
        self,
        request: adb_20211201_models.ModifyPerformanceViewRequest,
    ) -> adb_20211201_models.ModifyPerformanceViewResponse:
        """
        @param request: ModifyPerformanceViewRequest
        @return: ModifyPerformanceViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_performance_view_with_options_async(request, runtime)

    def preload_spark_app_metrics_with_options(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary Preloads metrics for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: PreloadSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.PreloadSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_spark_app_metrics_with_options_async(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary Preloads metrics for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: PreloadSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.PreloadSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_spark_app_metrics(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary Preloads metrics for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: PreloadSparkAppMetricsRequest
        @return: PreloadSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_spark_app_metrics_with_options(request, runtime)

    async def preload_spark_app_metrics_async(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary Preloads metrics for a Spark application.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: PreloadSparkAppMetricsRequest
        @return: PreloadSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preload_spark_app_metrics_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def rename_spark_template_file_with_options(
        self,
        request: adb_20211201_models.RenameSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.RenameSparkTemplateFileResponse:
        """
        @summary Renames a Spark template file.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: RenameSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.RenameSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_spark_template_file_with_options_async(
        self,
        request: adb_20211201_models.RenameSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.RenameSparkTemplateFileResponse:
        """
        @summary Renames a Spark template file.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: RenameSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.RenameSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_spark_template_file(
        self,
        request: adb_20211201_models.RenameSparkTemplateFileRequest,
    ) -> adb_20211201_models.RenameSparkTemplateFileResponse:
        """
        @summary Renames a Spark template file.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: RenameSparkTemplateFileRequest
        @return: RenameSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_spark_template_file_with_options(request, runtime)

    async def rename_spark_template_file_async(
        self,
        request: adb_20211201_models.RenameSparkTemplateFileRequest,
    ) -> adb_20211201_models.RenameSparkTemplateFileResponse:
        """
        @summary Renames a Spark template file.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: RenameSparkTemplateFileRequest
        @return: RenameSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_spark_template_file_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def set_spark_app_log_root_path_with_options(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        """
        @summary Modifies the Spark log configuration.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SetSparkAppLogRootPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSparkAppLogRootPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not UtilClient.is_unset(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSparkAppLogRootPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SetSparkAppLogRootPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_spark_app_log_root_path_with_options_async(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        """
        @summary Modifies the Spark log configuration.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SetSparkAppLogRootPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSparkAppLogRootPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not UtilClient.is_unset(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSparkAppLogRootPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SetSparkAppLogRootPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_spark_app_log_root_path(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        """
        @summary Modifies the Spark log configuration.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SetSparkAppLogRootPathRequest
        @return: SetSparkAppLogRootPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_spark_app_log_root_path_with_options(request, runtime)

    async def set_spark_app_log_root_path_async(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        """
        @summary Modifies the Spark log configuration.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SetSparkAppLogRootPathRequest
        @return: SetSparkAppLogRootPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_spark_app_log_root_path_with_options_async(request, runtime)

    def start_spark_sqlengine_with_options(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        """
        @summary Starts the Spark SQL engine.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: StartSparkSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSparkSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.jars):
            body['Jars'] = request.jars
        if not UtilClient.is_unset(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not UtilClient.is_unset(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.StartSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_spark_sqlengine_with_options_async(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        """
        @summary Starts the Spark SQL engine.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: StartSparkSQLEngineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSparkSQLEngineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.jars):
            body['Jars'] = request.jars
        if not UtilClient.is_unset(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not UtilClient.is_unset(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.StartSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_spark_sqlengine(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        """
        @summary Starts the Spark SQL engine.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: StartSparkSQLEngineRequest
        @return: StartSparkSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_spark_sqlengine_with_options(request, runtime)

    async def start_spark_sqlengine_async(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        """
        @summary Starts the Spark SQL engine.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: StartSparkSQLEngineRequest
        @return: StartSparkSQLEngineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_spark_sqlengine_with_options_async(request, runtime)

    def submit_spark_app_with_options(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        """
        @summary Submits a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: SubmitSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_app_with_options_async(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        """
        @summary Submits a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: SubmitSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_app(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        """
        @summary Submits a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: SubmitSparkAppRequest
        @return: SubmitSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_app_with_options(request, runtime)

    async def submit_spark_app_async(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        """
        @summary Submits a Spark application.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: SubmitSparkAppRequest
        @return: SubmitSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_app_with_options_async(request, runtime)

    def submit_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        """
        @summary Submits a Spark log analysis task and queries the analysis results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SubmitSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        """
        @summary Submits a Spark log analysis task and queries the analysis results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SubmitSparkLogAnalyzeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkLogAnalyzeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_log_analyze_task(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        """
        @summary Submits a Spark log analysis task and queries the analysis results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SubmitSparkLogAnalyzeTaskRequest
        @return: SubmitSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_log_analyze_task_with_options(request, runtime)

    async def submit_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        """
        @summary Submits a Spark log analysis task and queries the analysis results.
        
        @description    General endpoint: `adb.aliyuncs.com`.
        Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        
        @param request: SubmitSparkLogAnalyzeTaskRequest
        @return: SubmitSparkLogAnalyzeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_log_analyze_task_with_options_async(request, runtime)

    def unbind_account_with_options(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindAccountResponse:
        """
        @summary Disassociates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster from a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: UnbindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_account_with_options_async(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindAccountResponse:
        """
        @summary Disassociates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster from a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: UnbindAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_account(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
    ) -> adb_20211201_models.UnbindAccountResponse:
        """
        @summary Disassociates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster from a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: UnbindAccountRequest
        @return: UnbindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_account_with_options(request, runtime)

    async def unbind_account_async(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
    ) -> adb_20211201_models.UnbindAccountResponse:
        """
        @summary Disassociates a standard database account of an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster from a Resource Access Management (RAM) user.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see Endpoints.
        
        @param request: UnbindAccountRequest
        @return: UnbindAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_account_with_options_async(request, runtime)

    def unbind_dbresource_group_with_user_with_options(
        self,
        request: adb_20211201_models.UnbindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates resource groups from database accounts for an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourceGroupWithUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_group_with_user_with_options_async(
        self,
        request: adb_20211201_models.UnbindDBResourceGroupWithUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates resource groups from database accounts for an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDBResourceGroupWithUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDBResourceGroupWithUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_group_with_user(
        self,
        request: adb_20211201_models.UnbindDBResourceGroupWithUserRequest,
    ) -> adb_20211201_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates resource groups from database accounts for an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @return: UnbindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_dbresource_group_with_user_with_options(request, runtime)

    async def unbind_dbresource_group_with_user_async(
        self,
        request: adb_20211201_models.UnbindDBResourceGroupWithUserRequest,
    ) -> adb_20211201_models.UnbindDBResourceGroupWithUserResponse:
        """
        @summary Disassociates resource groups from database accounts for an AnalyticDB for MySQL cluster.
        
        @description For information about the endpoints of AnalyticDB for MySQL, see [Endpoints](https://help.aliyun.com/document_detail/612373.html).
        
        @param request: UnbindDBResourceGroupWithUserRequest
        @return: UnbindDBResourceGroupWithUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_dbresource_group_with_user_with_options_async(request, runtime)

    def update_spark_template_file_with_options(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        """
        @summary Updates a Spark application template.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: UpdateSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UpdateSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_spark_template_file_with_options_async(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        """
        @summary Updates a Spark application template.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: UpdateSparkTemplateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSparkTemplateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UpdateSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_spark_template_file(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        """
        @summary Updates a Spark application template.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: UpdateSparkTemplateFileRequest
        @return: UpdateSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_spark_template_file_with_options(request, runtime)

    async def update_spark_template_file_async(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        """
        @summary Updates a Spark application template.
        
        @description    Regional public endpoint: `adb.<region-id>.aliyuncs.com`. Example: `adb.cn-hangzhou.aliyuncs.com`.
        Regional Virtual Private Cloud (VPC) endpoint: `adb-vpc.<region-id>.aliyuncs.com`. Example: `adb-vpc.cn-hangzhou.aliyuncs.com`.
        >  If HTTP status code 409 is returned when you call this operation in the China (Qingdao), China (Shenzhen), China (Guangzhou), or China (Hong Kong) region, contact technical support.
        
        @param request: UpdateSparkTemplateFileRequest
        @return: UpdateSparkTemplateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_spark_template_file_with_options_async(request, runtime)
