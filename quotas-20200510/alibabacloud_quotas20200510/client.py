# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_quotas20200510 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('quotas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_quota_alarm_with_options(
        self,
        request: main_models.CreateQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.original_context):
            body['OriginalContext'] = request.original_context
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        if not DaraCore.is_null(request.threshold):
            body['Threshold'] = request.threshold
        if not DaraCore.is_null(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not DaraCore.is_null(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not DaraCore.is_null(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_alarm_with_options_async(
        self,
        request: main_models.CreateQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.original_context):
            body['OriginalContext'] = request.original_context
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        if not DaraCore.is_null(request.threshold):
            body['Threshold'] = request.threshold
        if not DaraCore.is_null(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not DaraCore.is_null(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not DaraCore.is_null(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_alarm(
        self,
        request: main_models.CreateQuotaAlarmRequest,
    ) -> main_models.CreateQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return self.create_quota_alarm_with_options(request, runtime)

    async def create_quota_alarm_async(
        self,
        request: main_models.CreateQuotaAlarmRequest,
    ) -> main_models.CreateQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return await self.create_quota_alarm_with_options_async(request, runtime)

    def create_quota_application_with_options(
        self,
        request: main_models.CreateQuotaApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.audit_mode):
            body['AuditMode'] = request.audit_mode
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaApplication',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_application_with_options_async(
        self,
        request: main_models.CreateQuotaApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.audit_mode):
            body['AuditMode'] = request.audit_mode
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaApplication',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_application(
        self,
        request: main_models.CreateQuotaApplicationRequest,
    ) -> main_models.CreateQuotaApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_quota_application_with_options(request, runtime)

    async def create_quota_application_async(
        self,
        request: main_models.CreateQuotaApplicationRequest,
    ) -> main_models.CreateQuotaApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_quota_application_with_options_async(request, runtime)

    def create_quota_applications_for_template_with_options(
        self,
        request: main_models.CreateQuotaApplicationsForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaApplicationsForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_uids):
            body['AliyunUids'] = request.aliyun_uids
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaApplicationsForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaApplicationsForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_applications_for_template_with_options_async(
        self,
        request: main_models.CreateQuotaApplicationsForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaApplicationsForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_uids):
            body['AliyunUids'] = request.aliyun_uids
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaApplicationsForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaApplicationsForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_applications_for_template(
        self,
        request: main_models.CreateQuotaApplicationsForTemplateRequest,
    ) -> main_models.CreateQuotaApplicationsForTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_quota_applications_for_template_with_options(request, runtime)

    async def create_quota_applications_for_template_async(
        self,
        request: main_models.CreateQuotaApplicationsForTemplateRequest,
    ) -> main_models.CreateQuotaApplicationsForTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_quota_applications_for_template_with_options_async(request, runtime)

    def create_template_quota_item_with_options(
        self,
        request: main_models.CreateTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateQuotaItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_quota_item_with_options_async(
        self,
        request: main_models.CreateTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateQuotaItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template_quota_item(
        self,
        request: main_models.CreateTemplateQuotaItemRequest,
    ) -> main_models.CreateTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return self.create_template_quota_item_with_options(request, runtime)

    async def create_template_quota_item_async(
        self,
        request: main_models.CreateTemplateQuotaItemRequest,
    ) -> main_models.CreateTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return await self.create_template_quota_item_with_options_async(request, runtime)

    def delete_quota_alarm_with_options(
        self,
        request: main_models.DeleteQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_alarm_with_options_async(
        self,
        request: main_models.DeleteQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota_alarm(
        self,
        request: main_models.DeleteQuotaAlarmRequest,
    ) -> main_models.DeleteQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return self.delete_quota_alarm_with_options(request, runtime)

    async def delete_quota_alarm_async(
        self,
        request: main_models.DeleteQuotaAlarmRequest,
    ) -> main_models.DeleteQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return await self.delete_quota_alarm_with_options_async(request, runtime)

    def delete_template_quota_item_with_options(
        self,
        request: main_models.DeleteTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateQuotaItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_quota_item_with_options_async(
        self,
        request: main_models.DeleteTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateQuotaItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template_quota_item(
        self,
        request: main_models.DeleteTemplateQuotaItemRequest,
    ) -> main_models.DeleteTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return self.delete_template_quota_item_with_options(request, runtime)

    async def delete_template_quota_item_async(
        self,
        request: main_models.DeleteTemplateQuotaItemRequest,
    ) -> main_models.DeleteTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_quota_item_with_options_async(request, runtime)

    def get_product_quota_with_options(
        self,
        request: main_models.GetProductQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProductQuota',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_quota_with_options_async(
        self,
        request: main_models.GetProductQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProductQuota',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_quota(
        self,
        request: main_models.GetProductQuotaRequest,
    ) -> main_models.GetProductQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_product_quota_with_options(request, runtime)

    async def get_product_quota_async(
        self,
        request: main_models.GetProductQuotaRequest,
    ) -> main_models.GetProductQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_product_quota_with_options_async(request, runtime)

    def get_product_quota_dimension_with_options(
        self,
        request: main_models.GetProductQuotaDimensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductQuotaDimensionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dependent_dimensions):
            body['DependentDimensions'] = request.dependent_dimensions
        if not DaraCore.is_null(request.dimension_key):
            body['DimensionKey'] = request.dimension_key
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProductQuotaDimension',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductQuotaDimensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_quota_dimension_with_options_async(
        self,
        request: main_models.GetProductQuotaDimensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductQuotaDimensionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dependent_dimensions):
            body['DependentDimensions'] = request.dependent_dimensions
        if not DaraCore.is_null(request.dimension_key):
            body['DimensionKey'] = request.dimension_key
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProductQuotaDimension',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductQuotaDimensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_quota_dimension(
        self,
        request: main_models.GetProductQuotaDimensionRequest,
    ) -> main_models.GetProductQuotaDimensionResponse:
        runtime = RuntimeOptions()
        return self.get_product_quota_dimension_with_options(request, runtime)

    async def get_product_quota_dimension_async(
        self,
        request: main_models.GetProductQuotaDimensionRequest,
    ) -> main_models.GetProductQuotaDimensionResponse:
        runtime = RuntimeOptions()
        return await self.get_product_quota_dimension_with_options_async(request, runtime)

    def get_quota_alarm_with_options(
        self,
        request: main_models.GetQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_alarm_with_options_async(
        self,
        request: main_models.GetQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_alarm(
        self,
        request: main_models.GetQuotaAlarmRequest,
    ) -> main_models.GetQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return self.get_quota_alarm_with_options(request, runtime)

    async def get_quota_alarm_async(
        self,
        request: main_models.GetQuotaAlarmRequest,
    ) -> main_models.GetQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_alarm_with_options_async(request, runtime)

    def get_quota_application_with_options(
        self,
        request: main_models.GetQuotaApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaApplication',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_application_with_options_async(
        self,
        request: main_models.GetQuotaApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaApplication',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_application(
        self,
        request: main_models.GetQuotaApplicationRequest,
    ) -> main_models.GetQuotaApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_quota_application_with_options(request, runtime)

    async def get_quota_application_async(
        self,
        request: main_models.GetQuotaApplicationRequest,
    ) -> main_models.GetQuotaApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_application_with_options_async(request, runtime)

    def get_quota_application_approval_with_options(
        self,
        request: main_models.GetQuotaApplicationApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaApplicationApprovalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaApplicationApproval',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaApplicationApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_application_approval_with_options_async(
        self,
        request: main_models.GetQuotaApplicationApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaApplicationApprovalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaApplicationApproval',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaApplicationApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_application_approval(
        self,
        request: main_models.GetQuotaApplicationApprovalRequest,
    ) -> main_models.GetQuotaApplicationApprovalResponse:
        runtime = RuntimeOptions()
        return self.get_quota_application_approval_with_options(request, runtime)

    async def get_quota_application_approval_async(
        self,
        request: main_models.GetQuotaApplicationApprovalRequest,
    ) -> main_models.GetQuotaApplicationApprovalResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_application_approval_with_options_async(request, runtime)

    def get_quota_template_service_status_with_options(
        self,
        request: main_models.GetQuotaTemplateServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaTemplateServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_directory_id):
            body['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaTemplateServiceStatus',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_template_service_status_with_options_async(
        self,
        request: main_models.GetQuotaTemplateServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaTemplateServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_directory_id):
            body['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaTemplateServiceStatus',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaTemplateServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_template_service_status(
        self,
        request: main_models.GetQuotaTemplateServiceStatusRequest,
    ) -> main_models.GetQuotaTemplateServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_quota_template_service_status_with_options(request, runtime)

    async def get_quota_template_service_status_async(
        self,
        request: main_models.GetQuotaTemplateServiceStatusRequest,
    ) -> main_models.GetQuotaTemplateServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_template_service_status_with_options_async(request, runtime)

    def get_quota_utilization_overview_with_options(
        self,
        request: main_models.GetQuotaUtilizationOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaUtilizationOverviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaUtilizationOverview',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaUtilizationOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_utilization_overview_with_options_async(
        self,
        request: main_models.GetQuotaUtilizationOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaUtilizationOverviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaUtilizationOverview',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaUtilizationOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_utilization_overview(
        self,
        request: main_models.GetQuotaUtilizationOverviewRequest,
    ) -> main_models.GetQuotaUtilizationOverviewResponse:
        runtime = RuntimeOptions()
        return self.get_quota_utilization_overview_with_options(request, runtime)

    async def get_quota_utilization_overview_async(
        self,
        request: main_models.GetQuotaUtilizationOverviewRequest,
    ) -> main_models.GetQuotaUtilizationOverviewResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_utilization_overview_with_options_async(request, runtime)

    def list_alarm_histories_with_options(
        self,
        request: main_models.ListAlarmHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmHistoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarmHistories',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_histories_with_options_async(
        self,
        request: main_models.ListAlarmHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlarmHistoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlarmHistories',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlarmHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_histories(
        self,
        request: main_models.ListAlarmHistoriesRequest,
    ) -> main_models.ListAlarmHistoriesResponse:
        runtime = RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    async def list_alarm_histories_async(
        self,
        request: main_models.ListAlarmHistoriesRequest,
    ) -> main_models.ListAlarmHistoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_alarm_histories_with_options_async(request, runtime)

    def list_dependent_quotas_with_options(
        self,
        request: main_models.ListDependentQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDependentQuotasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDependentQuotas',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDependentQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dependent_quotas_with_options_async(
        self,
        request: main_models.ListDependentQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDependentQuotasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDependentQuotas',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDependentQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dependent_quotas(
        self,
        request: main_models.ListDependentQuotasRequest,
    ) -> main_models.ListDependentQuotasResponse:
        runtime = RuntimeOptions()
        return self.list_dependent_quotas_with_options(request, runtime)

    async def list_dependent_quotas_async(
        self,
        request: main_models.ListDependentQuotasRequest,
    ) -> main_models.ListDependentQuotasResponse:
        runtime = RuntimeOptions()
        return await self.list_dependent_quotas_with_options_async(request, runtime)

    def list_product_dimension_groups_with_options(
        self,
        request: main_models.ListProductDimensionGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductDimensionGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductDimensionGroups',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductDimensionGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_dimension_groups_with_options_async(
        self,
        request: main_models.ListProductDimensionGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductDimensionGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductDimensionGroups',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductDimensionGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_dimension_groups(
        self,
        request: main_models.ListProductDimensionGroupsRequest,
    ) -> main_models.ListProductDimensionGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_product_dimension_groups_with_options(request, runtime)

    async def list_product_dimension_groups_async(
        self,
        request: main_models.ListProductDimensionGroupsRequest,
    ) -> main_models.ListProductDimensionGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_product_dimension_groups_with_options_async(request, runtime)

    def list_product_quota_dimensions_with_options(
        self,
        request: main_models.ListProductQuotaDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductQuotaDimensionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProductQuotaDimensions',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductQuotaDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_quota_dimensions_with_options_async(
        self,
        request: main_models.ListProductQuotaDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductQuotaDimensionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProductQuotaDimensions',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductQuotaDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_quota_dimensions(
        self,
        request: main_models.ListProductQuotaDimensionsRequest,
    ) -> main_models.ListProductQuotaDimensionsResponse:
        runtime = RuntimeOptions()
        return self.list_product_quota_dimensions_with_options(request, runtime)

    async def list_product_quota_dimensions_async(
        self,
        request: main_models.ListProductQuotaDimensionsRequest,
    ) -> main_models.ListProductQuotaDimensionsResponse:
        runtime = RuntimeOptions()
        return await self.list_product_quota_dimensions_with_options_async(request, runtime)

    def list_product_quotas_with_options(
        self,
        request: main_models.ListProductQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductQuotasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.key_word):
            body['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProductQuotas',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_quotas_with_options_async(
        self,
        request: main_models.ListProductQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductQuotasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.group_code):
            body['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.key_word):
            body['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.sort_field):
            body['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProductQuotas',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_quotas(
        self,
        request: main_models.ListProductQuotasRequest,
    ) -> main_models.ListProductQuotasResponse:
        runtime = RuntimeOptions()
        return self.list_product_quotas_with_options(request, runtime)

    async def list_product_quotas_async(
        self,
        request: main_models.ListProductQuotasRequest,
    ) -> main_models.ListProductQuotasResponse:
        runtime = RuntimeOptions()
        return await self.list_product_quotas_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_quota_alarms_with_options(
        self,
        request: main_models.ListQuotaAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaAlarmsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaAlarms',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_alarms_with_options_async(
        self,
        request: main_models.ListQuotaAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaAlarmsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaAlarms',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_alarms(
        self,
        request: main_models.ListQuotaAlarmsRequest,
    ) -> main_models.ListQuotaAlarmsResponse:
        runtime = RuntimeOptions()
        return self.list_quota_alarms_with_options(request, runtime)

    async def list_quota_alarms_async(
        self,
        request: main_models.ListQuotaAlarmsRequest,
    ) -> main_models.ListQuotaAlarmsResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_alarms_with_options_async(request, runtime)

    def list_quota_application_templates_with_options(
        self,
        request: main_models.ListQuotaApplicationTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationTemplates',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_application_templates_with_options_async(
        self,
        request: main_models.ListQuotaApplicationTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationTemplates',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_application_templates(
        self,
        request: main_models.ListQuotaApplicationTemplatesRequest,
    ) -> main_models.ListQuotaApplicationTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_quota_application_templates_with_options(request, runtime)

    async def list_quota_application_templates_async(
        self,
        request: main_models.ListQuotaApplicationTemplatesRequest,
    ) -> main_models.ListQuotaApplicationTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_application_templates_with_options_async(request, runtime)

    def list_quota_applications_with_options(
        self,
        request: main_models.ListQuotaApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.key_word):
            body['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplications',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_with_options_async(
        self,
        request: main_models.ListQuotaApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.key_word):
            body['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplications',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications(
        self,
        request: main_models.ListQuotaApplicationsRequest,
    ) -> main_models.ListQuotaApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_quota_applications_with_options(request, runtime)

    async def list_quota_applications_async(
        self,
        request: main_models.ListQuotaApplicationsRequest,
    ) -> main_models.ListQuotaApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_applications_with_options_async(request, runtime)

    def list_quota_applications_detail_for_template_with_options(
        self,
        request: main_models.ListQuotaApplicationsDetailForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsDetailForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationsDetailForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsDetailForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_detail_for_template_with_options_async(
        self,
        request: main_models.ListQuotaApplicationsDetailForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsDetailForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not DaraCore.is_null(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationsDetailForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsDetailForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications_detail_for_template(
        self,
        request: main_models.ListQuotaApplicationsDetailForTemplateRequest,
    ) -> main_models.ListQuotaApplicationsDetailForTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_quota_applications_detail_for_template_with_options(request, runtime)

    async def list_quota_applications_detail_for_template_async(
        self,
        request: main_models.ListQuotaApplicationsDetailForTemplateRequest,
    ) -> main_models.ListQuotaApplicationsDetailForTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_applications_detail_for_template_with_options_async(request, runtime)

    def list_quota_applications_for_template_with_options(
        self,
        request: main_models.ListQuotaApplicationsForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apply_end_time):
            body['ApplyEndTime'] = request.apply_end_time
        if not DaraCore.is_null(request.apply_start_time):
            body['ApplyStartTime'] = request.apply_start_time
        if not DaraCore.is_null(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationsForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_for_template_with_options_async(
        self,
        request: main_models.ListQuotaApplicationsForTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaApplicationsForTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.apply_end_time):
            body['ApplyEndTime'] = request.apply_end_time
        if not DaraCore.is_null(request.apply_start_time):
            body['ApplyStartTime'] = request.apply_start_time
        if not DaraCore.is_null(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaApplicationsForTemplate',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaApplicationsForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications_for_template(
        self,
        request: main_models.ListQuotaApplicationsForTemplateRequest,
    ) -> main_models.ListQuotaApplicationsForTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_quota_applications_for_template_with_options(request, runtime)

    async def list_quota_applications_for_template_async(
        self,
        request: main_models.ListQuotaApplicationsForTemplateRequest,
    ) -> main_models.ListQuotaApplicationsForTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_applications_for_template_with_options_async(request, runtime)

    def list_quota_utilization_report_with_options(
        self,
        request: main_models.ListQuotaUtilizationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaUtilizationReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.adjustable):
            body['Adjustable'] = request.adjustable
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.quota_region_id):
            body['QuotaRegionId'] = request.quota_region_id
        if not DaraCore.is_null(request.utilization_statuses):
            body['UtilizationStatuses'] = request.utilization_statuses
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaUtilizationReport',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaUtilizationReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_utilization_report_with_options_async(
        self,
        request: main_models.ListQuotaUtilizationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaUtilizationReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.adjustable):
            body['Adjustable'] = request.adjustable
        if not DaraCore.is_null(request.key_words):
            body['KeyWords'] = request.key_words
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not DaraCore.is_null(request.quota_region_id):
            body['QuotaRegionId'] = request.quota_region_id
        if not DaraCore.is_null(request.utilization_statuses):
            body['UtilizationStatuses'] = request.utilization_statuses
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaUtilizationReport',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaUtilizationReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_utilization_report(
        self,
        request: main_models.ListQuotaUtilizationReportRequest,
    ) -> main_models.ListQuotaUtilizationReportResponse:
        runtime = RuntimeOptions()
        return self.list_quota_utilization_report_with_options(request, runtime)

    async def list_quota_utilization_report_async(
        self,
        request: main_models.ListQuotaUtilizationReportRequest,
    ) -> main_models.ListQuotaUtilizationReportResponse:
        runtime = RuntimeOptions()
        return await self.list_quota_utilization_report_with_options_async(request, runtime)

    def modify_quota_template_service_status_with_options(
        self,
        request: main_models.ModifyQuotaTemplateServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQuotaTemplateServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_status):
            body['ServiceStatus'] = request.service_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQuotaTemplateServiceStatus',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_quota_template_service_status_with_options_async(
        self,
        request: main_models.ModifyQuotaTemplateServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQuotaTemplateServiceStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_status):
            body['ServiceStatus'] = request.service_status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQuotaTemplateServiceStatus',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQuotaTemplateServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_quota_template_service_status(
        self,
        request: main_models.ModifyQuotaTemplateServiceStatusRequest,
    ) -> main_models.ModifyQuotaTemplateServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_quota_template_service_status_with_options(request, runtime)

    async def modify_quota_template_service_status_async(
        self,
        request: main_models.ModifyQuotaTemplateServiceStatusRequest,
    ) -> main_models.ModifyQuotaTemplateServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_quota_template_service_status_with_options_async(request, runtime)

    def modify_template_quota_item_with_options(
        self,
        request: main_models.ModifyTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateQuotaItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        body = {}
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_quota_item_with_options_async(
        self,
        request: main_models.ModifyTemplateQuotaItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateQuotaItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        body = {}
        if not DaraCore.is_null(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not DaraCore.is_null(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplateQuotaItem',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template_quota_item(
        self,
        request: main_models.ModifyTemplateQuotaItemRequest,
    ) -> main_models.ModifyTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return self.modify_template_quota_item_with_options(request, runtime)

    async def modify_template_quota_item_async(
        self,
        request: main_models.ModifyTemplateQuotaItemRequest,
    ) -> main_models.ModifyTemplateQuotaItemResponse:
        runtime = RuntimeOptions()
        return await self.modify_template_quota_item_with_options_async(request, runtime)

    def remind_quota_application_approval_with_options(
        self,
        request: main_models.RemindQuotaApplicationApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemindQuotaApplicationApprovalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemindQuotaApplicationApproval',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemindQuotaApplicationApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def remind_quota_application_approval_with_options_async(
        self,
        request: main_models.RemindQuotaApplicationApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemindQuotaApplicationApprovalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemindQuotaApplicationApproval',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemindQuotaApplicationApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remind_quota_application_approval(
        self,
        request: main_models.RemindQuotaApplicationApprovalRequest,
    ) -> main_models.RemindQuotaApplicationApprovalResponse:
        runtime = RuntimeOptions()
        return self.remind_quota_application_approval_with_options(request, runtime)

    async def remind_quota_application_approval_async(
        self,
        request: main_models.RemindQuotaApplicationApprovalRequest,
    ) -> main_models.RemindQuotaApplicationApprovalResponse:
        runtime = RuntimeOptions()
        return await self.remind_quota_application_approval_with_options_async(request, runtime)

    def start_quota_utilization_report_with_options(
        self,
        request: main_models.StartQuotaUtilizationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartQuotaUtilizationReportResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartQuotaUtilizationReport',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartQuotaUtilizationReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_quota_utilization_report_with_options_async(
        self,
        request: main_models.StartQuotaUtilizationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartQuotaUtilizationReportResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'StartQuotaUtilizationReport',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartQuotaUtilizationReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_quota_utilization_report(
        self,
        request: main_models.StartQuotaUtilizationReportRequest,
    ) -> main_models.StartQuotaUtilizationReportResponse:
        runtime = RuntimeOptions()
        return self.start_quota_utilization_report_with_options(request, runtime)

    async def start_quota_utilization_report_async(
        self,
        request: main_models.StartQuotaUtilizationReportRequest,
    ) -> main_models.StartQuotaUtilizationReportResponse:
        runtime = RuntimeOptions()
        return await self.start_quota_utilization_report_with_options_async(request, runtime)

    def update_quota_alarm_with_options(
        self,
        request: main_models.UpdateQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.threshold):
            body['Threshold'] = request.threshold
        if not DaraCore.is_null(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not DaraCore.is_null(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not DaraCore.is_null(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_alarm_with_options_async(
        self,
        request: main_models.UpdateQuotaAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not DaraCore.is_null(request.threshold):
            body['Threshold'] = request.threshold
        if not DaraCore.is_null(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not DaraCore.is_null(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not DaraCore.is_null(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaAlarm',
            version = '2020-05-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_alarm(
        self,
        request: main_models.UpdateQuotaAlarmRequest,
    ) -> main_models.UpdateQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return self.update_quota_alarm_with_options(request, runtime)

    async def update_quota_alarm_async(
        self,
        request: main_models.UpdateQuotaAlarmRequest,
    ) -> main_models.UpdateQuotaAlarmResponse:
        runtime = RuntimeOptions()
        return await self.update_quota_alarm_with_options_async(request, runtime)
