# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms20180308 import models as cms_20180308_models
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

    def access_key_get_with_options(
        self,
        request: cms_20180308_models.AccessKeyGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.AccessKeyGetResponse:
        """
        @summary AccessKeyGet
        
        @param request: AccessKeyGetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AccessKeyGetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessKeyGet',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.AccessKeyGetResponse(),
            self.call_api(params, req, runtime)
        )

    async def access_key_get_with_options_async(
        self,
        request: cms_20180308_models.AccessKeyGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.AccessKeyGetResponse:
        """
        @summary AccessKeyGet
        
        @param request: AccessKeyGetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AccessKeyGetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccessKeyGet',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.AccessKeyGetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def access_key_get(
        self,
        request: cms_20180308_models.AccessKeyGetRequest,
    ) -> cms_20180308_models.AccessKeyGetResponse:
        """
        @summary AccessKeyGet
        
        @param request: AccessKeyGetRequest
        @return: AccessKeyGetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.access_key_get_with_options(request, runtime)

    async def access_key_get_async(
        self,
        request: cms_20180308_models.AccessKeyGetRequest,
    ) -> cms_20180308_models.AccessKeyGetResponse:
        """
        @summary AccessKeyGet
        
        @param request: AccessKeyGetRequest
        @return: AccessKeyGetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.access_key_get_with_options_async(request, runtime)

    def add_my_group_instances_with_options(
        self,
        request: cms_20180308_models.AddMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.AddMyGroupInstancesResponse:
        """
        @param request: AddMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMyGroupInstancesResponse
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
            action='AddMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.AddMyGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_my_group_instances_with_options_async(
        self,
        request: cms_20180308_models.AddMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.AddMyGroupInstancesResponse:
        """
        @param request: AddMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMyGroupInstancesResponse
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
            action='AddMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.AddMyGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_my_group_instances(
        self,
        request: cms_20180308_models.AddMyGroupInstancesRequest,
    ) -> cms_20180308_models.AddMyGroupInstancesResponse:
        """
        @param request: AddMyGroupInstancesRequest
        @return: AddMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_my_group_instances_with_options(request, runtime)

    async def add_my_group_instances_async(
        self,
        request: cms_20180308_models.AddMyGroupInstancesRequest,
    ) -> cms_20180308_models.AddMyGroupInstancesResponse:
        """
        @param request: AddMyGroupInstancesRequest
        @return: AddMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_my_group_instances_with_options_async(request, runtime)

    def create_alarm_with_options(
        self,
        request: cms_20180308_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateAlarmResponse:
        """
        @summary CreateAlarm
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='CreateAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        request: cms_20180308_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateAlarmResponse:
        """
        @summary CreateAlarm
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='CreateAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: cms_20180308_models.CreateAlarmRequest,
    ) -> cms_20180308_models.CreateAlarmResponse:
        """
        @summary CreateAlarm
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    async def create_alarm_async(
        self,
        request: cms_20180308_models.CreateAlarmRequest,
    ) -> cms_20180308_models.CreateAlarmResponse:
        """
        @summary CreateAlarm
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_with_options_async(request, runtime)

    def create_hybrid_double_write_with_options(
        self,
        request: cms_20180308_models.CreateHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateHybridDoubleWriteResponse:
        """
        @summary 创建双写配置
        
        @param request: CreateHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateHybridDoubleWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_double_write_with_options_async(
        self,
        request: cms_20180308_models.CreateHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateHybridDoubleWriteResponse:
        """
        @summary 创建双写配置
        
        @param request: CreateHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateHybridDoubleWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_double_write(
        self,
        request: cms_20180308_models.CreateHybridDoubleWriteRequest,
    ) -> cms_20180308_models.CreateHybridDoubleWriteResponse:
        """
        @summary 创建双写配置
        
        @param request: CreateHybridDoubleWriteRequest
        @return: CreateHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_double_write_with_options(request, runtime)

    async def create_hybrid_double_write_async(
        self,
        request: cms_20180308_models.CreateHybridDoubleWriteRequest,
    ) -> cms_20180308_models.CreateHybridDoubleWriteResponse:
        """
        @summary 创建双写配置
        
        @param request: CreateHybridDoubleWriteRequest
        @return: CreateHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_double_write_with_options_async(request, runtime)

    def create_monitoring_template_with_options(
        self,
        request: cms_20180308_models.CreateMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateMonitoringTemplateResponse:
        """
        @param request: CreateMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates_json):
            query['AlertTemplatesJson'] = request.alert_templates_json
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host_availability_template):
            query['HostAvailabilityTemplate'] = request.host_availability_template
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.process_monitor_templates):
            query['ProcessMonitorTemplates'] = request.process_monitor_templates
        if not UtilClient.is_unset(request.system_event_templates):
            query['SystemEventTemplates'] = request.system_event_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateMonitoringTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitoring_template_with_options_async(
        self,
        request: cms_20180308_models.CreateMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateMonitoringTemplateResponse:
        """
        @param request: CreateMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates_json):
            query['AlertTemplatesJson'] = request.alert_templates_json
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host_availability_template):
            query['HostAvailabilityTemplate'] = request.host_availability_template
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.process_monitor_templates):
            query['ProcessMonitorTemplates'] = request.process_monitor_templates
        if not UtilClient.is_unset(request.system_event_templates):
            query['SystemEventTemplates'] = request.system_event_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateMonitoringTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitoring_template(
        self,
        request: cms_20180308_models.CreateMonitoringTemplateRequest,
    ) -> cms_20180308_models.CreateMonitoringTemplateResponse:
        """
        @param request: CreateMonitoringTemplateRequest
        @return: CreateMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitoring_template_with_options(request, runtime)

    async def create_monitoring_template_async(
        self,
        request: cms_20180308_models.CreateMonitoringTemplateRequest,
    ) -> cms_20180308_models.CreateMonitoringTemplateResponse:
        """
        @param request: CreateMonitoringTemplateRequest
        @return: CreateMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitoring_template_with_options_async(request, runtime)

    def create_my_groups_with_options(
        self,
        request: cms_20180308_models.CreateMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateMyGroupsResponse:
        """
        @param request: CreateMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_url):
            query['BindUrl'] = request.bind_url
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateMyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_my_groups_with_options_async(
        self,
        request: cms_20180308_models.CreateMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateMyGroupsResponse:
        """
        @param request: CreateMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_url):
            query['BindUrl'] = request.bind_url
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateMyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_my_groups(
        self,
        request: cms_20180308_models.CreateMyGroupsRequest,
    ) -> cms_20180308_models.CreateMyGroupsResponse:
        """
        @param request: CreateMyGroupsRequest
        @return: CreateMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_my_groups_with_options(request, runtime)

    async def create_my_groups_async(
        self,
        request: cms_20180308_models.CreateMyGroupsRequest,
    ) -> cms_20180308_models.CreateMyGroupsResponse:
        """
        @param request: CreateMyGroupsRequest
        @return: CreateMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_my_groups_with_options_async(request, runtime)

    def create_task_with_options(
        self,
        request: cms_20180308_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateTaskResponse:
        """
        @summary CreateTask
        
        @param request: CreateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_rule):
            query['AlertRule'] = request.alert_rule
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_city):
            query['IspCity'] = request.isp_city
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.caller):
            query['caller'] = request.caller
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: cms_20180308_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.CreateTaskResponse:
        """
        @summary CreateTask
        
        @param request: CreateTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_rule):
            query['AlertRule'] = request.alert_rule
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_city):
            query['IspCity'] = request.isp_city
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.caller):
            query['caller'] = request.caller
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: cms_20180308_models.CreateTaskRequest,
    ) -> cms_20180308_models.CreateTaskResponse:
        """
        @summary CreateTask
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    async def create_task_async(
        self,
        request: cms_20180308_models.CreateTaskRequest,
    ) -> cms_20180308_models.CreateTaskResponse:
        """
        @summary CreateTask
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_with_options_async(request, runtime)

    def delete_alarm_with_options(
        self,
        request: cms_20180308_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteAlarmResponse:
        """
        @summary DeleteAlarm
        
        @param request: DeleteAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarm_with_options_async(
        self,
        request: cms_20180308_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteAlarmResponse:
        """
        @summary DeleteAlarm
        
        @param request: DeleteAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarm(
        self,
        request: cms_20180308_models.DeleteAlarmRequest,
    ) -> cms_20180308_models.DeleteAlarmResponse:
        """
        @summary DeleteAlarm
        
        @param request: DeleteAlarmRequest
        @return: DeleteAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    async def delete_alarm_async(
        self,
        request: cms_20180308_models.DeleteAlarmRequest,
    ) -> cms_20180308_models.DeleteAlarmResponse:
        """
        @summary DeleteAlarm
        
        @param request: DeleteAlarmRequest
        @return: DeleteAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_with_options_async(request, runtime)

    def delete_custom_metric_with_options(
        self,
        request: cms_20180308_models.DeleteCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteCustomMetricResponse:
        """
        @summary DeleteCustomMetric
        
        @param request: DeleteCustomMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomMetricResponse
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_metric_with_options_async(
        self,
        request: cms_20180308_models.DeleteCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteCustomMetricResponse:
        """
        @summary DeleteCustomMetric
        
        @param request: DeleteCustomMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomMetricResponse
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_metric(
        self,
        request: cms_20180308_models.DeleteCustomMetricRequest,
    ) -> cms_20180308_models.DeleteCustomMetricResponse:
        """
        @summary DeleteCustomMetric
        
        @param request: DeleteCustomMetricRequest
        @return: DeleteCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_metric_with_options(request, runtime)

    async def delete_custom_metric_async(
        self,
        request: cms_20180308_models.DeleteCustomMetricRequest,
    ) -> cms_20180308_models.DeleteCustomMetricResponse:
        """
        @summary DeleteCustomMetric
        
        @param request: DeleteCustomMetricRequest
        @return: DeleteCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_metric_with_options_async(request, runtime)

    def delete_hybrid_double_write_with_options(
        self,
        request: cms_20180308_models.DeleteHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteHybridDoubleWriteResponse:
        """
        @summary 删除双写配置
        
        @param request: DeleteHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteHybridDoubleWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_double_write_with_options_async(
        self,
        request: cms_20180308_models.DeleteHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteHybridDoubleWriteResponse:
        """
        @summary 删除双写配置
        
        @param request: DeleteHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteHybridDoubleWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_double_write(
        self,
        request: cms_20180308_models.DeleteHybridDoubleWriteRequest,
    ) -> cms_20180308_models.DeleteHybridDoubleWriteResponse:
        """
        @summary 删除双写配置
        
        @param request: DeleteHybridDoubleWriteRequest
        @return: DeleteHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_double_write_with_options(request, runtime)

    async def delete_hybrid_double_write_async(
        self,
        request: cms_20180308_models.DeleteHybridDoubleWriteRequest,
    ) -> cms_20180308_models.DeleteHybridDoubleWriteResponse:
        """
        @summary 删除双写配置
        
        @param request: DeleteHybridDoubleWriteRequest
        @return: DeleteHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hybrid_double_write_with_options_async(request, runtime)

    def delete_metric_rule_targets_with_options(
        self,
        request: cms_20180308_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMetricRuleTargetsResponse:
        """
        @summary DeleteMetricRuleTargets
        
        @param request: DeleteMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricRuleTargetsResponse
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_targets_with_options_async(
        self,
        request: cms_20180308_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMetricRuleTargetsResponse:
        """
        @summary DeleteMetricRuleTargets
        
        @param request: DeleteMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricRuleTargetsResponse
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_targets(
        self,
        request: cms_20180308_models.DeleteMetricRuleTargetsRequest,
    ) -> cms_20180308_models.DeleteMetricRuleTargetsResponse:
        """
        @summary DeleteMetricRuleTargets
        
        @param request: DeleteMetricRuleTargetsRequest
        @return: DeleteMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_targets_with_options(request, runtime)

    async def delete_metric_rule_targets_async(
        self,
        request: cms_20180308_models.DeleteMetricRuleTargetsRequest,
    ) -> cms_20180308_models.DeleteMetricRuleTargetsResponse:
        """
        @summary DeleteMetricRuleTargets
        
        @param request: DeleteMetricRuleTargetsRequest
        @return: DeleteMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rule_targets_with_options_async(request, runtime)

    def delete_metric_rules_with_options(
        self,
        request: cms_20180308_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMetricRulesResponse:
        """
        @summary DeleteMetricRules
        
        @param request: DeleteMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRules',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rules_with_options_async(
        self,
        request: cms_20180308_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMetricRulesResponse:
        """
        @summary DeleteMetricRules
        
        @param request: DeleteMetricRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRules',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rules(
        self,
        request: cms_20180308_models.DeleteMetricRulesRequest,
    ) -> cms_20180308_models.DeleteMetricRulesResponse:
        """
        @summary DeleteMetricRules
        
        @param request: DeleteMetricRulesRequest
        @return: DeleteMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rules_with_options(request, runtime)

    async def delete_metric_rules_async(
        self,
        request: cms_20180308_models.DeleteMetricRulesRequest,
    ) -> cms_20180308_models.DeleteMetricRulesResponse:
        """
        @summary DeleteMetricRules
        
        @param request: DeleteMetricRulesRequest
        @return: DeleteMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_metric_rules_with_options_async(request, runtime)

    def delete_my_group_instances_with_options(
        self,
        request: cms_20180308_models.DeleteMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMyGroupInstancesResponse:
        """
        @summary deletemygroupinstances
        
        @param request: DeleteMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMyGroupInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMyGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_my_group_instances_with_options_async(
        self,
        request: cms_20180308_models.DeleteMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMyGroupInstancesResponse:
        """
        @summary deletemygroupinstances
        
        @param request: DeleteMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMyGroupInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMyGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_my_group_instances(
        self,
        request: cms_20180308_models.DeleteMyGroupInstancesRequest,
    ) -> cms_20180308_models.DeleteMyGroupInstancesResponse:
        """
        @summary deletemygroupinstances
        
        @param request: DeleteMyGroupInstancesRequest
        @return: DeleteMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_my_group_instances_with_options(request, runtime)

    async def delete_my_group_instances_async(
        self,
        request: cms_20180308_models.DeleteMyGroupInstancesRequest,
    ) -> cms_20180308_models.DeleteMyGroupInstancesResponse:
        """
        @summary deletemygroupinstances
        
        @param request: DeleteMyGroupInstancesRequest
        @return: DeleteMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_my_group_instances_with_options_async(request, runtime)

    def delete_my_groups_with_options(
        self,
        request: cms_20180308_models.DeleteMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMyGroupsResponse:
        """
        @param request: DeleteMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_my_groups_with_options_async(
        self,
        request: cms_20180308_models.DeleteMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteMyGroupsResponse:
        """
        @param request: DeleteMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteMyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_my_groups(
        self,
        request: cms_20180308_models.DeleteMyGroupsRequest,
    ) -> cms_20180308_models.DeleteMyGroupsResponse:
        """
        @param request: DeleteMyGroupsRequest
        @return: DeleteMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_my_groups_with_options(request, runtime)

    async def delete_my_groups_async(
        self,
        request: cms_20180308_models.DeleteMyGroupsRequest,
    ) -> cms_20180308_models.DeleteMyGroupsResponse:
        """
        @param request: DeleteMyGroupsRequest
        @return: DeleteMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_my_groups_with_options_async(request, runtime)

    def delete_tasks_with_options(
        self,
        request: cms_20180308_models.DeleteTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteTasksResponse:
        """
        @param request: DeleteTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTasksResponse
        """
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
            action='DeleteTasks',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tasks_with_options_async(
        self,
        request: cms_20180308_models.DeleteTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DeleteTasksResponse:
        """
        @param request: DeleteTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTasksResponse
        """
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
            action='DeleteTasks',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DeleteTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tasks(
        self,
        request: cms_20180308_models.DeleteTasksRequest,
    ) -> cms_20180308_models.DeleteTasksResponse:
        """
        @param request: DeleteTasksRequest
        @return: DeleteTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tasks_with_options(request, runtime)

    async def delete_tasks_async(
        self,
        request: cms_20180308_models.DeleteTasksRequest,
    ) -> cms_20180308_models.DeleteTasksResponse:
        """
        @param request: DeleteTasksRequest
        @return: DeleteTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tasks_with_options_async(request, runtime)

    def describe_alarm_history_with_options(
        self,
        request: cms_20180308_models.DescribeAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmHistoryResponse:
        """
        @summary DescribeAlarmHistory
        
        @param request: DescribeAlarmHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
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
        if not UtilClient.is_unset(request.only_count):
            query['OnlyCount'] = request.only_count
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeAlarmHistory',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_history_with_options_async(
        self,
        request: cms_20180308_models.DescribeAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmHistoryResponse:
        """
        @summary DescribeAlarmHistory
        
        @param request: DescribeAlarmHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
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
        if not UtilClient.is_unset(request.only_count):
            query['OnlyCount'] = request.only_count
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeAlarmHistory',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_history(
        self,
        request: cms_20180308_models.DescribeAlarmHistoryRequest,
    ) -> cms_20180308_models.DescribeAlarmHistoryResponse:
        """
        @summary DescribeAlarmHistory
        
        @param request: DescribeAlarmHistoryRequest
        @return: DescribeAlarmHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_history_with_options(request, runtime)

    async def describe_alarm_history_async(
        self,
        request: cms_20180308_models.DescribeAlarmHistoryRequest,
    ) -> cms_20180308_models.DescribeAlarmHistoryResponse:
        """
        @summary DescribeAlarmHistory
        
        @param request: DescribeAlarmHistoryRequest
        @return: DescribeAlarmHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarm_history_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: cms_20180308_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmsResponse:
        """
        @summary DescribeAlarms
        
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_state):
            query['AlertState'] = request.alert_state
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.enable_state):
            query['EnableState'] = request.enable_state
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.name_keyword):
            query['NameKeyword'] = request.name_keyword
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: cms_20180308_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmsResponse:
        """
        @summary DescribeAlarms
        
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_state):
            query['AlertState'] = request.alert_state
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.enable_state):
            query['EnableState'] = request.enable_state
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.name_keyword):
            query['NameKeyword'] = request.name_keyword
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: cms_20180308_models.DescribeAlarmsRequest,
    ) -> cms_20180308_models.DescribeAlarmsResponse:
        """
        @summary DescribeAlarms
        
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: cms_20180308_models.DescribeAlarmsRequest,
    ) -> cms_20180308_models.DescribeAlarmsResponse:
        """
        @summary DescribeAlarms
        
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_alarms_for_resources_with_options(
        self,
        request: cms_20180308_models.DescribeAlarmsForResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmsForResourcesResponse:
        """
        @summary describealarmsforresources
        
        @param request: DescribeAlarmsForResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsForResourcesResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmsForResources',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmsForResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_for_resources_with_options_async(
        self,
        request: cms_20180308_models.DescribeAlarmsForResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlarmsForResourcesResponse:
        """
        @summary describealarmsforresources
        
        @param request: DescribeAlarmsForResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsForResourcesResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmsForResources',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlarmsForResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms_for_resources(
        self,
        request: cms_20180308_models.DescribeAlarmsForResourcesRequest,
    ) -> cms_20180308_models.DescribeAlarmsForResourcesResponse:
        """
        @summary describealarmsforresources
        
        @param request: DescribeAlarmsForResourcesRequest
        @return: DescribeAlarmsForResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_for_resources_with_options(request, runtime)

    async def describe_alarms_for_resources_async(
        self,
        request: cms_20180308_models.DescribeAlarmsForResourcesRequest,
    ) -> cms_20180308_models.DescribeAlarmsForResourcesResponse:
        """
        @summary describealarmsforresources
        
        @param request: DescribeAlarmsForResourcesRequest
        @return: DescribeAlarmsForResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_for_resources_with_options_async(request, runtime)

    def describe_alert_history_list_with_options(
        self,
        request: cms_20180308_models.DescribeAlertHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlertHistoryListResponse:
        """
        @param request: DescribeAlertHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertHistoryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
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
        if not UtilClient.is_unset(request.only_count):
            query['OnlyCount'] = request.only_count
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlertHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_history_list_with_options_async(
        self,
        request: cms_20180308_models.DescribeAlertHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeAlertHistoryListResponse:
        """
        @param request: DescribeAlertHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertHistoryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
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
        if not UtilClient.is_unset(request.only_count):
            query['OnlyCount'] = request.only_count
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeAlertHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_history_list(
        self,
        request: cms_20180308_models.DescribeAlertHistoryListRequest,
    ) -> cms_20180308_models.DescribeAlertHistoryListResponse:
        """
        @param request: DescribeAlertHistoryListRequest
        @return: DescribeAlertHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_history_list_with_options(request, runtime)

    async def describe_alert_history_list_async(
        self,
        request: cms_20180308_models.DescribeAlertHistoryListRequest,
    ) -> cms_20180308_models.DescribeAlertHistoryListResponse:
        """
        @param request: DescribeAlertHistoryListRequest
        @return: DescribeAlertHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_history_list_with_options_async(request, runtime)

    def describe_contact_with_options(
        self,
        request: cms_20180308_models.DescribeContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeContactResponse:
        """
        @param request: DescribeContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContact',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_with_options_async(
        self,
        request: cms_20180308_models.DescribeContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeContactResponse:
        """
        @param request: DescribeContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContact',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact(
        self,
        request: cms_20180308_models.DescribeContactRequest,
    ) -> cms_20180308_models.DescribeContactResponse:
        """
        @param request: DescribeContactRequest
        @return: DescribeContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_with_options(request, runtime)

    async def describe_contact_async(
        self,
        request: cms_20180308_models.DescribeContactRequest,
    ) -> cms_20180308_models.DescribeContactResponse:
        """
        @param request: DescribeContactRequest
        @return: DescribeContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_with_options_async(request, runtime)

    def describe_hybrid_double_write_with_options(
        self,
        request: cms_20180308_models.DescribeHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeHybridDoubleWriteResponse:
        """
        @summary 查询本数据源被双写到哪里
        
        @param request: DescribeHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeHybridDoubleWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_double_write_with_options_async(
        self,
        request: cms_20180308_models.DescribeHybridDoubleWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeHybridDoubleWriteResponse:
        """
        @summary 查询本数据源被双写到哪里
        
        @param request: DescribeHybridDoubleWriteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHybridDoubleWriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_namespace):
            query['SourceNamespace'] = request.source_namespace
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridDoubleWrite',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeHybridDoubleWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_double_write(
        self,
        request: cms_20180308_models.DescribeHybridDoubleWriteRequest,
    ) -> cms_20180308_models.DescribeHybridDoubleWriteResponse:
        """
        @summary 查询本数据源被双写到哪里
        
        @param request: DescribeHybridDoubleWriteRequest
        @return: DescribeHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_double_write_with_options(request, runtime)

    async def describe_hybrid_double_write_async(
        self,
        request: cms_20180308_models.DescribeHybridDoubleWriteRequest,
    ) -> cms_20180308_models.DescribeHybridDoubleWriteResponse:
        """
        @summary 查询本数据源被双写到哪里
        
        @param request: DescribeHybridDoubleWriteRequest
        @return: DescribeHybridDoubleWriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_double_write_with_options_async(request, runtime)

    def describe_isparea_city_with_options(
        self,
        request: cms_20180308_models.DescribeISPAreaCityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeISPAreaCityResponse:
        """
        @summary 获取探针列表
        
        @param request: DescribeISPAreaCityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeISPAreaCityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeISPAreaCity',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeISPAreaCityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isparea_city_with_options_async(
        self,
        request: cms_20180308_models.DescribeISPAreaCityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeISPAreaCityResponse:
        """
        @summary 获取探针列表
        
        @param request: DescribeISPAreaCityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeISPAreaCityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeISPAreaCity',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeISPAreaCityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isparea_city(
        self,
        request: cms_20180308_models.DescribeISPAreaCityRequest,
    ) -> cms_20180308_models.DescribeISPAreaCityResponse:
        """
        @summary 获取探针列表
        
        @param request: DescribeISPAreaCityRequest
        @return: DescribeISPAreaCityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_isparea_city_with_options(request, runtime)

    async def describe_isparea_city_async(
        self,
        request: cms_20180308_models.DescribeISPAreaCityRequest,
    ) -> cms_20180308_models.DescribeISPAreaCityResponse:
        """
        @summary 获取探针列表
        
        @param request: DescribeISPAreaCityRequest
        @return: DescribeISPAreaCityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_isparea_city_with_options_async(request, runtime)

    def describe_metric_rule_list_with_options(
        self,
        request: cms_20180308_models.DescribeMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeMetricRuleListResponse:
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_list_with_options_async(
        self,
        request: cms_20180308_models.DescribeMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeMetricRuleListResponse:
        """
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeMetricRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_list(
        self,
        request: cms_20180308_models.DescribeMetricRuleListRequest,
    ) -> cms_20180308_models.DescribeMetricRuleListResponse:
        """
        @param request: DescribeMetricRuleListRequest
        @return: DescribeMetricRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_list_with_options(request, runtime)

    async def describe_metric_rule_list_async(
        self,
        request: cms_20180308_models.DescribeMetricRuleListRequest,
    ) -> cms_20180308_models.DescribeMetricRuleListResponse:
        """
        @param request: DescribeMetricRuleListRequest
        @return: DescribeMetricRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_list_with_options_async(request, runtime)

    def describe_task_detail_with_options(
        self,
        request: cms_20180308_models.DescribeTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeTaskDetailResponse:
        """
        @param request: DescribeTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskDetail',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_detail_with_options_async(
        self,
        request: cms_20180308_models.DescribeTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeTaskDetailResponse:
        """
        @param request: DescribeTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskDetail',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_detail(
        self,
        request: cms_20180308_models.DescribeTaskDetailRequest,
    ) -> cms_20180308_models.DescribeTaskDetailResponse:
        """
        @param request: DescribeTaskDetailRequest
        @return: DescribeTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_detail_with_options(request, runtime)

    async def describe_task_detail_async(
        self,
        request: cms_20180308_models.DescribeTaskDetailRequest,
    ) -> cms_20180308_models.DescribeTaskDetailResponse:
        """
        @param request: DescribeTaskDetailRequest
        @return: DescribeTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_detail_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: cms_20180308_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeTasksResponse:
        """
        @summary DescribeTasks
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
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
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: cms_20180308_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DescribeTasksResponse:
        """
        @summary DescribeTasks
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
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
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: cms_20180308_models.DescribeTasksRequest,
    ) -> cms_20180308_models.DescribeTasksResponse:
        """
        @summary DescribeTasks
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: cms_20180308_models.DescribeTasksRequest,
    ) -> cms_20180308_models.DescribeTasksResponse:
        """
        @summary DescribeTasks
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def disable_alarm_with_options(
        self,
        request: cms_20180308_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DisableAlarmResponse:
        """
        @summary DisableAlarm
        
        @param request: DisableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DisableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alarm_with_options_async(
        self,
        request: cms_20180308_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.DisableAlarmResponse:
        """
        @summary DisableAlarm
        
        @param request: DisableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.DisableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alarm(
        self,
        request: cms_20180308_models.DisableAlarmRequest,
    ) -> cms_20180308_models.DisableAlarmResponse:
        """
        @summary DisableAlarm
        
        @param request: DisableAlarmRequest
        @return: DisableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    async def disable_alarm_async(
        self,
        request: cms_20180308_models.DisableAlarmRequest,
    ) -> cms_20180308_models.DisableAlarmResponse:
        """
        @summary DisableAlarm
        
        @param request: DisableAlarmRequest
        @return: DisableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_alarm_with_options_async(request, runtime)

    def enable_alarm_with_options(
        self,
        request: cms_20180308_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.EnableAlarmResponse:
        """
        @summary EnableAlarm
        
        @param request: EnableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.EnableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alarm_with_options_async(
        self,
        request: cms_20180308_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.EnableAlarmResponse:
        """
        @summary EnableAlarm
        
        @param request: EnableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.EnableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alarm(
        self,
        request: cms_20180308_models.EnableAlarmRequest,
    ) -> cms_20180308_models.EnableAlarmResponse:
        """
        @summary EnableAlarm
        
        @param request: EnableAlarmRequest
        @return: EnableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    async def enable_alarm_async(
        self,
        request: cms_20180308_models.EnableAlarmRequest,
    ) -> cms_20180308_models.EnableAlarmResponse:
        """
        @summary EnableAlarm
        
        @param request: EnableAlarmRequest
        @return: EnableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_alarm_with_options_async(request, runtime)

    def get_contacts_with_options(
        self,
        request: cms_20180308_models.GetContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetContactsResponse:
        """
        @param request: GetContactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContacts',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_contacts_with_options_async(
        self,
        request: cms_20180308_models.GetContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetContactsResponse:
        """
        @param request: GetContactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContacts',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_contacts(
        self,
        request: cms_20180308_models.GetContactsRequest,
    ) -> cms_20180308_models.GetContactsResponse:
        """
        @param request: GetContactsRequest
        @return: GetContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_contacts_with_options(request, runtime)

    async def get_contacts_async(
        self,
        request: cms_20180308_models.GetContactsRequest,
    ) -> cms_20180308_models.GetContactsResponse:
        """
        @param request: GetContactsRequest
        @return: GetContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_contacts_with_options_async(request, runtime)

    def get_line_split_result_with_options(
        self,
        request: cms_20180308_models.GetLineSplitResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetLineSplitResultResponse:
        """
        @summary 获取行切分结果
        
        @param request: GetLineSplitResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLineSplitResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        if not UtilClient.is_unset(request.select_content):
            query['SelectContent'] = request.select_content
        if not UtilClient.is_unset(request.split_type):
            query['SplitType'] = request.split_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLineSplitResult',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetLineSplitResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_line_split_result_with_options_async(
        self,
        request: cms_20180308_models.GetLineSplitResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetLineSplitResultResponse:
        """
        @summary 获取行切分结果
        
        @param request: GetLineSplitResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLineSplitResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        if not UtilClient.is_unset(request.select_content):
            query['SelectContent'] = request.select_content
        if not UtilClient.is_unset(request.split_type):
            query['SplitType'] = request.split_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLineSplitResult',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetLineSplitResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_line_split_result(
        self,
        request: cms_20180308_models.GetLineSplitResultRequest,
    ) -> cms_20180308_models.GetLineSplitResultResponse:
        """
        @summary 获取行切分结果
        
        @param request: GetLineSplitResultRequest
        @return: GetLineSplitResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_line_split_result_with_options(request, runtime)

    async def get_line_split_result_async(
        self,
        request: cms_20180308_models.GetLineSplitResultRequest,
    ) -> cms_20180308_models.GetLineSplitResultResponse:
        """
        @summary 获取行切分结果
        
        @param request: GetLineSplitResultRequest
        @return: GetLineSplitResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_line_split_result_with_options_async(request, runtime)

    def get_log_column_translate_result_with_options(
        self,
        request: cms_20180308_models.GetLogColumnTranslateResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetLogColumnTranslateResultResponse:
        """
        @summary 获取日期提取结果的翻译
        
        @param request: GetLogColumnTranslateResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogColumnTranslateResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_value):
            query['ColumnValue'] = request.column_value
        if not UtilClient.is_unset(request.translate_config):
            query['TranslateConfig'] = request.translate_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogColumnTranslateResult',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetLogColumnTranslateResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_column_translate_result_with_options_async(
        self,
        request: cms_20180308_models.GetLogColumnTranslateResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetLogColumnTranslateResultResponse:
        """
        @summary 获取日期提取结果的翻译
        
        @param request: GetLogColumnTranslateResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogColumnTranslateResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_value):
            query['ColumnValue'] = request.column_value
        if not UtilClient.is_unset(request.translate_config):
            query['TranslateConfig'] = request.translate_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogColumnTranslateResult',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetLogColumnTranslateResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_column_translate_result(
        self,
        request: cms_20180308_models.GetLogColumnTranslateResultRequest,
    ) -> cms_20180308_models.GetLogColumnTranslateResultResponse:
        """
        @summary 获取日期提取结果的翻译
        
        @param request: GetLogColumnTranslateResultRequest
        @return: GetLogColumnTranslateResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_column_translate_result_with_options(request, runtime)

    async def get_log_column_translate_result_async(
        self,
        request: cms_20180308_models.GetLogColumnTranslateResultRequest,
    ) -> cms_20180308_models.GetLogColumnTranslateResultResponse:
        """
        @summary 获取日期提取结果的翻译
        
        @param request: GetLogColumnTranslateResultRequest
        @return: GetLogColumnTranslateResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_column_translate_result_with_options_async(request, runtime)

    def get_monitoring_template_with_options(
        self,
        request: cms_20180308_models.GetMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetMonitoringTemplateResponse:
        """
        @param request: GetMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetMonitoringTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitoring_template_with_options_async(
        self,
        request: cms_20180308_models.GetMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetMonitoringTemplateResponse:
        """
        @param request: GetMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetMonitoringTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitoring_template(
        self,
        request: cms_20180308_models.GetMonitoringTemplateRequest,
    ) -> cms_20180308_models.GetMonitoringTemplateResponse:
        """
        @param request: GetMonitoringTemplateRequest
        @return: GetMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_monitoring_template_with_options(request, runtime)

    async def get_monitoring_template_async(
        self,
        request: cms_20180308_models.GetMonitoringTemplateRequest,
    ) -> cms_20180308_models.GetMonitoringTemplateResponse:
        """
        @param request: GetMonitoringTemplateRequest
        @return: GetMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_monitoring_template_with_options_async(request, runtime)

    def get_my_groups_with_options(
        self,
        request: cms_20180308_models.GetMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetMyGroupsResponse:
        """
        @param request: GetMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_url):
            query['BindUrl'] = request.bind_url
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetMyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_groups_with_options_async(
        self,
        request: cms_20180308_models.GetMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.GetMyGroupsResponse:
        """
        @param request: GetMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_url):
            query['BindUrl'] = request.bind_url
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.GetMyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_groups(
        self,
        request: cms_20180308_models.GetMyGroupsRequest,
    ) -> cms_20180308_models.GetMyGroupsResponse:
        """
        @param request: GetMyGroupsRequest
        @return: GetMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_my_groups_with_options(request, runtime)

    async def get_my_groups_async(
        self,
        request: cms_20180308_models.GetMyGroupsRequest,
    ) -> cms_20180308_models.GetMyGroupsResponse:
        """
        @param request: GetMyGroupsRequest
        @return: GetMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_my_groups_with_options_async(request, runtime)

    def list_alarm_with_options(
        self,
        request: cms_20180308_models.ListAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListAlarmResponse:
        """
        @summary ListAlarm
        
        @param request: ListAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_with_options_async(
        self,
        request: cms_20180308_models.ListAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListAlarmResponse:
        """
        @summary ListAlarm
        
        @param request: ListAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm(
        self,
        request: cms_20180308_models.ListAlarmRequest,
    ) -> cms_20180308_models.ListAlarmResponse:
        """
        @summary ListAlarm
        
        @param request: ListAlarmRequest
        @return: ListAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_with_options(request, runtime)

    async def list_alarm_async(
        self,
        request: cms_20180308_models.ListAlarmRequest,
    ) -> cms_20180308_models.ListAlarmResponse:
        """
        @summary ListAlarm
        
        @param request: ListAlarmRequest
        @return: ListAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_with_options_async(request, runtime)

    def list_alarm_history_with_options(
        self,
        request: cms_20180308_models.ListAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListAlarmHistoryResponse:
        """
        @summary ListAlarmHistory
        
        @param request: ListAlarmHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmHistory',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListAlarmHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_history_with_options_async(
        self,
        request: cms_20180308_models.ListAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListAlarmHistoryResponse:
        """
        @summary ListAlarmHistory
        
        @param request: ListAlarmHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlarmHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmHistory',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListAlarmHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_history(
        self,
        request: cms_20180308_models.ListAlarmHistoryRequest,
    ) -> cms_20180308_models.ListAlarmHistoryResponse:
        """
        @summary ListAlarmHistory
        
        @param request: ListAlarmHistoryRequest
        @return: ListAlarmHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_history_with_options(request, runtime)

    async def list_alarm_history_async(
        self,
        request: cms_20180308_models.ListAlarmHistoryRequest,
    ) -> cms_20180308_models.ListAlarmHistoryResponse:
        """
        @summary ListAlarmHistory
        
        @param request: ListAlarmHistoryRequest
        @return: ListAlarmHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_history_with_options_async(request, runtime)

    def list_contact_group_with_options(
        self,
        request: cms_20180308_models.ListContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListContactGroupResponse:
        """
        @param request: ListContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactGroupResponse
        """
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
            action='ListContactGroup',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_group_with_options_async(
        self,
        request: cms_20180308_models.ListContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListContactGroupResponse:
        """
        @param request: ListContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactGroupResponse
        """
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
            action='ListContactGroup',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact_group(
        self,
        request: cms_20180308_models.ListContactGroupRequest,
    ) -> cms_20180308_models.ListContactGroupResponse:
        """
        @param request: ListContactGroupRequest
        @return: ListContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_contact_group_with_options(request, runtime)

    async def list_contact_group_async(
        self,
        request: cms_20180308_models.ListContactGroupRequest,
    ) -> cms_20180308_models.ListContactGroupResponse:
        """
        @param request: ListContactGroupRequest
        @return: ListContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_group_with_options_async(request, runtime)

    def list_event_rules_with_options(
        self,
        request: cms_20180308_models.ListEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListEventRulesResponse:
        """
        @param request: ListEventRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventRules',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_rules_with_options_async(
        self,
        request: cms_20180308_models.ListEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListEventRulesResponse:
        """
        @param request: ListEventRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventRules',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_rules(
        self,
        request: cms_20180308_models.ListEventRulesRequest,
    ) -> cms_20180308_models.ListEventRulesResponse:
        """
        @param request: ListEventRulesRequest
        @return: ListEventRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_event_rules_with_options(request, runtime)

    async def list_event_rules_async(
        self,
        request: cms_20180308_models.ListEventRulesRequest,
    ) -> cms_20180308_models.ListEventRulesResponse:
        """
        @param request: ListEventRulesRequest
        @return: ListEventRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_event_rules_with_options_async(request, runtime)

    def list_my_group_instances_with_options(
        self,
        request: cms_20180308_models.ListMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListMyGroupInstancesResponse:
        """
        @param request: ListMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupInstancesResponse
        """
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
            action='ListMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListMyGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_my_group_instances_with_options_async(
        self,
        request: cms_20180308_models.ListMyGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListMyGroupInstancesResponse:
        """
        @param request: ListMyGroupInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupInstancesResponse
        """
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
            action='ListMyGroupInstances',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListMyGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_my_group_instances(
        self,
        request: cms_20180308_models.ListMyGroupInstancesRequest,
    ) -> cms_20180308_models.ListMyGroupInstancesResponse:
        """
        @param request: ListMyGroupInstancesRequest
        @return: ListMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_my_group_instances_with_options(request, runtime)

    async def list_my_group_instances_async(
        self,
        request: cms_20180308_models.ListMyGroupInstancesRequest,
    ) -> cms_20180308_models.ListMyGroupInstancesResponse:
        """
        @param request: ListMyGroupInstancesRequest
        @return: ListMyGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_my_group_instances_with_options_async(request, runtime)

    def list_my_groups_with_options(
        self,
        request: cms_20180308_models.ListMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListMyGroupsResponse:
        """
        @param request: ListMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_urls):
            query['BindUrls'] = request.bind_urls
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListMyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_my_groups_with_options_async(
        self,
        request: cms_20180308_models.ListMyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ListMyGroupsResponse:
        """
        @param request: ListMyGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_urls):
            query['BindUrls'] = request.bind_urls
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMyGroups',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ListMyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_my_groups(
        self,
        request: cms_20180308_models.ListMyGroupsRequest,
    ) -> cms_20180308_models.ListMyGroupsResponse:
        """
        @param request: ListMyGroupsRequest
        @return: ListMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_my_groups_with_options(request, runtime)

    async def list_my_groups_async(
        self,
        request: cms_20180308_models.ListMyGroupsRequest,
    ) -> cms_20180308_models.ListMyGroupsResponse:
        """
        @param request: ListMyGroupsRequest
        @return: ListMyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_my_groups_with_options_async(request, runtime)

    def modify_task_with_options(
        self,
        request: cms_20180308_models.ModifyTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ModifyTaskResponse:
        """
        @param request: ModifyTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_rule):
            query['AlertRule'] = request.alert_rule
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_city):
            query['IspCity'] = request.isp_city
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.caller):
            query['caller'] = request.caller
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTask',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ModifyTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_task_with_options_async(
        self,
        request: cms_20180308_models.ModifyTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.ModifyTaskResponse:
        """
        @param request: ModifyTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_rule):
            query['AlertRule'] = request.alert_rule
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_city):
            query['IspCity'] = request.isp_city
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.caller):
            query['caller'] = request.caller
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTask',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.ModifyTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_task(
        self,
        request: cms_20180308_models.ModifyTaskRequest,
    ) -> cms_20180308_models.ModifyTaskResponse:
        """
        @param request: ModifyTaskRequest
        @return: ModifyTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_task_with_options(request, runtime)

    async def modify_task_async(
        self,
        request: cms_20180308_models.ModifyTaskRequest,
    ) -> cms_20180308_models.ModifyTaskResponse:
        """
        @param request: ModifyTaskRequest
        @return: ModifyTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_task_with_options_async(request, runtime)

    def node_list_with_options(
        self,
        request: cms_20180308_models.NodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeListResponse:
        """
        @summary NodeList
        
        @param request: NodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def node_list_with_options_async(
        self,
        request: cms_20180308_models.NodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeListResponse:
        """
        @summary NodeList
        
        @param request: NodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def node_list(
        self,
        request: cms_20180308_models.NodeListRequest,
    ) -> cms_20180308_models.NodeListResponse:
        """
        @summary NodeList
        
        @param request: NodeListRequest
        @return: NodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.node_list_with_options(request, runtime)

    async def node_list_async(
        self,
        request: cms_20180308_models.NodeListRequest,
    ) -> cms_20180308_models.NodeListResponse:
        """
        @summary NodeList
        
        @param request: NodeListRequest
        @return: NodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.node_list_with_options_async(request, runtime)

    def node_process_create_with_options(
        self,
        request: cms_20180308_models.NodeProcessCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeProcessCreateResponse:
        """
        @summary NodeProcessCreate
        
        @param request: NodeProcessCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeProcessCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeProcessCreate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeProcessCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def node_process_create_with_options_async(
        self,
        request: cms_20180308_models.NodeProcessCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeProcessCreateResponse:
        """
        @summary NodeProcessCreate
        
        @param request: NodeProcessCreateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeProcessCreateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeProcessCreate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeProcessCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def node_process_create(
        self,
        request: cms_20180308_models.NodeProcessCreateRequest,
    ) -> cms_20180308_models.NodeProcessCreateResponse:
        """
        @summary NodeProcessCreate
        
        @param request: NodeProcessCreateRequest
        @return: NodeProcessCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.node_process_create_with_options(request, runtime)

    async def node_process_create_async(
        self,
        request: cms_20180308_models.NodeProcessCreateRequest,
    ) -> cms_20180308_models.NodeProcessCreateResponse:
        """
        @summary NodeProcessCreate
        
        @param request: NodeProcessCreateRequest
        @return: NodeProcessCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.node_process_create_with_options_async(request, runtime)

    def node_processes_with_options(
        self,
        request: cms_20180308_models.NodeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeProcessesResponse:
        """
        @summary NodeProcesses
        
        @param request: NodeProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeProcesses',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def node_processes_with_options_async(
        self,
        request: cms_20180308_models.NodeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeProcessesResponse:
        """
        @summary NodeProcesses
        
        @param request: NodeProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeProcesses',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def node_processes(
        self,
        request: cms_20180308_models.NodeProcessesRequest,
    ) -> cms_20180308_models.NodeProcessesResponse:
        """
        @summary NodeProcesses
        
        @param request: NodeProcessesRequest
        @return: NodeProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.node_processes_with_options(request, runtime)

    async def node_processes_async(
        self,
        request: cms_20180308_models.NodeProcessesRequest,
    ) -> cms_20180308_models.NodeProcessesResponse:
        """
        @summary NodeProcesses
        
        @param request: NodeProcessesRequest
        @return: NodeProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.node_processes_with_options_async(request, runtime)

    def node_status_list_with_options(
        self,
        request: cms_20180308_models.NodeStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeStatusListResponse:
        """
        @summary NodeStatusList
        
        @param request: NodeStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeStatusList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    async def node_status_list_with_options_async(
        self,
        request: cms_20180308_models.NodeStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeStatusListResponse:
        """
        @summary NodeStatusList
        
        @param request: NodeStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeStatusList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeStatusListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def node_status_list(
        self,
        request: cms_20180308_models.NodeStatusListRequest,
    ) -> cms_20180308_models.NodeStatusListResponse:
        """
        @summary NodeStatusList
        
        @param request: NodeStatusListRequest
        @return: NodeStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.node_status_list_with_options(request, runtime)

    async def node_status_list_async(
        self,
        request: cms_20180308_models.NodeStatusListRequest,
    ) -> cms_20180308_models.NodeStatusListResponse:
        """
        @summary NodeStatusList
        
        @param request: NodeStatusListRequest
        @return: NodeStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.node_status_list_with_options_async(request, runtime)

    def node_uninstall_with_options(
        self,
        request: cms_20180308_models.NodeUninstallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeUninstallResponse:
        """
        @summary NodeUninstall
        
        @param request: NodeUninstallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeUninstallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeUninstall',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeUninstallResponse(),
            self.call_api(params, req, runtime)
        )

    async def node_uninstall_with_options_async(
        self,
        request: cms_20180308_models.NodeUninstallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.NodeUninstallResponse:
        """
        @summary NodeUninstall
        
        @param request: NodeUninstallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NodeUninstallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NodeUninstall',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.NodeUninstallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def node_uninstall(
        self,
        request: cms_20180308_models.NodeUninstallRequest,
    ) -> cms_20180308_models.NodeUninstallResponse:
        """
        @summary NodeUninstall
        
        @param request: NodeUninstallRequest
        @return: NodeUninstallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.node_uninstall_with_options(request, runtime)

    async def node_uninstall_async(
        self,
        request: cms_20180308_models.NodeUninstallRequest,
    ) -> cms_20180308_models.NodeUninstallResponse:
        """
        @summary NodeUninstall
        
        @param request: NodeUninstallRequest
        @return: NodeUninstallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.node_uninstall_with_options_async(request, runtime)

    def put_custom_metric_with_options(
        self,
        request: cms_20180308_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutCustomMetricResponse:
        """
        @summary PutCustomMetric
        
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_metric_with_options_async(
        self,
        request: cms_20180308_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutCustomMetricResponse:
        """
        @summary PutCustomMetric
        
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
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_metric(
        self,
        request: cms_20180308_models.PutCustomMetricRequest,
    ) -> cms_20180308_models.PutCustomMetricResponse:
        """
        @summary PutCustomMetric
        
        @param request: PutCustomMetricRequest
        @return: PutCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_with_options(request, runtime)

    async def put_custom_metric_async(
        self,
        request: cms_20180308_models.PutCustomMetricRequest,
    ) -> cms_20180308_models.PutCustomMetricResponse:
        """
        @summary PutCustomMetric
        
        @param request: PutCustomMetricRequest
        @return: PutCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_metric_with_options_async(request, runtime)

    def put_event_with_options(
        self,
        request: cms_20180308_models.PutEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventResponse:
        """
        @summary PutEvent
        
        @param request: PutEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEvent',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_with_options_async(
        self,
        request: cms_20180308_models.PutEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventResponse:
        """
        @summary PutEvent
        
        @param request: PutEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEvent',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event(
        self,
        request: cms_20180308_models.PutEventRequest,
    ) -> cms_20180308_models.PutEventResponse:
        """
        @summary PutEvent
        
        @param request: PutEventRequest
        @return: PutEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_event_with_options(request, runtime)

    async def put_event_async(
        self,
        request: cms_20180308_models.PutEventRequest,
    ) -> cms_20180308_models.PutEventResponse:
        """
        @summary PutEvent
        
        @param request: PutEventRequest
        @return: PutEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_event_with_options_async(request, runtime)

    def put_event_rule_with_options(
        self,
        request: cms_20180308_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventRuleResponse:
        """
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRule',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_rule_with_options_async(
        self,
        request: cms_20180308_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventRuleResponse:
        """
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRule',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_rule(
        self,
        request: cms_20180308_models.PutEventRuleRequest,
    ) -> cms_20180308_models.PutEventRuleResponse:
        """
        @param request: PutEventRuleRequest
        @return: PutEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_with_options(request, runtime)

    async def put_event_rule_async(
        self,
        request: cms_20180308_models.PutEventRuleRequest,
    ) -> cms_20180308_models.PutEventRuleResponse:
        """
        @param request: PutEventRuleRequest
        @return: PutEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_event_rule_with_options_async(request, runtime)

    def put_event_targets_with_options(
        self,
        request: cms_20180308_models.PutEventTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventTargetsResponse:
        """
        @param request: PutEventTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not UtilClient.is_unset(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not UtilClient.is_unset(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
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
            action='PutEventTargets',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_targets_with_options_async(
        self,
        request: cms_20180308_models.PutEventTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutEventTargetsResponse:
        """
        @param request: PutEventTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEventTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not UtilClient.is_unset(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not UtilClient.is_unset(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
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
            action='PutEventTargets',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutEventTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_targets(
        self,
        request: cms_20180308_models.PutEventTargetsRequest,
    ) -> cms_20180308_models.PutEventTargetsResponse:
        """
        @param request: PutEventTargetsRequest
        @return: PutEventTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_event_targets_with_options(request, runtime)

    async def put_event_targets_async(
        self,
        request: cms_20180308_models.PutEventTargetsRequest,
    ) -> cms_20180308_models.PutEventTargetsResponse:
        """
        @param request: PutEventTargetsRequest
        @return: PutEventTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_event_targets_with_options_async(request, runtime)

    def put_metric_rule_targets_with_options(
        self,
        request: cms_20180308_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutMetricRuleTargetsResponse:
        """
        @summary PutMetricRuleTargets
        
        @param request: PutMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['Actions'] = request.actions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutMetricRuleTargets',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_metric_rule_targets_with_options_async(
        self,
        request: cms_20180308_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutMetricRuleTargetsResponse:
        """
        @summary PutMetricRuleTargets
        
        @param request: PutMetricRuleTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        body = {}
        if not UtilClient.is_unset(request.actions):
            body['Actions'] = request.actions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutMetricRuleTargets',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_metric_rule_targets(
        self,
        request: cms_20180308_models.PutMetricRuleTargetsRequest,
    ) -> cms_20180308_models.PutMetricRuleTargetsResponse:
        """
        @summary PutMetricRuleTargets
        
        @param request: PutMetricRuleTargetsRequest
        @return: PutMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_metric_rule_targets_with_options(request, runtime)

    async def put_metric_rule_targets_async(
        self,
        request: cms_20180308_models.PutMetricRuleTargetsRequest,
    ) -> cms_20180308_models.PutMetricRuleTargetsResponse:
        """
        @summary PutMetricRuleTargets
        
        @param request: PutMetricRuleTargetsRequest
        @return: PutMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_metric_rule_targets_with_options_async(request, runtime)

    def put_resource_metric_rule_with_options(
        self,
        request: cms_20180308_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutResourceMetricRuleResponse:
        """
        @summary PutResourceMetricRule
        
        @param request: PutResourceMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
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
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRule',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutResourceMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_metric_rule_with_options_async(
        self,
        request: cms_20180308_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.PutResourceMetricRuleResponse:
        """
        @summary PutResourceMetricRule
        
        @param request: PutResourceMetricRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutResourceMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
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
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRule',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.PutResourceMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_metric_rule(
        self,
        request: cms_20180308_models.PutResourceMetricRuleRequest,
    ) -> cms_20180308_models.PutResourceMetricRuleResponse:
        """
        @summary PutResourceMetricRule
        
        @param request: PutResourceMetricRuleRequest
        @return: PutResourceMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rule_with_options(request, runtime)

    async def put_resource_metric_rule_async(
        self,
        request: cms_20180308_models.PutResourceMetricRuleRequest,
    ) -> cms_20180308_models.PutResourceMetricRuleResponse:
        """
        @summary PutResourceMetricRule
        
        @param request: PutResourceMetricRuleRequest
        @return: PutResourceMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_metric_rule_with_options_async(request, runtime)

    def query_custom_metric_list_with_options(
        self,
        request: cms_20180308_models.QueryCustomMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryCustomMetricListResponse:
        """
        @param request: QueryCustomMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomMetricListResponse
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomMetricList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryCustomMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_custom_metric_list_with_options_async(
        self,
        request: cms_20180308_models.QueryCustomMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryCustomMetricListResponse:
        """
        @param request: QueryCustomMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomMetricListResponse
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomMetricList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryCustomMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_custom_metric_list(
        self,
        request: cms_20180308_models.QueryCustomMetricListRequest,
    ) -> cms_20180308_models.QueryCustomMetricListResponse:
        """
        @param request: QueryCustomMetricListRequest
        @return: QueryCustomMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_custom_metric_list_with_options(request, runtime)

    async def query_custom_metric_list_async(
        self,
        request: cms_20180308_models.QueryCustomMetricListRequest,
    ) -> cms_20180308_models.QueryCustomMetricListResponse:
        """
        @param request: QueryCustomMetricListRequest
        @return: QueryCustomMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_custom_metric_list_with_options_async(request, runtime)

    def query_metric_data_with_options(
        self,
        request: cms_20180308_models.QueryMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricDataResponse:
        """
        @summary QueryMetricData
        
        @param request: QueryMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricDataResponse
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
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricData',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_data_with_options_async(
        self,
        request: cms_20180308_models.QueryMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricDataResponse:
        """
        @summary QueryMetricData
        
        @param request: QueryMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricDataResponse
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
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricData',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_data(
        self,
        request: cms_20180308_models.QueryMetricDataRequest,
    ) -> cms_20180308_models.QueryMetricDataResponse:
        """
        @summary QueryMetricData
        
        @param request: QueryMetricDataRequest
        @return: QueryMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_data_with_options(request, runtime)

    async def query_metric_data_async(
        self,
        request: cms_20180308_models.QueryMetricDataRequest,
    ) -> cms_20180308_models.QueryMetricDataResponse:
        """
        @summary QueryMetricData
        
        @param request: QueryMetricDataRequest
        @return: QueryMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_data_with_options_async(request, runtime)

    def query_metric_last_with_options(
        self,
        request: cms_20180308_models.QueryMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricLastResponse:
        """
        @param request: QueryMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricLastResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricLast',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_last_with_options_async(
        self,
        request: cms_20180308_models.QueryMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricLastResponse:
        """
        @param request: QueryMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricLastResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricLast',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_last(
        self,
        request: cms_20180308_models.QueryMetricLastRequest,
    ) -> cms_20180308_models.QueryMetricLastResponse:
        """
        @param request: QueryMetricLastRequest
        @return: QueryMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_last_with_options(request, runtime)

    async def query_metric_last_async(
        self,
        request: cms_20180308_models.QueryMetricLastRequest,
    ) -> cms_20180308_models.QueryMetricLastResponse:
        """
        @param request: QueryMetricLastRequest
        @return: QueryMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_last_with_options_async(request, runtime)

    def query_metric_list_with_options(
        self,
        request: cms_20180308_models.QueryMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricListResponse:
        """
        @param request: QueryMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_list_with_options_async(
        self,
        request: cms_20180308_models.QueryMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricListResponse:
        """
        @param request: QueryMetricListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_list(
        self,
        request: cms_20180308_models.QueryMetricListRequest,
    ) -> cms_20180308_models.QueryMetricListResponse:
        """
        @param request: QueryMetricListRequest
        @return: QueryMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_list_with_options(request, runtime)

    async def query_metric_list_async(
        self,
        request: cms_20180308_models.QueryMetricListRequest,
    ) -> cms_20180308_models.QueryMetricListResponse:
        """
        @param request: QueryMetricListRequest
        @return: QueryMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_list_with_options_async(request, runtime)

    def query_metric_meta_with_options(
        self,
        request: cms_20180308_models.QueryMetricMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricMetaResponse:
        """
        @summary 查询云监控开放的监控项详情
        
        @param request: QueryMetricMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricMeta',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_meta_with_options_async(
        self,
        request: cms_20180308_models.QueryMetricMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricMetaResponse:
        """
        @summary 查询云监控开放的监控项详情
        
        @param request: QueryMetricMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricMeta',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_meta(
        self,
        request: cms_20180308_models.QueryMetricMetaRequest,
    ) -> cms_20180308_models.QueryMetricMetaResponse:
        """
        @summary 查询云监控开放的监控项详情
        
        @param request: QueryMetricMetaRequest
        @return: QueryMetricMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_meta_with_options(request, runtime)

    async def query_metric_meta_async(
        self,
        request: cms_20180308_models.QueryMetricMetaRequest,
    ) -> cms_20180308_models.QueryMetricMetaResponse:
        """
        @summary 查询云监控开放的监控项详情
        
        @param request: QueryMetricMetaRequest
        @return: QueryMetricMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_meta_with_options_async(request, runtime)

    def query_metric_top_with_options(
        self,
        request: cms_20180308_models.QueryMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricTopResponse:
        """
        @summary QueryMetricTop
        
        @param request: QueryMetricTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricTopResponse
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
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricTop',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_top_with_options_async(
        self,
        request: cms_20180308_models.QueryMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryMetricTopResponse:
        """
        @summary QueryMetricTop
        
        @param request: QueryMetricTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMetricTopResponse
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
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricTop',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryMetricTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_top(
        self,
        request: cms_20180308_models.QueryMetricTopRequest,
    ) -> cms_20180308_models.QueryMetricTopResponse:
        """
        @summary QueryMetricTop
        
        @param request: QueryMetricTopRequest
        @return: QueryMetricTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_metric_top_with_options(request, runtime)

    async def query_metric_top_async(
        self,
        request: cms_20180308_models.QueryMetricTopRequest,
    ) -> cms_20180308_models.QueryMetricTopResponse:
        """
        @summary QueryMetricTop
        
        @param request: QueryMetricTopRequest
        @return: QueryMetricTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_top_with_options_async(request, runtime)

    def query_project_meta_with_options(
        self,
        request: cms_20180308_models.QueryProjectMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryProjectMetaResponse:
        """
        @summary 查询云监控支持的时序类监控项产品列表
        
        @param request: QueryProjectMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectMetaResponse
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
            action='QueryProjectMeta',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryProjectMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_meta_with_options_async(
        self,
        request: cms_20180308_models.QueryProjectMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryProjectMetaResponse:
        """
        @summary 查询云监控支持的时序类监控项产品列表
        
        @param request: QueryProjectMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectMetaResponse
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
            action='QueryProjectMeta',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryProjectMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project_meta(
        self,
        request: cms_20180308_models.QueryProjectMetaRequest,
    ) -> cms_20180308_models.QueryProjectMetaResponse:
        """
        @summary 查询云监控支持的时序类监控项产品列表
        
        @param request: QueryProjectMetaRequest
        @return: QueryProjectMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_project_meta_with_options(request, runtime)

    async def query_project_meta_async(
        self,
        request: cms_20180308_models.QueryProjectMetaRequest,
    ) -> cms_20180308_models.QueryProjectMetaResponse:
        """
        @summary 查询云监控支持的时序类监控项产品列表
        
        @param request: QueryProjectMetaRequest
        @return: QueryProjectMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_project_meta_with_options_async(request, runtime)

    def query_statics_availability_with_options(
        self,
        request: cms_20180308_models.QueryStaticsAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryStaticsAvailabilityResponse:
        """
        @param request: QueryStaticsAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStaticsAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStaticsAvailability',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryStaticsAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statics_availability_with_options_async(
        self,
        request: cms_20180308_models.QueryStaticsAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryStaticsAvailabilityResponse:
        """
        @param request: QueryStaticsAvailabilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStaticsAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStaticsAvailability',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryStaticsAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statics_availability(
        self,
        request: cms_20180308_models.QueryStaticsAvailabilityRequest,
    ) -> cms_20180308_models.QueryStaticsAvailabilityResponse:
        """
        @param request: QueryStaticsAvailabilityRequest
        @return: QueryStaticsAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_statics_availability_with_options(request, runtime)

    async def query_statics_availability_async(
        self,
        request: cms_20180308_models.QueryStaticsAvailabilityRequest,
    ) -> cms_20180308_models.QueryStaticsAvailabilityResponse:
        """
        @param request: QueryStaticsAvailabilityRequest
        @return: QueryStaticsAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_statics_availability_with_options_async(request, runtime)

    def query_statics_response_time_with_options(
        self,
        request: cms_20180308_models.QueryStaticsResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryStaticsResponseTimeResponse:
        """
        @param request: QueryStaticsResponseTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStaticsResponseTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStaticsResponseTime',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryStaticsResponseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statics_response_time_with_options_async(
        self,
        request: cms_20180308_models.QueryStaticsResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryStaticsResponseTimeResponse:
        """
        @param request: QueryStaticsResponseTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStaticsResponseTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStaticsResponseTime',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryStaticsResponseTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statics_response_time(
        self,
        request: cms_20180308_models.QueryStaticsResponseTimeRequest,
    ) -> cms_20180308_models.QueryStaticsResponseTimeResponse:
        """
        @param request: QueryStaticsResponseTimeRequest
        @return: QueryStaticsResponseTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_statics_response_time_with_options(request, runtime)

    async def query_statics_response_time_async(
        self,
        request: cms_20180308_models.QueryStaticsResponseTimeRequest,
    ) -> cms_20180308_models.QueryStaticsResponseTimeResponse:
        """
        @param request: QueryStaticsResponseTimeRequest
        @return: QueryStaticsResponseTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_statics_response_time_with_options_async(request, runtime)

    def query_system_event_count_with_options(
        self,
        request: cms_20180308_models.QuerySystemEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QuerySystemEventCountResponse:
        """
        @summary QuerySystemEventCount
        
        @param request: QuerySystemEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySystemEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_json):
            query['QueryJson'] = request.query_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEventCount',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QuerySystemEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_system_event_count_with_options_async(
        self,
        request: cms_20180308_models.QuerySystemEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QuerySystemEventCountResponse:
        """
        @summary QuerySystemEventCount
        
        @param request: QuerySystemEventCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySystemEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_json):
            query['QueryJson'] = request.query_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEventCount',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QuerySystemEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_system_event_count(
        self,
        request: cms_20180308_models.QuerySystemEventCountRequest,
    ) -> cms_20180308_models.QuerySystemEventCountResponse:
        """
        @summary QuerySystemEventCount
        
        @param request: QuerySystemEventCountRequest
        @return: QuerySystemEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_system_event_count_with_options(request, runtime)

    async def query_system_event_count_async(
        self,
        request: cms_20180308_models.QuerySystemEventCountRequest,
    ) -> cms_20180308_models.QuerySystemEventCountResponse:
        """
        @summary QuerySystemEventCount
        
        @param request: QuerySystemEventCountRequest
        @return: QuerySystemEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_system_event_count_with_options_async(request, runtime)

    def query_system_event_demo_with_options(
        self,
        request: cms_20180308_models.QuerySystemEventDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QuerySystemEventDemoResponse:
        """
        @param request: QuerySystemEventDemoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySystemEventDemoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEventDemo',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QuerySystemEventDemoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_system_event_demo_with_options_async(
        self,
        request: cms_20180308_models.QuerySystemEventDemoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QuerySystemEventDemoResponse:
        """
        @param request: QuerySystemEventDemoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySystemEventDemoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEventDemo',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QuerySystemEventDemoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_system_event_demo(
        self,
        request: cms_20180308_models.QuerySystemEventDemoRequest,
    ) -> cms_20180308_models.QuerySystemEventDemoResponse:
        """
        @param request: QuerySystemEventDemoRequest
        @return: QuerySystemEventDemoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_system_event_demo_with_options(request, runtime)

    async def query_system_event_demo_async(
        self,
        request: cms_20180308_models.QuerySystemEventDemoRequest,
    ) -> cms_20180308_models.QuerySystemEventDemoResponse:
        """
        @param request: QuerySystemEventDemoRequest
        @return: QuerySystemEventDemoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_system_event_demo_with_options_async(request, runtime)

    def query_task_config_with_options(
        self,
        request: cms_20180308_models.QueryTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryTaskConfigResponse:
        """
        @param request: QueryTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryTaskConfig',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_config_with_options_async(
        self,
        request: cms_20180308_models.QueryTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryTaskConfigResponse:
        """
        @param request: QueryTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryTaskConfig',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_config(
        self,
        request: cms_20180308_models.QueryTaskConfigRequest,
    ) -> cms_20180308_models.QueryTaskConfigResponse:
        """
        @param request: QueryTaskConfigRequest
        @return: QueryTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_config_with_options(request, runtime)

    async def query_task_config_async(
        self,
        request: cms_20180308_models.QueryTaskConfigRequest,
    ) -> cms_20180308_models.QueryTaskConfigResponse:
        """
        @param request: QueryTaskConfigRequest
        @return: QueryTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_config_with_options_async(request, runtime)

    def query_task_monitor_data_with_options(
        self,
        request: cms_20180308_models.QueryTaskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryTaskMonitorDataResponse:
        """
        @summary QueryTaskMonitorData
        
        @param request: QueryTaskMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskMonitorDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.metric_name):
            query['metricName'] = request.metric_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskMonitorData',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryTaskMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_monitor_data_with_options_async(
        self,
        request: cms_20180308_models.QueryTaskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.QueryTaskMonitorDataResponse:
        """
        @summary QueryTaskMonitorData
        
        @param request: QueryTaskMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskMonitorDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.metric_name):
            query['metricName'] = request.metric_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskMonitorData',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.QueryTaskMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_monitor_data(
        self,
        request: cms_20180308_models.QueryTaskMonitorDataRequest,
    ) -> cms_20180308_models.QueryTaskMonitorDataResponse:
        """
        @summary QueryTaskMonitorData
        
        @param request: QueryTaskMonitorDataRequest
        @return: QueryTaskMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_monitor_data_with_options(request, runtime)

    async def query_task_monitor_data_async(
        self,
        request: cms_20180308_models.QueryTaskMonitorDataRequest,
    ) -> cms_20180308_models.QueryTaskMonitorDataResponse:
        """
        @summary QueryTaskMonitorData
        
        @param request: QueryTaskMonitorDataRequest
        @return: QueryTaskMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_monitor_data_with_options_async(request, runtime)

    def task_config_list_with_options(
        self,
        request: cms_20180308_models.TaskConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.TaskConfigListResponse:
        """
        @param request: TaskConfigListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TaskConfigListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='TaskConfigList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.TaskConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def task_config_list_with_options_async(
        self,
        request: cms_20180308_models.TaskConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.TaskConfigListResponse:
        """
        @param request: TaskConfigListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TaskConfigListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='TaskConfigList',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.TaskConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def task_config_list(
        self,
        request: cms_20180308_models.TaskConfigListRequest,
    ) -> cms_20180308_models.TaskConfigListResponse:
        """
        @param request: TaskConfigListRequest
        @return: TaskConfigListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.task_config_list_with_options(request, runtime)

    async def task_config_list_async(
        self,
        request: cms_20180308_models.TaskConfigListRequest,
    ) -> cms_20180308_models.TaskConfigListResponse:
        """
        @param request: TaskConfigListRequest
        @return: TaskConfigListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.task_config_list_with_options_async(request, runtime)

    def update_alarm_with_options(
        self,
        request: cms_20180308_models.UpdateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.UpdateAlarmResponse:
        """
        @summary UpdateAlarm
        
        @param request: UpdateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='UpdateAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.UpdateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alarm_with_options_async(
        self,
        request: cms_20180308_models.UpdateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.UpdateAlarmResponse:
        """
        @summary UpdateAlarm
        
        @param request: UpdateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
            action='UpdateAlarm',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.UpdateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alarm(
        self,
        request: cms_20180308_models.UpdateAlarmRequest,
    ) -> cms_20180308_models.UpdateAlarmResponse:
        """
        @summary UpdateAlarm
        
        @param request: UpdateAlarmRequest
        @return: UpdateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alarm_with_options(request, runtime)

    async def update_alarm_async(
        self,
        request: cms_20180308_models.UpdateAlarmRequest,
    ) -> cms_20180308_models.UpdateAlarmResponse:
        """
        @summary UpdateAlarm
        
        @param request: UpdateAlarmRequest
        @return: UpdateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_alarm_with_options_async(request, runtime)

    def update_monitoring_template_with_options(
        self,
        request: cms_20180308_models.UpdateMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.UpdateMonitoringTemplateResponse:
        """
        @param request: UpdateMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates_json):
            query['AlertTemplatesJson'] = request.alert_templates_json
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host_availability_template):
            query['HostAvailabilityTemplate'] = request.host_availability_template
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.process_monitor_templates):
            query['ProcessMonitorTemplates'] = request.process_monitor_templates
        if not UtilClient.is_unset(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not UtilClient.is_unset(request.system_event_templates):
            query['SystemEventTemplates'] = request.system_event_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.UpdateMonitoringTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitoring_template_with_options_async(
        self,
        request: cms_20180308_models.UpdateMonitoringTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20180308_models.UpdateMonitoringTemplateResponse:
        """
        @param request: UpdateMonitoringTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMonitoringTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates_json):
            query['AlertTemplatesJson'] = request.alert_templates_json
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host_availability_template):
            query['HostAvailabilityTemplate'] = request.host_availability_template
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.process_monitor_templates):
            query['ProcessMonitorTemplates'] = request.process_monitor_templates
        if not UtilClient.is_unset(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not UtilClient.is_unset(request.system_event_templates):
            query['SystemEventTemplates'] = request.system_event_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMonitoringTemplate',
            version='2018-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20180308_models.UpdateMonitoringTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitoring_template(
        self,
        request: cms_20180308_models.UpdateMonitoringTemplateRequest,
    ) -> cms_20180308_models.UpdateMonitoringTemplateResponse:
        """
        @param request: UpdateMonitoringTemplateRequest
        @return: UpdateMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_monitoring_template_with_options(request, runtime)

    async def update_monitoring_template_async(
        self,
        request: cms_20180308_models.UpdateMonitoringTemplateRequest,
    ) -> cms_20180308_models.UpdateMonitoringTemplateResponse:
        """
        @param request: UpdateMonitoringTemplateRequest
        @return: UpdateMonitoringTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_monitoring_template_with_options_async(request, runtime)
