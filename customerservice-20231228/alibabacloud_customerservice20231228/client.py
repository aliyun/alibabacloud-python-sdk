# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_customerservice20231228 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('customerservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def list_enterprise_support_plan_with_options(
        self,
        request: main_models.ListEnterpriseSupportPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseSupportPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseSupportPlan',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseSupportPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_support_plan_with_options_async(
        self,
        request: main_models.ListEnterpriseSupportPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseSupportPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseSupportPlan',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseSupportPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_support_plan(
        self,
        request: main_models.ListEnterpriseSupportPlanRequest,
    ) -> main_models.ListEnterpriseSupportPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_enterprise_support_plan_with_options(request, headers, runtime)

    async def list_enterprise_support_plan_async(
        self,
        request: main_models.ListEnterpriseSupportPlanRequest,
    ) -> main_models.ListEnterpriseSupportPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_enterprise_support_plan_with_options_async(request, headers, runtime)

    def list_enterprise_support_plan_simple_with_options(
        self,
        request: main_models.ListEnterpriseSupportPlanSimpleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseSupportPlanSimpleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseSupportPlanSimple',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlanSimple',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseSupportPlanSimpleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_support_plan_simple_with_options_async(
        self,
        request: main_models.ListEnterpriseSupportPlanSimpleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseSupportPlanSimpleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseSupportPlanSimple',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlanSimple',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseSupportPlanSimpleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_support_plan_simple(
        self,
        request: main_models.ListEnterpriseSupportPlanSimpleRequest,
    ) -> main_models.ListEnterpriseSupportPlanSimpleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_enterprise_support_plan_simple_with_options(request, headers, runtime)

    async def list_enterprise_support_plan_simple_async(
        self,
        request: main_models.ListEnterpriseSupportPlanSimpleRequest,
    ) -> main_models.ListEnterpriseSupportPlanSimpleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_enterprise_support_plan_simple_with_options_async(request, headers, runtime)

    def list_service_apply_with_options(
        self,
        request: main_models.ListServiceApplyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceApplyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apply_type):
            body['applyType'] = request.apply_type
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            body['productCode'] = request.product_code
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceApply',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/expert/service/listServiceApply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_apply_with_options_async(
        self,
        request: main_models.ListServiceApplyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceApplyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apply_type):
            body['applyType'] = request.apply_type
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            body['productCode'] = request.product_code
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceApply',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/expert/service/listServiceApply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_apply(
        self,
        request: main_models.ListServiceApplyRequest,
    ) -> main_models.ListServiceApplyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_apply_with_options(request, headers, runtime)

    async def list_service_apply_async(
        self,
        request: main_models.ListServiceApplyRequest,
    ) -> main_models.ListServiceApplyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_apply_with_options_async(request, headers, runtime)

    def list_yun_qi_task_by_uid_with_options(
        self,
        request: main_models.ListYunQiTaskByUidRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListYunQiTaskByUidResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['createTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['createTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.free_order_apply_codes):
            body['freeOrderApplyCodes'] = request.free_order_apply_codes
        if not DaraCore.is_null(request.free_order_apply_ids):
            body['freeOrderApplyIds'] = request.free_order_apply_ids
        if not DaraCore.is_null(request.order_ids):
            body['orderIds'] = request.order_ids
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListYunQiTaskByUid',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/record/listYunQiTaskByUid',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYunQiTaskByUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_yun_qi_task_by_uid_with_options_async(
        self,
        request: main_models.ListYunQiTaskByUidRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListYunQiTaskByUidResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['createTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['createTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.free_order_apply_codes):
            body['freeOrderApplyCodes'] = request.free_order_apply_codes
        if not DaraCore.is_null(request.free_order_apply_ids):
            body['freeOrderApplyIds'] = request.free_order_apply_ids
        if not DaraCore.is_null(request.order_ids):
            body['orderIds'] = request.order_ids
        if not DaraCore.is_null(request.page_num):
            body['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListYunQiTaskByUid',
            version = '2023-12-28',
            protocol = 'HTTPS',
            pathname = f'/customerWorkbench/pop/api/record/listYunQiTaskByUid',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYunQiTaskByUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_yun_qi_task_by_uid(
        self,
        request: main_models.ListYunQiTaskByUidRequest,
    ) -> main_models.ListYunQiTaskByUidResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_yun_qi_task_by_uid_with_options(request, headers, runtime)

    async def list_yun_qi_task_by_uid_async(
        self,
        request: main_models.ListYunQiTaskByUidRequest,
    ) -> main_models.ListYunQiTaskByUidResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_yun_qi_task_by_uid_with_options_async(request, headers, runtime)
