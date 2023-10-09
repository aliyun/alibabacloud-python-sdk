# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20190916 import models as alikafka_20190916_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafka', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: alikafka_20190916_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: alikafka_20190916_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: alikafka_20190916_models.ChangeResourceGroupRequest,
    ) -> alikafka_20190916_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: alikafka_20190916_models.ChangeResourceGroupRequest,
    ) -> alikafka_20190916_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def convert_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertPostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ConvertPostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertPostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ConvertPostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_post_pay_order(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    async def convert_post_pay_order_async(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_post_pay_order_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
    ) -> alikafka_20190916_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
    ) -> alikafka_20190916_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: CreatePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostPayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: CreatePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostPayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_post_pay_order(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: CreatePostPayOrderRequest
        @return: CreatePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_post_pay_order_with_options(request, runtime)

    async def create_post_pay_order_async(
        self,
        request: alikafka_20190916_models.CreatePostPayOrderRequest,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: CreatePostPayOrderRequest
        @return: CreatePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_post_pay_order_with_options_async(request, runtime)

    def create_pre_pay_order_with_options(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](~~84737~~).
        *   If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param request: CreatePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrePayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pre_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](~~84737~~).
        *   If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param request: CreatePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrePayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePrePayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pre_pay_order(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](~~84737~~).
        *   If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param request: CreatePrePayOrderRequest
        @return: CreatePrePayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pre_pay_order_with_options(request, runtime)

    async def create_pre_pay_order_async(
        self,
        request: alikafka_20190916_models.CreatePrePayOrderRequest,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](~~84737~~).
        *   If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param request: CreatePrePayOrderRequest
        @return: CreatePrePayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pre_pay_order_with_options_async(request, runtime)

    def create_sasl_user_with_options(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sasl_user_with_options_async(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateSaslUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sasl_user(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    async def create_sasl_user_async(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sasl_user_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        """
        Each Alibaba Cloud account can call this operation up to once per second.
        *   The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compact_topic):
            query['CompactTopic'] = request.compact_topic
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.local_topic):
            query['LocalTopic'] = request.local_topic
        if not UtilClient.is_unset(request.min_insync_replicas):
            query['MinInsyncReplicas'] = request.min_insync_replicas
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        """
        Each Alibaba Cloud account can call this operation up to once per second.
        *   The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compact_topic):
            query['CompactTopic'] = request.compact_topic
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.local_topic):
            query['LocalTopic'] = request.local_topic
        if not UtilClient.is_unset(request.min_insync_replicas):
            query['MinInsyncReplicas'] = request.min_insync_replicas
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        """
        Each Alibaba Cloud account can call this operation up to once per second.
        *   The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        """
        Each Alibaba Cloud account can call this operation up to once per second.
        *   The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sasl_user_with_options(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sasl_user_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteSaslUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sasl_user(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    async def delete_sasl_user_async(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sasl_user_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAcls',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAcls',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acls(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_sasl_users_with_options(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSaslUsers',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeSaslUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sasl_users_with_options_async(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSaslUsers',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeSaslUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sasl_users(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    async def describe_sasl_users_async(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sasl_users_with_options_async(request, runtime)

    def get_all_instance_id_list_with_options(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllInstanceIdList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllInstanceIdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_instance_id_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllInstanceIdList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllInstanceIdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_instance_id_list(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_instance_id_list_with_options(request, runtime)

    async def get_all_instance_id_list_async(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_instance_id_list_with_options_async(request, runtime)

    def get_allowed_ip_list_with_options(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllowedIpList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllowedIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_allowed_ip_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllowedIpList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllowedIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_allowed_ip_list(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    async def get_allowed_ip_list_async(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_allowed_ip_list_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_list(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerProgress',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_progress_with_options_async(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerProgress',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_progress(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='GetInstanceList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='GetInstanceList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_list(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_quota_tip_with_options(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaTip',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetQuotaTipResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_tip_with_options_async(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaTip',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetQuotaTipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_tip(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quota_tip_with_options(request, runtime)

    async def get_quota_tip_async(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_tip_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_list_with_options_async(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_list(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicStatus',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_status_with_options_async(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicStatus',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_status(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_name(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_partition_num_with_options(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_partition_num):
            query['AddPartitionNum'] = request.add_partition_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPartitionNum',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyPartitionNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_partition_num_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_partition_num):
            query['AddPartitionNum'] = request.add_partition_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPartitionNum',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyPartitionNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_partition_num(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    async def modify_partition_num_async(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_partition_num_with_options_async(request, runtime)

    def modify_topic_remark_with_options(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTopicRemark',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyTopicRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_topic_remark_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTopicRemark',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyTopicRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_topic_remark(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    async def modify_topic_remark_async(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_topic_remark_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        """
        You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_instance):
            query['ForceDeleteInstance'] = request.force_delete_instance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        """
        You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_instance):
            query['ForceDeleteInstance'] = request.force_delete_instance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        """
        You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        """
        You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        """
        >  You can call this operation up to twice per second.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cross_zone):
            query['CrossZone'] = request.cross_zone
        if not UtilClient.is_unset(request.deploy_module):
            query['DeployModule'] = request.deploy_module
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_eip_inner):
            query['IsEipInner'] = request.is_eip_inner
        if not UtilClient.is_unset(request.is_force_selected_zones):
            query['IsForceSelectedZones'] = request.is_force_selected_zones
        if not UtilClient.is_unset(request.is_set_user_and_password):
            query['IsSetUserAndPassword'] = request.is_set_user_and_password
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notifier):
            query['Notifier'] = request.notifier
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group):
            query['SecurityGroup'] = request.security_group
        if not UtilClient.is_unset(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.user_phone_num):
            query['UserPhoneNum'] = request.user_phone_num
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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
            action='StartInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        """
        >  You can call this operation up to twice per second.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cross_zone):
            query['CrossZone'] = request.cross_zone
        if not UtilClient.is_unset(request.deploy_module):
            query['DeployModule'] = request.deploy_module
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_eip_inner):
            query['IsEipInner'] = request.is_eip_inner
        if not UtilClient.is_unset(request.is_force_selected_zones):
            query['IsForceSelectedZones'] = request.is_force_selected_zones
        if not UtilClient.is_unset(request.is_set_user_and_password):
            query['IsSetUserAndPassword'] = request.is_set_user_and_password
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notifier):
            query['Notifier'] = request.notifier
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group):
            query['SecurityGroup'] = request.security_group
        if not UtilClient.is_unset(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.user_phone_num):
            query['UserPhoneNum'] = request.user_phone_num
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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
            action='StartInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        """
        >  You can call this operation up to twice per second.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        """
        >  You can call this operation up to twice per second.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_allowed_ip_with_options(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_list_ip):
            query['AllowedListIp'] = request.allowed_list_ip
        if not UtilClient.is_unset(request.allowed_list_type):
            query['AllowedListType'] = request.allowed_list_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAllowedIp',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateAllowedIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_allowed_ip_with_options_async(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_list_ip):
            query['AllowedListIp'] = request.allowed_list_ip
        if not UtilClient.is_unset(request.allowed_list_type):
            query['AllowedListType'] = request.allowed_list_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAllowedIp',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateAllowedIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_allowed_ip(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    async def update_allowed_ip_async(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_allowed_ip_with_options_async(request, runtime)

    def update_consumer_offset_with_options(
        self,
        tmp_req: alikafka_20190916_models.UpdateConsumerOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateConsumerOffsetResponse:
        """
        You can call this operation to reset the consumer offsets of the subscribed topics of a consumer group. You can specify a timestamp or an offset to reset a consumer offset. You can implement the following features by configuring a combination of different parameters:
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        *   Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
        @param tmp_req: UpdateConsumerOffsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerOffsetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpdateConsumerOffsetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.offsets):
            request.offsets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.offsets, 'Offsets', 'json')
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offsets_shrink):
            query['Offsets'] = request.offsets_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConsumerOffset',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateConsumerOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_offset_with_options_async(
        self,
        tmp_req: alikafka_20190916_models.UpdateConsumerOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateConsumerOffsetResponse:
        """
        You can call this operation to reset the consumer offsets of the subscribed topics of a consumer group. You can specify a timestamp or an offset to reset a consumer offset. You can implement the following features by configuring a combination of different parameters:
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        *   Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
        @param tmp_req: UpdateConsumerOffsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerOffsetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpdateConsumerOffsetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.offsets):
            request.offsets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.offsets, 'Offsets', 'json')
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offsets_shrink):
            query['Offsets'] = request.offsets_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConsumerOffset',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateConsumerOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_offset(
        self,
        request: alikafka_20190916_models.UpdateConsumerOffsetRequest,
    ) -> alikafka_20190916_models.UpdateConsumerOffsetResponse:
        """
        You can call this operation to reset the consumer offsets of the subscribed topics of a consumer group. You can specify a timestamp or an offset to reset a consumer offset. You can implement the following features by configuring a combination of different parameters:
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        *   Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
        @param request: UpdateConsumerOffsetRequest
        @return: UpdateConsumerOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_consumer_offset_with_options(request, runtime)

    async def update_consumer_offset_async(
        self,
        request: alikafka_20190916_models.UpdateConsumerOffsetRequest,
    ) -> alikafka_20190916_models.UpdateConsumerOffsetResponse:
        """
        You can call this operation to reset the consumer offsets of the subscribed topics of a consumer group. You can specify a timestamp or an offset to reset a consumer offset. You can implement the following features by configuring a combination of different parameters:
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        *   Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        *   Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
        @param request: UpdateConsumerOffsetRequest
        @return: UpdateConsumerOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_consumer_offset_with_options_async(request, runtime)

    def update_instance_config_with_options(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        """
        ## *Permissions**\
        If a RAM user wants to call the **UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka:*:*:{instanceId}|
        
        @param request: UpdateInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceConfig',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_config_with_options_async(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        """
        ## *Permissions**\
        If a RAM user wants to call the **UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka:*:*:{instanceId}|
        
        @param request: UpdateInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceConfig',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_config(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        """
        ## *Permissions**\
        If a RAM user wants to call the **UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka:*:*:{instanceId}|
        
        @param request: UpdateInstanceConfigRequest
        @return: UpdateInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_config_with_options(request, runtime)

    async def update_instance_config_async(
        self,
        request: alikafka_20190916_models.UpdateInstanceConfigRequest,
    ) -> alikafka_20190916_models.UpdateInstanceConfigResponse:
        """
        ## *Permissions**\
        If a RAM user wants to call the **UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka:*:*:{instanceId}|
        
        @param request: UpdateInstanceConfigRequest
        @return: UpdateInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_config_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        """
        ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user call the **UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka:*:*:{instanceId}|
        ## **QPS limits**\
        You can send a maximum of two queries per second (QPS).
        
        @param request: UpgradeInstanceVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradeInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        """
        ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user call the **UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka:*:*:{instanceId}|
        ## **QPS limits**\
        You can send a maximum of two queries per second (QPS).
        
        @param request: UpgradeInstanceVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradeInstanceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        """
        ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user call the **UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka:*:*:{instanceId}|
        ## **QPS limits**\
        You can send a maximum of two queries per second (QPS).
        
        @param request: UpgradeInstanceVersionRequest
        @return: UpgradeInstanceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        """
        ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user call the **UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](~~185815~~).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka:*:*:{instanceId}|
        ## **QPS limits**\
        You can send a maximum of two queries per second (QPS).
        
        @param request: UpgradeInstanceVersionRequest
        @return: UpgradeInstanceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def upgrade_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: UpgradePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePostPayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_post_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: UpgradePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePostPayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_post_pay_order(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: UpgradePostPayOrderRequest
        @return: UpgradePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_post_pay_order_with_options(request, runtime)

    async def upgrade_post_pay_order_async(
        self,
        request: alikafka_20190916_models.UpgradePostPayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](~~84737~~).
        
        @param request: UpgradePostPayOrderRequest
        @return: UpgradePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_post_pay_order_with_options_async(request, runtime)

    def upgrade_pre_pay_order_with_options(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](~~84737~~).
        
        @param request: UpgradePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePrePayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_pre_pay_order_with_options_async(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](~~84737~~).
        
        @param request: UpgradePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePrePayOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePrePayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_pre_pay_order(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](~~84737~~).
        
        @param request: UpgradePrePayOrderRequest
        @return: UpgradePrePayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_pre_pay_order_with_options(request, runtime)

    async def upgrade_pre_pay_order_async(
        self,
        request: alikafka_20190916_models.UpgradePrePayOrderRequest,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](~~84737~~).
        
        @param request: UpgradePrePayOrderRequest
        @return: UpgradePrePayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_pre_pay_order_with_options_async(request, runtime)
