# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_r_kvstore20150101 import models as r_kvstore_20150101_models
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
            'cn-qingdao': 'r-kvstore.aliyuncs.com',
            'cn-beijing': 'r-kvstore.aliyuncs.com',
            'cn-wulanchabu': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou': 'r-kvstore.aliyuncs.com',
            'cn-shanghai': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen': 'r-kvstore.aliyuncs.com',
            'cn-heyuan': 'r-kvstore.aliyuncs.com',
            'cn-guangzhou': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-finance': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-north-2-gov-1': 'r-kvstore.aliyuncs.com',
            'ap-northeast-2-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-gov-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-nu16-b01': 'r-kvstore.aliyuncs.com',
            'cn-edge-1': 'r-kvstore.aliyuncs.com',
            'cn-fujian': 'r-kvstore.aliyuncs.com',
            'cn-haidian-cm12-c01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-test-306': 'r-kvstore.aliyuncs.com',
            'cn-hongkong-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-qingdao-nebula': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et15-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et2-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-inner': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-inner': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'r-kvstore.aliyuncs.com',
            'cn-wuhan': 'r-kvstore.aliyuncs.com',
            'cn-yushanfang': 'r-kvstore.aliyuncs.com',
            'cn-zhangbei': 'r-kvstore.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'r-kvstore.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'r-kvstore.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'r-kvstore.aliyuncs.com',
            'eu-west-1-oxs': 'r-kvstore.aliyuncs.com',
            'rus-west-1-pop': 'r-kvstore.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('r-kvstore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        """
        @summary Adds one or more data shards to an ApsaraDB for Redis cluster instance.
        
        @description This operation is available only for cluster instances that use cloud disks.
        
        @param request: AddShardingNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShardingNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        """
        @summary Adds one or more data shards to an ApsaraDB for Redis cluster instance.
        
        @description This operation is available only for cluster instances that use cloud disks.
        
        @param request: AddShardingNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShardingNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sharding_node(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        """
        @summary Adds one or more data shards to an ApsaraDB for Redis cluster instance.
        
        @description This operation is available only for cluster instances that use cloud disks.
        
        @param request: AddShardingNodeRequest
        @return: AddShardingNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_sharding_node_with_options(request, runtime)

    async def add_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        """
        @summary Adds one or more data shards to an ApsaraDB for Redis cluster instance.
        
        @description This operation is available only for cluster instances that use cloud disks.
        
        @param request: AddShardingNodeRequest
        @return: AddShardingNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_sharding_node_with_options_async(request, runtime)

    def allocate_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        """
        @summary Applies for a private endpoint for an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, you can use private endpoints to bypass proxy nodes and connect to ApsaraDB for Redis instances from clients in the same manner as you connect to native Redis clusters. The direct connection mode can reduce communication overheads and accelerate the response speed. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        To call this operation, the instance must meet the following requirements:
        The instance is an ApsaraDB for Redis cluster instance.
        The instance is a Community Edition instance that runs Redis 4.0 or 5.0, or an Enhanced Edition instance (Tair) that runs Redis 5.0.
        The instance is deployed in a virtual private cloud (VPC). If the instance is deployed in the classic network, call the [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html) operation to change the network type to VPC.
        SSL encryption is disabled for the instance. If SSL encryption is enabled, you can call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation to disable it.
        The vSwitch to which the instance is connected has sufficient IP addresses to be allocated. For more information, see [Obtain the number of available IP addresses in the vSwitch to which an ApsaraDB for Redis instance is connected](https://help.aliyun.com/document_detail/183151.html).
        
        @param request: AllocateDirectConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateDirectConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        """
        @summary Applies for a private endpoint for an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, you can use private endpoints to bypass proxy nodes and connect to ApsaraDB for Redis instances from clients in the same manner as you connect to native Redis clusters. The direct connection mode can reduce communication overheads and accelerate the response speed. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        To call this operation, the instance must meet the following requirements:
        The instance is an ApsaraDB for Redis cluster instance.
        The instance is a Community Edition instance that runs Redis 4.0 or 5.0, or an Enhanced Edition instance (Tair) that runs Redis 5.0.
        The instance is deployed in a virtual private cloud (VPC). If the instance is deployed in the classic network, call the [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html) operation to change the network type to VPC.
        SSL encryption is disabled for the instance. If SSL encryption is enabled, you can call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation to disable it.
        The vSwitch to which the instance is connected has sufficient IP addresses to be allocated. For more information, see [Obtain the number of available IP addresses in the vSwitch to which an ApsaraDB for Redis instance is connected](https://help.aliyun.com/document_detail/183151.html).
        
        @param request: AllocateDirectConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateDirectConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_direct_connection(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        """
        @summary Applies for a private endpoint for an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, you can use private endpoints to bypass proxy nodes and connect to ApsaraDB for Redis instances from clients in the same manner as you connect to native Redis clusters. The direct connection mode can reduce communication overheads and accelerate the response speed. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        To call this operation, the instance must meet the following requirements:
        The instance is an ApsaraDB for Redis cluster instance.
        The instance is a Community Edition instance that runs Redis 4.0 or 5.0, or an Enhanced Edition instance (Tair) that runs Redis 5.0.
        The instance is deployed in a virtual private cloud (VPC). If the instance is deployed in the classic network, call the [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html) operation to change the network type to VPC.
        SSL encryption is disabled for the instance. If SSL encryption is enabled, you can call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation to disable it.
        The vSwitch to which the instance is connected has sufficient IP addresses to be allocated. For more information, see [Obtain the number of available IP addresses in the vSwitch to which an ApsaraDB for Redis instance is connected](https://help.aliyun.com/document_detail/183151.html).
        
        @param request: AllocateDirectConnectionRequest
        @return: AllocateDirectConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_direct_connection_with_options(request, runtime)

    async def allocate_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        """
        @summary Applies for a private endpoint for an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, you can use private endpoints to bypass proxy nodes and connect to ApsaraDB for Redis instances from clients in the same manner as you connect to native Redis clusters. The direct connection mode can reduce communication overheads and accelerate the response speed. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        To call this operation, the instance must meet the following requirements:
        The instance is an ApsaraDB for Redis cluster instance.
        The instance is a Community Edition instance that runs Redis 4.0 or 5.0, or an Enhanced Edition instance (Tair) that runs Redis 5.0.
        The instance is deployed in a virtual private cloud (VPC). If the instance is deployed in the classic network, call the [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html) operation to change the network type to VPC.
        SSL encryption is disabled for the instance. If SSL encryption is enabled, you can call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation to disable it.
        The vSwitch to which the instance is connected has sufficient IP addresses to be allocated. For more information, see [Obtain the number of available IP addresses in the vSwitch to which an ApsaraDB for Redis instance is connected](https://help.aliyun.com/document_detail/183151.html).
        
        @param request: AllocateDirectConnectionRequest
        @return: AllocateDirectConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_direct_connection_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for Redis instance.
        
        @description You can also apply for public endpoints in the ApsaraDB for Redis console. For more information, see [Use a public endpoint to connect to an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/43850.html).
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for Redis instance.
        
        @description You can also apply for public endpoints in the ApsaraDB for Redis console. For more information, see [Use a public endpoint to connect to an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/43850.html).
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for Redis instance.
        
        @description You can also apply for public endpoints in the ApsaraDB for Redis console. For more information, see [Use a public endpoint to connect to an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/43850.html).
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for Redis instance.
        
        @description You can also apply for public endpoints in the ApsaraDB for Redis console. For more information, see [Use a public endpoint to connect to an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/43850.html).
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary Queries whether an ApsaraDB for Redis instance is authorized to use Key Management Service (KMS).
        
        @description    For information about Transparent Data Encryption (TDE) and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        If the ApsaraDB for Redis instance is authorized to use KMS, you can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable TDE.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary Queries whether an ApsaraDB for Redis instance is authorized to use Key Management Service (KMS).
        
        @description    For information about Transparent Data Encryption (TDE) and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        If the ApsaraDB for Redis instance is authorized to use KMS, you can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable TDE.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary Queries whether an ApsaraDB for Redis instance is authorized to use Key Management Service (KMS).
        
        @description    For information about Transparent Data Encryption (TDE) and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        If the ApsaraDB for Redis instance is authorized to use KMS, you can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable TDE.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary Queries whether an ApsaraDB for Redis instance is authorized to use Key Management Service (KMS).
        
        @description    For information about Transparent Data Encryption (TDE) and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        If the ApsaraDB for Redis instance is authorized to use KMS, you can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable TDE.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        """
        @summary Creates an account that has specific permissions for an ApsaraDB for Redis instance.
        
        @description >
        This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0 or later.
        The ApsaraDB for Redis instance for which you want to call this operation must be in the running state.
        You can create up to 18 accounts for an ApsaraDB for Redis instance.
        You can also create an account in the ApsaraDB for Redis console. For more information, see [Manage database accounts](https://help.aliyun.com/document_detail/92665.html).
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        """
        @summary Creates an account that has specific permissions for an ApsaraDB for Redis instance.
        
        @description >
        This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0 or later.
        The ApsaraDB for Redis instance for which you want to call this operation must be in the running state.
        You can create up to 18 accounts for an ApsaraDB for Redis instance.
        You can also create an account in the ApsaraDB for Redis console. For more information, see [Manage database accounts](https://help.aliyun.com/document_detail/92665.html).
        
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
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        """
        @summary Creates an account that has specific permissions for an ApsaraDB for Redis instance.
        
        @description >
        This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0 or later.
        The ApsaraDB for Redis instance for which you want to call this operation must be in the running state.
        You can create up to 18 accounts for an ApsaraDB for Redis instance.
        You can also create an account in the ApsaraDB for Redis console. For more information, see [Manage database accounts](https://help.aliyun.com/document_detail/92665.html).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        """
        @summary Creates an account that has specific permissions for an ApsaraDB for Redis instance.
        
        @description >
        This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0 or later.
        The ApsaraDB for Redis instance for which you want to call this operation must be in the running state.
        You can create up to 18 accounts for an ApsaraDB for Redis instance.
        You can also create an account in the ApsaraDB for Redis console. For more information, see [Manage database accounts](https://help.aliyun.com/document_detail/92665.html).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        """
        @summary Backs up an ApsaraDB for Redis instance.
        
        @description You can also back up an instance in the ApsaraDB for Redis console. For more information, see [Backup and recovery](https://help.aliyun.com/document_detail/43886.html).
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateBackup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        """
        @summary Backs up an ApsaraDB for Redis instance.
        
        @description You can also back up an instance in the ApsaraDB for Redis console. For more information, see [Backup and recovery](https://help.aliyun.com/document_detail/43886.html).
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateBackup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        """
        @summary Backs up an ApsaraDB for Redis instance.
        
        @description You can also back up an instance in the ApsaraDB for Redis console. For more information, see [Backup and recovery](https://help.aliyun.com/document_detail/43886.html).
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        """
        @summary Backs up an ApsaraDB for Redis instance.
        
        @description You can also back up an instance in the ApsaraDB for Redis console. For more information, see [Backup and recovery](https://help.aliyun.com/document_detail/43886.html).
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_cache_analysis_task_with_options(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        """
        @summary Manually creates a cache analytics task.
        
        @description This operation is no longer available. Use the new operation. For more information, see [Real-time key statistics and offline key analysis](https://help.aliyun.com/document_detail/184226.html).
        
        @param request: CreateCacheAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCacheAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateCacheAnalysisTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cache_analysis_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        """
        @summary Manually creates a cache analytics task.
        
        @description This operation is no longer available. Use the new operation. For more information, see [Real-time key statistics and offline key analysis](https://help.aliyun.com/document_detail/184226.html).
        
        @param request: CreateCacheAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCacheAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateCacheAnalysisTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cache_analysis_task(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        """
        @summary Manually creates a cache analytics task.
        
        @description This operation is no longer available. Use the new operation. For more information, see [Real-time key statistics and offline key analysis](https://help.aliyun.com/document_detail/184226.html).
        
        @param request: CreateCacheAnalysisTaskRequest
        @return: CreateCacheAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_task_with_options(request, runtime)

    async def create_cache_analysis_task_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        """
        @summary Manually creates a cache analytics task.
        
        @description This operation is no longer available. Use the new operation. For more information, see [Real-time key statistics and offline key analysis](https://help.aliyun.com/document_detail/184226.html).
        
        @param request: CreateCacheAnalysisTaskRequest
        @return: CreateCacheAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_task_with_options_async(request, runtime)

    def create_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        """
        @summary Converts an existing ApsaraDB for Redis instance to the first child instance of a distributed ApsaraDB for Redis instance.
        
        @description You cannot directly create a distributed instance. If you require a distributed instance, you must call this operation to convert an existing instance to the first child instance of the distributed instance. After the instance is converted, the distributed instance is created. Before you call this operation, make sure that the following requirements are met:
        A [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html) of Enhanced Edition is used.
        If the existing instance is a cluster instance, the direct connection mode must be disabled for the instance. For more information, see [Release a private endpoint](https://help.aliyun.com/document_detail/150047.html).
        > You can also call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance that is specified as the first child instance of a distributed instance. After the child instance is created, the distributed instance to which the child instance belongs is created.
        
        @param request: CreateGlobalDistributeCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalDistributeCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.seed_sub_instance_id):
            query['SeedSubInstanceId'] = request.seed_sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        """
        @summary Converts an existing ApsaraDB for Redis instance to the first child instance of a distributed ApsaraDB for Redis instance.
        
        @description You cannot directly create a distributed instance. If you require a distributed instance, you must call this operation to convert an existing instance to the first child instance of the distributed instance. After the instance is converted, the distributed instance is created. Before you call this operation, make sure that the following requirements are met:
        A [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html) of Enhanced Edition is used.
        If the existing instance is a cluster instance, the direct connection mode must be disabled for the instance. For more information, see [Release a private endpoint](https://help.aliyun.com/document_detail/150047.html).
        > You can also call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance that is specified as the first child instance of a distributed instance. After the child instance is created, the distributed instance to which the child instance belongs is created.
        
        @param request: CreateGlobalDistributeCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalDistributeCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.seed_sub_instance_id):
            query['SeedSubInstanceId'] = request.seed_sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        """
        @summary Converts an existing ApsaraDB for Redis instance to the first child instance of a distributed ApsaraDB for Redis instance.
        
        @description You cannot directly create a distributed instance. If you require a distributed instance, you must call this operation to convert an existing instance to the first child instance of the distributed instance. After the instance is converted, the distributed instance is created. Before you call this operation, make sure that the following requirements are met:
        A [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html) of Enhanced Edition is used.
        If the existing instance is a cluster instance, the direct connection mode must be disabled for the instance. For more information, see [Release a private endpoint](https://help.aliyun.com/document_detail/150047.html).
        > You can also call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance that is specified as the first child instance of a distributed instance. After the child instance is created, the distributed instance to which the child instance belongs is created.
        
        @param request: CreateGlobalDistributeCacheRequest
        @return: CreateGlobalDistributeCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_distribute_cache_with_options(request, runtime)

    async def create_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        """
        @summary Converts an existing ApsaraDB for Redis instance to the first child instance of a distributed ApsaraDB for Redis instance.
        
        @description You cannot directly create a distributed instance. If you require a distributed instance, you must call this operation to convert an existing instance to the first child instance of the distributed instance. After the instance is converted, the distributed instance is created. Before you call this operation, make sure that the following requirements are met:
        A [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html) of Enhanced Edition is used.
        If the existing instance is a cluster instance, the direct connection mode must be disabled for the instance. For more information, see [Release a private endpoint](https://help.aliyun.com/document_detail/150047.html).
        > You can also call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance that is specified as the first child instance of a distributed instance. After the child instance is created, the distributed instance to which the child instance belongs is created.
        
        @param request: CreateGlobalDistributeCacheRequest
        @return: CreateGlobalDistributeCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_distribute_cache_with_options_async(request, runtime)

    def create_global_security_ipgroup_with_options(
        self,
        request: r_kvstore_20150101_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
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
            action='CreateGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_security_ipgroup_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
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
            action='CreateGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_security_ipgroup(
        self,
        request: r_kvstore_20150101_models.CreateGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_security_ipgroup_with_options(request, runtime)

    async def create_global_security_ipgroup_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_security_ipgroup_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can call this operation to create an ApsaraDB for Redis instance or a classic Tair DRAM-based instance. To create a cloud-native Tair instance, call the [CreateTairInstance](https://help.aliyun.com/document_detail/208271.html) operation.
        > For more information about how to create an instance that meets your requirements in the ApsaraDB for Redis console, see [Step 1: Create an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/26351.html).
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.appendonly):
            query['Appendonly'] = request.appendonly
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_backup_id):
            query['ClusterBackupId'] = request.cluster_backup_id
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param_group_id):
            query['ParamGroupId'] = request.param_group_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.recover_config_mode):
            query['RecoverConfigMode'] = request.recover_config_mode
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
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can call this operation to create an ApsaraDB for Redis instance or a classic Tair DRAM-based instance. To create a cloud-native Tair instance, call the [CreateTairInstance](https://help.aliyun.com/document_detail/208271.html) operation.
        > For more information about how to create an instance that meets your requirements in the ApsaraDB for Redis console, see [Step 1: Create an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/26351.html).
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.appendonly):
            query['Appendonly'] = request.appendonly
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_backup_id):
            query['ClusterBackupId'] = request.cluster_backup_id
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param_group_id):
            query['ParamGroupId'] = request.param_group_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.recover_config_mode):
            query['RecoverConfigMode'] = request.recover_config_mode
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
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can call this operation to create an ApsaraDB for Redis instance or a classic Tair DRAM-based instance. To create a cloud-native Tair instance, call the [CreateTairInstance](https://help.aliyun.com/document_detail/208271.html) operation.
        > For more information about how to create an instance that meets your requirements in the ApsaraDB for Redis console, see [Step 1: Create an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/26351.html).
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can call this operation to create an ApsaraDB for Redis instance or a classic Tair DRAM-based instance. To create a cloud-native Tair instance, call the [CreateTairInstance](https://help.aliyun.com/document_detail/208271.html) operation.
        > For more information about how to create an instance that meets your requirements in the ApsaraDB for Redis console, see [Step 1: Create an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/26351.html).
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        """
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        >  You can call this operation to create an ApsaraDB for Redis classic instance or a Tair DRAM-based classic instance. We recommend that you use an API operation for creating a single instance:
        [CreateInstance](https://help.aliyun.com/document_detail/473757.html): creates an ApsaraDB for Redis instance or a Tair DRAM-based classic instance.
        [CreateTairInstance](https://help.aliyun.com/document_detail/473770.html): creates a Tair cloud-native instance. The instance can be a DRAM-based, persistent memory-optimized, or ESSD/SSD-based instance.
        
        @param request: CreateInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rebuild_instance):
            query['RebuildInstance'] = request.rebuild_instance
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        """
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        >  You can call this operation to create an ApsaraDB for Redis classic instance or a Tair DRAM-based classic instance. We recommend that you use an API operation for creating a single instance:
        [CreateInstance](https://help.aliyun.com/document_detail/473757.html): creates an ApsaraDB for Redis instance or a Tair DRAM-based classic instance.
        [CreateTairInstance](https://help.aliyun.com/document_detail/473770.html): creates a Tair cloud-native instance. The instance can be a DRAM-based, persistent memory-optimized, or ESSD/SSD-based instance.
        
        @param request: CreateInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rebuild_instance):
            query['RebuildInstance'] = request.rebuild_instance
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instances(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        """
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        >  You can call this operation to create an ApsaraDB for Redis classic instance or a Tair DRAM-based classic instance. We recommend that you use an API operation for creating a single instance:
        [CreateInstance](https://help.aliyun.com/document_detail/473757.html): creates an ApsaraDB for Redis instance or a Tair DRAM-based classic instance.
        [CreateTairInstance](https://help.aliyun.com/document_detail/473770.html): creates a Tair cloud-native instance. The instance can be a DRAM-based, persistent memory-optimized, or ESSD/SSD-based instance.
        
        @param request: CreateInstancesRequest
        @return: CreateInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        """
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        >  You can call this operation to create an ApsaraDB for Redis classic instance or a Tair DRAM-based classic instance. We recommend that you use an API operation for creating a single instance:
        [CreateInstance](https://help.aliyun.com/document_detail/473757.html): creates an ApsaraDB for Redis instance or a Tair DRAM-based classic instance.
        [CreateTairInstance](https://help.aliyun.com/document_detail/473770.html): creates a Tair cloud-native instance. The instance can be a DRAM-based, persistent memory-optimized, or ESSD/SSD-based instance.
        
        @param request: CreateInstancesRequest
        @return: CreateInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_parameter_group_with_options(
        self,
        request: r_kvstore_20150101_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateParameterGroupResponse:
        """
        @summary 创建实例参数模板。
        
        @param request: CreateParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='CreateParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateParameterGroupResponse:
        """
        @summary 创建实例参数模板。
        
        @param request: CreateParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='CreateParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter_group(
        self,
        request: r_kvstore_20150101_models.CreateParameterGroupRequest,
    ) -> r_kvstore_20150101_models.CreateParameterGroupResponse:
        """
        @summary 创建实例参数模板。
        
        @param request: CreateParameterGroupRequest
        @return: CreateParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    async def create_parameter_group_async(
        self,
        request: r_kvstore_20150101_models.CreateParameterGroupRequest,
    ) -> r_kvstore_20150101_models.CreateParameterGroupResponse:
        """
        @summary 创建实例参数模板。
        
        @param request: CreateParameterGroupRequest
        @return: CreateParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_group_with_options_async(request, runtime)

    def create_tair_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        """
        @summary Creates a Tair instance.
        
        @description For information about instance selection, see [Select an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/223808.html).
        Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        For information about how to create a Tair instance in the Tair console, see [Create a Tair instance](https://help.aliyun.com/document_detail/443863.html).
        If you want to create other types of instances, such as Community Edition instances or [Tair DRAM-based](https://help.aliyun.com/document_detail/126164.html) instances, you can call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation.
        
        @param request: CreateTairInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTairInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_backup_id):
            query['ClusterBackupId'] = request.cluster_backup_id
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param_group_id):
            query['ParamGroupId'] = request.param_group_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.recover_config_mode):
            query['RecoverConfigMode'] = request.recover_config_mode
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
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.shard_type):
            query['ShardType'] = request.shard_type
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTairInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tair_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        """
        @summary Creates a Tair instance.
        
        @description For information about instance selection, see [Select an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/223808.html).
        Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        For information about how to create a Tair instance in the Tair console, see [Create a Tair instance](https://help.aliyun.com/document_detail/443863.html).
        If you want to create other types of instances, such as Community Edition instances or [Tair DRAM-based](https://help.aliyun.com/document_detail/126164.html) instances, you can call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation.
        
        @param request: CreateTairInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTairInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_backup_id):
            query['ClusterBackupId'] = request.cluster_backup_id
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.param_group_id):
            query['ParamGroupId'] = request.param_group_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.recover_config_mode):
            query['RecoverConfigMode'] = request.recover_config_mode
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
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.shard_type):
            query['ShardType'] = request.shard_type
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTairInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tair_instance(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        """
        @summary Creates a Tair instance.
        
        @description For information about instance selection, see [Select an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/223808.html).
        Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        For information about how to create a Tair instance in the Tair console, see [Create a Tair instance](https://help.aliyun.com/document_detail/443863.html).
        If you want to create other types of instances, such as Community Edition instances or [Tair DRAM-based](https://help.aliyun.com/document_detail/126164.html) instances, you can call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation.
        
        @param request: CreateTairInstanceRequest
        @return: CreateTairInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tair_instance_with_options(request, runtime)

    async def create_tair_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        """
        @summary Creates a Tair instance.
        
        @description For information about instance selection, see [Select an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/223808.html).
        Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        For information about how to create a Tair instance in the Tair console, see [Create a Tair instance](https://help.aliyun.com/document_detail/443863.html).
        If you want to create other types of instances, such as Community Edition instances or [Tair DRAM-based](https://help.aliyun.com/document_detail/126164.html) instances, you can call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation.
        
        @param request: CreateTairInstanceRequest
        @return: CreateTairInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tair_instance_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        """
        @summary Deletes an account from an ApsaraDB for Redis instance.
        
        @description    This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0.
        The ApsaraDB for Redis instance must be in the Running state.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        """
        @summary Deletes an account from an ApsaraDB for Redis instance.
        
        @description    This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0.
        The ApsaraDB for Redis instance must be in the Running state.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        """
        @summary Deletes an account from an ApsaraDB for Redis instance.
        
        @description    This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0.
        The ApsaraDB for Redis instance must be in the Running state.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        """
        @summary Deletes an account from an ApsaraDB for Redis instance.
        
        @description    This operation is supported only for ApsaraDB for Redis instances that run Redis 4.0.
        The ApsaraDB for Redis instance must be in the Running state.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_global_security_ipgroup_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @description Before you delete an IP whitelist template, you must unbind (disassociate) the instances that are currently associated with the template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='DeleteGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_security_ipgroup_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @description Before you delete an IP whitelist template, you must unbind (disassociate) the instances that are currently associated with the template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='DeleteGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_security_ipgroup(
        self,
        request: r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @description Before you delete an IP whitelist template, you must unbind (disassociate) the instances that are currently associated with the template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_security_ipgroup_with_options(request, runtime)

    async def delete_global_security_ipgroup_async(
        self,
        request: r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @description Before you delete an IP whitelist template, you must unbind (disassociate) the instances that are currently associated with the template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_security_ipgroup_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        """
        @summary Release the Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Release an instance](https://help.aliyun.com/document_detail/43882.html).
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is charged on a pay-as-you-go basis.
        >  You cannot call this operation to release a subscription instance, which is automatically released when it expires. To release a subscription instance before it expires, submit a ticket.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DeleteInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        """
        @summary Release the Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Release an instance](https://help.aliyun.com/document_detail/43882.html).
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is charged on a pay-as-you-go basis.
        >  You cannot call this operation to release a subscription instance, which is automatically released when it expires. To release a subscription instance before it expires, submit a ticket.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DeleteInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        """
        @summary Release the Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Release an instance](https://help.aliyun.com/document_detail/43882.html).
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is charged on a pay-as-you-go basis.
        >  You cannot call this operation to release a subscription instance, which is automatically released when it expires. To release a subscription instance before it expires, submit a ticket.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        """
        @summary Release the Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Release an instance](https://help.aliyun.com/document_detail/43882.html).
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is charged on a pay-as-you-go basis.
        >  You cannot call this operation to release a subscription instance, which is automatically released when it expires. To release a subscription instance before it expires, submit a ticket.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_parameter_group_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template.
        
        @param request: DeleteParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
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
            action='DeleteParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template.
        
        @param request: DeleteParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
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
            action='DeleteParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter_group(
        self,
        request: r_kvstore_20150101_models.DeleteParameterGroupRequest,
    ) -> r_kvstore_20150101_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template.
        
        @param request: DeleteParameterGroupRequest
        @return: DeleteParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    async def delete_parameter_group_async(
        self,
        request: r_kvstore_20150101_models.DeleteParameterGroupRequest,
    ) -> r_kvstore_20150101_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template.
        
        @param request: DeleteParameterGroupRequest
        @return: DeleteParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_group_with_options_async(request, runtime)

    def delete_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        """
        @summary Removes one or more data shards from an ApsaraDB for Redis cluster instance.
        
        @description You can also remove data shards from an instance in the ApsaraDB for Redis console. For more information, see [Adjust the number of shards for an ApsaraDB for Redis instance with cloud disks](https://help.aliyun.com/document_detail/198082.html).\\
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a persistent memory-optimized instance in the cluster architecture. For more information about persistent memory-optimized instances, see [Persistent memory-optimized instances](https://help.aliyun.com/document_detail/183956.html).
        The instance has more than one data shard.
        
        @param request: DeleteShardingNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShardingNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        """
        @summary Removes one or more data shards from an ApsaraDB for Redis cluster instance.
        
        @description You can also remove data shards from an instance in the ApsaraDB for Redis console. For more information, see [Adjust the number of shards for an ApsaraDB for Redis instance with cloud disks](https://help.aliyun.com/document_detail/198082.html).\\
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a persistent memory-optimized instance in the cluster architecture. For more information about persistent memory-optimized instances, see [Persistent memory-optimized instances](https://help.aliyun.com/document_detail/183956.html).
        The instance has more than one data shard.
        
        @param request: DeleteShardingNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShardingNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sharding_node(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        """
        @summary Removes one or more data shards from an ApsaraDB for Redis cluster instance.
        
        @description You can also remove data shards from an instance in the ApsaraDB for Redis console. For more information, see [Adjust the number of shards for an ApsaraDB for Redis instance with cloud disks](https://help.aliyun.com/document_detail/198082.html).\\
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a persistent memory-optimized instance in the cluster architecture. For more information about persistent memory-optimized instances, see [Persistent memory-optimized instances](https://help.aliyun.com/document_detail/183956.html).
        The instance has more than one data shard.
        
        @param request: DeleteShardingNodeRequest
        @return: DeleteShardingNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sharding_node_with_options(request, runtime)

    async def delete_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        """
        @summary Removes one or more data shards from an ApsaraDB for Redis cluster instance.
        
        @description You can also remove data shards from an instance in the ApsaraDB for Redis console. For more information, see [Adjust the number of shards for an ApsaraDB for Redis instance with cloud disks](https://help.aliyun.com/document_detail/198082.html).\\
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a persistent memory-optimized instance in the cluster architecture. For more information about persistent memory-optimized instances, see [Persistent memory-optimized instances](https://help.aliyun.com/document_detail/183956.html).
        The instance has more than one data shard.
        
        @param request: DeleteShardingNodeRequest
        @return: DeleteShardingNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sharding_node_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        """
        @summary Queries all accounts or a specified account of an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeAccounts',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        """
        @summary Queries all accounts or a specified account of an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeAccounts',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        """
        @summary Queries all accounts or a specified account of an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        """
        @summary Queries all accounts or a specified account of an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        """
        @summary Queries the detailed information about O&M tasks of an ApsaraDB for Redis instance.
        
        @description After you have called this API operation and queried the information about a specific O&M task, you can also call the [ModifyActiveOperationTask](~~ModifyActiveOperationTask~~) operation to modify the scheduled switchover time of the O&M task.
        
        @param request: DescribeActiveOperationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        """
        @summary Queries the detailed information about O&M tasks of an ApsaraDB for Redis instance.
        
        @description After you have called this API operation and queried the information about a specific O&M task, you can also call the [ModifyActiveOperationTask](~~ModifyActiveOperationTask~~) operation to modify the scheduled switchover time of the O&M task.
        
        @param request: DescribeActiveOperationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        """
        @summary Queries the detailed information about O&M tasks of an ApsaraDB for Redis instance.
        
        @description After you have called this API operation and queried the information about a specific O&M task, you can also call the [ModifyActiveOperationTask](~~ModifyActiveOperationTask~~) operation to modify the scheduled switchover time of the O&M task.
        
        @param request: DescribeActiveOperationTaskRequest
        @return: DescribeActiveOperationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_with_options(request, runtime)

    async def describe_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        """
        @summary Queries the detailed information about O&M tasks of an ApsaraDB for Redis instance.
        
        @description After you have called this API operation and queried the information about a specific O&M task, you can also call the [ModifyActiveOperationTask](~~ModifyActiveOperationTask~~) operation to modify the scheduled switchover time of the O&M task.
        
        @param request: DescribeActiveOperationTaskRequest
        @return: DescribeActiveOperationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTasksResponse:
        """
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTasksResponse:
        """
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTasksResponse:
        """
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTasksResponse:
        """
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_audit_log_config_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the audit log configurations of an ApsaraDB for Redis instance. The configurations include whether the audit log feature is enabled and the retention period of audit logs.
        
        @description > You can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html) operation to enable or disable the audit log feature for an ApsaraDB for Redis instance. For more information, see [Enable the new audit log feature](https://help.aliyun.com/document_detail/102015.html).
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest minor version.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the audit log configurations of an ApsaraDB for Redis instance. The configurations include whether the audit log feature is enabled and the retention period of audit logs.
        
        @description > You can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html) operation to enable or disable the audit log feature for an ApsaraDB for Redis instance. For more information, see [Enable the new audit log feature](https://help.aliyun.com/document_detail/102015.html).
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest minor version.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_config(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the audit log configurations of an ApsaraDB for Redis instance. The configurations include whether the audit log feature is enabled and the retention period of audit logs.
        
        @description > You can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html) operation to enable or disable the audit log feature for an ApsaraDB for Redis instance. For more information, see [Enable the new audit log feature](https://help.aliyun.com/document_detail/102015.html).
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest minor version.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditLogConfigRequest
        @return: DescribeAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    async def describe_audit_log_config_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        """
        @summary Queries the audit log configurations of an ApsaraDB for Redis instance. The configurations include whether the audit log feature is enabled and the retention period of audit logs.
        
        @description > You can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html) operation to enable or disable the audit log feature for an ApsaraDB for Redis instance. For more information, see [Enable the new audit log feature](https://help.aliyun.com/document_detail/102015.html).
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest minor version.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditLogConfigRequest
        @return: DescribeAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_config_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for Redis instance.
        
        @description This operation can be called up to 100 times per minute. You can also query audit logs in the ApsaraDB for Redis console. For more information, see [Query audit logs of an instance](https://help.aliyun.com/document_detail/101937.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or an ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance.
        The engine version of the instance is Redis 4.0 or later.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for Redis instance.
        
        @description This operation can be called up to 100 times per minute. You can also query audit logs in the ApsaraDB for Redis console. For more information, see [Query audit logs of an instance](https://help.aliyun.com/document_detail/101937.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or an ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance.
        The engine version of the instance is Redis 4.0 or later.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_records(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for Redis instance.
        
        @description This operation can be called up to 100 times per minute. You can also query audit logs in the ApsaraDB for Redis console. For more information, see [Query audit logs of an instance](https://help.aliyun.com/document_detail/101937.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or an ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance.
        The engine version of the instance is Redis 4.0 or later.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditRecordsRequest
        @return: DescribeAuditRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for Redis instance.
        
        @description This operation can be called up to 100 times per minute. You can also query audit logs in the ApsaraDB for Redis console. For more information, see [Query audit logs of an instance](https://help.aliyun.com/document_detail/101937.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or an ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance.
        The engine version of the instance is Redis 4.0 or later.
        The audit log feature is enabled for the instance. For more information, see [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/130206.html).
        
        @param request: DescribeAuditRecordsRequest
        @return: DescribeAuditRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the types of ApsaraDB for Redis instances that can be created in a specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_scene):
            query['InstanceScene'] = request.instance_scene
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the types of ApsaraDB for Redis instances that can be created in a specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_scene):
            query['InstanceScene'] = request.instance_scene
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the types of ApsaraDB for Redis instances that can be created in a specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the types of ApsaraDB for Redis instances that can be created in a specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for Redis instance, including the backup cycle and backup time.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for Redis instance, including the backup cycle and backup time.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for Redis instance, including the backup cycle and backup time.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for Redis instance, including the backup cycle and backup time.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        """
        @summary Queries the states of backup tasks for an ApsaraDB for Redis instance.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_mode):
            query['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeBackupTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        """
        @summary Queries the states of backup tasks for an ApsaraDB for Redis instance.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_mode):
            query['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeBackupTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        """
        @summary Queries the states of backup tasks for an ApsaraDB for Redis instance.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        """
        @summary Queries the states of backup tasks for an ApsaraDB for Redis instance.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        """
        @summary Queries the backup files of the ApsaraDB for Redis instance.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_aof):
            query['NeedAof'] = request.need_aof
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        """
        @summary Queries the backup files of the ApsaraDB for Redis instance.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_aof):
            query['NeedAof'] = request.need_aof
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        """
        @summary Queries the backup files of the ApsaraDB for Redis instance.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        """
        @summary Queries the backup files of the ApsaraDB for Redis instance.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cache_analysis_report_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        """
        @summary Queries the cache analytics report that is generated on a specified date for an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['AnalysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeCacheAnalysisReport',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_report_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        """
        @summary Queries the cache analytics report that is generated on a specified date for an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['AnalysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeCacheAnalysisReport',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_report(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        """
        @summary Queries the cache analytics report that is generated on a specified date for an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportRequest
        @return: DescribeCacheAnalysisReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_with_options(request, runtime)

    async def describe_cache_analysis_report_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        """
        @summary Queries the cache analytics report that is generated on a specified date for an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportRequest
        @return: DescribeCacheAnalysisReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_with_options_async(request, runtime)

    def describe_cache_analysis_report_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        """
        @summary Queries the cache analytics reports of an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeCacheAnalysisReportList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_report_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        """
        @summary Queries the cache analytics reports of an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeCacheAnalysisReportList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_report_list(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        """
        @summary Queries the cache analytics reports of an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportListRequest
        @return: DescribeCacheAnalysisReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_list_with_options(request, runtime)

    async def describe_cache_analysis_report_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        """
        @summary Queries the cache analytics reports of an ApsaraDB for Redis instance.
        
        @description > ApsaraDB for Redis has optimized the cache analytics feature to improve user experience. This API operation is phased out. You can use the new API operation for cache analytics. For more information, see [API operations for cache analytics are upgraded](https://help.aliyun.com/document_detail/186019.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The engine version of the instance is Redis 4.0 or later.
        The instance uses the latest minor version. For more information about how to check whether to update the minor version of an instance, see [How do I check whether the minor version of an ApsaraDB for Redis instance is the latest?](https://help.aliyun.com/document_detail/129203.html)
        
        @param request: DescribeCacheAnalysisReportListRequest
        @return: DescribeCacheAnalysisReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_list_with_options_async(request, runtime)

    def describe_cluster_backup_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeClusterBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterBackupListResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for Redis or Tair cluster instance.
        
        @param request: DescribeClusterBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterBackupListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterBackupList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_backup_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterBackupListResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for Redis or Tair cluster instance.
        
        @param request: DescribeClusterBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterBackupListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterBackupList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_backup_list(
        self,
        request: r_kvstore_20150101_models.DescribeClusterBackupListRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterBackupListResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for Redis or Tair cluster instance.
        
        @param request: DescribeClusterBackupListRequest
        @return: DescribeClusterBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_backup_list_with_options(request, runtime)

    async def describe_cluster_backup_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterBackupListRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterBackupListResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for Redis or Tair cluster instance.
        
        @param request: DescribeClusterBackupListRequest
        @return: DescribeClusterBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_backup_list_with_options_async(request, runtime)

    def describe_cluster_member_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        """
        @summary Queries the configuration information of nodes in an ApsaraDB for Redis cluster instance, such as the specifications and the maximum number of connections.
        
        @description > This API operation is applicable only to ApsaraDB for Redis instances that use [cloud disks](https://help.aliyun.com/document_detail/188068.html) and the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        
        @param request: DescribeClusterMemberInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterMemberInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterMemberInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_member_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        """
        @summary Queries the configuration information of nodes in an ApsaraDB for Redis cluster instance, such as the specifications and the maximum number of connections.
        
        @description > This API operation is applicable only to ApsaraDB for Redis instances that use [cloud disks](https://help.aliyun.com/document_detail/188068.html) and the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        
        @param request: DescribeClusterMemberInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterMemberInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterMemberInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_member_info(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        """
        @summary Queries the configuration information of nodes in an ApsaraDB for Redis cluster instance, such as the specifications and the maximum number of connections.
        
        @description > This API operation is applicable only to ApsaraDB for Redis instances that use [cloud disks](https://help.aliyun.com/document_detail/188068.html) and the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        
        @param request: DescribeClusterMemberInfoRequest
        @return: DescribeClusterMemberInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_member_info_with_options(request, runtime)

    async def describe_cluster_member_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        """
        @summary Queries the configuration information of nodes in an ApsaraDB for Redis cluster instance, such as the specifications and the maximum number of connections.
        
        @description > This API operation is applicable only to ApsaraDB for Redis instances that use [cloud disks](https://help.aliyun.com/document_detail/188068.html) and the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        
        @param request: DescribeClusterMemberInfoRequest
        @return: DescribeClusterMemberInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_member_info_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information of an ApsaraDB for Redis instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeDBInstanceNetInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information of an ApsaraDB for Redis instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeDBInstanceNetInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information of an ApsaraDB for Redis instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information of an ApsaraDB for Redis instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbnode_direct_vip_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse:
        """
        @summary Queries the information about virtual IP addresses (VIPs) of child instances of a cluster instance in direct connection mode.
        
        @description > Only instances that use cloud disks support this operation.
        
        @param request: DescribeDBNodeDirectVipInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodeDirectVipInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeDBNodeDirectVipInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbnode_direct_vip_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse:
        """
        @summary Queries the information about virtual IP addresses (VIPs) of child instances of a cluster instance in direct connection mode.
        
        @description > Only instances that use cloud disks support this operation.
        
        @param request: DescribeDBNodeDirectVipInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodeDirectVipInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeDBNodeDirectVipInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbnode_direct_vip_info(
        self,
        request: r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse:
        """
        @summary Queries the information about virtual IP addresses (VIPs) of child instances of a cluster instance in direct connection mode.
        
        @description > Only instances that use cloud disks support this operation.
        
        @param request: DescribeDBNodeDirectVipInfoRequest
        @return: DescribeDBNodeDirectVipInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_direct_vip_info_with_options(request, runtime)

    async def describe_dbnode_direct_vip_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBNodeDirectVipInfoResponse:
        """
        @summary Queries the information about virtual IP addresses (VIPs) of child instances of a cluster instance in direct connection mode.
        
        @description > Only instances that use cloud disks support this operation.
        
        @param request: DescribeDBNodeDirectVipInfoRequest
        @return: DescribeDBNodeDirectVipInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnode_direct_vip_info_with_options_async(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        """
        @summary Queries the information of an ApsaraDB for Redis instance deployed in a dedicated cluster.
        
        @description > If you want to query the information about ApsaraDB for Redis instances that are not deployed in a dedicated cluster, call the [DescribeInstanceAttribute](https://help.aliyun.com/document_detail/60996.html) operation.
        
        @param request: DescribeDedicatedClusterInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_net_type):
            query['InstanceNetType'] = request.instance_net_type
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterInstanceList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_cluster_instance_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        """
        @summary Queries the information of an ApsaraDB for Redis instance deployed in a dedicated cluster.
        
        @description > If you want to query the information about ApsaraDB for Redis instances that are not deployed in a dedicated cluster, call the [DescribeInstanceAttribute](https://help.aliyun.com/document_detail/60996.html) operation.
        
        @param request: DescribeDedicatedClusterInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedClusterInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_net_type):
            query['InstanceNetType'] = request.instance_net_type
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterInstanceList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_cluster_instance_list(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        """
        @summary Queries the information of an ApsaraDB for Redis instance deployed in a dedicated cluster.
        
        @description > If you want to query the information about ApsaraDB for Redis instances that are not deployed in a dedicated cluster, call the [DescribeInstanceAttribute](https://help.aliyun.com/document_detail/60996.html) operation.
        
        @param request: DescribeDedicatedClusterInstanceListRequest
        @return: DescribeDedicatedClusterInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    async def describe_dedicated_cluster_instance_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        """
        @summary Queries the information of an ApsaraDB for Redis instance deployed in a dedicated cluster.
        
        @description > If you want to query the information about ApsaraDB for Redis instances that are not deployed in a dedicated cluster, call the [DescribeInstanceAttribute](https://help.aliyun.com/document_detail/60996.html) operation.
        
        @param request: DescribeDedicatedClusterInstanceListRequest
        @return: DescribeDedicatedClusterInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_instance_list_with_options_async(request, runtime)

    def describe_encryption_key_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        """
        @summary Queries the details of a Transparent Data Encryption (TDE) custom key for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, TDE must be enabled for the ApsaraDB for Redis instance by using a custom key. For more information, see [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html).
        > For more information about TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEncryptionKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEncryptionKey',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_encryption_key_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        """
        @summary Queries the details of a Transparent Data Encryption (TDE) custom key for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, TDE must be enabled for the ApsaraDB for Redis instance by using a custom key. For more information, see [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html).
        > For more information about TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEncryptionKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEncryptionKey',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_encryption_key(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        """
        @summary Queries the details of a Transparent Data Encryption (TDE) custom key for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, TDE must be enabled for the ApsaraDB for Redis instance by using a custom key. For more information, see [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html).
        > For more information about TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyRequest
        @return: DescribeEncryptionKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_encryption_key_with_options(request, runtime)

    async def describe_encryption_key_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        """
        @summary Queries the details of a Transparent Data Encryption (TDE) custom key for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, TDE must be enabled for the ApsaraDB for Redis instance by using a custom key. For more information, see [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html).
        > For more information about TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyRequest
        @return: DescribeEncryptionKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_encryption_key_with_options_async(request, runtime)

    def describe_encryption_key_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        """
        @summary Queries the custom keys used by an ApsaraDB for Redis instance.
        
        @description    You can specify a custom key when you call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable Transparent Data Encryption (TDE). You can call the DescribeEncryptionKeyList operation to query the custom keys that are in use. To create a custom key, you can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation of Key Management Service (KMS).
        For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEncryptionKeyList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_encryption_key_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        """
        @summary Queries the custom keys used by an ApsaraDB for Redis instance.
        
        @description    You can specify a custom key when you call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable Transparent Data Encryption (TDE). You can call the DescribeEncryptionKeyList operation to query the custom keys that are in use. To create a custom key, you can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation of Key Management Service (KMS).
        For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEncryptionKeyList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_encryption_key_list(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        """
        @summary Queries the custom keys used by an ApsaraDB for Redis instance.
        
        @description    You can specify a custom key when you call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable Transparent Data Encryption (TDE). You can call the DescribeEncryptionKeyList operation to query the custom keys that are in use. To create a custom key, you can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation of Key Management Service (KMS).
        For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyListRequest
        @return: DescribeEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_encryption_key_list_with_options(request, runtime)

    async def describe_encryption_key_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        """
        @summary Queries the custom keys used by an ApsaraDB for Redis instance.
        
        @description    You can specify a custom key when you call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) operation to enable Transparent Data Encryption (TDE). You can call the DescribeEncryptionKeyList operation to query the custom keys that are in use. To create a custom key, you can call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation of Key Management Service (KMS).
        For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: DescribeEncryptionKeyListRequest
        @return: DescribeEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_encryption_key_list_with_options_async(request, runtime)

    def describe_engine_version_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        """
        @summary Queries the major version and minor version of an ApsaraDB for Redis instance and the release notes for minor versions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeEngineVersion\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEngineVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_engine_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        """
        @summary Queries the major version and minor version of an ApsaraDB for Redis instance and the release notes for minor versions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeEngineVersion\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeEngineVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_engine_version(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        """
        @summary Queries the major version and minor version of an ApsaraDB for Redis instance and the release notes for minor versions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeEngineVersion\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeEngineVersionRequest
        @return: DescribeEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_engine_version_with_options(request, runtime)

    async def describe_engine_version_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        """
        @summary Queries the major version and minor version of an ApsaraDB for Redis instance and the release notes for minor versions.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeEngineVersion\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeEngineVersionRequest
        @return: DescribeEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_engine_version_with_options_async(request, runtime)

    def describe_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        """
        @summary Queries the details of a distributed ApsaraDB for Redis instance.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeGlobalDistributeCache\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeGlobalDistributeCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDistributeCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sub_instance_id):
            query['SubInstanceId'] = request.sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        """
        @summary Queries the details of a distributed ApsaraDB for Redis instance.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeGlobalDistributeCache\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeGlobalDistributeCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDistributeCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sub_instance_id):
            query['SubInstanceId'] = request.sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        """
        @summary Queries the details of a distributed ApsaraDB for Redis instance.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeGlobalDistributeCache\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeGlobalDistributeCacheRequest
        @return: DescribeGlobalDistributeCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_distribute_cache_with_options(request, runtime)

    async def describe_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        """
        @summary Queries the details of a distributed ApsaraDB for Redis instance.
        
        @description ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=R-kvstore\\&api=DescribeGlobalDistributeCache\\&type=RPC\\&version=2015-01-01)
        
        @param request: DescribeGlobalDistributeCacheRequest
        @return: DescribeGlobalDistributeCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_distribute_cache_with_options_async(request, runtime)

    def describe_global_security_ipgroup_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_with_options(request, runtime)

    async def describe_global_security_ipgroup_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_with_options_async(request, runtime)

    def describe_global_security_ipgroup_relation_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries information about the global IP whitelist templates associated with an instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_relation_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries information about the global IP whitelist templates associated with an instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup_relation(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries information about the global IP whitelist templates associated with an instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_relation_with_options(request, runtime)

    async def describe_global_security_ipgroup_relation_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries information about the global IP whitelist templates associated with an instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_relation_with_options_async(request, runtime)

    def describe_history_monitor_values_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        """
        @summary Queries the performance monitoring data of an ApsaraDB for Redis instance.
        
        @description You can also query the performance monitoring data of an instance in the ApsaraDB for Redis console. For more information, see [Metrics](https://help.aliyun.com/document_detail/43887.html).
        
        @param request: DescribeHistoryMonitorValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryMonitorValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_for_history):
            query['IntervalForHistory'] = request.interval_for_history
        if not UtilClient.is_unset(request.monitor_keys):
            query['MonitorKeys'] = request.monitor_keys
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryMonitorValues',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_monitor_values_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        """
        @summary Queries the performance monitoring data of an ApsaraDB for Redis instance.
        
        @description You can also query the performance monitoring data of an instance in the ApsaraDB for Redis console. For more information, see [Metrics](https://help.aliyun.com/document_detail/43887.html).
        
        @param request: DescribeHistoryMonitorValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryMonitorValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_for_history):
            query['IntervalForHistory'] = request.interval_for_history
        if not UtilClient.is_unset(request.monitor_keys):
            query['MonitorKeys'] = request.monitor_keys
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_role):
            query['NodeRole'] = request.node_role
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryMonitorValues',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_monitor_values(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        """
        @summary Queries the performance monitoring data of an ApsaraDB for Redis instance.
        
        @description You can also query the performance monitoring data of an instance in the ApsaraDB for Redis console. For more information, see [Metrics](https://help.aliyun.com/document_detail/43887.html).
        
        @param request: DescribeHistoryMonitorValuesRequest
        @return: DescribeHistoryMonitorValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_history_monitor_values_with_options(request, runtime)

    async def describe_history_monitor_values_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        """
        @summary Queries the performance monitoring data of an ApsaraDB for Redis instance.
        
        @description You can also query the performance monitoring data of an instance in the ApsaraDB for Redis console. For more information, see [Metrics](https://help.aliyun.com/document_detail/43887.html).
        
        @param request: DescribeHistoryMonitorValuesRequest
        @return: DescribeHistoryMonitorValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_monitor_values_with_options_async(request, runtime)

    def describe_history_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @return: DescribeHistoryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_history_tasks_with_options(request, runtime)

    async def describe_history_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @return: DescribeHistoryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_tasks_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary Queries whether auto-renewal is enabled for an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary Queries whether auto-renewal is enabled for an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary Queries whether auto-renewal is enabled for an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary Queries whether auto-renewal is enabled for an ApsaraDB for Redis instance.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use cloud disks.
        > You can call the [DescribeParameters](https://help.aliyun.com/document_detail/473847.html) operation to query the parameter settings of instances that use local disks.
        
        @param request: DescribeInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use cloud disks.
        > You can call the [DescribeParameters](https://help.aliyun.com/document_detail/473847.html) operation to query the parameter settings of instances that use local disks.
        
        @param request: DescribeInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_config(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use cloud disks.
        > You can call the [DescribeParameters](https://help.aliyun.com/document_detail/473847.html) operation to query the parameter settings of instances that use local disks.
        
        @param request: DescribeInstanceConfigRequest
        @return: DescribeInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_config_with_options(request, runtime)

    async def describe_instance_config_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use cloud disks.
        > You can call the [DescribeParameters](https://help.aliyun.com/document_detail/473847.html) operation to query the parameter settings of instances that use local disks.
        
        @param request: DescribeInstanceConfigRequest
        @return: DescribeInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_config_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        """
        @summary Queries whether TLS (SSL) encryption is enabled for an instance.
        
        @description SSL encryption is supported for ApsaraDB for Redis 2.8 standard master-replica instances, ApsaraDB for Redis 2.8 master-replica cluster instances, and ApsaraDB for Redis 4.0 master-replica cluster instances. You can enable SSL encryption to enhance data transmission security.
        You can use one of the following methods to enable or disable SSL encryption or update the SSL certificate for an ApsaraDB for Redis instance:
        Call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation.
        Enable or disable SSL encryption or update the SSL certificate in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        > After SSL encryption is enabled, the instance may respond slower.
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        """
        @summary Queries whether TLS (SSL) encryption is enabled for an instance.
        
        @description SSL encryption is supported for ApsaraDB for Redis 2.8 standard master-replica instances, ApsaraDB for Redis 2.8 master-replica cluster instances, and ApsaraDB for Redis 4.0 master-replica cluster instances. You can enable SSL encryption to enhance data transmission security.
        You can use one of the following methods to enable or disable SSL encryption or update the SSL certificate for an ApsaraDB for Redis instance:
        Call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation.
        Enable or disable SSL encryption or update the SSL certificate in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        > After SSL encryption is enabled, the instance may respond slower.
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        """
        @summary Queries whether TLS (SSL) encryption is enabled for an instance.
        
        @description SSL encryption is supported for ApsaraDB for Redis 2.8 standard master-replica instances, ApsaraDB for Redis 2.8 master-replica cluster instances, and ApsaraDB for Redis 4.0 master-replica cluster instances. You can enable SSL encryption to enhance data transmission security.
        You can use one of the following methods to enable or disable SSL encryption or update the SSL certificate for an ApsaraDB for Redis instance:
        Call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation.
        Enable or disable SSL encryption or update the SSL certificate in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        > After SSL encryption is enabled, the instance may respond slower.
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        """
        @summary Queries whether TLS (SSL) encryption is enabled for an instance.
        
        @description SSL encryption is supported for ApsaraDB for Redis 2.8 standard master-replica instances, ApsaraDB for Redis 2.8 master-replica cluster instances, and ApsaraDB for Redis 4.0 master-replica cluster instances. You can enable SSL encryption to enhance data transmission security.
        You can use one of the following methods to enable or disable SSL encryption or update the SSL certificate for an ApsaraDB for Redis instance:
        Call the [ModifyInstanceSSL](https://help.aliyun.com/document_detail/96194.html) operation.
        Enable or disable SSL encryption or update the SSL certificate in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        > After SSL encryption is enabled, the instance may respond slower.
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_tdestatus_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        """
        @summary Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for Redis instance.
        
        @description For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        >  You can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) to enable or disable TDE.
        
        @param request: DescribeInstanceTDEStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTDEStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceTDEStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_tdestatus_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        """
        @summary Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for Redis instance.
        
        @description For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        >  You can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) to enable or disable TDE.
        
        @param request: DescribeInstanceTDEStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTDEStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeInstanceTDEStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_tdestatus(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        """
        @summary Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for Redis instance.
        
        @description For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        >  You can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) to enable or disable TDE.
        
        @param request: DescribeInstanceTDEStatusRequest
        @return: DescribeInstanceTDEStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tdestatus_with_options(request, runtime)

    async def describe_instance_tdestatus_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        """
        @summary Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for Redis instance.
        
        @description For more information about TDE and the usage notes of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        >  You can call the [ModifyInstanceTDE](https://help.aliyun.com/document_detail/302337.html) to enable or disable TDE.
        
        @param request: DescribeInstanceTDEStatusRequest
        @return: DescribeInstanceTDEStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tdestatus_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        """
        @summary Queries the information about one or more ApsaraDB for Redis instances.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        """
        @summary Queries the information about one or more ApsaraDB for Redis instances.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        """
        @summary Queries the information about one or more ApsaraDB for Redis instances.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        """
        @summary Queries the information about one or more ApsaraDB for Redis instances.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instances_overview_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for Redis instances.
        
        @description If you do not specify the InstanceIds parameter when you call this operation, the overview information of all instances is returned.
        > This operation returns non-paged results.
        
        @param request: DescribeInstancesOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancesOverview',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_overview_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for Redis instances.
        
        @description If you do not specify the InstanceIds parameter when you call this operation, the overview information of all instances is returned.
        > This operation returns non-paged results.
        
        @param request: DescribeInstancesOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancesOverview',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances_overview(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for Redis instances.
        
        @description If you do not specify the InstanceIds parameter when you call this operation, the overview information of all instances is returned.
        > This operation returns non-paged results.
        
        @param request: DescribeInstancesOverviewRequest
        @return: DescribeInstancesOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_overview_with_options(request, runtime)

    async def describe_instances_overview_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for Redis instances.
        
        @description If you do not specify the InstanceIds parameter when you call this operation, the overview information of all instances is returned.
        > This operation returns non-paged results.
        
        @param request: DescribeInstancesOverviewRequest
        @return: DescribeInstancesOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_overview_with_options_async(request, runtime)

    def describe_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        """
        @summary Queries the internal bandwidth of an ApsaraDB for Redis instance. If you have purchased extra internal bandwidth, the expiration time of the purchased bandwidth is also returned.
        
        @description You can call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to increase the internal bandwidth of an instance.
        
        @param request: DescribeIntranetAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntranetAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        """
        @summary Queries the internal bandwidth of an ApsaraDB for Redis instance. If you have purchased extra internal bandwidth, the expiration time of the purchased bandwidth is also returned.
        
        @description You can call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to increase the internal bandwidth of an instance.
        
        @param request: DescribeIntranetAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntranetAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        """
        @summary Queries the internal bandwidth of an ApsaraDB for Redis instance. If you have purchased extra internal bandwidth, the expiration time of the purchased bandwidth is also returned.
        
        @description You can call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to increase the internal bandwidth of an instance.
        
        @param request: DescribeIntranetAttributeRequest
        @return: DescribeIntranetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_intranet_attribute_with_options(request, runtime)

    async def describe_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        """
        @summary Queries the internal bandwidth of an ApsaraDB for Redis instance. If you have purchased extra internal bandwidth, the expiration time of the purchased bandwidth is also returned.
        
        @description You can call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to increase the internal bandwidth of an instance.
        
        @param request: DescribeIntranetAttributeRequest
        @return: DescribeIntranetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_intranet_attribute_with_options_async(request, runtime)

    def describe_logic_instance_topology_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        """
        @summary Queries the logical topology of an ApsaraDB for Redis instance.
        
        @description This parameter is supported only for cluster and read/write splitting instances.
        
        @param request: DescribeLogicInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogicInstanceTopologyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeLogicInstanceTopology',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_logic_instance_topology_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        """
        @summary Queries the logical topology of an ApsaraDB for Redis instance.
        
        @description This parameter is supported only for cluster and read/write splitting instances.
        
        @param request: DescribeLogicInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogicInstanceTopologyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeLogicInstanceTopology',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_logic_instance_topology(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        """
        @summary Queries the logical topology of an ApsaraDB for Redis instance.
        
        @description This parameter is supported only for cluster and read/write splitting instances.
        
        @param request: DescribeLogicInstanceTopologyRequest
        @return: DescribeLogicInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_logic_instance_topology_with_options(request, runtime)

    async def describe_logic_instance_topology_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        """
        @summary Queries the logical topology of an ApsaraDB for Redis instance.
        
        @description This parameter is supported only for cluster and read/write splitting instances.
        
        @param request: DescribeLogicInstanceTopologyRequest
        @return: DescribeLogicInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_logic_instance_topology_with_options_async(request, runtime)

    def describe_monitor_items_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        """
        @summary Queries the metrics of an ApsaraDB for Redis instance.
        
        @description >  ApsaraDB for Redis has upgraded the monitoring metrics. The DescribeMonitorItems operation is phased out. For more information, see [The DescribeMonitorItems operation supported by ApsaraDB for Redis is phased out](https://help.aliyun.com/document_detail/189893.html).
        After you call this operation to retrieve a list of metrics for a specified ApsaraDB for Redis instance, you can call the [DescribeHistoryMonitorValues](~~DescribeHistoryMonitorValues~~) operation to query monitoring history of the instance.
        
        @param request: DescribeMonitorItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeMonitorItems',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_items_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        """
        @summary Queries the metrics of an ApsaraDB for Redis instance.
        
        @description >  ApsaraDB for Redis has upgraded the monitoring metrics. The DescribeMonitorItems operation is phased out. For more information, see [The DescribeMonitorItems operation supported by ApsaraDB for Redis is phased out](https://help.aliyun.com/document_detail/189893.html).
        After you call this operation to retrieve a list of metrics for a specified ApsaraDB for Redis instance, you can call the [DescribeHistoryMonitorValues](~~DescribeHistoryMonitorValues~~) operation to query monitoring history of the instance.
        
        @param request: DescribeMonitorItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeMonitorItems',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_items(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        """
        @summary Queries the metrics of an ApsaraDB for Redis instance.
        
        @description >  ApsaraDB for Redis has upgraded the monitoring metrics. The DescribeMonitorItems operation is phased out. For more information, see [The DescribeMonitorItems operation supported by ApsaraDB for Redis is phased out](https://help.aliyun.com/document_detail/189893.html).
        After you call this operation to retrieve a list of metrics for a specified ApsaraDB for Redis instance, you can call the [DescribeHistoryMonitorValues](~~DescribeHistoryMonitorValues~~) operation to query monitoring history of the instance.
        
        @param request: DescribeMonitorItemsRequest
        @return: DescribeMonitorItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_items_with_options(request, runtime)

    async def describe_monitor_items_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        """
        @summary Queries the metrics of an ApsaraDB for Redis instance.
        
        @description >  ApsaraDB for Redis has upgraded the monitoring metrics. The DescribeMonitorItems operation is phased out. For more information, see [The DescribeMonitorItems operation supported by ApsaraDB for Redis is phased out](https://help.aliyun.com/document_detail/189893.html).
        After you call this operation to retrieve a list of metrics for a specified ApsaraDB for Redis instance, you can call the [DescribeHistoryMonitorValues](~~DescribeHistoryMonitorValues~~) operation to query monitoring history of the instance.
        
        @param request: DescribeMonitorItemsRequest
        @return: DescribeMonitorItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_items_with_options_async(request, runtime)

    def describe_parameter_group_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupResponse:
        """
        @summary Queries the basic information about a parameter template.
        
        @param request: DescribeParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
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
            action='DescribeParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupResponse:
        """
        @summary Queries the basic information about a parameter template.
        
        @param request: DescribeParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
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
            action='DescribeParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_group(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupResponse:
        """
        @summary Queries the basic information about a parameter template.
        
        @param request: DescribeParameterGroupRequest
        @return: DescribeParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    async def describe_parameter_group_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupResponse:
        """
        @summary Queries the basic information about a parameter template.
        
        @param request: DescribeParameterGroupRequest
        @return: DescribeParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_with_options_async(request, runtime)

    def describe_parameter_group_support_param_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupSupportParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse:
        """
        @summary Queries the parameters that can be configured in parameter templates across different database versions.
        
        @param request: DescribeParameterGroupSupportParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupSupportParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeParameterGroupSupportParam',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_group_support_param_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupSupportParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse:
        """
        @summary Queries the parameters that can be configured in parameter templates across different database versions.
        
        @param request: DescribeParameterGroupSupportParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupSupportParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeParameterGroupSupportParam',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_group_support_param(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupSupportParamRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse:
        """
        @summary Queries the parameters that can be configured in parameter templates across different database versions.
        
        @param request: DescribeParameterGroupSupportParamRequest
        @return: DescribeParameterGroupSupportParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_support_param_with_options(request, runtime)

    async def describe_parameter_group_support_param_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupSupportParamRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupSupportParamResponse:
        """
        @summary Queries the parameters that can be configured in parameter templates across different database versions.
        
        @param request: DescribeParameterGroupSupportParamRequest
        @return: DescribeParameterGroupSupportParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_support_param_with_options_async(request, runtime)

    def describe_parameter_group_template_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse:
        """
        @summary 查询参数模板支持设置的参数列表
        
        @param request: DescribeParameterGroupTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroupTemplateList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_group_template_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse:
        """
        @summary 查询参数模板支持设置的参数列表
        
        @param request: DescribeParameterGroupTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroupTemplateList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_group_template_list(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupTemplateListRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse:
        """
        @summary 查询参数模板支持设置的参数列表
        
        @param request: DescribeParameterGroupTemplateListRequest
        @return: DescribeParameterGroupTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_template_list_with_options(request, runtime)

    async def describe_parameter_group_template_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupTemplateListRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupTemplateListResponse:
        """
        @summary 查询参数模板支持设置的参数列表
        
        @param request: DescribeParameterGroupTemplateListRequest
        @return: DescribeParameterGroupTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_template_list_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupsResponse:
        """
        @summary Queries a list of available parameter templates.
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
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
            action='DescribeParameterGroups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupsResponse:
        """
        @summary Queries a list of available parameter templates.
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
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
            action='DescribeParameterGroups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupsRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupsResponse:
        """
        @summary Queries a list of available parameter templates.
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterGroupsRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterGroupsResponse:
        """
        @summary Queries a list of available parameter templates.
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameter_modification_history_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification history of a Tair or ApsaraDB for Redis instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterModificationHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_name):
            query['ParameterName'] = request.parameter_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_modification_history_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification history of a Tair or ApsaraDB for Redis instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterModificationHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_name):
            query['ParameterName'] = request.parameter_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_modification_history(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification history of a Tair or ApsaraDB for Redis instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @return: DescribeParameterModificationHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    async def describe_parameter_modification_history_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification history of a Tair or ApsaraDB for Redis instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @return: DescribeParameterModificationHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_modification_history_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the parameters and their default values that are supported by ApsaraDB for Redis instances of different architectures and major versions.
        
        @description After you call this operation to query the parameters and default values of an instance, you can call the [ModifyInstanceConfig](https://help.aliyun.com/document_detail/61113.html) operation to reconfigure the parameters of the instance.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the parameters and their default values that are supported by ApsaraDB for Redis instances of different architectures and major versions.
        
        @description After you call this operation to query the parameters and default values of an instance, you can call the [ModifyInstanceConfig](https://help.aliyun.com/document_detail/61113.html) operation to reconfigure the parameters of the instance.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the parameters and their default values that are supported by ApsaraDB for Redis instances of different architectures and major versions.
        
        @description After you call this operation to query the parameters and default values of an instance, you can call the [ModifyInstanceConfig](https://help.aliyun.com/document_detail/61113.html) operation to reconfigure the parameters of the instance.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the parameters and their default values that are supported by ApsaraDB for Redis instances of different architectures and major versions.
        
        @description After you call this operation to query the parameters and default values of an instance, you can call the [ModifyInstanceConfig](https://help.aliyun.com/document_detail/61113.html) operation to reconfigure the parameters of the instance.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        """
        @summary Queries the configuration parameters and running parameters of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use local disks.
        > You can call the [DescribeInstanceConfig](https://help.aliyun.com/document_detail/473846.html) operation to query the parameter settings of instances that use cloud disks.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
            action='DescribeParameters',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        """
        @summary Queries the configuration parameters and running parameters of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use local disks.
        > You can call the [DescribeInstanceConfig](https://help.aliyun.com/document_detail/473846.html) operation to query the parameter settings of instances that use cloud disks.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
            action='DescribeParameters',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        """
        @summary Queries the configuration parameters and running parameters of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use local disks.
        > You can call the [DescribeInstanceConfig](https://help.aliyun.com/document_detail/473846.html) operation to query the parameter settings of instances that use cloud disks.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        """
        @summary Queries the configuration parameters and running parameters of an ApsaraDB for Redis instance.
        
        @description This operation is available only for instances that use local disks.
        > You can call the [DescribeInstanceConfig](https://help.aliyun.com/document_detail/473846.html) operation to query the parameter settings of instances that use cloud disks.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        """
        @summary Queries the fees that you must pay when you create, upgrade, or renew an ApsaraDB for Redis instance.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        """
        @summary Queries the fees that you must pay when you create, upgrade, or renew an ApsaraDB for Redis instance.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        """
        @summary Queries the fees that you must pay when you create, upgrade, or renew an ApsaraDB for Redis instance.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        """
        @summary Queries the fees that you must pay when you create, upgrade, or renew an ApsaraDB for Redis instance.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which ApsaraDB for Redis instances can be created.
        
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
            action='DescribeRegions',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which ApsaraDB for Redis instances can be created.
        
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
            action='DescribeRegions',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which ApsaraDB for Redis instances can be created.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which ApsaraDB for Redis instances can be created.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role, type, minor version, and zone of each node in an ApsaraDB for Redis instance.
        
        @param request: DescribeRoleZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoleZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
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
            action='DescribeRoleZoneInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role, type, minor version, and zone of each node in an ApsaraDB for Redis instance.
        
        @param request: DescribeRoleZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoleZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
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
            action='DescribeRoleZoneInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role, type, minor version, and zone of each node in an ApsaraDB for Redis instance.
        
        @param request: DescribeRoleZoneInfoRequest
        @return: DescribeRoleZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role, type, minor version, and zone of each node in an ApsaraDB for Redis instance.
        
        @param request: DescribeRoleZoneInfoRequest
        @return: DescribeRoleZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries the active logs of an ApsaraDB for Redis instance.
        
        @description For more information about how to view the operational logs of an instance in the ApsaraDB for Redis console, see [View active logs](https://help.aliyun.com/document_detail/101713.html).
        This operation can be called up to 100 times per minute.
        
        @param request: DescribeRunningLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries the active logs of an ApsaraDB for Redis instance.
        
        @description For more information about how to view the operational logs of an instance in the ApsaraDB for Redis console, see [View active logs](https://help.aliyun.com/document_detail/101713.html).
        This operation can be called up to 100 times per minute.
        
        @param request: DescribeRunningLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_running_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries the active logs of an ApsaraDB for Redis instance.
        
        @description For more information about how to view the operational logs of an instance in the ApsaraDB for Redis console, see [View active logs](https://help.aliyun.com/document_detail/101713.html).
        This operation can be called up to 100 times per minute.
        
        @param request: DescribeRunningLogRecordsRequest
        @return: DescribeRunningLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries the active logs of an ApsaraDB for Redis instance.
        
        @description For more information about how to view the operational logs of an instance in the ApsaraDB for Redis console, see [View active logs](https://help.aliyun.com/document_detail/101713.html).
        This operation can be called up to 100 times per minute.
        
        @param request: DescribeRunningLogRecordsRequest
        @return: DescribeRunningLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary Queries the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeSecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary Queries the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeSecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary Queries the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @return: DescribeSecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary Queries the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @return: DescribeSecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        """
        @summary Queries the IP address whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeSecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        """
        @summary Queries the IP address whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeSecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ips(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        """
        @summary Queries the IP address whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        """
        @summary Queries the IP address whitelists of an ApsaraDB for Redis instance.
        
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the slow logs of an ApsaraDB for Redis instance that are generated within a specified period of time.
        
        @description You can also query slow logs in the ApsaraDB for Redis console. For more information, see [Query slow logs of an instance](https://help.aliyun.com/document_detail/95874.html). This operation can be called up to 100 times per minute.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.slow_log_record_type):
            query['SlowLogRecordType'] = request.slow_log_record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the slow logs of an ApsaraDB for Redis instance that are generated within a specified period of time.
        
        @description You can also query slow logs in the ApsaraDB for Redis console. For more information, see [Query slow logs of an instance](https://help.aliyun.com/document_detail/95874.html). This operation can be called up to 100 times per minute.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.slow_log_record_type):
            query['SlowLogRecordType'] = request.slow_log_record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the slow logs of an ApsaraDB for Redis instance that are generated within a specified period of time.
        
        @description You can also query slow logs in the ApsaraDB for Redis console. For more information, see [Query slow logs of an instance](https://help.aliyun.com/document_detail/95874.html). This operation can be called up to 100 times per minute.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the slow logs of an ApsaraDB for Redis instance that are generated within a specified period of time.
        
        @description You can also query slow logs in the ApsaraDB for Redis console. For more information, see [Query slow logs of an instance](https://help.aliyun.com/document_detail/95874.html). This operation can be called up to 100 times per minute.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        """
        @summary Queries all tasks that are performed on an ApsaraDB for Redis instance within a specified period of time.
        
        @description You can call this operation to query the progress of a task when you perform time-consuming operations. You can also log on to the ApsaraDB for Redis console and click the Tasks icon in the upper-right corner of the *Instance Information** page to view the progress of the current task.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        """
        @summary Queries all tasks that are performed on an ApsaraDB for Redis instance within a specified period of time.
        
        @description You can call this operation to query the progress of a task when you perform time-consuming operations. You can also log on to the ApsaraDB for Redis console and click the Tasks icon in the upper-right corner of the *Instance Information** page to view the progress of the current task.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        """
        @summary Queries all tasks that are performed on an ApsaraDB for Redis instance within a specified period of time.
        
        @description You can call this operation to query the progress of a task when you perform time-consuming operations. You can also log on to the ApsaraDB for Redis console and click the Tasks icon in the upper-right corner of the *Instance Information** page to view the progress of the current task.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        """
        @summary Queries all tasks that are performed on an ApsaraDB for Redis instance within a specified period of time.
        
        @description You can call this operation to query the progress of a task when you perform time-consuming operations. You can also log on to the ApsaraDB for Redis console and click the Tasks icon in the upper-right corner of the *Instance Information** page to view the progress of the current task.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        """
        @summary Queries the zones available for ApsaraDB for Redis.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        """
        @summary Queries the zones available for ApsaraDB for Redis.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        """
        @summary Queries the zones available for ApsaraDB for Redis.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        """
        @summary Queries the zones available for ApsaraDB for Redis.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def enable_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        """
        @summary Adjusts the bandwidth of an ApsaraDB for Redis instance.
        
        @description If you enable the bandwidth auto scaling feature and call this operation at the same time, bandwidth auto scaling takes precedence. During bandwidth scale-back, the instance is scaled back to the default bandwidth of the instance type. For more information about the limits, costs, and FAQ about this feature, see [Adjust the bandwidth of an instance](https://help.aliyun.com/document_detail/102588.html).
        >  Before you call this operation, you can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/190794.html) operation to query the current bandwidth of each data node in an instance.
        
        @param request: EnableAdditionalBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAdditionalBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        """
        @summary Adjusts the bandwidth of an ApsaraDB for Redis instance.
        
        @description If you enable the bandwidth auto scaling feature and call this operation at the same time, bandwidth auto scaling takes precedence. During bandwidth scale-back, the instance is scaled back to the default bandwidth of the instance type. For more information about the limits, costs, and FAQ about this feature, see [Adjust the bandwidth of an instance](https://help.aliyun.com/document_detail/102588.html).
        >  Before you call this operation, you can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/190794.html) operation to query the current bandwidth of each data node in an instance.
        
        @param request: EnableAdditionalBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAdditionalBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        """
        @summary Adjusts the bandwidth of an ApsaraDB for Redis instance.
        
        @description If you enable the bandwidth auto scaling feature and call this operation at the same time, bandwidth auto scaling takes precedence. During bandwidth scale-back, the instance is scaled back to the default bandwidth of the instance type. For more information about the limits, costs, and FAQ about this feature, see [Adjust the bandwidth of an instance](https://help.aliyun.com/document_detail/102588.html).
        >  Before you call this operation, you can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/190794.html) operation to query the current bandwidth of each data node in an instance.
        
        @param request: EnableAdditionalBandwidthRequest
        @return: EnableAdditionalBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_additional_bandwidth_with_options(request, runtime)

    async def enable_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        """
        @summary Adjusts the bandwidth of an ApsaraDB for Redis instance.
        
        @description If you enable the bandwidth auto scaling feature and call this operation at the same time, bandwidth auto scaling takes precedence. During bandwidth scale-back, the instance is scaled back to the default bandwidth of the instance type. For more information about the limits, costs, and FAQ about this feature, see [Adjust the bandwidth of an instance](https://help.aliyun.com/document_detail/102588.html).
        >  Before you call this operation, you can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/190794.html) operation to query the current bandwidth of each data node in an instance.
        
        @param request: EnableAdditionalBandwidthRequest
        @return: EnableAdditionalBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_additional_bandwidth_with_options_async(request, runtime)

    def flush_expire_keys_with_options(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        """
        @summary Deletes the expired keys from an ApsaraDB for Redis instance.
        
        @description For more information about how to clear the expired keys in the ApsaraDB for Redis console, see [Clear data](https://help.aliyun.com/document_detail/43881.html).
        >  Expired keys cannot be recovered after they are deleted. Exercise caution when you call this operation.
        
        @param request: FlushExpireKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushExpireKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='FlushExpireKeys',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def flush_expire_keys_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        """
        @summary Deletes the expired keys from an ApsaraDB for Redis instance.
        
        @description For more information about how to clear the expired keys in the ApsaraDB for Redis console, see [Clear data](https://help.aliyun.com/document_detail/43881.html).
        >  Expired keys cannot be recovered after they are deleted. Exercise caution when you call this operation.
        
        @param request: FlushExpireKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushExpireKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='FlushExpireKeys',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flush_expire_keys(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        """
        @summary Deletes the expired keys from an ApsaraDB for Redis instance.
        
        @description For more information about how to clear the expired keys in the ApsaraDB for Redis console, see [Clear data](https://help.aliyun.com/document_detail/43881.html).
        >  Expired keys cannot be recovered after they are deleted. Exercise caution when you call this operation.
        
        @param request: FlushExpireKeysRequest
        @return: FlushExpireKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flush_expire_keys_with_options(request, runtime)

    async def flush_expire_keys_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        """
        @summary Deletes the expired keys from an ApsaraDB for Redis instance.
        
        @description For more information about how to clear the expired keys in the ApsaraDB for Redis console, see [Clear data](https://help.aliyun.com/document_detail/43881.html).
        >  Expired keys cannot be recovered after they are deleted. Exercise caution when you call this operation.
        
        @param request: FlushExpireKeysRequest
        @return: FlushExpireKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flush_expire_keys_with_options_async(request, runtime)

    def flush_instance_with_options(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        """
        @summary Clears the data of an ApsaraDB for Redis instance. The cleared data cannot be restored.
        
        @param request: FlushInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='FlushInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def flush_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        """
        @summary Clears the data of an ApsaraDB for Redis instance. The cleared data cannot be restored.
        
        @param request: FlushInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='FlushInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flush_instance(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        """
        @summary Clears the data of an ApsaraDB for Redis instance. The cleared data cannot be restored.
        
        @param request: FlushInstanceRequest
        @return: FlushInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flush_instance_with_options(request, runtime)

    async def flush_instance_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        """
        @summary Clears the data of an ApsaraDB for Redis instance. The cleared data cannot be restored.
        
        @param request: FlushInstanceRequest
        @return: FlushInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flush_instance_with_options_async(request, runtime)

    def flush_instance_for_dbwith_options(
        self,
        request: r_kvstore_20150101_models.FlushInstanceForDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceForDBResponse:
        """
        @summary Cleans the data of specified databases in an instance.
        
        @description Each ApsaraDB for Redis or Tair instance can contain up to 256 databases. Each database does not have a separate memory usage limit. The memory capacity that a database can use is subject to the total memory limit of the instance. You can execute the `SELECT` statement to switch between databases. For more information, see [What is the size of each database on an ApsaraDB for Redis instance, and how can I choose databases?](https://help.aliyun.com/document_detail/38688.html)
        >  This operation is available only for cloud-native instances that use cloud disks.
        
        @param request: FlushInstanceForDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushInstanceForDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_index):
            query['DbIndex'] = request.db_index
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='FlushInstanceForDB',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceForDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def flush_instance_for_dbwith_options_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceForDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceForDBResponse:
        """
        @summary Cleans the data of specified databases in an instance.
        
        @description Each ApsaraDB for Redis or Tair instance can contain up to 256 databases. Each database does not have a separate memory usage limit. The memory capacity that a database can use is subject to the total memory limit of the instance. You can execute the `SELECT` statement to switch between databases. For more information, see [What is the size of each database on an ApsaraDB for Redis instance, and how can I choose databases?](https://help.aliyun.com/document_detail/38688.html)
        >  This operation is available only for cloud-native instances that use cloud disks.
        
        @param request: FlushInstanceForDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlushInstanceForDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_index):
            query['DbIndex'] = request.db_index
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='FlushInstanceForDB',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceForDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flush_instance_for_db(
        self,
        request: r_kvstore_20150101_models.FlushInstanceForDBRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceForDBResponse:
        """
        @summary Cleans the data of specified databases in an instance.
        
        @description Each ApsaraDB for Redis or Tair instance can contain up to 256 databases. Each database does not have a separate memory usage limit. The memory capacity that a database can use is subject to the total memory limit of the instance. You can execute the `SELECT` statement to switch between databases. For more information, see [What is the size of each database on an ApsaraDB for Redis instance, and how can I choose databases?](https://help.aliyun.com/document_detail/38688.html)
        >  This operation is available only for cloud-native instances that use cloud disks.
        
        @param request: FlushInstanceForDBRequest
        @return: FlushInstanceForDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flush_instance_for_dbwith_options(request, runtime)

    async def flush_instance_for_db_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceForDBRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceForDBResponse:
        """
        @summary Cleans the data of specified databases in an instance.
        
        @description Each ApsaraDB for Redis or Tair instance can contain up to 256 databases. Each database does not have a separate memory usage limit. The memory capacity that a database can use is subject to the total memory limit of the instance. You can execute the `SELECT` statement to switch between databases. For more information, see [What is the size of each database on an ApsaraDB for Redis instance, and how can I choose databases?](https://help.aliyun.com/document_detail/38688.html)
        >  This operation is available only for cloud-native instances that use cloud disks.
        
        @param request: FlushInstanceForDBRequest
        @return: FlushInstanceForDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flush_instance_for_dbwith_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        """
        @summary Modifies the permissions of an account for an ApsaraDB for Redis instance.
        
        @description >
        Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        The ApsaraDB for Redis instance must be in the running state.
        
        @param request: GrantAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        """
        @summary Modifies the permissions of an account for an ApsaraDB for Redis instance.
        
        @description >
        Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        The ApsaraDB for Redis instance must be in the running state.
        
        @param request: GrantAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_account_privilege(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        """
        @summary Modifies the permissions of an account for an ApsaraDB for Redis instance.
        
        @description >
        Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        The ApsaraDB for Redis instance must be in the running state.
        
        @param request: GrantAccountPrivilegeRequest
        @return: GrantAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        """
        @summary Modifies the permissions of an account for an ApsaraDB for Redis instance.
        
        @description >
        Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        The ApsaraDB for Redis instance must be in the running state.
        
        @param request: GrantAccountPrivilegeRequest
        @return: GrantAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def initialize_kvstore_permission_with_options(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        """
        @summary Assigns a service-linked role to ApsaraDB for Redis.
        
        @description The log management feature of ApsaraDB for Redis requires the resources of [Log Service](https://help.aliyun.com/document_detail/48869.html). To use the log management feature of ApsaraDB for Redis, you can call this operation to associate the RAM role named AliyunServiceRoleForKvstore with the ApsaraDB for Redis instance. For more information, see [Associated RAM roles of ApsaraDB for Redis](https://help.aliyun.com/document_detail/184337.html).
        
        @param request: InitializeKvstorePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeKvstorePermissionResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeKvstorePermission',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_kvstore_permission_with_options_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        """
        @summary Assigns a service-linked role to ApsaraDB for Redis.
        
        @description The log management feature of ApsaraDB for Redis requires the resources of [Log Service](https://help.aliyun.com/document_detail/48869.html). To use the log management feature of ApsaraDB for Redis, you can call this operation to associate the RAM role named AliyunServiceRoleForKvstore with the ApsaraDB for Redis instance. For more information, see [Associated RAM roles of ApsaraDB for Redis](https://help.aliyun.com/document_detail/184337.html).
        
        @param request: InitializeKvstorePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeKvstorePermissionResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeKvstorePermission',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_kvstore_permission(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        """
        @summary Assigns a service-linked role to ApsaraDB for Redis.
        
        @description The log management feature of ApsaraDB for Redis requires the resources of [Log Service](https://help.aliyun.com/document_detail/48869.html). To use the log management feature of ApsaraDB for Redis, you can call this operation to associate the RAM role named AliyunServiceRoleForKvstore with the ApsaraDB for Redis instance. For more information, see [Associated RAM roles of ApsaraDB for Redis](https://help.aliyun.com/document_detail/184337.html).
        
        @param request: InitializeKvstorePermissionRequest
        @return: InitializeKvstorePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_kvstore_permission_with_options(request, runtime)

    async def initialize_kvstore_permission_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        """
        @summary Assigns a service-linked role to ApsaraDB for Redis.
        
        @description The log management feature of ApsaraDB for Redis requires the resources of [Log Service](https://help.aliyun.com/document_detail/48869.html). To use the log management feature of ApsaraDB for Redis, you can call this operation to associate the RAM role named AliyunServiceRoleForKvstore with the ApsaraDB for Redis instance. For more information, see [Associated RAM roles of ApsaraDB for Redis](https://help.aliyun.com/document_detail/184337.html).
        
        @param request: InitializeKvstorePermissionRequest
        @return: InitializeKvstorePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_kvstore_permission_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        """
        @summary Queries the relationships between ApsaraDB for Redis instances and tags.
        
        @description You can also query the relationships between instances and tags in the ApsaraDB for Redis console. For more information, see [Filter ApsaraDB for Redis instances by tag](https://help.aliyun.com/document_detail/119160.html) and [View tags bound to an instance](https://help.aliyun.com/document_detail/134038.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        """
        @summary Queries the relationships between ApsaraDB for Redis instances and tags.
        
        @description You can also query the relationships between instances and tags in the ApsaraDB for Redis console. For more information, see [Filter ApsaraDB for Redis instances by tag](https://help.aliyun.com/document_detail/119160.html) and [View tags bound to an instance](https://help.aliyun.com/document_detail/134038.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        """
        @summary Queries the relationships between ApsaraDB for Redis instances and tags.
        
        @description You can also query the relationships between instances and tags in the ApsaraDB for Redis console. For more information, see [Filter ApsaraDB for Redis instances by tag](https://help.aliyun.com/document_detail/119160.html) and [View tags bound to an instance](https://help.aliyun.com/document_detail/134038.html).
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        """
        @summary Queries the relationships between ApsaraDB for Redis instances and tags.
        
        @description You can also query the relationships between instances and tags in the ApsaraDB for Redis console. For more information, see [Filter ApsaraDB for Redis instances by tag](https://help.aliyun.com/document_detail/119160.html) and [View tags bound to an instance](https://help.aliyun.com/document_detail/134038.html).
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def lock_dbinstance_write_with_options(
        self,
        request: r_kvstore_20150101_models.LockDBInstanceWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.LockDBInstanceWriteResponse:
        """
        @summary Places a write lock on an instance. After the instance is locked, it supports only read operations.
        
        @param request: LockDBInstanceWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockDBInstanceWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='LockDBInstanceWrite',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.LockDBInstanceWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_dbinstance_write_with_options_async(
        self,
        request: r_kvstore_20150101_models.LockDBInstanceWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.LockDBInstanceWriteResponse:
        """
        @summary Places a write lock on an instance. After the instance is locked, it supports only read operations.
        
        @param request: LockDBInstanceWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockDBInstanceWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='LockDBInstanceWrite',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.LockDBInstanceWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_dbinstance_write(
        self,
        request: r_kvstore_20150101_models.LockDBInstanceWriteRequest,
    ) -> r_kvstore_20150101_models.LockDBInstanceWriteResponse:
        """
        @summary Places a write lock on an instance. After the instance is locked, it supports only read operations.
        
        @param request: LockDBInstanceWriteRequest
        @return: LockDBInstanceWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_dbinstance_write_with_options(request, runtime)

    async def lock_dbinstance_write_async(
        self,
        request: r_kvstore_20150101_models.LockDBInstanceWriteRequest,
    ) -> r_kvstore_20150101_models.LockDBInstanceWriteResponse:
        """
        @summary Places a write lock on an instance. After the instance is locked, it supports only read operations.
        
        @param request: LockDBInstanceWriteRequest
        @return: LockDBInstanceWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_dbinstance_write_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        """
        @summary Migrates an ApsaraDB for Redis instance to another zone in the same region.
        
        @description Before you call this operation, you must release the public endpoint (if any) of the instance. For more information, see [Migrate an instance across zones](https://help.aliyun.com/document_detail/106272.html).
        >
        If the network type of an ApsaraDB for Redis instance is switched from classic network to Virtual Private Cloud (VPC), and the classic network endpoint is retained, you can migrate the instance across zones only after the classic network endpoint is released upon expiration.
        After the instance is migrated, the endpoint of the instance remains unchanged. However, the virtual IP address (VIP) is changed. We recommend that you use the endpoint instead of the VIP to connect to the instance.
        
        @param request: MigrateToOtherZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        """
        @summary Migrates an ApsaraDB for Redis instance to another zone in the same region.
        
        @description Before you call this operation, you must release the public endpoint (if any) of the instance. For more information, see [Migrate an instance across zones](https://help.aliyun.com/document_detail/106272.html).
        >
        If the network type of an ApsaraDB for Redis instance is switched from classic network to Virtual Private Cloud (VPC), and the classic network endpoint is retained, you can migrate the instance across zones only after the classic network endpoint is released upon expiration.
        After the instance is migrated, the endpoint of the instance remains unchanged. However, the virtual IP address (VIP) is changed. We recommend that you use the endpoint instead of the VIP to connect to the instance.
        
        @param request: MigrateToOtherZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        """
        @summary Migrates an ApsaraDB for Redis instance to another zone in the same region.
        
        @description Before you call this operation, you must release the public endpoint (if any) of the instance. For more information, see [Migrate an instance across zones](https://help.aliyun.com/document_detail/106272.html).
        >
        If the network type of an ApsaraDB for Redis instance is switched from classic network to Virtual Private Cloud (VPC), and the classic network endpoint is retained, you can migrate the instance across zones only after the classic network endpoint is released upon expiration.
        After the instance is migrated, the endpoint of the instance remains unchanged. However, the virtual IP address (VIP) is changed. We recommend that you use the endpoint instead of the VIP to connect to the instance.
        
        @param request: MigrateToOtherZoneRequest
        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        """
        @summary Migrates an ApsaraDB for Redis instance to another zone in the same region.
        
        @description Before you call this operation, you must release the public endpoint (if any) of the instance. For more information, see [Migrate an instance across zones](https://help.aliyun.com/document_detail/106272.html).
        >
        If the network type of an ApsaraDB for Redis instance is switched from classic network to Virtual Private Cloud (VPC), and the classic network endpoint is retained, you can migrate the instance across zones only after the classic network endpoint is released upon expiration.
        After the instance is migrated, the endpoint of the instance remains unchanged. However, the virtual IP address (VIP) is changed. We recommend that you use the endpoint instead of the VIP to connect to the instance.
        
        @param request: MigrateToOtherZoneRequest
        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of an account for an ApsaraDB for Redis instance.
        
        @description > This operation is supported only for instances that run Redis 4.0 or later.
        
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of an account for an ApsaraDB for Redis instance.
        
        @description > This operation is supported only for instances that run Redis 4.0 or later.
        
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of an account for an ApsaraDB for Redis instance.
        
        @description > This operation is supported only for instances that run Redis 4.0 or later.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of an account for an ApsaraDB for Redis instance.
        
        @description > This operation is supported only for instances that run Redis 4.0 or later.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a specific account for an ApsaraDB for Redis instance.
        
        @param request: ModifyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.old_account_password):
            query['OldAccountPassword'] = request.old_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a specific account for an ApsaraDB for Redis instance.
        
        @param request: ModifyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.old_account_password):
            query['OldAccountPassword'] = request.old_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_password(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a specific account for an ApsaraDB for Redis instance.
        
        @param request: ModifyAccountPasswordRequest
        @return: ModifyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a specific account for an ApsaraDB for Redis instance.
        
        @param request: ModifyAccountPasswordRequest
        @return: ModifyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        """
        @summary Changes the scheduled switchover time of an O&M task.
        
        @description You can receive notifications for ApsaraDB for Redis events such as instance migration and version upgrade by text message, phone call, email, internal message, or by using the ApsaraDB for Redis console. You can also change the scheduled switchover time of a task in the ApsaraDB for Redis console. For more information, see [Query or manage pending events](https://help.aliyun.com/document_detail/187022.html).
        
        @param request: ModifyActiveOperationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        """
        @summary Changes the scheduled switchover time of an O&M task.
        
        @description You can receive notifications for ApsaraDB for Redis events such as instance migration and version upgrade by text message, phone call, email, internal message, or by using the ApsaraDB for Redis console. You can also change the scheduled switchover time of a task in the ApsaraDB for Redis console. For more information, see [Query or manage pending events](https://help.aliyun.com/document_detail/187022.html).
        
        @param request: ModifyActiveOperationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_task(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        """
        @summary Changes the scheduled switchover time of an O&M task.
        
        @description You can receive notifications for ApsaraDB for Redis events such as instance migration and version upgrade by text message, phone call, email, internal message, or by using the ApsaraDB for Redis console. You can also change the scheduled switchover time of a task in the ApsaraDB for Redis console. For more information, see [Query or manage pending events](https://help.aliyun.com/document_detail/187022.html).
        
        @param request: ModifyActiveOperationTaskRequest
        @return: ModifyActiveOperationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_task_with_options(request, runtime)

    async def modify_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        """
        @summary Changes the scheduled switchover time of an O&M task.
        
        @description You can receive notifications for ApsaraDB for Redis events such as instance migration and version upgrade by text message, phone call, email, internal message, or by using the ApsaraDB for Redis console. You can also change the scheduled switchover time of a task in the ApsaraDB for Redis console. For more information, see [Query or manage pending events](https://help.aliyun.com/document_detail/187022.html).
        
        @param request: ModifyActiveOperationTaskRequest
        @return: ModifyActiveOperationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_task_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTasksResponse:
        """
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTasksResponse:
        """
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTasksRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTasksResponse:
        """
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTasksRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTasksResponse:
        """
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the audit log settings of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of the audit log feature.
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest major version and minor version.
        
        @param request: ModifyAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_audit):
            query['DbAudit'] = request.db_audit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the audit log settings of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of the audit log feature.
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest major version and minor version.
        
        @param request: ModifyAuditLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_audit):
            query['DbAudit'] = request.db_audit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the audit log settings of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of the audit log feature.
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest major version and minor version.
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        """
        @summary Modifies the audit log settings of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of the audit log feature.
        Before you call this operation, make sure that the ApsaraDB for Redis instance meets the following requirements:
        The instance is an ApsaraDB for Redis Community Edition instance or ApsaraDB for Redis Enhanced Edition (Tair) [DRAM-based instance](https://help.aliyun.com/document_detail/126164.html).
        The engine version of the instance is Redis 4.0 or later, and the latest minor version is used. You can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to check whether the instance uses the latest major version and minor version.
        
        @param request: ModifyAuditLogConfigRequest
        @return: ModifyAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of an ApsaraDB for Redis instance.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of an ApsaraDB for Redis instance.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of an ApsaraDB for Redis instance.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of an ApsaraDB for Redis instance.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_auto_upgrade_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse:
        """
        @summary Modifies the setting related to the automatic update of minor versions for an instance.
        
        @param request: ModifyDBInstanceAutoUpgradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAutoUpgradeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgrade',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_auto_upgrade_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse:
        """
        @summary Modifies the setting related to the automatic update of minor versions for an instance.
        
        @param request: ModifyDBInstanceAutoUpgradeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAutoUpgradeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgrade',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_auto_upgrade(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse:
        """
        @summary Modifies the setting related to the automatic update of minor versions for an instance.
        
        @param request: ModifyDBInstanceAutoUpgradeRequest
        @return: ModifyDBInstanceAutoUpgradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_with_options(request, runtime)

    async def modify_dbinstance_auto_upgrade_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceAutoUpgradeResponse:
        """
        @summary Modifies the setting related to the automatic update of minor versions for an instance.
        
        @param request: ModifyDBInstanceAutoUpgradeRequest
        @return: ModifyDBInstanceAutoUpgradeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_auto_upgrade_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Changes the endpoint or port number of an ApsaraDB for Redis instance.
        
        @description You can also modify the endpoint or port number of an instance in the ApsaraDB for Redis console. For more information, see [Change the endpoint or port number of an instance](https://help.aliyun.com/document_detail/85683.html).
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Changes the endpoint or port number of an ApsaraDB for Redis instance.
        
        @description You can also modify the endpoint or port number of an instance in the ApsaraDB for Redis console. For more information, see [Change the endpoint or port number of an instance](https://help.aliyun.com/document_detail/85683.html).
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Changes the endpoint or port number of an ApsaraDB for Redis instance.
        
        @description You can also modify the endpoint or port number of an instance in the ApsaraDB for Redis console. For more information, see [Change the endpoint or port number of an instance](https://help.aliyun.com/document_detail/85683.html).
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Changes the endpoint or port number of an ApsaraDB for Redis instance.
        
        @description You can also modify the endpoint or port number of an instance in the ApsaraDB for Redis console. For more information, see [Change the endpoint or port number of an instance](https://help.aliyun.com/document_detail/85683.html).
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_global_security_ipgroup_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_with_options(request, runtime)

    async def modify_global_security_ipgroup_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_with_options_async(request, runtime)

    def modify_global_security_ipgroup_name_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroupName',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_name_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroupName',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_name(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_name_with_options(request, runtime)

    async def modify_global_security_ipgroup_name_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_name_with_options_async(request, runtime)

    def modify_global_security_ipgroup_relation_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Adds a specified instance to a specified IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_relation_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Adds a specified instance to a specified IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_relation(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Adds a specified instance to a specified IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_relation_with_options(request, runtime)

    async def modify_global_security_ipgroup_relation_async(
        self,
        request: r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> r_kvstore_20150101_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Adds a specified instance to a specified IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_relation_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        """
        @summary Changes the information of an ApsaraDB for Redis instance, such as the name and password.
        
        @description You can also modify the information of an instance in the ApsaraDB for Redis console. For more information, see [Change or reset the password](https://help.aliyun.com/document_detail/43874.html).
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_release_protection):
            query['InstanceReleaseProtection'] = request.instance_release_protection
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        """
        @summary Changes the information of an ApsaraDB for Redis instance, such as the name and password.
        
        @description You can also modify the information of an instance in the ApsaraDB for Redis console. For more information, see [Change or reset the password](https://help.aliyun.com/document_detail/43874.html).
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_release_protection):
            query['InstanceReleaseProtection'] = request.instance_release_protection
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        """
        @summary Changes the information of an ApsaraDB for Redis instance, such as the name and password.
        
        @description You can also modify the information of an instance in the ApsaraDB for Redis console. For more information, see [Change or reset the password](https://help.aliyun.com/document_detail/43874.html).
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        """
        @summary Changes the information of an ApsaraDB for Redis instance, such as the name and password.
        
        @description You can also modify the information of an instance in the ApsaraDB for Redis console. For more information, see [Change or reset the password](https://help.aliyun.com/document_detail/43874.html).
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for Redis instance.
        
        @description > Auto-renewal is triggered seven days before the expiration date of the instance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for Redis instance.
        
        @description > Auto-renewal is triggered seven days before the expiration date of the instance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for Redis instance.
        
        @description > Auto-renewal is triggered seven days before the expiration date of the instance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for Redis instance.
        
        @description > Auto-renewal is triggered seven days before the expiration date of the instance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        """
        @summary Modifies the parameter settings of an ApsaraDB for Redis instance.
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        """
        @summary Modifies the parameter settings of an ApsaraDB for Redis instance.
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        """
        @summary Modifies the parameter settings of an ApsaraDB for Redis instance.
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        """
        @summary Modifies the parameter settings of an ApsaraDB for Redis instance.
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for Redis instance. Alibaba Cloud maintains ApsaraDB for Redis instances during the specified maintenance window.
        
        @description You can also modify the maintenance window of an instance in the ApsaraDB for Redis console. For more information, see [Set a maintenance window](https://help.aliyun.com/document_detail/55252.html).
        
        @param request: ModifyInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMaintainTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for Redis instance. Alibaba Cloud maintains ApsaraDB for Redis instances during the specified maintenance window.
        
        @description You can also modify the maintenance window of an instance in the ApsaraDB for Redis console. For more information, see [Set a maintenance window](https://help.aliyun.com/document_detail/55252.html).
        
        @param request: ModifyInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMaintainTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for Redis instance. Alibaba Cloud maintains ApsaraDB for Redis instances during the specified maintenance window.
        
        @description You can also modify the maintenance window of an instance in the ApsaraDB for Redis console. For more information, see [Set a maintenance window](https://help.aliyun.com/document_detail/55252.html).
        
        @param request: ModifyInstanceMaintainTimeRequest
        @return: ModifyInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for Redis instance. Alibaba Cloud maintains ApsaraDB for Redis instances during the specified maintenance window.
        
        @description You can also modify the maintenance window of an instance in the ApsaraDB for Redis console. For more information, see [Set a maintenance window](https://help.aliyun.com/document_detail/55252.html).
        
        @param request: ModifyInstanceMaintainTimeRequest
        @return: ModifyInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_major_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        """
        @summary Upgrades the major version of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Upgrade the major version](https://help.aliyun.com/document_detail/101764.html).
        
        @param request: ModifyInstanceMajorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMajorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMajorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_major_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        """
        @summary Upgrades the major version of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Upgrade the major version](https://help.aliyun.com/document_detail/101764.html).
        
        @param request: ModifyInstanceMajorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMajorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMajorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_major_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        """
        @summary Upgrades the major version of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Upgrade the major version](https://help.aliyun.com/document_detail/101764.html).
        
        @param request: ModifyInstanceMajorVersionRequest
        @return: ModifyInstanceMajorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_major_version_with_options(request, runtime)

    async def modify_instance_major_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        """
        @summary Upgrades the major version of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the corresponding operation in the console, see [Upgrade the major version](https://help.aliyun.com/document_detail/101764.html).
        
        @param request: ModifyInstanceMajorVersionRequest
        @return: ModifyInstanceMajorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_major_version_with_options_async(request, runtime)

    def modify_instance_minor_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        """
        @summary Updates the minor version of an ApsaraDB for Redis instance.
        
        @description The procedure to update the minor version of an instance varies based on types of ApsaraDB for Redis instances. For more information, see [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        >
        Before you call this operation, you can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to query the minor version of the current instance.
        When you switch your workloads over from the original instance to a new instance or from the master node to the replica node in the original instance, you may experience disconnections that last a few seconds. The original instance stays in the read-only state within 60 seconds until all data is synchronized. We recommend that you upgrade the original instance during off-peak hours and make sure that your application is configured to automatically reconnect to the original instance.
        
        @param request: ModifyInstanceMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minorversion):
            query['Minorversion'] = request.minorversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMinorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_minor_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        """
        @summary Updates the minor version of an ApsaraDB for Redis instance.
        
        @description The procedure to update the minor version of an instance varies based on types of ApsaraDB for Redis instances. For more information, see [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        >
        Before you call this operation, you can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to query the minor version of the current instance.
        When you switch your workloads over from the original instance to a new instance or from the master node to the replica node in the original instance, you may experience disconnections that last a few seconds. The original instance stays in the read-only state within 60 seconds until all data is synchronized. We recommend that you upgrade the original instance during off-peak hours and make sure that your application is configured to automatically reconnect to the original instance.
        
        @param request: ModifyInstanceMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minorversion):
            query['Minorversion'] = request.minorversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceMinorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_minor_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        """
        @summary Updates the minor version of an ApsaraDB for Redis instance.
        
        @description The procedure to update the minor version of an instance varies based on types of ApsaraDB for Redis instances. For more information, see [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        >
        Before you call this operation, you can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to query the minor version of the current instance.
        When you switch your workloads over from the original instance to a new instance or from the master node to the replica node in the original instance, you may experience disconnections that last a few seconds. The original instance stays in the read-only state within 60 seconds until all data is synchronized. We recommend that you upgrade the original instance during off-peak hours and make sure that your application is configured to automatically reconnect to the original instance.
        
        @param request: ModifyInstanceMinorVersionRequest
        @return: ModifyInstanceMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_minor_version_with_options(request, runtime)

    async def modify_instance_minor_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        """
        @summary Updates the minor version of an ApsaraDB for Redis instance.
        
        @description The procedure to update the minor version of an instance varies based on types of ApsaraDB for Redis instances. For more information, see [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        >
        Before you call this operation, you can call the [DescribeEngineVersion](https://help.aliyun.com/document_detail/95268.html) operation to query the minor version of the current instance.
        When you switch your workloads over from the original instance to a new instance or from the master node to the replica node in the original instance, you may experience disconnections that last a few seconds. The original instance stays in the read-only state within 60 seconds until all data is synchronized. We recommend that you upgrade the original instance during off-peak hours and make sure that your application is configured to automatically reconnect to the original instance.
        
        @param request: ModifyInstanceMinorVersionRequest
        @return: ModifyInstanceMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_minor_version_with_options_async(request, runtime)

    def modify_instance_net_expire_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for Redis instance. You can call this operation after you change the network type of the ApsaraDB for Redis instance from classic network to Virtual Private Cloud (VPC) with the classic network endpoint retained.
        
        @description You can also perform this operation in the ApsaraDB for Redis console. For more information, see [Change the expiration time for the endpoint of the classic network](https://help.aliyun.com/document_detail/60062.html).
        > For more information about how to switch the network type of an ApsaraDB for Redis instance from classic network to VPC, see [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html).
        
        @param request: ModifyInstanceNetExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNetExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceNetExpireTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_net_expire_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for Redis instance. You can call this operation after you change the network type of the ApsaraDB for Redis instance from classic network to Virtual Private Cloud (VPC) with the classic network endpoint retained.
        
        @description You can also perform this operation in the ApsaraDB for Redis console. For more information, see [Change the expiration time for the endpoint of the classic network](https://help.aliyun.com/document_detail/60062.html).
        > For more information about how to switch the network type of an ApsaraDB for Redis instance from classic network to VPC, see [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html).
        
        @param request: ModifyInstanceNetExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNetExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyInstanceNetExpireTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_net_expire_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for Redis instance. You can call this operation after you change the network type of the ApsaraDB for Redis instance from classic network to Virtual Private Cloud (VPC) with the classic network endpoint retained.
        
        @description You can also perform this operation in the ApsaraDB for Redis console. For more information, see [Change the expiration time for the endpoint of the classic network](https://help.aliyun.com/document_detail/60062.html).
        > For more information about how to switch the network type of an ApsaraDB for Redis instance from classic network to VPC, see [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html).
        
        @param request: ModifyInstanceNetExpireTimeRequest
        @return: ModifyInstanceNetExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_net_expire_time_with_options(request, runtime)

    async def modify_instance_net_expire_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for Redis instance. You can call this operation after you change the network type of the ApsaraDB for Redis instance from classic network to Virtual Private Cloud (VPC) with the classic network endpoint retained.
        
        @description You can also perform this operation in the ApsaraDB for Redis console. For more information, see [Change the expiration time for the endpoint of the classic network](https://help.aliyun.com/document_detail/60062.html).
        > For more information about how to switch the network type of an ApsaraDB for Redis instance from classic network to VPC, see [SwitchNetwork](https://help.aliyun.com/document_detail/61005.html).
        
        @param request: ModifyInstanceNetExpireTimeRequest
        @return: ModifyInstanceNetExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_net_expire_time_with_options_async(request, runtime)

    def modify_instance_parameter_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceParameterResponse:
        """
        @summary 修改实例参数
        
        @param request: ModifyInstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='ModifyInstanceParameter',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_parameter_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceParameterResponse:
        """
        @summary 修改实例参数
        
        @param request: ModifyInstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='ModifyInstanceParameter',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_parameter(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceParameterRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceParameterResponse:
        """
        @summary 修改实例参数
        
        @param request: ModifyInstanceParameterRequest
        @return: ModifyInstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_parameter_with_options(request, runtime)

    async def modify_instance_parameter_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceParameterRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceParameterResponse:
        """
        @summary 修改实例参数
        
        @param request: ModifyInstanceParameterRequest
        @return: ModifyInstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_parameter_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for Redis instance.
        
        @description You can also modify SSL encryption configurations in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        >  To specify the earliest supported SSL version, you can call the [ModifyInstanceConfig](~~ModifyInstanceConfig~~) operation to modify the required parameter.
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for Redis instance.
        
        @description You can also modify SSL encryption configurations in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        >  To specify the earliest supported SSL version, you can call the [ModifyInstanceConfig](~~ModifyInstanceConfig~~) operation to modify the required parameter.
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for Redis instance.
        
        @description You can also modify SSL encryption configurations in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        >  To specify the earliest supported SSL version, you can call the [ModifyInstanceConfig](~~ModifyInstanceConfig~~) operation to modify the required parameter.
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for Redis instance.
        
        @description You can also modify SSL encryption configurations in the ApsaraDB for Redis console. For more information, see [Configure SSL encryption](https://help.aliyun.com/document_detail/84898.html).
        >  To specify the earliest supported SSL version, you can call the [ModifyInstanceConfig](~~ModifyInstanceConfig~~) operation to modify the required parameter.
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        """
        @summary Changes the specifications of an ApsaraDB for Redis instance.
        
        @description >  For more information about the procedure, impacts, limits, and fees of this operation, see [Change the configurations of an instance](https://help.aliyun.com/document_detail/26353.html).
        
        @param request: ModifyInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        """
        @summary Changes the specifications of an ApsaraDB for Redis instance.
        
        @description >  For more information about the procedure, impacts, limits, and fees of this operation, see [Change the configurations of an instance](https://help.aliyun.com/document_detail/26353.html).
        
        @param request: ModifyInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.force_trans):
            query['ForceTrans'] = request.force_trans
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.slave_read_only_count):
            query['SlaveReadOnlyCount'] = request.slave_read_only_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_spec(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        """
        @summary Changes the specifications of an ApsaraDB for Redis instance.
        
        @description >  For more information about the procedure, impacts, limits, and fees of this operation, see [Change the configurations of an instance](https://help.aliyun.com/document_detail/26353.html).
        
        @param request: ModifyInstanceSpecRequest
        @return: ModifyInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        """
        @summary Changes the specifications of an ApsaraDB for Redis instance.
        
        @description >  For more information about the procedure, impacts, limits, and fees of this operation, see [Change the configurations of an instance](https://help.aliyun.com/document_detail/26353.html).
        
        @param request: ModifyInstanceSpecRequest
        @return: ModifyInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_tdewith_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        """
        @summary Enables transparent data encryption (TDE) for an ApsaraDB for Redis instance. You can use existing custom keys.
        
        @description > For more information about TDE and the impact of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: ModifyInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_name):
            query['EncryptionName'] = request.encryption_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTDE',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_tdewith_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        """
        @summary Enables transparent data encryption (TDE) for an ApsaraDB for Redis instance. You can use existing custom keys.
        
        @description > For more information about TDE and the impact of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: ModifyInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_name):
            query['EncryptionName'] = request.encryption_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTDE',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_tde(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        """
        @summary Enables transparent data encryption (TDE) for an ApsaraDB for Redis instance. You can use existing custom keys.
        
        @description > For more information about TDE and the impact of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: ModifyInstanceTDERequest
        @return: ModifyInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_tdewith_options(request, runtime)

    async def modify_instance_tde_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        """
        @summary Enables transparent data encryption (TDE) for an ApsaraDB for Redis instance. You can use existing custom keys.
        
        @description > For more information about TDE and the impact of TDE, see [Enable TDE](https://help.aliyun.com/document_detail/265913.html).
        
        @param request: ModifyInstanceTDERequest
        @return: ModifyInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_tdewith_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Enables or disables password-free access for an ApsaraDB for Redis instance. This way, you can connect to a database in a convenient and secure manner.
        
        @description When the password-free access feature is enabled, Elastic Compute Service (ECS) instances in the same virtual private cloud (VPC) can connect to the ApsaraDB for Redis instance without a password. You can also use the username and password to connect to the ApsaraDB for Redis instance.
        > The ApsaraDB for Redis instance is deployed in a VPC. For more information, see [Enable password-free access](https://help.aliyun.com/document_detail/85168.html).
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVpcAuthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Enables or disables password-free access for an ApsaraDB for Redis instance. This way, you can connect to a database in a convenient and secure manner.
        
        @description When the password-free access feature is enabled, Elastic Compute Service (ECS) instances in the same virtual private cloud (VPC) can connect to the ApsaraDB for Redis instance without a password. You can also use the username and password to connect to the ApsaraDB for Redis instance.
        > The ApsaraDB for Redis instance is deployed in a VPC. For more information, see [Enable password-free access](https://help.aliyun.com/document_detail/85168.html).
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVpcAuthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Enables or disables password-free access for an ApsaraDB for Redis instance. This way, you can connect to a database in a convenient and secure manner.
        
        @description When the password-free access feature is enabled, Elastic Compute Service (ECS) instances in the same virtual private cloud (VPC) can connect to the ApsaraDB for Redis instance without a password. You can also use the username and password to connect to the ApsaraDB for Redis instance.
        > The ApsaraDB for Redis instance is deployed in a VPC. For more information, see [Enable password-free access](https://help.aliyun.com/document_detail/85168.html).
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @return: ModifyInstanceVpcAuthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Enables or disables password-free access for an ApsaraDB for Redis instance. This way, you can connect to a database in a convenient and secure manner.
        
        @description When the password-free access feature is enabled, Elastic Compute Service (ECS) instances in the same virtual private cloud (VPC) can connect to the ApsaraDB for Redis instance without a password. You can also use the username and password to connect to the ApsaraDB for Redis instance.
        > The ApsaraDB for Redis instance is deployed in a VPC. For more information, see [Enable password-free access](https://help.aliyun.com/document_detail/85168.html).
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @return: ModifyInstanceVpcAuthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        """
        @summary Temporarily adjusts the internal bandwidth of an ApsaraDB for Redis instance that is deployed in a dedicated cluster.
        
        @description >
        This operation is applicable only to an ApsaraDB for Redis instance that is deployed in a dedicated cluster. To adjust the bandwidth of a standard ApsaraDB for Redis instance, call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation.
        
        @param request: ModifyIntranetAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIntranetAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.band_width):
            query['BandWidth'] = request.band_width
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        """
        @summary Temporarily adjusts the internal bandwidth of an ApsaraDB for Redis instance that is deployed in a dedicated cluster.
        
        @description >
        This operation is applicable only to an ApsaraDB for Redis instance that is deployed in a dedicated cluster. To adjust the bandwidth of a standard ApsaraDB for Redis instance, call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation.
        
        @param request: ModifyIntranetAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIntranetAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.band_width):
            query['BandWidth'] = request.band_width
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ModifyIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        """
        @summary Temporarily adjusts the internal bandwidth of an ApsaraDB for Redis instance that is deployed in a dedicated cluster.
        
        @description >
        This operation is applicable only to an ApsaraDB for Redis instance that is deployed in a dedicated cluster. To adjust the bandwidth of a standard ApsaraDB for Redis instance, call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation.
        
        @param request: ModifyIntranetAttributeRequest
        @return: ModifyIntranetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_intranet_attribute_with_options(request, runtime)

    async def modify_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        """
        @summary Temporarily adjusts the internal bandwidth of an ApsaraDB for Redis instance that is deployed in a dedicated cluster.
        
        @description >
        This operation is applicable only to an ApsaraDB for Redis instance that is deployed in a dedicated cluster. To adjust the bandwidth of a standard ApsaraDB for Redis instance, call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation.
        
        @param request: ModifyIntranetAttributeRequest
        @return: ModifyIntranetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_intranet_attribute_with_options_async(request, runtime)

    def modify_parameter_group_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyParameterGroupResponse:
        """
        @summary Modifies the settings of a parameter template.
        
        @param request: ModifyParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='ModifyParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameter_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyParameterGroupResponse:
        """
        @summary Modifies the settings of a parameter template.
        
        @param request: ModifyParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
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
            action='ModifyParameterGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameter_group(
        self,
        request: r_kvstore_20150101_models.ModifyParameterGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyParameterGroupResponse:
        """
        @summary Modifies the settings of a parameter template.
        
        @param request: ModifyParameterGroupRequest
        @return: ModifyParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    async def modify_parameter_group_async(
        self,
        request: r_kvstore_20150101_models.ModifyParameterGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyParameterGroupResponse:
        """
        @summary Modifies the settings of a parameter template.
        
        @param request: ModifyParameterGroupRequest
        @return: ModifyParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_group_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        """
        @summary Changes the resource group to which an ApsaraDB for Redis instance belongs.
        
        @description Resource groups allow you to sort resources owned by your Alibaba Cloud account into groups. This simplifies resource and permission management within your Alibaba Cloud account. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        > For more information about resource group API operations, see [Resource Management API overview](https://help.aliyun.com/document_detail/160024.html).
        
        @param request: ModifyResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyResourceGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        """
        @summary Changes the resource group to which an ApsaraDB for Redis instance belongs.
        
        @description Resource groups allow you to sort resources owned by your Alibaba Cloud account into groups. This simplifies resource and permission management within your Alibaba Cloud account. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        > For more information about resource group API operations, see [Resource Management API overview](https://help.aliyun.com/document_detail/160024.html).
        
        @param request: ModifyResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyResourceGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_group(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        """
        @summary Changes the resource group to which an ApsaraDB for Redis instance belongs.
        
        @description Resource groups allow you to sort resources owned by your Alibaba Cloud account into groups. This simplifies resource and permission management within your Alibaba Cloud account. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        > For more information about resource group API operations, see [Resource Management API overview](https://help.aliyun.com/document_detail/160024.html).
        
        @param request: ModifyResourceGroupRequest
        @return: ModifyResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        """
        @summary Changes the resource group to which an ApsaraDB for Redis instance belongs.
        
        @description Resource groups allow you to sort resources owned by your Alibaba Cloud account into groups. This simplifies resource and permission management within your Alibaba Cloud account. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        > For more information about resource group API operations, see [Resource Management API overview](https://help.aliyun.com/document_detail/160024.html).
        
        @param request: ModifyResourceGroupRequest
        @return: ModifyResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary Resets the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @description > After you call this operation, the security groups that are added to the whitelists of the ApsaraDB for Redis instance are deleted, and the security group specified by the *SecurityGroupId** parameter is added to the whitelists. For more information about how to reset security groups in the ApsaraDB for Redis console, see [Add security groups](https://help.aliyun.com/document_detail/148267.html).
        
        @param request: ModifySecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary Resets the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @description > After you call this operation, the security groups that are added to the whitelists of the ApsaraDB for Redis instance are deleted, and the security group specified by the *SecurityGroupId** parameter is added to the whitelists. For more information about how to reset security groups in the ApsaraDB for Redis console, see [Add security groups](https://help.aliyun.com/document_detail/148267.html).
        
        @param request: ModifySecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary Resets the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @description > After you call this operation, the security groups that are added to the whitelists of the ApsaraDB for Redis instance are deleted, and the security group specified by the *SecurityGroupId** parameter is added to the whitelists. For more information about how to reset security groups in the ApsaraDB for Redis console, see [Add security groups](https://help.aliyun.com/document_detail/148267.html).
        
        @param request: ModifySecurityGroupConfigurationRequest
        @return: ModifySecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary Resets the security groups that are added to the whitelists of an ApsaraDB for Redis instance.
        
        @description > After you call this operation, the security groups that are added to the whitelists of the ApsaraDB for Redis instance are deleted, and the security group specified by the *SecurityGroupId** parameter is added to the whitelists. For more information about how to reset security groups in the ApsaraDB for Redis console, see [Add security groups](https://help.aliyun.com/document_detail/148267.html).
        
        @param request: ModifySecurityGroupConfigurationRequest
        @return: ModifySecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelists of an ApsaraDB for Redis instance.
        
        @description You can also modify the whitelists of an instance in the ApsaraDB for Redis console. For more information, see [Configure a whitelist for an instance](https://help.aliyun.com/document_detail/56464.html).
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelists of an ApsaraDB for Redis instance.
        
        @description You can also modify the whitelists of an instance in the ApsaraDB for Redis console. For more information, see [Configure a whitelist for an instance](https://help.aliyun.com/document_detail/56464.html).
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelists of an ApsaraDB for Redis instance.
        
        @description You can also modify the whitelists of an instance in the ApsaraDB for Redis console. For more information, see [Configure a whitelist for an instance](https://help.aliyun.com/document_detail/56464.html).
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelists of an ApsaraDB for Redis instance.
        
        @description You can also modify the whitelists of an instance in the ApsaraDB for Redis console. For more information, see [Configure a whitelist for an instance](https://help.aliyun.com/document_detail/56464.html).
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def release_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        """
        @summary Releases the private endpoint of an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, clients can bypass proxy nodes and use private endpoints to connect to ApsaraDB for Redis instances. This is similar to the connection to a native Redis cluster. The direct connection mode can reduce communication overheads and the response time of ApsaraDB for Redis. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        
        @param request: ReleaseDirectConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseDirectConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ReleaseDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        """
        @summary Releases the private endpoint of an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, clients can bypass proxy nodes and use private endpoints to connect to ApsaraDB for Redis instances. This is similar to the connection to a native Redis cluster. The direct connection mode can reduce communication overheads and the response time of ApsaraDB for Redis. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        
        @param request: ReleaseDirectConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseDirectConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ReleaseDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_direct_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        """
        @summary Releases the private endpoint of an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, clients can bypass proxy nodes and use private endpoints to connect to ApsaraDB for Redis instances. This is similar to the connection to a native Redis cluster. The direct connection mode can reduce communication overheads and the response time of ApsaraDB for Redis. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        
        @param request: ReleaseDirectConnectionRequest
        @return: ReleaseDirectConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_direct_connection_with_options(request, runtime)

    async def release_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        """
        @summary Releases the private endpoint of an ApsaraDB for Redis cluster instance.
        
        @description In direct connection mode, clients can bypass proxy nodes and use private endpoints to connect to ApsaraDB for Redis instances. This is similar to the connection to a native Redis cluster. The direct connection mode can reduce communication overheads and the response time of ApsaraDB for Redis. For more information, see [Enable the direct connection mode](https://help.aliyun.com/document_detail/146901.html).
        
        @param request: ReleaseDirectConnectionRequest
        @return: ReleaseDirectConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_direct_connection_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the API operation in the ApsaraDB for Redis console, see [Release public endpoints](https://help.aliyun.com/document_detail/125424.html).
        
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ReleaseInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the API operation in the ApsaraDB for Redis console, see [Release public endpoints](https://help.aliyun.com/document_detail/125424.html).
        
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ReleaseInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the API operation in the ApsaraDB for Redis console, see [Release public endpoints](https://help.aliyun.com/document_detail/125424.html).
        
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for Redis instance.
        
        @description For more information about how to perform the API operation in the ApsaraDB for Redis console, see [Release public endpoints](https://help.aliyun.com/document_detail/125424.html).
        
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def remove_sub_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        """
        @summary Removes a child instance from a distributed instance.
        
        @description The operation that you want to perform. Set the value to *RemoveSubInstance**.
        
        @param request: RemoveSubInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSubInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='RemoveSubInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RemoveSubInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_sub_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        """
        @summary Removes a child instance from a distributed instance.
        
        @description The operation that you want to perform. Set the value to *RemoveSubInstance**.
        
        @param request: RemoveSubInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSubInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='RemoveSubInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RemoveSubInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_sub_instance(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        """
        @summary Removes a child instance from a distributed instance.
        
        @description The operation that you want to perform. Set the value to *RemoveSubInstance**.
        
        @param request: RemoveSubInstanceRequest
        @return: RemoveSubInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_sub_instance_with_options(request, runtime)

    async def remove_sub_instance_async(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        """
        @summary Removes a child instance from a distributed instance.
        
        @description The operation that you want to perform. Set the value to *RemoveSubInstance**.
        
        @param request: RemoveSubInstanceRequest
        @return: RemoveSubInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_sub_instance_with_options_async(request, runtime)

    def renew_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        """
        @summary Renews the purchased bandwidth for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can adjust the bandwidth of an instance in the ApsaraDB for Redis console. For more information, see [Adjust the bandwidth of an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/102588.html). You can also call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to adjust the bandwidth of an instance. If you want to continue using the bandwidth that you purchase after the validity period of the bandwidth, you must call the RenewAdditionalBandwidth operation to renew the bandwidth before the bandwidth expires.
        > Before you call this operation, you can call the [DescribeIntranetAttribute](https://help.aliyun.com/document_detail/128715.html) operation, which returns the expiration time of the purchased bandwidth in the *BandwidthExpireTime** parameter.
        
        @param request: RenewAdditionalBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAdditionalBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        """
        @summary Renews the purchased bandwidth for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can adjust the bandwidth of an instance in the ApsaraDB for Redis console. For more information, see [Adjust the bandwidth of an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/102588.html). You can also call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to adjust the bandwidth of an instance. If you want to continue using the bandwidth that you purchase after the validity period of the bandwidth, you must call the RenewAdditionalBandwidth operation to renew the bandwidth before the bandwidth expires.
        > Before you call this operation, you can call the [DescribeIntranetAttribute](https://help.aliyun.com/document_detail/128715.html) operation, which returns the expiration time of the purchased bandwidth in the *BandwidthExpireTime** parameter.
        
        @param request: RenewAdditionalBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAdditionalBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        """
        @summary Renews the purchased bandwidth for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can adjust the bandwidth of an instance in the ApsaraDB for Redis console. For more information, see [Adjust the bandwidth of an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/102588.html). You can also call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to adjust the bandwidth of an instance. If you want to continue using the bandwidth that you purchase after the validity period of the bandwidth, you must call the RenewAdditionalBandwidth operation to renew the bandwidth before the bandwidth expires.
        > Before you call this operation, you can call the [DescribeIntranetAttribute](https://help.aliyun.com/document_detail/128715.html) operation, which returns the expiration time of the purchased bandwidth in the *BandwidthExpireTime** parameter.
        
        @param request: RenewAdditionalBandwidthRequest
        @return: RenewAdditionalBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_additional_bandwidth_with_options(request, runtime)

    async def renew_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        """
        @summary Renews the purchased bandwidth for an ApsaraDB for Redis instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/54532.html) of ApsaraDB for Redis.
        You can adjust the bandwidth of an instance in the ApsaraDB for Redis console. For more information, see [Adjust the bandwidth of an ApsaraDB for Redis instance](https://help.aliyun.com/document_detail/102588.html). You can also call the [EnableAdditionalBandwidth](https://help.aliyun.com/document_detail/206173.html) operation to adjust the bandwidth of an instance. If you want to continue using the bandwidth that you purchase after the validity period of the bandwidth, you must call the RenewAdditionalBandwidth operation to renew the bandwidth before the bandwidth expires.
        > Before you call this operation, you can call the [DescribeIntranetAttribute](https://help.aliyun.com/document_detail/128715.html) operation, which returns the expiration time of the purchased bandwidth in the *BandwidthExpireTime** parameter.
        
        @param request: RenewAdditionalBandwidthRequest
        @return: RenewAdditionalBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_additional_bandwidth_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        """
        @summary Renews an ApsaraDB for Redis instance.
        
        @description This operation is applicable only to subscription instances.
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='RenewInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        """
        @summary Renews an ApsaraDB for Redis instance.
        
        @description This operation is applicable only to subscription instances.
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='RenewInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        """
        @summary Renews an ApsaraDB for Redis instance.
        
        @description This operation is applicable only to subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        """
        @summary Renews an ApsaraDB for Redis instance.
        
        @description This operation is applicable only to subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for Redis instance.
        
        @description >  Only ApsaraDB for Redis instances of Redis 4.0 or later are supported.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        """
        @summary Restarts a running ApsaraDB for Redis instance.
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_minor_version):
            query['UpgradeMinorVersion'] = request.upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        """
        @summary Restarts a running ApsaraDB for Redis instance.
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_minor_version):
            query['UpgradeMinorVersion'] = request.upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        """
        @summary Restarts a running ApsaraDB for Redis instance.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        """
        @summary Restarts a running ApsaraDB for Redis instance.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def restore_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        """
        @summary Restores the data in a backup file to a specified ApsaraDB for Redis instance.
        
        @description    If your instance is a [persistent memory-optimized instance](https://help.aliyun.com/document_detail/443828.html) or [DRAM-based instance](https://help.aliyun.com/document_detail/443827.html) that is compatible with Redis 5.0 and the [data flashback](https://help.aliyun.com/document_detail/443784.html) feature is enabled, you can call this operation to restore the data of a specified key to a specified point in time that is accurate to the second. Other keys are not affected. This way, you can achieve more fine-grained data restoration.
        For other instance series, this operation overwrites the existing data of your instance with the backup data. Proceed with caution. We recommend that you call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance. Then, you can restore data to the new instance.
        
        @param request: RestoreInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time_shift):
            query['TimeShift'] = request.time_shift
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        """
        @summary Restores the data in a backup file to a specified ApsaraDB for Redis instance.
        
        @description    If your instance is a [persistent memory-optimized instance](https://help.aliyun.com/document_detail/443828.html) or [DRAM-based instance](https://help.aliyun.com/document_detail/443827.html) that is compatible with Redis 5.0 and the [data flashback](https://help.aliyun.com/document_detail/443784.html) feature is enabled, you can call this operation to restore the data of a specified key to a specified point in time that is accurate to the second. Other keys are not affected. This way, you can achieve more fine-grained data restoration.
        For other instance series, this operation overwrites the existing data of your instance with the backup data. Proceed with caution. We recommend that you call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance. Then, you can restore data to the new instance.
        
        @param request: RestoreInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time_shift):
            query['TimeShift'] = request.time_shift
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_instance(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        """
        @summary Restores the data in a backup file to a specified ApsaraDB for Redis instance.
        
        @description    If your instance is a [persistent memory-optimized instance](https://help.aliyun.com/document_detail/443828.html) or [DRAM-based instance](https://help.aliyun.com/document_detail/443827.html) that is compatible with Redis 5.0 and the [data flashback](https://help.aliyun.com/document_detail/443784.html) feature is enabled, you can call this operation to restore the data of a specified key to a specified point in time that is accurate to the second. Other keys are not affected. This way, you can achieve more fine-grained data restoration.
        For other instance series, this operation overwrites the existing data of your instance with the backup data. Proceed with caution. We recommend that you call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance. Then, you can restore data to the new instance.
        
        @param request: RestoreInstanceRequest
        @return: RestoreInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_instance_with_options(request, runtime)

    async def restore_instance_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        """
        @summary Restores the data in a backup file to a specified ApsaraDB for Redis instance.
        
        @description    If your instance is a [persistent memory-optimized instance](https://help.aliyun.com/document_detail/443828.html) or [DRAM-based instance](https://help.aliyun.com/document_detail/443827.html) that is compatible with Redis 5.0 and the [data flashback](https://help.aliyun.com/document_detail/443784.html) feature is enabled, you can call this operation to restore the data of a specified key to a specified point in time that is accurate to the second. Other keys are not affected. This way, you can achieve more fine-grained data restoration.
        For other instance series, this operation overwrites the existing data of your instance with the backup data. Proceed with caution. We recommend that you call the [CreateInstance](https://help.aliyun.com/document_detail/60873.html) operation to create an instance. Then, you can restore data to the new instance.
        
        @param request: RestoreInstanceRequest
        @return: RestoreInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_instance_with_options_async(request, runtime)

    def switch_instance_hawith_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        """
        @summary Performs a master-replica switchover to switch node roles. This operation is applicable to disaster recovery drills and nearby access to applications that are deployed across zones.
        
        @description > For more information about nearby access to applications that are deployed across zones, see [Switch node roles](https://help.aliyun.com/document_detail/164222.html).
        The instance must be an ApsaraDB for Redis Community Edition instance or Enhanced Edition (Tair) [DRAM-based](https://help.aliyun.com/document_detail/126164.html) instance that uses local disks.
        A call to this operation has the following impacts on your instance:
        The data shards in the instance may change to the read-only state and experience transient connections within seconds. Make sure that your application is configured to automatically reconnect to the instance.
        If the instance enters the switching state, you cannot manage this instance. For example, you cannot modify the instance configurations or migrate the instance to another zone.
        
        @param request: SwitchInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceHA',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_instance_hawith_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        """
        @summary Performs a master-replica switchover to switch node roles. This operation is applicable to disaster recovery drills and nearby access to applications that are deployed across zones.
        
        @description > For more information about nearby access to applications that are deployed across zones, see [Switch node roles](https://help.aliyun.com/document_detail/164222.html).
        The instance must be an ApsaraDB for Redis Community Edition instance or Enhanced Edition (Tair) [DRAM-based](https://help.aliyun.com/document_detail/126164.html) instance that uses local disks.
        A call to this operation has the following impacts on your instance:
        The data shards in the instance may change to the read-only state and experience transient connections within seconds. Make sure that your application is configured to automatically reconnect to the instance.
        If the instance enters the switching state, you cannot manage this instance. For example, you cannot modify the instance configurations or migrate the instance to another zone.
        
        @param request: SwitchInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceHA',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_instance_ha(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        """
        @summary Performs a master-replica switchover to switch node roles. This operation is applicable to disaster recovery drills and nearby access to applications that are deployed across zones.
        
        @description > For more information about nearby access to applications that are deployed across zones, see [Switch node roles](https://help.aliyun.com/document_detail/164222.html).
        The instance must be an ApsaraDB for Redis Community Edition instance or Enhanced Edition (Tair) [DRAM-based](https://help.aliyun.com/document_detail/126164.html) instance that uses local disks.
        A call to this operation has the following impacts on your instance:
        The data shards in the instance may change to the read-only state and experience transient connections within seconds. Make sure that your application is configured to automatically reconnect to the instance.
        If the instance enters the switching state, you cannot manage this instance. For example, you cannot modify the instance configurations or migrate the instance to another zone.
        
        @param request: SwitchInstanceHARequest
        @return: SwitchInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_hawith_options(request, runtime)

    async def switch_instance_ha_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        """
        @summary Performs a master-replica switchover to switch node roles. This operation is applicable to disaster recovery drills and nearby access to applications that are deployed across zones.
        
        @description > For more information about nearby access to applications that are deployed across zones, see [Switch node roles](https://help.aliyun.com/document_detail/164222.html).
        The instance must be an ApsaraDB for Redis Community Edition instance or Enhanced Edition (Tair) [DRAM-based](https://help.aliyun.com/document_detail/126164.html) instance that uses local disks.
        A call to this operation has the following impacts on your instance:
        The data shards in the instance may change to the read-only state and experience transient connections within seconds. Make sure that your application is configured to automatically reconnect to the instance.
        If the instance enters the switching state, you cannot manage this instance. For example, you cannot modify the instance configurations or migrate the instance to another zone.
        
        @param request: SwitchInstanceHARequest
        @return: SwitchInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_hawith_options_async(request, runtime)

    def switch_instance_proxy_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        """
        @summary Enables or disables the proxy mode for an ApsaraDB for Redis cluster instance in a dedicated cluster.
        
        @description For more information about the proxy mode, see [Features of proxy nodes](https://help.aliyun.com/document_detail/142959.html). Before you call this operation, make sure that the following requirements are met:
        Your ApsaraDB for Redis instance is created by using a dedicated cluster. For more information, see [What is ApsaraDB MyBase?](https://help.aliyun.com/document_detail/141455.html)
        The instance uses the cluster architecture. For more information about the cluster architecture, see [Cluster master-replica instances](https://help.aliyun.com/document_detail/52228.html).
        > Before you call the SwitchInstanceProxy operation, you must call the [DescribeDedicatedClusterInstanceList](https://help.aliyun.com/document_detail/229522.html) operation and view the value of the *ProxyCount** response parameter to check whether the proxy mode is enabled. A value of 0 indicates that the proxy mode is disabled. A value that is greater than 0 indicates that the proxy mode is enabled.
        
        @param request: SwitchInstanceProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchInstanceProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='SwitchInstanceProxy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_instance_proxy_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        """
        @summary Enables or disables the proxy mode for an ApsaraDB for Redis cluster instance in a dedicated cluster.
        
        @description For more information about the proxy mode, see [Features of proxy nodes](https://help.aliyun.com/document_detail/142959.html). Before you call this operation, make sure that the following requirements are met:
        Your ApsaraDB for Redis instance is created by using a dedicated cluster. For more information, see [What is ApsaraDB MyBase?](https://help.aliyun.com/document_detail/141455.html)
        The instance uses the cluster architecture. For more information about the cluster architecture, see [Cluster master-replica instances](https://help.aliyun.com/document_detail/52228.html).
        > Before you call the SwitchInstanceProxy operation, you must call the [DescribeDedicatedClusterInstanceList](https://help.aliyun.com/document_detail/229522.html) operation and view the value of the *ProxyCount** response parameter to check whether the proxy mode is enabled. A value of 0 indicates that the proxy mode is disabled. A value that is greater than 0 indicates that the proxy mode is enabled.
        
        @param request: SwitchInstanceProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchInstanceProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='SwitchInstanceProxy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_instance_proxy(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        """
        @summary Enables or disables the proxy mode for an ApsaraDB for Redis cluster instance in a dedicated cluster.
        
        @description For more information about the proxy mode, see [Features of proxy nodes](https://help.aliyun.com/document_detail/142959.html). Before you call this operation, make sure that the following requirements are met:
        Your ApsaraDB for Redis instance is created by using a dedicated cluster. For more information, see [What is ApsaraDB MyBase?](https://help.aliyun.com/document_detail/141455.html)
        The instance uses the cluster architecture. For more information about the cluster architecture, see [Cluster master-replica instances](https://help.aliyun.com/document_detail/52228.html).
        > Before you call the SwitchInstanceProxy operation, you must call the [DescribeDedicatedClusterInstanceList](https://help.aliyun.com/document_detail/229522.html) operation and view the value of the *ProxyCount** response parameter to check whether the proxy mode is enabled. A value of 0 indicates that the proxy mode is disabled. A value that is greater than 0 indicates that the proxy mode is enabled.
        
        @param request: SwitchInstanceProxyRequest
        @return: SwitchInstanceProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_proxy_with_options(request, runtime)

    async def switch_instance_proxy_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        """
        @summary Enables or disables the proxy mode for an ApsaraDB for Redis cluster instance in a dedicated cluster.
        
        @description For more information about the proxy mode, see [Features of proxy nodes](https://help.aliyun.com/document_detail/142959.html). Before you call this operation, make sure that the following requirements are met:
        Your ApsaraDB for Redis instance is created by using a dedicated cluster. For more information, see [What is ApsaraDB MyBase?](https://help.aliyun.com/document_detail/141455.html)
        The instance uses the cluster architecture. For more information about the cluster architecture, see [Cluster master-replica instances](https://help.aliyun.com/document_detail/52228.html).
        > Before you call the SwitchInstanceProxy operation, you must call the [DescribeDedicatedClusterInstanceList](https://help.aliyun.com/document_detail/229522.html) operation and view the value of the *ProxyCount** response parameter to check whether the proxy mode is enabled. A value of 0 indicates that the proxy mode is disabled. A value that is greater than 0 indicates that the proxy mode is enabled.
        
        @param request: SwitchInstanceProxyRequest
        @return: SwitchInstanceProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_proxy_with_options_async(request, runtime)

    def switch_network_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        """
        @summary Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB for Redis instance. If the instance is deployed in the classic network, the network type of the instance is changed from the classic network to VPC.
        
        @param request: SwitchNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_network_type):
            query['TargetNetworkType'] = request.target_network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchNetwork',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_network_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        """
        @summary Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB for Redis instance. If the instance is deployed in the classic network, the network type of the instance is changed from the classic network to VPC.
        
        @param request: SwitchNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_network_type):
            query['TargetNetworkType'] = request.target_network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchNetwork',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_network(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        """
        @summary Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB for Redis instance. If the instance is deployed in the classic network, the network type of the instance is changed from the classic network to VPC.
        
        @param request: SwitchNetworkRequest
        @return: SwitchNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_network_with_options(request, runtime)

    async def switch_network_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        """
        @summary Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB for Redis instance. If the instance is deployed in the classic network, the network type of the instance is changed from the classic network to VPC.
        
        @param request: SwitchNetworkRequest
        @return: SwitchNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_network_with_options_async(request, runtime)

    def sync_dts_status_with_options(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        """
        @summary Disables configuration changes for an ApsaraDB for Redis instance before you use Data Transmission Service (DTS) to migrate or synchronize data of the instance. This prevents migration and synchronization task failures due to the configuration change.
        
        @param request: SyncDtsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncDtsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDtsStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_dts_status_with_options_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        """
        @summary Disables configuration changes for an ApsaraDB for Redis instance before you use Data Transmission Service (DTS) to migrate or synchronize data of the instance. This prevents migration and synchronization task failures due to the configuration change.
        
        @param request: SyncDtsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncDtsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDtsStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_dts_status(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        """
        @summary Disables configuration changes for an ApsaraDB for Redis instance before you use Data Transmission Service (DTS) to migrate or synchronize data of the instance. This prevents migration and synchronization task failures due to the configuration change.
        
        @param request: SyncDtsStatusRequest
        @return: SyncDtsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_dts_status_with_options(request, runtime)

    async def sync_dts_status_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        """
        @summary Disables configuration changes for an ApsaraDB for Redis instance before you use Data Transmission Service (DTS) to migrate or synchronize data of the instance. This prevents migration and synchronization task failures due to the configuration change.
        
        @param request: SyncDtsStatusRequest
        @return: SyncDtsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_dts_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        """
        @summary Adds specified tags to one or more ApsaraDB for Redis instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to each instance.
        You can add tags to up to 50 instances in each request.
        You can also add tags to instances in the ApsaraDB for Redis console. For more information, see [Create a tag](https://help.aliyun.com/document_detail/118779.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        """
        @summary Adds specified tags to one or more ApsaraDB for Redis instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to each instance.
        You can add tags to up to 50 instances in each request.
        You can also add tags to instances in the ApsaraDB for Redis console. For more information, see [Create a tag](https://help.aliyun.com/document_detail/118779.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        """
        @summary Adds specified tags to one or more ApsaraDB for Redis instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to each instance.
        You can add tags to up to 50 instances in each request.
        You can also add tags to instances in the ApsaraDB for Redis console. For more information, see [Create a tag](https://help.aliyun.com/document_detail/118779.html).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        """
        @summary Adds specified tags to one or more ApsaraDB for Redis instances.
        
        @description If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        You can add up to 20 tags to each instance.
        You can add tags to up to 50 instances in each request.
        You can also add tags to instances in the ApsaraDB for Redis console. For more information, see [Create a tag](https://help.aliyun.com/document_detail/118779.html).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transform_instance_charge_type_with_options(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go or from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand relevant precautions and billing rules. For more information, see the following topics:
        [Change the billing method to subscription](https://help.aliyun.com/document_detail/54542.html).
        [Change the billing method to pay-as-you-go](https://help.aliyun.com/document_detail/211549.html).
        
        @param request: TransformInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='TransformInstanceChargeType',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_instance_charge_type_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go or from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand relevant precautions and billing rules. For more information, see the following topics:
        [Change the billing method to subscription](https://help.aliyun.com/document_detail/54542.html).
        [Change the billing method to pay-as-you-go](https://help.aliyun.com/document_detail/211549.html).
        
        @param request: TransformInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='TransformInstanceChargeType',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_instance_charge_type(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go or from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand relevant precautions and billing rules. For more information, see the following topics:
        [Change the billing method to subscription](https://help.aliyun.com/document_detail/54542.html).
        [Change the billing method to pay-as-you-go](https://help.aliyun.com/document_detail/211549.html).
        
        @param request: TransformInstanceChargeTypeRequest
        @return: TransformInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_instance_charge_type_with_options(request, runtime)

    async def transform_instance_charge_type_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go or from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand relevant precautions and billing rules. For more information, see the following topics:
        [Change the billing method to subscription](https://help.aliyun.com/document_detail/54542.html).
        [Change the billing method to pay-as-you-go](https://help.aliyun.com/document_detail/211549.html).
        
        @param request: TransformInstanceChargeTypeRequest
        @return: TransformInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transform_instance_charge_type_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from pay-as-you-go to subscription.
        
        @description For more information about how to change the billing method in the ApsaraDB for Redis console, see [Switch to subscription](https://help.aliyun.com/document_detail/54542.html).
        >  You cannot change the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go.
        
        @param request: TransformToPrePaidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformToPrePaidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='TransformToPrePaid',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from pay-as-you-go to subscription.
        
        @description For more information about how to change the billing method in the ApsaraDB for Redis console, see [Switch to subscription](https://help.aliyun.com/document_detail/54542.html).
        >  You cannot change the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go.
        
        @param request: TransformToPrePaidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformToPrePaidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
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
            action='TransformToPrePaid',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from pay-as-you-go to subscription.
        
        @description For more information about how to change the billing method in the ApsaraDB for Redis console, see [Switch to subscription](https://help.aliyun.com/document_detail/54542.html).
        >  You cannot change the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go.
        
        @param request: TransformToPrePaidRequest
        @return: TransformToPrePaidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for Redis instance from pay-as-you-go to subscription.
        
        @description For more information about how to change the billing method in the ApsaraDB for Redis console, see [Switch to subscription](https://help.aliyun.com/document_detail/54542.html).
        >  You cannot change the billing method of an ApsaraDB for Redis instance from subscription to pay-as-you-go.
        
        @param request: TransformToPrePaidRequest
        @return: TransformToPrePaidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

    def unlock_dbinstance_write_with_options(
        self,
        request: r_kvstore_20150101_models.UnlockDBInstanceWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UnlockDBInstanceWriteResponse:
        """
        @summary Removes the write lock from an instance. After the instance is unlocked, it supports both read and write operations.
        
        @param request: UnlockDBInstanceWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockDBInstanceWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UnlockDBInstanceWrite',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UnlockDBInstanceWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_dbinstance_write_with_options_async(
        self,
        request: r_kvstore_20150101_models.UnlockDBInstanceWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UnlockDBInstanceWriteResponse:
        """
        @summary Removes the write lock from an instance. After the instance is unlocked, it supports both read and write operations.
        
        @param request: UnlockDBInstanceWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockDBInstanceWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UnlockDBInstanceWrite',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UnlockDBInstanceWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_dbinstance_write(
        self,
        request: r_kvstore_20150101_models.UnlockDBInstanceWriteRequest,
    ) -> r_kvstore_20150101_models.UnlockDBInstanceWriteResponse:
        """
        @summary Removes the write lock from an instance. After the instance is unlocked, it supports both read and write operations.
        
        @param request: UnlockDBInstanceWriteRequest
        @return: UnlockDBInstanceWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_dbinstance_write_with_options(request, runtime)

    async def unlock_dbinstance_write_async(
        self,
        request: r_kvstore_20150101_models.UnlockDBInstanceWriteRequest,
    ) -> r_kvstore_20150101_models.UnlockDBInstanceWriteResponse:
        """
        @summary Removes the write lock from an instance. After the instance is unlocked, it supports both read and write operations.
        
        @param request: UnlockDBInstanceWriteRequest
        @return: UnlockDBInstanceWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_dbinstance_write_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more ApsaraDB for Redis instances.
        
        @description    You can remove up to 20 tags at a time.
        If a tag is removed from an instance and is not added to other instances, the tag is deleted.
        You can also remove tags from instances in the ApsaraDB for Redis console. For more information, see [Remove a tag](https://help.aliyun.com/document_detail/119157.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more ApsaraDB for Redis instances.
        
        @description    You can remove up to 20 tags at a time.
        If a tag is removed from an instance and is not added to other instances, the tag is deleted.
        You can also remove tags from instances in the ApsaraDB for Redis console. For more information, see [Remove a tag](https://help.aliyun.com/document_detail/119157.html).
        
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more ApsaraDB for Redis instances.
        
        @description    You can remove up to 20 tags at a time.
        If a tag is removed from an instance and is not added to other instances, the tag is deleted.
        You can also remove tags from instances in the ApsaraDB for Redis console. For more information, see [Remove a tag](https://help.aliyun.com/document_detail/119157.html).
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        """
        @summary Removes tags from one or more ApsaraDB for Redis instances.
        
        @description    You can remove up to 20 tags at a time.
        If a tag is removed from an instance and is not added to other instances, the tag is deleted.
        You can also remove tags from instances in the ApsaraDB for Redis console. For more information, see [Remove a tag](https://help.aliyun.com/document_detail/119157.html).
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
