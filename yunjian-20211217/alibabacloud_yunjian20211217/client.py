# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yunjian20211217 import models as yunjian_20211217_models
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
        self._endpoint = self.get_endpoint('yunjian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_demand_plan_with_options(
        self,
        request: yunjian_20211217_models.CreateDemandPlanRequest,
        headers: yunjian_20211217_models.CreateDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.CreateDemandPlanResponse:
        """
        @param request: CreateDemandPlanRequest
        @param headers: CreateDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.target_cid):
            body['targetCid'] = request.target_cid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveUrgentDemandPlanItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.CreateDemandPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_demand_plan_with_options_async(
        self,
        request: yunjian_20211217_models.CreateDemandPlanRequest,
        headers: yunjian_20211217_models.CreateDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.CreateDemandPlanResponse:
        """
        @param request: CreateDemandPlanRequest
        @param headers: CreateDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.target_cid):
            body['targetCid'] = request.target_cid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveUrgentDemandPlanItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.CreateDemandPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_demand_plan(
        self,
        request: yunjian_20211217_models.CreateDemandPlanRequest,
    ) -> yunjian_20211217_models.CreateDemandPlanResponse:
        """
        @param request: CreateDemandPlanRequest
        @return: CreateDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.CreateDemandPlanHeaders()
        return self.create_demand_plan_with_options(request, headers, runtime)

    async def create_demand_plan_async(
        self,
        request: yunjian_20211217_models.CreateDemandPlanRequest,
    ) -> yunjian_20211217_models.CreateDemandPlanResponse:
        """
        @param request: CreateDemandPlanRequest
        @return: CreateDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.CreateDemandPlanHeaders()
        return await self.create_demand_plan_with_options_async(request, headers, runtime)

    def create_demand_plan_v2with_options(
        self,
        request: yunjian_20211217_models.CreateDemandPlanV2Request,
        headers: yunjian_20211217_models.CreateDemandPlanV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.CreateDemandPlanV2Response:
        """
        @summary 创建plan2.0版本
        
        @param request: CreateDemandPlanV2Request
        @param headers: CreateDemandPlanV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDemandPlanV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        if not UtilClient.is_unset(request.target_cid):
            body['targetCid'] = request.target_cid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDemandPlanV2',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.CreateDemandPlanV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_demand_plan_v2with_options_async(
        self,
        request: yunjian_20211217_models.CreateDemandPlanV2Request,
        headers: yunjian_20211217_models.CreateDemandPlanV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.CreateDemandPlanV2Response:
        """
        @summary 创建plan2.0版本
        
        @param request: CreateDemandPlanV2Request
        @param headers: CreateDemandPlanV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDemandPlanV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        if not UtilClient.is_unset(request.target_cid):
            body['targetCid'] = request.target_cid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDemandPlanV2',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.CreateDemandPlanV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_demand_plan_v2(
        self,
        request: yunjian_20211217_models.CreateDemandPlanV2Request,
    ) -> yunjian_20211217_models.CreateDemandPlanV2Response:
        """
        @summary 创建plan2.0版本
        
        @param request: CreateDemandPlanV2Request
        @return: CreateDemandPlanV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.CreateDemandPlanV2Headers()
        return self.create_demand_plan_v2with_options(request, headers, runtime)

    async def create_demand_plan_v2_async(
        self,
        request: yunjian_20211217_models.CreateDemandPlanV2Request,
    ) -> yunjian_20211217_models.CreateDemandPlanV2Response:
        """
        @summary 创建plan2.0版本
        
        @param request: CreateDemandPlanV2Request
        @return: CreateDemandPlanV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.CreateDemandPlanV2Headers()
        return await self.create_demand_plan_v2with_options_async(request, headers, runtime)

    def delete_urgent_demand_item_with_options(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandItemRequest,
        headers: yunjian_20211217_models.DeleteUrgentDemandItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeleteUrgentDemandItemResponse:
        """
        @summary 紧急需求单ite 删除
        
        @param request: DeleteUrgentDemandItemRequest
        @param headers: DeleteUrgentDemandItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUrgentDemandItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUrgentDemandItem',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/deleteUrgentDemandItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeleteUrgentDemandItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_urgent_demand_item_with_options_async(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandItemRequest,
        headers: yunjian_20211217_models.DeleteUrgentDemandItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeleteUrgentDemandItemResponse:
        """
        @summary 紧急需求单ite 删除
        
        @param request: DeleteUrgentDemandItemRequest
        @param headers: DeleteUrgentDemandItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUrgentDemandItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUrgentDemandItem',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/deleteUrgentDemandItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeleteUrgentDemandItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_urgent_demand_item(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandItemRequest,
    ) -> yunjian_20211217_models.DeleteUrgentDemandItemResponse:
        """
        @summary 紧急需求单ite 删除
        
        @param request: DeleteUrgentDemandItemRequest
        @return: DeleteUrgentDemandItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeleteUrgentDemandItemHeaders()
        return self.delete_urgent_demand_item_with_options(request, headers, runtime)

    async def delete_urgent_demand_item_async(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandItemRequest,
    ) -> yunjian_20211217_models.DeleteUrgentDemandItemResponse:
        """
        @summary 紧急需求单ite 删除
        
        @param request: DeleteUrgentDemandItemRequest
        @return: DeleteUrgentDemandItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeleteUrgentDemandItemHeaders()
        return await self.delete_urgent_demand_item_with_options_async(request, headers, runtime)

    def delete_urgent_demand_plan_with_options(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandPlanRequest,
        headers: yunjian_20211217_models.DeleteUrgentDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeleteUrgentDemandPlanResponse:
        """
        @summary 紧急需求单plan删除
        
        @param request: DeleteUrgentDemandPlanRequest
        @param headers: DeleteUrgentDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUrgentDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUrgentDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/deleteUrgentDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeleteUrgentDemandPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_urgent_demand_plan_with_options_async(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandPlanRequest,
        headers: yunjian_20211217_models.DeleteUrgentDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeleteUrgentDemandPlanResponse:
        """
        @summary 紧急需求单plan删除
        
        @param request: DeleteUrgentDemandPlanRequest
        @param headers: DeleteUrgentDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUrgentDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUrgentDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/deleteUrgentDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeleteUrgentDemandPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_urgent_demand_plan(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandPlanRequest,
    ) -> yunjian_20211217_models.DeleteUrgentDemandPlanResponse:
        """
        @summary 紧急需求单plan删除
        
        @param request: DeleteUrgentDemandPlanRequest
        @return: DeleteUrgentDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeleteUrgentDemandPlanHeaders()
        return self.delete_urgent_demand_plan_with_options(request, headers, runtime)

    async def delete_urgent_demand_plan_async(
        self,
        request: yunjian_20211217_models.DeleteUrgentDemandPlanRequest,
    ) -> yunjian_20211217_models.DeleteUrgentDemandPlanResponse:
        """
        @summary 紧急需求单plan删除
        
        @param request: DeleteUrgentDemandPlanRequest
        @return: DeleteUrgentDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeleteUrgentDemandPlanHeaders()
        return await self.delete_urgent_demand_plan_with_options_async(request, headers, runtime)

    def delivery_item_detail_syn_with_options(
        self,
        request: yunjian_20211217_models.DeliveryItemDetailSynRequest,
        headers: yunjian_20211217_models.DeliveryItemDetailSynHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeliveryItemDetailSynResponse:
        """
        @summary 交付信息同步
        
        @param request: DeliveryItemDetailSynRequest
        @param headers: DeliveryItemDetailSynHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeliveryItemDetailSynResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.delivery_item_detail_dtos):
            body['deliveryItemDetailDTOS'] = request.delivery_item_detail_dtos
        if not UtilClient.is_unset(request.delivery_item_id):
            body['deliveryItemId'] = request.delivery_item_id
        if not UtilClient.is_unset(request.delivery_plan_id):
            body['deliveryPlanId'] = request.delivery_plan_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeliveryItemDetailSyn',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/deliveryItemDataSync',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeliveryItemDetailSynResponse(),
            self.call_api(params, req, runtime)
        )

    async def delivery_item_detail_syn_with_options_async(
        self,
        request: yunjian_20211217_models.DeliveryItemDetailSynRequest,
        headers: yunjian_20211217_models.DeliveryItemDetailSynHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.DeliveryItemDetailSynResponse:
        """
        @summary 交付信息同步
        
        @param request: DeliveryItemDetailSynRequest
        @param headers: DeliveryItemDetailSynHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeliveryItemDetailSynResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.delivery_item_detail_dtos):
            body['deliveryItemDetailDTOS'] = request.delivery_item_detail_dtos
        if not UtilClient.is_unset(request.delivery_item_id):
            body['deliveryItemId'] = request.delivery_item_id
        if not UtilClient.is_unset(request.delivery_plan_id):
            body['deliveryPlanId'] = request.delivery_plan_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeliveryItemDetailSyn',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/deliveryItemDataSync',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.DeliveryItemDetailSynResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delivery_item_detail_syn(
        self,
        request: yunjian_20211217_models.DeliveryItemDetailSynRequest,
    ) -> yunjian_20211217_models.DeliveryItemDetailSynResponse:
        """
        @summary 交付信息同步
        
        @param request: DeliveryItemDetailSynRequest
        @return: DeliveryItemDetailSynResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeliveryItemDetailSynHeaders()
        return self.delivery_item_detail_syn_with_options(request, headers, runtime)

    async def delivery_item_detail_syn_async(
        self,
        request: yunjian_20211217_models.DeliveryItemDetailSynRequest,
    ) -> yunjian_20211217_models.DeliveryItemDetailSynResponse:
        """
        @summary 交付信息同步
        
        @param request: DeliveryItemDetailSynRequest
        @return: DeliveryItemDetailSynResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.DeliveryItemDetailSynHeaders()
        return await self.delivery_item_detail_syn_with_options_async(request, headers, runtime)

    def get_urgent_demand_item_list_with_options(
        self,
        request: yunjian_20211217_models.GetUrgentDemandItemListRequest,
        headers: yunjian_20211217_models.GetUrgentDemandItemListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandItemListResponse:
        """
        @summary 查询报备单中报备项列表
        
        @param request: GetUrgentDemandItemListRequest
        @param headers: GetUrgentDemandItemListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandItemListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.commodity_type_code):
            body['commodityTypeCode'] = request.commodity_type_code
        if not UtilClient.is_unset(request.current):
            body['current'] = request.current
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandItemList',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandItemList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_urgent_demand_item_list_with_options_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandItemListRequest,
        headers: yunjian_20211217_models.GetUrgentDemandItemListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandItemListResponse:
        """
        @summary 查询报备单中报备项列表
        
        @param request: GetUrgentDemandItemListRequest
        @param headers: GetUrgentDemandItemListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandItemListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.commodity_type_code):
            body['commodityTypeCode'] = request.commodity_type_code
        if not UtilClient.is_unset(request.current):
            body['current'] = request.current
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandItemList',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandItemList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_urgent_demand_item_list(
        self,
        request: yunjian_20211217_models.GetUrgentDemandItemListRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandItemListResponse:
        """
        @summary 查询报备单中报备项列表
        
        @param request: GetUrgentDemandItemListRequest
        @return: GetUrgentDemandItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandItemListHeaders()
        return self.get_urgent_demand_item_list_with_options(request, headers, runtime)

    async def get_urgent_demand_item_list_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandItemListRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandItemListResponse:
        """
        @summary 查询报备单中报备项列表
        
        @param request: GetUrgentDemandItemListRequest
        @return: GetUrgentDemandItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandItemListHeaders()
        return await self.get_urgent_demand_item_list_with_options_async(request, headers, runtime)

    def get_urgent_demand_plan_detail_with_options(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanDetailRequest,
        headers: yunjian_20211217_models.GetUrgentDemandPlanDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanDetailResponse:
        """
        @summary getUrgentDemandPlanDetail
        
        @param request: GetUrgentDemandPlanDetailRequest
        @param headers: GetUrgentDemandPlanDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandPlanDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandPlanDetail',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandPlanDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_urgent_demand_plan_detail_with_options_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanDetailRequest,
        headers: yunjian_20211217_models.GetUrgentDemandPlanDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanDetailResponse:
        """
        @summary getUrgentDemandPlanDetail
        
        @param request: GetUrgentDemandPlanDetailRequest
        @param headers: GetUrgentDemandPlanDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandPlanDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandPlanDetail',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandPlanDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandPlanDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_urgent_demand_plan_detail(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanDetailRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanDetailResponse:
        """
        @summary getUrgentDemandPlanDetail
        
        @param request: GetUrgentDemandPlanDetailRequest
        @return: GetUrgentDemandPlanDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandPlanDetailHeaders()
        return self.get_urgent_demand_plan_detail_with_options(request, headers, runtime)

    async def get_urgent_demand_plan_detail_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanDetailRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanDetailResponse:
        """
        @summary getUrgentDemandPlanDetail
        
        @param request: GetUrgentDemandPlanDetailRequest
        @return: GetUrgentDemandPlanDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandPlanDetailHeaders()
        return await self.get_urgent_demand_plan_detail_with_options_async(request, headers, runtime)

    def get_urgent_demand_plan_list_with_options(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanListRequest,
        headers: yunjian_20211217_models.GetUrgentDemandPlanListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanListResponse:
        """
        @summary 查询报备单列表
        
        @param request: GetUrgentDemandPlanListRequest
        @param headers: GetUrgentDemandPlanListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandPlanListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['current'] = request.current
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.plan_type):
            body['planType'] = request.plan_type
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandPlanList',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandPlanList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandPlanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_urgent_demand_plan_list_with_options_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanListRequest,
        headers: yunjian_20211217_models.GetUrgentDemandPlanListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanListResponse:
        """
        @summary 查询报备单列表
        
        @param request: GetUrgentDemandPlanListRequest
        @param headers: GetUrgentDemandPlanListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUrgentDemandPlanListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['current'] = request.current
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.plan_type):
            body['planType'] = request.plan_type
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUrgentDemandPlanList',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/getUrgentDemandPlanList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.GetUrgentDemandPlanListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_urgent_demand_plan_list(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanListRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanListResponse:
        """
        @summary 查询报备单列表
        
        @param request: GetUrgentDemandPlanListRequest
        @return: GetUrgentDemandPlanListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandPlanListHeaders()
        return self.get_urgent_demand_plan_list_with_options(request, headers, runtime)

    async def get_urgent_demand_plan_list_async(
        self,
        request: yunjian_20211217_models.GetUrgentDemandPlanListRequest,
    ) -> yunjian_20211217_models.GetUrgentDemandPlanListResponse:
        """
        @summary 查询报备单列表
        
        @param request: GetUrgentDemandPlanListRequest
        @return: GetUrgentDemandPlanListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.GetUrgentDemandPlanListHeaders()
        return await self.get_urgent_demand_plan_list_with_options_async(request, headers, runtime)

    def push_resource_plan_with_options(
        self,
        request: yunjian_20211217_models.PushResourcePlanRequest,
        headers: yunjian_20211217_models.PushResourcePlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.PushResourcePlanResponse:
        """
        @summary ecs资源方案
        
        @param request: PushResourcePlanRequest
        @param headers: PushResourcePlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushResourcePlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.buffer_cnt):
            body['bufferCnt'] = request.buffer_cnt
        if not UtilClient.is_unset(request.demand_count):
            body['demandCount'] = request.demand_count
        if not UtilClient.is_unset(request.demand_id):
            body['demandId'] = request.demand_id
        if not UtilClient.is_unset(request.method_list):
            body['methodList'] = request.method_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.require_cnt):
            body['requireCnt'] = request.require_cnt
        if not UtilClient.is_unset(request.sub_demand_id):
            body['subDemandId'] = request.sub_demand_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushResourcePlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/resourcePlan/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.PushResourcePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_resource_plan_with_options_async(
        self,
        request: yunjian_20211217_models.PushResourcePlanRequest,
        headers: yunjian_20211217_models.PushResourcePlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.PushResourcePlanResponse:
        """
        @summary ecs资源方案
        
        @param request: PushResourcePlanRequest
        @param headers: PushResourcePlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushResourcePlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.buffer_cnt):
            body['bufferCnt'] = request.buffer_cnt
        if not UtilClient.is_unset(request.demand_count):
            body['demandCount'] = request.demand_count
        if not UtilClient.is_unset(request.demand_id):
            body['demandId'] = request.demand_id
        if not UtilClient.is_unset(request.method_list):
            body['methodList'] = request.method_list
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.require_cnt):
            body['requireCnt'] = request.require_cnt
        if not UtilClient.is_unset(request.sub_demand_id):
            body['subDemandId'] = request.sub_demand_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushResourcePlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/resourcePlan/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.PushResourcePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_resource_plan(
        self,
        request: yunjian_20211217_models.PushResourcePlanRequest,
    ) -> yunjian_20211217_models.PushResourcePlanResponse:
        """
        @summary ecs资源方案
        
        @param request: PushResourcePlanRequest
        @return: PushResourcePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.PushResourcePlanHeaders()
        return self.push_resource_plan_with_options(request, headers, runtime)

    async def push_resource_plan_async(
        self,
        request: yunjian_20211217_models.PushResourcePlanRequest,
    ) -> yunjian_20211217_models.PushResourcePlanResponse:
        """
        @summary ecs资源方案
        
        @param request: PushResourcePlanRequest
        @return: PushResourcePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.PushResourcePlanHeaders()
        return await self.push_resource_plan_with_options_async(request, headers, runtime)

    def query_delivered_supply_items_with_options(
        self,
        request: yunjian_20211217_models.QueryDeliveredSupplyItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.QueryDeliveredSupplyItemsResponse:
        """
        @summary 查询accountId下所有存在交付状态（包括部分）的报备数据, 以及开通数据情况
        
        @param request: QueryDeliveredSupplyItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeliveredSupplyItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.commodity_type_code):
            query['commodityTypeCode'] = request.commodity_type_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeliveredSupplyItems',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/queryDeliveredSupplyItems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.QueryDeliveredSupplyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_delivered_supply_items_with_options_async(
        self,
        request: yunjian_20211217_models.QueryDeliveredSupplyItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.QueryDeliveredSupplyItemsResponse:
        """
        @summary 查询accountId下所有存在交付状态（包括部分）的报备数据, 以及开通数据情况
        
        @param request: QueryDeliveredSupplyItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeliveredSupplyItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.commodity_type_code):
            query['commodityTypeCode'] = request.commodity_type_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeliveredSupplyItems',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/supply/queryDeliveredSupplyItems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.QueryDeliveredSupplyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_delivered_supply_items(
        self,
        request: yunjian_20211217_models.QueryDeliveredSupplyItemsRequest,
    ) -> yunjian_20211217_models.QueryDeliveredSupplyItemsResponse:
        """
        @summary 查询accountId下所有存在交付状态（包括部分）的报备数据, 以及开通数据情况
        
        @param request: QueryDeliveredSupplyItemsRequest
        @return: QueryDeliveredSupplyItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_delivered_supply_items_with_options(request, headers, runtime)

    async def query_delivered_supply_items_async(
        self,
        request: yunjian_20211217_models.QueryDeliveredSupplyItemsRequest,
    ) -> yunjian_20211217_models.QueryDeliveredSupplyItemsResponse:
        """
        @summary 查询accountId下所有存在交付状态（包括部分）的报备数据, 以及开通数据情况
        
        @param request: QueryDeliveredSupplyItemsRequest
        @return: QueryDeliveredSupplyItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_delivered_supply_items_with_options_async(request, headers, runtime)

    def query_period_budget_bill_with_options(
        self,
        request: yunjian_20211217_models.QueryPeriodBudgetBillRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.QueryPeriodBudgetBillResponse:
        """
        @summary 查询账单预算数据
        
        @param request: QueryPeriodBudgetBillRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPeriodBudgetBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_ids):
            query['objectIds'] = request.object_ids
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        if not UtilClient.is_unset(request.period):
            query['period'] = request.period
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPeriodBudgetBill',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/annual/budget/queryPeriodBudgetBill',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.QueryPeriodBudgetBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_period_budget_bill_with_options_async(
        self,
        request: yunjian_20211217_models.QueryPeriodBudgetBillRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.QueryPeriodBudgetBillResponse:
        """
        @summary 查询账单预算数据
        
        @param request: QueryPeriodBudgetBillRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPeriodBudgetBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_ids):
            query['objectIds'] = request.object_ids
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        if not UtilClient.is_unset(request.period):
            query['period'] = request.period
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPeriodBudgetBill',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/annual/budget/queryPeriodBudgetBill',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.QueryPeriodBudgetBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_period_budget_bill(
        self,
        request: yunjian_20211217_models.QueryPeriodBudgetBillRequest,
    ) -> yunjian_20211217_models.QueryPeriodBudgetBillResponse:
        """
        @summary 查询账单预算数据
        
        @param request: QueryPeriodBudgetBillRequest
        @return: QueryPeriodBudgetBillResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_period_budget_bill_with_options(request, headers, runtime)

    async def query_period_budget_bill_async(
        self,
        request: yunjian_20211217_models.QueryPeriodBudgetBillRequest,
    ) -> yunjian_20211217_models.QueryPeriodBudgetBillResponse:
        """
        @summary 查询账单预算数据
        
        @param request: QueryPeriodBudgetBillRequest
        @return: QueryPeriodBudgetBillResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_period_budget_bill_with_options_async(request, headers, runtime)

    def save_urgent_demand_item_with_options(
        self,
        request: yunjian_20211217_models.SaveUrgentDemandItemRequest,
        headers: yunjian_20211217_models.SaveUrgentDemandItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.SaveUrgentDemandItemResponse:
        """
        @summary 紧急需求单item新增
        
        @param request: SaveUrgentDemandItemRequest
        @param headers: SaveUrgentDemandItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveUrgentDemandItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.effect_time):
            body['effectTime'] = request.effect_time
        if not UtilClient.is_unset(request.modifier):
            body['modifier'] = request.modifier
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.pay_duration):
            body['payDuration'] = request.pay_duration
        if not UtilClient.is_unset(request.pay_duration_unit):
            body['payDurationUnit'] = request.pay_duration_unit
        if not UtilClient.is_unset(request.pay_type):
            body['payType'] = request.pay_type
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.urgent_demand_ebs_request):
            body['urgentDemandEbsRequest'] = request.urgent_demand_ebs_request
        if not UtilClient.is_unset(request.urgent_demand_ecs_request):
            body['urgentDemandEcsRequest'] = request.urgent_demand_ecs_request
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveUrgentDemandItem',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveUrgentDemandItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.SaveUrgentDemandItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_urgent_demand_item_with_options_async(
        self,
        request: yunjian_20211217_models.SaveUrgentDemandItemRequest,
        headers: yunjian_20211217_models.SaveUrgentDemandItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.SaveUrgentDemandItemResponse:
        """
        @summary 紧急需求单item新增
        
        @param request: SaveUrgentDemandItemRequest
        @param headers: SaveUrgentDemandItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveUrgentDemandItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.effect_time):
            body['effectTime'] = request.effect_time
        if not UtilClient.is_unset(request.modifier):
            body['modifier'] = request.modifier
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.pay_duration):
            body['payDuration'] = request.pay_duration
        if not UtilClient.is_unset(request.pay_duration_unit):
            body['payDurationUnit'] = request.pay_duration_unit
        if not UtilClient.is_unset(request.pay_type):
            body['payType'] = request.pay_type
        if not UtilClient.is_unset(request.plan_id):
            body['planId'] = request.plan_id
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.urgent_demand_ebs_request):
            body['urgentDemandEbsRequest'] = request.urgent_demand_ebs_request
        if not UtilClient.is_unset(request.urgent_demand_ecs_request):
            body['urgentDemandEcsRequest'] = request.urgent_demand_ecs_request
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveUrgentDemandItem',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/saveUrgentDemandItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.SaveUrgentDemandItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_urgent_demand_item(
        self,
        request: yunjian_20211217_models.SaveUrgentDemandItemRequest,
    ) -> yunjian_20211217_models.SaveUrgentDemandItemResponse:
        """
        @summary 紧急需求单item新增
        
        @param request: SaveUrgentDemandItemRequest
        @return: SaveUrgentDemandItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.SaveUrgentDemandItemHeaders()
        return self.save_urgent_demand_item_with_options(request, headers, runtime)

    async def save_urgent_demand_item_async(
        self,
        request: yunjian_20211217_models.SaveUrgentDemandItemRequest,
    ) -> yunjian_20211217_models.SaveUrgentDemandItemResponse:
        """
        @summary 紧急需求单item新增
        
        @param request: SaveUrgentDemandItemRequest
        @return: SaveUrgentDemandItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.SaveUrgentDemandItemHeaders()
        return await self.save_urgent_demand_item_with_options_async(request, headers, runtime)

    def submit_urgent_demand_plan_with_options(
        self,
        request: yunjian_20211217_models.SubmitUrgentDemandPlanRequest,
        headers: yunjian_20211217_models.SubmitUrgentDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.SubmitUrgentDemandPlanResponse:
        """
        @summary submitUrgentDemandPlan
        
        @param request: SubmitUrgentDemandPlanRequest
        @param headers: SubmitUrgentDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitUrgentDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['planId'] = request.plan_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitUrgentDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/submitUrgentDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.SubmitUrgentDemandPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_urgent_demand_plan_with_options_async(
        self,
        request: yunjian_20211217_models.SubmitUrgentDemandPlanRequest,
        headers: yunjian_20211217_models.SubmitUrgentDemandPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.SubmitUrgentDemandPlanResponse:
        """
        @summary submitUrgentDemandPlan
        
        @param request: SubmitUrgentDemandPlanRequest
        @param headers: SubmitUrgentDemandPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitUrgentDemandPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['planId'] = request.plan_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.yun_user_id):
            real_headers['Yun-User-Id'] = UtilClient.to_jsonstring(headers.yun_user_id)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitUrgentDemandPlan',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/api/demand/urgent/submitUrgentDemandPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.SubmitUrgentDemandPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_urgent_demand_plan(
        self,
        request: yunjian_20211217_models.SubmitUrgentDemandPlanRequest,
    ) -> yunjian_20211217_models.SubmitUrgentDemandPlanResponse:
        """
        @summary submitUrgentDemandPlan
        
        @param request: SubmitUrgentDemandPlanRequest
        @return: SubmitUrgentDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.SubmitUrgentDemandPlanHeaders()
        return self.submit_urgent_demand_plan_with_options(request, headers, runtime)

    async def submit_urgent_demand_plan_async(
        self,
        request: yunjian_20211217_models.SubmitUrgentDemandPlanRequest,
    ) -> yunjian_20211217_models.SubmitUrgentDemandPlanResponse:
        """
        @summary submitUrgentDemandPlan
        
        @param request: SubmitUrgentDemandPlanRequest
        @return: SubmitUrgentDemandPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = yunjian_20211217_models.SubmitUrgentDemandPlanHeaders()
        return await self.submit_urgent_demand_plan_with_options_async(request, headers, runtime)

    def accept_fulfillment_decision_with_options(
        self,
        request: yunjian_20211217_models.AcceptFulfillmentDecisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.AcceptFulfillmentDecisionResponse:
        """
        @summary 云产品交付决策反馈回调
        
        @param request: AcceptFulfillmentDecisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptFulfillmentDecisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.decision_conclusion):
            body['DecisionConclusion'] = request.decision_conclusion
        if not UtilClient.is_unset(request.decision_type):
            body['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='acceptFulfillmentDecision',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/acceptFulfillmentDecision',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.AcceptFulfillmentDecisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_fulfillment_decision_with_options_async(
        self,
        request: yunjian_20211217_models.AcceptFulfillmentDecisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yunjian_20211217_models.AcceptFulfillmentDecisionResponse:
        """
        @summary 云产品交付决策反馈回调
        
        @param request: AcceptFulfillmentDecisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptFulfillmentDecisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.decision_conclusion):
            body['DecisionConclusion'] = request.decision_conclusion
        if not UtilClient.is_unset(request.decision_type):
            body['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='acceptFulfillmentDecision',
            version='2021-12-17',
            protocol='HTTPS',
            pathname=f'/acceptFulfillmentDecision',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yunjian_20211217_models.AcceptFulfillmentDecisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_fulfillment_decision(
        self,
        request: yunjian_20211217_models.AcceptFulfillmentDecisionRequest,
    ) -> yunjian_20211217_models.AcceptFulfillmentDecisionResponse:
        """
        @summary 云产品交付决策反馈回调
        
        @param request: AcceptFulfillmentDecisionRequest
        @return: AcceptFulfillmentDecisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.accept_fulfillment_decision_with_options(request, headers, runtime)

    async def accept_fulfillment_decision_async(
        self,
        request: yunjian_20211217_models.AcceptFulfillmentDecisionRequest,
    ) -> yunjian_20211217_models.AcceptFulfillmentDecisionResponse:
        """
        @summary 云产品交付决策反馈回调
        
        @param request: AcceptFulfillmentDecisionRequest
        @return: AcceptFulfillmentDecisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.accept_fulfillment_decision_with_options_async(request, headers, runtime)
