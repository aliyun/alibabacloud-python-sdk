# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms20190101 import models as cms_20190101_models
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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_tags_with_options(
        self,
        request: cms_20190101_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.AddTagsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: AddTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: cms_20190101_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.AddTagsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: AddTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.AddTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags(
        self,
        request: cms_20190101_models.AddTagsRequest,
    ) -> cms_20190101_models.AddTagsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: AddTagsRequest
        @return: AddTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: cms_20190101_models.AddTagsRequest,
    ) -> cms_20190101_models.AddTagsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: AddTagsRequest
        @return: AddTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def apply_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: ApplyMetricRuleTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_mode):
            query['ApplyMode'] = request.apply_mode
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.notify_level):
            query['NotifyLevel'] = request.notify_level
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ApplyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: ApplyMetricRuleTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_mode):
            query['ApplyMode'] = request.apply_mode
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.notify_level):
            query['NotifyLevel'] = request.notify_level
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ApplyMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_metric_rule_template(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: ApplyMetricRuleTemplateRequest
        @return: ApplyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_metric_rule_template_with_options(request, runtime)

    async def apply_metric_rule_template_async(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: ApplyMetricRuleTemplateRequest
        @return: ApplyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_metric_rule_template_with_options_async(request, runtime)

    def batch_create_instant_site_monitor_with_options(
        self,
        request: cms_20190101_models.BatchCreateInstantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchCreateInstantSiteMonitorResponse:
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        
        @param request: BatchCreateInstantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_instant_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.BatchCreateInstantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchCreateInstantSiteMonitorResponse:
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        
        @param request: BatchCreateInstantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateInstantSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_instant_site_monitor(
        self,
        request: cms_20190101_models.BatchCreateInstantSiteMonitorRequest,
    ) -> cms_20190101_models.BatchCreateInstantSiteMonitorResponse:
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        
        @param request: BatchCreateInstantSiteMonitorRequest
        @return: BatchCreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_instant_site_monitor_with_options(request, runtime)

    async def batch_create_instant_site_monitor_async(
        self,
        request: cms_20190101_models.BatchCreateInstantSiteMonitorRequest,
    ) -> cms_20190101_models.BatchCreateInstantSiteMonitorResponse:
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        
        @param request: BatchCreateInstantSiteMonitorRequest
        @return: BatchCreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_instant_site_monitor_with_options_async(request, runtime)

    def batch_create_intant_site_monitor_with_options(
        self,
        request: cms_20190101_models.BatchCreateIntantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchCreateIntantSiteMonitorResponse:
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        
        @param request: BatchCreateIntantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateIntantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateIntantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_intant_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.BatchCreateIntantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchCreateIntantSiteMonitorResponse:
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        
        @param request: BatchCreateIntantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateIntantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateIntantSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_intant_site_monitor(
        self,
        request: cms_20190101_models.BatchCreateIntantSiteMonitorRequest,
    ) -> cms_20190101_models.BatchCreateIntantSiteMonitorResponse:
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        
        @param request: BatchCreateIntantSiteMonitorRequest
        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_intant_site_monitor_with_options(request, runtime)

    async def batch_create_intant_site_monitor_async(
        self,
        request: cms_20190101_models.BatchCreateIntantSiteMonitorRequest,
    ) -> cms_20190101_models.BatchCreateIntantSiteMonitorResponse:
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        
        @param request: BatchCreateIntantSiteMonitorRequest
        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_intant_site_monitor_with_options_async(request, runtime)

    def batch_export_with_options(
        self,
        tmp_req: cms_20190101_models.BatchExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchExportResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.BatchExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.measurements):
            request.measurements_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.measurements, 'Measurements', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.measurements_shrink):
            body['Measurements'] = request.measurements_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchExport',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_export_with_options_async(
        self,
        tmp_req: cms_20190101_models.BatchExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.BatchExportResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.BatchExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.measurements):
            request.measurements_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.measurements, 'Measurements', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.measurements_shrink):
            body['Measurements'] = request.measurements_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchExport',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_export(
        self,
        request: cms_20190101_models.BatchExportRequest,
    ) -> cms_20190101_models.BatchExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_export_with_options(request, runtime)

    async def batch_export_async(
        self,
        request: cms_20190101_models.BatchExportRequest,
    ) -> cms_20190101_models.BatchExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_export_with_options_async(request, runtime)

    def create_cms_call_num_order_with_options(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsCallNumOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsCallNumOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cms_call_num_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsCallNumOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsCallNumOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cms_call_num_order(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cms_call_num_order_with_options(request, runtime)

    async def create_cms_call_num_order_async(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cms_call_num_order_with_options_async(request, runtime)

    def create_cms_order_with_options(
        self,
        request: cms_20190101_models.CreateCmsOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_count):
            query['ApiCount'] = request.api_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.custom_time_series):
            query['CustomTimeSeries'] = request.custom_time_series
        if not UtilClient.is_unset(request.event_store_num):
            query['EventStoreNum'] = request.event_store_num
        if not UtilClient.is_unset(request.event_store_time):
            query['EventStoreTime'] = request.event_store_time
        if not UtilClient.is_unset(request.log_monitor_stream):
            query['LogMonitorStream'] = request.log_monitor_stream
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not UtilClient.is_unset(request.site_ecs_num):
            query['SiteEcsNum'] = request.site_ecs_num
        if not UtilClient.is_unset(request.site_operator_num):
            query['SiteOperatorNum'] = request.site_operator_num
        if not UtilClient.is_unset(request.site_task_num):
            query['SiteTaskNum'] = request.site_task_num
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        if not UtilClient.is_unset(request.suggest_type):
            query['SuggestType'] = request.suggest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cms_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_count):
            query['ApiCount'] = request.api_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.custom_time_series):
            query['CustomTimeSeries'] = request.custom_time_series
        if not UtilClient.is_unset(request.event_store_num):
            query['EventStoreNum'] = request.event_store_num
        if not UtilClient.is_unset(request.event_store_time):
            query['EventStoreTime'] = request.event_store_time
        if not UtilClient.is_unset(request.log_monitor_stream):
            query['LogMonitorStream'] = request.log_monitor_stream
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not UtilClient.is_unset(request.site_ecs_num):
            query['SiteEcsNum'] = request.site_ecs_num
        if not UtilClient.is_unset(request.site_operator_num):
            query['SiteOperatorNum'] = request.site_operator_num
        if not UtilClient.is_unset(request.site_task_num):
            query['SiteTaskNum'] = request.site_task_num
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        if not UtilClient.is_unset(request.suggest_type):
            query['SuggestType'] = request.suggest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cms_order(
        self,
        request: cms_20190101_models.CreateCmsOrderRequest,
    ) -> cms_20190101_models.CreateCmsOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cms_order_with_options(request, runtime)

    async def create_cms_order_async(
        self,
        request: cms_20190101_models.CreateCmsOrderRequest,
    ) -> cms_20190101_models.CreateCmsOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cms_order_with_options_async(request, runtime)

    def create_cms_smspackage_order_with_options(
        self,
        request: cms_20190101_models.CreateCmsSmspackageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsSmspackageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsSmspackageOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsSmspackageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cms_smspackage_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsSmspackageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsSmspackageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsSmspackageOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsSmspackageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cms_smspackage_order(
        self,
        request: cms_20190101_models.CreateCmsSmspackageOrderRequest,
    ) -> cms_20190101_models.CreateCmsSmspackageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cms_smspackage_order_with_options(request, runtime)

    async def create_cms_smspackage_order_async(
        self,
        request: cms_20190101_models.CreateCmsSmspackageOrderRequest,
    ) -> cms_20190101_models.CreateCmsSmspackageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cms_smspackage_order_with_options_async(request, runtime)

    def create_dynamic_tag_group_with_options(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        
        @param request: CreateDynamicTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDynamicTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.template_id_list):
            query['TemplateIdList'] = request.template_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dynamic_tag_group_with_options_async(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        
        @param request: CreateDynamicTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDynamicTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.template_id_list):
            query['TemplateIdList'] = request.template_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateDynamicTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dynamic_tag_group(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        
        @param request: CreateDynamicTagGroupRequest
        @return: CreateDynamicTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_tag_group_with_options(request, runtime)

    async def create_dynamic_tag_group_async(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        
        @param request: CreateDynamicTagGroupRequest
        @return: CreateDynamicTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dynamic_tag_group_with_options_async(request, runtime)

    def create_group_metric_rules_with_options(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        """
        The details of the alert rules.
        
        @param request: CreateGroupMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_metric_rules):
            query['GroupMetricRules'] = request.group_metric_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        """
        The details of the alert rules.
        
        @param request: CreateGroupMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_metric_rules):
            query['GroupMetricRules'] = request.group_metric_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_metric_rules(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        """
        The details of the alert rules.
        
        @param request: CreateGroupMetricRulesRequest
        @return: CreateGroupMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_metric_rules_with_options(request, runtime)

    async def create_group_metric_rules_async(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        """
        The details of the alert rules.
        
        @param request: CreateGroupMetricRulesRequest
        @return: CreateGroupMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_metric_rules_with_options_async(request, runtime)

    def create_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_monitoring_agent_process(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_monitoring_agent_process_with_options(request, runtime)

    async def create_group_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_monitoring_agent_process_with_options_async(request, runtime)

    def create_host_availability_with_options(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        """
        The ID of the resource for which alerts are triggered.
        
        @param request: CreateHostAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_availability_with_options_async(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        """
        The ID of the resource for which alerts are triggered.
        
        @param request: CreateHostAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_availability(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        """
        The ID of the resource for which alerts are triggered.
        
        @param request: CreateHostAvailabilityRequest
        @return: CreateHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_availability_with_options(request, runtime)

    async def create_host_availability_async(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        """
        The ID of the resource for which alerts are triggered.
        
        @param request: CreateHostAvailabilityRequest
        @return: CreateHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_host_availability_with_options_async(request, runtime)

    def create_hybrid_monitor_namespace_with_options(
        self,
        request: cms_20190101_models.CreateHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_namespace_with_options_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_namespace(
        self,
        request: cms_20190101_models.CreateHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.CreateHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateHybridMonitorNamespaceRequest
        @return: CreateHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_namespace_with_options(request, runtime)

    async def create_hybrid_monitor_namespace_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.CreateHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateHybridMonitorNamespaceRequest
        @return: CreateHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_monitor_namespace_with_options_async(request, runtime)

    def create_hybrid_monitor_slsgroup_with_options(
        self,
        request: cms_20190101_models.CreateHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: CreateHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: CreateHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_slsgroup(
        self,
        request: cms_20190101_models.CreateHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.CreateHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: CreateHybridMonitorSLSGroupRequest
        @return: CreateHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def create_hybrid_monitor_slsgroup_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.CreateHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: CreateHybridMonitorSLSGroupRequest
        @return: CreateHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def create_hybrid_monitor_task_with_options(
        self,
        request: cms_20190101_models.CreateHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorTaskResponse:
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        
        @param request: CreateHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.collect_target_type):
            query['CollectTargetType'] = request.collect_target_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.target_user_id_list):
            query['TargetUserIdList'] = request.target_user_id_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.yarmconfig):
            query['YARMConfig'] = request.yarmconfig
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_task_with_options_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHybridMonitorTaskResponse:
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        
        @param request: CreateHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.collect_target_type):
            query['CollectTargetType'] = request.collect_target_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.target_user_id_list):
            query['TargetUserIdList'] = request.target_user_id_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.yarmconfig):
            query['YARMConfig'] = request.yarmconfig
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_task(
        self,
        request: cms_20190101_models.CreateHybridMonitorTaskRequest,
    ) -> cms_20190101_models.CreateHybridMonitorTaskResponse:
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        
        @param request: CreateHybridMonitorTaskRequest
        @return: CreateHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_task_with_options(request, runtime)

    async def create_hybrid_monitor_task_async(
        self,
        request: cms_20190101_models.CreateHybridMonitorTaskRequest,
    ) -> cms_20190101_models.CreateHybridMonitorTaskResponse:
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        
        @param request: CreateHybridMonitorTaskRequest
        @return: CreateHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_monitor_task_with_options_async(request, runtime)

    def create_instant_site_monitor_with_options(
        self,
        request: cms_20190101_models.CreateInstantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateInstantSiteMonitorResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        
        @param request: CreateInstantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.random_isp_city):
            query['RandomIspCity'] = request.random_isp_city
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instant_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.CreateInstantSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateInstantSiteMonitorResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        
        @param request: CreateInstantSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.random_isp_city):
            query['RandomIspCity'] = request.random_isp_city
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateInstantSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instant_site_monitor(
        self,
        request: cms_20190101_models.CreateInstantSiteMonitorRequest,
    ) -> cms_20190101_models.CreateInstantSiteMonitorResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        
        @param request: CreateInstantSiteMonitorRequest
        @return: CreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instant_site_monitor_with_options(request, runtime)

    async def create_instant_site_monitor_async(
        self,
        request: cms_20190101_models.CreateInstantSiteMonitorRequest,
    ) -> cms_20190101_models.CreateInstantSiteMonitorResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        
        @param request: CreateInstantSiteMonitorRequest
        @return: CreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instant_site_monitor_with_options_async(request, runtime)

    def create_metric_rule_black_list_with_options(
        self,
        request: cms_20190101_models.CreateMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleBlackListResponse:
        """
        The name of the metric.
        Valid values of N: 1 to 10
        
        @param request: CreateMetricRuleBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricRuleBlackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_black_list_with_options_async(
        self,
        request: cms_20190101_models.CreateMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleBlackListResponse:
        """
        The name of the metric.
        Valid values of N: 1 to 10
        
        @param request: CreateMetricRuleBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricRuleBlackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_black_list(
        self,
        request: cms_20190101_models.CreateMetricRuleBlackListRequest,
    ) -> cms_20190101_models.CreateMetricRuleBlackListResponse:
        """
        The name of the metric.
        Valid values of N: 1 to 10
        
        @param request: CreateMetricRuleBlackListRequest
        @return: CreateMetricRuleBlackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_black_list_with_options(request, runtime)

    async def create_metric_rule_black_list_async(
        self,
        request: cms_20190101_models.CreateMetricRuleBlackListRequest,
    ) -> cms_20190101_models.CreateMetricRuleBlackListResponse:
        """
        The name of the metric.
        Valid values of N: 1 to 10
        
        @param request: CreateMetricRuleBlackListRequest
        @return: CreateMetricRuleBlackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_metric_rule_black_list_with_options_async(request, runtime)

    def create_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_resources(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_resources_with_options(request, runtime)

    async def create_metric_rule_resources_async(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_metric_rule_resources_with_options_async(request, runtime)

    def create_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.CreateMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.CreateMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_template(
        self,
        request: cms_20190101_models.CreateMetricRuleTemplateRequest,
    ) -> cms_20190101_models.CreateMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_template_with_options(request, runtime)

    async def create_metric_rule_template_async(
        self,
        request: cms_20190101_models.CreateMetricRuleTemplateRequest,
    ) -> cms_20190101_models.CreateMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_metric_rule_template_with_options_async(request, runtime)

    def create_monitor_agent_process_with_options(
        self,
        request: cms_20190101_models.CreateMonitorAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_agent_process(
        self,
        request: cms_20190101_models.CreateMonitorAgentProcessRequest,
    ) -> cms_20190101_models.CreateMonitorAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_agent_process_with_options(request, runtime)

    async def create_monitor_agent_process_async(
        self,
        request: cms_20190101_models.CreateMonitorAgentProcessRequest,
    ) -> cms_20190101_models.CreateMonitorAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_agent_process_with_options_async(request, runtime)

    def create_monitor_group_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        """
        The name of the application group.
        
        @param request: CreateMonitorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        """
        The name of the application group.
        
        @param request: CreateMonitorGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        """
        The name of the application group.
        
        @param request: CreateMonitorGroupRequest
        @return: CreateMonitorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    async def create_monitor_group_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        """
        The name of the application group.
        
        @param request: CreateMonitorGroupRequest
        @return: CreateMonitorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_with_options_async(request, runtime)

    def create_monitor_group_by_resource_group_id_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        
        @param request: CreateMonitorGroupByResourceGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupByResourceGroupId',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_by_resource_group_id_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        
        @param request: CreateMonitorGroupByResourceGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupByResourceGroupId',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_by_resource_group_id(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        
        @param request: CreateMonitorGroupByResourceGroupIdRequest
        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_by_resource_group_id_with_options(request, runtime)

    async def create_monitor_group_by_resource_group_id_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        
        @param request: CreateMonitorGroupByResourceGroupIdRequest
        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_by_resource_group_id_with_options_async(request, runtime)

    def create_monitor_group_instances_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        
        @param request: CreateMonitorGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        
        @param request: CreateMonitorGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_instances(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        
        @param request: CreateMonitorGroupInstancesRequest
        @return: CreateMonitorGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_instances_with_options(request, runtime)

    async def create_monitor_group_instances_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        
        @param request: CreateMonitorGroupInstancesRequest
        @return: CreateMonitorGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_instances_with_options_async(request, runtime)

    def create_monitor_group_notify_policy_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        """
        The type of the policy. Valid value: PauseNotify.
        
        @param request: CreateMonitorGroupNotifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_notify_policy_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        """
        The type of the policy. Valid value: PauseNotify.
        
        @param request: CreateMonitorGroupNotifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_notify_policy(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        """
        The type of the policy. Valid value: PauseNotify.
        
        @param request: CreateMonitorGroupNotifyPolicyRequest
        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_notify_policy_with_options(request, runtime)

    async def create_monitor_group_notify_policy_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        """
        The type of the policy. Valid value: PauseNotify.
        
        @param request: CreateMonitorGroupNotifyPolicyRequest
        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_notify_policy_with_options_async(request, runtime)

    def create_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitoring_agent_process(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitoring_agent_process_with_options(request, runtime)

    async def create_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitoring_agent_process_with_options_async(request, runtime)

    def create_site_monitor_with_options(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateSiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_site_monitor(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateSiteMonitorRequest
        @return: CreateSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_site_monitor_with_options(request, runtime)

    async def create_site_monitor_async(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: CreateSiteMonitorRequest
        @return: CreateSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_site_monitor_with_options_async(request, runtime)

    def cursor_with_options(
        self,
        tmp_req: cms_20190101_models.CursorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CursorResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.CursorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.matchers):
            request.matchers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cursor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CursorResponse(),
            self.call_api(params, req, runtime)
        )

    async def cursor_with_options_async(
        self,
        tmp_req: cms_20190101_models.CursorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CursorResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.CursorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.matchers):
            request.matchers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cursor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CursorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cursor(
        self,
        request: cms_20190101_models.CursorRequest,
    ) -> cms_20190101_models.CursorResponse:
        runtime = util_models.RuntimeOptions()
        return self.cursor_with_options(request, runtime)

    async def cursor_async(
        self,
        request: cms_20190101_models.CursorRequest,
    ) -> cms_20190101_models.CursorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cursor_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: cms_20190101_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: cms_20190101_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact(
        self,
        request: cms_20190101_models.DeleteContactRequest,
    ) -> cms_20190101_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    async def delete_contact_async(
        self,
        request: cms_20190101_models.DeleteContactRequest,
    ) -> cms_20190101_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_with_options_async(request, runtime)

    def delete_contact_group_with_options(
        self,
        request: cms_20190101_models.DeleteContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_group(
        self,
        request: cms_20190101_models.DeleteContactGroupRequest,
    ) -> cms_20190101_models.DeleteContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    async def delete_contact_group_async(
        self,
        request: cms_20190101_models.DeleteContactGroupRequest,
    ) -> cms_20190101_models.DeleteContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_group_with_options_async(request, runtime)

    def delete_custom_metric_with_options(
        self,
        request: cms_20190101_models.DeleteCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteCustomMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_metric_with_options_async(
        self,
        request: cms_20190101_models.DeleteCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteCustomMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_metric(
        self,
        request: cms_20190101_models.DeleteCustomMetricRequest,
    ) -> cms_20190101_models.DeleteCustomMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_metric_with_options(request, runtime)

    async def delete_custom_metric_async(
        self,
        request: cms_20190101_models.DeleteCustomMetricRequest,
    ) -> cms_20190101_models.DeleteCustomMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_metric_with_options_async(request, runtime)

    def delete_dynamic_tag_group_with_options(
        self,
        request: cms_20190101_models.DeleteDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteDynamicTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_tag_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteDynamicTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteDynamicTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_tag_group(
        self,
        request: cms_20190101_models.DeleteDynamicTagGroupRequest,
    ) -> cms_20190101_models.DeleteDynamicTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_tag_group_with_options(request, runtime)

    async def delete_dynamic_tag_group_async(
        self,
        request: cms_20190101_models.DeleteDynamicTagGroupRequest,
    ) -> cms_20190101_models.DeleteDynamicTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dynamic_tag_group_with_options_async(request, runtime)

    def delete_event_rule_targets_with_options(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_rule_targets(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_rule_targets_with_options(request, runtime)

    async def delete_event_rule_targets_async(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_rule_targets_with_options_async(request, runtime)

    def delete_event_rules_with_options(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_rules_with_options_async(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_rules(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_rules_with_options(request, runtime)

    async def delete_event_rules_async(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_rules_with_options_async(request, runtime)

    def delete_exporter_output_with_options(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exporter_output_with_options_async(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exporter_output(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_exporter_output_with_options(request, runtime)

    async def delete_exporter_output_async(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_exporter_output_with_options_async(request, runtime)

    def delete_exporter_rule_with_options(
        self,
        request: cms_20190101_models.DeleteExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exporter_rule_with_options_async(
        self,
        request: cms_20190101_models.DeleteExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exporter_rule(
        self,
        request: cms_20190101_models.DeleteExporterRuleRequest,
    ) -> cms_20190101_models.DeleteExporterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_exporter_rule_with_options(request, runtime)

    async def delete_exporter_rule_async(
        self,
        request: cms_20190101_models.DeleteExporterRuleRequest,
    ) -> cms_20190101_models.DeleteExporterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_exporter_rule_with_options_async(request, runtime)

    def delete_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.DeleteGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DeleteGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_monitoring_agent_process(
        self,
        request: cms_20190101_models.DeleteGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_monitoring_agent_process_with_options(request, runtime)

    async def delete_group_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.DeleteGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_monitoring_agent_process_with_options_async(request, runtime)

    def delete_host_availability_with_options(
        self,
        request: cms_20190101_models.DeleteHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DeleteHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_availability(
        self,
        request: cms_20190101_models.DeleteHostAvailabilityRequest,
    ) -> cms_20190101_models.DeleteHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_availability_with_options(request, runtime)

    async def delete_host_availability_async(
        self,
        request: cms_20190101_models.DeleteHostAvailabilityRequest,
    ) -> cms_20190101_models.DeleteHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_availability_with_options_async(request, runtime)

    def delete_hybrid_monitor_namespace_with_options(
        self,
        request: cms_20190101_models.DeleteHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_namespace_with_options_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_namespace(
        self,
        request: cms_20190101_models.DeleteHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorNamespaceRequest
        @return: DeleteHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_namespace_with_options(request, runtime)

    async def delete_hybrid_monitor_namespace_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorNamespaceRequest
        @return: DeleteHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hybrid_monitor_namespace_with_options_async(request, runtime)

    def delete_hybrid_monitor_slsgroup_with_options(
        self,
        request: cms_20190101_models.DeleteHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DeleteHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DeleteHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_slsgroup(
        self,
        request: cms_20190101_models.DeleteHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DeleteHybridMonitorSLSGroupRequest
        @return: DeleteHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def delete_hybrid_monitor_slsgroup_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DeleteHybridMonitorSLSGroupRequest
        @return: DeleteHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def delete_hybrid_monitor_task_with_options(
        self,
        request: cms_20190101_models.DeleteHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorTaskResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_task_with_options_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHybridMonitorTaskResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_task(
        self,
        request: cms_20190101_models.DeleteHybridMonitorTaskRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorTaskResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorTaskRequest
        @return: DeleteHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_task_with_options(request, runtime)

    async def delete_hybrid_monitor_task_async(
        self,
        request: cms_20190101_models.DeleteHybridMonitorTaskRequest,
    ) -> cms_20190101_models.DeleteHybridMonitorTaskResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DeleteHybridMonitorTaskRequest
        @return: DeleteHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hybrid_monitor_task_with_options_async(request, runtime)

    def delete_log_monitor_with_options(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_monitor_with_options_async(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteLogMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_monitor(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_log_monitor_with_options(request, runtime)

    async def delete_log_monitor_async(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_log_monitor_with_options_async(request, runtime)

    def delete_metric_rule_black_list_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_black_list_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_black_list(
        self,
        request: cms_20190101_models.DeleteMetricRuleBlackListRequest,
    ) -> cms_20190101_models.DeleteMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_black_list_with_options(request, runtime)

    async def delete_metric_rule_black_list_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleBlackListRequest,
    ) -> cms_20190101_models.DeleteMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rule_black_list_with_options_async(request, runtime)

    def delete_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_resources(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_resources_with_options(request, runtime)

    async def delete_metric_rule_resources_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rule_resources_with_options_async(request, runtime)

    def delete_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_targets(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_targets_with_options(request, runtime)

    async def delete_metric_rule_targets_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rule_targets_with_options_async(request, runtime)

    def delete_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_template(
        self,
        request: cms_20190101_models.DeleteMetricRuleTemplateRequest,
    ) -> cms_20190101_models.DeleteMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_template_with_options(request, runtime)

    async def delete_metric_rule_template_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTemplateRequest,
    ) -> cms_20190101_models.DeleteMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rule_template_with_options_async(request, runtime)

    def delete_metric_rules_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rules(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rules_with_options(request, runtime)

    async def delete_metric_rules_async(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rules_with_options_async(request, runtime)

    def delete_monitor_group_with_options(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_with_options(request, runtime)

    async def delete_monitor_group_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_monitor_group_with_options_async(request, runtime)

    def delete_monitor_group_dynamic_rule_with_options(
        self,
        request: cms_20190101_models.DeleteMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_dynamic_rule_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_dynamic_rule(
        self,
        request: cms_20190101_models.DeleteMonitorGroupDynamicRuleRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_dynamic_rule_with_options(request, runtime)

    async def delete_monitor_group_dynamic_rule_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupDynamicRuleRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_monitor_group_dynamic_rule_with_options_async(request, runtime)

    def delete_monitor_group_instances_with_options(
        self,
        request: cms_20190101_models.DeleteMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_instances(
        self,
        request: cms_20190101_models.DeleteMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_instances_with_options(request, runtime)

    async def delete_monitor_group_instances_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_monitor_group_instances_with_options_async(request, runtime)

    def delete_monitor_group_notify_policy_with_options(
        self,
        request: cms_20190101_models.DeleteMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_notify_policy_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_notify_policy(
        self,
        request: cms_20190101_models.DeleteMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_notify_policy_with_options(request, runtime)

    async def delete_monitor_group_notify_policy_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_monitor_group_notify_policy_with_options_async(request, runtime)

    def delete_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.DeleteMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitoring_agent_process(
        self,
        request: cms_20190101_models.DeleteMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DeleteMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_monitoring_agent_process_with_options(request, runtime)

    async def delete_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.DeleteMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DeleteMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_monitoring_agent_process_with_options_async(request, runtime)

    def delete_site_monitors_with_options(
        self,
        request: cms_20190101_models.DeleteSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_delete_alarms):
            query['IsDeleteAlarms'] = request.is_delete_alarms
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.DeleteSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_delete_alarms):
            query['IsDeleteAlarms'] = request.is_delete_alarms
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_site_monitors(
        self,
        request: cms_20190101_models.DeleteSiteMonitorsRequest,
    ) -> cms_20190101_models.DeleteSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_site_monitors_with_options(request, runtime)

    async def delete_site_monitors_async(
        self,
        request: cms_20190101_models.DeleteSiteMonitorsRequest,
    ) -> cms_20190101_models.DeleteSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_site_monitors_with_options_async(request, runtime)

    def describe_active_metric_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeActiveMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeActiveMetricRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeActiveMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_metric_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeActiveMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeActiveMetricRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeActiveMetricRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_metric_rule_list(
        self,
        request: cms_20190101_models.DescribeActiveMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeActiveMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_metric_rule_list_with_options(request, runtime)

    async def describe_active_metric_rule_list_async(
        self,
        request: cms_20190101_models.DescribeActiveMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeActiveMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_metric_rule_list_with_options_async(request, runtime)

    def describe_alert_history_list_with_options(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        
        @param request: DescribeAlertHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending):
            query['Ascending'] = request.ascending
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertHistoryList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_history_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        
        @param request: DescribeAlertHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending):
            query['Ascending'] = request.ascending
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertHistoryList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_history_list(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        
        @param request: DescribeAlertHistoryListRequest
        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_history_list_with_options(request, runtime)

    async def describe_alert_history_list_async(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        
        @param request: DescribeAlertHistoryListRequest
        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_history_list_with_options_async(request, runtime)

    def describe_alert_log_count_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        
        @param request: DescribeAlertLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        
        @param request: DescribeAlertLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_count(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        
        @param request: DescribeAlertLogCountRequest
        @return: DescribeAlertLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_count_with_options(request, runtime)

    async def describe_alert_log_count_async(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        
        @param request: DescribeAlertLogCountRequest
        @return: DescribeAlertLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_count_with_options_async(request, runtime)

    def describe_alert_log_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        
        @param request: DescribeAlertLogHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogHistogramResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        
        @param request: DescribeAlertLogHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogHistogramResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_histogram(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        
        @param request: DescribeAlertLogHistogramRequest
        @return: DescribeAlertLogHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_histogram_with_options(request, runtime)

    async def describe_alert_log_histogram_async(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        
        @param request: DescribeAlertLogHistogramRequest
        @return: DescribeAlertLogHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_histogram_with_options_async(request, runtime)

    def describe_alert_log_list_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeAlertLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeAlertLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_list(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeAlertLogListRequest
        @return: DescribeAlertLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_list_with_options(request, runtime)

    async def describe_alert_log_list_async(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeAlertLogListRequest
        @return: DescribeAlertLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_list_with_options_async(request, runtime)

    def describe_alerting_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertingMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerting_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertingMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerting_metric_rule_resources(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alerting_metric_rule_resources_with_options(request, runtime)

    async def describe_alerting_metric_rule_resources_async(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alerting_metric_rule_resources_with_options_async(request, runtime)

    def describe_contact_group_list_with_options(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroupList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_group_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroupList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_group_list(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_group_list_with_options(request, runtime)

    async def describe_contact_group_list_async(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_group_list_with_options_async(request, runtime)

    def describe_contact_list_with_options(
        self,
        request: cms_20190101_models.DescribeContactListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chanel_type):
            query['ChanelType'] = request.chanel_type
        if not UtilClient.is_unset(request.chanel_value):
            query['ChanelValue'] = request.chanel_value
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chanel_type):
            query['ChanelType'] = request.chanel_type
        if not UtilClient.is_unset(request.chanel_value):
            query['ChanelValue'] = request.chanel_value
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_list(
        self,
        request: cms_20190101_models.DescribeContactListRequest,
    ) -> cms_20190101_models.DescribeContactListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_list_with_options(request, runtime)

    async def describe_contact_list_async(
        self,
        request: cms_20190101_models.DescribeContactListRequest,
    ) -> cms_20190101_models.DescribeContactListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_list_with_options_async(request, runtime)

    def describe_contact_list_by_contact_group_with_options(
        self,
        request: cms_20190101_models.DescribeContactListByContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListByContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactListByContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListByContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_list_by_contact_group_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactListByContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListByContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactListByContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListByContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_list_by_contact_group(
        self,
        request: cms_20190101_models.DescribeContactListByContactGroupRequest,
    ) -> cms_20190101_models.DescribeContactListByContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_list_by_contact_group_with_options(request, runtime)

    async def describe_contact_list_by_contact_group_async(
        self,
        request: cms_20190101_models.DescribeContactListByContactGroupRequest,
    ) -> cms_20190101_models.DescribeContactListByContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_list_by_contact_group_with_options_async(request, runtime)

    def describe_custom_event_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeCustomEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_attribute(
        self,
        request: cms_20190101_models.DescribeCustomEventAttributeRequest,
    ) -> cms_20190101_models.DescribeCustomEventAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_attribute_with_options(request, runtime)

    async def describe_custom_event_attribute_async(
        self,
        request: cms_20190101_models.DescribeCustomEventAttributeRequest,
    ) -> cms_20190101_models.DescribeCustomEventAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_event_attribute_with_options_async(request, runtime)

    def describe_custom_event_count_with_options(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        """
        The name of the custom event.
        
        @param request: DescribeCustomEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        """
        The name of the custom event.
        
        @param request: DescribeCustomEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_count(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        """
        The name of the custom event.
        
        @param request: DescribeCustomEventCountRequest
        @return: DescribeCustomEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_count_with_options(request, runtime)

    async def describe_custom_event_count_async(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        """
        The name of the custom event.
        
        @param request: DescribeCustomEventCountRequest
        @return: DescribeCustomEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_event_count_with_options_async(request, runtime)

    def describe_custom_event_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_histogram(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_histogram_with_options(request, runtime)

    async def describe_custom_event_histogram_async(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_event_histogram_with_options_async(request, runtime)

    def describe_custom_metric_list_with_options(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: DescribeCustomMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_metric_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: DescribeCustomMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_metric_list(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: DescribeCustomMetricListRequest
        @return: DescribeCustomMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_metric_list_with_options(request, runtime)

    async def describe_custom_metric_list_async(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        
        @param request: DescribeCustomMetricListRequest
        @return: DescribeCustomMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_metric_list_with_options_async(request, runtime)

    def describe_dynamic_tag_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeDynamicTagRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDynamicTagRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDynamicTagRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeDynamicTagRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dynamic_tag_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeDynamicTagRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDynamicTagRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDynamicTagRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeDynamicTagRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dynamic_tag_rule_list(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeDynamicTagRuleListRequest
        @return: DescribeDynamicTagRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dynamic_tag_rule_list_with_options(request, runtime)

    async def describe_dynamic_tag_rule_list_async(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeDynamicTagRuleListRequest
        @return: DescribeDynamicTagRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dynamic_tag_rule_list_with_options_async(request, runtime)

    def describe_event_rule_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        
        @param request: DescribeEventRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        
        @param request: DescribeEventRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_attribute(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        
        @param request: DescribeEventRuleAttributeRequest
        @return: DescribeEventRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_attribute_with_options(request, runtime)

    async def describe_event_rule_attribute_async(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        
        @param request: DescribeEventRuleAttributeRequest
        @return: DescribeEventRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_rule_attribute_with_options_async(request, runtime)

    def describe_event_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_list(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_list_with_options(request, runtime)

    async def describe_event_rule_list_async(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_rule_list_with_options_async(request, runtime)

    def describe_event_rule_target_list_with_options(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        """
        The error message.
        
        @param request: DescribeEventRuleTargetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventRuleTargetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleTargetList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleTargetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_target_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        """
        The error message.
        
        @param request: DescribeEventRuleTargetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventRuleTargetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleTargetList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleTargetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_target_list(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        """
        The error message.
        
        @param request: DescribeEventRuleTargetListRequest
        @return: DescribeEventRuleTargetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_target_list_with_options(request, runtime)

    async def describe_event_rule_target_list_async(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        """
        The error message.
        
        @param request: DescribeEventRuleTargetListRequest
        @return: DescribeEventRuleTargetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_rule_target_list_with_options_async(request, runtime)

    def describe_exporter_output_list_with_options(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterOutputList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exporter_output_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterOutputList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterOutputListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exporter_output_list(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exporter_output_list_with_options(request, runtime)

    async def describe_exporter_output_list_async(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exporter_output_list_with_options_async(request, runtime)

    def describe_exporter_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeExporterRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exporter_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeExporterRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterRuleListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exporter_rule_list(
        self,
        request: cms_20190101_models.DescribeExporterRuleListRequest,
    ) -> cms_20190101_models.DescribeExporterRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exporter_rule_list_with_options(request, runtime)

    async def describe_exporter_rule_list_async(
        self,
        request: cms_20190101_models.DescribeExporterRuleListRequest,
    ) -> cms_20190101_models.DescribeExporterRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exporter_rule_list_with_options_async(request, runtime)

    def describe_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        """
        The ID of the application group.
        
        @param request: DescribeGroupMonitoringAgentProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        """
        The ID of the application group.
        
        @param request: DescribeGroupMonitoringAgentProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_monitoring_agent_process(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        """
        The ID of the application group.
        
        @param request: DescribeGroupMonitoringAgentProcessRequest
        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_monitoring_agent_process_with_options(request, runtime)

    async def describe_group_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        """
        The ID of the application group.
        
        @param request: DescribeGroupMonitoringAgentProcessRequest
        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_monitoring_agent_process_with_options_async(request, runtime)

    def describe_host_availability_list_with_options(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        """
        The ID of the availability monitoring task.
        
        @param request: DescribeHostAvailabilityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostAvailabilityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostAvailabilityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHostAvailabilityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_host_availability_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        """
        The ID of the availability monitoring task.
        
        @param request: DescribeHostAvailabilityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostAvailabilityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostAvailabilityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHostAvailabilityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_host_availability_list(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        """
        The ID of the availability monitoring task.
        
        @param request: DescribeHostAvailabilityListRequest
        @return: DescribeHostAvailabilityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_host_availability_list_with_options(request, runtime)

    async def describe_host_availability_list_async(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        """
        The ID of the availability monitoring task.
        
        @param request: DescribeHostAvailabilityListRequest
        @return: DescribeHostAvailabilityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_availability_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_data_list_with_options(
        self,
        request: cms_20190101_models.DescribeHybridMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorDataListResponse:
        """
        The tag key.
        
        @param request: DescribeHybridMonitorDataListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prom_sql):
            query['PromSQL'] = request.prom_sql
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorDataList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_data_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorDataListResponse:
        """
        The tag key.
        
        @param request: DescribeHybridMonitorDataListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prom_sql):
            query['PromSQL'] = request.prom_sql
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorDataList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_data_list(
        self,
        request: cms_20190101_models.DescribeHybridMonitorDataListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorDataListResponse:
        """
        The tag key.
        
        @param request: DescribeHybridMonitorDataListRequest
        @return: DescribeHybridMonitorDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_data_list_with_options(request, runtime)

    async def describe_hybrid_monitor_data_list_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorDataListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorDataListResponse:
        """
        The tag key.
        
        @param request: DescribeHybridMonitorDataListRequest
        @return: DescribeHybridMonitorDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_monitor_data_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_namespace_list_with_options(
        self,
        request: cms_20190101_models.DescribeHybridMonitorNamespaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorNamespaceListResponse:
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        
        @param request: DescribeHybridMonitorNamespaceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorNamespaceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_task_statistic):
            query['ShowTaskStatistic'] = request.show_task_statistic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorNamespaceList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_namespace_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorNamespaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorNamespaceListResponse:
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        
        @param request: DescribeHybridMonitorNamespaceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorNamespaceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_task_statistic):
            query['ShowTaskStatistic'] = request.show_task_statistic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorNamespaceList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_namespace_list(
        self,
        request: cms_20190101_models.DescribeHybridMonitorNamespaceListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorNamespaceListResponse:
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        
        @param request: DescribeHybridMonitorNamespaceListRequest
        @return: DescribeHybridMonitorNamespaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_namespace_list_with_options(request, runtime)

    async def describe_hybrid_monitor_namespace_list_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorNamespaceListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorNamespaceListResponse:
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        
        @param request: DescribeHybridMonitorNamespaceListRequest
        @return: DescribeHybridMonitorNamespaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_monitor_namespace_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_slsgroup_with_options(
        self,
        request: cms_20190101_models.DescribeHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DescribeHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DescribeHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_slsgroup(
        self,
        request: cms_20190101_models.DescribeHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DescribeHybridMonitorSLSGroupRequest
        @return: DescribeHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def describe_hybrid_monitor_slsgroup_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorSLSGroupResponse:
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        
        @param request: DescribeHybridMonitorSLSGroupRequest
        @return: DescribeHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def describe_hybrid_monitor_task_list_with_options(
        self,
        request: cms_20190101_models.DescribeHybridMonitorTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorTaskListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeHybridMonitorTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.include_aliyun_task):
            query['IncludeAliyunTask'] = request.include_aliyun_task
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorTaskList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_task_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHybridMonitorTaskListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeHybridMonitorTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridMonitorTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.include_aliyun_task):
            query['IncludeAliyunTask'] = request.include_aliyun_task
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorTaskList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_task_list(
        self,
        request: cms_20190101_models.DescribeHybridMonitorTaskListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorTaskListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeHybridMonitorTaskListRequest
        @return: DescribeHybridMonitorTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_task_list_with_options(request, runtime)

    async def describe_hybrid_monitor_task_list_async(
        self,
        request: cms_20190101_models.DescribeHybridMonitorTaskListRequest,
    ) -> cms_20190101_models.DescribeHybridMonitorTaskListResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: DescribeHybridMonitorTaskListRequest
        @return: DescribeHybridMonitorTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_monitor_task_list_with_options_async(request, runtime)

    def describe_log_monitor_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_monitor_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_monitor_attribute(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_monitor_attribute_with_options(request, runtime)

    async def describe_log_monitor_attribute_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_monitor_attribute_with_options_async(request, runtime)

    def describe_log_monitor_list_with_options(
        self,
        request: cms_20190101_models.DescribeLogMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_monitor_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_monitor_list(
        self,
        request: cms_20190101_models.DescribeLogMonitorListRequest,
    ) -> cms_20190101_models.DescribeLogMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_monitor_list_with_options(request, runtime)

    async def describe_log_monitor_list_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorListRequest,
    ) -> cms_20190101_models.DescribeLogMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_monitor_list_with_options_async(request, runtime)

    def describe_metric_data_with_options(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_data_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_data(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricDataRequest
        @return: DescribeMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    async def describe_metric_data_async(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricDataRequest
        @return: DescribeMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_data_with_options_async(request, runtime)

    def describe_metric_last_with_options(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        
        @param request: DescribeMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricLastResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricLast',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_last_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        
        @param request: DescribeMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricLastResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricLast',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_last(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        
        @param request: DescribeMetricLastRequest
        @return: DescribeMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_last_with_options(request, runtime)

    async def describe_metric_last_async(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        
        @param request: DescribeMetricLastRequest
        @return: DescribeMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_last_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_list(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricListRequest
        @return: DescribeMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricListRequest
        @return: DescribeMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_metric_meta_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_meta_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_meta_list(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricMetaListRequest
        @return: DescribeMetricMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_meta_list_with_options(request, runtime)

    async def describe_metric_meta_list_async(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        
        @param request: DescribeMetricMetaListRequest
        @return: DescribeMetricMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_meta_list_with_options_async(request, runtime)

    def describe_metric_rule_black_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_black_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_black_list(
        self,
        request: cms_20190101_models.DescribeMetricRuleBlackListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_black_list_with_options(request, runtime)

    async def describe_metric_rule_black_list_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleBlackListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_black_list_with_options_async(request, runtime)

    def describe_metric_rule_count_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_count(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_count_with_options(request, runtime)

    async def describe_metric_rule_count_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_count_with_options_async(request, runtime)

    def describe_metric_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        
        @param request: DescribeMetricRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_state):
            query['AlertState'] = request.alert_state
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.enable_state):
            query['EnableState'] = request.enable_state
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        
        @param request: DescribeMetricRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_state):
            query['AlertState'] = request.alert_state
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.enable_state):
            query['EnableState'] = request.enable_state
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_list(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        
        @param request: DescribeMetricRuleListRequest
        @return: DescribeMetricRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_list_with_options(request, runtime)

    async def describe_metric_rule_list_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        
        @param request: DescribeMetricRuleListRequest
        @return: DescribeMetricRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_list_with_options_async(request, runtime)

    def describe_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        
        @param request: DescribeMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        
        @param request: DescribeMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_targets(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        
        @param request: DescribeMetricRuleTargetsRequest
        @return: DescribeMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_targets_with_options(request, runtime)

    async def describe_metric_rule_targets_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        
        @param request: DescribeMetricRuleTargetsRequest
        @return: DescribeMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_targets_with_options_async(request, runtime)

    def describe_metric_rule_template_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        
        @param request: DescribeMetricRuleTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_template_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        
        @param request: DescribeMetricRuleTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_template_attribute(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        
        @param request: DescribeMetricRuleTemplateAttributeRequest
        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_attribute_with_options(request, runtime)

    async def describe_metric_rule_template_attribute_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        
        @param request: DescribeMetricRuleTemplateAttributeRequest
        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_template_attribute_with_options_async(request, runtime)

    def describe_metric_rule_template_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeMetricRuleTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.history):
            query['History'] = request.history
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_template_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeMetricRuleTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricRuleTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.history):
            query['History'] = request.history
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_template_list(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeMetricRuleTemplateListRequest
        @return: DescribeMetricRuleTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_list_with_options(request, runtime)

    async def describe_metric_rule_template_list_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        
        @param request: DescribeMetricRuleTemplateListRequest
        @return: DescribeMetricRuleTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_template_list_with_options_async(request, runtime)

    def describe_metric_top_with_options(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        
        @param request: DescribeMetricTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricTopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricTop',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_top_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        
        @param request: DescribeMetricTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricTopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricTop',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_top(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        
        @param request: DescribeMetricTopRequest
        @return: DescribeMetricTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_top_with_options(request, runtime)

    async def describe_metric_top_async(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        
        @param request: DescribeMetricTopRequest
        @return: DescribeMetricTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_top_with_options_async(request, runtime)

    def describe_monitor_group_categories_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupCategories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_categories_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupCategories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_categories(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_categories_with_options(request, runtime)

    async def describe_monitor_group_categories_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_group_categories_with_options_async(request, runtime)

    def describe_monitor_group_dynamic_rules_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupDynamicRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupDynamicRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_dynamic_rules_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupDynamicRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupDynamicRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_dynamic_rules(
        self,
        request: cms_20190101_models.DescribeMonitorGroupDynamicRulesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_dynamic_rules_with_options(request, runtime)

    async def describe_monitor_group_dynamic_rules_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupDynamicRulesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_group_dynamic_rules_with_options_async(request, runtime)

    def describe_monitor_group_instance_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstanceAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_instance_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstanceAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_instance_attribute(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstanceAttributeRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_instance_attribute_with_options(request, runtime)

    async def describe_monitor_group_instance_attribute_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstanceAttributeRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_group_instance_attribute_with_options_async(request, runtime)

    def describe_monitor_group_instances_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_instances(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_instances_with_options(request, runtime)

    async def describe_monitor_group_instances_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_group_instances_with_options_async(request, runtime)

    def describe_monitor_group_notify_policy_list_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupNotifyPolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupNotifyPolicyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_notify_policy_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupNotifyPolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupNotifyPolicyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_notify_policy_list(
        self,
        request: cms_20190101_models.DescribeMonitorGroupNotifyPolicyListRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_notify_policy_list_with_options(request, runtime)

    async def describe_monitor_group_notify_policy_list_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupNotifyPolicyListRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_group_notify_policy_list_with_options_async(request, runtime)

    def describe_monitor_groups_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        
        @param request: DescribeMonitorGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.group_founder_tag_key):
            query['GroupFounderTagKey'] = request.group_founder_tag_key
        if not UtilClient.is_unset(request.group_founder_tag_value):
            query['GroupFounderTagValue'] = request.group_founder_tag_value
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.include_template_history):
            query['IncludeTemplateHistory'] = request.include_template_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_groups_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        
        @param request: DescribeMonitorGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.group_founder_tag_key):
            query['GroupFounderTagKey'] = request.group_founder_tag_key
        if not UtilClient.is_unset(request.group_founder_tag_value):
            query['GroupFounderTagValue'] = request.group_founder_tag_value
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.include_template_history):
            query['IncludeTemplateHistory'] = request.include_template_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_groups(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        
        @param request: DescribeMonitorGroupsRequest
        @return: DescribeMonitorGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_groups_with_options(request, runtime)

    async def describe_monitor_groups_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        
        @param request: DescribeMonitorGroupsRequest
        @return: DescribeMonitorGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_groups_with_options_async(request, runtime)

    def describe_monitor_resource_quota_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.show_used):
            query['ShowUsed'] = request.show_used
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorResourceQuotaAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_resource_quota_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.show_used):
            query['ShowUsed'] = request.show_used
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorResourceQuotaAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_resource_quota_attribute(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_resource_quota_attribute_with_options(request, runtime)

    async def describe_monitor_resource_quota_attribute_async(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_resource_quota_attribute_with_options_async(request, runtime)

    def describe_monitoring_agent_access_key_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentAccessKey',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_access_key_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentAccessKey',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_access_key(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_access_key_with_options(request, runtime)

    async def describe_monitoring_agent_access_key_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_access_key_with_options_async(request, runtime)

    def describe_monitoring_agent_config_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_config_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_config(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentConfigRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_config_with_options(request, runtime)

    async def describe_monitoring_agent_config_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentConfigRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_config_with_options_async(request, runtime)

    def describe_monitoring_agent_hosts_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_host):
            query['AliyunHost'] = request.aliyun_host
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sysom_status):
            query['SysomStatus'] = request.sysom_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentHosts',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_hosts_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_host):
            query['AliyunHost'] = request.aliyun_host
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sysom_status):
            query['SysomStatus'] = request.sysom_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentHosts',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_hosts(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentHostsRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_hosts_with_options(request, runtime)

    async def describe_monitoring_agent_hosts_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentHostsRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_hosts_with_options_async(request, runtime)

    def describe_monitoring_agent_processes_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        
        @param request: DescribeMonitoringAgentProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitoringAgentProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentProcesses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_processes_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        
        @param request: DescribeMonitoringAgentProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitoringAgentProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentProcesses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_processes(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        
        @param request: DescribeMonitoringAgentProcessesRequest
        @return: DescribeMonitoringAgentProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_processes_with_options(request, runtime)

    async def describe_monitoring_agent_processes_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        
        @param request: DescribeMonitoringAgentProcessesRequest
        @return: DescribeMonitoringAgentProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_processes_with_options_async(request, runtime)

    def describe_monitoring_agent_statuses_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        
        @param request: DescribeMonitoringAgentStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitoringAgentStatusesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_availability_task_id):
            query['HostAvailabilityTaskId'] = request.host_availability_task_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentStatuses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_statuses_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        
        @param request: DescribeMonitoringAgentStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitoringAgentStatusesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_availability_task_id):
            query['HostAvailabilityTaskId'] = request.host_availability_task_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentStatuses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_statuses(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        
        @param request: DescribeMonitoringAgentStatusesRequest
        @return: DescribeMonitoringAgentStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_statuses_with_options(request, runtime)

    async def describe_monitoring_agent_statuses_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        
        @param request: DescribeMonitoringAgentStatusesRequest
        @return: DescribeMonitoringAgentStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_statuses_with_options_async(request, runtime)

    def describe_monitoring_config_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_config_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_config(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_config_with_options(request, runtime)

    async def describe_monitoring_config_async(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_config_with_options_async(request, runtime)

    def describe_product_resource_tag_key_list_with_options(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        
        @param request: DescribeProductResourceTagKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductResourceTagKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProductResourceTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductResourceTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_resource_tag_key_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        
        @param request: DescribeProductResourceTagKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductResourceTagKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProductResourceTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductResourceTagKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_resource_tag_key_list(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        
        @param request: DescribeProductResourceTagKeyListRequest
        @return: DescribeProductResourceTagKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_resource_tag_key_list_with_options(request, runtime)

    async def describe_product_resource_tag_key_list_async(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        
        @param request: DescribeProductResourceTagKeyListRequest
        @return: DescribeProductResourceTagKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_resource_tag_key_list_with_options_async(request, runtime)

    def describe_products_of_active_metric_rule_with_options(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeProductsOfActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_of_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeProductsOfActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products_of_active_metric_rule(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_products_of_active_metric_rule_with_options(request, runtime)

    async def describe_products_of_active_metric_rule_async(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_products_of_active_metric_rule_with_options_async(request, runtime)

    def describe_project_meta_with_options(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        
        @param request: DescribeProjectMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectMeta',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProjectMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_meta_with_options_async(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        
        @param request: DescribeProjectMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectMeta',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProjectMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_meta(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        
        @param request: DescribeProjectMetaRequest
        @return: DescribeProjectMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_meta_with_options(request, runtime)

    async def describe_project_meta_async(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        
        @param request: DescribeProjectMetaRequest
        @return: DescribeProjectMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_meta_with_options_async(request, runtime)

    def describe_site_monitor_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        
        @param request: DescribeSiteMonitorAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_alert):
            query['IncludeAlert'] = request.include_alert
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        
        @param request: DescribeSiteMonitorAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_alert):
            query['IncludeAlert'] = request.include_alert
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_attribute(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        
        @param request: DescribeSiteMonitorAttributeRequest
        @return: DescribeSiteMonitorAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_attribute_with_options(request, runtime)

    async def describe_site_monitor_attribute_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        
        @param request: DescribeSiteMonitorAttributeRequest
        @return: DescribeSiteMonitorAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_attribute_with_options_async(request, runtime)

    def describe_site_monitor_data_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_data_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_data(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_data_with_options(request, runtime)

    async def describe_site_monitor_data_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_data_with_options_async(request, runtime)

    def describe_site_monitor_ispcity_list_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorISPCityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorISPCityListResponse:
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        
        @param request: DescribeSiteMonitorISPCityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorISPCityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.ipv4):
            query['IPV4'] = request.ipv4
        if not UtilClient.is_unset(request.ipv6):
            query['IPV6'] = request.ipv6
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorISPCityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorISPCityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_ispcity_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorISPCityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorISPCityListResponse:
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        
        @param request: DescribeSiteMonitorISPCityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorISPCityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.ipv4):
            query['IPV4'] = request.ipv4
        if not UtilClient.is_unset(request.ipv6):
            query['IPV6'] = request.ipv6
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorISPCityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorISPCityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_ispcity_list(
        self,
        request: cms_20190101_models.DescribeSiteMonitorISPCityListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorISPCityListResponse:
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        
        @param request: DescribeSiteMonitorISPCityListRequest
        @return: DescribeSiteMonitorISPCityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_ispcity_list_with_options(request, runtime)

    async def describe_site_monitor_ispcity_list_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorISPCityListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorISPCityListResponse:
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        
        @param request: DescribeSiteMonitorISPCityListRequest
        @return: DescribeSiteMonitorISPCityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_ispcity_list_with_options_async(request, runtime)

    def describe_site_monitor_list_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        """
        The content of the HTTP request.
        
        @param request: DescribeSiteMonitorListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_state):
            query['TaskState'] = request.task_state
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        """
        The content of the HTTP request.
        
        @param request: DescribeSiteMonitorListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_state):
            query['TaskState'] = request.task_state
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_list(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        """
        The content of the HTTP request.
        
        @param request: DescribeSiteMonitorListRequest
        @return: DescribeSiteMonitorListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_list_with_options(request, runtime)

    async def describe_site_monitor_list_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        """
        The content of the HTTP request.
        
        @param request: DescribeSiteMonitorListRequest
        @return: DescribeSiteMonitorListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_list_with_options_async(request, runtime)

    def describe_site_monitor_log_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorLogResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        
        @param request: DescribeSiteMonitorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorLog',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_log_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorLogResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        
        @param request: DescribeSiteMonitorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSiteMonitorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorLog',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_log(
        self,
        request: cms_20190101_models.DescribeSiteMonitorLogRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorLogResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        
        @param request: DescribeSiteMonitorLogRequest
        @return: DescribeSiteMonitorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_log_with_options(request, runtime)

    async def describe_site_monitor_log_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorLogRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorLogResponse:
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        
        @param request: DescribeSiteMonitorLogRequest
        @return: DescribeSiteMonitorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_log_with_options_async(request, runtime)

    def describe_site_monitor_quota_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSiteMonitorQuota',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_quota_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSiteMonitorQuota',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_quota(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_quota_with_options(request, runtime)

    async def describe_site_monitor_quota_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_quota_with_options_async(request, runtime)

    def describe_site_monitor_statistics_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorStatistics',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_statistics_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorStatistics',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_statistics(
        self,
        request: cms_20190101_models.DescribeSiteMonitorStatisticsRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_statistics_with_options(request, runtime)

    async def describe_site_monitor_statistics_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorStatisticsRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_statistics_with_options_async(request, runtime)

    def describe_system_event_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeSystemEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_attribute(
        self,
        request: cms_20190101_models.DescribeSystemEventAttributeRequest,
    ) -> cms_20190101_models.DescribeSystemEventAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_attribute_with_options(request, runtime)

    async def describe_system_event_attribute_async(
        self,
        request: cms_20190101_models.DescribeSystemEventAttributeRequest,
    ) -> cms_20190101_models.DescribeSystemEventAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_event_attribute_with_options_async(request, runtime)

    def describe_system_event_count_with_options(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        
        @param request: DescribeSystemEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        
        @param request: DescribeSystemEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_count(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        
        @param request: DescribeSystemEventCountRequest
        @return: DescribeSystemEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_count_with_options(request, runtime)

    async def describe_system_event_count_async(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        
        @param request: DescribeSystemEventCountRequest
        @return: DescribeSystemEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_event_count_with_options_async(request, runtime)

    def describe_system_event_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_histogram(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_histogram_with_options(request, runtime)

    async def describe_system_event_histogram_async(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_event_histogram_with_options_async(request, runtime)

    def describe_system_event_meta_list_with_options(
        self,
        request: cms_20190101_models.DescribeSystemEventMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSystemEventMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_meta_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSystemEventMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_meta_list(
        self,
        request: cms_20190101_models.DescribeSystemEventMetaListRequest,
    ) -> cms_20190101_models.DescribeSystemEventMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_meta_list_with_options(request, runtime)

    async def describe_system_event_meta_list_async(
        self,
        request: cms_20190101_models.DescribeSystemEventMetaListRequest,
    ) -> cms_20190101_models.DescribeSystemEventMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_event_meta_list_with_options_async(request, runtime)

    def describe_tag_key_list_with_options(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_key_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_key_list(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_key_list_with_options(request, runtime)

    async def describe_tag_key_list_async(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_key_list_with_options_async(request, runtime)

    def describe_tag_value_list_with_options(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        
        @param request: DescribeTagValueListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValueListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValueList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_value_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        
        @param request: DescribeTagValueListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValueListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValueList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagValueListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_value_list(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        
        @param request: DescribeTagValueListRequest
        @return: DescribeTagValueListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_value_list_with_options(request, runtime)

    async def describe_tag_value_list_async(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        
        @param request: DescribeTagValueListRequest
        @return: DescribeTagValueListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_value_list_with_options_async(request, runtime)

    def describe_unhealthy_host_availability_with_options(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnhealthyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unhealthy_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnhealthyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_unhealthy_host_availability(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_unhealthy_host_availability_with_options(request, runtime)

    async def describe_unhealthy_host_availability_async(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_unhealthy_host_availability_with_options_async(request, runtime)

    def disable_active_metric_rule_with_options(
        self,
        request: cms_20190101_models.DisableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.DisableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_active_metric_rule(
        self,
        request: cms_20190101_models.DisableActiveMetricRuleRequest,
    ) -> cms_20190101_models.DisableActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_active_metric_rule_with_options(request, runtime)

    async def disable_active_metric_rule_async(
        self,
        request: cms_20190101_models.DisableActiveMetricRuleRequest,
    ) -> cms_20190101_models.DisableActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_active_metric_rule_with_options_async(request, runtime)

    def disable_event_rules_with_options(
        self,
        request: cms_20190101_models.DisableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_event_rules_with_options_async(
        self,
        request: cms_20190101_models.DisableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_event_rules(
        self,
        request: cms_20190101_models.DisableEventRulesRequest,
    ) -> cms_20190101_models.DisableEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_event_rules_with_options(request, runtime)

    async def disable_event_rules_async(
        self,
        request: cms_20190101_models.DisableEventRulesRequest,
    ) -> cms_20190101_models.DisableEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_event_rules_with_options_async(request, runtime)

    def disable_host_availability_with_options(
        self,
        request: cms_20190101_models.DisableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DisableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_host_availability(
        self,
        request: cms_20190101_models.DisableHostAvailabilityRequest,
    ) -> cms_20190101_models.DisableHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_host_availability_with_options(request, runtime)

    async def disable_host_availability_async(
        self,
        request: cms_20190101_models.DisableHostAvailabilityRequest,
    ) -> cms_20190101_models.DisableHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_host_availability_with_options_async(request, runtime)

    def disable_metric_rules_with_options(
        self,
        request: cms_20190101_models.DisableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.DisableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_metric_rules(
        self,
        request: cms_20190101_models.DisableMetricRulesRequest,
    ) -> cms_20190101_models.DisableMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_metric_rules_with_options(request, runtime)

    async def disable_metric_rules_async(
        self,
        request: cms_20190101_models.DisableMetricRulesRequest,
    ) -> cms_20190101_models.DisableMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_metric_rules_with_options_async(request, runtime)

    def disable_site_monitors_with_options(
        self,
        request: cms_20190101_models.DisableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.DisableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_site_monitors(
        self,
        request: cms_20190101_models.DisableSiteMonitorsRequest,
    ) -> cms_20190101_models.DisableSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_site_monitors_with_options(request, runtime)

    async def disable_site_monitors_async(
        self,
        request: cms_20190101_models.DisableSiteMonitorsRequest,
    ) -> cms_20190101_models.DisableSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_site_monitors_with_options_async(request, runtime)

    def enable_active_metric_rule_with_options(
        self,
        request: cms_20190101_models.EnableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.EnableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_active_metric_rule(
        self,
        request: cms_20190101_models.EnableActiveMetricRuleRequest,
    ) -> cms_20190101_models.EnableActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_active_metric_rule_with_options(request, runtime)

    async def enable_active_metric_rule_async(
        self,
        request: cms_20190101_models.EnableActiveMetricRuleRequest,
    ) -> cms_20190101_models.EnableActiveMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_active_metric_rule_with_options_async(request, runtime)

    def enable_event_rules_with_options(
        self,
        request: cms_20190101_models.EnableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_event_rules_with_options_async(
        self,
        request: cms_20190101_models.EnableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableEventRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_event_rules(
        self,
        request: cms_20190101_models.EnableEventRulesRequest,
    ) -> cms_20190101_models.EnableEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_event_rules_with_options(request, runtime)

    async def enable_event_rules_async(
        self,
        request: cms_20190101_models.EnableEventRulesRequest,
    ) -> cms_20190101_models.EnableEventRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_event_rules_with_options_async(request, runtime)

    def enable_host_availability_with_options(
        self,
        request: cms_20190101_models.EnableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_host_availability_with_options_async(
        self,
        request: cms_20190101_models.EnableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_host_availability(
        self,
        request: cms_20190101_models.EnableHostAvailabilityRequest,
    ) -> cms_20190101_models.EnableHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_host_availability_with_options(request, runtime)

    async def enable_host_availability_async(
        self,
        request: cms_20190101_models.EnableHostAvailabilityRequest,
    ) -> cms_20190101_models.EnableHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_host_availability_with_options_async(request, runtime)

    def enable_metric_rule_black_list_with_options(
        self,
        request: cms_20190101_models.EnableMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_rule_black_list_with_options_async(
        self,
        request: cms_20190101_models.EnableMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric_rule_black_list(
        self,
        request: cms_20190101_models.EnableMetricRuleBlackListRequest,
    ) -> cms_20190101_models.EnableMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_rule_black_list_with_options(request, runtime)

    async def enable_metric_rule_black_list_async(
        self,
        request: cms_20190101_models.EnableMetricRuleBlackListRequest,
    ) -> cms_20190101_models.EnableMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_metric_rule_black_list_with_options_async(request, runtime)

    def enable_metric_rules_with_options(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric_rules(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_rules_with_options(request, runtime)

    async def enable_metric_rules_async(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_metric_rules_with_options_async(request, runtime)

    def enable_site_monitors_with_options(
        self,
        request: cms_20190101_models.EnableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.EnableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_site_monitors(
        self,
        request: cms_20190101_models.EnableSiteMonitorsRequest,
    ) -> cms_20190101_models.EnableSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_site_monitors_with_options(request, runtime)

    async def enable_site_monitors_async(
        self,
        request: cms_20190101_models.EnableSiteMonitorsRequest,
    ) -> cms_20190101_models.EnableSiteMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_site_monitors_with_options_async(request, runtime)

    def install_monitoring_agent_with_options(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: InstallMonitoringAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.install_command):
            query['InstallCommand'] = request.install_command
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.InstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_monitoring_agent_with_options_async(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: InstallMonitoringAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.install_command):
            query['InstallCommand'] = request.install_command
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.InstallMonitoringAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_monitoring_agent(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: InstallMonitoringAgentRequest
        @return: InstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_monitoring_agent_with_options(request, runtime)

    async def install_monitoring_agent_async(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: InstallMonitoringAgentRequest
        @return: InstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_monitoring_agent_with_options_async(request, runtime)

    def modify_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group_monitoring_agent_process(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_group_monitoring_agent_process_with_options(request, runtime)

    async def modify_group_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_group_monitoring_agent_process_with_options_async(request, runtime)

    def modify_host_availability_with_options(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHostAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_availability_with_options_async(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHostAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_availability(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHostAvailabilityRequest
        @return: ModifyHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_availability_with_options(request, runtime)

    async def modify_host_availability_async(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHostAvailabilityRequest
        @return: ModifyHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_availability_with_options_async(request, runtime)

    def modify_host_info_with_options(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        """
        ***\
        
        @param request: ModifyHostInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_info_with_options_async(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        """
        ***\
        
        @param request: ModifyHostInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_info(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        """
        ***\
        
        @param request: ModifyHostInfoRequest
        @return: ModifyHostInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_info_with_options(request, runtime)

    async def modify_host_info_async(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        """
        ***\
        
        @param request: ModifyHostInfoRequest
        @return: ModifyHostInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_info_with_options_async(request, runtime)

    def modify_hybrid_monitor_namespace_with_options(
        self,
        request: cms_20190101_models.ModifyHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_namespace_with_options_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHybridMonitorNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_namespace(
        self,
        request: cms_20190101_models.ModifyHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHybridMonitorNamespaceRequest
        @return: ModifyHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_namespace_with_options(request, runtime)

    async def modify_hybrid_monitor_namespace_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorNamespaceRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorNamespaceResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyHybridMonitorNamespaceRequest
        @return: ModifyHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hybrid_monitor_namespace_with_options_async(request, runtime)

    def modify_hybrid_monitor_slsgroup_with_options(
        self,
        request: cms_20190101_models.ModifyHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: ModifyHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorSLSGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: ModifyHybridMonitorSLSGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_slsgroup(
        self,
        request: cms_20190101_models.ModifyHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: ModifyHybridMonitorSLSGroupRequest
        @return: ModifyHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def modify_hybrid_monitor_slsgroup_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorSLSGroupRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorSLSGroupResponse:
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        
        @param request: ModifyHybridMonitorSLSGroupRequest
        @return: ModifyHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def modify_hybrid_monitor_task_with_options(
        self,
        request: cms_20190101_models.ModifyHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorTaskResponse:
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        
        @param request: ModifyHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_task_with_options_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHybridMonitorTaskResponse:
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        
        @param request: ModifyHybridMonitorTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_task(
        self,
        request: cms_20190101_models.ModifyHybridMonitorTaskRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorTaskResponse:
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        
        @param request: ModifyHybridMonitorTaskRequest
        @return: ModifyHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_task_with_options(request, runtime)

    async def modify_hybrid_monitor_task_async(
        self,
        request: cms_20190101_models.ModifyHybridMonitorTaskRequest,
    ) -> cms_20190101_models.ModifyHybridMonitorTaskResponse:
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        
        @param request: ModifyHybridMonitorTaskRequest
        @return: ModifyHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hybrid_monitor_task_with_options_async(request, runtime)

    def modify_metric_rule_black_list_with_options(
        self,
        request: cms_20190101_models.ModifyMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_metric_rule_black_list_with_options_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_metric_rule_black_list(
        self,
        request: cms_20190101_models.ModifyMetricRuleBlackListRequest,
    ) -> cms_20190101_models.ModifyMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_metric_rule_black_list_with_options(request, runtime)

    async def modify_metric_rule_black_list_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleBlackListRequest,
    ) -> cms_20190101_models.ModifyMetricRuleBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_metric_rule_black_list_with_options_async(request, runtime)

    def modify_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyMetricRuleTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyMetricRuleTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_metric_rule_template(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyMetricRuleTemplateRequest
        @return: ModifyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_metric_rule_template_with_options(request, runtime)

    async def modify_metric_rule_template_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: ModifyMetricRuleTemplateRequest
        @return: ModifyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_metric_rule_template_with_options_async(request, runtime)

    def modify_monitor_group_with_options(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_monitor_group(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_monitor_group_with_options(request, runtime)

    async def modify_monitor_group_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_monitor_group_with_options_async(request, runtime)

    def modify_monitor_group_instances_with_options(
        self,
        request: cms_20190101_models.ModifyMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_monitor_group_instances(
        self,
        request: cms_20190101_models.ModifyMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.ModifyMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_monitor_group_instances_with_options(request, runtime)

    async def modify_monitor_group_instances_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.ModifyMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_monitor_group_instances_with_options_async(request, runtime)

    def modify_site_monitor_with_options(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        """
        The number of site monitoring tasks.
        
        @param request: ModifySiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifySiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        """
        The number of site monitoring tasks.
        
        @param request: ModifySiteMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifySiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_site_monitor(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        """
        The number of site monitoring tasks.
        
        @param request: ModifySiteMonitorRequest
        @return: ModifySiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_site_monitor_with_options(request, runtime)

    async def modify_site_monitor_async(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        """
        The number of site monitoring tasks.
        
        @param request: ModifySiteMonitorRequest
        @return: ModifySiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_site_monitor_with_options_async(request, runtime)

    def open_cms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.OpenCmsServiceResponse:
        """
        @deprecated
        
        @param request: OpenCmsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCmsServiceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCmsService',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.OpenCmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cms_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.OpenCmsServiceResponse:
        """
        @deprecated
        
        @param request: OpenCmsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCmsServiceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCmsService',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.OpenCmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cms_service(self) -> cms_20190101_models.OpenCmsServiceResponse:
        """
        @deprecated
        
        @return: OpenCmsServiceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.open_cms_service_with_options(runtime)

    async def open_cms_service_async(self) -> cms_20190101_models.OpenCmsServiceResponse:
        """
        @deprecated
        
        @return: OpenCmsServiceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_cms_service_with_options_async(runtime)

    def put_contact_with_options(
        self,
        request: cms_20190101_models.PutContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_contact_with_options_async(
        self,
        request: cms_20190101_models.PutContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_contact(
        self,
        request: cms_20190101_models.PutContactRequest,
    ) -> cms_20190101_models.PutContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_contact_with_options(request, runtime)

    async def put_contact_async(
        self,
        request: cms_20190101_models.PutContactRequest,
    ) -> cms_20190101_models.PutContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_contact_with_options_async(request, runtime)

    def put_contact_group_with_options(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactGroupResponse:
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        
        @param request: PutContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutContactGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_names):
            query['ContactNames'] = request.contact_names
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.enable_subscribed):
            query['EnableSubscribed'] = request.enable_subscribed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_contact_group_with_options_async(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactGroupResponse:
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        
        @param request: PutContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutContactGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_names):
            query['ContactNames'] = request.contact_names
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.enable_subscribed):
            query['EnableSubscribed'] = request.enable_subscribed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_contact_group(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
    ) -> cms_20190101_models.PutContactGroupResponse:
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        
        @param request: PutContactGroupRequest
        @return: PutContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_contact_group_with_options(request, runtime)

    async def put_contact_group_async(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
    ) -> cms_20190101_models.PutContactGroupResponse:
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        
        @param request: PutContactGroupRequest
        @return: PutContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_contact_group_with_options_async(request, runtime)

    def put_custom_event_with_options(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_event_with_options_async(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_event(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
    ) -> cms_20190101_models.PutCustomEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_custom_event_with_options(request, runtime)

    async def put_custom_event_async(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
    ) -> cms_20190101_models.PutCustomEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_event_with_options_async(request, runtime)

    def put_custom_event_rule_with_options(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        
        @param request: PutCustomEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_event_rule_with_options_async(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        
        @param request: PutCustomEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_event_rule(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        
        @param request: PutCustomEventRuleRequest
        @return: PutCustomEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_event_rule_with_options(request, runtime)

    async def put_custom_event_rule_async(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        
        @param request: PutCustomEventRuleRequest
        @return: PutCustomEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_event_rule_with_options_async(request, runtime)

    def put_custom_metric_with_options(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        
        @param request: PutCustomMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_metric_with_options_async(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        
        @param request: PutCustomMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_metric(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        
        @param request: PutCustomMetricRequest
        @return: PutCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_with_options(request, runtime)

    async def put_custom_metric_async(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        
        @param request: PutCustomMetricRequest
        @return: PutCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_metric_with_options_async(request, runtime)

    def put_custom_metric_rule_with_options(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        
        @param request: PutCustomMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        
        @param request: PutCustomMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutCustomMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_metric_rule(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        
        @param request: PutCustomMetricRuleRequest
        @return: PutCustomMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_rule_with_options(request, runtime)

    async def put_custom_metric_rule_async(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        
        @param request: PutCustomMetricRuleRequest
        @return: PutCustomMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_metric_rule_with_options_async(request, runtime)

    def put_event_rule_with_options(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleResponse:
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        
        @param request: PutEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_pattern):
            query['EventPattern'] = request.event_pattern
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_rule_with_options_async(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleResponse:
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        
        @param request: PutEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_pattern):
            query['EventPattern'] = request.event_pattern
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_rule(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
    ) -> cms_20190101_models.PutEventRuleResponse:
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        
        @param request: PutEventRuleRequest
        @return: PutEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_with_options(request, runtime)

    async def put_event_rule_async(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
    ) -> cms_20190101_models.PutEventRuleResponse:
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        
        @param request: PutEventRuleRequest
        @return: PutEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_event_rule_with_options_async(request, runtime)

    def put_event_rule_targets_with_options(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not UtilClient.is_unset(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not UtilClient.is_unset(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
        if not UtilClient.is_unset(request.open_api_parameters):
            query['OpenApiParameters'] = request.open_api_parameters
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sls_parameters):
            query['SlsParameters'] = request.sls_parameters
        if not UtilClient.is_unset(request.webhook_parameters):
            query['WebhookParameters'] = request.webhook_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not UtilClient.is_unset(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not UtilClient.is_unset(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
        if not UtilClient.is_unset(request.open_api_parameters):
            query['OpenApiParameters'] = request.open_api_parameters
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sls_parameters):
            query['SlsParameters'] = request.sls_parameters
        if not UtilClient.is_unset(request.webhook_parameters):
            query['WebhookParameters'] = request.webhook_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_rule_targets(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_targets_with_options(request, runtime)

    async def put_event_rule_targets_async(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_event_rule_targets_with_options_async(request, runtime)

    def put_exporter_output_with_options(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        
        @param request: PutExporterOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutExporterOutputResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_json):
            query['ConfigJson'] = request.config_json
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        if not UtilClient.is_unset(request.dest_type):
            query['DestType'] = request.dest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_exporter_output_with_options_async(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        
        @param request: PutExporterOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutExporterOutputResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_json):
            query['ConfigJson'] = request.config_json
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        if not UtilClient.is_unset(request.dest_type):
            query['DestType'] = request.dest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_exporter_output(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        
        @param request: PutExporterOutputRequest
        @return: PutExporterOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_exporter_output_with_options(request, runtime)

    async def put_exporter_output_async(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        
        @param request: PutExporterOutputRequest
        @return: PutExporterOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_exporter_output_with_options_async(request, runtime)

    def put_exporter_rule_with_options(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.dst_names):
            query['DstNames'] = request.dst_names
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.target_windows):
            query['TargetWindows'] = request.target_windows
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_exporter_rule_with_options_async(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.dst_names):
            query['DstNames'] = request.dst_names
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.target_windows):
            query['TargetWindows'] = request.target_windows
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_exporter_rule(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_exporter_rule_with_options(request, runtime)

    async def put_exporter_rule_async(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_exporter_rule_with_options_async(request, runtime)

    def put_group_metric_rule_with_options(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutGroupMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutGroupMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.extra_dimension_json):
            query['ExtraDimensionJson'] = request.extra_dimension_json
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutGroupMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_group_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutGroupMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutGroupMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.extra_dimension_json):
            query['ExtraDimensionJson'] = request.extra_dimension_json
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutGroupMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_group_metric_rule(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutGroupMetricRuleRequest
        @return: PutGroupMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_group_metric_rule_with_options(request, runtime)

    async def put_group_metric_rule_async(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutGroupMetricRuleRequest
        @return: PutGroupMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_group_metric_rule_with_options_async(request, runtime)

    def put_hybrid_monitor_metric_data_with_options(
        self,
        request: cms_20190101_models.PutHybridMonitorMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutHybridMonitorMetricDataResponse:
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        
        @param request: PutHybridMonitorMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutHybridMonitorMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutHybridMonitorMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutHybridMonitorMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_hybrid_monitor_metric_data_with_options_async(
        self,
        request: cms_20190101_models.PutHybridMonitorMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutHybridMonitorMetricDataResponse:
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        
        @param request: PutHybridMonitorMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutHybridMonitorMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutHybridMonitorMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutHybridMonitorMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_hybrid_monitor_metric_data(
        self,
        request: cms_20190101_models.PutHybridMonitorMetricDataRequest,
    ) -> cms_20190101_models.PutHybridMonitorMetricDataResponse:
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        
        @param request: PutHybridMonitorMetricDataRequest
        @return: PutHybridMonitorMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_hybrid_monitor_metric_data_with_options(request, runtime)

    async def put_hybrid_monitor_metric_data_async(
        self,
        request: cms_20190101_models.PutHybridMonitorMetricDataRequest,
    ) -> cms_20190101_models.PutHybridMonitorMetricDataResponse:
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        
        @param request: PutHybridMonitorMetricDataRequest
        @return: PutHybridMonitorMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_hybrid_monitor_metric_data_with_options_async(request, runtime)

    def put_log_monitor_with_options(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        
        @param request: PutLogMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLogMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregates):
            query['Aggregates'] = request.aggregates
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.groupbys):
            query['Groupbys'] = request.groupbys
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        if not UtilClient.is_unset(request.metric_express):
            query['MetricExpress'] = request.metric_express
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        if not UtilClient.is_unset(request.tumblingwindows):
            query['Tumblingwindows'] = request.tumblingwindows
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        if not UtilClient.is_unset(request.value_filter_relation):
            query['ValueFilterRelation'] = request.value_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_log_monitor_with_options_async(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        
        @param request: PutLogMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLogMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregates):
            query['Aggregates'] = request.aggregates
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.groupbys):
            query['Groupbys'] = request.groupbys
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        if not UtilClient.is_unset(request.metric_express):
            query['MetricExpress'] = request.metric_express
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        if not UtilClient.is_unset(request.tumblingwindows):
            query['Tumblingwindows'] = request.tumblingwindows
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        if not UtilClient.is_unset(request.value_filter_relation):
            query['ValueFilterRelation'] = request.value_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutLogMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_log_monitor(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        
        @param request: PutLogMonitorRequest
        @return: PutLogMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_log_monitor_with_options(request, runtime)

    async def put_log_monitor_async(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        
        @param request: PutLogMonitorRequest
        @return: PutLogMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_log_monitor_with_options_async(request, runtime)

    def put_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_metric_rule_targets(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutMetricRuleTargetsRequest
        @return: PutMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_metric_rule_targets_with_options(request, runtime)

    async def put_metric_rule_targets_async(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutMetricRuleTargetsRequest
        @return: PutMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_metric_rule_targets_with_options_async(request, runtime)

    def put_monitor_group_dynamic_rule_with_options(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_rules):
            query['GroupRules'] = request.group_rules
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_monitor_group_dynamic_rule_with_options_async(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_rules):
            query['GroupRules'] = request.group_rules
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitorGroupDynamicRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_monitor_group_dynamic_rule(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_monitor_group_dynamic_rule_with_options(request, runtime)

    async def put_monitor_group_dynamic_rule_async(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_monitor_group_dynamic_rule_with_options_async(request, runtime)

    def put_monitoring_config_with_options(
        self,
        request: cms_20190101_models.PutMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitoringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.enable_install_agent_new_ecs):
            query['EnableInstallAgentNewECS'] = request.enable_install_agent_new_ecs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_monitoring_config_with_options_async(
        self,
        request: cms_20190101_models.PutMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitoringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.enable_install_agent_new_ecs):
            query['EnableInstallAgentNewECS'] = request.enable_install_agent_new_ecs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitoringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_monitoring_config(
        self,
        request: cms_20190101_models.PutMonitoringConfigRequest,
    ) -> cms_20190101_models.PutMonitoringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_monitoring_config_with_options(request, runtime)

    async def put_monitoring_config_async(
        self,
        request: cms_20190101_models.PutMonitoringConfigRequest,
    ) -> cms_20190101_models.PutMonitoringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_monitoring_config_with_options_async(request, runtime)

    def put_resource_metric_rule_with_options(
        self,
        tmp_req: cms_20190101_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        
        @param tmp_req: PutResourceMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.PutResourceMetricRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.composite_expression):
            request.composite_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.composite_expression, 'CompositeExpression', 'json')
        if not UtilClient.is_unset(tmp_req.prometheus):
            request.prometheus_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prometheus, 'Prometheus', 'json')
        query = {}
        if not UtilClient.is_unset(request.composite_expression_shrink):
            query['CompositeExpression'] = request.composite_expression_shrink
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prometheus_shrink):
            query['Prometheus'] = request.prometheus_shrink
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_metric_rule_with_options_async(
        self,
        tmp_req: cms_20190101_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        
        @param tmp_req: PutResourceMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.PutResourceMetricRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.composite_expression):
            request.composite_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.composite_expression, 'CompositeExpression', 'json')
        if not UtilClient.is_unset(tmp_req.prometheus):
            request.prometheus_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prometheus, 'Prometheus', 'json')
        query = {}
        if not UtilClient.is_unset(request.composite_expression_shrink):
            query['CompositeExpression'] = request.composite_expression_shrink
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prometheus_shrink):
            query['Prometheus'] = request.prometheus_shrink
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_metric_rule(
        self,
        request: cms_20190101_models.PutResourceMetricRuleRequest,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        
        @param request: PutResourceMetricRuleRequest
        @return: PutResourceMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rule_with_options(request, runtime)

    async def put_resource_metric_rule_async(
        self,
        request: cms_20190101_models.PutResourceMetricRuleRequest,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        
        @param request: PutResourceMetricRuleRequest
        @return: PutResourceMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_metric_rule_with_options_async(request, runtime)

    def put_resource_metric_rules_with_options(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutResourceMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutResourceMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_metric_rules(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutResourceMetricRulesRequest
        @return: PutResourceMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rules_with_options(request, runtime)

    async def put_resource_metric_rules_async(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        
        @param request: PutResourceMetricRulesRequest
        @return: PutResourceMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_metric_rules_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.RemoveTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tags(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
    ) -> cms_20190101_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
    ) -> cms_20190101_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def send_dry_run_system_event_with_options(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        
        @param request: SendDryRunSystemEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDryRunSystemEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_content):
            query['EventContent'] = request.event_content
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDryRunSystemEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.SendDryRunSystemEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_dry_run_system_event_with_options_async(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        
        @param request: SendDryRunSystemEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDryRunSystemEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_content):
            query['EventContent'] = request.event_content
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDryRunSystemEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.SendDryRunSystemEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_dry_run_system_event(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        
        @param request: SendDryRunSystemEventRequest
        @return: SendDryRunSystemEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_dry_run_system_event_with_options(request, runtime)

    async def send_dry_run_system_event_async(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        
        @param request: SendDryRunSystemEventRequest
        @return: SendDryRunSystemEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_dry_run_system_event_with_options_async(request, runtime)

    def uninstall_monitoring_agent_with_options(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        
        @param request: UninstallMonitoringAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.UninstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_monitoring_agent_with_options_async(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        
        @param request: UninstallMonitoringAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.UninstallMonitoringAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_monitoring_agent(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        
        @param request: UninstallMonitoringAgentRequest
        @return: UninstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_monitoring_agent_with_options(request, runtime)

    async def uninstall_monitoring_agent_async(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        
        @param request: UninstallMonitoringAgentRequest
        @return: UninstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_monitoring_agent_with_options_async(request, runtime)
