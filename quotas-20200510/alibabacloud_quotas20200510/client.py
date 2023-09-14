# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quotas20200510 import models as quotas_20200510_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        """
        The ID of the alert.
        
        @param request: CreateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        """
        The ID of the alert.
        
        @param request: CreateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_alarm(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        """
        The ID of the alert.
        
        @param request: CreateQuotaAlarmRequest
        @return: CreateQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quota_alarm_with_options(request, runtime)

    async def create_quota_alarm_async(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        """
        The ID of the alert.
        
        @param request: CreateQuotaAlarmRequest
        @return: CreateQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_alarm_with_options_async(request, runtime)

    def create_quota_application_with_options(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        """
        In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
        @param request: CreateQuotaApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audit_mode):
            body['AuditMode'] = request.audit_mode
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_application_with_options_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        """
        In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
        @param request: CreateQuotaApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audit_mode):
            body['AuditMode'] = request.audit_mode
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_application(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        """
        In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
        @param request: CreateQuotaApplicationRequest
        @return: CreateQuotaApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quota_application_with_options(request, runtime)

    async def create_quota_application_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        """
        In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
        @param request: CreateQuotaApplicationRequest
        @return: CreateQuotaApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_application_with_options_async(request, runtime)

    def create_quota_applications_for_template_with_options(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationsForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uids):
            body['AliyunUids'] = request.aliyun_uids
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaApplicationsForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_applications_for_template_with_options_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationsForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uids):
            body['AliyunUids'] = request.aliyun_uids
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaApplicationsForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_applications_for_template(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quota_applications_for_template_with_options(request, runtime)

    async def create_quota_applications_for_template_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_applications_for_template_with_options_async(request, runtime)

    def create_template_quota_item_with_options(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_quota_item_with_options_async(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template_quota_item(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_quota_item_with_options(request, runtime)

    async def create_template_quota_item_async(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_quota_item_with_options_async(request, runtime)

    def delete_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        """
        In this example, the operation is called to delete a quota alert whose ID is `6b512ab7-da3a-4142-b529-2b2a9294***`.
        
        @param request: DeleteQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        """
        In this example, the operation is called to delete a quota alert whose ID is `6b512ab7-da3a-4142-b529-2b2a9294***`.
        
        @param request: DeleteQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota_alarm(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        """
        In this example, the operation is called to delete a quota alert whose ID is `6b512ab7-da3a-4142-b529-2b2a9294***`.
        
        @param request: DeleteQuotaAlarmRequest
        @return: DeleteQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quota_alarm_with_options(request, runtime)

    async def delete_quota_alarm_async(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        """
        In this example, the operation is called to delete a quota alert whose ID is `6b512ab7-da3a-4142-b529-2b2a9294***`.
        
        @param request: DeleteQuotaAlarmRequest
        @return: DeleteQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_quota_alarm_with_options_async(request, runtime)

    def delete_template_quota_item_with_options(
        self,
        request: quotas_20200510_models.DeleteTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_quota_item_with_options_async(
        self,
        request: quotas_20200510_models.DeleteTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template_quota_item(
        self,
        request: quotas_20200510_models.DeleteTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.DeleteTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_quota_item_with_options(request, runtime)

    async def delete_template_quota_item_async(
        self,
        request: quotas_20200510_models.DeleteTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.DeleteTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_quota_item_with_options_async(request, runtime)

    def get_product_quota_with_options(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        """
        In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
        @param request: GetProductQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuota',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_quota_with_options_async(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        """
        In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
        @param request: GetProductQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuota',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_quota(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        """
        In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
        @param request: GetProductQuotaRequest
        @return: GetProductQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_with_options(request, runtime)

    async def get_product_quota_async(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        """
        In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
        @param request: GetProductQuotaRequest
        @return: GetProductQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_product_quota_with_options_async(request, runtime)

    def get_product_quota_dimension_with_options(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        """
        In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        *   The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   The name of the quota dimension is `region`.
        
        @param request: GetProductQuotaDimensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductQuotaDimensionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dependent_dimensions):
            body['DependentDimensions'] = request.dependent_dimensions
        if not UtilClient.is_unset(request.dimension_key):
            body['DimensionKey'] = request.dimension_key
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuotaDimension',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaDimensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_quota_dimension_with_options_async(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        """
        In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        *   The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   The name of the quota dimension is `region`.
        
        @param request: GetProductQuotaDimensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductQuotaDimensionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dependent_dimensions):
            body['DependentDimensions'] = request.dependent_dimensions
        if not UtilClient.is_unset(request.dimension_key):
            body['DimensionKey'] = request.dimension_key
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuotaDimension',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaDimensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_quota_dimension(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        """
        In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        *   The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   The name of the quota dimension is `region`.
        
        @param request: GetProductQuotaDimensionRequest
        @return: GetProductQuotaDimensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_dimension_with_options(request, runtime)

    async def get_product_quota_dimension_async(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        """
        In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        *   The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   The name of the quota dimension is `region`.
        
        @param request: GetProductQuotaDimensionRequest
        @return: GetProductQuotaDimensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_product_quota_dimension_with_options_async(request, runtime)

    def get_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        """
        For more information about common request parameters, see [Common parameters](~~171299~~).
        
        @param request: GetQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        """
        For more information about common request parameters, see [Common parameters](~~171299~~).
        
        @param request: GetQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_alarm(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        """
        For more information about common request parameters, see [Common parameters](~~171299~~).
        
        @param request: GetQuotaAlarmRequest
        @return: GetQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_alarm_with_options(request, runtime)

    async def get_quota_alarm_async(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        """
        For more information about common request parameters, see [Common parameters](~~171299~~).
        
        @param request: GetQuotaAlarmRequest
        @return: GetQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_alarm_with_options_async(request, runtime)

    def get_quota_application_with_options(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        """
        In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
        @param request: GetQuotaApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_application_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        """
        In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
        @param request: GetQuotaApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_application(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        """
        In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
        @param request: GetQuotaApplicationRequest
        @return: GetQuotaApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_application_with_options(request, runtime)

    async def get_quota_application_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        """
        In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
        @param request: GetQuotaApplicationRequest
        @return: GetQuotaApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_application_with_options_async(request, runtime)

    def get_quota_template_service_status_with_options(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_directory_id):
            body['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_template_service_status_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_directory_id):
            body['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaTemplateServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_template_service_status(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quota_template_service_status_with_options(request, runtime)

    async def get_quota_template_service_status_async(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_template_service_status_with_options_async(request, runtime)

    def list_alarm_histories_with_options(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListAlarmHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_histories_with_options_async(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListAlarmHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_histories(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    async def list_alarm_histories_async(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_histories_with_options_async(request, runtime)

    def list_dependent_quotas_with_options(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        """
        In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        *   An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        *   An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
        @param request: ListDependentQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDependentQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDependentQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListDependentQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dependent_quotas_with_options_async(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        """
        In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        *   An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        *   An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
        @param request: ListDependentQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDependentQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDependentQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListDependentQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dependent_quotas(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        """
        In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        *   An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        *   An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
        @param request: ListDependentQuotasRequest
        @return: ListDependentQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dependent_quotas_with_options(request, runtime)

    async def list_dependent_quotas_async(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        """
        In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        *   An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        *   A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        *   An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
        @param request: ListDependentQuotasRequest
        @return: ListDependentQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dependent_quotas_with_options_async(request, runtime)

    def list_product_dimension_groups_with_options(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        """
        This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
        @param request: ListProductDimensionGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductDimensionGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDimensionGroups',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductDimensionGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_dimension_groups_with_options_async(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        """
        This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
        @param request: ListProductDimensionGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductDimensionGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDimensionGroups',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductDimensionGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_dimension_groups(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        """
        This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
        @param request: ListProductDimensionGroupsRequest
        @return: ListProductDimensionGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_dimension_groups_with_options(request, runtime)

    async def list_product_dimension_groups_async(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        """
        This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
        @param request: ListProductDimensionGroupsRequest
        @return: ListProductDimensionGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_dimension_groups_with_options_async(request, runtime)

    def list_product_quota_dimensions_with_options(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        """
        In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
        @param request: ListProductQuotaDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductQuotaDimensionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotaDimensions',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotaDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_quota_dimensions_with_options_async(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        """
        In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
        @param request: ListProductQuotaDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductQuotaDimensionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotaDimensions',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotaDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_quota_dimensions(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        """
        In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
        @param request: ListProductQuotaDimensionsRequest
        @return: ListProductQuotaDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_quota_dimensions_with_options(request, runtime)

    async def list_product_quota_dimensions_async(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        """
        In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
        @param request: ListProductQuotaDimensionsRequest
        @return: ListProductQuotaDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_quota_dimensions_with_options_async(request, runtime)

    def list_product_quotas_with_options(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        """
        In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
        @param request: ListProductQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.group_code):
            body['GroupCode'] = request.group_code
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_quotas_with_options_async(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        """
        In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
        @param request: ListProductQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.group_code):
            body['GroupCode'] = request.group_code
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_quotas(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        """
        In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
        @param request: ListProductQuotasRequest
        @return: ListProductQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_quotas_with_options(request, runtime)

    async def list_product_quotas_async(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        """
        In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
        @param request: ListProductQuotasRequest
        @return: ListProductQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_quotas_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: quotas_20200510_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: quotas_20200510_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: quotas_20200510_models.ListProductsRequest,
    ) -> quotas_20200510_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: quotas_20200510_models.ListProductsRequest,
    ) -> quotas_20200510_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_quota_alarms_with_options(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaAlarms',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_alarms_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaAlarms',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_alarms(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_alarms_with_options(request, runtime)

    async def list_quota_alarms_async(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_alarms_with_options_async(request, runtime)

    def list_quota_application_templates_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationTemplates',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_application_templates_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationTemplates',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_application_templates(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_application_templates_with_options(request, runtime)

    async def list_quota_application_templates_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_application_templates_with_options_async(request, runtime)

    def list_quota_applications_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        """
        In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
        @param request: ListQuotaApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplications',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        """
        In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
        @param request: ListQuotaApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplications',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        """
        In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
        @param request: ListQuotaApplicationsRequest
        @return: ListQuotaApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_with_options(request, runtime)

    async def list_quota_applications_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        """
        In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
        @param request: ListQuotaApplicationsRequest
        @return: ListQuotaApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_with_options_async(request, runtime)

    def list_quota_applications_detail_for_template_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsDetailForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationsDetailForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_detail_for_template_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsDetailForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationsDetailForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications_detail_for_template(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsDetailForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_detail_for_template_with_options(request, runtime)

    async def list_quota_applications_detail_for_template_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsDetailForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_detail_for_template_with_options_async(request, runtime)

    def list_quota_applications_for_template_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_end_time):
            body['ApplyEndTime'] = request.apply_end_time
        if not UtilClient.is_unset(request.apply_start_time):
            body['ApplyStartTime'] = request.apply_start_time
        if not UtilClient.is_unset(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationsForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsForTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_applications_for_template_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_end_time):
            body['ApplyEndTime'] = request.apply_end_time
        if not UtilClient.is_unset(request.apply_start_time):
            body['ApplyStartTime'] = request.apply_start_time
        if not UtilClient.is_unset(request.batch_quota_application_id):
            body['BatchQuotaApplicationId'] = request.batch_quota_application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationsForTemplate',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsForTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_applications_for_template(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_for_template_with_options(request, runtime)

    async def list_quota_applications_for_template_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_for_template_with_options_async(request, runtime)

    def modify_quota_template_service_status_with_options(
        self,
        request: quotas_20200510_models.ModifyQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse:
        """
        By default, the quota template is enabled.
        
        @param request: ModifyQuotaTemplateServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQuotaTemplateServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_quota_template_service_status_with_options_async(
        self,
        request: quotas_20200510_models.ModifyQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse:
        """
        By default, the quota template is enabled.
        
        @param request: ModifyQuotaTemplateServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQuotaTemplateServiceStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_quota_template_service_status(
        self,
        request: quotas_20200510_models.ModifyQuotaTemplateServiceStatusRequest,
    ) -> quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse:
        """
        By default, the quota template is enabled.
        
        @param request: ModifyQuotaTemplateServiceStatusRequest
        @return: ModifyQuotaTemplateServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_quota_template_service_status_with_options(request, runtime)

    async def modify_quota_template_service_status_async(
        self,
        request: quotas_20200510_models.ModifyQuotaTemplateServiceStatusRequest,
    ) -> quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse:
        """
        By default, the quota template is enabled.
        
        @param request: ModifyQuotaTemplateServiceStatusRequest
        @return: ModifyQuotaTemplateServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_quota_template_service_status_with_options_async(request, runtime)

    def modify_template_quota_item_with_options(
        self,
        request: quotas_20200510_models.ModifyTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ModifyTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_quota_item_with_options_async(
        self,
        request: quotas_20200510_models.ModifyTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ModifyTemplateQuotaItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_time):
            body['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyTemplateQuotaItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template_quota_item(
        self,
        request: quotas_20200510_models.ModifyTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.ModifyTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_template_quota_item_with_options(request, runtime)

    async def modify_template_quota_item_async(
        self,
        request: quotas_20200510_models.ModifyTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.ModifyTemplateQuotaItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_quota_item_with_options_async(request, runtime)

    def update_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        """
        In this example, the operation is called to modify the information about a quota alert whose ID is `a2efa7fc-832f-47bb-8054-39e28012***` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
        @param request: UpdateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.UpdateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        """
        In this example, the operation is called to modify the information about a quota alert whose ID is `a2efa7fc-832f-47bb-8054-39e28012***` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
        @param request: UpdateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.UpdateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_alarm(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        """
        In this example, the operation is called to modify the information about a quota alert whose ID is `a2efa7fc-832f-47bb-8054-39e28012***` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
        @param request: UpdateQuotaAlarmRequest
        @return: UpdateQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_quota_alarm_with_options(request, runtime)

    async def update_quota_alarm_async(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        """
        In this example, the operation is called to modify the information about a quota alert whose ID is `a2efa7fc-832f-47bb-8054-39e28012***` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
        @param request: UpdateQuotaAlarmRequest
        @return: UpdateQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_quota_alarm_with_options_async(request, runtime)
