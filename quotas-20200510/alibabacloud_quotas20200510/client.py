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
        @summary Creates a quota alert.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to create a quota alert of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: CreateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.original_context):
            body['OriginalContext'] = request.original_context
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
        @summary Creates a quota alert.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to create a quota alert of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: CreateQuotaAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.original_context):
            body['OriginalContext'] = request.original_context
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
        @summary Creates a quota alert.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to create a quota alert of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        
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
        @summary Creates a quota alert.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to create a quota alert of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        
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
        @summary Submits an application to increase a quota.
        
        @description In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
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
        @summary Submits an application to increase a quota.
        
        @description In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
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
        @summary Submits an application to increase a quota.
        
        @description In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
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
        @summary Submits an application to increase a quota.
        
        @description In this example, the operation is called to submit an application to increase the value of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. The quota belongs to Elastic Compute Service (ECS). The expected value of the quota is `804`, the application reason is `Scale Out`, and the ID of the region to which the quota belongs is `cn-hangzhou`.
        
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
        """
        @summary Submits a quota increase application. After you add a quota item to a quota template, the system automatically submits quota applications only for new members of the resource directory. The quota values for existing members remain unchanged. If you want to increase the quota values of existing members, you can submit a quota application for the members by applying quota templates to the members. Only the management account of a resource directory can create multiple quota applications at a time.
        
        @description ### [](#)QPS limit
        You can add a maximum of 10 quota items to a quota template at a time.
        
        @param request: CreateQuotaApplicationsForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaApplicationsForTemplateResponse
        """
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
        """
        @summary Submits a quota increase application. After you add a quota item to a quota template, the system automatically submits quota applications only for new members of the resource directory. The quota values for existing members remain unchanged. If you want to increase the quota values of existing members, you can submit a quota application for the members by applying quota templates to the members. Only the management account of a resource directory can create multiple quota applications at a time.
        
        @description ### [](#)QPS limit
        You can add a maximum of 10 quota items to a quota template at a time.
        
        @param request: CreateQuotaApplicationsForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaApplicationsForTemplateResponse
        """
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
        """
        @summary Submits a quota increase application. After you add a quota item to a quota template, the system automatically submits quota applications only for new members of the resource directory. The quota values for existing members remain unchanged. If you want to increase the quota values of existing members, you can submit a quota application for the members by applying quota templates to the members. Only the management account of a resource directory can create multiple quota applications at a time.
        
        @description ### [](#)QPS limit
        You can add a maximum of 10 quota items to a quota template at a time.
        
        @param request: CreateQuotaApplicationsForTemplateRequest
        @return: CreateQuotaApplicationsForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quota_applications_for_template_with_options(request, runtime)

    async def create_quota_applications_for_template_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationsForTemplateResponse:
        """
        @summary Submits a quota increase application. After you add a quota item to a quota template, the system automatically submits quota applications only for new members of the resource directory. The quota values for existing members remain unchanged. If you want to increase the quota values of existing members, you can submit a quota application for the members by applying quota templates to the members. Only the management account of a resource directory can create multiple quota applications at a time.
        
        @description ### [](#)QPS limit
        You can add a maximum of 10 quota items to a quota template at a time.
        
        @param request: CreateQuotaApplicationsForTemplateRequest
        @return: CreateQuotaApplicationsForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_applications_for_template_with_options_async(request, runtime)

    def create_template_quota_item_with_options(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        """
        @summary Creates a quota template by using the management account of a resource directory. After you create a quota template, if a member is added to the resource directory, the quota template automatically submits a quota increase request for the member. The quota values for existing members remain unchanged. You can use a quota template to apply for increases on multiple quotas at the same time. This automated approach improves the efficiency of quota management across your organization. Only the management account of a resource directory can create quota templates.
        
        @description ### [](#)Usage notes
        You must set the `ServiceStatus` parameter to `1`. This ensures that the quota template is enabled.
        You can call the [GetQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450407.html) operation to query the status of a quota template. If the value of the `ServiceStatus` parameter in the response is `0` or `-1`, you must call the [ModifyQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450406.html) operation to modify the value to `1`. A value of 0 indicates that the quota template is not configured. A value of -1 indicates that the quota template is disabled. A value of 1 indicates that the quota template is enabled.
        ### [](#)
        After you create a quota template, you can call the [ListQuotaApplicationsForTemplate](https://help.aliyun.com/document_detail/2584864.html) operation to view the approval result. If the value of the `Status` parameter in the response is `Agree`, the quota template is approved.
        
        @param request: CreateTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateQuotaItemResponse
        """
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
        """
        @summary Creates a quota template by using the management account of a resource directory. After you create a quota template, if a member is added to the resource directory, the quota template automatically submits a quota increase request for the member. The quota values for existing members remain unchanged. You can use a quota template to apply for increases on multiple quotas at the same time. This automated approach improves the efficiency of quota management across your organization. Only the management account of a resource directory can create quota templates.
        
        @description ### [](#)Usage notes
        You must set the `ServiceStatus` parameter to `1`. This ensures that the quota template is enabled.
        You can call the [GetQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450407.html) operation to query the status of a quota template. If the value of the `ServiceStatus` parameter in the response is `0` or `-1`, you must call the [ModifyQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450406.html) operation to modify the value to `1`. A value of 0 indicates that the quota template is not configured. A value of -1 indicates that the quota template is disabled. A value of 1 indicates that the quota template is enabled.
        ### [](#)
        After you create a quota template, you can call the [ListQuotaApplicationsForTemplate](https://help.aliyun.com/document_detail/2584864.html) operation to view the approval result. If the value of the `Status` parameter in the response is `Agree`, the quota template is approved.
        
        @param request: CreateTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateQuotaItemResponse
        """
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
        """
        @summary Creates a quota template by using the management account of a resource directory. After you create a quota template, if a member is added to the resource directory, the quota template automatically submits a quota increase request for the member. The quota values for existing members remain unchanged. You can use a quota template to apply for increases on multiple quotas at the same time. This automated approach improves the efficiency of quota management across your organization. Only the management account of a resource directory can create quota templates.
        
        @description ### [](#)Usage notes
        You must set the `ServiceStatus` parameter to `1`. This ensures that the quota template is enabled.
        You can call the [GetQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450407.html) operation to query the status of a quota template. If the value of the `ServiceStatus` parameter in the response is `0` or `-1`, you must call the [ModifyQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450406.html) operation to modify the value to `1`. A value of 0 indicates that the quota template is not configured. A value of -1 indicates that the quota template is disabled. A value of 1 indicates that the quota template is enabled.
        ### [](#)
        After you create a quota template, you can call the [ListQuotaApplicationsForTemplate](https://help.aliyun.com/document_detail/2584864.html) operation to view the approval result. If the value of the `Status` parameter in the response is `Agree`, the quota template is approved.
        
        @param request: CreateTemplateQuotaItemRequest
        @return: CreateTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_quota_item_with_options(request, runtime)

    async def create_template_quota_item_async(
        self,
        request: quotas_20200510_models.CreateTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.CreateTemplateQuotaItemResponse:
        """
        @summary Creates a quota template by using the management account of a resource directory. After you create a quota template, if a member is added to the resource directory, the quota template automatically submits a quota increase request for the member. The quota values for existing members remain unchanged. You can use a quota template to apply for increases on multiple quotas at the same time. This automated approach improves the efficiency of quota management across your organization. Only the management account of a resource directory can create quota templates.
        
        @description ### [](#)Usage notes
        You must set the `ServiceStatus` parameter to `1`. This ensures that the quota template is enabled.
        You can call the [GetQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450407.html) operation to query the status of a quota template. If the value of the `ServiceStatus` parameter in the response is `0` or `-1`, you must call the [ModifyQuotaTemplateServiceStatus](https://help.aliyun.com/document_detail/450406.html) operation to modify the value to `1`. A value of 0 indicates that the quota template is not configured. A value of -1 indicates that the quota template is disabled. A value of 1 indicates that the quota template is enabled.
        ### [](#)
        After you create a quota template, you can call the [ListQuotaApplicationsForTemplate](https://help.aliyun.com/document_detail/2584864.html) operation to view the approval result. If the value of the `Status` parameter in the response is `Agree`, the quota template is approved.
        
        @param request: CreateTemplateQuotaItemRequest
        @return: CreateTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_quota_item_with_options_async(request, runtime)

    def delete_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        """
        @summary Deletes a quota alert.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to delete a quota alert rule of the old version. If you want to delete a quota alert rule of the new version, call the CloudMonitor API operation [DeleteMetricRules](https://help.aliyun.com/document_detail/2513295.html) or [DeleteMetricRuleTargets](https://help.aliyun.com/document_detail/2513294.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to delete a quota alert rule whose ID is `6b512ab7-da3a-4142-b529-2b2a9294****`.
        
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
        @summary Deletes a quota alert.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to delete a quota alert rule of the old version. If you want to delete a quota alert rule of the new version, call the CloudMonitor API operation [DeleteMetricRules](https://help.aliyun.com/document_detail/2513295.html) or [DeleteMetricRuleTargets](https://help.aliyun.com/document_detail/2513294.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to delete a quota alert rule whose ID is `6b512ab7-da3a-4142-b529-2b2a9294****`.
        
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
        @summary Deletes a quota alert.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to delete a quota alert rule of the old version. If you want to delete a quota alert rule of the new version, call the CloudMonitor API operation [DeleteMetricRules](https://help.aliyun.com/document_detail/2513295.html) or [DeleteMetricRuleTargets](https://help.aliyun.com/document_detail/2513294.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to delete a quota alert rule whose ID is `6b512ab7-da3a-4142-b529-2b2a9294****`.
        
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
        @summary Deletes a quota alert.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to delete a quota alert rule of the old version. If you want to delete a quota alert rule of the new version, call the CloudMonitor API operation [DeleteMetricRules](https://help.aliyun.com/document_detail/2513295.html) or [DeleteMetricRuleTargets](https://help.aliyun.com/document_detail/2513294.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to delete a quota alert rule whose ID is `6b512ab7-da3a-4142-b529-2b2a9294****`.
        
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
        """
        @summary Deletes a quota template by using the management account of a resource directory. After you delete a quota template, if a member is added to the resource directory, the quota template no longer automatically submits a quota increase request for the member. Only the management account of a resource directory can delete quota templates.
        
        @param request: DeleteTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateQuotaItemResponse
        """
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
        """
        @summary Deletes a quota template by using the management account of a resource directory. After you delete a quota template, if a member is added to the resource directory, the quota template no longer automatically submits a quota increase request for the member. Only the management account of a resource directory can delete quota templates.
        
        @param request: DeleteTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateQuotaItemResponse
        """
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
        """
        @summary Deletes a quota template by using the management account of a resource directory. After you delete a quota template, if a member is added to the resource directory, the quota template no longer automatically submits a quota increase request for the member. Only the management account of a resource directory can delete quota templates.
        
        @param request: DeleteTemplateQuotaItemRequest
        @return: DeleteTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_quota_item_with_options(request, runtime)

    async def delete_template_quota_item_async(
        self,
        request: quotas_20200510_models.DeleteTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.DeleteTemplateQuotaItemResponse:
        """
        @summary Deletes a quota template by using the management account of a resource directory. After you delete a quota template, if a member is added to the resource directory, the quota template no longer automatically submits a quota increase request for the member. Only the management account of a resource directory can delete quota templates.
        
        @param request: DeleteTemplateQuotaItemRequest
        @return: DeleteTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_quota_item_with_options_async(request, runtime)

    def get_product_quota_with_options(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        """
        @summary Queries the details of a quota of a cloud service.
        
        @description In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
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
        @summary Queries the details of a quota of a cloud service.
        
        @description In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
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
        @summary Queries the details of a quota of a cloud service.
        
        @description In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
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
        @summary Queries the details of a quota of a cloud service.
        
        @description In this example, the operation is called to query the details of a quota whose ID is `q_security-groups` and whose name is Maximum Number of Security Groups. This quota belongs to Elastic Compute Service (ECS). The query result shows the details of the quota. The details include the name, ID, description, quota value, used quota, unit, and dimension of the quota. In this example, the quota name is `Maximum Number of Security Groups`. The quota ID is `q_security-groups`. The description is `The maximum number of security groups that can be created for the current account`. The quota value is `801`. The used quota is `26`. The quota unit is `Number of security groups`. The quota dimension is `{"regionId":"cn-hangzhou"}`.
        
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
        @summary Queries the details of a quota dimension that is supported by an Alibaba Cloud service.
        
        @description In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        The name of the quota dimension is `region`.
        
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
        @summary Queries the details of a quota dimension that is supported by an Alibaba Cloud service.
        
        @description In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        The name of the quota dimension is `region`.
        
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
        @summary Queries the details of a quota dimension that is supported by an Alibaba Cloud service.
        
        @description In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        The name of the quota dimension is `region`.
        
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
        @summary Queries the details of a quota dimension that is supported by an Alibaba Cloud service.
        
        @description In this example, the operation is called to query the details of a quota dimension whose key is `regionId`. The quota dimension belongs to Elastic Compute Service (ECS) Quotas by Instance Type whose service code is ecs-spec. The following query results are returned:
        The values of the quota dimension include `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        The name of the quota dimension is `region`.
        
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
        @summary In this example, the operation is called to query the details of a quota alert. The details of the alert are returned. The query results include the alert ID, alert name, alert contact, and time when the quota alert was created.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the details about the quota alert rules of the old version. If you want to query the details about the quota alert rules of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the operation is called to query the details of a quota alert rule whose ID is `78d7e436-4b25-4897-84b5-d7b656bb****`. The details of the alert rule are returned. The query result includes the alert ID, alert name, alert contact, and the time when the quota alert rule was created.
        
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
        @summary In this example, the operation is called to query the details of a quota alert. The details of the alert are returned. The query results include the alert ID, alert name, alert contact, and time when the quota alert was created.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the details about the quota alert rules of the old version. If you want to query the details about the quota alert rules of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the operation is called to query the details of a quota alert rule whose ID is `78d7e436-4b25-4897-84b5-d7b656bb****`. The details of the alert rule are returned. The query result includes the alert ID, alert name, alert contact, and the time when the quota alert rule was created.
        
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
        @summary In this example, the operation is called to query the details of a quota alert. The details of the alert are returned. The query results include the alert ID, alert name, alert contact, and time when the quota alert was created.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the details about the quota alert rules of the old version. If you want to query the details about the quota alert rules of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the operation is called to query the details of a quota alert rule whose ID is `78d7e436-4b25-4897-84b5-d7b656bb****`. The details of the alert rule are returned. The query result includes the alert ID, alert name, alert contact, and the time when the quota alert rule was created.
        
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
        @summary In this example, the operation is called to query the details of a quota alert. The details of the alert are returned. The query results include the alert ID, alert name, alert contact, and time when the quota alert was created.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the details about the quota alert rules of the old version. If you want to query the details about the quota alert rules of the new version, call CloudMonitor API operations. For more information, see [Use API operations to manage new quota alert rules](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the operation is called to query the details of a quota alert rule whose ID is `78d7e436-4b25-4897-84b5-d7b656bb****`. The details of the alert rule are returned. The query result includes the alert ID, alert name, alert contact, and the time when the quota alert rule was created.
        
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
        @summary Queries the details about a specified application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
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
        @summary Queries the details about a specified application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
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
        @summary Queries the details about a specified application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
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
        @summary Queries the details about a specified application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details about an application whose ID is `d314d6ae-867d-484c-9009-3d421a80***`. The query result shows the details about the application. The details include the application ID, application time, expected quota value, and application result.
        
        @param request: GetQuotaApplicationRequest
        @return: GetQuotaApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_application_with_options_async(request, runtime)

    def get_quota_application_approval_with_options(
        self,
        request: quotas_20200510_models.GetQuotaApplicationApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationApprovalResponse:
        """
        @summary Queries the information about quota application approval, such as the average amount of time required for approval, whether approval reminders are supported, and the interval between two consecutive approval reminders.
        
        @description ### [](#)Prerequisites
        Make sure that you have created an application for quota increase. For more information, see [CreateQuotaApplication](https://help.aliyun.com/document_detail/440566.html).
        
        @param request: GetQuotaApplicationApprovalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaApplicationApprovalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaApplicationApproval',
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
            quotas_20200510_models.GetQuotaApplicationApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_application_approval_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationApprovalResponse:
        """
        @summary Queries the information about quota application approval, such as the average amount of time required for approval, whether approval reminders are supported, and the interval between two consecutive approval reminders.
        
        @description ### [](#)Prerequisites
        Make sure that you have created an application for quota increase. For more information, see [CreateQuotaApplication](https://help.aliyun.com/document_detail/440566.html).
        
        @param request: GetQuotaApplicationApprovalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaApplicationApprovalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaApplicationApproval',
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
            quotas_20200510_models.GetQuotaApplicationApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_application_approval(
        self,
        request: quotas_20200510_models.GetQuotaApplicationApprovalRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationApprovalResponse:
        """
        @summary Queries the information about quota application approval, such as the average amount of time required for approval, whether approval reminders are supported, and the interval between two consecutive approval reminders.
        
        @description ### [](#)Prerequisites
        Make sure that you have created an application for quota increase. For more information, see [CreateQuotaApplication](https://help.aliyun.com/document_detail/440566.html).
        
        @param request: GetQuotaApplicationApprovalRequest
        @return: GetQuotaApplicationApprovalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_application_approval_with_options(request, runtime)

    async def get_quota_application_approval_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationApprovalRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationApprovalResponse:
        """
        @summary Queries the information about quota application approval, such as the average amount of time required for approval, whether approval reminders are supported, and the interval between two consecutive approval reminders.
        
        @description ### [](#)Prerequisites
        Make sure that you have created an application for quota increase. For more information, see [CreateQuotaApplication](https://help.aliyun.com/document_detail/440566.html).
        
        @param request: GetQuotaApplicationApprovalRequest
        @return: GetQuotaApplicationApprovalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_application_approval_with_options_async(request, runtime)

    def get_quota_template_service_status_with_options(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        """
        @summary Queries the status of a quota template.
        
        @description By default, the value of `ServiceStatus` is `0`, which indicates that no quota template is specified. If you want to use a quota template, make sure that the quota template is enabled. In this case, the value of `ServiceStatus` is `1`.
        
        @param request: GetQuotaTemplateServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaTemplateServiceStatusResponse
        """
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
        """
        @summary Queries the status of a quota template.
        
        @description By default, the value of `ServiceStatus` is `0`, which indicates that no quota template is specified. If you want to use a quota template, make sure that the quota template is enabled. In this case, the value of `ServiceStatus` is `1`.
        
        @param request: GetQuotaTemplateServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaTemplateServiceStatusResponse
        """
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
        """
        @summary Queries the status of a quota template.
        
        @description By default, the value of `ServiceStatus` is `0`, which indicates that no quota template is specified. If you want to use a quota template, make sure that the quota template is enabled. In this case, the value of `ServiceStatus` is `1`.
        
        @param request: GetQuotaTemplateServiceStatusRequest
        @return: GetQuotaTemplateServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_template_service_status_with_options(request, runtime)

    async def get_quota_template_service_status_async(
        self,
        request: quotas_20200510_models.GetQuotaTemplateServiceStatusRequest,
    ) -> quotas_20200510_models.GetQuotaTemplateServiceStatusResponse:
        """
        @summary Queries the status of a quota template.
        
        @description By default, the value of `ServiceStatus` is `0`, which indicates that no quota template is specified. If you want to use a quota template, make sure that the quota template is enabled. In this case, the value of `ServiceStatus` is `1`.
        
        @param request: GetQuotaTemplateServiceStatusRequest
        @return: GetQuotaTemplateServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_template_service_status_with_options_async(request, runtime)

    def list_alarm_histories_with_options(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        """
        @summary Queries the alert records.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the historical records of quota alert rules of the old version. If you want to query the historical records of quota alert rules of the new version, call the CloudMonitor API operation [DescribeAlertLogCount](https://help.aliyun.com/document_detail/2513275.html) or [DescribeAlertLogList](https://help.aliyun.com/document_detail/2513276.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListAlarmHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmHistoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
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
        """
        @summary Queries the alert records.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the historical records of quota alert rules of the old version. If you want to query the historical records of quota alert rules of the new version, call the CloudMonitor API operation [DescribeAlertLogCount](https://help.aliyun.com/document_detail/2513275.html) or [DescribeAlertLogList](https://help.aliyun.com/document_detail/2513276.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListAlarmHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmHistoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
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
        """
        @summary Queries the alert records.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the historical records of quota alert rules of the old version. If you want to query the historical records of quota alert rules of the new version, call the CloudMonitor API operation [DescribeAlertLogCount](https://help.aliyun.com/document_detail/2513275.html) or [DescribeAlertLogList](https://help.aliyun.com/document_detail/2513276.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListAlarmHistoriesRequest
        @return: ListAlarmHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    async def list_alarm_histories_async(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        """
        @summary Queries the alert records.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query the historical records of quota alert rules of the old version. If you want to query the historical records of quota alert rules of the new version, call the CloudMonitor API operation [DescribeAlertLogCount](https://help.aliyun.com/document_detail/2513275.html) or [DescribeAlertLogList](https://help.aliyun.com/document_detail/2513276.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListAlarmHistoriesRequest
        @return: ListAlarmHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_histories_with_options_async(request, runtime)

    def list_dependent_quotas_with_options(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        """
        @summary Queries the quotas on which a specified quota depends.
        
        @description In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
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
        @summary Queries the quotas on which a specified quota depends.
        
        @description In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
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
        @summary Queries the quotas on which a specified quota depends.
        
        @description In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
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
        @summary Queries the quotas on which a specified quota depends.
        
        @description In this example, the operation is called to query the quotas on which a Container Service for Kubernetes (ACK) quota whose ID is `q_i5uzm3` depends. This quota is the maximum number of nodes that can be created in an ACK cluster. The query result indicates that the specified quota depends on the following three quotas:
        An Elastic Compute Service (ECS) quota whose ID is `q_elastic-network-interfaces`. This quota is the maximum number of ENIs (Secondary ENIs) that can be owned by an Alibaba Cloud account. The quota is available in the following regions: `cn-shenzhen`, `cn-beijing`, and `cn-hangzhou`.
        A Server Load Balancer (SLB) quota whose ID is `q_fh20b0`. This quota is the number of servers that can be attached to the backend of an SLB instance.
        An SLB quota whose ID is `q_3mmbsp`. This quota is the number of SLB instances that can be owned by an Alibaba Cloud account.
        
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
        @summary Queries the dimension groups of an Alibaba Cloud service.
        
        @description This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
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
        @summary Queries the dimension groups of an Alibaba Cloud service.
        
        @description This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
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
        @summary Queries the dimension groups of an Alibaba Cloud service.
        
        @description This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
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
        @summary Queries the dimension groups of an Alibaba Cloud service.
        
        @description This topic provides an example on how to call the ListProductDimensionGroups operation to query the dimension groups of Object Storage Service (OSS). In this example, a dimension group is returned. The group name is `OSS_Group`, the group code is `oss_wf1ngqmd7q`, and the group key is `chargeType`.
        
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
        @summary Queries the quota dimensions that are supported by the specified Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
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
        @summary Queries the quota dimensions that are supported by the specified Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
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
        @summary Queries the quota dimensions that are supported by the specified Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
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
        @summary Queries the quota dimensions that are supported by the specified Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quota dimensions that are supported by Elastic Compute Service (ECS). The query results show all the quota dimensions that are supported by ECS.
        
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
        @summary Queries the quotas of a specific Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
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
        @summary Queries the quotas of a specific Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
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
        @summary Queries the quotas of a specific Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
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
        @summary Queries the quotas of a specific Alibaba Cloud service.
        
        @description In this example, the operation is called to query the quotas whose instance type is `ecs.g5.2xlarge`. The quotas belong to Elastic Compute Service (ECS) Quotas by Instance Type. The query result includes the name, ID, unit, dimensions, and cycle of each quota.
        
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
        """
        @summary Queries the Alibaba Cloud services that support Quota Center.
        
        @description The services in the query result are the same as the services listed in [Alibaba Cloud services that support Quota Center](https://help.aliyun.com/document_detail/182368.html).
        
        @param request: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
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
        """
        @summary Queries the Alibaba Cloud services that support Quota Center.
        
        @description The services in the query result are the same as the services listed in [Alibaba Cloud services that support Quota Center](https://help.aliyun.com/document_detail/182368.html).
        
        @param request: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
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
        """
        @summary Queries the Alibaba Cloud services that support Quota Center.
        
        @description The services in the query result are the same as the services listed in [Alibaba Cloud services that support Quota Center](https://help.aliyun.com/document_detail/182368.html).
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: quotas_20200510_models.ListProductsRequest,
    ) -> quotas_20200510_models.ListProductsResponse:
        """
        @summary Queries the Alibaba Cloud services that support Quota Center.
        
        @description The services in the query result are the same as the services listed in [Alibaba Cloud services that support Quota Center](https://help.aliyun.com/document_detail/182368.html).
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_quota_alarms_with_options(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        """
        @summary Queries quota alerts.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query quota alert rules of the old version. If you want to query quota alert rules of the new version, call the CloudMonitor API operation [DescribeMetricRuleList](https://help.aliyun.com/document_detail/2513291.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListQuotaAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaAlarmsResponse
        """
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
        """
        @summary Queries quota alerts.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query quota alert rules of the old version. If you want to query quota alert rules of the new version, call the CloudMonitor API operation [DescribeMetricRuleList](https://help.aliyun.com/document_detail/2513291.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListQuotaAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaAlarmsResponse
        """
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
        """
        @summary Queries quota alerts.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query quota alert rules of the old version. If you want to query quota alert rules of the new version, call the CloudMonitor API operation [DescribeMetricRuleList](https://help.aliyun.com/document_detail/2513291.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListQuotaAlarmsRequest
        @return: ListQuotaAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quota_alarms_with_options(request, runtime)

    async def list_quota_alarms_async(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        """
        @summary Queries quota alerts.
        
        @description The quota alerting feature has been upgraded and this API operation will be deprecated. You can call this operation only to query quota alert rules of the old version. If you want to query quota alert rules of the new version, call the CloudMonitor API operation [DescribeMetricRuleList](https://help.aliyun.com/document_detail/2513291.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        
        @param request: ListQuotaAlarmsRequest
        @return: ListQuotaAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_alarms_with_options_async(request, runtime)

    def list_quota_application_templates_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        """
        @summary Queries quota templates by using the management account of a resource directory.
        
        @param request: ListQuotaApplicationTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationTemplatesResponse
        """
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
        """
        @summary Queries quota templates by using the management account of a resource directory.
        
        @param request: ListQuotaApplicationTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationTemplatesResponse
        """
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
        """
        @summary Queries quota templates by using the management account of a resource directory.
        
        @param request: ListQuotaApplicationTemplatesRequest
        @return: ListQuotaApplicationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quota_application_templates_with_options(request, runtime)

    async def list_quota_application_templates_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationTemplatesRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationTemplatesResponse:
        """
        @summary Queries quota templates by using the management account of a resource directory.
        
        @param request: ListQuotaApplicationTemplatesRequest
        @return: ListQuotaApplicationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_application_templates_with_options_async(request, runtime)

    def list_quota_applications_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        """
        @summary Queries the details of an application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
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
        @summary Queries the details of an application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
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
        @summary Queries the details of an application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
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
        @summary Queries the details of an application that is submitted to increase a quota.
        
        @description In this example, the operation is called to query the details of an application that is submitted to increase a quota whose ID is `q_i5uzm3` and whose name is Maximum Number of Nodes. This quota belongs to Container Service for Kubernetes (ACK). The query result shows the details of the application. The details include the application ID, application time, requested quota, and application result. In this example, the application ID is `b926571d-cc09-4711-b547-58a615f0***`. The application time is `2021-01-15T09:13:53Z`. The expected quota value is `101`. The application result is `Agree`.
        
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
        """
        @summary Queries the details of a quota increase application for member accounts in a resource directory.
        
        @param request: ListQuotaApplicationsDetailForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsDetailForTemplateResponse
        """
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
        """
        @summary Queries the details of a quota increase application for member accounts in a resource directory.
        
        @param request: ListQuotaApplicationsDetailForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsDetailForTemplateResponse
        """
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
        """
        @summary Queries the details of a quota increase application for member accounts in a resource directory.
        
        @param request: ListQuotaApplicationsDetailForTemplateRequest
        @return: ListQuotaApplicationsDetailForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_detail_for_template_with_options(request, runtime)

    async def list_quota_applications_detail_for_template_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsDetailForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsDetailForTemplateResponse:
        """
        @summary Queries the details of a quota increase application for member accounts in a resource directory.
        
        @param request: ListQuotaApplicationsDetailForTemplateRequest
        @return: ListQuotaApplicationsDetailForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_detail_for_template_with_options_async(request, runtime)

    def list_quota_applications_for_template_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        """
        @summary Queries the application records of a quota template that is used to apply for quotas for member accounts.
        
        @param request: ListQuotaApplicationsForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsForTemplateResponse
        """
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
        """
        @summary Queries the application records of a quota template that is used to apply for quotas for member accounts.
        
        @param request: ListQuotaApplicationsForTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaApplicationsForTemplateResponse
        """
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
        """
        @summary Queries the application records of a quota template that is used to apply for quotas for member accounts.
        
        @param request: ListQuotaApplicationsForTemplateRequest
        @return: ListQuotaApplicationsForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_for_template_with_options(request, runtime)

    async def list_quota_applications_for_template_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsForTemplateRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsForTemplateResponse:
        """
        @summary Queries the application records of a quota template that is used to apply for quotas for member accounts.
        
        @param request: ListQuotaApplicationsForTemplateRequest
        @return: ListQuotaApplicationsForTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_for_template_with_options_async(request, runtime)

    def modify_quota_template_service_status_with_options(
        self,
        request: quotas_20200510_models.ModifyQuotaTemplateServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse:
        """
        @summary Changes the status of a quota template. By default, the quota template is not configured. If the management account of a resource directory uses a quota template for the first time, you must enable the quota template. Only the management account of a resource directory can change the status of quota templates.
        
        @description ### [](#)Prerequisites
        A resource directory is enabled. For more information, see [EnableResourceDirectory](https://help.aliyun.com/document_detail/604185.html).
        ### [](#)Usage notes
        If the `ServiceStatus` parameter is set to `0` or `-1`, you can call this operation to set the parameter to `1`. Then, you can call the [CreateTemplateQuotaItem](https://help.aliyun.com/document_detail/450615.html) operation to create a quota template.
        
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
        @summary Changes the status of a quota template. By default, the quota template is not configured. If the management account of a resource directory uses a quota template for the first time, you must enable the quota template. Only the management account of a resource directory can change the status of quota templates.
        
        @description ### [](#)Prerequisites
        A resource directory is enabled. For more information, see [EnableResourceDirectory](https://help.aliyun.com/document_detail/604185.html).
        ### [](#)Usage notes
        If the `ServiceStatus` parameter is set to `0` or `-1`, you can call this operation to set the parameter to `1`. Then, you can call the [CreateTemplateQuotaItem](https://help.aliyun.com/document_detail/450615.html) operation to create a quota template.
        
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
        @summary Changes the status of a quota template. By default, the quota template is not configured. If the management account of a resource directory uses a quota template for the first time, you must enable the quota template. Only the management account of a resource directory can change the status of quota templates.
        
        @description ### [](#)Prerequisites
        A resource directory is enabled. For more information, see [EnableResourceDirectory](https://help.aliyun.com/document_detail/604185.html).
        ### [](#)Usage notes
        If the `ServiceStatus` parameter is set to `0` or `-1`, you can call this operation to set the parameter to `1`. Then, you can call the [CreateTemplateQuotaItem](https://help.aliyun.com/document_detail/450615.html) operation to create a quota template.
        
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
        @summary Changes the status of a quota template. By default, the quota template is not configured. If the management account of a resource directory uses a quota template for the first time, you must enable the quota template. Only the management account of a resource directory can change the status of quota templates.
        
        @description ### [](#)Prerequisites
        A resource directory is enabled. For more information, see [EnableResourceDirectory](https://help.aliyun.com/document_detail/604185.html).
        ### [](#)Usage notes
        If the `ServiceStatus` parameter is set to `0` or `-1`, you can call this operation to set the parameter to `1`. Then, you can call the [CreateTemplateQuotaItem](https://help.aliyun.com/document_detail/450615.html) operation to create a quota template.
        
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
        """
        @summary The ID of the quota template.
        
        @param request: ModifyTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateQuotaItemResponse
        """
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
        """
        @summary The ID of the quota template.
        
        @param request: ModifyTemplateQuotaItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateQuotaItemResponse
        """
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
        """
        @summary The ID of the quota template.
        
        @param request: ModifyTemplateQuotaItemRequest
        @return: ModifyTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_template_quota_item_with_options(request, runtime)

    async def modify_template_quota_item_async(
        self,
        request: quotas_20200510_models.ModifyTemplateQuotaItemRequest,
    ) -> quotas_20200510_models.ModifyTemplateQuotaItemResponse:
        """
        @summary The ID of the quota template.
        
        @param request: ModifyTemplateQuotaItemRequest
        @return: ModifyTemplateQuotaItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_quota_item_with_options_async(request, runtime)

    def remind_quota_application_approval_with_options(
        self,
        request: quotas_20200510_models.RemindQuotaApplicationApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.RemindQuotaApplicationApprovalResponse:
        """
        @summary Reminds the approver of a quota application to review the application. This operation is applicable to quota applications that support the approval reminding feature.
        
        @description >  You can call this operation to enable the approval reminder feature for quota applications that support this feature. To check whether this feature is supported, you can view the value of `SupportReminder` in the GetQuotaApplicationApproval operation. If the value of SupportReminder is `true`, this feature is supported.
        
        @param request: RemindQuotaApplicationApprovalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemindQuotaApplicationApprovalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemindQuotaApplicationApproval',
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
            quotas_20200510_models.RemindQuotaApplicationApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def remind_quota_application_approval_with_options_async(
        self,
        request: quotas_20200510_models.RemindQuotaApplicationApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.RemindQuotaApplicationApprovalResponse:
        """
        @summary Reminds the approver of a quota application to review the application. This operation is applicable to quota applications that support the approval reminding feature.
        
        @description >  You can call this operation to enable the approval reminder feature for quota applications that support this feature. To check whether this feature is supported, you can view the value of `SupportReminder` in the GetQuotaApplicationApproval operation. If the value of SupportReminder is `true`, this feature is supported.
        
        @param request: RemindQuotaApplicationApprovalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemindQuotaApplicationApprovalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemindQuotaApplicationApproval',
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
            quotas_20200510_models.RemindQuotaApplicationApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remind_quota_application_approval(
        self,
        request: quotas_20200510_models.RemindQuotaApplicationApprovalRequest,
    ) -> quotas_20200510_models.RemindQuotaApplicationApprovalResponse:
        """
        @summary Reminds the approver of a quota application to review the application. This operation is applicable to quota applications that support the approval reminding feature.
        
        @description >  You can call this operation to enable the approval reminder feature for quota applications that support this feature. To check whether this feature is supported, you can view the value of `SupportReminder` in the GetQuotaApplicationApproval operation. If the value of SupportReminder is `true`, this feature is supported.
        
        @param request: RemindQuotaApplicationApprovalRequest
        @return: RemindQuotaApplicationApprovalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remind_quota_application_approval_with_options(request, runtime)

    async def remind_quota_application_approval_async(
        self,
        request: quotas_20200510_models.RemindQuotaApplicationApprovalRequest,
    ) -> quotas_20200510_models.RemindQuotaApplicationApprovalResponse:
        """
        @summary Reminds the approver of a quota application to review the application. This operation is applicable to quota applications that support the approval reminding feature.
        
        @description >  You can call this operation to enable the approval reminder feature for quota applications that support this feature. To check whether this feature is supported, you can view the value of `SupportReminder` in the GetQuotaApplicationApproval operation. If the value of SupportReminder is `true`, this feature is supported.
        
        @param request: RemindQuotaApplicationApprovalRequest
        @return: RemindQuotaApplicationApprovalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remind_quota_application_approval_with_options_async(request, runtime)

    def update_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        """
        @summary Modifies a quota alert rule.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to modify the information about a specific quota alert rule of the new version, call the CloudMonitor API operation [PutResourceMetricRules](https://help.aliyun.com/document_detail/2513316.html) or [PutMetricRuleTargets](https://help.aliyun.com/document_detail/2513302.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to modify the information about a quota alert rule whose ID is `a2efa7fc-832f-47bb-8054-39e28012****` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
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
        @summary Modifies a quota alert rule.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to modify the information about a specific quota alert rule of the new version, call the CloudMonitor API operation [PutResourceMetricRules](https://help.aliyun.com/document_detail/2513316.html) or [PutMetricRuleTargets](https://help.aliyun.com/document_detail/2513302.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to modify the information about a quota alert rule whose ID is `a2efa7fc-832f-47bb-8054-39e28012****` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
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
        @summary Modifies a quota alert rule.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to modify the information about a specific quota alert rule of the new version, call the CloudMonitor API operation [PutResourceMetricRules](https://help.aliyun.com/document_detail/2513316.html) or [PutMetricRuleTargets](https://help.aliyun.com/document_detail/2513302.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to modify the information about a quota alert rule whose ID is `a2efa7fc-832f-47bb-8054-39e28012****` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
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
        @summary Modifies a quota alert rule.
        
        @description    The quota alerting feature has been upgraded and this API operation will be deprecated. If you want to modify the information about a specific quota alert rule of the new version, call the CloudMonitor API operation [PutResourceMetricRules](https://help.aliyun.com/document_detail/2513316.html) or [PutMetricRuleTargets](https://help.aliyun.com/document_detail/2513302.html). For more information about how to call API operations to manage quota alert rules of the new version, see [Manage quota alerts of the new version by calling API operations](https://help.aliyun.com/document_detail/2863234.html).
        In this example, the API operation is called to modify the information about a quota alert rule whose ID is `a2efa7fc-832f-47bb-8054-39e28012****` and whose name is `rules`. The alert threshold is changed from `150` to `160`.
        
        @param request: UpdateQuotaAlarmRequest
        @return: UpdateQuotaAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_quota_alarm_with_options_async(request, runtime)
