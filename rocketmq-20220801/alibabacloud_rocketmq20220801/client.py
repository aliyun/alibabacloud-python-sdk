# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rocketmq20220801 import models as rocket_mq20220801_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('rocketmq', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: rocket_mq20220801_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a ApsaraMQ for RocketMQ instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: rocket_mq20220801_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a ApsaraMQ for RocketMQ instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: rocket_mq20220801_models.ChangeResourceGroupRequest,
    ) -> rocket_mq20220801_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a ApsaraMQ for RocketMQ instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: rocket_mq20220801_models.ChangeResourceGroupRequest,
    ) -> rocket_mq20220801_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a ApsaraMQ for RocketMQ instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.CreateConsumerGroupRequest,
    ) -> rocket_mq20220801_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def create_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.CreateConsumerGroupRequest,
    ) -> rocket_mq20220801_models.CreateConsumerGroupResponse:
        """
        @summary Creates a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: rocket_mq20220801_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraMQ for RocketMQ 5.x instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['periodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series_code):
            body['seriesCode'] = request.series_code
        if not UtilClient.is_unset(request.service_code):
            body['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.sub_series_code):
            body['subSeriesCode'] = request.sub_series_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: rocket_mq20220801_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraMQ for RocketMQ 5.x instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['periodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series_code):
            body['seriesCode'] = request.series_code
        if not UtilClient.is_unset(request.service_code):
            body['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.sub_series_code):
            body['subSeriesCode'] = request.sub_series_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: rocket_mq20220801_models.CreateInstanceRequest,
    ) -> rocket_mq20220801_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraMQ for RocketMQ 5.x instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: rocket_mq20220801_models.CreateInstanceRequest,
    ) -> rocket_mq20220801_models.CreateInstanceResponse:
        """
        @summary Creates an ApsaraMQ for RocketMQ 5.x instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_account_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceAccountResponse:
        """
        @summary 创建访问控制acl用户
        
        @param request: CreateInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_account_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceAccountResponse:
        """
        @summary 创建访问控制acl用户
        
        @param request: CreateInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_account(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceAccountRequest,
    ) -> rocket_mq20220801_models.CreateInstanceAccountResponse:
        """
        @summary 创建访问控制acl用户
        
        @param request: CreateInstanceAccountRequest
        @return: CreateInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_account_with_options(instance_id, request, headers, runtime)

    async def create_instance_account_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceAccountRequest,
    ) -> rocket_mq20220801_models.CreateInstanceAccountResponse:
        """
        @summary 创建访问控制acl用户
        
        @param request: CreateInstanceAccountRequest
        @return: CreateInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_account_with_options_async(instance_id, request, headers, runtime)

    def create_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.CreateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceAclResponse:
        """
        @summary 创建访问控制acl数据
        
        @param request: CreateInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceAclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.decision):
            body['decision'] = request.decision
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not UtilClient.is_unset(request.resource_name):
            body['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.CreateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceAclResponse:
        """
        @summary 创建访问控制acl数据
        
        @param request: CreateInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceAclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.decision):
            body['decision'] = request.decision
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not UtilClient.is_unset(request.resource_name):
            body['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.CreateInstanceAclRequest,
    ) -> rocket_mq20220801_models.CreateInstanceAclResponse:
        """
        @summary 创建访问控制acl数据
        
        @param request: CreateInstanceAclRequest
        @return: CreateInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def create_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.CreateInstanceAclRequest,
    ) -> rocket_mq20220801_models.CreateInstanceAclResponse:
        """
        @summary 创建访问控制acl数据
        
        @param request: CreateInstanceAclRequest
        @return: CreateInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def create_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceIpWhitelistResponse:
        """
        @summary 创建访问控制ip白名单
        
        @param request: CreateInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateInstanceIpWhitelistResponse:
        """
        @summary 创建访问控制ip白名单
        
        @param request: CreateInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_ip_whitelist(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.CreateInstanceIpWhitelistResponse:
        """
        @summary 创建访问控制ip白名单
        
        @param request: CreateInstanceIpWhitelistRequest
        @return: CreateInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def create_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.CreateInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.CreateInstanceIpWhitelistResponse:
        """
        @summary 创建访问控制ip白名单
        
        @param request: CreateInstanceIpWhitelistRequest
        @return: CreateInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def create_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.CreateTopicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_type):
            body['messageType'] = request.message_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.CreateTopicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_type):
            body['messageType'] = request.message_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.CreateTopicRequest,
    ) -> rocket_mq20220801_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_topic_with_options(instance_id, topic_name, request, headers, runtime)

    async def create_topic_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.CreateTopicRequest,
    ) -> rocket_mq20220801_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_topic_with_options_async(instance_id, topic_name, request, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    async def delete_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupResponse:
        """
        @summary Deletes a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def delete_consumer_group_subscription_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.DeleteConsumerGroupSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse:
        """
        @summary 取消消费组订阅关系
        
        @param request: DeleteConsumerGroupSubscriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_expression):
            query['filterExpression'] = request.filter_expression
        if not UtilClient.is_unset(request.filter_type):
            query['filterType'] = request.filter_type
        if not UtilClient.is_unset(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroupSubscription',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_subscription_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.DeleteConsumerGroupSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse:
        """
        @summary 取消消费组订阅关系
        
        @param request: DeleteConsumerGroupSubscriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_expression):
            query['filterExpression'] = request.filter_expression
        if not UtilClient.is_unset(request.filter_type):
            query['filterType'] = request.filter_type
        if not UtilClient.is_unset(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroupSubscription',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group_subscription(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.DeleteConsumerGroupSubscriptionRequest,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse:
        """
        @summary 取消消费组订阅关系
        
        @param request: DeleteConsumerGroupSubscriptionRequest
        @return: DeleteConsumerGroupSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_subscription_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def delete_consumer_group_subscription_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.DeleteConsumerGroupSubscriptionRequest,
    ) -> rocket_mq20220801_models.DeleteConsumerGroupSubscriptionResponse:
        """
        @summary 取消消费组订阅关系
        
        @param request: DeleteConsumerGroupSubscriptionRequest
        @return: DeleteConsumerGroupSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_subscription_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceResponse:
        """
        @summary Deletes a ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceResponse:
        """
        @summary Deletes a ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> rocket_mq20220801_models.DeleteInstanceResponse:
        """
        @summary Deletes a ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> rocket_mq20220801_models.DeleteInstanceResponse:
        """
        @summary Deletes a ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_account_with_options(
        self,
        instance_id: str,
        username: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceAccountResponse:
        """
        @summary 删除访问控制acl用户
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceAccountResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts/{OpenApiUtilClient.get_encode_param(username)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_account_with_options_async(
        self,
        instance_id: str,
        username: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceAccountResponse:
        """
        @summary 删除访问控制acl用户
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceAccountResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts/{OpenApiUtilClient.get_encode_param(username)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_account(
        self,
        instance_id: str,
        username: str,
    ) -> rocket_mq20220801_models.DeleteInstanceAccountResponse:
        """
        @summary 删除访问控制acl用户
        
        @return: DeleteInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_account_with_options(instance_id, username, headers, runtime)

    async def delete_instance_account_async(
        self,
        instance_id: str,
        username: str,
    ) -> rocket_mq20220801_models.DeleteInstanceAccountResponse:
        """
        @summary 删除访问控制acl用户
        
        @return: DeleteInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_account_with_options_async(instance_id, username, headers, runtime)

    def delete_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.DeleteInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: DeleteInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_name):
            query['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.DeleteInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: DeleteInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_name):
            query['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.DeleteInstanceAclRequest,
    ) -> rocket_mq20220801_models.DeleteInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: DeleteInstanceAclRequest
        @return: DeleteInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def delete_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.DeleteInstanceAclRequest,
    ) -> rocket_mq20220801_models.DeleteInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: DeleteInstanceAclRequest
        @return: DeleteInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def delete_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.DeleteInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse:
        """
        @summary 删除访问控制ip白名单
        
        @param request: DeleteInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.DeleteInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse:
        """
        @summary 删除访问控制ip白名单
        
        @param request: DeleteInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_ip_whitelist(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.DeleteInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse:
        """
        @summary 删除访问控制ip白名单
        
        @param request: DeleteInstanceIpWhitelistRequest
        @return: DeleteInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def delete_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.DeleteInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.DeleteInstanceIpWhitelistResponse:
        """
        @summary 删除访问控制ip白名单
        
        @param request: DeleteInstanceIpWhitelistRequest
        @return: DeleteInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def delete_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteTopicResponse:
        """
        @summary Deletes a specified topic.
        
        @description If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.DeleteTopicResponse:
        """
        @summary Deletes a specified topic.
        
        @description If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.DeleteTopicResponse:
        """
        @summary Deletes a specified topic.
        
        @description If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_topic_with_options(instance_id, topic_name, headers, runtime)

    async def delete_topic_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.DeleteTopicResponse:
        """
        @summary Deletes a specified topic.
        
        @description If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_topic_with_options_async(instance_id, topic_name, headers, runtime)

    def get_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupResponse:
        """
        @summary Queries the details of a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupResponse:
        """
        @summary Queries the details of a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupResponse:
        """
        @summary Queries the details of a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @return: GetConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    async def get_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupResponse:
        """
        @summary Queries the details of a specified consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @return: GetConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def get_consumer_group_lag_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupLagResponse:
        """
        @summary 查询消费者组堆积信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupLagResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroupLag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/lag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupLagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_lag_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupLagResponse:
        """
        @summary 查询消费者组堆积信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupLagResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroupLag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/lag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupLagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group_lag(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupLagResponse:
        """
        @summary 查询消费者组堆积信息
        
        @return: GetConsumerGroupLagResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_group_lag_with_options(instance_id, consumer_group_id, headers, runtime)

    async def get_consumer_group_lag_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupLagResponse:
        """
        @summary 查询消费者组堆积信息
        
        @return: GetConsumerGroupLagResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_lag_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def get_consumer_group_subscription_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse:
        """
        @summary 查询消费组订阅关系列表客户端分布
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupSubscriptionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroupSubscription',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_subscription_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse:
        """
        @summary 查询消费组订阅关系列表客户端分布
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerGroupSubscriptionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroupSubscription',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group_subscription(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse:
        """
        @summary 查询消费组订阅关系列表客户端分布
        
        @return: GetConsumerGroupSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_group_subscription_with_options(instance_id, consumer_group_id, topic_name, headers, runtime)

    async def get_consumer_group_subscription_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.GetConsumerGroupSubscriptionResponse:
        """
        @summary 查询消费组订阅关系列表客户端分布
        
        @return: GetConsumerGroupSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_subscription_with_options_async(instance_id, consumer_group_id, topic_name, headers, runtime)

    def get_consumer_stack_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.GetConsumerStackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerStackResponse:
        """
        @summary 查询消费者堆栈信息
        
        @param request: GetConsumerStackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerStack',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/stack',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_stack_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.GetConsumerStackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetConsumerStackResponse:
        """
        @summary 查询消费者堆栈信息
        
        @param request: GetConsumerStackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsumerStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['clientId'] = request.client_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerStack',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/stack',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_stack(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.GetConsumerStackRequest,
    ) -> rocket_mq20220801_models.GetConsumerStackResponse:
        """
        @summary 查询消费者堆栈信息
        
        @param request: GetConsumerStackRequest
        @return: GetConsumerStackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_stack_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def get_consumer_stack_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.GetConsumerStackRequest,
    ) -> rocket_mq20220801_models.GetConsumerStackResponse:
        """
        @summary 查询消费者堆栈信息
        
        @param request: GetConsumerStackRequest
        @return: GetConsumerStackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_consumer_stack_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetInstanceResponse:
        """
        @summary Queries the detailed information about an instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetInstanceResponse:
        """
        @summary Queries the detailed information about an instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> rocket_mq20220801_models.GetInstanceResponse:
        """
        @summary Queries the detailed information about an instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> rocket_mq20220801_models.GetInstanceResponse:
        """
        @summary Queries the detailed information about an instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_account_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.GetInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetInstanceAccountResponse:
        """
        @summary 获取实例账号
        
        @param request: GetInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/account',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_account_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.GetInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetInstanceAccountResponse:
        """
        @summary 获取实例账号
        
        @param request: GetInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/account',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_account(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.GetInstanceAccountRequest,
    ) -> rocket_mq20220801_models.GetInstanceAccountResponse:
        """
        @summary 获取实例账号
        
        @param request: GetInstanceAccountRequest
        @return: GetInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_account_with_options(instance_id, request, headers, runtime)

    async def get_instance_account_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.GetInstanceAccountRequest,
    ) -> rocket_mq20220801_models.GetInstanceAccountResponse:
        """
        @summary 获取实例账号
        
        @param request: GetInstanceAccountRequest
        @return: GetInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_account_with_options_async(instance_id, request, headers, runtime)

    def get_message_detail_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetMessageDetailResponse:
        """
        @summary 消息详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessageDetailResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageDetail',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages/{OpenApiUtilClient.get_encode_param(message_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetMessageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_detail_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetMessageDetailResponse:
        """
        @summary 消息详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessageDetailResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMessageDetail',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages/{OpenApiUtilClient.get_encode_param(message_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetMessageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_detail(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> rocket_mq20220801_models.GetMessageDetailResponse:
        """
        @summary 消息详情
        
        @return: GetMessageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_detail_with_options(instance_id, topic_name, message_id, headers, runtime)

    async def get_message_detail_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> rocket_mq20220801_models.GetMessageDetailResponse:
        """
        @summary 消息详情
        
        @return: GetMessageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_message_detail_with_options_async(instance_id, topic_name, message_id, headers, runtime)

    def get_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetTopicResponse:
        """
        @summary Queries the details of a specified topic.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetTopicResponse:
        """
        @summary Queries the details of a specified topic.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.GetTopicResponse:
        """
        @summary Queries the details of a specified topic.
        
        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_topic_with_options(instance_id, topic_name, headers, runtime)

    async def get_topic_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.GetTopicResponse:
        """
        @summary Queries the details of a specified topic.
        
        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_topic_with_options_async(instance_id, topic_name, headers, runtime)

    def get_trace_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetTraceResponse:
        """
        @summary 轨迹查询
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/traces/{OpenApiUtilClient.get_encode_param(message_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.GetTraceResponse:
        """
        @summary 轨迹查询
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/traces/{OpenApiUtilClient.get_encode_param(message_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> rocket_mq20220801_models.GetTraceResponse:
        """
        @summary 轨迹查询
        
        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trace_with_options(instance_id, topic_name, message_id, headers, runtime)

    async def get_trace_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> rocket_mq20220801_models.GetTraceResponse:
        """
        @summary 轨迹查询
        
        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_trace_with_options_async(instance_id, topic_name, message_id, headers, runtime)

    def list_available_zones_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListAvailableZonesResponse:
        """
        @summary 查询支持的可用区
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableZonesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableZones',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/zones',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_zones_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListAvailableZonesResponse:
        """
        @summary 查询支持的可用区
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableZonesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableZones',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/zones',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_zones(self) -> rocket_mq20220801_models.ListAvailableZonesResponse:
        """
        @summary 查询支持的可用区
        
        @return: ListAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_zones_with_options(headers, runtime)

    async def list_available_zones_async(self) -> rocket_mq20220801_models.ListAvailableZonesResponse:
        """
        @summary 查询支持的可用区
        
        @return: ListAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_available_zones_with_options_async(headers, runtime)

    def list_consumer_connections_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerConnectionsResponse:
        """
        @summary 查询消费者客户端连接信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerConnectionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerConnections',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/connections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_connections_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerConnectionsResponse:
        """
        @summary 查询消费者客户端连接信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerConnectionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerConnections',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/connections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_connections(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.ListConsumerConnectionsResponse:
        """
        @summary 查询消费者客户端连接信息
        
        @return: ListConsumerConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_connections_with_options(instance_id, consumer_group_id, headers, runtime)

    async def list_consumer_connections_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.ListConsumerConnectionsResponse:
        """
        @summary 查询消费者客户端连接信息
        
        @return: ListConsumerConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumer_connections_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def list_consumer_group_subscriptions_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific consumer group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupSubscriptionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroupSubscriptions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_group_subscriptions_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific consumer group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupSubscriptionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroupSubscriptions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/subscriptions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_group_subscriptions(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific consumer group.
        
        @return: ListConsumerGroupSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_subscriptions_with_options(instance_id, consumer_group_id, headers, runtime)

    async def list_consumer_group_subscriptions_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific consumer group.
        
        @return: ListConsumerGroupSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_subscriptions_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def list_consumer_groups_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerGroupsResponse:
        """
        @summary Queries the consumer groups in a specified instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListConsumerGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumerGroups',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_groups_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListConsumerGroupsResponse:
        """
        @summary Queries the consumer groups in a specified instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListConsumerGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumerGroups',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_groups(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListConsumerGroupsRequest,
    ) -> rocket_mq20220801_models.ListConsumerGroupsResponse:
        """
        @summary Queries the consumer groups in a specified instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListConsumerGroupsRequest
        @return: ListConsumerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_groups_with_options(instance_id, request, headers, runtime)

    async def list_consumer_groups_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListConsumerGroupsRequest,
    ) -> rocket_mq20220801_models.ListConsumerGroupsResponse:
        """
        @summary Queries the consumer groups in a specified instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListConsumerGroupsRequest
        @return: ListConsumerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumer_groups_with_options_async(instance_id, request, headers, runtime)

    def list_instance_account_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceAccountResponse:
        """
        @summary 访问控制acl用户列表
        
        @param request: ListInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['accountStatus'] = request.account_status
        if not UtilClient.is_unset(request.account_type):
            query['accountType'] = request.account_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_account_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceAccountResponse:
        """
        @summary 访问控制acl用户列表
        
        @param request: ListInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['accountStatus'] = request.account_status
        if not UtilClient.is_unset(request.account_type):
            query['accountType'] = request.account_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_account(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAccountRequest,
    ) -> rocket_mq20220801_models.ListInstanceAccountResponse:
        """
        @summary 访问控制acl用户列表
        
        @param request: ListInstanceAccountRequest
        @return: ListInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_account_with_options(instance_id, request, headers, runtime)

    async def list_instance_account_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAccountRequest,
    ) -> rocket_mq20220801_models.ListInstanceAccountResponse:
        """
        @summary 访问控制acl用户列表
        
        @param request: ListInstanceAccountRequest
        @return: ListInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_account_with_options_async(instance_id, request, headers, runtime)

    def list_instance_acl_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceAclResponse:
        """
        @summary 访问控制acl数据列表
        
        @param request: ListInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_acl_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceAclResponse:
        """
        @summary 访问控制acl数据列表
        
        @param request: ListInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_acl(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAclRequest,
    ) -> rocket_mq20220801_models.ListInstanceAclResponse:
        """
        @summary 访问控制acl数据列表
        
        @param request: ListInstanceAclRequest
        @return: ListInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_acl_with_options(instance_id, request, headers, runtime)

    async def list_instance_acl_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceAclRequest,
    ) -> rocket_mq20220801_models.ListInstanceAclResponse:
        """
        @summary 访问控制acl数据列表
        
        @param request: ListInstanceAclRequest
        @return: ListInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_acl_with_options_async(instance_id, request, headers, runtime)

    def list_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceIpWhitelistResponse:
        """
        @summary 查询访问控制ip白名单列表
        
        @param request: ListInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstanceIpWhitelistResponse:
        """
        @summary 查询访问控制ip白名单列表
        
        @param request: ListInstanceIpWhitelistRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceIpWhitelist',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ip/whitelist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_ip_whitelist(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.ListInstanceIpWhitelistResponse:
        """
        @summary 查询访问控制ip白名单列表
        
        @param request: ListInstanceIpWhitelistRequest
        @return: ListInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def list_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListInstanceIpWhitelistRequest,
    ) -> rocket_mq20220801_models.ListInstanceIpWhitelistResponse:
        """
        @summary 查询访问控制ip白名单列表
        
        @param request: ListInstanceIpWhitelistRequest
        @return: ListInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: rocket_mq20220801_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstancesResponse:
        """
        @summary Queries all ApsaraMQ for RocketMQ instances in a specific region.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rocket_mq20220801_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.series_codes):
            request.series_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.series_codes, 'seriesCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series_codes_shrink):
            query['seriesCodes'] = request.series_codes_shrink
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: rocket_mq20220801_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListInstancesResponse:
        """
        @summary Queries all ApsaraMQ for RocketMQ instances in a specific region.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rocket_mq20220801_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.series_codes):
            request.series_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.series_codes, 'seriesCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series_codes_shrink):
            query['seriesCodes'] = request.series_codes_shrink
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: rocket_mq20220801_models.ListInstancesRequest,
    ) -> rocket_mq20220801_models.ListInstancesResponse:
        """
        @summary Queries all ApsaraMQ for RocketMQ instances in a specific region.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: rocket_mq20220801_models.ListInstancesRequest,
    ) -> rocket_mq20220801_models.ListInstancesResponse:
        """
        @summary Queries all ApsaraMQ for RocketMQ instances in a specific region.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_messages_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListMessagesResponse:
        """
        @summary 查询消息列表
        
        @param request: ListMessagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.message_id):
            query['messageId'] = request.message_id
        if not UtilClient.is_unset(request.message_key):
            query['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scroll_id):
            query['scrollId'] = request.scroll_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListMessagesResponse:
        """
        @summary 查询消息列表
        
        @param request: ListMessagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.message_id):
            query['messageId'] = request.message_id
        if not UtilClient.is_unset(request.message_key):
            query['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scroll_id):
            query['scrollId'] = request.scroll_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListMessagesRequest,
    ) -> rocket_mq20220801_models.ListMessagesResponse:
        """
        @summary 查询消息列表
        
        @param request: ListMessagesRequest
        @return: ListMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(instance_id, topic_name, request, headers, runtime)

    async def list_messages_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListMessagesRequest,
    ) -> rocket_mq20220801_models.ListMessagesResponse:
        """
        @summary 查询消息列表
        
        @param request: ListMessagesRequest
        @return: ListMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(instance_id, topic_name, request, headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListRegionsResponse:
        """
        @summary Queries regions in which ApsaraMQ for RocketMQ is available.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListRegionsResponse:
        """
        @summary Queries regions in which ApsaraMQ for RocketMQ is available.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> rocket_mq20220801_models.ListRegionsResponse:
        """
        @summary Queries regions in which ApsaraMQ for RocketMQ is available.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> rocket_mq20220801_models.ListRegionsResponse:
        """
        @summary Queries regions in which ApsaraMQ for RocketMQ is available.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: rocket_mq20220801_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTagResourcesResponse:
        """
        @summary 查询可见的资源标签关系
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: rocket_mq20220801_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTagResourcesResponse:
        """
        @summary 查询可见的资源标签关系
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: rocket_mq20220801_models.ListTagResourcesRequest,
    ) -> rocket_mq20220801_models.ListTagResourcesResponse:
        """
        @summary 查询可见的资源标签关系
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: rocket_mq20220801_models.ListTagResourcesRequest,
    ) -> rocket_mq20220801_models.ListTagResourcesResponse:
        """
        @summary 查询可见的资源标签关系
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_topic_subscriptions_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTopicSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific topic.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicSubscriptionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTopicSubscriptions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/subscriptions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTopicSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_subscriptions_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTopicSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific topic.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicSubscriptionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTopicSubscriptions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/subscriptions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTopicSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_subscriptions(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.ListTopicSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific topic.
        
        @return: ListTopicSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_topic_subscriptions_with_options(instance_id, topic_name, headers, runtime)

    async def list_topic_subscriptions_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> rocket_mq20220801_models.ListTopicSubscriptionsResponse:
        """
        @summary Queries the subscriptions of a specific topic.
        
        @return: ListTopicSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_topic_subscriptions_with_options_async(instance_id, topic_name, headers, runtime)

    def list_topics_with_options(
        self,
        instance_id: str,
        tmp_req: rocket_mq20220801_models.ListTopicsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTopicsResponse:
        """
        @summary Queries the topics in a specified instance.
        
        @param tmp_req: ListTopicsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rocket_mq20220801_models.ListTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.message_types):
            request.message_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.message_types, 'messageTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.message_types_shrink):
            query['messageTypes'] = request.message_types_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topics_with_options_async(
        self,
        instance_id: str,
        tmp_req: rocket_mq20220801_models.ListTopicsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTopicsResponse:
        """
        @summary Queries the topics in a specified instance.
        
        @param tmp_req: ListTopicsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rocket_mq20220801_models.ListTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.message_types):
            request.message_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.message_types, 'messageTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.message_types_shrink):
            query['messageTypes'] = request.message_types_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topics(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListTopicsRequest,
    ) -> rocket_mq20220801_models.ListTopicsResponse:
        """
        @summary Queries the topics in a specified instance.
        
        @param request: ListTopicsRequest
        @return: ListTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_topics_with_options(instance_id, request, headers, runtime)

    async def list_topics_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.ListTopicsRequest,
    ) -> rocket_mq20220801_models.ListTopicsResponse:
        """
        @summary Queries the topics in a specified instance.
        
        @param request: ListTopicsRequest
        @return: ListTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_topics_with_options_async(instance_id, request, headers, runtime)

    def list_traces_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListTracesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTracesResponse:
        """
        @summary 轨迹消息列表
        
        @param request: ListTracesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.message_id):
            query['messageId'] = request.message_id
        if not UtilClient.is_unset(request.message_key):
            query['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['queryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraces',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/traces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traces_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListTracesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ListTracesResponse:
        """
        @summary 轨迹消息列表
        
        @param request: ListTracesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.message_id):
            query['messageId'] = request.message_id
        if not UtilClient.is_unset(request.message_key):
            query['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['queryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraces',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/traces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traces(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListTracesRequest,
    ) -> rocket_mq20220801_models.ListTracesResponse:
        """
        @summary 轨迹消息列表
        
        @param request: ListTracesRequest
        @return: ListTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_traces_with_options(instance_id, topic_name, request, headers, runtime)

    async def list_traces_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ListTracesRequest,
    ) -> rocket_mq20220801_models.ListTracesResponse:
        """
        @summary 轨迹消息列表
        
        @param request: ListTracesRequest
        @return: ListTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_traces_with_options_async(instance_id, topic_name, request, headers, runtime)

    def reset_consume_offset_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ResetConsumeOffsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ResetConsumeOffsetResponse:
        """
        @summary Resets the consumer offset of a consumer group.
        
        @param request: ResetConsumeOffsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetConsumeOffsetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.reset_time):
            body['resetTime'] = request.reset_time
        if not UtilClient.is_unset(request.reset_type):
            body['resetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetConsumeOffset',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/consumeOffsets/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ResetConsumeOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_consume_offset_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ResetConsumeOffsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.ResetConsumeOffsetResponse:
        """
        @summary Resets the consumer offset of a consumer group.
        
        @param request: ResetConsumeOffsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetConsumeOffsetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.reset_time):
            body['resetTime'] = request.reset_time
        if not UtilClient.is_unset(request.reset_type):
            body['resetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetConsumeOffset',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}/consumeOffsets/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ResetConsumeOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_consume_offset(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ResetConsumeOffsetRequest,
    ) -> rocket_mq20220801_models.ResetConsumeOffsetResponse:
        """
        @summary Resets the consumer offset of a consumer group.
        
        @param request: ResetConsumeOffsetRequest
        @return: ResetConsumeOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_consume_offset_with_options(instance_id, consumer_group_id, topic_name, request, headers, runtime)

    async def reset_consume_offset_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.ResetConsumeOffsetRequest,
    ) -> rocket_mq20220801_models.ResetConsumeOffsetResponse:
        """
        @summary Resets the consumer offset of a consumer group.
        
        @param request: ResetConsumeOffsetRequest
        @return: ResetConsumeOffsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_consume_offset_with_options_async(instance_id, consumer_group_id, topic_name, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: rocket_mq20220801_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.TagResourcesResponse:
        """
        @summary 用户创建标签资源关系（用户标签）
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: rocket_mq20220801_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.TagResourcesResponse:
        """
        @summary 用户创建标签资源关系（用户标签）
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: rocket_mq20220801_models.TagResourcesRequest,
    ) -> rocket_mq20220801_models.TagResourcesResponse:
        """
        @summary 用户创建标签资源关系（用户标签）
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: rocket_mq20220801_models.TagResourcesRequest,
    ) -> rocket_mq20220801_models.TagResourcesResponse:
        """
        @summary 用户创建标签资源关系（用户标签）
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: rocket_mq20220801_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UntagResourcesResponse:
        """
        @summary 用户删除标签资源关系
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['tagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: rocket_mq20220801_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UntagResourcesResponse:
        """
        @summary 用户删除标签资源关系
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['tagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/resourceTag/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: rocket_mq20220801_models.UntagResourcesRequest,
    ) -> rocket_mq20220801_models.UntagResourcesResponse:
        """
        @summary 用户删除标签资源关系
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: rocket_mq20220801_models.UntagResourcesRequest,
    ) -> rocket_mq20220801_models.UntagResourcesResponse:
        """
        @summary 用户删除标签资源关系
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateConsumerGroupResponse:
        """
        @summary Updates the basic information about and the consumption retry policy of a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateConsumerGroupResponse:
        """
        @summary Updates the basic information about and the consumption retry policy of a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/consumerGroups/{OpenApiUtilClient.get_encode_param(consumer_group_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_group(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.UpdateConsumerGroupRequest,
    ) -> rocket_mq20220801_models.UpdateConsumerGroupResponse:
        """
        @summary Updates the basic information about and the consumption retry policy of a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateConsumerGroupRequest
        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: rocket_mq20220801_models.UpdateConsumerGroupRequest,
    ) -> rocket_mq20220801_models.UpdateConsumerGroupResponse:
        """
        @summary Updates the basic information about and the consumption retry policy of a consumer group.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateConsumerGroupRequest
        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceResponse:
        """
        @summary Updates the basic information and specifications of an ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl_info):
            body['aclInfo'] = request.acl_info
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceResponse:
        """
        @summary Updates the basic information and specifications of an ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl_info):
            body['aclInfo'] = request.acl_info
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.UpdateInstanceRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceResponse:
        """
        @summary Updates the basic information and specifications of an ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: rocket_mq20220801_models.UpdateInstanceRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceResponse:
        """
        @summary Updates the basic information and specifications of an ApsaraMQ for RocketMQ instance.
        
        @description > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_account_with_options(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceAccountResponse:
        """
        @summary 修改访问控制acl用户
        
        @param request: UpdateInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['accountStatus'] = request.account_status
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts/{OpenApiUtilClient.get_encode_param(username)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_account_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceAccountResponse:
        """
        @summary 修改访问控制acl用户
        
        @param request: UpdateInstanceAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['accountStatus'] = request.account_status
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAccount',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/accounts/{OpenApiUtilClient.get_encode_param(username)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_account(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAccountRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceAccountResponse:
        """
        @summary 修改访问控制acl用户
        
        @param request: UpdateInstanceAccountRequest
        @return: UpdateInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_account_with_options(instance_id, username, request, headers, runtime)

    async def update_instance_account_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAccountRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceAccountResponse:
        """
        @summary 修改访问控制acl用户
        
        @param request: UpdateInstanceAccountRequest
        @return: UpdateInstanceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_account_with_options_async(instance_id, username, request, headers, runtime)

    def update_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: UpdateInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.decision):
            body['decision'] = request.decision
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not UtilClient.is_unset(request.resource_name):
            body['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: UpdateInstanceAclRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAclResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['actions'] = request.actions
        if not UtilClient.is_unset(request.decision):
            body['decision'] = request.decision
        if not UtilClient.is_unset(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not UtilClient.is_unset(request.resource_name):
            body['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAcl',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/acl/account/{OpenApiUtilClient.get_encode_param(username)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAclRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: UpdateInstanceAclRequest
        @return: UpdateInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def update_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: rocket_mq20220801_models.UpdateInstanceAclRequest,
    ) -> rocket_mq20220801_models.UpdateInstanceAclResponse:
        """
        @summary 删除访问控制acl数据
        
        @param request: UpdateInstanceAclRequest
        @return: UpdateInstanceAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def update_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.UpdateTopicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateTopicResponse:
        """
        @summary Updates the basic information about a topic.
        
        @param request: UpdateTopicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.UpdateTopicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.UpdateTopicResponse:
        """
        @summary Updates the basic information about a topic.
        
        @param request: UpdateTopicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_topic(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.UpdateTopicRequest,
    ) -> rocket_mq20220801_models.UpdateTopicResponse:
        """
        @summary Updates the basic information about a topic.
        
        @param request: UpdateTopicRequest
        @return: UpdateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_topic_with_options(instance_id, topic_name, request, headers, runtime)

    async def update_topic_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.UpdateTopicRequest,
    ) -> rocket_mq20220801_models.UpdateTopicResponse:
        """
        @summary Updates the basic information about a topic.
        
        @param request: UpdateTopicRequest
        @return: UpdateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_topic_with_options_async(instance_id, topic_name, request, headers, runtime)

    def verify_consume_message_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: rocket_mq20220801_models.VerifyConsumeMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.VerifyConsumeMessageResponse:
        """
        @summary 消费验证
        
        @param request: VerifyConsumeMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyConsumeMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['clientId'] = request.client_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyConsumeMessage',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages/{OpenApiUtilClient.get_encode_param(message_id)}/action/verifyConsume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.VerifyConsumeMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_consume_message_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: rocket_mq20220801_models.VerifyConsumeMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.VerifyConsumeMessageResponse:
        """
        @summary 消费验证
        
        @param request: VerifyConsumeMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyConsumeMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['clientId'] = request.client_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyConsumeMessage',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages/{OpenApiUtilClient.get_encode_param(message_id)}/action/verifyConsume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.VerifyConsumeMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_consume_message(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: rocket_mq20220801_models.VerifyConsumeMessageRequest,
    ) -> rocket_mq20220801_models.VerifyConsumeMessageResponse:
        """
        @summary 消费验证
        
        @param request: VerifyConsumeMessageRequest
        @return: VerifyConsumeMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_consume_message_with_options(instance_id, topic_name, message_id, request, headers, runtime)

    async def verify_consume_message_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: rocket_mq20220801_models.VerifyConsumeMessageRequest,
    ) -> rocket_mq20220801_models.VerifyConsumeMessageResponse:
        """
        @summary 消费验证
        
        @param request: VerifyConsumeMessageRequest
        @return: VerifyConsumeMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_consume_message_with_options_async(instance_id, topic_name, message_id, request, headers, runtime)

    def verify_send_message_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.VerifySendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.VerifySendMessageResponse:
        """
        @summary 发送消息
        
        @param request: VerifySendMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySendMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.message_key):
            body['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.message_tag):
            body['messageTag'] = request.message_tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifySendMessage',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.VerifySendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_send_message_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.VerifySendMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> rocket_mq20220801_models.VerifySendMessageResponse:
        """
        @summary 发送消息
        
        @param request: VerifySendMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySendMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.message_key):
            body['messageKey'] = request.message_key
        if not UtilClient.is_unset(request.message_tag):
            body['messageTag'] = request.message_tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifySendMessage',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/topics/{OpenApiUtilClient.get_encode_param(topic_name)}/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.VerifySendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_send_message(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.VerifySendMessageRequest,
    ) -> rocket_mq20220801_models.VerifySendMessageResponse:
        """
        @summary 发送消息
        
        @param request: VerifySendMessageRequest
        @return: VerifySendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_send_message_with_options(instance_id, topic_name, request, headers, runtime)

    async def verify_send_message_async(
        self,
        instance_id: str,
        topic_name: str,
        request: rocket_mq20220801_models.VerifySendMessageRequest,
    ) -> rocket_mq20220801_models.VerifySendMessageResponse:
        """
        @summary 发送消息
        
        @param request: VerifySendMessageRequest
        @return: VerifySendMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_send_message_with_options_async(instance_id, topic_name, request, headers, runtime)
