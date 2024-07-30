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
        """
        @summary Changes the resource group of an ApsaraMQ for Kafka instance.
        
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
        """
        @summary Changes the resource group of an ApsaraMQ for Kafka instance.
        
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
        """
        @summary Changes the resource group of an ApsaraMQ for Kafka instance.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: alikafka_20190916_models.ChangeResourceGroupRequest,
    ) -> alikafka_20190916_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group of an ApsaraMQ for Kafka instance.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def convert_post_pay_order_with_options(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        """
        @summary Changes the billing method of a Message Queue for Apache Kafka instance from pay-as-you-go to subscription.
        
        @param request: ConvertPostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPostPayOrderResponse
        """
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
        """
        @summary Changes the billing method of a Message Queue for Apache Kafka instance from pay-as-you-go to subscription.
        
        @param request: ConvertPostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPostPayOrderResponse
        """
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
        """
        @summary Changes the billing method of a Message Queue for Apache Kafka instance from pay-as-you-go to subscription.
        
        @param request: ConvertPostPayOrderRequest
        @return: ConvertPostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    async def convert_post_pay_order_async(
        self,
        request: alikafka_20190916_models.ConvertPostPayOrderRequest,
    ) -> alikafka_20190916_models.ConvertPostPayOrderResponse:
        """
        @summary Changes the billing method of a Message Queue for Apache Kafka instance from pay-as-you-go to subscription.
        
        @param request: ConvertPostPayOrderRequest
        @return: ConvertPostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_post_pay_order_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL).
        
        @param request: CreateAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Creates an access control list (ACL).
        
        @param request: CreateAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Creates an access control list (ACL).
        
        @param request: CreateAclRequest
        @return: CreateAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alikafka_20190916_models.CreateAclRequest,
    ) -> alikafka_20190916_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL).
        
        @param request: CreateAclRequest
        @return: CreateAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
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
        """
        @summary Creates a consumer group.
        
        @param request: CreateConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
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
        """
        @summary Creates a consumer group.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: alikafka_20190916_models.CreateConsumerGroupRequest,
    ) -> alikafka_20190916_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_post_pay_order_with_options(
        self,
        tmp_req: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        @summary Creates a pay-as-you-go ApsaraMQ for Kafka instance. Pay-as-you-go instances allow you to pay after you use the resources. You are charged for pay-as-you-go instances based on the actual resource usage. You can use pay-as-you-go instances in test scenarios or scenarios in which the peak traffic is uncertain.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: CreatePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostPayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreatePostPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
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
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
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
        tmp_req: alikafka_20190916_models.CreatePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePostPayOrderResponse:
        """
        @summary Creates a pay-as-you-go ApsaraMQ for Kafka instance. Pay-as-you-go instances allow you to pay after you use the resources. You are charged for pay-as-you-go instances based on the actual resource usage. You can use pay-as-you-go instances in test scenarios or scenarios in which the peak traffic is uncertain.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: CreatePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePostPayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreatePostPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
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
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
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
        @summary Creates a pay-as-you-go ApsaraMQ for Kafka instance. Pay-as-you-go instances allow you to pay after you use the resources. You are charged for pay-as-you-go instances based on the actual resource usage. You can use pay-as-you-go instances in test scenarios or scenarios in which the peak traffic is uncertain.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
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
        @summary Creates a pay-as-you-go ApsaraMQ for Kafka instance. Pay-as-you-go instances allow you to pay after you use the resources. You are charged for pay-as-you-go instances based on the actual resource usage. You can use pay-as-you-go instances in test scenarios or scenarios in which the peak traffic is uncertain.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param request: CreatePostPayOrderRequest
        @return: CreatePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_post_pay_order_with_options_async(request, runtime)

    def create_pre_pay_order_with_options(
        self,
        tmp_req: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        @summary Creates a subscription ApsaraMQ for Kafka instance. You can use subscription instances only after you pay for them. Subscription instances are suitable for long-term and stable business scenarios.
        
        @description    Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param tmp_req: CreatePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrePayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreatePrePayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.confluent_config):
            request.confluent_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
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
        tmp_req: alikafka_20190916_models.CreatePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreatePrePayOrderResponse:
        """
        @summary Creates a subscription ApsaraMQ for Kafka instance. You can use subscription instances only after you pay for them. Subscription instances are suitable for long-term and stable business scenarios.
        
        @description    Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
        @param tmp_req: CreatePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrePayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreatePrePayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.confluent_config):
            request.confluent_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
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
        @summary Creates a subscription ApsaraMQ for Kafka instance. You can use subscription instances only after you pay for them. Subscription instances are suitable for long-term and stable business scenarios.
        
        @description    Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
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
        @summary Creates a subscription ApsaraMQ for Kafka instance. You can use subscription instances only after you pay for them. Subscription instances are suitable for long-term and stable business scenarios.
        
        @description    Before you call this operation, make sure that you understand the billing methods and pricing of subscription ApsaraMQ for Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        If you create an ApsaraMQ for Kafka instance by calling this operation, the subscription duration is one month and the auto-renewal feature is enabled by default. The auto-renewal cycle is also one month. If you want to change the auto-renewal cycle or disable the auto-renewal feature, you can go to the [Renewal](https://renew.console.aliyun.com/#/ecs) page in the Alibaba Cloud Management Console.
        
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
        """
        @summary Creates a Simple Authentication and Security Layer (SASL) user.
        
        @param request: CreateSaslUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSaslUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mechanism):
            query['Mechanism'] = request.mechanism
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
        """
        @summary Creates a Simple Authentication and Security Layer (SASL) user.
        
        @param request: CreateSaslUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSaslUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mechanism):
            query['Mechanism'] = request.mechanism
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
        """
        @summary Creates a Simple Authentication and Security Layer (SASL) user.
        
        @param request: CreateSaslUserRequest
        @return: CreateSaslUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    async def create_sasl_user_async(
        self,
        request: alikafka_20190916_models.CreateSaslUserRequest,
    ) -> alikafka_20190916_models.CreateSaslUserResponse:
        """
        @summary Creates a Simple Authentication and Security Layer (SASL) user.
        
        @param request: CreateSaslUserRequest
        @return: CreateSaslUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sasl_user_with_options_async(request, runtime)

    def create_scheduled_scaling_rule_with_options(
        self,
        tmp_req: alikafka_20190916_models.CreateScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateScheduledScalingRuleResponse:
        """
        @summary Creates a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param tmp_req: CreateScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledScalingRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreateScheduledScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.weekly_types):
            request.weekly_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.weekly_types, 'WeeklyTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.duration_minutes):
            query['DurationMinutes'] = request.duration_minutes
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.first_scheduled_time):
            query['FirstScheduledTime'] = request.first_scheduled_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.reserved_pub_flow):
            query['ReservedPubFlow'] = request.reserved_pub_flow
        if not UtilClient.is_unset(request.reserved_sub_flow):
            query['ReservedSubFlow'] = request.reserved_sub_flow
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.weekly_types_shrink):
            query['WeeklyTypes'] = request.weekly_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledScalingRule',
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
            alikafka_20190916_models.CreateScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_scaling_rule_with_options_async(
        self,
        tmp_req: alikafka_20190916_models.CreateScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateScheduledScalingRuleResponse:
        """
        @summary Creates a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param tmp_req: CreateScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledScalingRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreateScheduledScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.weekly_types):
            request.weekly_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.weekly_types, 'WeeklyTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.duration_minutes):
            query['DurationMinutes'] = request.duration_minutes
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.first_scheduled_time):
            query['FirstScheduledTime'] = request.first_scheduled_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.reserved_pub_flow):
            query['ReservedPubFlow'] = request.reserved_pub_flow
        if not UtilClient.is_unset(request.reserved_sub_flow):
            query['ReservedSubFlow'] = request.reserved_sub_flow
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.weekly_types_shrink):
            query['WeeklyTypes'] = request.weekly_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledScalingRule',
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
            alikafka_20190916_models.CreateScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_scaling_rule(
        self,
        request: alikafka_20190916_models.CreateScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.CreateScheduledScalingRuleResponse:
        """
        @summary Creates a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: CreateScheduledScalingRuleRequest
        @return: CreateScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_scaling_rule_with_options(request, runtime)

    async def create_scheduled_scaling_rule_async(
        self,
        request: alikafka_20190916_models.CreateScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.CreateScheduledScalingRuleResponse:
        """
        @summary Creates a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: CreateScheduledScalingRuleRequest
        @return: CreateScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_scaling_rule_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: alikafka_20190916_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @description    Each Alibaba Cloud account can call this operation up to once per second.
        The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
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
        @summary Creates a topic.
        
        @description    Each Alibaba Cloud account can call this operation up to once per second.
        The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
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
        @summary Creates a topic.
        
        @description    Each Alibaba Cloud account can call this operation up to once per second.
        The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
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
        @summary Creates a topic.
        
        @description    Each Alibaba Cloud account can call this operation up to once per second.
        The maximum number of topics that you can create in an instance is determined by the specification of the instance.
        
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
        """
        @summary Deletes an access control list (ACL).
        
        @param request: DeleteAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Deletes an access control list (ACL).
        
        @param request: DeleteAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Deletes an access control list (ACL).
        
        @param request: DeleteAclRequest
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alikafka_20190916_models.DeleteAclRequest,
    ) -> alikafka_20190916_models.DeleteAclResponse:
        """
        @summary Deletes an access control list (ACL).
        
        @param request: DeleteAclRequest
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group from a specified Message Queue for Apache Kafka instance.
        
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
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
        """
        @summary Deletes a consumer group from a specified Message Queue for Apache Kafka instance.
        
        @param request: DeleteConsumerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
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
        """
        @summary Deletes a consumer group from a specified Message Queue for Apache Kafka instance.
        
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: alikafka_20190916_models.DeleteConsumerGroupRequest,
    ) -> alikafka_20190916_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a consumer group from a specified Message Queue for Apache Kafka instance.
        
        @param request: DeleteConsumerGroupRequest
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance. You can delete subscription and pay-as-you-go instances after you release them.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        """
        @summary Deletes an instance. You can delete subscription and pay-as-you-go instances after you release them.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        """
        @summary Deletes an instance. You can delete subscription and pay-as-you-go instances after you release them.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: alikafka_20190916_models.DeleteInstanceRequest,
    ) -> alikafka_20190916_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance. You can delete subscription and pay-as-you-go instances after you release them.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sasl_user_with_options(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        """
        @summary Deletes a Simple Authentication and Security Layer (SASL) user.
        
        @param request: DeleteSaslUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSaslUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mechanism):
            query['Mechanism'] = request.mechanism
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
        """
        @summary Deletes a Simple Authentication and Security Layer (SASL) user.
        
        @param request: DeleteSaslUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSaslUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mechanism):
            query['Mechanism'] = request.mechanism
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
        """
        @summary Deletes a Simple Authentication and Security Layer (SASL) user.
        
        @param request: DeleteSaslUserRequest
        @return: DeleteSaslUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    async def delete_sasl_user_async(
        self,
        request: alikafka_20190916_models.DeleteSaslUserRequest,
    ) -> alikafka_20190916_models.DeleteSaslUserResponse:
        """
        @summary Deletes a Simple Authentication and Security Layer (SASL) user.
        
        @param request: DeleteSaslUserRequest
        @return: DeleteSaslUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sasl_user_with_options_async(request, runtime)

    def delete_scheduled_scaling_rule_with_options(
        self,
        request: alikafka_20190916_models.DeleteScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteScheduledScalingRuleResponse:
        """
        @summary Deletes a scheduled scaling task for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instance.
        
        @param request: DeleteScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledScalingRule',
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
            alikafka_20190916_models.DeleteScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_scaling_rule_with_options_async(
        self,
        request: alikafka_20190916_models.DeleteScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteScheduledScalingRuleResponse:
        """
        @summary Deletes a scheduled scaling task for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instance.
        
        @param request: DeleteScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledScalingRule',
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
            alikafka_20190916_models.DeleteScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_scaling_rule(
        self,
        request: alikafka_20190916_models.DeleteScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.DeleteScheduledScalingRuleResponse:
        """
        @summary Deletes a scheduled scaling task for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instance.
        
        @param request: DeleteScheduledScalingRuleRequest
        @return: DeleteScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_scaling_rule_with_options(request, runtime)

    async def delete_scheduled_scaling_rule_async(
        self,
        request: alikafka_20190916_models.DeleteScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.DeleteScheduledScalingRuleResponse:
        """
        @summary Deletes a scheduled scaling task for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instance.
        
        @param request: DeleteScheduledScalingRuleRequest
        @return: DeleteScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_scaling_rule_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
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
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
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
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: alikafka_20190916_models.DeleteTopicRequest,
    ) -> alikafka_20190916_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        """
        @summary Queries access control lists (ACLs).
        
        @param request: DescribeAclsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAclsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Queries access control lists (ACLs).
        
        @param request: DescribeAclsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAclsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
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
        """
        @summary Queries access control lists (ACLs).
        
        @param request: DescribeAclsRequest
        @return: DescribeAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: alikafka_20190916_models.DescribeAclsRequest,
    ) -> alikafka_20190916_models.DescribeAclsResponse:
        """
        @summary Queries access control lists (ACLs).
        
        @param request: DescribeAclsRequest
        @return: DescribeAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_sasl_users_with_options(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        """
        @summary Queries Simple Authentication and Security Layer (SASL) users.
        
        @param request: DescribeSaslUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSaslUsersResponse
        """
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
        """
        @summary Queries Simple Authentication and Security Layer (SASL) users.
        
        @param request: DescribeSaslUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSaslUsersResponse
        """
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
        """
        @summary Queries Simple Authentication and Security Layer (SASL) users.
        
        @param request: DescribeSaslUsersRequest
        @return: DescribeSaslUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    async def describe_sasl_users_async(
        self,
        request: alikafka_20190916_models.DescribeSaslUsersRequest,
    ) -> alikafka_20190916_models.DescribeSaslUsersResponse:
        """
        @summary Queries Simple Authentication and Security Layer (SASL) users.
        
        @param request: DescribeSaslUsersRequest
        @return: DescribeSaslUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sasl_users_with_options_async(request, runtime)

    def enable_auto_group_creation_with_options(
        self,
        request: alikafka_20190916_models.EnableAutoGroupCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.EnableAutoGroupCreationResponse:
        """
        @summary Enables and disables the flexible group creation feature.
        
        @param request: EnableAutoGroupCreationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoGroupCreationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoGroupCreation',
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
            alikafka_20190916_models.EnableAutoGroupCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_group_creation_with_options_async(
        self,
        request: alikafka_20190916_models.EnableAutoGroupCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.EnableAutoGroupCreationResponse:
        """
        @summary Enables and disables the flexible group creation feature.
        
        @param request: EnableAutoGroupCreationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoGroupCreationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoGroupCreation',
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
            alikafka_20190916_models.EnableAutoGroupCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_group_creation(
        self,
        request: alikafka_20190916_models.EnableAutoGroupCreationRequest,
    ) -> alikafka_20190916_models.EnableAutoGroupCreationResponse:
        """
        @summary Enables and disables the flexible group creation feature.
        
        @param request: EnableAutoGroupCreationRequest
        @return: EnableAutoGroupCreationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_group_creation_with_options(request, runtime)

    async def enable_auto_group_creation_async(
        self,
        request: alikafka_20190916_models.EnableAutoGroupCreationRequest,
    ) -> alikafka_20190916_models.EnableAutoGroupCreationResponse:
        """
        @summary Enables and disables the flexible group creation feature.
        
        @param request: EnableAutoGroupCreationRequest
        @return: EnableAutoGroupCreationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_group_creation_with_options_async(request, runtime)

    def enable_auto_topic_creation_with_options(
        self,
        request: alikafka_20190916_models.EnableAutoTopicCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.EnableAutoTopicCreationResponse:
        """
        @summary Enables or disables the automatic topic creation feature, or changes the number of partitions in topics that are automatically created.
        
        @param request: EnableAutoTopicCreationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoTopicCreationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operate):
            query['Operate'] = request.operate
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoTopicCreation',
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
            alikafka_20190916_models.EnableAutoTopicCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_topic_creation_with_options_async(
        self,
        request: alikafka_20190916_models.EnableAutoTopicCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.EnableAutoTopicCreationResponse:
        """
        @summary Enables or disables the automatic topic creation feature, or changes the number of partitions in topics that are automatically created.
        
        @param request: EnableAutoTopicCreationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoTopicCreationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operate):
            query['Operate'] = request.operate
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoTopicCreation',
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
            alikafka_20190916_models.EnableAutoTopicCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_topic_creation(
        self,
        request: alikafka_20190916_models.EnableAutoTopicCreationRequest,
    ) -> alikafka_20190916_models.EnableAutoTopicCreationResponse:
        """
        @summary Enables or disables the automatic topic creation feature, or changes the number of partitions in topics that are automatically created.
        
        @param request: EnableAutoTopicCreationRequest
        @return: EnableAutoTopicCreationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_topic_creation_with_options(request, runtime)

    async def enable_auto_topic_creation_async(
        self,
        request: alikafka_20190916_models.EnableAutoTopicCreationRequest,
    ) -> alikafka_20190916_models.EnableAutoTopicCreationResponse:
        """
        @summary Enables or disables the automatic topic creation feature, or changes the number of partitions in topics that are automatically created.
        
        @param request: EnableAutoTopicCreationRequest
        @return: EnableAutoTopicCreationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_topic_creation_with_options_async(request, runtime)

    def get_all_instance_id_list_with_options(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        """
        @summary Queries the IDs of all instances in the current account.
        
        @param request: GetAllInstanceIdListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllInstanceIdListResponse
        """
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
        """
        @summary Queries the IDs of all instances in the current account.
        
        @param request: GetAllInstanceIdListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllInstanceIdListResponse
        """
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
        """
        @summary Queries the IDs of all instances in the current account.
        
        @param request: GetAllInstanceIdListRequest
        @return: GetAllInstanceIdListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_all_instance_id_list_with_options(request, runtime)

    async def get_all_instance_id_list_async(
        self,
        request: alikafka_20190916_models.GetAllInstanceIdListRequest,
    ) -> alikafka_20190916_models.GetAllInstanceIdListResponse:
        """
        @summary Queries the IDs of all instances in the current account.
        
        @param request: GetAllInstanceIdListRequest
        @return: GetAllInstanceIdListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_all_instance_id_list_with_options_async(request, runtime)

    def get_allowed_ip_list_with_options(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        """
        @summary Queries the IP address whitelist.
        
        @param request: GetAllowedIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllowedIpListResponse
        """
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
        """
        @summary Queries the IP address whitelist.
        
        @param request: GetAllowedIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAllowedIpListResponse
        """
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
        """
        @summary Queries the IP address whitelist.
        
        @param request: GetAllowedIpListRequest
        @return: GetAllowedIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    async def get_allowed_ip_list_async(
        self,
        request: alikafka_20190916_models.GetAllowedIpListRequest,
    ) -> alikafka_20190916_models.GetAllowedIpListResponse:
        """
        @summary Queries the IP address whitelist.
        
        @param request: GetAllowedIpListRequest
        @return: GetAllowedIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_allowed_ip_list_with_options_async(request, runtime)

    def get_auto_scaling_configuration_with_options(
        self,
        request: alikafka_20190916_models.GetAutoScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAutoScalingConfigurationResponse:
        """
        @summary Queries the configurations of the scheduled scaling rule of a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)*This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: GetAutoScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingConfigurationResponse
        """
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
            action='GetAutoScalingConfiguration',
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
            alikafka_20190916_models.GetAutoScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_configuration_with_options_async(
        self,
        request: alikafka_20190916_models.GetAutoScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetAutoScalingConfigurationResponse:
        """
        @summary Queries the configurations of the scheduled scaling rule of a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)*This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: GetAutoScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingConfigurationResponse
        """
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
            action='GetAutoScalingConfiguration',
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
            alikafka_20190916_models.GetAutoScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_configuration(
        self,
        request: alikafka_20190916_models.GetAutoScalingConfigurationRequest,
    ) -> alikafka_20190916_models.GetAutoScalingConfigurationResponse:
        """
        @summary Queries the configurations of the scheduled scaling rule of a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)*This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: GetAutoScalingConfigurationRequest
        @return: GetAutoScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_configuration_with_options(request, runtime)

    async def get_auto_scaling_configuration_async(
        self,
        request: alikafka_20190916_models.GetAutoScalingConfigurationRequest,
    ) -> alikafka_20190916_models.GetAutoScalingConfigurationResponse:
        """
        @summary Queries the configurations of the scheduled scaling rule of a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)*This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: GetAutoScalingConfigurationRequest
        @return: GetAutoScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_configuration_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        """
        @summary Queries one or more consumer groups in a specified Message Queue for Apache Kafka instance.
        
        @param request: GetConsumerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
        """
        @summary Queries one or more consumer groups in a specified Message Queue for Apache Kafka instance.
        
        @param request: GetConsumerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
        """
        @summary Queries one or more consumer groups in a specified Message Queue for Apache Kafka instance.
        
        @param request: GetConsumerListRequest
        @return: GetConsumerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: alikafka_20190916_models.GetConsumerListRequest,
    ) -> alikafka_20190916_models.GetConsumerListResponse:
        """
        @summary Queries one or more consumer groups in a specified Message Queue for Apache Kafka instance.
        
        @param request: GetConsumerListRequest
        @return: GetConsumerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        """
        @summary Queries the consumer progress of a consumer group.
        
        @param request: GetConsumerProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.hide_last_timestamp):
            query['HideLastTimestamp'] = request.hide_last_timestamp
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
        """
        @summary Queries the consumer progress of a consumer group.
        
        @param request: GetConsumerProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.hide_last_timestamp):
            query['HideLastTimestamp'] = request.hide_last_timestamp
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
        """
        @summary Queries the consumer progress of a consumer group.
        
        @param request: GetConsumerProgressRequest
        @return: GetConsumerProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: alikafka_20190916_models.GetConsumerProgressRequest,
    ) -> alikafka_20190916_models.GetConsumerProgressResponse:
        """
        @summary Queries the consumer progress of a consumer group.
        
        @param request: GetConsumerProgressRequest
        @return: GetConsumerProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        """
        @summary Queries the information about instances in a specified region.
        
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
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
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
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
        """
        @summary Queries the information about instances in a specified region.
        
        @param request: GetInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceListResponse
        """
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
        if not UtilClient.is_unset(request.series):
            query['Series'] = request.series
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
        """
        @summary Queries the information about instances in a specified region.
        
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: alikafka_20190916_models.GetInstanceListRequest,
    ) -> alikafka_20190916_models.GetInstanceListResponse:
        """
        @summary Queries the information about instances in a specified region.
        
        @param request: GetInstanceListRequest
        @return: GetInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_quota_tip_with_options(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        """
        @summary Queries the used quota of topics and partitions.
        
        @param request: GetQuotaTipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaTipResponse
        """
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
        """
        @summary Queries the used quota of topics and partitions.
        
        @param request: GetQuotaTipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaTipResponse
        """
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
        """
        @summary Queries the used quota of topics and partitions.
        
        @param request: GetQuotaTipRequest
        @return: GetQuotaTipResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_tip_with_options(request, runtime)

    async def get_quota_tip_async(
        self,
        request: alikafka_20190916_models.GetQuotaTipRequest,
    ) -> alikafka_20190916_models.GetQuotaTipResponse:
        """
        @summary Queries the used quota of topics and partitions.
        
        @param request: GetQuotaTipRequest
        @return: GetQuotaTipResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_tip_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        """
        @summary Queries the information about a topic.
        
        @param request: GetTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicListResponse
        """
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
        """
        @summary Queries the information about a topic.
        
        @param request: GetTopicListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicListResponse
        """
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
        """
        @summary Queries the information about a topic.
        
        @param request: GetTopicListRequest
        @return: GetTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: alikafka_20190916_models.GetTopicListRequest,
    ) -> alikafka_20190916_models.GetTopicListResponse:
        """
        @summary Queries the information about a topic.
        
        @param request: GetTopicListRequest
        @return: GetTopicListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        """
        @summary Queries the messaging status of a topic.
        
        @param request: GetTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicStatusResponse
        """
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
        """
        @summary Queries the messaging status of a topic.
        
        @param request: GetTopicStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicStatusResponse
        """
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
        """
        @summary Queries the messaging status of a topic.
        
        @param request: GetTopicStatusRequest
        @return: GetTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: alikafka_20190916_models.GetTopicStatusRequest,
    ) -> alikafka_20190916_models.GetTopicStatusResponse:
        """
        @summary Queries the messaging status of a topic.
        
        @param request: GetTopicStatusRequest
        @return: GetTopicStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)

    def get_topic_subscribe_status_with_options(
        self,
        request: alikafka_20190916_models.GetTopicSubscribeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicSubscribeStatusResponse:
        """
        @summary Queries the information about the groups that subscribe to a topic.
        
        @param request: GetTopicSubscribeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSubscribeStatusResponse
        """
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
            action='GetTopicSubscribeStatus',
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
            alikafka_20190916_models.GetTopicSubscribeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_subscribe_status_with_options_async(
        self,
        request: alikafka_20190916_models.GetTopicSubscribeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.GetTopicSubscribeStatusResponse:
        """
        @summary Queries the information about the groups that subscribe to a topic.
        
        @param request: GetTopicSubscribeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSubscribeStatusResponse
        """
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
            action='GetTopicSubscribeStatus',
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
            alikafka_20190916_models.GetTopicSubscribeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_subscribe_status(
        self,
        request: alikafka_20190916_models.GetTopicSubscribeStatusRequest,
    ) -> alikafka_20190916_models.GetTopicSubscribeStatusResponse:
        """
        @summary Queries the information about the groups that subscribe to a topic.
        
        @param request: GetTopicSubscribeStatusRequest
        @return: GetTopicSubscribeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_subscribe_status_with_options(request, runtime)

    async def get_topic_subscribe_status_async(
        self,
        request: alikafka_20190916_models.GetTopicSubscribeStatusRequest,
    ) -> alikafka_20190916_models.GetTopicSubscribeStatusResponse:
        """
        @summary Queries the information about the groups that subscribe to a topic.
        
        @param request: GetTopicSubscribeStatusRequest
        @return: GetTopicSubscribeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_subscribe_status_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
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
        """
        @summary Queries the tags that are attached to a specified resource.
        
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
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alikafka_20190916_models.ListTagResourcesRequest,
    ) -> alikafka_20190916_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        """
        @summary Changes the name of an ApsaraMQ for Kafka instance. After you deploy an instance, you can call this operation to change the name of the instance.
        
        @param request: ModifyInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNameResponse
        """
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
        """
        @summary Changes the name of an ApsaraMQ for Kafka instance. After you deploy an instance, you can call this operation to change the name of the instance.
        
        @param request: ModifyInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNameResponse
        """
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
        """
        @summary Changes the name of an ApsaraMQ for Kafka instance. After you deploy an instance, you can call this operation to change the name of the instance.
        
        @param request: ModifyInstanceNameRequest
        @return: ModifyInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: alikafka_20190916_models.ModifyInstanceNameRequest,
    ) -> alikafka_20190916_models.ModifyInstanceNameResponse:
        """
        @summary Changes the name of an ApsaraMQ for Kafka instance. After you deploy an instance, you can call this operation to change the name of the instance.
        
        @param request: ModifyInstanceNameRequest
        @return: ModifyInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_partition_num_with_options(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        """
        @summary Changes the number of partitions in a topic.
        
        @param request: ModifyPartitionNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPartitionNumResponse
        """
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
        """
        @summary Changes the number of partitions in a topic.
        
        @param request: ModifyPartitionNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPartitionNumResponse
        """
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
        """
        @summary Changes the number of partitions in a topic.
        
        @param request: ModifyPartitionNumRequest
        @return: ModifyPartitionNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    async def modify_partition_num_async(
        self,
        request: alikafka_20190916_models.ModifyPartitionNumRequest,
    ) -> alikafka_20190916_models.ModifyPartitionNumResponse:
        """
        @summary Changes the number of partitions in a topic.
        
        @param request: ModifyPartitionNumRequest
        @return: ModifyPartitionNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_partition_num_with_options_async(request, runtime)

    def modify_scheduled_scaling_rule_with_options(
        self,
        request: alikafka_20190916_models.ModifyScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyScheduledScalingRuleResponse:
        """
        @summary Modifies a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: ModifyScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledScalingRule',
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
            alikafka_20190916_models.ModifyScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_scaling_rule_with_options_async(
        self,
        request: alikafka_20190916_models.ModifyScheduledScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyScheduledScalingRuleResponse:
        """
        @summary Modifies a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: ModifyScheduledScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledScalingRule',
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
            alikafka_20190916_models.ModifyScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_scaling_rule(
        self,
        request: alikafka_20190916_models.ModifyScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.ModifyScheduledScalingRuleResponse:
        """
        @summary Modifies a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: ModifyScheduledScalingRuleRequest
        @return: ModifyScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_scaling_rule_with_options(request, runtime)

    async def modify_scheduled_scaling_rule_async(
        self,
        request: alikafka_20190916_models.ModifyScheduledScalingRuleRequest,
    ) -> alikafka_20190916_models.ModifyScheduledScalingRuleResponse:
        """
        @summary Modifies a scheduled scaling rule for a serverless ApsaraMQ for Kafka V3 instance.
        
        @description ###### [](#-v3-serverless-)This operation is supported only by serverless ApsaraMQ for Kafka V3 instances.
        
        @param request: ModifyScheduledScalingRuleRequest
        @return: ModifyScheduledScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduled_scaling_rule_with_options_async(request, runtime)

    def modify_topic_remark_with_options(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        """
        @summary Modifies the description of a topic.
        
        @param request: ModifyTopicRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTopicRemarkResponse
        """
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
        """
        @summary Modifies the description of a topic.
        
        @param request: ModifyTopicRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTopicRemarkResponse
        """
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
        """
        @summary Modifies the description of a topic.
        
        @param request: ModifyTopicRemarkRequest
        @return: ModifyTopicRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    async def modify_topic_remark_async(
        self,
        request: alikafka_20190916_models.ModifyTopicRemarkRequest,
    ) -> alikafka_20190916_models.ModifyTopicRemarkResponse:
        """
        @summary Modifies the description of a topic.
        
        @param request: ModifyTopicRemarkRequest
        @return: ModifyTopicRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_topic_remark_with_options_async(request, runtime)

    def query_message_with_options(
        self,
        request: alikafka_20190916_models.QueryMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.QueryMessageResponse:
        """
        @summary Queries messages stored in a topic. You can query messages by creation time or offset.
        
        @param request: QueryMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessage',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.QueryMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_with_options_async(
        self,
        request: alikafka_20190916_models.QueryMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.QueryMessageResponse:
        """
        @summary Queries messages stored in a topic. You can query messages by creation time or offset.
        
        @param request: QueryMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessage',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.QueryMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message(
        self,
        request: alikafka_20190916_models.QueryMessageRequest,
    ) -> alikafka_20190916_models.QueryMessageResponse:
        """
        @summary Queries messages stored in a topic. You can query messages by creation time or offset.
        
        @param request: QueryMessageRequest
        @return: QueryMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_message_with_options(request, runtime)

    async def query_message_async(
        self,
        request: alikafka_20190916_models.QueryMessageRequest,
    ) -> alikafka_20190916_models.QueryMessageResponse:
        """
        @summary Queries messages stored in a topic. You can query messages by creation time or offset.
        
        @param request: QueryMessageRequest
        @return: QueryMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_message_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: alikafka_20190916_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReleaseInstanceResponse:
        """
        @summary Releases a pay-as-you-go instance.
        
        @description You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
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
        @summary Releases a pay-as-you-go instance.
        
        @description You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
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
        @summary Releases a pay-as-you-go instance.
        
        @description You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
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
        @summary Releases a pay-as-you-go instance.
        
        @description You cannot call this operation to release a subscription Message Queue for Apache Kafka instance.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def reopen_instance_with_options(
        self,
        request: alikafka_20190916_models.ReopenInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReopenInstanceResponse:
        """
        @summary Enables an ApsaraMQ for Kafka instance.
        
        @description You can call this operation only if your instance is in the Stopped state.
        
        @param request: ReopenInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReopenInstanceResponse
        """
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
            action='ReopenInstance',
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
            alikafka_20190916_models.ReopenInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reopen_instance_with_options_async(
        self,
        request: alikafka_20190916_models.ReopenInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.ReopenInstanceResponse:
        """
        @summary Enables an ApsaraMQ for Kafka instance.
        
        @description You can call this operation only if your instance is in the Stopped state.
        
        @param request: ReopenInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReopenInstanceResponse
        """
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
            action='ReopenInstance',
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
            alikafka_20190916_models.ReopenInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reopen_instance(
        self,
        request: alikafka_20190916_models.ReopenInstanceRequest,
    ) -> alikafka_20190916_models.ReopenInstanceResponse:
        """
        @summary Enables an ApsaraMQ for Kafka instance.
        
        @description You can call this operation only if your instance is in the Stopped state.
        
        @param request: ReopenInstanceRequest
        @return: ReopenInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reopen_instance_with_options(request, runtime)

    async def reopen_instance_async(
        self,
        request: alikafka_20190916_models.ReopenInstanceRequest,
    ) -> alikafka_20190916_models.ReopenInstanceResponse:
        """
        @summary Enables an ApsaraMQ for Kafka instance.
        
        @description You can call this operation only if your instance is in the Stopped state.
        
        @param request: ReopenInstanceRequest
        @return: ReopenInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reopen_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: alikafka_20190916_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StartInstanceResponse:
        """
        @summary Deploys an ApsaraMQ for Kafka instance. You must purchase and deploy an ApsaraMQ for Kafka instance before you can use the instance to send and receive messages.
        
        @description >  You can call this operation up to twice per second.
        
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
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
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
        @summary Deploys an ApsaraMQ for Kafka instance. You must purchase and deploy an ApsaraMQ for Kafka instance before you can use the instance to send and receive messages.
        
        @description >  You can call this operation up to twice per second.
        
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
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
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
        @summary Deploys an ApsaraMQ for Kafka instance. You must purchase and deploy an ApsaraMQ for Kafka instance before you can use the instance to send and receive messages.
        
        @description >  You can call this operation up to twice per second.
        
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
        @summary Deploys an ApsaraMQ for Kafka instance. You must purchase and deploy an ApsaraMQ for Kafka instance before you can use the instance to send and receive messages.
        
        @description >  You can call this operation up to twice per second.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: alikafka_20190916_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StopInstanceResponse:
        """
        @summary Stops an ApsaraMQ for Kafka instance.
        
        @description You cannot stop a subscription ApsaraMQ for Kafka instance. If you want to stop a subscription ApsaraMQ for Kafka instance, submit a ticket.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
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
            action='StopInstance',
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
            alikafka_20190916_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: alikafka_20190916_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.StopInstanceResponse:
        """
        @summary Stops an ApsaraMQ for Kafka instance.
        
        @description You cannot stop a subscription ApsaraMQ for Kafka instance. If you want to stop a subscription ApsaraMQ for Kafka instance, submit a ticket.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
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
            action='StopInstance',
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
            alikafka_20190916_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: alikafka_20190916_models.StopInstanceRequest,
    ) -> alikafka_20190916_models.StopInstanceResponse:
        """
        @summary Stops an ApsaraMQ for Kafka instance.
        
        @description You cannot stop a subscription ApsaraMQ for Kafka instance. If you want to stop a subscription ApsaraMQ for Kafka instance, submit a ticket.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: alikafka_20190916_models.StopInstanceRequest,
    ) -> alikafka_20190916_models.StopInstanceResponse:
        """
        @summary Stops an ApsaraMQ for Kafka instance.
        
        @description You cannot stop a subscription ApsaraMQ for Kafka instance. If you want to stop a subscription ApsaraMQ for Kafka instance, submit a ticket.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        """
        @summary Attaches a tag to a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Attaches a tag to a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Attaches a tag to a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alikafka_20190916_models.TagResourcesRequest,
    ) -> alikafka_20190916_models.TagResourcesResponse:
        """
        @summary Attaches a tag to a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        """
        @summary Detaches tags from a specified resource.
        
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
        """
        @summary Detaches tags from a specified resource.
        
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
        """
        @summary Detaches tags from a specified resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: alikafka_20190916_models.UntagResourcesRequest,
    ) -> alikafka_20190916_models.UntagResourcesResponse:
        """
        @summary Detaches tags from a specified resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_allowed_ip_with_options(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        """
        @summary Updates the IP address whitelist of an ApsaraMQ for Kafka instance. Only IP addresses and ports that are configured in the IP address whitelist of an instance can access the instance.
        
        @param request: UpdateAllowedIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAllowedIpResponse
        """
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
        """
        @summary Updates the IP address whitelist of an ApsaraMQ for Kafka instance. Only IP addresses and ports that are configured in the IP address whitelist of an instance can access the instance.
        
        @param request: UpdateAllowedIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAllowedIpResponse
        """
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
        """
        @summary Updates the IP address whitelist of an ApsaraMQ for Kafka instance. Only IP addresses and ports that are configured in the IP address whitelist of an instance can access the instance.
        
        @param request: UpdateAllowedIpRequest
        @return: UpdateAllowedIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    async def update_allowed_ip_async(
        self,
        request: alikafka_20190916_models.UpdateAllowedIpRequest,
    ) -> alikafka_20190916_models.UpdateAllowedIpResponse:
        """
        @summary Updates the IP address whitelist of an ApsaraMQ for Kafka instance. Only IP addresses and ports that are configured in the IP address whitelist of an instance can access the instance.
        
        @param request: UpdateAllowedIpRequest
        @return: UpdateAllowedIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_allowed_ip_with_options_async(request, runtime)

    def update_consumer_offset_with_options(
        self,
        tmp_req: alikafka_20190916_models.UpdateConsumerOffsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateConsumerOffsetResponse:
        """
        @summary Resets the consumer offsets of the subscribed topics of a consumer group.
        
        @description You can call this operation to reset the consumer offset of a specific consumer group. You can use the timestamp or offset parameter to reset the consumer offset of a consumer group. You can implement the following features by configuring a combination of different parameters:
        Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
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
        @summary Resets the consumer offsets of the subscribed topics of a consumer group.
        
        @description You can call this operation to reset the consumer offset of a specific consumer group. You can use the timestamp or offset parameter to reset the consumer offset of a consumer group. You can implement the following features by configuring a combination of different parameters:
        Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
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
        @summary Resets the consumer offsets of the subscribed topics of a consumer group.
        
        @description You can call this operation to reset the consumer offset of a specific consumer group. You can use the timestamp or offset parameter to reset the consumer offset of a consumer group. You can implement the following features by configuring a combination of different parameters:
        Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
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
        @summary Resets the consumer offsets of the subscribed topics of a consumer group.
        
        @description You can call this operation to reset the consumer offset of a specific consumer group. You can use the timestamp or offset parameter to reset the consumer offset of a consumer group. You can implement the following features by configuring a combination of different parameters:
        Reset the consumer offsets of one or all subscribed topics of a consumer group to the latest offset. This way, you can consume messages in the topics from the latest offset.
        Reset the consumer offsets of one or all subscribed topics of a consumer group to a specific point in time. This way, you can consume messages in the topics from the specified point in time.
        Reset the consumer offset of one subscribed topic of a consumer group to a specific offset in a specific partition. This way, you can consume messages from the specified offset in the specified partition.
        
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
        @summary Modifies the configurations of an ApsaraMQ for Kafka instance. ApsaraMQ for Kafka allows you to modify the configurations of an instance, including the access control list (ACL) feature, the Secure Sockets Layer (SSL) feature, the message retention period, and the maximum message size.
        
        @description ## *Permissions**\
        If a RAM user wants to call the *UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka::*:{instanceId}|
        
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
        @summary Modifies the configurations of an ApsaraMQ for Kafka instance. ApsaraMQ for Kafka allows you to modify the configurations of an instance, including the access control list (ACL) feature, the Secure Sockets Layer (SSL) feature, the message retention period, and the maximum message size.
        
        @description ## *Permissions**\
        If a RAM user wants to call the *UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka::*:{instanceId}|
        
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
        @summary Modifies the configurations of an ApsaraMQ for Kafka instance. ApsaraMQ for Kafka allows you to modify the configurations of an instance, including the access control list (ACL) feature, the Secure Sockets Layer (SSL) feature, the message retention period, and the maximum message size.
        
        @description ## *Permissions**\
        If a RAM user wants to call the *UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka::*:{instanceId}|
        
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
        @summary Modifies the configurations of an ApsaraMQ for Kafka instance. ApsaraMQ for Kafka allows you to modify the configurations of an instance, including the access control list (ACL) feature, the Secure Sockets Layer (SSL) feature, the message retention period, and the maximum message size.
        
        @description ## *Permissions**\
        If a RAM user wants to call the *UpdateInstanceConfig** operation, the RAM user must be granted the required permissions. For more information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpdateInstanceConfig|alikafka: UpdateInstance|acs:alikafka::*:{instanceId}|
        
        @param request: UpdateInstanceConfigRequest
        @return: UpdateInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_config_with_options_async(request, runtime)

    def update_topic_config_with_options(
        self,
        request: alikafka_20190916_models.UpdateTopicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateTopicConfigResponse:
        """
        @summary Modifies the configurations of a topic. After you create a topic, you can modify the message retention period and maximum message size of the topic.
        
        @param request: UpdateTopicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTopicConfig',
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
            alikafka_20190916_models.UpdateTopicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_topic_config_with_options_async(
        self,
        request: alikafka_20190916_models.UpdateTopicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpdateTopicConfigResponse:
        """
        @summary Modifies the configurations of a topic. After you create a topic, you can modify the message retention period and maximum message size of the topic.
        
        @param request: UpdateTopicConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTopicConfig',
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
            alikafka_20190916_models.UpdateTopicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_topic_config(
        self,
        request: alikafka_20190916_models.UpdateTopicConfigRequest,
    ) -> alikafka_20190916_models.UpdateTopicConfigResponse:
        """
        @summary Modifies the configurations of a topic. After you create a topic, you can modify the message retention period and maximum message size of the topic.
        
        @param request: UpdateTopicConfigRequest
        @return: UpdateTopicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_topic_config_with_options(request, runtime)

    async def update_topic_config_async(
        self,
        request: alikafka_20190916_models.UpdateTopicConfigRequest,
    ) -> alikafka_20190916_models.UpdateTopicConfigResponse:
        """
        @summary Modifies the configurations of a topic. After you create a topic, you can modify the message retention period and maximum message size of the topic.
        
        @param request: UpdateTopicConfigRequest
        @return: UpdateTopicConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_topic_config_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: alikafka_20190916_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradeInstanceVersionResponse:
        """
        @summary Updates the version of an instance.
        
        @description ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user calls the *UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka::*:{instanceId}|
        ## *QPS limits**\
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
        @summary Updates the version of an instance.
        
        @description ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user calls the *UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka::*:{instanceId}|
        ## *QPS limits**\
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
        @summary Updates the version of an instance.
        
        @description ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user calls the *UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka::*:{instanceId}|
        ## *QPS limits**\
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
        @summary Updates the version of an instance.
        
        @description ## *Permissions**\
        A RAM user must be granted the required permissions before the RAM user calls the *UpgradeInstanceVersion** operation. For information about how to grant permissions, see [RAM policies](https://help.aliyun.com/document_detail/185815.html).
        |API|Action|Resource|
        |---|---|---|
        |UpgradeInstanceVersion|UpdateInstance|acs:alikafka::*:{instanceId}|
        ## *QPS limits**\
        You can send a maximum of two queries per second (QPS).
        
        @param request: UpgradeInstanceVersionRequest
        @return: UpgradeInstanceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def upgrade_post_pay_order_with_options(
        self,
        tmp_req: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        @summary Upgrades a pay-as-you-go ApsaraMQ for Kafka instance.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: UpgradePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePostPayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpgradePostPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
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
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
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
        tmp_req: alikafka_20190916_models.UpgradePostPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePostPayOrderResponse:
        """
        @summary Upgrades a pay-as-you-go ApsaraMQ for Kafka instance.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: UpgradePostPayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePostPayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpgradePostPayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
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
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
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
        @summary Upgrades a pay-as-you-go ApsaraMQ for Kafka instance.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
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
        @summary Upgrades a pay-as-you-go ApsaraMQ for Kafka instance.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of pay-as-you-go Message Queue for Apache Kafka instances. For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        
        @param request: UpgradePostPayOrderRequest
        @return: UpgradePostPayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_post_pay_order_with_options_async(request, runtime)

    def upgrade_pre_pay_order_with_options(
        self,
        tmp_req: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        @summary Upgrades a Message Queue for Apache Kafka instance that uses the subscription billing method.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: UpgradePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePrePayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpgradePrePayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.confluent_config):
            request.confluent_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
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
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
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
        tmp_req: alikafka_20190916_models.UpgradePrePayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alikafka_20190916_models.UpgradePrePayOrderResponse:
        """
        @summary Upgrades a Message Queue for Apache Kafka instance that uses the subscription billing method.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        
        @param tmp_req: UpgradePrePayOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradePrePayOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.UpgradePrePayOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.confluent_config):
            request.confluent_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
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
        if not UtilClient.is_unset(request.paid_type):
            query['PaidType'] = request.paid_type
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
        @summary Upgrades a Message Queue for Apache Kafka instance that uses the subscription billing method.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        
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
        @summary Upgrades a Message Queue for Apache Kafka instance that uses the subscription billing method.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of subscription Message Queue for Apache Kafka instances. For more information, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        
        @param request: UpgradePrePayOrderRequest
        @return: UpgradePrePayOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_pre_pay_order_with_options_async(request, runtime)
