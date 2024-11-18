# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hologram20220601 import models as hologram_20220601_models
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
        self._endpoint = self.get_endpoint('hologram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: hologram_20220601_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ChangeResourceGroupResponse:
        """
        @summary Updates a resource group.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tag/changeResourceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: hologram_20220601_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ChangeResourceGroupResponse:
        """
        @summary Updates a resource group.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tag/changeResourceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: hologram_20220601_models.ChangeResourceGroupRequest,
    ) -> hologram_20220601_models.ChangeResourceGroupResponse:
        """
        @summary Updates a resource group.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: hologram_20220601_models.ChangeResourceGroupRequest,
    ) -> hologram_20220601_models.ChangeResourceGroupResponse:
        """
        @summary Updates a resource group.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.CreateHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.CreateHoloWarehouseResponse:
        """
        @summary Creates a virtual warehouse.
        
        @param request: CreateHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/createHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.CreateHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.CreateHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.CreateHoloWarehouseResponse:
        """
        @summary Creates a virtual warehouse.
        
        @param request: CreateHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/createHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.CreateHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.CreateHoloWarehouseRequest,
    ) -> hologram_20220601_models.CreateHoloWarehouseResponse:
        """
        @summary Creates a virtual warehouse.
        
        @param request: CreateHoloWarehouseRequest
        @return: CreateHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def create_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.CreateHoloWarehouseRequest,
    ) -> hologram_20220601_models.CreateHoloWarehouseResponse:
        """
        @summary Creates a virtual warehouse.
        
        @param request: CreateHoloWarehouseRequest
        @return: CreateHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: hologram_20220601_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.CreateInstanceResponse:
        """
        @summary Creates a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['autoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.initial_databases):
            body['initialDatabases'] = request.initial_databases
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.leader_instance_id):
            body['leaderInstanceId'] = request.leader_instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['pricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: hologram_20220601_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.CreateInstanceResponse:
        """
        @summary Creates a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['autoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.initial_databases):
            body['initialDatabases'] = request.initial_databases
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.leader_instance_id):
            body['leaderInstanceId'] = request.leader_instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['pricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: hologram_20220601_models.CreateInstanceRequest,
    ) -> hologram_20220601_models.CreateInstanceResponse:
        """
        @summary Creates a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: hologram_20220601_models.CreateInstanceRequest,
    ) -> hologram_20220601_models.CreateInstanceResponse:
        """
        @summary Creates a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def delete_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DeleteHoloWarehouseResponse:
        """
        @summary Deletes a virtual warehouse.
        
        @param request: DeleteHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/deleteHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DeleteHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DeleteHoloWarehouseResponse:
        """
        @summary Deletes a virtual warehouse.
        
        @param request: DeleteHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/deleteHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DeleteHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteHoloWarehouseRequest,
    ) -> hologram_20220601_models.DeleteHoloWarehouseResponse:
        """
        @summary Deletes a virtual warehouse.
        
        @param request: DeleteHoloWarehouseRequest
        @return: DeleteHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def delete_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteHoloWarehouseRequest,
    ) -> hologram_20220601_models.DeleteHoloWarehouseResponse:
        """
        @summary Deletes a virtual warehouse.
        
        @param request: DeleteHoloWarehouseRequest
        @return: DeleteHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DeleteInstanceResponse:
        """
        @summary Deletes a Hologres instance.
        
        @description > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        You can delete only pay-as-you-go instances.
        If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DeleteInstanceResponse:
        """
        @summary Deletes a Hologres instance.
        
        @description > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        You can delete only pay-as-you-go instances.
        If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteInstanceRequest,
    ) -> hologram_20220601_models.DeleteInstanceResponse:
        """
        @summary Deletes a Hologres instance.
        
        @description > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        You can delete only pay-as-you-go instances.
        If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DeleteInstanceRequest,
    ) -> hologram_20220601_models.DeleteInstanceResponse:
        """
        @summary Deletes a Hologres instance.
        
        @description > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        You can delete only pay-as-you-go instances.
        If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, request, headers, runtime)

    def disable_hive_access_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.DisableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DisableHiveAccessResponse:
        """
        @summary Disables data lake acceleration.
        
        @param request: DisableHiveAccessRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableHiveAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHiveAccess',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/disableHiveAccess',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DisableHiveAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_hive_access_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DisableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.DisableHiveAccessResponse:
        """
        @summary Disables data lake acceleration.
        
        @param request: DisableHiveAccessRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableHiveAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHiveAccess',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/disableHiveAccess',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DisableHiveAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_hive_access(
        self,
        instance_id: str,
        request: hologram_20220601_models.DisableHiveAccessRequest,
    ) -> hologram_20220601_models.DisableHiveAccessResponse:
        """
        @summary Disables data lake acceleration.
        
        @param request: DisableHiveAccessRequest
        @return: DisableHiveAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_hive_access_with_options(instance_id, request, headers, runtime)

    async def disable_hive_access_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.DisableHiveAccessRequest,
    ) -> hologram_20220601_models.DisableHiveAccessResponse:
        """
        @summary Disables data lake acceleration.
        
        @param request: DisableHiveAccessRequest
        @return: DisableHiveAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_hive_access_with_options_async(instance_id, request, headers, runtime)

    def enable_hive_access_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.EnableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.EnableHiveAccessResponse:
        """
        @summary Enables data lake acceleration.
        
        @param request: EnableHiveAccessRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableHiveAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHiveAccess',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/enableHiveAccess',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.EnableHiveAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hive_access_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.EnableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.EnableHiveAccessResponse:
        """
        @summary Enables data lake acceleration.
        
        @param request: EnableHiveAccessRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableHiveAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHiveAccess',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/enableHiveAccess',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.EnableHiveAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hive_access(
        self,
        instance_id: str,
        request: hologram_20220601_models.EnableHiveAccessRequest,
    ) -> hologram_20220601_models.EnableHiveAccessResponse:
        """
        @summary Enables data lake acceleration.
        
        @param request: EnableHiveAccessRequest
        @return: EnableHiveAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_hive_access_with_options(instance_id, request, headers, runtime)

    async def enable_hive_access_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.EnableHiveAccessRequest,
    ) -> hologram_20220601_models.EnableHiveAccessResponse:
        """
        @summary Enables data lake acceleration.
        
        @param request: EnableHiveAccessRequest
        @return: EnableHiveAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_hive_access_with_options_async(instance_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetInstanceResponse:
        """
        @summary Obtains the details of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetInstanceResponse:
        """
        @summary Obtains the details of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.GetInstanceResponse:
        """
        @summary Obtains the details of an instance.
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.GetInstanceResponse:
        """
        @summary Obtains the details of an instance.
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_warehouse_detail_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetWarehouseDetailResponse:
        """
        @summary Queries details of a virtual warehouse instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarehouseDetailResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWarehouseDetail',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/getWarehouseDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetWarehouseDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warehouse_detail_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetWarehouseDetailResponse:
        """
        @summary Queries details of a virtual warehouse instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarehouseDetailResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWarehouseDetail',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/getWarehouseDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetWarehouseDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warehouse_detail(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.GetWarehouseDetailResponse:
        """
        @summary Queries details of a virtual warehouse instance.
        
        @return: GetWarehouseDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_warehouse_detail_with_options(instance_id, headers, runtime)

    async def get_warehouse_detail_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.GetWarehouseDetailResponse:
        """
        @summary Queries details of a virtual warehouse instance.
        
        @return: GetWarehouseDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_warehouse_detail_with_options_async(instance_id, headers, runtime)

    def list_backup_data_with_options(
        self,
        request: hologram_20220601_models.ListBackupDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListBackupDataResponse:
        """
        @summary 获取备份列表
        
        @param request: ListBackupDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBackupDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['backupType'] = request.backup_type
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackupData',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/backups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListBackupDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backup_data_with_options_async(
        self,
        request: hologram_20220601_models.ListBackupDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListBackupDataResponse:
        """
        @summary 获取备份列表
        
        @param request: ListBackupDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBackupDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_type):
            query['backupType'] = request.backup_type
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackupData',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/backups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListBackupDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_backup_data(
        self,
        request: hologram_20220601_models.ListBackupDataRequest,
    ) -> hologram_20220601_models.ListBackupDataResponse:
        """
        @summary 获取备份列表
        
        @param request: ListBackupDataRequest
        @return: ListBackupDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_backup_data_with_options(request, headers, runtime)

    async def list_backup_data_async(
        self,
        request: hologram_20220601_models.ListBackupDataRequest,
    ) -> hologram_20220601_models.ListBackupDataResponse:
        """
        @summary 获取备份列表
        
        @param request: ListBackupDataRequest
        @return: ListBackupDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_backup_data_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cms_instance_type):
            body['cmsInstanceType'] = request.cms_instance_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cms_instance_type):
            body['cmsInstanceType'] = request.cms_instance_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
    ) -> hologram_20220601_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
    ) -> hologram_20220601_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_warehouses_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListWarehousesResponse:
        """
        @summary Queries the list of virtual warehouse instances.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarehousesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWarehouses',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/listWarehouses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListWarehousesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warehouses_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListWarehousesResponse:
        """
        @summary Queries the list of virtual warehouse instances.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarehousesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWarehouses',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/listWarehouses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListWarehousesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warehouses(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ListWarehousesResponse:
        """
        @summary Queries the list of virtual warehouse instances.
        
        @return: ListWarehousesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_warehouses_with_options(instance_id, headers, runtime)

    async def list_warehouses_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ListWarehousesResponse:
        """
        @summary Queries the list of virtual warehouse instances.
        
        @return: ListWarehousesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_warehouses_with_options_async(instance_id, headers, runtime)

    def rebalance_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.RebalanceHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RebalanceHoloWarehouseResponse:
        """
        @summary Triggers shard rebalancing for a virtual warehouse.
        
        @param request: RebalanceHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebalanceHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rebalanceHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RebalanceHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RebalanceHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RebalanceHoloWarehouseResponse:
        """
        @summary Triggers shard rebalancing for a virtual warehouse.
        
        @param request: RebalanceHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebalanceHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rebalanceHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RebalanceHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.RebalanceHoloWarehouseRequest,
    ) -> hologram_20220601_models.RebalanceHoloWarehouseResponse:
        """
        @summary Triggers shard rebalancing for a virtual warehouse.
        
        @param request: RebalanceHoloWarehouseRequest
        @return: RebalanceHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rebalance_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def rebalance_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RebalanceHoloWarehouseRequest,
    ) -> hologram_20220601_models.RebalanceHoloWarehouseResponse:
        """
        @summary Triggers shard rebalancing for a virtual warehouse.
        
        @param request: RebalanceHoloWarehouseRequest
        @return: RebalanceHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rebalance_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def rename_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenameHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RenameHoloWarehouseResponse:
        """
        @summary Renames a virtual warehouse.
        
        @param request: RenameHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.new_warehouse_name):
            body['newWarehouseName'] = request.new_warehouse_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/renameHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RenameHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenameHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RenameHoloWarehouseResponse:
        """
        @summary Renames a virtual warehouse.
        
        @param request: RenameHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.new_warehouse_name):
            body['newWarehouseName'] = request.new_warehouse_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/renameHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RenameHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenameHoloWarehouseRequest,
    ) -> hologram_20220601_models.RenameHoloWarehouseResponse:
        """
        @summary Renames a virtual warehouse.
        
        @param request: RenameHoloWarehouseRequest
        @return: RenameHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def rename_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenameHoloWarehouseRequest,
    ) -> hologram_20220601_models.RenameHoloWarehouseResponse:
        """
        @summary Renames a virtual warehouse.
        
        @param request: RenameHoloWarehouseRequest
        @return: RenameHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rename_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def renew_instance_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RenewInstanceResponse:
        """
        @summary Manually renews a Hologres instance. You can enable monthly auto-renewal when you renew a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        You can renew only subscription instances.
        
        @param request: RenewInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RenewInstanceResponse:
        """
        @summary Manually renews a Hologres instance. You can enable monthly auto-renewal when you renew a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        You can renew only subscription instances.
        
        @param request: RenewInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenewInstanceRequest,
    ) -> hologram_20220601_models.RenewInstanceResponse:
        """
        @summary Manually renews a Hologres instance. You can enable monthly auto-renewal when you renew a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        You can renew only subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    async def renew_instance_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RenewInstanceRequest,
    ) -> hologram_20220601_models.RenewInstanceResponse:
        """
        @summary Manually renews a Hologres instance. You can enable monthly auto-renewal when you renew a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        You can renew only subscription instances.
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(instance_id, request, headers, runtime)

    def restart_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.RestartHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartHoloWarehouseResponse:
        """
        @summary Restarts a virtual warehouse.
        
        @param request: RestartHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restartHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RestartHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartHoloWarehouseResponse:
        """
        @summary Restarts a virtual warehouse.
        
        @param request: RestartHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restartHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.RestartHoloWarehouseRequest,
    ) -> hologram_20220601_models.RestartHoloWarehouseResponse:
        """
        @summary Restarts a virtual warehouse.
        
        @param request: RestartHoloWarehouseRequest
        @return: RestartHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def restart_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.RestartHoloWarehouseRequest,
    ) -> hologram_20220601_models.RestartHoloWarehouseResponse:
        """
        @summary Restarts a virtual warehouse.
        
        @param request: RestartHoloWarehouseRequest
        @return: RestartHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def restart_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, headers, runtime)

    async def restart_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(instance_id, headers, runtime)

    def resume_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.ResumeHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeHoloWarehouseResponse:
        """
        @summary Resumes a virtual warehouse.
        
        @param request: ResumeHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resumeHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ResumeHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeHoloWarehouseResponse:
        """
        @summary Resumes a virtual warehouse.
        
        @param request: ResumeHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resumeHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.ResumeHoloWarehouseRequest,
    ) -> hologram_20220601_models.ResumeHoloWarehouseResponse:
        """
        @summary Resumes a virtual warehouse.
        
        @param request: ResumeHoloWarehouseRequest
        @return: ResumeHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def resume_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ResumeHoloWarehouseRequest,
    ) -> hologram_20220601_models.ResumeHoloWarehouseResponse:
        """
        @summary Resumes a virtual warehouse.
        
        @param request: ResumeHoloWarehouseRequest
        @return: ResumeHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def resume_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        """
        @summary Resumes a suspended instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        """
        @summary Resumes a suspended instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        """
        @summary Resumes a suspended instance.
        
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_instance_with_options(instance_id, headers, runtime)

    async def resume_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        """
        @summary Resumes a suspended instance.
        
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_instance_with_options_async(instance_id, headers, runtime)

    def scale_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ScaleHoloWarehouseResponse:
        """
        @summary Scales in or out a virtual warehouse.
        
        @param request: ScaleHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scaleHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ScaleHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ScaleHoloWarehouseResponse:
        """
        @summary Scales in or out a virtual warehouse.
        
        @param request: ScaleHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scaleHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ScaleHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleHoloWarehouseRequest,
    ) -> hologram_20220601_models.ScaleHoloWarehouseResponse:
        """
        @summary Scales in or out a virtual warehouse.
        
        @param request: ScaleHoloWarehouseRequest
        @return: ScaleHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def scale_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleHoloWarehouseRequest,
    ) -> hologram_20220601_models.ScaleHoloWarehouseResponse:
        """
        @summary Scales in or out a virtual warehouse.
        
        @param request: ScaleHoloWarehouseRequest
        @return: ScaleHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def scale_instance_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ScaleInstanceResponse:
        """
        @summary Changes the specifications and storage space of a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing of Hologres, see [Billing overview](https://www.alibabacloud.com/help/zh/hologres/product-overview/billing-overview).
        During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resource specifications of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade or downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications).
        
        @param request: ScaleInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scale',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ScaleInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_instance_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ScaleInstanceResponse:
        """
        @summary Changes the specifications and storage space of a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing of Hologres, see [Billing overview](https://www.alibabacloud.com/help/zh/hologres/product-overview/billing-overview).
        During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resource specifications of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade or downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications).
        
        @param request: ScaleInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scale',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ScaleInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_instance(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleInstanceRequest,
    ) -> hologram_20220601_models.ScaleInstanceResponse:
        """
        @summary Changes the specifications and storage space of a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing of Hologres, see [Billing overview](https://www.alibabacloud.com/help/zh/hologres/product-overview/billing-overview).
        During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resource specifications of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade or downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications).
        
        @param request: ScaleInstanceRequest
        @return: ScaleInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_instance_with_options(instance_id, request, headers, runtime)

    async def scale_instance_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.ScaleInstanceRequest,
    ) -> hologram_20220601_models.ScaleInstanceResponse:
        """
        @summary Changes the specifications and storage space of a Hologres instance.
        
        @description > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        For more information about the billing of Hologres, see [Billing overview](https://www.alibabacloud.com/help/zh/hologres/product-overview/billing-overview).
        During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resource specifications of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade or downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications).
        
        @param request: ScaleInstanceRequest
        @return: ScaleInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_instance_with_options_async(instance_id, request, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, headers, runtime)

    def suspend_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.SuspendHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.SuspendHoloWarehouseResponse:
        """
        @summary Suspends a virtual warehouse.
        
        @param request: SuspendHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/suspendHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.SuspendHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.SuspendHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.SuspendHoloWarehouseResponse:
        """
        @summary Suspends a virtual warehouse.
        
        @param request: SuspendHoloWarehouseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendHoloWarehouseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendHoloWarehouse',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/suspendHoloWarehouse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.SuspendHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_holo_warehouse(
        self,
        instance_id: str,
        request: hologram_20220601_models.SuspendHoloWarehouseRequest,
    ) -> hologram_20220601_models.SuspendHoloWarehouseResponse:
        """
        @summary Suspends a virtual warehouse.
        
        @param request: SuspendHoloWarehouseRequest
        @return: SuspendHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.suspend_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def suspend_holo_warehouse_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.SuspendHoloWarehouseRequest,
    ) -> hologram_20220601_models.SuspendHoloWarehouseResponse:
        """
        @summary Suspends a virtual warehouse.
        
        @param request: SuspendHoloWarehouseRequest
        @return: SuspendHoloWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.suspend_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def update_instance_name_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        """
        @summary Changes the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/instanceName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        """
        @summary Changes the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/instanceName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        """
        @summary Changes the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(instance_id, request, headers, runtime)

    async def update_instance_name_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        """
        @summary Changes the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(instance_id, request, headers, runtime)

    def update_instance_network_type_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        """
        @summary Modifies the network configuration of an instance.
        
        @param request: UpdateInstanceNetworkTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not UtilClient.is_unset(request.network_types):
            body['networkTypes'] = request.network_types
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetworkType',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/network',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_network_type_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        """
        @summary Modifies the network configuration of an instance.
        
        @param request: UpdateInstanceNetworkTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not UtilClient.is_unset(request.network_types):
            body['networkTypes'] = request.network_types
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetworkType',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/network',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_network_type(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        """
        @summary Modifies the network configuration of an instance.
        
        @param request: UpdateInstanceNetworkTypeRequest
        @return: UpdateInstanceNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_network_type_with_options(instance_id, request, headers, runtime)

    async def update_instance_network_type_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        """
        @summary Modifies the network configuration of an instance.
        
        @param request: UpdateInstanceNetworkTypeRequest
        @return: UpdateInstanceNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_network_type_with_options_async(instance_id, request, headers, runtime)
